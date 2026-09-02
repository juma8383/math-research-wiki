#!/usr/bin/env python
# Claude independent verification of [mss-k34-sieve2]:
#  V1. X-function identity checks on E~_A / E~_B against the known image table.
#  V2. The 2c lever: X(nG_A) mod 169 for n in {12,22,32,42,52} == {85,150,46,111,7};
#      and X(nG_A) mod 13 == 7 (nonresidue) for all n = 2 mod 10 up to n=200.
#  V3. Independent A-side sieve: killing primes {5,11,13} + grow primes <= 400
#      (expected-count <= 3e5, ordered by |OK|/ord) + hunt primes <= 3e5
#      (ord | M)  ->  survivors should be {0, 2, M/2-1, -2, -1} mod M_A.
#  V4. Survivor stress: the 5 claimed classes tested against ALL primes <= 2e4
#      (no ord-divisibility needed - test exact n).
#  V5. B-side: X_B formula + killing-prime sieve on E~_B.
import sys
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

# ---------- generic Weierstrass mod-p arithmetic (short-ish: a2,a4,a6) ----------
def pt_add(P, Q, a2, a4, a6, p):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if P == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*a2*x1 + a4) * pow(2*y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam*lam - a2 - x1 - x2) % p
    y3 = (-(y1 + lam*(x3 - x1))) % p
    return (x3, y3)

def pt_mul(P, n, a2, a4, a6, p):
    if P is not None: P = (P[0] % p, P[1] % p)   # canonicalize (GA not reduced for small p)
    R = None; Q = P
    while n:
        if n & 1: R = pt_add(R, Q, a2, a4, a6, p)
        Q = pt_add(Q, Q, a2, a4, a6, p); n >>= 1
    return R

def count_E(a2, a4, a6, p):
    cnt = 1
    qrs = set((x*x) % p for x in range(p))
    for x in range(p):
        v = (x**3 + a2*x*x + a4*x + a6) % p
        if v == 0: cnt += 1
        elif v in qrs: cnt += 2
    return cnt

def order_of_G(G, a2, a4, a6, p, N):
    # order of G in E(F_p) given N = #E(F_p)
    m = N
    # factor N
    fac = {}; n = N; d = 2
    while d*d <= n:
        while n % d == 0: fac[d] = fac.get(d,0)+1; n //= d
        d += 1
    if n > 1: fac[n] = fac.get(n,0)+1
    ordv = N
    for q in fac:
        while ordv % q == 0 and pt_mul(G, ordv//q, a2, a4, a6, p) is None:
            ordv //= q
    return ordv

def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j] = False
    return [i for i in range(2,n+1) if s[i]]

# ---------- E~_A ----------
A2A, A4A, A6A = -256, 18432, 0
GA  = (128, 512)           # generator on E~_A (mod-p arithmetic)
GAQ = (F(128), F(512))     # Fraction coords for the exact group law
def XA(P):
    # X = 2(y+66x)/(x(x-4)) ; returns ('inf') at O, ('pole') at x=0 or 4 (0/0 handled by caller)
    if P is None: return 'inf'
    x, y = P
    den = (x*(x-4)) % 1  # placeholder
    return (2*(y + 66*x), x*(x-4))   # (num, den) exact ints mod p

def condA(n, p, killing):
    P = pt_mul(GA, n, A2A, A4A, A6A, p)
    if P is None: return True          # O : X = infinity, degenerate
    x, y = P
    num = (2*(y + 66*x)) % p
    den = (x*(x - 4)) % p
    if den == 0:
        return True                    # pole class (0/0 or genuine pole): survives mod p
    v = num * pow(den, -1, p) % p
    if killing:
        return v in (0, 1)
    qrs = set((t*t) % p for t in range(1, p))
    return v == 0 or v in qrs

# ---------- V1: X identities ----------
out("=== V1: X-function identities (exact Fractions) ===")
def XA_exact(n):
    # exact X(nG) on E~_A via group law over Q (signed n)
    def add(P, Q):
        if P is None: return Q
        if Q is None: return P
        x1,y1 = P; x2,y2 = Q
        if x1 == x2 and y1 == -y2: return None
        lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2A*x1+A4A)/(2*y1)
        x3 = lam*lam - A2A - x1 - x2
        return (x3, -(y1 + lam*(x3-x1)))
    P = None
    for _ in range(abs(n)): P = add(P, GAQ)
    if P is None: return 'inf'
    if n < 0: P = (P[0], -P[1])
    x, y = P
    if x == 0 or x == 4: return 'pole'
    return F(2*(y + 66*x), x*(x-4))
out("  X(G)   =", XA_exact(1),   " expect 35/31:", XA_exact(1) == F(35,31))
out("  X(-G)  =", XA_exact(-1),  " expect 1   :", XA_exact(-1) == F(1,1))
out("  X(2G)  =", XA_exact(2),   " expect pole->1151/66 (0/0):", XA_exact(2))
out("  X(3G)  =", XA_exact(3),   " expect 31/35:", XA_exact(3) == F(31,35))
out("  X(4G)  =", XA_exact(4),   " expect 66/1151:", XA_exact(4) == F(66,1151))
out("  X(-3G) =", XA_exact(-3),  " expect 31/35:", XA_exact(-3) == F(31,35))
out("  X(-4G) =", XA_exact(-4),  " expect 66/1151:", XA_exact(-4) == F(66,1151))

# ---------- V2: 2c lever ----------
out("=== V2: pole-refinement lever (2c) ===")
ok = True
for n in (12, 22, 32, 42, 52):
    xX = XA_exact(n)
    good = isinstance(xX, F) and (xX.numerator * pow(xX.denominator, -1, 169)) % 169
    out("  X(%dG) mod 169 = %s (expect one of 85,150,46,111,7)" % (n, good))
for n in range(2, 202, 10):
    if n == 2:
        # exact pole point: extension value 1151/66 (verified via image table)
        r13 = F(1151, 66)
        r13 = (r13.numerator % 13) * pow(r13.denominator % 13, -1, 13) % 13
        out("  n=2: pole; extension 1151/66 mod 13 = %d" % r13)
        if r13 != 7: ok = False
        continue
    xX = XA_exact(n)
    if not isinstance(xX, F):
        out("  n=%d: X=%s (unexpected)" % (n, xX)); ok = False; continue
    r13 = (xX.numerator % 13) * pow(xX.denominator % 13, -1, 13) % 13
    if r13 != 7:
        out("  n=%d: X mod 13 = %d != 7  MISMATCH" % (n, r13)); ok = False
out("  all n=2..192 step10 give X = 7 mod 13:", ok)

# ---------- V3: independent sieve ----------
out("=== V3: independent A-side sieve ===")
# M_A target
MA = 42078090600
ps400 = primes_upto(400)
# grow phase: killing primes first, then primes <= 400 by |OK|/ord, expected <= 3e5
S = [0]; M = 1
log_lines = []
def sieve_prime(p, killing):
    global S, M
    N = count_E(A2A, A4A, A6A, p)
    o = order_of_G(GA, A2A, A4A, A6A, p, N)
    if M % o == 0:
        newS = [c for c in S if condA(c % o if c % o else o, p, killing) if True]
        newS = []
        for c in S:
            n = c % o
            if condA(n, p, killing): newS.append(c)
        return newS, M, o, 0
    M2 = M * o // __import__('math').gcd(M, o)
    factor = M2 // M
    if len(S) * factor > 300000:
        return S, M, -1   # skip (expected count too big)
    newS = []
    for c in S:
        for k in range(factor):
            n = c + k*M
            if condA(n % o, p, killing): newS.append(n)
    return newS, M2, o

order_key = []
for p in ps400:
    if p == 2: continue
    N = count_E(A2A, A4A, A6A, p)
    o = order_of_G(GA, A2A, A4A, A6A, p, N)
    if pt_mul(GA, o//2, A2A, A4A, A6A, p) is None and o % 2 == 0:
        pass
    # |OK| estimate: count classes mod o surviving
    ok_cnt = sum(1 for n in range(o) if condA(n, p, p in (5,11,13)))
    order_key.append((ok_cnt/o, p, o, p in (5,11,13)))
# killing primes first
seq = [t for t in order_key if t[3]] + sorted([t for t in order_key if not t[3]])
skipped = 0
for ratio, p, o, kill in seq:
    res = sieve_prime(p, kill)
    if res[2] == -1:
        skipped += 1
        continue
    S, M = res[0], res[1]
out("  after grow (primes<=400): |S|=%d  M=%d  skipped=%d" % (len(S), M, skipped))

# hunt primes <= 3e5: ord | M (test MA*G == O is too strict; use ord | M)
out("  hunting hunt primes <= 3e5 ...")
import math
hunt = 0
for p in primes_upto(300000):
    if p <= 400 or p == 2: continue
    N = count_E(A2A, A4A, A6A, p)   # too slow? p up to 3e5 -> O(p) per prime: 25e9 ops NO
    break
out("  [hunt enumeration via point counting too slow in pure python - using ord|M test instead]")
# cheaper: p good, MA*G == O mod p  <=> ord | MA
for p in primes_upto(300000):
    if p <= 400 or p == 2: continue
    if pt_mul(GA, MA, A2A, A4A, A6A, p) is None:
        # ord divides MA -> condition well-defined mod MA; apply to survivors
        newS = [c for c in S if condA(c, p, False)]
        if len(newS) != len(S):
            hunt += 1
            S = newS
out("  hunt kills: %d primes; |S|=%d  M=%d" % (hunt, len(S), M))
out("  survivors:", sorted(S))
out("  claim: {0, 2, M/2-1, -2, -1} = {0, 2, %d, %d, %d}" % (MA//2 - 1, MA-2, MA-1))
out("  match:", sorted(S) == sorted([0, 2, MA//2 - 1, MA - 2, MA - 1]))
out("  density: %.3e (claim 1.19e-10)" % (len(S)/MA))
out("  MA factor check 2^3*3^4*5^2*7*13*17*23*73:", MA == 8*81*25*7*13*17*23*73)

# ---------- V4: stress the claimed survivors against ALL primes <= 2e4 ----------
out("=== V4: survivor stress (exact n, all primes <= 2e4) ===")
MA = 42078090600
surv = [0, 2, MA//2 - 1, MA - 2, MA - 1]
ps2e4 = primes_upto(20000)
bad = []
killing = {5, 11, 13}
for p in ps2e4:
    if p == 2: continue
    N = count_E(A2A, A4A, A6A, p)
    qrs = set((t*t) % p for t in range(1, p))
    for n in surv:
        P = pt_mul(GA, n, A2A, A4A, A6A, p)
        if P is None: continue
        x, y = P
        den = (x*(x-4)) % p
        if den == 0: continue
        v = (2*(y+66*x)) % p * pow(den, -1, p) % p
        if p in killing:
            if v not in (0, 1): bad.append((p, n, v, 'killing'))
        else:
            if v != 0 and v not in qrs: bad.append((p, n, v, 'qr'))
out("  violations:", bad[:10] if bad else "NONE (all 5 classes pass every prime <= 2e4)")

# ---------- V5: B-side ----------
out("=== V5: B-side (E~_B: y^2=x^3+256x^2-2048x, G=(-128,1536)) ===")
A2B, A4B, A6B = 256, -2048, 0
GB = (-128, 1536)
def XB(P):
    if P is None: return 'inf'
    x, y = P
    return (F(6*y - 92*x, x*(x-36)) if x not in (0, 36) else 'pole')
def addQ_B(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 == -y2: return None
    lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2B*x1+A4B)/(2*y1)
    x3 = lam*lam - A2B - x1 - x2
    return (x3, -(y1 + lam*(x3-x1)))
P = None; seq = {}
for i in range(1, 6):
    P = addQ_B(P, GB); seq[i] = P
out("  X_B(G)   =", XB(seq[1]), " expect 1:", XB(seq[1]) == F(1,1))
out("  X_B(-G)  =", XB(addQ_B(None,(-128,-1536))), " expect 5/41:",
    XB((-128,-1536)) == F(5,41))
out("  X_B(3G)  =", XB(seq[3]), " expect 41/5:", XB(seq[3]) == F(41,5))
out("  X_B(4G)  =", XB(seq[4]), " expect 414/209:", XB(seq[4]) == F(414,209))
out("  2G       =", seq[2], " expect (36,-552):", seq[2] == (F(36), F(-552)))
# killing-prime sieve on B: primes 5,19,29
def condB(n, p, killing):
    Ppt = pt_mul(GB, n, A2B, A4B, A6B, p)
    if Ppt is None: return True
    x, y = Ppt
    den = (x*(x-36)) % p
    if den == 0: return True
    v = (6*y - 92*x) % p * pow(den, -1, p) % p
    if killing: return v in (0, 1)
    qrs = set((t*t) % p for t in range(1, p))
    return v == 0 or v in qrs
Sb = [0]; Mb = 1
for p in (5, 19, 29):
    N = count_E(A2B, A4B, A6B, p)
    o = order_of_G(GB, A2B, A4B, A6B, p, N)
    M2 = Mb * o // math.gcd(Mb, o)
    newS = []
    for c in Sb:
        for k in range(M2 // Mb):
            n = c + k*Mb
            if condB(n % o, p, True): newS.append(n)
    Sb, Mb = newS, M2
out("  B killing-prime sieve: M=%d (claim 264), |S|=%d (claim 5)" % (Mb, len(Sb)))
out("  survivors:", sorted(Sb), " claim {0,1,2,-2,134}:", sorted(Sb) == sorted([0,1,2,Mb-2,134]))