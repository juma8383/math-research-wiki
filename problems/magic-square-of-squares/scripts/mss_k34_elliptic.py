#!/usr/bin/env python
# K34 as rational points on genus-1 quartics M_A, M_B.
# Part 1: re-verify the reduction A(n)=[] <=> M_A point with X=(a/b)^2.
import sys, math
from fractions import Fraction as F

def out(*a):
    print(*a); sys.stdout.flush()

def is_square(n):
    if n < 0: return False
    r = math.isqrt(n)
    return r*r == n

def rep(n):
    # a^2+b^2=n, a>b>0
    for aa in range(math.isqrt(n), 0, -1):
        r = n - aa*aa
        if r > 0 and is_square(r):
            bb = math.isqrt(r)
            if aa > bb > 0: return aa, bb
    return None

# ---- symbolic check of the quartic identities (sympy) ----
import sympy as sp
u, X, w, x = sp.symbols('u X w x')
QA = u**4 + 136*u**2 + 16
QB = 9*u**4 - 56*u**2 + 144
# u = x - 1/x ; u^2 = x^2 - 2 + 1/x^2
def sub_u(poly):
    return sp.expand(poly.subs(u, x - 1/x) * x**4)
sA = sp.expand(sub_u(QA) - (x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1))
sB = sp.expand(sub_u(QB) - (9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9))
out("sym: QA*(x^4) - P_A(x^2) ==", sA)
out("sym: QB*(x^4) - P_B(x^2) ==", sB)
# A(n) = t^4*QA(u); t^4 = (ab)^4 = (ab)^4. With X=(a/b)^2:
# (V)^2 = t^4 QA(u)  <=>  (V b^4)^2 = b^8 QA(u) = P_A(X) with X=(a/b)^2.
# i.e. A(n) square <=> P_A(X) square * b^8 scaling. Verify:
a, b = sp.symbols('a b')
sa, sb = a**2 - b**2, a*b
ua = sa/sb   # u = s/t = x - 1/x
out("sym: t^4*QA - (a^8+132a^6b^2-250a^4b^4+132a^2b^6+b^8) ==",
    sp.simplify(sp.together(sp.expand((ua**4+136*ua**2+16)*(a*b)**4) -
        (a**8+132*a**6*b**2-250*a**4*b**4+132*a**2*b**6+b**8))))
out("sym: t^4*QB - (9a^8-92a^6b^2+310a^4b^4-92a^2b^6+9b^8) ==",
    sp.simplify(sp.together(sp.expand((9*ua**4-56*ua**2+144)*(a*b)**4) -
        (9*a**8-92*a**6*b**2+310*a**4*b**4-92*a**2*b**6+9*b**8))))