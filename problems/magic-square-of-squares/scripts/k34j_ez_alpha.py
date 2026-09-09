#!/usr/bin/env python3
# E_Z rank 1 (candidate G=(64,2112), torsion Z/2 T=(0,0)) — same shape AGAIN.
# The tower question on E_Z: x(E_Z) = 8 * square (with x=8x_C1... wait recheck:
# x(E_Z) = 8 w^2 where the C1 point has x_C1 = w^2. So x(E_Z) = 8x_C1 = 8w^2.
# Condition: x(E_Z)/8 = w^2 a nonzero square.
# alpha-style: x(E_Z) = 8*w^2 => x(E_Z) has square class 8 (2*4 = 2-class: sqclass(8)=2).
# E_Z has rational 2-torsion T=(0,0): alpha_Ez(P) = x(P) mod squares.
# alpha(T) = a4 = 576 = 24^2 => sqclass 1! Interesting: alpha(T)=1.
# A point with x = 8*square: x-class 2 (sqclass(8) = 2).
# So the tower question: is class 2 in image(alpha_Ez)? Compute:
# alpha(2mG) = 1-class (duplication); alpha(T) = 576-class = 1;
# alpha(G): x = 64 => sqclass(64) = 1!! G=(64,2112): x(G)=64=8^2 -> alpha(G)=1!
# => image(alpha_Ez) = {1}?? Then EVERY point has x = square-class 1?! No wait:
# alpha is a homomorphism to Q*/Q*2; image = {alpha(T), alpha(G)}-generated =
# {1, 1} = {1}. That would mean x(P) is ALWAYS a square class... but x(3G) etc
# must then all be square classes. Check: G=(64,2112); 2G = ? Compute and see.
# If image(alpha_Ez) = {1} exactly, the class-2 fiber (x=8*square) is EMPTY
# unless 8 ≡ 1 mod squares — 8 is not a square. x(P)=8w^2 needs class 8;
# class 8 = class 2 (8 = 2*2^2). If image = {1}, NO point has x of class 2:
# the TOWER CLOSES AT HEIGHT 1! Verify image(alpha_Ez) carefully via mwrank
# (which just started) + exact point checks.
from fractions import Fraction as F
import math
a2, a4 = 1016, 576
def on(x,y): return y*y == x**3 + a2*x*x + a4*x
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
    return s*sf(fr.numerator)*sf(fr.denominator)
T=(F(0),F(0)); G=(F(64),F(2112))
assert on(*T) and on(*G)
print("E_Z: T=(0,0) [order 2], G=(64,2112).")
print("alpha(T) = sqclass(a4=576):", sqclass(F(576)))
print("alpha(G) = x(G)=64 sqclass:", sqclass(F(64)))
for m in (1,2,3):
    Q = mul(G,2*m)
    print(f"x({2*m}G) = {str(Q[0])[:20]} sqclass {sqclass(Q[0])}")
GT = add(G,T)
print("x(G+T) =", GT[0], " sqclass:", sqclass(GT[0]))
print("x(G)/... G+T = (b/x, -b y/x^2) formula: x = 576/64 = 9: sqclass:", sqclass(F(9)))
print("\nimage(alpha_Ez) = <sqclass(576)=1, sqclass(64)=1> = {1}!!")
print("=> EVERY rational point on E_Z has x of square class 1.")
print("=> the class-2 fiber (x = 8*square, i.e. class 2) is EMPTY:")
print("=> NO point on E_Z has x(E_Z) = 8*w^2 with w ≠ 0.")
print("=> C1 has NO square-x point except possibly x=0 (degenerate).")
print("=> THE TOWER CLOSES AT HEIGHT 1: C1 has no square-x point. The lift gate")
print("   fails for every fiber point -- IF image(alpha_Ez)={1} holds rigorously")
print("   (needs mwrank: rank, torsion, and the alpha-image computation).")