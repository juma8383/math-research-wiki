#!/usr/bin/env python
# Part 2: quartic -> Weierstrass maps, verified on known points.
from fractions import Fraction as F
import sys
def out(*a): print(*a); sys.stdout.flush()

# M_A: V^2 = Xq^4+132Xq^3-250Xq^2+132Xq+1, point (0,1), slope m=d/(2V0)=66
# map: x_E = (V - V0 - m*Xq)/Xq^2  -- pole 2 at (0,V0), regular at (0,-V0)?
# corrected: need +m*Xq: x_E=(V+1+66Xq)/Xq^2  (derived by killing pole at (0,-1))
# Resulting cubic in Xq: (xE^2-1)Xq^2 -132(1+xE)Xq + (4606-2xE) = 0
# => YE^2 = D(xE) = 8*xE^3-1000*xE^2+34840*xE+35848 ; with U=2xE:
# E_A: Y^2 = U^3 - 250U^2 + 17420U + 35848   (to verify)
# M_B: V^2 = 9Xq^4-92Xq^3+310Xq^2-92Xq+9, point (0,3), m=d/(2V0)=-46/3
# x_E=(V-3+(46/3)Xq)/Xq^2 ; derive analogous curve symbolically below.

import sympy as sp
xE, Xq, V = sp.symbols('xE Xq V')

def quartic_to_cubic(f, V0, m, name):
    # f in Xq; substitution V = xE*Xq^2 + m*Xq - V0 ... careful sign:
    # xE := (V - V0 - m*Xq)/Xq^2  => V = xE*Xq^2 + m*Xq + V0
    x = sp.symbols('x')
    rel = sp.expand((x*Xq**2 + m*Xq + V0)**2 - f)
    # divide by Xq^2 (the point Xq=0,V=V0 is the map's O); remaining is quadratic in Xq
    poly = sp.Poly(sp.cancel(rel/Xq**2), Xq)
    c2, c1, c0 = [sp.expand(poly.coeff_monomial(Xq**k)) for k in (2,1,0)]
    disc = sp.expand(c1**2 - 4*c2*c0)
    out(name, "quadratic coeffs:", sp.factor(c2), "|", sp.factor(c1), "|", sp.factor(c0))
    out(name, "discriminant poly in x:", sp.factor(disc))
    return disc

fA = Xq**4 + 132*Xq**3 - 250*Xq**2 + 132*Xq + 1
fB = 9*Xq**4 - 92*Xq**3 + 310*Xq**2 - 92*Xq + 9
# which sign of m kills the pole? try both, keep the one giving quadratic in Xq
for nm, f, V0, m in (("M_A", fA, 1, sp.Rational(132,2)),
                     ("M_B", fB, 3, sp.Rational(-92,6))):
    rel = sp.cancel(sp.expand((xE*Xq**2 + m*Xq + V0)**2 - f)/Xq**2)
    out(nm, "degree after cancel:", sp.Poly(rel, Xq).degree())
out("== M_A map (sgn=+1) ==")
dA = quartic_to_cubic(fA, 1, 66, "M_A")
out("== M_B map ==")
dB = quartic_to_cubic(fB, 3, sp.Rational(-46,3), "M_B")