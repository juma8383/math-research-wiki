#!/usr/bin/env python
# Part 11: (1) Frobenius-trace test: is claimed Jacobian y^2=x^3-27*I2*x-27*I1
#          isogenous to the verified models?  (2) empirical check of the
#          classical invariants->Jacobian formula on a test quartic.
import sys
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

def group_order(a2, a4, a6, p):
    # E: y^2 = x^3+a2 x^2+a4 x+a6 over F_p, brute force
    n = 1  # point at infinity
    for x in range(p):
        v = (x*x*x + a2*x*x + a4*x + a6) % p
        if v == 0: n += 1
        else:
            ls = pow(v, (p-1)//2, p)
            if ls == 1: n += 2
    return n

print("=== S1: Frobenius traces, Ẽ_A vs claimed Jacobian J_A ===")
# E~_A (verified isomorphic to E_A, j=-8000/81): y^2=x^3-256x^2+18432x
# claimed J_A: y^2 = x^3 - 27*I2 x - 27*I1 = x^3+240648192x-276480
for p in (7, 11, 13, 17, 19, 23, 29, 31):
    n1 = group_order(-256, 18432, 0, p)
    n2 = group_order(0, 240648192 % p, (-276480) % p, p)
    print("p=%2d  a_p(E~_A)=%3d   a_p(J_A)=%3d  %s" % (
        p, p+1-n1, p+1-n2, "SAME" if p+1-n1 == p+1-n2 else "DIFFER"))

print("=== S1b: Ẽ_B vs claimed J_B ===")
# E~_B: y^2=x^3+256x^2-2048x (j=2744000/9)
# claimed J_B: y^2 = x^3 - 27*(-38273024) x - 27*71680
for p in (5, 7, 11, 13, 17, 19, 23, 31):
    n1 = group_order(256, -2048, 0, p)
    n2 = group_order(0, 1033371648 % p, (-1935360) % p, p)
    print("p=%2d  a_p(E~_B)=%3d   a_p(J_B)=%3d  %s" % (
        p, p+1-n1, p+1-n2, "SAME" if p+1-n1 == p+1-n2 else "DIFFER"))

print("=== S2: generic quartic->Weierstrass vs classical formula ===")
import sympy as sp
Xq, xE, Xq2 = sp.symbols('Xq xE X2')
def generic_model(a, b, c, d, e, v0):
    # quartic V^2 = a X^4+b X^3+c X^2+d X+e, origin (0, v0), e = v0^2.
    # subst V = xE*X^2 + m*X + v0 with m = d/(2 v0); cancel known root,
    # remaining quadratic in X; its discriminant D(xE) is the Weierstrass cubic.
    m = sp.Rational(d, 1) / (2*v0)
    V = xE*Xq**2 + m*Xq + v0
    expr = sp.expand(V**2 - (a*Xq**4 + b*Xq**3 + c*Xq**2 + d*Xq + e))
    # Xq = 0 is a root; divide by Xq (twice if double)
    q, r = sp.div(sp.Poly(expr, Xq), sp.Poly(Xq, Xq))
    assert r.as_expr() == 0
    # factor out the root at Xq = 0 coming from the tangent double contact:
    # divide once more only if still divisible (pole cancellation point)
    if q.as_expr().subs(Xq, 0) == 0:
        q2, r2 = sp.div(q, sp.Poly(Xq, Xq))
        assert r2.as_expr() == 0
        q = q2
    poly = sp.Poly(q.as_expr(), Xq)
    c2, c1, c0 = poly.all_coeffs()
    D = sp.expand(sp.discriminant(poly.as_expr(), Xq))  # in xE
    D = sp.factor(D)
    return c2, c1, c0, D

def jinv(a2, a4, a6):
    from fractions import Fraction as F
    b2 = 4*a2; b4 = 2*a4; b6 = 4*a6; b8 = 4*a2*a6 - a4*a4
    c4 = b2*b2 - 24*b4; c6 = -b2**3 + 36*b2*b4 - 216*b6
    return F(1728)*c4**3/(c4**3 - c6**2)

# test quartic with rational point (0,1): v^2 = x^4+3x^3+5x^2+3x+1
c2, c1, c0, D = generic_model(1, 3, 5, 3, 1, 1)
print("test quartic: quad coeffs", c2, c1, c0)
print("  D(xE) =", D)
# extract Weierstrass y^2 = cubic by scaling xE -> k*x so leading coeff is 1:
# D(xE) = L*xE^3+... ; set x' = -2*... generic: y^2 = D(xE); scale to monic.
Dp = sp.Poly(D, xE)
coefs = Dp.all_coeffs()
L = coefs[0]
# y = L*YE, x = L*xE  =>  y^2 = L^2*YE^2 = L*D(xE) = L^3 xE^3+... = x^3+...
Ds = sp.Poly(sp.expand(L*D.as_expr().subs(xE, Xq2/L)), Xq2)
co = [sp.simplify(t) for t in Ds.all_coeffs()]
print("  scaled monic cubic: y^2 = x^3 + (%s) x^2 + (%s) x + (%s)" % tuple(co[1:]))
a2s, a4s, a6s = [int(t) for t in co[1:]]
j_gen = jinv(a2s, a4s, a6s)
print("  j(generic-method Jac) =", j_gen)
# classical formula: I=12ae-3bd+c^2, J=72ace+9bcd-27ad^2-27b^2e-2c^3
I = 12*1*1 - 3*3*3 + 25
J = 72*1*5*1 + 9*3*5*3 - 27*1*9 - 27*9*1 - 2*125
print("  I,J =", I, J, " claimed Jac y^2=x^3-27Jx-27I; j =", jinv(0, -27*J, -27*I))
print("  match:", j_gen == jinv(0, -27*J, -27*I))
# same on M_A for the record
c2, c1, c0, D = generic_model(1, 132, -250, 132, 1, 1)
Dp = sp.Poly(D, xE); L = Dp.all_coeffs()[0]
Ds = sp.Poly(sp.expand(L*D.as_expr().subs(xE, Xq2/L)), Xq2)
co = [int(sp.simplify(t)) for t in Ds.all_coeffs()]
print("M_A generic cubic: y^2 = x^3 + (%d) x^2 + (%d) x + (%d)" % tuple(co[1:]))
j_gen = jinv(co[1], co[2], co[3])
print("  j =", j_gen, " equals j(E_A)=-8000/81:", j_gen == F(-8000, 81))
c2, c1, c0, D = generic_model(9, -92, 310, -92, 9, 3)
Dp = sp.Poly(D, xE)
co0 = Dp.all_coeffs()
L = co0[0]
Ds = sp.Poly(sp.expand(L*D.as_expr().subs(xE, Xq2/L)), Xq2)
co = [int(sp.simplify(t)) for t in Ds.all_coeffs()]
print("M_B generic cubic: y^2 = x^3 + (%d) x^2 + (%d) x + (%d)" % tuple(co[1:]))
j_gen = jinv(co[1], co[2], co[3])
print("  j =", j_gen, " equals j(E_B)=2744000/9:", j_gen == F(2744000, 9))