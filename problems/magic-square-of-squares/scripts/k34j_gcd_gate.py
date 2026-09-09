#!/usr/bin/env python3
# While the census runs: theory work. The gcd refinement lemma, stated properly.
# Claim: f1*f2 square AND f1 = g*a^2, f2 = g*b^2 with the SAME squarefree g.
# If additionally g is a square, both f1, f2 are squares: LIFT.
# g | 2^{v2} * 7^a * 17^b (odd part); f1, f2 both odd => g odd => g = 7^a 17^b.
# But WAIT: is g | rs needed? p | f1, f2 => p | f1+f2 = 2n and p | f1-f2 = 4urs.
# p odd: p | n and p | urs. gcd(n,u)=1, gcd(n,r)=1 (n ≡ s^4 mod r since 238r^4...).
#   p|r: n = s^4-238r^4 ≡ s^4 mod p, p|r, gcd(r,s)=1 => s^4 ≠ 0 mod p => p ∤ n. Contradiction.
#   p|s: n ≡ -238r^4 mod p => p | 238 => p in {7, 17}.
# So g = 7^a 17^b, EXACTLY. And the lift requires g square (a, b even).
# NEW PROVABLE GATE (the 7-17 gate): if 7 ∤ s and 17 ∤ s then g = 1 (square!) =>
# the D-gate (product square) becomes SUFFICIENT on those fibers.
# Conversely if v7(s) or v17(s) is odd, g is nonsquare and the product CAN be
# square without a lift. So: for s not divisible by 7 or 17, product-square ⟺ lift.
# Which admissible fiber points have 7|s or 17|s? Census that too.
# ALSO: the wiki's delta lemma says gcd = 2^j for the (a,b) split — but that was
# for gcd((X-n)/2, (X+n)/2) with X = R (the 238-split world). Here f1, f2 are
# odd, so no 2-part; consistent.
print("== 7-17 gate: the squarefree kernel of g is 7^a 17^b ==")
print("lift ⟺ f1*f2 square AND g square; g = 7^v7(s-ish) 17^v17(s-ish) structure")
print("if 7∤s and 17∤s: g=1 (odd case) -> product-square ⟺ LIFT (sufficiency!)")
print()
# Now verify at m=8 (alive, product not square): the D-gate failure is decisive
# there IF 7∤s, 17∤s. Check v7, v17 of s at the admissible m values:
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
def vp(p, n):
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

for m in (8, 10, 16, 18, 24, 26):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    X2 = PT[0]/238
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    r,s = rn,rd
    g0 = math.gcd(r,s); r//=g0; s//=g0
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    n = s**4 - 238*r**4
    t2 = 2*u*r*s
    f1, f2 = n + t2, n - t2
    g = math.gcd(f1, f2)
    print(f"m={m}: v7(s)={vp(7,s)} v17(s)={vp(17,s)} gcd(f1,f2)={str(g)[:15]}... "
          f"gcd sq? {math.isqrt(g)**2==g}, 7|g {g%7==0}, 17|g {g%17==0}")