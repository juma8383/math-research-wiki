from fractions import Fraction as F
import math

# E_a : y^2 = x^3 + 32 x^2 + 238 x ; P_a = (-14, 14), T_a = (0,0), rank 1 (mwrank)
A2, A4 = 32, 238
def on_E(P):
    x,y = P
    return y*y == x**3 + A2*x*x + A4*x
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1==x2 and (y1+y2)==0: return None
    if P==Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*A2*x1 + A4)/(2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - A2 - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3,y3)
def mul(P,n):
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q)
        Q=add(Q,Q); n>>=1
    return R

T=(F(0),F(0)); Pa=(F(-14),F(14))
# verify: 2Pa = (9/4, ?)  -> X(2Pa) via quartic map = (1/2)*x(2Pa) = 9/8?
Q2 = mul(Pa,2)
print("2Pa =", Q2)
# quartic X for point 2Pa: X^2 = x(2Pa)/2 = (9/4)/2 = 9/8 -> not a square -> NOT a quartic fiber point
# The quartic map: quartic pt (X,y) -> (d X^2, d X y). Image point = T_a + (point in <2E_a>? no:)
# The image of C_d under the map is exactly the set of points whose x/d is a square... 
# For d=238: image = alpha^{-1}(class 238) = {T_a + 2E_a(Q)} = T_a + 2E(Q) 
# (since beta(Q) = 1 for all Q in E_a: x(2Q) square, verified below for several)
for m in range(1,6):
    R = mul(Pa, 2*m)
    print(f"x({2*m}Pa) square? {str(R[0].numerator < 10**9 and math.isqrt(R[0].numerator)**2==R[0].numerator and math.isqrt(R[0].denominator)**2==R[0].denominator)}  ({str(R[0])[:40]})")
# So alpha^{-1}(238) = T_a + 2E_a(Q) = {T_a + 2m Pa + t T_a}? T_a is killed mod phi:
# image(alpha) = <238, -14> with kernel = 2E_a + <T_a>? Let's verify: E_a/2E_a + <T> has order 4;
# alpha(T)=238, alpha(Pa)=-14 -> all four classes realized: 1=alpha(2Pa), 238=alpha(T),
# -14=alpha(Pa), -3332=alpha(Pa+T). Kernel of alpha = 2E_a(Q) (index 4 => [E:2E]=4 -> kernel exactly 2E_a).
print()
print("kernel(alpha) = 2E_a(Q); image(alpha) = {1,238,-14,-3332}")
print("alpha(Pa+T) =", add(Pa,T)[0])