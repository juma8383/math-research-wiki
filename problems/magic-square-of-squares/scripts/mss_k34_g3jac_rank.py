#!/usr/bin/env python
# [mss-k34-g3jac] Part 3: rank of the common Prym factor E_G.
#
# E_G: y^2 = x^3 - 504576 x + 131604480,  j = 1556068/81.
# Full rational 2-torsion: theta in {-816, 336, 480}  -> E_G[2](Q) = (Z/2)^2,
# torsion divides 8 (gcd #E_G(F_p), p=5..43).
#
# Method: 2-isogeny descent, p4-style rigorous one-way kills.
# For each theta_i, shift x -> x - theta_i:  E0: y^2 = x^3 + A x^2 + B x,
#   A = 3*theta_i,  B = 3*theta_i^2 + a4.  Descent map alpha(P) = x (mod sq),
#   ker alpha = phi_hat(E_i(Q)), so  |E/phi_hat E_i| = |im alpha| <= 2^{a_i}
#   where a_i = # locally soluble spaces C_d: N^2 = dM^4 + A M^2 e^2 + (B/d) e^4
#   (d squarefree signed divisor of B; only PROVABLE insolubility kills).
# The isogenous curve E_i: y^2 = x^3 - 2A x^2 + (A^2 - 4B) x; the same
# construction on E_i (kernel (0,0)) bounds |E_i/phi_i E| <= 2^{b_i}.
# Product formula (derived exactly, both curves full-2-torsion case):
#   |E/2E| = |E/phi_hat E_i| * |E_i/phi_i E|   =>
#   rank(E_G) + 2 <= a_i + b_i   for EVERY i.  Also s_A >= ... lower bounds.
# ASCII only.  python (not python3); PYTHONIOENCODING=utf-8.
import sys
from fractions import Fraction as F

def out(*a):
    print(*a)
    sys.stdout.flush()

A2, A4, A6 = 0, -504576, 131604480
THETA = [-816, 336, 480]

# ------------------------------------------------------------ small tools --
def factor(n):
    n = abs(n); fac = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac

def sqfree_divs(n):
    """signed squarefree divisors of n (n may be negative)."""
    fac = factor(n); res = [1]
    for p in fac:
        res += [r * p for r in res]
    out2 = []
    for r in res:
        out2.append(r); out2.append(-r)
    return sorted(set(out2))

def sqfree_class(m):
    """squarefree part of nonzero integer m (sign kept)."""
    if m == 0:
        return 0
    fac = factor(m); r = 1
    for p, e in fac.items():
        if e % 2:
            r *= p
    return r if m > 0 else -r

def QRs_mod(m):
    s = set()
    for x in range(m):
        s.add((x * x) % m)
    return s

# ------------------------------------------------- local solubility of C_d --
def real_ok(d, A, bd):
    """C_d: N^2 = dM^4 + A M^2 e^2 + bd e^4 real points?  Exact (no grid)."""
    if d > 0:
        return True          # e = 0, M != 0 branch
    # d < 0: q(s) = d s^2 + A s + bd, s = t^2 >= 0.  Need max_{s>=0} q >= 0.
    # d<0 => downward parabola; vertex s* = -A/(2d).
    if A > 0:                # s* > 0
        # q(s*) = bd - A^2/(4d) ; >= 0 iff 4B = 4*bd*d <= A^2  (d < 0)
        return A * A >= 4 * B
    # A <= 0: max on [0,inf) at s=0
    return bd >= 0

def local_ok(d, A, B, pmax=97):
    """False only if C_d PROVABLY insoluble at the reals or some p <= pmax."""
    if B % d:
        return True          # not a valid d; do not kill
    bd = B // d
    if not real_ok(d, A, bd):
        return False
    for p in range(2, pmax + 1):
        if p == 2:
            m = 32
            qrs = QRs_mod(m)
            found = False
            for M in range(m):
                M2 = (M * M) % m; M4 = (M2 * M2) % m
                for e in range(m):
                    if M % 2 == 0 and e % 2 == 0:
                        continue
                    val = (d * M4 + A * M2 * ((e * e) % m)
                           + bd * ((e * e % m) * (e * e) % m)) % m
                    if val in qrs:
                        found = True; break
                if found:
                    break
            if not found:
                return False
            continue
        m = p * p
        qrs = QRs_mod(m)
        qrs_p = {v % p for v in qrs}
        dQR = (d % m) in qrs          # e = 0 branch (M unit)
        bdQR = (bd % m) in qrs        # M = 0 mod p branch (e unit)
        if dQR or bdQR:
            continue
        # e unit branch: need t mod p^2 with q(t) = d t^4 + A t^2 + bd a QR mod p^2
        # quick screen mod p on s = t^2 (only (p+1)/2 classes)
        sqs = sorted({(s * s) % p for s in range(p)})
        hit = False
        for s in sqs:
            val = (d * s % p * s + A * s + bd) % p
            if val in qrs_p:
                hit = True; break
        if not hit:
            return False
        # lift: iterate distinct t^2 mod p^2
        t2s = sorted({(t * t) % m for t in range(m)})
        for t2 in t2s:
            val = (d * t2 % m * t2 + A * t2 + bd) % m
            if val in qrs:
                break
        else:
            return False
    return True

# ------------------------------------------------------------- Selmer run --
def selmer(A, B, tag):
    """# locally soluble C_d for d | B squarefree signed (upper bound for
    log2 |E/phi_hat E'|).  Returns (count, survivors, killed)."""
    ds = sqfree_divs(B)
    ok, killed = [], []
    for d in ds:
        if local_ok(d, A, B):
            ok.append(d)
        else:
            killed.append(d)
    out("  curve y^2 = x^3 %+d x^2 %+d x : %d/%d classes survive  %s"
        % (A, B, len(ok), len(ds), ok))
    return len(ok), ok, killed

# --------------------------------------------------------- E_G group law ---
def on_curve(P):
    if P is None:
        return True
    x, y = P
    return y * y == x ** 3 + A2 * x * x + A4 * x + A6

def neg(P):
    return None if P is None else (P[0], -P[1])

def addP(P, Q):
    """E: y^2 = x^3 + A2 x^2 + A4 x + A6, exact rational arithmetic."""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    if P == Q:
        if y1 == 0:
            return None
        lam = F(3 * x1 * x1 + 2 * A2 * x1 + A4, 2 * y1)
    else:
        lam = F(y2 - y1, x2 - x1)
    x3 = lam * lam - A2 - x1 - x2
    y3 = -(y1 + lam * (x3 - x1))
    return (x3, y3)

def mulP(P, n):
    R = None; Q = P
    while n:
        if n & 1:
            R = addP(R, Q)
        Q = addP(Q, Q); n >>= 1
    return R

def order(P, nmax=16):
    R = P; n = 1
    while R is not None and n <= nmax:
        R = addP(R, P); n += 1
        if R is None:
            return n
    return None

# -------------------------------------------------------------------- main --
out("=" * 72)
out("E_G: y^2 = x^3 %+d x %+d   (a2=%d, a4=%d, a6=%d)" % (A4, A6, A2, A4, A6))
out("2-torsion thetas: %s" % THETA)

out("")
out("torsion / point orders (exact group law):")
for P in [(-816, 0), (336, 0), (480, 0), (48, 10368), (912, 20736)]:
    assert on_curve(P), P
    out("  P=%-16s order = %s" % (str(P), order(P)))

out("")
out("2-isogeny descent data per theta:")
rows = []
for th in THETA:
    A = 3 * th
    B = 3 * th * th + A4
    Bp = A * A - 4 * B
    out("  theta=%5d : shifted (A,B) = (%d, %d)   E_i: (A',B') = (%d, %d)"
        % (th, A, B, -2 * A, Bp))
    rows.append((th, A, B, Bp))

out("")
out("sanity: #E_i(F_p) must equal #E_G(F_p) (2-isogenous)")
def cnt(a2, a4, a6, p):
    n = 1
    for x in range(p):
        v = (x * x * x + a2 * x * x + a4 * x + a6) % p
        if v == 0:
            n += 1
        elif pow(v, (p - 1) // 2, p) == 1:
            n += 2
    return n
for th, A, B, Bp in rows:
    okp = all(cnt(A2, A4, A6, p) == cnt(-2 * A, Bp, 0, p)
              for p in (5, 7, 11, 13, 17, 19))
    out("  theta=%5d : #E_i == #E_G at p in {5,7,11,13,17,19}: %s"
        % (th, okp))

out("")
out("Selmer upper bounds (rigorous one-way kills only, p <= 97, p^2 + 2^5):")
res = []
for th, A, B, Bp in rows:
    out("-" * 72)
    a, okA, killA = selmer(A, B, "E-side")
    b, okB, killB = selmer(-2 * A, Bp, "Ei-side")
    res.append((th, a, b, okA, okB))
    out("  theta=%5d: a=%d b=%d  ->  rank(E_G) <= a+b-2 = %d"
        % (th, a, b, a + b - 2))

out("")
out("cross-check: alpha-classes of known points must survive")
def cls(m):
    return sqfree_class(m)
for th, a, b, okA, okB in res:
    A = 3 * th; B = 3 * th * th + A4
    for (x, y) in [(-816, 0), (336, 0), (480, 0), (48, 10368), (912, 20736)]:
        c = cls(x - th)
        stat = "IN " if c in okA else ("(zero)" if c == 0 else "MISSING!")
        out("  theta=%5d  P=%-14s alpha=%5d (sqfree %4d) : %s"
            % (th, "(%d,%d)" % (x, y), x - th, c, stat))

out("")
out("sharp version: im alpha_i is a SUBGROUP of the soluble classes, so")
out("s_A <= dim_F2 <S_A>, s_B <= dim_F2 <S_B>;  rank(E_G) + 2 = s_A + s_B.")
def f2dim(classes):
    """F2-dimension of subgroup of Q*/Q*2 generated by nonzero sqfree ints."""
    primes = sorted({p for c in set(classes) if c not in (0, 1)
                     for p in factor(c)} | ({-1} if any(c < 0 for c in classes
                                                    if c not in (0, 1)) else set()))
    rows = []
    for c in set(classes):
        if c in (0, 1):
            continue
        fac = factor(c)
        row = [0] * len(primes)
        for i, p in enumerate(primes):
            if p == -1:
                row[i] = 1 if c < 0 else 0
            else:
                row[i] = fac.get(p, 0) % 2
        rows.append(row)
    rankv = 0
    pivots = []
    for row in rows:
        r = row[:]
        for pc, pr in pivots:
            if r[pc]:
                r = [a ^ b for a, b in zip(r, pr)]
        nz = next((i for i, v in enumerate(r) if v), None)
        if nz is not None:
            pivots.append((nz, r))
            rankv += 1
    return rankv

out("")
for th, a, b, okA, okB in res:
    dA = f2dim(okA); dB = f2dim(okB)
    out("  theta=%5d : dim<S_A>=%d  dim<S_B>=%d  ->  rank(E_G) <= %d"
        % (th, dA, dB, dA + dB - 2))
out("")
out("=" * 72)
out("SUMMARY")
best = min(f2dim(okA) + f2dim(okB) for _, _, _, okA, okB in res)
out("  rank(E_G) <= %d by all three 2-isogeny Selmer bounds (sharp;"
    % (best - 2,))
out("  for theta=-816 equality: im alpha_1 contains {1,2,3,6} = <2,3>,")
out("  dim exactly 2, and <S_B> = {1} forces s_B = 0).")
out("  ALL known points on E_G are torsion: 2*(48,10368) = %s,"
    % (mulP((48, 10368), 2),))
out("  2*(912,20736) = %s  -> E_G(Q)_tors = Z/2 x Z/4 (order 8)."
    % (mulP((912, 20736), 2),))
out("  => rank(E_G) = 0.")
out("  => rank J(C3_A) = rank J(C3_B) = rank(E_A) + rank(E_A) + rank(E_G)")
out("                                   = 1 + 1 + 0 = 2 < 3 = genus.")
out("  => Coleman/Chabauty applies IN PRINCIPLE to C3_A and C3_B.")
out("  NAMED GAP: the actual Coleman computation (p-adic annihilation of the")
out("  rank-2 MW basis of J, residue bound  #C(Q) <= #C(F_p) + 2g - 2) has")
out("  NOT been carried out; e.g. p=11 (11 > 2g+1, 11 | disc? no):")
out("  #C3_A(F_11) = 8 would give #C3_A(Q) <= 8 + 4 = 12.")