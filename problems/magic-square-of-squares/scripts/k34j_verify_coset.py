#!/usr/bin/env python3
# Exact verification of the shared-Jacobian structure of the four K34 leaf quartics.
# E_a : y^2 = x^3 + 32x^2 + 238x   (2-isogenous to master E_mw)
# Leaf quartics C_d : y^2 = d*X^4 + 32*X^2 + 238/d  (ae = 238 family), d in {238,-119,17,-34}
# map: (X,y) -> (d*X^2, d*X*y) in E_a ; quartic point (r,s,u): X=r/s, y=u/s^2.
from fractions import Fraction as F
import math

A2, A4 = 32, 238
B = A4  # b = 238

def on_E(P):
    x, y = P
    return y*y == x**3 + A2*x*x + A4*x

def neg(P): return (P[0], -P[1])

def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1 == x2 and (y1+y2) == 0: return None
    if P is Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*A2*x1 + A4) / (2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - A2 - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3, y3)

def mul(P, n):
    R = None; Q = P
    while n:
        if n & 1: R = add(R, Q)
        Q = add(Q, Q); n >>= 1
    return R

T = (F(0), F(0))
Pa = (F(-14), F(14))
assert on_E(T) and on_E(Pa)
print("T=(0,0), P=(-14,14) on E_a: OK")

def xclass(fr):
    # square class of a rational (as (num,den) mod squares, sign kept)
    return (fr.numerator, fr.denominator)

def issq_rat(fr):
    if fr < 0: return False
    n, d = fr.numerator, fr.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return rn*rn == n and rd*rd == d

print("\n== x-classes of the small coset points ==")
pts = {}
for m in range(0, 8):
    for sgn in ([1] if m == 0 else [1, -1]):
        Q = mul(Pa, 2*m) if m else None
        if sgn < 0 and m: Q = neg(Q)
        P = add(Q, T) if Q else T
        if P is None:
            print(f"m={m:+d}: T+{2*m}P = O (infinity)")
            continue
        x = P[0]
        print(f"m={m:+d}: x(T+{2*m}P) = {x}   x(2mP) = {mul(P,1) if False else (add(Q,T) and '') or ''}", end="")
        # also x(2mP) itself:
        if Q is not None:
            print(f"  [x(2mP) = {Q[0]}]")
        else:
            print()

# Verify the duplication identity x(2P) = (x^2-b)^2 / (4x(x^2+ax+b)) mod squares
print("\n== beta(2P) == 1 check (x(2P) is a square times ...) ==")
for m in range(1, 5):
    Q = mul(Pa, 2*m)
    x2 = Q[0]
    # predicted: x(2mP) ≡ square  (beta of any 2E point is 1)
    print(f"x({2*m}P) = {x2}  -> square? {issq_rat(x2)}")

print("\n== the candidate quartic points from the class-238 fiber ==")
# class-238 points: P = T + Q with x(Q) a square (beta(Q)=1) -> quartic X^2 = x(P)/238
for m in range(0, 7):
    Q = mul(Pa, 2*m)
    P = add(Q, T) if Q else T
    if P is None: continue
    xP = P[0]
    X2 = xP / 238
    if X2 > 0 and issq_rat(X2):
        # X = r/s in lowest terms
        rt = issq_rat and math.isqrt(X2.numerator), math.isqrt(X2.denominator)
        rnum = math.isqrt(X2.numerator); rden = math.isqrt(X2.denominator)
        g = math.gcd(rnum, rden)
        rnum //= g; rden //= g
        # u^2 = 238 r^4 + 32 r^2 s^2 + s^4
        u2 = 238*rnum**4 + 32*rnum**2*rden**2 + rden**4
        usq = issq_rat(F(u2))
        admissible = (rnum % 2 == 0) and (rden % 2 == 1) and (rnum % 3 == 0) and (abs(F(rnum,rden)) < F(1,1)/ (238**0.25 if False else 1) or True)
        print(f"m={m}: X^2 = {X2} = ({rnum}/{rden})^2 ; u^2 = {u2} square? {usq}; "
              f"r even {rnum%2==0}, s odd {rden%2==1}, 3|r {rnum%3==0}, |X|={abs(float(F(rnum,rden))):.4f} vs 238^-1/4={238**-0.25:.4f}")