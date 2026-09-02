#!/usr/bin/env python
# 2c refinement round, step 1: exact 3G_A, 4G_A on E~_A and the pole-lever
# kill test for survivor classes -1, M/2-1 (g=3) and -2 (g=4).
#
# Lever: X = 2(y+66x)/(x(x-4)) has a 0/0 point at 2G_A=(4,-264) with regular
# extension 1151/66. For ANY prime p of good reduction with ord_p(G) | g,
# every n = c + kM (M = M_A) satisfies nG = 2G + (n-2)G with (n-2)G = O mod p
# (since ord | gcd(c-2,M) = g), so X(nG) = 1151/66 mod p for ALL class members.
# If (1151/66 | p) = -1, the whole class is dead (X would be a nonresidue,
# but square-X points need X in QR union {0}).
# ord_p(G) | g=3 iff 3G = O mod p iff p | denom(x(3G)); g=4 iff p | denom(x(4G)).
import sys
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

A2, A4 = -256, 18432          # y^2 = x^3 + A2 x^2 + A4 x
G = (F(128), F(512))
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 == -y2: return None
    lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2*x1+A4)/(2*y1)
    x3 = lam*lam - A2 - x1 - x2
    return (x3, -(y1 + lam*(x3-x1)))
def mul(P, n):
    R = None; Q = P
    while n:
        if n & 1: R = add(R, Q)
        Q = add(Q, Q); n >>= 1
    return R

P3 = mul(G, 3); P4 = mul(G, 4)
out("3G_A =", P3)
out("4G_A =", P4)
for name, P in (("3", P3), ("4", P4)):
    x = P[0]
    d = x.denominator
    fs = {}; n = d; dd = 2
    while dd*dd <= n:
        while n % dd == 0: fs[dd] = fs.get(dd,0)+1; n //= dd
        dd += 1 if dd == 2 else 2
    if n > 1: fs[n] = fs.get(n,0)+1
    out("denom(x(%sG)) = %d = %s" % (name, d, fs))

# Legendre symbol of the constant 1151/66 at each candidate prime
CONST = F(1151, 66)
def legendre(a, p):
    a %= p
    if a == 0: return 0
    r = pow(a, (p-1)//2, p)
    return 1 if r == 1 else -1
def sym(fr, p):
    return legendre(fr.numerator % p * pow(fr.denominator % p, -1, p), p) \
        if False else legendre(fr.numerator, p) * legendre(fr.denominator, p)

for name, P in (("3", P3), ("4", P4)):
    d = P[0].denominator
    fs = {}; n = d; dd = 2
    while dd*dd <= n:
        while n % dd == 0: fs[dd] = fs.get(dd,0)+1; n //= dd
        dd += 1 if dd == 2 else 2
    if n > 1: fs[n] = fs.get(n,0)+1
    out("--- class kill via g=%s: primes p | denom(x(%sG)) ---" % (name, name))
    for p in sorted(fs):
        if p in (2, 3, 11):   # bad/constant-denominator primes: skip
            tag = "(excluded: p | 66 or bad reduction)"
        else:
            s = sym(CONST, p)
            tag = "CONST %sresidue -> class %s" % ("non" if s == -1 else "resi", "DEAD" if s == -1 else "survives lever")
        out("  p=%d: %s" % (p, tag))