# mss_k34_sieve2_sage_check2.sage -- decisive follow-ups (2026-09-08, hermes-win)
#  E1: X(-3G), X(-4G) exact (sign-symmetry check of the image table)
#  E2: ord_p(G) for the 10 V4 "violation" primes -> expect ord ∤ M_A (spurious)
#  E3: FILTERED stress: the 5 filed classes mod M_A vs all good primes
#      p <= 3e4 with ord_p(G) | M_A -> expect ZERO violations (reproduces §6ii)
#  E4: factor M' = 23736358800 (my re-run modulus) vs M_A
def out(*a):
    print(*a); sys.stdout.flush()

MA = 42078090600
KILL = [5, 11, 13]
EA = EllipticCurve([0, -256, 0, 18432, 0])
GQ = EA(128, 512)

def Xexact(P):
    if P.is_zero(): return 'O'
    xP, yP = P[0], P[1]
    if xP == 0 or xP == 4: return 'pole'
    return QQ(2*(yP + 66*xP)) / QQ(xP*(xP - 4))

out('=== E1: exact X on negative multiples ===')
for n in (3, 4):
    out('  X(-%d*G) = %s' % (n, Xexact((-n) * GQ)))

out('=== E2: ord_p(G) at the V4 violation primes ===')
for p in [23, 71, 83, 109, 113, 127, 137, 173, 181, 191]:
    Ep = EllipticCurve(GF(p), [0, -256, 0, 18432, 0])
    o = Ep(128, 512).order()
    out('  p=%d: ord=%d, ord|M_A: %s' % (p, o, MA % o == 0))

out('=== E3: FILTERED stress (ord | M_A), primes <= 3e4 ===')
claim = [0, 2, MA//2 - 1, MA - 2, MA - 1]
nvalid = 0
bad = []
for p in prime_range(5, 30001):
    Ep = EllipticCurve(GF(p), [0, -256, 0, 18432, 0])
    Gp = Ep(128, 512)
    o = Gp.order()
    if MA % o != 0:
        continue
    nvalid += 1
    K = p in KILL
    sq = set(GF(p)(i)^2 for i in range(1, p))
    for c in claim:
        P = (c % o) * Gp
        if P.is_zero():
            continue
        xP, yP = P[0], P[1]
        if xP == 0 or xP == 4:
            continue
        v = (2*(yP + 66*xP)) / (xP*(xP - 4))
        ok = (v in (0, 1)) if K else (v == 0 or v in sq)
        if not ok:
            bad.append((p, c))
            break
out('  valid primes: %d ; violations: %s' % (nvalid, bad if bad else 'NONE'))

out('=== E4: my re-run modulus ===')
out('  M\' = 23736358800 =', factor(23736358800))
out('  M_A =', factor(MA))
out('=== DONE ===')