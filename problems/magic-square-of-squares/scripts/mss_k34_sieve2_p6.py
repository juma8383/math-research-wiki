#!/usr/bin/env python
# K34 round 2, part 6: sibling cover D_B: w^2 = 9z^4-128z^2+512.
# (1) invariants match M_B (I1=71680, I2=-38273024);
# (2) C3_B correspondence (x,W)->(z,w)=(x+1/x,W/x^4);
# (3) z^2=u^2+4 form gives 9u^4-56u^2+144, and z^2=(X+1)^2/X so the extra
#     condition z^2-4=nonzero square <=> X nonzero rational square (same as A).
import sys
import sympy as sp
def out(*a): print(*a); sys.stdout.flush()
x,z,u,W = sp.symbols('x z u W')
fB = 9*z**4-128*z**2+512
I1 = 12*9*512 + (-128)**2
I2 = 72*9*(-128)*512 - 2*(-128)**3
out("D_B invariants: I1=%d (M_B 71680: %s)  I2=%d (M_B -38273024: %s)"%(I1,I1==71680,I2,I2==-38273024))
c3 = sp.expand(fB.subs(z,x+1/x)*x**4 - (9*x**8-92*x**6+310*x**4-92*x**2+9))
out("fB(x+1/x)*x^4 == C3_B octic:", sp.simplify(c3)==0)
out("fB(z^2=u^2+4) == 9u^4-56u^2+144:", sp.expand(fB.subs(z**2,u**2+4))-(9*u**4-56*u**2+144)==0)
# known point: z=2 -> w^2=9*16-512+512=144 -> w=+-12 (matches task brief)
out("fB(2)=%d (=12^2)"%fB.subs(z,2))
# z^2=(X+1)^2/X with X=x^2: square iff X square (X!=0) -- symbolic statement
out("z=x+1/x => z^2 = (x^2+1)^2/x^2; X=x^2 nonzero square <=> z^2 square (birational both ways)")