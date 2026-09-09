#!/usr/bin/env python3
# Verify the duplication formula discrepancy and nail the four alpha^L classes.
from fractions import Fraction as F
import math

a2, a4 = -18288, 83589408
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

x, y = F(8568), F(51408)
# group-law doubling (trusted)
lam = (3*x*x + 2*a2*x + a4)/(2*y)
x3 = lam*lam - a2 - x
y3 = lam*(x - x3) - y
print("2G =", (x3, y3))
# check on curve
print("on curve:", y3*y3 == x3**3 + a2*x3**2 + a4*x3)
print("x(2G) sqclass:", sqclass(x3))
# the wrong 'formula' gave 9801 (sqclass 1) vs true 18369: which is right? verify both
for cand in (x3, F(9801)):
    ok = (cand**3 + a2*cand**2 + a4*cand)
    # find y: is there y with y^2 = rhs and consistent?
    print(cand, "-> rhs", cand**3 + a2*cand**2 + a4*cand, "square?", end=" ")
    r = cand**3 + a2*cand**2 + a4*cand
    print(r >= 0 and math.isqrt(r.numerator)**2 == r.numerator and math.isqrt(r.denominator)**2 == r.denominator)
# G+T = (b/x, -b y / x^2)
xGT = F(a4)/x
yGT = -F(a4)*y/(x*x)
print("G+T on curve:", yGT := yGT if False else None) if False else None
print("G+T check:", yGT if False else (yGT := None))
rhs = xGT**3 + a2*xGT**2 + a4*xGT
print("x(G+T) =", xGT, " y^2 should be", yGT if False else -F(a4)*y/(x*x), "^2 =", (F(a4)*y/(x*x))**2)
print("  rhs:", rhs, " match:", (F(a4)*y/(x*x))**2 == rhs)
print("sqclass x(G+T):", sqclass(xGT))
# ALSO: x(G+T) = b/x => sqclass = sqclass(b)/sqclass(x) = 64498/238 = 271 (since 64498 = 238*271)
print("64498 = 238*271?", 238*271 == 64498)
print("\n== THE FOUR REALIZED CLASSES ==")
print("1 (from 2E), 64498 (=alpha(T)), 238 (=alpha(G)), 271 (=alpha(G+T)=64498/238)")
print("\nD's quartic point classes needed: does D have a point with X = x(G)/... ?")
print("The class-238 fiber of alpha^L contains G; the class-271 fiber contains G+T.")
# KEY: which class does the D-quartic (V^2=N(x), x in square-classes) correspond to?
# The lift quartic D came from x = (s/r)^2 with N((s/r)^2) = square*r^(-8)-class.
# The alpha^L-preimage structure: D point (x,V) -> (V^2...,) map to J_L^sh?
# D(x) at its degenerate point x=0: V=238 -> which point? x=0 on the quartic maps to T
# under (X,Y)=(0... ) analogous: quartic->cubic map for y^2=x^3+ax^2+bx quartic V^2=N?