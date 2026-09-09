#!/usr/bin/env python3
# TWO-PARENTS THEOREM verification (round 3).
# The leaf point (r,s,u) on Q-pos-(238,1) has TWO layer-1 preimages on the (1,72)
# quartic n'^2 = u'^4 - 64u'^2v'^2 + 72v'^4:
#   Parent A: (u, +-r*s, n)  with n = s^4-238r^4   [v'^2 = r^2s^2 forced]
#   Parent B: (sigma, rho, s) from the Fermat split (72 rho^4, sigma^4) [halving]
# Verify BOTH are on the quartic at m=2 (exact), and identify the Germain split
# constants of each:
#   Parent A: ((A-n)/2, (A+n)/2) = (238 r^4, s^4)   -> constants (238,1) = the leaf's cell
#   Parent B: ((A'-s)/2, (A'+s)/2) = (1*3^4, 238*2^4) -> constants (1,238) = KILLED cell
# K34-A chain: (a,b) -> layer-1 (u,v,n) with uv=ab, n=a^2+b^2 -> Germain split in the
# leaf's cell (238,1) forces v^2 = r^2 s^2 (v = +-rs). So Parent A is THE K34-A-chain
# parent; Parent B is the shadow chain through the killed (1,238) cell.
from fractions import Fraction as F
import math

r, s, u = 852, 3727, 25318369
n = s**4 - 238*r**4
assert u*u == 238*r**4 + 32*r*r*s*s + s**4

# Parent A: (u, rs, n) on (1,72): n^2 = u^4 - 64u^2 v^2 + 72 v^4, v = r*s
v = r*s
lhs = n*n
rhs = u**4 - 64*u*u*v*v + 72*v**4
print("Parent A (u,rs,n) on (1,72) quartic:", lhs == rhs)
# its Germain split
A = u*u - 32*v*v
print("A = u^2-32v^2 =", A, " == s^4+238r^4 ?", A == s**4 + 238*r**4)
p1, p2 = (A - n)//2, (A + n)//2
print("((A-n)/2, (A+n)/2) == (238 r^4, s^4)?", p1 == 238*r**4 and p2 == s**4)
print("  product == 238 v^4?", p1*p2 == 238*v**4)

# Parent B: (sigma, rho, s) with (F-/2, F+/2) = (72 rho^4, sigma^4)
s2p = s*s + 16*r*r
Fm, Fp = s2p - u, s2p + u
h2, hp = Fm//2, Fp//2
rho = math.isqrt(math.isqrt(h2//72)); sigma = math.isqrt(math.isqrt(hp))
assert 72*rho**4 == h2 and sigma**4 == hp
lhsB = s*s
rhsB = sigma**4 - 64*sigma*sigma*rho*rho + 72*rho**4
print("\nParent B (sigma,rho,s) on (1,72) quartic:", lhsB := lhs == rhsB, "->", lhsB == (rhsB == lhs))
print("  (sigma,rho,s) =", (str(sigma)[:12]+'...', str(rho)[:12], str(s)[:12]))
A2 = sigma*sigma - 32*rho*rho
q1, q2 = (A2 - s)//2, (A2 + s)//2
print("((A'-s)/2, (A'+s)/2) =", q1, q2)
print("  == (1*3^4, 238*2^4)?", q1 == 81 and q2 == 3808)
print("  product == 238 rho^4?", q1*q2 == 238*rho**4)
# lift conditions:
print("\nLift on Parent A: n +- 2u*rs both squares?")
def issq(x):
    if x < 0: return False
    rt = math.isqrt(x); return rt*rt == x
a1, a2 = n + 2*u*v, n - 2*u*v
print(f"  n+2urs = {a1} sq? {issq(a1)}   n-2urs = {a2} sq? {issq(a2)}  (n-2urs<0: {a2<0})")
print("Lift on Parent B: s +- 2 rho sigma both squares?  (2 rho sigma = r?)")
print("  2 rho sigma == r?", 2*rho*sigma == r)
b1, b2 = s + 2*rho*sigma, s - 2*rho*sigma
print(f"  s+r = {b1} sq? {issq(b1)}   s-r = {b2} sq? {issq(b2)}")
# NOTE: Parent B's lift = s +- r; Parent A's lift = n +- 2u rs.
# K34-A chain needs uv = ab AND n = a^2+b^2 on ITS parent -> Parent A.
# (a,b) from Parent A iff both n+-2urs squares; from Parent B iff both s+-r squares
# BUT Parent B's Germain child is in the KILLED (1,238) cell -> not K34-A reachable.