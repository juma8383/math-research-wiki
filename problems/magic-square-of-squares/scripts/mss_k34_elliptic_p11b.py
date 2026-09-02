#!/usr/bin/env python
# Part 11b: corrected j-extraction for the generic quartic->Weierstrass cubic.
# D(xE) = A xE^3 + B xE^2 + C xE + D0 defines y^2 = D(xE); as a long
# Weierstrass it is (via X=A*xE, Y=A*y): Y^2 = X^3 + B X^2 + A*C X + A^2*D0.
import sys
import sympy as sp
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()
xE, Xq, X2 = sp.symbols('xE Xq X2')

def jinv(a2, a4, a6):
    b2 = 4*a2; b4 = 2*a4; b6 = 4*a6; b8 = 4*a2*a6 - a4*a4
    c4 = b2*b2 - 24*b4; c6 = -b2**3 + 36*b2*b4 - 216*b6
    return F(1728)*F(c4**3)/(F(c4**3 - c6**2))

def generic_model(a, b, c, d, e, v0):
    m = sp.Rational(d, 1)/(2*v0)
    V = xE*Xq**2 + m*Xq + v0
    expr = sp.expand(V**2 - (a*Xq**4 + b*Xq**3 + c*Xq**2 + d*Xq + e))
    q, r = sp.div(sp.Poly(expr, Xq), sp.Poly(Xq, Xq)); assert r.as_expr() == 0
    if q.as_expr().subs(Xq, 0) == 0:
        q2, r2 = sp.div(q, sp.Poly(Xq, Xq)); assert r2.as_expr() == 0; q = q2
    poly = sp.Poly(q.as_expr(), Xq)
    D = sp.factor(sp.discriminant(poly.as_expr(), Xq))
    return D

def report(name, a, b, c, d, e, v0, expect_j):
    D = generic_model(a, b, c, d, e, v0)
    A, B, C, D0 = sp.Poly(D, xE).all_coeffs()
    a2, a4, a6 = int(B), int(A*C), int(A*A*D0)
    j = jinv(a2, a4, a6)
    out("%s: D(xE) = %s" % (name, D))
    out("   Weierstrass y^2 = x^3 + (%d)x^2 + (%d)x + (%d)" % (a2, a4, a6))
    out("   j = %s   expected %s   match: %s" % (j, expect_j, j == expect_j))
    return (a2, a4, a6)

# test quartic v^2 = x^4+3x^3+5x^2+3x+1 (origin (0,1))
w = generic_model(1, 3, 5, 3, 1, 1)
A, B, C, D0 = sp.Poly(w, xE).all_coeffs()
jt = jinv(int(B), int(A*C), int(A*A*D0))
out("test quartic j (generic) =", jt)
I = 10; J = 29
out("test quartic j (claimed formula -27J,-27I):", jinv(0, -27*J, -27*I))
out("test quartic j (claimed formula -27I,-27J):", jinv(0, -27*I, -27*J))
out("")
wa = report("M_A", 1, 132, -250, 132, 1, 1, F(-8000, 81))
wb = report("M_B", 9, -92, 310, -92, 9, 3, F(2744000, 9))
out("")
out("M_A model from generic method:", wa)
out("M_B model from generic method:", wb)