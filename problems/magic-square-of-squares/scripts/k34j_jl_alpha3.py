#!/usr/bin/env python3
# image(alpha^L) with capped arithmetic: only m<=2 needed for the four classes.
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

T=(F(0),F(0)); G=(F(8568),F(51408))
print("alpha^L(T) = a4-class:", sqclass(F(a4)))
print("alpha^L(G):", sqclass(G[0]))
# 2G via the duplication formula (no group law needed):
# x(2Q) = (x^2 - a4class)^2 / (4y^2)... general: x(2Q)=(x^2-a)^2-8bx / (4(x^3+ax^2+bx)) for y^2=x^3+ax^2+bx
x, y = G[0], G[1]
num = (x*x - a4)*(x*x - a4) - 8*a2*x*x*x if False else 0
# correct duplication for y^2 = x^3 + a x^2 + b x:
# x(2Q) = (x^2 - b)^2 / (4(x^3 + a x^2 + b x))   -- since (x^2-b)^2 - ... let me verify numerically
den = 4*(x**3 + a2*x*x + a4*x)
x2 = (x*x - a4)**2 / den
print("x(2G) via formula:", x2)
# verify via y: y(2Q) computed from slope: lam = (3x^2+2ax+b)/(2y); then standard
lam = (3*x*x + 2*a2*x + a4)/(2*y)
x3 = lam*lam - a2 - x
y3 = lam*(x - x3) - y
print("x(2G) via group law:", x3, " match:", x3 == x2)
print("x(2G) sqclass:", sqclass(x2))
print("alpha^L(G+T): x(G)+... G+T: x = (y^2... ) use formula x(P+T): y(P)^2 / x(P)^2 *? ")
# For T=(0,0): P+T = (b/x(P), -b y(P)/x(P)^2) -> x(P+T) = b/x(P)
xGT = F(a4)/x
print("x(G+T) =", xGT, " sqclass:", sqclass(xGT))