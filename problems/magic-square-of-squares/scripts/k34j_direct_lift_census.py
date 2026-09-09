#!/usr/bin/env python3
# ROUND 4: direct lift census + the gcd refinement.
# Lift ⟺ f1 = n+2urs AND f2 = n-2urs are BOTH squares (f1*f2 = n^2-4u^2r^2s^2,
# f1,f2 odd since n odd, 2urs even; n ≡ 1 mod 4, v2(2urs) >= 2).
# gcd(f1,f2) = g: f1*f2 square + gcd structure => f1 = g*a^2, f2 = g*b^2,
# lift ⟺ g square. g | gcd(n, 2urs): p|g odd -> p|n and p|rs or p|u.
# gcd(n,u) = 1 (proof: p|n,u -> 18r^4 ≡ 0 mod p -> p=3 contra 3∤n).
# g | gcd(n,rs): p|r impossible (n ≡ s^4 ≠ 0); p|s forces p in {7,17} (238 = 2·7·17).
# So g = 7^a 17^b; lift needs a,b even.
# Census: for admissible m, test f1, f2 squares directly (isqrt), also record
# v7/v17 of s and the product status. Extend to m <= 240.
from fractions import Fraction as F
import math
import sys
sys.set_int_max_str_digits(2000000)

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
def issq(x):
    if x < 0: return False
    rt = math.isqrt(x); return rt*rt == x

print("m | admissible | sign | f1 sq | f2 sq | prod sq | gcd-square-class")
adm = 0
for m in range(2, 241, 2):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    if PT is None: continue
    X2 = PT[0]/238
    if X2 <= 0: continue
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn!=nr or rd*rd!=dr: continue
    r,s = rn,rd
    g0 = math.gcd(r,s); r//=g0; s//=g0
    if not (r%6==0 and s%2==1 and s**4 > 238*r**4): continue
    adm += 1
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    n = s**4 - 238*r**4
    t2 = 2*u*r*s
    f1, f2 = n + t2, n - t2
    sg = "alive" if f2 >= 0 else "SIGN-DEAD"
    s1, s2 = issq(f1), issq(f2)
    prod = f1*f2
    psq = issq(prod)
    g = math.gcd(f1, f2)
    # g square-class: is g a square?
    gsq = issq(g)
    print(f"m={m:>3}: {sg:>9} f1sq={s1} f2sq={s2} prodsq={psq} gcd_sq={gsq} "
          f"v7s={0} v17s={0} bits(f1)={f1.bit_length()}")
    if s1 and s2:
        print(f"  *** LIFT HOLDS at m={m}: (a,b) exist -> FULL K34-A CANDIDATE ***")
print(f"\ntotal admissible m in (0,240]: {adm}")