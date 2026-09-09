#!/usr/bin/env python3
# image(alpha^L) for J_L^sh : y^2 = X^3 - 18288X^2 + 83589408X ; G^sh = (8568, 51408)
# Same group law but keep numbers small (the curve has smaller coefficients than E_a).
from fractions import Fraction as F
import math

a2, a4 = -18288, 83589408
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1==x2 and (y1+y2)==0: return None
    if P==Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*a2*x1 + a4)/(2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - a2 - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3,y3)
def mul(P,n):
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q)
        Q=add(Q,Q); n>>=1
    return R
T=(F(0),F(0)); G=(F(8568),F(51408))
assert G[1]*G[1] == G[0]**3 + a2*G[0]**2 + a4*G[0]

def sf(n):
    n=abs(n); out=1; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e%2: out*=d
        d+=1
    if n>1: out*=n
    return out
def sqclass(fr):
    s = -1 if fr<0 else 1
    return (s*sf(fr.numerator), sf(fr.denominator))

print("alpha^L(T) = a4-class:", sqclass(F(a4)))
print("alpha^L(G) :", sqclass(G[0]))
for m in (1,2,3):
    Q = mul(G,2*m)
    print(f"x({2*m}G) sqclass:", sqclass(Q[0]))
GT = add(G,T)
print("alpha^L(G+T):", sqclass(GT[0]))
print("a4*x(G):", sqclass(F(a4)*G[0]))
print("a4*x(G+T):", sqclass(F(a4)*GT[0]))