#!/usr/bin/env python3
# First: verify the lift-reduction identity n^2-4u^2(rs)^2 = r^8 * N(s^2/r^2)
# at the admissible m=2 point, and test the TRUE candidate lift there.
from fractions import Fraction as F
import math

def N(x):
    if isinstance(x, F):
        return x**4 - 4*x**3 - 604*x*x - 952*x + 56644
    return x**4 - 4*x**3 - 604*x*x - 952*x + 56644

# m=2 admissible point
r, s, u = 852, 3727, 25318369
n = s**4 - 238*r**4
assert u*u == 238*r**4 + 32*r*r*s*s + s**4
v = r*s
lhs = n*n - 4*u*u*v*v
xval = F(s*s, r*r)
rhs = r**8 * N(xval)   # N of a Fraction
print("n^2 - 4u^2(rs)^2 =", lhs)
print("r^8 * N(s^2/r^2) =", rhs)
print("identity holds:", lhs == rhs)

# TRUE candidate lift test at m=2: n +- 2uv squares?
p1 = n + 2*u*v
p2 = n - 2*u*v
def issq(x):
    if x < 0: return False
    rt = math.isqrt(x)
    return rt*rt == x
print(f"\nm=2 TRUE candidate lift: n+2uv = {p1} square? {issq(p1)}")
print(f"                         n-2uv = {p2} square? {issq(p2)}")
print(f"product square? {issq(p1*p2)}  (== N(s^2/r^2) square: {issq(N(xval).numerator) and issq(N(xval).denominator)})")
g = math.gcd(p1, p2)
print(f"gcd(n+2uv, n-2uv) = {g} (delta lemma predicts 2 for the j=1 stratum)")

# also check: is N(s^2/r^2) positive? and (s^2/r^2, V) on D means V^2 = N(x)
print(f"\nN((s/r)^2) = {N(F(s*s, r*r))}  (want square*1764^... i.e. product/(r^8) form)")
# cross-check via D directly: x = s^2/r^2
# N(x) as fraction: V^2 = N(x); V = (a^2-b^2)/r^4 * sign if lift holds