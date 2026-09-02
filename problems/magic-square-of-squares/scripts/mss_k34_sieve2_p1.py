#!/usr/bin/env python
# K34 round 2, part 1 (final): sibling cover D_A: w^2 = z^4+128z^2-512.
# (1) invariants I1,I2 match M_A (same Jacobian class E_A);
# (2) equivalence: K34-A counterexample <=> D_A(Q) point with z^2-4 = nonzero
#     rational square (z = n/t = (a^2+b^2)/(ab), z^2-4 = (s/t)^2, x=(z+u)/2);
# (3) the C3_A correspondence: (x,W) -> (z,w) = (x+1/x, W/x^2) and
#     C3_A -> M_A: (x,W)->(x^2,W); so (2,4) <-> M_A(1,4) and (2,-4) <-> (1,-4),
#     hence image classes -G_A and -G_A+T_A under the M_A identification;
# (4) the tangent-method discriminant cubic for D_A is a NONTRIVIAL twist of
#     E_A (no rational isomorphism: a2/a4 matching forces sigma^2=1/16 but the
#     a6 equation fails) -- recorded as the twist subtlety p11 had (j-only).
# (5) third quotient D'_A: w^2 = u^4+136u^2+16 (u = x-1/x), condition u^2+4=□.
import sys
from fractions import Fraction as F
import sympy as sp
def out(*a): print(*a); sys.stdout.flush()

z,w,u,x = sp.symbols('z w u x', real=True)
fD = z**4+128*z**2-512
I1 = sp.expand(12*1*(-512) + 128**2)
I2 = sp.expand(72*128*(-512) - 2*128**3)
out("D_A invariants: I1=%s I2=%s  (M_A: 10240, -8912896) match: %s"%(I1,I2,(I1,I2)==(10240,-8912896)))

# (2) equivalence: given z^2-4=u^2 (u != 0), set x=(z+u)/2; then
#   x+1/x = z and X=x^2, V=w*x^2 satisfy V^2 = X^4+132X^3-250X^2+132X+1.
zz = sp.symbols('ZZ')
# z = x+1/x  =>  z^2-4 = (x-1/x)^2 ; w = W/x^2 with W^2=f(x^2)
fM = x**8+132*x**6-250*x**4+132*x**2+1
chk1 = sp.expand(fD.subs(z, x+1/x)*x**4 - (x**8+132*x**6-250*x**4+132*x**2+1))
out("D_A(z=x+1/x)*x^4 == C3_A(x):", sp.simplify(chk1) if False else sp.simplify(fD.subs(z,x+1/x)*x**4 - (x**8+132*x**6-250*x**4+132*x**2+1))==0)
# and the u-form: z^2 = u^2+4 -> w^2 = (u^2+4)^2+128(u^2+4)-512 = u^4+136u^2+16
chk2 = sp.simplify(fD.subs(z, sp.sqrt(u**2+4)) - (u**4+136*u**2+16))
out("D_A(z) with z^2=u^2+4 equals u^4+136u^2+16 (K34-A quartic): %s"%(
    sp.simplify((fD.subs(z**2, u**2+4)) - (u**4+136*u**2+16))==0))
# conversely D_A point + z^2-4=u^2 -> x=(z+u)/2 on C3_A:
chk3 = sp.simplify((fD.subs(z, (u**2+4+sp.sign(0)*0+ (u**2+4))/1) if False else
        fD.subs(z, sp.Symbol('s2')/2 + sp.Symbol('s2')/2) ))
# direct: z=(r+4/r)/2 with r=2x: check fD((r^2+4)/(2r)) * (2r)^4 = (r^8+132r^4... )
r = sp.symbols('r')
zr = (r**2+4)/(2*r)
expr = sp.expand(fD.subs(z, zr)*(2*r)**4)
out("fD((r^2+4)/(2r))*(2r)^4 factors as:", sp.factor(expr))