#!/usr/bin/env python3
# The two-parents structure at m=2 verified. Now the KEY structural question:
# does Parent A's Germain split (238 r^4, s^4) regenerate r,s themselves?
# YES trivially: the constants are the leaf's own cell. Parent A's Germain step
# returns (r,s,u) ITSELF (the split IS the fiber parametrization: 238r^4 * s^4
# with the completing square A = s^4+238r^4). So the Fermat loop from Parent A
# is IDENTITY, not halving! The halving happens on Parent B.
# => The K34-A chain structure: leaf point -> Parent A -> Germain split = itself
#    (fixed point!). The descent loop on the K34-A chain is TRIVIAL - the leaf
#    point IS its own Germain regeneration. No descent possible; no contradiction.
# This RESOLVES the §2j puzzle: the halving map was on the SHADOW chain (Parent B),
# not the K34-A chain.
#
# Now the lift on Parent A: n +- 2u rs = (a +- b)^2. At m=2: fails (n-2urs<0 even).
# n - 2urs < 0 always? n = s^4-238r^4, 2urs vs n: check sign condition.
# n > 2urs <=> s^4 - 238r^4 > 2rs*u.
# For the lift to hold with n-2uv >= 0 we need n >= 2urs.
# Check at m=2: n = 6.75e13, 2urs = 1.6e14 -> negative. FAILS BY SIGN.
# Question: is n >= 2urs possible for ANY admissible fiber point?
# n/(2urs) = (s^4-238r^4)/(2rs u). With X = s/r: = (s^3/r - 238r^3/s)/(2u) * ...
# Let me test the sign condition across admissible m exactly.
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
T=(F(0),F(0)); Pa=(F(-14),F(14))

print("m | admissible | n vs 2urs (sign of n-2urs)")
for m in (2,4,6,8,10,12,14,16,18,20):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    if PT is None: continue
    X2 = PT[0]/238
    if X2 <= 0: continue
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn!=nr or rd*rd!=dr: continue
    r,s = rn,rd
    g = math.gcd(r,s); r//=g; s//=g
    if not (r%6==0 and s%2==1 and s**4 > 238*r**4): continue
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    n = s**4 - 238*r**4
    two = 2*u*r*s
    print(f"{m} | YES | n-2urs = {n-two>0 and '+' or 'NEG'} (n={str(n)[:12]}..., 2urs={str(two)[:12]}...)")
    print(f"    ratio n/(2urs) = {float(F(n, two)):.6f}")
# X < 238^{-1/4} ~ 0.2546 means s > r/0.2546 = 3.93r roughly; n = s^4-238r^4 vs 2urs ~ 2s^2 u (r~small)
# u ~ s^2 for small X: u = sqrt(238r^4+32r^2s^2+s^4) ~ s^2(1+16r^2/s^2+...)
# n/(2urs) ~ (s^4 - 238r^4)/(2rs*s^2) = (s/r - 238 r^3/s^3)/(2) * (1/s^0)... 
# ~ s/(2r) * (1 - 238(X)^4...) -> large when s >> r. So for VERY small X, n > 2urs!
# X = r/s small: n/(2urs) ~ (s^4)/(2 r s s^2) = s/(2r) -> huge. So the sign CAN be positive.
# At m=2 X=852/3727=0.2286, s/(2r)=2.19, but 238r^4 term matters. Border: solve
# s^4 - 238 r^4 = 2 r s u -> in X: (1 - 238X^4) = 2X*sqrt(238X^4+32X^2+1)
# solve: 1 - 238X^4 = 2X sqrt(1+32X^2+238X^4). Square: (1-238X^4)^2 = 4X^2(1+32X^2+238X^4)
# Let me solve numerically:
def f(X):
    return (1-238*X**4)**2 - 4*X*X*(1+32*X*X+238*X**4)
# binary search for root in (0, 0.2546)
lo, hi = 0.0, 0.2546
for _ in range(60):
    mid = (lo+hi)/2
    if f(mid) > 0: lo = mid
    else: hi = mid
print(f"\nroot X* = {lo:.6f}; n>2urs iff X < X* (approx)")
print(f"238^(-1/4) = {238**-0.25:.6f}")
print(f"At m=2: X = {852/3727:.6f} -> n-2urs {'>' if f(852/3727)>0 else '<'} 0")