from fractions import Fraction as F
import math

# D's second point: (x, V) = (-33/2, 5/4). Where does it map in J_L^sh?
# D's Jacobian = J_L: y^2 = x^3 - 27894240x + 56491485696, T=(-6096,0).
# The quartic-to-cubic map for V^2 = quartic with rational point (x0,V0):
# Use the standard map sending (x0,V0) to infinity/2-torsion, then trace the
# image of (-33/2, 5/4). Implement via the classical transformation.
# Quartic: V^2 = a x^4 + b x^3 + c x^2 + d x + e, point (0, v0), v0^2 = e (v0=238, e=56644).
# Substitution x = 1/X? Standard trick: the map to the Jacobian with T at (0,0):
#   The cover map C -> Jac is abstract; easier: use the INVARIANT test instead.
# Test: does the point (-33/2, 5/4) map to a NON-torsion point of J_L (rank 1 => D soluble
# with a nontrivial point => the lift gate has solutions!?), or is it the generator's preimage?
# CRUCIAL: check what the point (-33/2,5/4) MEANS for K34:
#   x = -33/2 = (s/r)^2?? NEGATIVE -> (s/r)^2 must be positive! So this point is NOT
#   of the fiber-lift form (s/r)^2 > 0. But it's a rational point on D nonetheless.
# What matters: rational points on D with x a POSITIVE square of a rational.
print("N(x) for x = square classes; search x = (p/q)^2:")
found = []
for q in range(1, 30):
    for p in range(1, 200):
        if math.gcd(p,q) != 1: continue
        xv = F(p*p, q*q)
        v = xv**4 - 4*xv**3 - 604*xv*xv - 952*xv + 56644
        if v > 0 and math.isqrt(v.numerator)**2 == v.numerator and math.isqrt(v.denominator)**2 == v.denominator:
            found.append((xv, F(math.isqrt(v.numerator), math.isqrt(v.denominator))))
            print(f"  x = {xv} = ({p}/{q})^2, V = {found[-1][1]}")
            if len(found) > 8: break
    if len(found) > 8: break
if not found:
    print("none found in the small box")
# x=0 IS a square class (0 = (0/q)^2) - the degenerate point. Note x=0 <=> s=0.
print("\nAlso check: does x=8568-class connection appear? alpha^L(G)=238: the D-quartic")
print("represents which alpha^L-class? J_L^sh alpha(T)=a4=83589408 sqclass: ")
def sf(n):
    n=abs(n); out=1; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e%2: out*=d
        d+=1
    if n>1: out*=n
    return out
print("  sqclass(83589408) =", sf(83589408))
print("  sqclass(238) = 238; 83589408 = 238^2 * 1476.5? compute:", 83589408/238, "sqclass of that:", sf(83589408//238) if 83589408%238==0 else "non-integer")
print("  83589408 = 2^5*3^4*7*17*271 ; 238 = 2*7*17 -> ratio = 2^4*3^4*271 -> sqclass = 271")
print("  => alpha^L(T) class = 238 * 271; image = <238, 271> = {1, 238, 271, 64498}")