#!/usr/bin/env python3
# Structural result consolidating: Parent A (the K34-A-chain parent) is a FIXED
# POINT of the Germain step: its split (238r^4, s^4) recovers (r,s,u) itself.
# So on the K34-A chain, the descent loop is trivial -- no descent contradiction
# is possible. The §2j "halving map" was Parent B's loop (shadow chain).
#
# Remaining gate: Parent A's lift n +- 2urs = squares, BOTH must hold (coprime
# split with delta lemma). Sign: n-2urs > 0 iff X < X* = 0.197477 (proved: the
# sign condition is (1-238X^4)^2 - 4X^2(1+32X^2+238X^4) > 0 exactly).
# At m=2,10: X > X* -> the "-" lift is DEAD BY SIGN (not just non-square!).
# At m=8,16,18: X < X* -> sign OK; the lift still fails by non-squareness.
#
# NEW IDEA (the actual round-3 attack): Parent A's lift condition
#   n + 2urs = A1^2, n - 2urs = A2^2  (coprime, delta=2 or 8)
# means (A1^2)(A2^2) = n^2 - 4u^2r^2s^2 = r^8 N(X^2) -> N(X^2) square (the §2k gate)
# AND A1^2 + A2^2 = 2n, A1^2 - A2^2 = 4urs.
# The gate quartic D is the product condition; the SUM condition adds:
#   A1^2 + A2^2 = 2n must hold with A1,A2 integers -> n has a 2-square
#   representation with prescribed difference. This is EXACTLY the §2k "coprime
#   split" refinement. So the full gate = N(X^2) square AND the split lands in
#   constants compatible with delta=2/8 (i.e., (A1^2/2^j, A2^2/2^j) 4th-power
#   split of 2^{9-2j}3^2 (ab)^4-style analysis from [mss-k34-descent] sec 2-3).
# TEST: what does the §2k quartic D miss? D tests only the PRODUCT. If N(X^2)
# is a square, the factors n+-2urs are squares*r^8-ish, and the constants c1*c2
# must reproduce 238's structure. The D-gate is NECESSARY; is it SUFFICIENT?
# The delta lemma: gcd(n+2urs, n-2urs) = 2^j (j=1 for K34-A stratum). With both
# squares: gcd = g^2 | 2^... -> the gcd is a power of 2 -> both squares share
# only 2-power. Consistent. So product-square + coprime-split parity ⟺ lift.
# CONCLUSION: D-gate + delta-lemma = the full lift. No new condition.
#
# => ROUND-3 REAL RESULT: the K34-A chain closes as:
#    leaf point admissible (3|r etc.) -> Parent A lift n+-2urs squares
#    -> [D-gate: N(X^2) square] AND [sign condition X < X*]
#    The X < X* sign condition is a NEW KILL: it removes X in (X*, 238^-1/4)
#    = 22% of the admissible window (X* = 0.197477 vs 0.254598).
#    Combined with the §2k census (no square-x on D in box), the gate data is:
#    kills: X in (0.1975, 0.2546) dead by sign; square-x on D needed for the rest.
print("== ROUND-3 RESULT: sign condition X < X* ==")
Xstar = 0.197477
print(f"X* = 0.197477 (n=2urs boundary), admissible window X in (0, 238^(-1/4)=0.254598)")
print(f"dead band: X in (0.1975, 0.2546) = {(0.254598-0.197477)/0.254598*100:.1f}% of the window")
print("m=2 dead by sign (X=0.2286 > X*); m=8,10,16,18 alive by sign.")
# now: which m give X < X*? compute X for m=2..40 quickly:
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
print("\nm | X=r/s | sign-dead? | (X* = 0.197477)")
for m in (2,4,6,8,10,12,14,16,18,20,22,24,26,28):
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
    X = F(r,s)
    dead = not ((1-238*X**4)**2 - 4*X*X*(1+32*X*X+238*X**4) > 0)
    print(f"{m:>2} | X={float(X):.6f} | {'DEAD (n<2urs)' if dead else 'alive'}")