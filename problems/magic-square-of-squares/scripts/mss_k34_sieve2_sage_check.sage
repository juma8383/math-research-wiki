# mss_k34_sieve2_sage_check.sage -- SageMath 10.9 independent re-verification
# of [mss-k34-sieve2] (A-side). hermes-win, 2026-09-08.
# NOTE: ad-hoc probes written earlier this session used the WRONG map numerator
# 2y+66x instead of the filed 2(y+66x) = 2y+132x (notes.md ~line 964:
# X = 2(y+66x)/(x(x-4)); mss_k34_sieve2_claude_check.py line 79). Their
# apparent kills of the M/2-1 class were spurious. The identity X(G) = 35/31
# (V1 below) validates the correct map.
# Sections:
#   V1 exact X identities on ~E_A: y^2 = x^3 - 256x^2 + 18432x, G = (128,512)
#   V2 pole-extension lever: X(2G) = 1151/66 (0/0), mod 13 == 7 (nonresidue)
#   C  independent sieve re-run: killing {5,11,13} + grow <= 400
#      + hunt <= 5e4 (ord | M) -> survivors should be {0, 2, M/2-1, -2, -1}
#   D  survivor stress: exact n against ALL primes <= 2e4
import sys
def out(*a):
    print(*a); sys.stdout.flush()

MA = 42078090600
KILL = [5, 11, 13]
EA = EllipticCurve([0, -256, 0, 18432, 0])

def ctx(p):
    Ep = EllipticCurve(GF(p), [0, -256, 0, 18432, 0])
    Gp = Ep(128, 512)
    o = Gp.order()
    K = p in KILL
    sq = set(GF(p)(i)^2 for i in range(1, p)) if not K else None
    return (Gp, o, K, sq)

def keep(n, c4):
    Gp, o, K, sq = c4
    P = (n % o) * Gp
    if P.is_zero(): return True          # O: X = infinity, degenerate
    xP, yP = P[0], P[1]
    if xP == 0 or xP == 4: return True   # pole class (survives mod p; 2c lever handles)
    v = (2*(yP + 66*xP)) / (xP*(xP - 4))
    if K: return v in (0, 1)
    return v == 0 or v in sq

def Xexact(P):
    if P.is_zero(): return 'O'
    xP, yP = P[0], P[1]
    if xP == 0 or xP == 4: return 'pole'
    return QQ(2*(yP + 66*xP)) / QQ(xP*(xP - 4))

out('=== V1: exact X identities on ~E_A (correct map) ===')
GQ = EA(128, 512)
for n, exp in [(1, '35/31'), (-1, '1'), (3, '31/35'), (4, '66/1151')]:
    got = Xexact(n * GQ)
    out('  X(%d*G) = %s  expect %s : %s' % (n, got, exp, str(got) == exp))
out('  X(2*G) = %s  expect pole : %s' % (Xexact(2*GQ), Xexact(2*GQ) == 'pole'))

out('=== V2: pole-extension lever (2c) ===')
r13 = (1151 * inverse_mod(66, 13)) % 13
out('  1151/66 mod 13 = %d (expect 7 nonresidue): %s' % (r13, r13 == 7))
ok = True
for n in range(2, 202, 10):
    got = Xexact(n * GQ)
    if got == 'pole':
        if n != 2:
            ok = False
            out('  unexpected pole at n=%d' % n)
        continue
    v13 = (ZZ(got.numerator()) % 13) * inverse_mod(ZZ(got.denominator()) % 13, 13) % 13
    if v13 != 7:
        ok = False
        out('  n=%d: X mod 13 = %d != 7  MISMATCH' % (n, v13))
out('  all n = 2 mod 10 in [2,192] give X = 7 mod 13: %s' % ok)

out('=== C: independent sieve re-run ===')
S = [0]; M = 1; skipped = 0
for p in KILL:
    c4 = ctx(p); o = c4[1]
    M2 = lcm(M, o); f = M2 // M
    newS = []
    for c in S:
        for k in range(f):
            n = c + k*M
            if keep(n, c4): newS.append(n)
    S, M = newS, M2
    out('  killing p=%d: ord=%d |S|=%d M=%d' % (p, o, len(S), M))
# grow primes <= 400 ordered by ok-ratio
def ok_ratio(p):
    c4 = ctx(p); o = c4[1]
    okc = sum(1 for n in range(o) if keep(n, c4))
    return (QQ(okc)/QQ(o), p, o)
grow = sorted(ok_ratio(p) for p in prime_range(5, 401) if p not in KILL)
for ratio, p, o in grow:
    c4 = ctx(p)
    if M % o == 0:
        S = [c for c in S if keep(c, c4)]
    else:
        M2 = lcm(M, o); f = M2 // M
        if len(S) * f > 300000:
            skipped += 1
            continue
        newS = []
        for c in S:
            for k in range(f):
                n = c + k*M
                if keep(n, c4): newS.append(n)
        S, M = newS, M2
out('  after grow: |S|=%d M=%d skipped=%d  (claim M=MA=%d: %s)'
    % (len(S), M, skipped, MA, M == MA))
hunt = 0
for p in prime_range(401, 50000):
    c4 = ctx(p); o = c4[1]
    if MA % o == 0 and M % o == 0:
        S2 = [c for c in S if keep(c, c4)]
        if len(S2) != len(S):
            hunt += 1
            S = S2
out('  hunt kills: %d primes; |S|=%d M=%d' % (hunt, len(S), M))
claim = sorted([0, 2, MA//2 - 1, MA - 2, MA - 1])
out('  survivors: %s' % sorted(S))
out('  matches claim {0, 2, M/2-1, -2, -1}: %s' % (sorted(S) == claim))
out('  density: %.3e (claim 1.19e-10)' % (float(len(S))/float(MA)))

out('=== D: survivor stress, exact n, ALL primes <= 2e4 ===')
bad = []
for p in prime_range(3, 20001):
    if p in (2, 3):
        continue            # p=2,3 bad primes: ~E_A is singular (disc divisible by 2,3)
    c4 = ctx(p)
    for n in claim:
        if not keep(n, c4):
            bad.append((p, n))
            break
out('  violations: %s' % (bad[:10] if bad else 'NONE (all 5 classes pass every prime <= 2e4)'))
out('=== DONE ===')