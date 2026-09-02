#!/usr/bin/env python
# [mss-k34-g3jac] Part 2: the bielliptic decomposition of C3_A, C3_B.
#
# C3_A: W^2 = x^8+132x^6-250x^4+132x^2+1  has involutions
#   iota : x -> -x      quotient M_A: V^2 = X^4+132X^3-250X^2+132X+1
#   rho  : x -> 1/x     quotient D_A: v^2 = z^4+128z^2-512     (z=x+1/x)
#   iota*rho: x -> -1/x quotient G_A: w^2 = u^4+136u^2+16      (u=x-1/x)
# (G_A is exactly the QA(u)=u^4+136u^2+16 quartic of the K34 reduction;
#  D_A is the "sibling 2-cover" of notes sec.5.)
# Claim: C3 is bielliptic, J(C3) ~ J(M) x J(D) x J(G) (all genus 1), and
#   J(D_A) ~ E_A  (same I,J invariants),  J(G_A) ~ E_G,
#   J(D_B) ~ E_B,                         J(G_B) ~ E_G   (SAME E_G),
# where E_G: y^2 = x^3 - 504576 x + 131604480.
# We verify: (a) the quotient maps symbolically; (b) exact factorization of
# the degree-6 Frobenius polynomial into the three quadratic charpolys at 8
# primes; (c) the same N1 prediction at 36 more primes; (d) Jacobian cubics
# from classical invariants vs quartic Frobenius traces; (e) E_G torsion
# bound + rational point search.  ASCII only.
import sys
from fractions import Fraction as F

def out(*a):
    print(*a)
    sys.stdout.flush()

src = open("mss_k34_g3jac_frobenius.py").read().split(
    "# ------------------------------------------------------------------- main --")[0]
ns = {}
exec(src, ns)
legendre_count_poly = ns["legendre_count_poly"]
count_fk = ns["count_fk"]
frob_poly = ns["frob_poly"]
count_cubic = ns["count_cubic"]
polydiv = ns["polydiv"]
split_quartic = ns["split_quartic"]

# ---------------------------------------------------------------- part (a) --
out("(a) symbolic quotient maps")
import sympy
xs = sympy.symbols("x")
def check(tag, octic, Mquartic, Dquartic, Gquartic):
    gx = sum(c * xs ** i for i, c in enumerate(octic))
    pal = sympy.expand(gx - xs ** 8 * gx.subs(xs, 1 / xs))
    out("  C3_%s palindromic (g - x^8 g(1/x) = 0): %s" % (tag, pal == 0))
    z = sympy.symbols("z")
    u = sympy.symbols("u")
    # full DESCENDING coefficient lists (deg 4): c0 z^4 + c1 z^3 + ...
    Dpoly = sum(c * z ** (4 - i) for i, c in enumerate(Dquartic))
    Gpoly = sum(c * u ** (4 - i) for i, c in enumerate(Gquartic))
    id1 = sympy.simplify(gx - xs ** 4 * Dpoly.subs(z, xs + 1 / xs))
    id2 = sympy.simplify(gx - xs ** 4 * Gpoly.subs(u, xs - 1 / xs))
    out("  rho-quotient identity g = x^4*D(x+1/x): %s ; "
        "iota*rho identity g = x^4*G(x-1/x): %s" % (id1 == 0, id2 == 0))

C3A = ns["C3"]["A"]
C3B = ns["C3"]["B"]
# full DESCENDING quartic coefficient lists (z^4 .. z^0)
check("A", C3A, None, [1, 0, 128, 0, -512], [1, 0, 136, 0, 16])
check("B", C3B, None, [9, 0, -128, 0, 512], [9, 0, -56, 0, 144])

# ------------------------------------------------------------- part (b,c) --
out("")
out("(b) exact triple factorization of the degree-6 Frobenius polynomial")
# ASCENDING coefficient lists (coeffs[-1] = leading)
QUART = {
    "A": {"iota": [1, 132, -250, 132, 1], "rho": [-512, 0, 128, 0, 1],
          "iota_rho": [16, 0, 136, 0, 1]},
    "B": {"iota": [9, -92, 310, -92, 9], "rho": [512, 0, -128, 0, 9],
          "iota_rho": [144, 0, -56, 0, 9]},
}
BASE = {"A": "E_A", "B": "E_B"}
full_primes = [7, 11, 13, 17, 19, 23, 29, 31]
many_primes = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
               167, 173, 179, 181, 191, 193, 197, 199, 211]
for tag in ("A", "B"):
    out("-" * 70)
    out("C3_%s" % tag)
    for p in full_primes:
        N1, N2, N3 = (legendre_count_poly(C3A if tag == "A" else C3B, p),
                      count_fk(C3A if tag == "A" else C3B, p, 2),
                      count_fk(C3A if tag == "A" else C3B, p, 3))
        P6 = frob_poly(N1, N2, N3, p)
        ts = []
        for q in ("iota", "rho", "iota_rho"):
            nq = legendre_count_poly(QUART[tag][q], p)
            ts.append(p + 1 - nq)
        L = [1]
        for t in ts:
            L = list(__import__("numpy").convolve(L, [1, -t, p]))
        okfull = (list(L) == [int(v) for v in P6])
        out("  p=%3d  #J=%8d  traces(iota,rho,ir)=%s  P6==prod: %s"
            % (p, sum(P6), ts, okfull))
    ok = 0
    for p in many_primes:
        pred = p + 1 - sum(p + 1 - legendre_count_poly(QUART[tag][q], p)
                           for q in ("iota", "rho", "iota_rho"))
        act = legendre_count_poly(C3A if tag == "A" else C3B, p)
        ok += (pred == act)
    out("  N1 prediction at %d primes (7..211): %d OK" % (len(many_primes), ok))

# ---------------------------------------------------------------- part (d) --
out("")
out("(d) Jacobian cubics from classical invariants")
def invariantsJ(q):
    a, b, c, d, e = q
    I = 12 * a * e - 3 * b * d + c * c
    J = 72 * a * c * e + 9 * b * c * d - 27 * a * d * d - 27 * b * b * e - 2 * c ** 3
    return I, J

JAC = {}
for tag in ("A", "B"):
    for q in ("iota", "rho", "iota_rho"):
        quart = QUART[tag][q]
        a4c, b4c, c4c, d4c, e4c = quart[4], quart[3], quart[2], quart[1], quart[0]
        I, J = invariantsJ((a4c, b4c, c4c, d4c, e4c))
        # Jacobian: y^2 = x^3 - 27 I x - 27 J   -> (a2,a4,a6) = (0,-27I,-27J)
        JAC[(tag, q)] = (0, -27 * I, -27 * J)
        out("  C3_%s/%s quartic invariants I=%d J=%d -> cubic y^2=x^3%+dx%+d"
            % (tag, q, I, J, -27 * I, -27 * J))
# check traces: quartic vs its Jacobian cubic at many primes
out("")
out("  quartic-vs-cubic Frobenius trace agreement (primes 7..211):")
okall = True
for tag in ("A", "B"):
    for q in ("iota", "rho", "iota_rho"):
        quart = QUART[tag][q]
        A2c, A4c, A6c = JAC[(tag, q)]
        b2 = 4 * A2c; b4 = 2 * A4c; b6 = 4 * A6c
        b8 = 4 * A2c * A6c - A4c * A4c
        Disc = (-b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6)
        bad = []
        for pp in range(7, 212):
            p = pp
            ip = 2
            while ip * ip <= p and p % ip:
                ip += 1
            if (ip * ip <= p) or p == 2 or Disc % p == 0:
                continue
            tq = p + 1 - legendre_count_poly(quart, p)
            tc = p + 1 - count_cubic(A2c, A4c, A6c, p)
            if tq != tc:
                bad.append(p)
        out("  C3_%s/%s: trace mismatches 7..211: %s"
            % (tag, q, bad if bad else "NONE (cubic ~ Jac(quartic))"))

# ---------------------------------------------------------------- part (e) --
out("")
out("(e) the common Prym factor E_G: y^2 = x^3 - 504576 x + 131604480")
EG = (0, -504576, 131604480)
# c4, c6, j, discriminant
A2, A4, A6 = EG
b2 = 4 * A2; b4 = 2 * A4; b6 = 4 * A6
b8 = 4 * A2 * A6 - A4 * A4
c4 = b2 * b2 - 24 * b4
c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
Disc = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
out("  c4=%d c6=%d" % (c4, c6))
out("  Delta=%d  j=%s" % (Disc, F(c4 ** 3, Disc)))
# torsion bound from gcd of #E(F_p)
g = 0
for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
    n = count_cubic(A2, A4, A6, p)
    g = n if g == 0 else __import__("math").gcd(g, n)
out("  gcd #E_G(F_p) over p in {5..43} = %d  -> torsion divides %d" % (g, g))
# rational 2-torsion? rational roots of the cubic
import math
def introot(c):
    n = abs(c); r = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            for s in (d, -d, n // d, -(n // d)):
                if s and (s ** 3 + A2 * 0 + A4 * 0 + A6) % 1 == 0:
                    pass
        d += 1
    return None
found = []
n0 = abs(A6)
d = 1
while d * d <= n0:
    if n0 % d == 0:
        for s in (d, n0 // d, -d, -(n0 // d)):
            if (s ** 3 + A2 * s * s + A4 * s + A6) == 0:
                found.append(s)
    d += 1
out("  rational roots of cubic (2-torsion x-coords): %s" % sorted(set(found)))
# rational point search on E_G
pts = []
B = 4000
for x in range(-B, B + 1):
    v = x ** 3 + A2 * x * x + A4 * x + A6
    if v < 0:
        continue
    r = int(v ** 0.5)
    for y in (r - 1, r, r + 1):
        if y >= 0 and y * y == v:
            pts.append((x, y))
            pts.append((x, -y))
# also rational x = m/n with small n
for nn in range(2, 30):
    for mm in range(-400, 401):
        x = F(mm, nn)
        v = x ** 3 + A2 * x * x + A4 * x + A6
        if v >= 0:
            r = int(v ** F(1, 2)) if isinstance(v, int) else None
            if r is not None and r * r == v:
                pts.append((x, r))
                pts.append((x, -r))
pts = sorted(set(pts))
out("  small rational points on E_G (|x|<=%d or denom<30): %d found" % (B, len(pts)))
for P in pts[:24]:
    out("    %s" % (P,))