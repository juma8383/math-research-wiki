#!/usr/bin/env python3
# CORRECTION ROUND: the leaf point (r,s,u) has TWO layer-1 preimages:
#  (a) CANDIDATE-chain preimage (the K34-A-relevant one):
#      (u, +-r*s, n_L2) with n_L2 = s^4-238r^4, on the (1,72) quartic (tautology).
#      Its lift condition: n_L2 +- 2*u*r*s = (a+-b)^2  [uv = u*rs = ab]
#      ==> (n+2uv)(n-2uv) = n^2-4u^2v^2 must be a square, with coprime factors.
#  (b) The Fermat-regenerated one (sigma,rho,s) -- what §2j tested (s +- r).
# The candidate lift reduces via the duplication formula:
#   x(2R) = (x^2-238)^2 / (4x(x^2+32x+238))  on E_a
#   phi(Q) = (x(Q)-1)/x(Q);  phi(2R) = N(x(R))/(x(R)^2-238)^2
#   N(x) = x^4 - 4x^3 - 604x^2 - 952x + 56644
# so the candidate lift for fiber(T_a + 2m P_a) <=> N(x(m P_a)) = square  (+size cond).
# The quartic D: V^2 = N(x) has the degenerate point (0, +-238) (R = T_a).
# Compute D's invariants exactly and its Jacobian j-invariant.
from fractions import Fraction as F
import math

# N(x) coefficients
a,b,c,d,e = 1,-4,-604,-952,56644
I = 12*a*e - 3*b*d + c*c
J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
print(f"D: V^2 = x^4-4x^3-604x^2-952x+56644")
print(f"I = {I} = 12ae-3bd+c^2")
print(f"J = {J}")
print(f"Jacobian: y^2 = x^3 - 27*I*x - 27*J = x^3 + {(-27*I)} x + {-27*J}")
# independent check via the depressed quartic z = x+1 (kills x^3)
# N(z-1+1)=N(z): wait x = z+1 means z = x-1; recompute directly
def N(x): return x**4 - 4*x**3 - 604*x*x - 952*x + 56644
# depressed: substitute x = z+1, expand symbolically by evaluation
# N(z+1) = z^4 + P z^2 + Q z + R
P  = N(1) - N(-1)  # no; do it properly with binomials
def shift(coeffs, s):
    # coeffs c0..c4 for x^0..x^4 -> (z+s)^i expansion
    from math import comb
    out = [0]*4
    for i,ci in enumerate(coeffs):
        for j in range(i+1):
            out[j] += ci*comb(i,i-j)*s**(i-j) if False else 0
    return out
# explicit: N(x) with x = z+1
# (z+1)^4 = z4+4z3+6z2+4z+1 ; -4(z+1)^3 = -4z3-12z2-12z-4
# -604(z+1)^2 = -604z2-1208z-604 ; -952(z+1) = -952z-952
c4 = 1
c3 = 4-4
c2 = 6-12-604
c1 = 4-12-1208-952
c0 = 1-4-604-952+56644
print(f"depressed (x=z+1): V^2 = z^4 + ({c2})z^2 + ({c1})z + {c0}")
a2,b2,c2_,d2,e2 = 1,0,c2,c1,c0
I2 = 12*a2*e2 - 3*b2*d2 + c2_*c2_
J2 = 72*a2*c2_*e2 + 9*b2*c2_*d2 - 27*a2*d2*d2 - 27*b2*b2*e2 - 2*c2_**3
print(f"depressed invariants: I={I2} (match {I==I2}), J={J2} (match {J==J2})")
# j-invariant of the Jacobian y^2 = x^3 - 27 I x - 27 J
A, B = -27*I, -27*J
jnum = 1728*4*A**3
jden = 4*A**3 + 27*B**2
from math import gcd
g = gcd(abs(jnum), abs(jden))
jn, jd = jnum//g, jden//g
print(f"J_L: y^2 = x^3 + {A}x + {B}")
print(f"j(J_L) = {jn}/{jd} = {float(jn)/jd:.6f}")
print(f"j(E_a)  = 238328000/127449   = {238328000/127449:.6f}")
print(f"j(E_2)  = 7301384000/9639 = {7301384000/9639:.6f}")
print(f"j(J_L)==j(E_a)? {jn==238328000 and jd==127449}")
# sanity: N at known points
print("\nN(x(P_a)) = N(-14) =", N(-14), " (x(P_a)=-14; phi(2P_a)=5/9 -> N should be 5*14^4-class)")
print("N(0) =", N(0), "= 238^2?", 238**2)
print("(x^2-238)^2 at x=-14:", (-14**2-238)**2 if False else (196-238)**2, "; phi(2P)=N/(x^2-238)^2 =", N(-14), "/", (196-238)**2)