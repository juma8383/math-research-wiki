#!/usr/bin/env python3
from fractions import Fraction as F
import math
# D, C1, C2 all share (I,J) = (1033120, -2092277248) — same Jacobian J_L, confirming
# D is a cover of J_L. Now the gate question precisely:
#   D-point with x = positive rational square (from (s/r)^2 of C_238 fiber points).
# The alpha^L-fibers: image(alpha^L) = {1, 238, 271, 64498}. The quartic D has a
# rational point (-33/2,5/4) so it represents ONE of the four classes (as an
# alpha^L-cover in the NON-diagonal form). Determine which class by mapping
# the known D points into J_L^sh and checking n mod 2 / T-shift.
# Map via C2 (the non-diagonal cover, structurally closer to D):
# C2: y^2 = 9x^4+168x^3+566x^2-1312x+477 with map [33048/y^2*x^4 + ... + (6084y^2+2258856)/y^2, ...]
# Instead of transcribing, test the square-x points DIRECTLY on D (exact):
# D-point with x=(p/q)^2: found NONE in the small box (only x=0).
# Enlarge the search using the J_L group law: D(Q) ~= fiber(alpha^L-class).
# Points of J_L^sh: n*G^sh (+T). The fiber containing the D-point's image:
# the D-point (-33/2,5/4) maps to some n*G^sh (+-T). Its alpha^L class is in {238,271}
# (the G-cosets). The square-x condition picks the class of (s/r)^2-type points:
# For a D-point coming from a C_238 fiber point: x_D = (s/r)^2 has square class 1!
# So the gate quartic D, restricted to the K34-relevant preimages, is the CLASS-1
# fiber of alpha^L. D(Q) has points in classes {238,271} (found) — but the K34
# lift needs the CLASS-1 fiber (x a square). Class-1 points of J_L^sh = 2E(Q) =
# <2G^sh>. So the gate = '2G^sh-orbit has a point with quartic-x a positive square'.
# Test: does the class-1 fiber quartic C1: y^2 = 8x^4+1016x^2+9 have square-x points?
print("C1 fiber (class 1): y^2 = 8x^4 + 1016x^2 + 9; x square <=> x=(p/q)^2:")
found = []
for q in range(1, 40):
    for p in range(1, 400):
        if math.gcd(p, q) != 1: continue
        xv = F(p*p, q*q)
        v = 8*xv**4 + 1016*xv*xv + 9
        if v > 0 and math.isqrt(v.numerator)**2 == v.numerator and math.isqrt(v.denominator)**2 == v.denominator:
            found.append((xv, F(math.isqrt(v.numerator), math.isqrt(v.denominator))))
            print(f"  HIT: x = {xv} = ({p}/{q})^2, y = {found[-1][1]}")
            break
    if found: break
if not found:
    print("  no hit in p<=400, q<=40")
# x=1: 8+1016+9 = 1033 not square. x=1/4: 8/256+1016/16+9 = 0.5+63.5+9=64 = 8^2 !!!
v = 8*F(1,16) + 1016*F(1,16) + 9
print("\nx=1/4 direct: 8*(1/256)+1016*(1/16)+9 =", v, " square?", v == 64)
# CHECK: x = 1/4 = (1/2)^2: y^2 = 8/256 + 1016/16 + 9 = 1/32 + 63.5 + 9 = 72.53?? recompute
print("exact:", F(8,256) + F(1016,16) + 9)
# = 1/32 + 63.5 + 9 = 72.53... not 64. Careful: 1016/16 = 63.5. total = 72.53125. not square.
# So my loop's test would catch it if square; it printed nothing => no hit there.
print("\nStructural conclusion: the gate is a rank-1 square-x question on the C1 cover,")
print("same shape as K34-A. It does NOT collapse. Filing the correction + the D data.")