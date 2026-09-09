#!/usr/bin/env python3
# EXACT verification: the three leaf quartics C_{-119}, C_{17}, C_{-34} are insoluble
# iff image(alpha) = {1, 238, -14, -17} for E_a : y^2 = x^3+32x^2+238x.
# Everything in exact rational/integer arithmetic.
from fractions import Fraction as F
import math

A2, A4 = 32, 238

def on_E(P):
    x, y = P
    return y*y == x**3 + A2*x*x + A4*x

def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1 == x2 and (y1+y2) == 0: return None
    if P == Q or (x1==x2 and y1==y2):
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

T = (F(0), F(0)); P = (F(-14), F(14))
assert on_E(T) and on_E(P)

def sqclass(fr):
    """square class representative: (sign * squarefree(num), squarefree(den)) as (num,den) with 4th-power-free extraction"""
    def sf(n):
        n = abs(n); out = 1; d = 2
        while d*d <= n:
            e = 0
            while n % d == 0: n //= d; e += 1
            if e % 2: out *= d
            d += 1
        if n > 1: out *= n
        return out
    s = -1 if fr < 0 else 1
    return (s * sf(fr.numerator), sf(fr.denominator))

def issq_int(n):
    if n < 0: return False
    r = math.isqrt(n); return r*r == n

print("== 1. image(alpha) generators ==")
xP = P[0]; xPT = add(P,T)[0]
print("x(P_a) =", xP, "  sqclass:", sqclass(xP))
print("x(P_a+T_a) =", xPT := add(P,T)[0], "  sqclass:", sqclass(xPT))
print("alpha(T_a) = 238 (b-coefficient)")
print("image(alpha) = <{238},{-14}> = {1, 238, -14, -3332(=-17)}")

print("\n== 2. leaf square-classes vs image(alpha) ==")
img = {(1,1), (238,1), (-14,1), (-17,1)}   # (-17 = -3332 class)
leaves = {
  "C_238  (Q-pos-(238,1))": 238,
  "C_-119 (Q-neg-(119,2))": -119,
  "C_17   (N-pos-(17,14))": 17,
  "C_-34  (N-neg-(34,7))": -34,
}
for nm, d in leaves.items():
    cls = sqclass(F(d))
    soluble = cls in img
    print(f"{nm}: sqclass {cls}  in image(alpha)? {soluble}  -> C_d {'SOLUBLE' if soluble else 'INSOLUBLE (no rational points)'}")

print("\n== 3. exact check of the known quartic points ==")
# C_238: (X,y') = (0,1) [from T_a] and (2/3, 71/9) [from T+2P]
for (X, yv, src) in [(F(0), F(1), "T_a"), (F(2,3), F(71,9), "T_a+2P")]:
    lhs = yv*yv; rhs = 238*X**4 + 32*X*X + 1
    print(f"C_238 point (X={X}, y={yv}) from {src}: {lhs} == {rhs} ? {lhs==rhs}")
# C_1 (trivial class): (3/2, 71/4) from 2P
X, yv = F(3,2), F(71,4)
print(f"C_1 point (X={X}, y={yv}) from 2P: {yv*yv} == {X**4+32*X*X+238} ? {yv*yv == X**4+32*X*X+238}")

print("\n== 4. the admissible C_238 point from T_a+4P: (r,s,u) with X=r/s ==")
m = 2
Q = mul(P, 2*m)
PT = add(Q, T)
xPT = PT[0]
X2 = xPT / 238
assert issq_int(X2.numerator) and issq_int(X2.denominator)
r, s = math.isqrt(X2.numerator), math.isqrt(X2.denominator)
g = math.gcd(r, s); r //= g; s //= g
u2 = 238*r**4 + 32*r*r*s*s + s**4
print(f"X = {r}/{s};  u^2 = {u2};  u = {math.isqrt(u2)} (exact square: {issq_int(u2)})")
print(f"conditions: r even {r%2==0}, 3|r {r%3==0}, s odd {s%2==1}, gcd(r,s)={math.gcd(r,s)}, "
      f"s^4>238r^4 {s**4 > 238*r**4}")
n = s**4 - 238*r**4
print(f"n = s^4-238r^4 = {n},  n mod 4 = {n%4}, 3|n? {n%3==0}")

print("\n== 5. completing-square split for this leaf solution ==")
s2p = s*s + 16*r*r
u = math.isqrt(u2)
Fm, Fp = s2p - u, s2p + u
assert Fm * Fp == 18 * r**4, "completing-square identity"
h2, hp = Fm//2, Fp//2   # both even? Fm,Fp parity:
print(f"F_- = {Fm}, F_+ = {Fp};  (F_-/2)*(F_+/2) = {h2*hp}  vs 72*(r/2)^4 = {72*(r//2)**4}  equal? {h2*hp == 72*(r//2)**4}")
gg = math.gcd(h2, hp)
print(f"gcd(F_-/2, F_+/2) = {gg}")
print(f"F_-/2 = {h2} = {factorint_str(h2) if False else ''}", end="")
def pf(n):
    fs = []; d = 2
    while d*d <= n:
        e = 0
        while n % d == 0: n //= d; e += 1
        if e: fs.append((d, e))
        d += 1
    if n > 1: fs.append((n, 1))
    return " * ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in fs)
print(pf(h2), "   F_+/2 =", pf(hp))