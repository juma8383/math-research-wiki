#!/usr/bin/env python3
# While the census grinds: the m=2 case detail — v7(s), v17(s) check and the
# exact-verification of the valuation lemma at the found admissible points.
from fractions import Fraction as F
import math
a2c, a4c = 32, 238
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1==x2 and (y1+y2)==0: return None
    if P==Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*a2c*x1 + a4c)/(2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - a2c - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3,y3)
def mul(P,n):
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q)
        Q=add(Q,Q); n>>=1
    return R
def vp(p, n):
    v = 0
    while n % p == 0: n //= p; v += 1
    return v
T=(F(0),F(0)); Pa=(F(-14),F(14))
print("empirical: v7(s), v17(s), v7(n), v17(n) at admissible m:")
for m in (2,8,10,16,18,24):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    X2 = PT[0]/238
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    r,s = rn,rd
    g0 = math.gcd(r,s); r//=g0; s//=g0
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    n = s**4 - 238*r**4
    print(f"m={m}: v7(s)={vp(7,s)} v17(s)={vp(17,s)} v7(n)={vp(7,n)} v17(n)={vp(17,n)} "
          f"v7(u)={vp(7,u)} v17(u)={vp(17,u)}")