#!/usr/bin/env python3
# image(alpha^L) settled: {1, 64498, 238, 271}. Now the KEY question:
# which square-class does the quartic D (V^2 = N(x)) represent, and does D
# have rational points beyond its degenerate one?
#
# D arose from: leaf fiber point (r,s,u) -> lift condition n +- 2u*rs = squares
#   <=> V^2 = N((s/r)^2) for V = (n+2uv)/r^4-type.
# Equivalently: D is the quartic whose points parametrize fiber points of
# C_238 (on E_a) that ALSO satisfy the candidate lift on E_a.
#
# Connection to J_L: we COMPUTED D's Jacobian = J_L. The map quartic->cubic:
#   for quartic V^2 = N(x) with degenerate point (0, 238) [x=0, V=238]:
#   standard: set x = 1/X-ish transform... let's just find the map by matching
#   the degenerate point to T = (0,0) of J_L^sh and checking where the known
#   second point goes. D's known points: (0, +-238). Any other?
# Try to find small rational points on D by brute force.
from fractions import Fraction as F
import math

def N(x): return x**4 - 4*x**3 - 604*x*x - 952*x + 56644
def issq_int(n):
    if n < 0: return False
    r = math.isqrt(n); return r*r == n

print("integer points x in [-200..200] with N(x) a positive square:")
hits = []
for x in range(-200, 201):
    v = N(x)
    if v >= 0 and issq_int(v):
        hits.append((x, math.isqrt(v)))
print(hits)
# also x with denominators: x = p/q small
print("\nsmall rational points (q<=12, p in [-40,40]):")
rhits = []
for q in range(1, 13):
    for p in range(-40, 41):
        if math.gcd(p, q) != 1 and q != 1: continue
        xv = F(p, q)
        v = xv**4 - 4*xv**3 - 604*xv*xv - 952*xv + 56644
        if v >= 0 and issq_int(v.numerator) and issq_int(v.denominator):
            rhits.append((xv, F(math.isqrt(v.numerator), math.isqrt(v.denominator))))
print(rhits[:20])