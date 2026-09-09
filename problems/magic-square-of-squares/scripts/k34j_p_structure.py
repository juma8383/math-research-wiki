#!/usr/bin/env python3
# ROUND 6: identify the ±pair elliptics via the genus-2 splitting structure.
# P : y^2 = x^5 - 4x^4 - 604x^3 - 952x^2 + 56644x has the Weierstrass point (0,0).
# A genus-2 curve with a rational Weierstrass point admits an EXTRA involution
# only if the quintic has special structure. The ±pair E, E^chi suggests P is
# a DOUBLE COVER of two elliptic curves: y^2 = x*N(x) — the substitutions
# x -> ... For a quintic with a rational root x=0: the classic decomposition:
# Jac(P) ~ E1 x E2 where E_i come from the two involutions when P is a
# fiber product of two quadratics. Test whether N(x) has quadratic-structure:
# N(x) = x^4-4x^3-604x^2-952x+56644. Complete square: (x^2-2x)^2 - (608x^2+952x-56644).
# Check if N(x) = (x^2+ax+b)^2 - c*(dx+e)^2 form (then P covers two elliptics).
from fractions import Fraction as F
import math

# Solve N(x) = (x^2+ux+v)^2 - c(w x + z)^2 by matching coefficients.
# x^4 + (2u)x^3 + (u^2+2v)x^2 + (2uv)x + v^2 - c(w^2 x^2 + 2we x + e^2)
# match: 2u = -4 => u = -2; u^2+2v - c w^2 = -604; 2uv - 2cwe = -952; v^2 - c e^2 = 56644.
# v^2 - c e^2 = 56644 = 238^2. Try v = 238, e = 0? then c w^2 = -604 - u^2 - 2v... 
# u=-2: u^2 = 4. c w^2 = -604 - 4 - 2v; 2(-2)v - 2cwe = -952 => -4v = -952 (e=0? no: 
# 2uv term: 2*(-2)*v = -4v; minus 2c w e: if e=0: -4v = -952 => v = 238!
# Then c w^2 = -604-4-476 = -1084 => c w^2 = -1084 (negative: c<0 or imaginary).
# v^2 = 238^2 = 56644 ✓ with e=0: the "square" is (x^2-2x+238)^2 and 
# c(w x)^2 = -1084 x^2 => N(x) = (x^2-2x+238)^2 + 1084 x^2. Verify:
def N(x): return x**4 - 4*x**3 - 604*x*x - 952*x + 56644
for xx in (0, 1, 2, 3, -1, 10):
    lhs = N(xx)
    rhs = (xx*xx - 2*xx + 238)**2 + 1084*xx*xx
    print(f"x={xx}: N={lhs}, completed-square form={rhs}, match={lhs==rhs}")
# So N(x) = (x^2-2x+238)^2 + 1084x^2. And P: y^2 = x[(x^2-2x+238)^2 + 1084x^2].
# With w = x: y^2 = x(x^2-2x+238)^2 + 1084x^3.
# The natural subcover: y^2 = x(x^2-2x+238)^2 is a genus-1 curve? y^2 = x(cubic^2)
# => y = (x^2-2x+238)*sqrt(x) => set t^2 = x: y = ±t(t^4-2t^2+238)... 
# The two elliptic quotients of P: the involutions (x,y)->(x,-y) [hyperelliptic]
# and possibly (x,y)->(x, -y + 2(x^2-2x+238)*sqrt-ish)? For y^2 = x S(x)^2 + 1084 x^3
# with S = x^2-2x+238: the curve has the map (x, y) -> (x, y ± S(x)*t) with t^2 = x...
# over Q(sqrt(x)) — not rational. The REAL splitting: check if 1084 = 4*271: 
print("\n1084 = 4*271:", 1084 == 4*271)
# y^2 - x S(x)^2 = 1084 x^2 = (2 sqrt(271) x)^2 over Q(sqrt(271))!
# => over K = Q(sqrt(271)): y^2 = x(S(x)^2 + 4*271 x) = x(S(x)^2 + 4 k^2 x), k=sqrt(271)
# = x(S + 2k sqrt(x))(S - 2k sqrt(x)): genus-1 structure over K(x, sqrt(x)).
# The elliptic factors over Q: E1: y^2 = x^3 + a x^2 + b x with discriminant 271-ish?
# The ±pair curves should have conductors with 271. find_pair4's candidate A=2178, B=225:
# 2178 = 2*3^2*11^2; 225 = 3^2*5^2. Its ap failed at 199,223,239,241 — note 271 was
# a bad prime for J_L. Let me test twists of THAT curve or search with 271-family.
print("The J_L conductor had 271; the pair may live in the 271-isogeny family.")
print("Try: curves y^2 = x^3 + A x + B with 271 | cond, matching ap(23)=+-4 first.")
print("(deferred to PARI).")