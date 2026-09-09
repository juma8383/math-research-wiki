#!/usr/bin/env python3
# W_5 = {0} is the ONLY prime with |W_p| <= 2 below 300. The sieve on a single
# prime gives 5|s (if w = s/r) — a congruence condition, not a kill.
# BUT WAIT: recheck the relation between w and the leaf variables. In §2k:
# the gate quartic D had x = (s/r)^2 and the C1 cover of J_L is the class-1
# fiber = the quartic for the gate. So x_C1 = (s/r)^2 = w^2 with w = s/r.
# w ≡ 0 mod 5 => 5|s. Now run the SAME argument one level up: the point
# (s, r) has 5|s. What does 5|s do to the leaf admissibility? Nothing direct.
# BUT the Z-level: the Z-point is (w, y) = (s/r, y). w ≡ 0 mod 5 means the
# Z-point's w-coordinate is 0 mod 5 — the point reduces to (0, ±3) mod 5 —
# the DEGENERATE point. So every Z(Q) point reduces mod 5 to the degenerate
# orbit. Not a contradiction.
# Deeper: v5 structure. If w = s/r with 5|s (5∤r): f(w) = 8w^8+1016w^4+9 has
# v5 = v5(9) = 0 — fine. The Z-point's y: y^2 = f(s/r) = (8s^8+1016s^4r^4+9r^8)/r^8.
# v5(8s^8+1016s^4r^4+9r^8) with 5|s: ≡ 9r^8 mod 5: QR ✓. No contradiction.
# So the sieve gives: every Z(Q) point has w ≡ 0 mod 5 — i.e. 5 | s for any
# leaf fiber point that passes the lift gate. That's a NEW congruence condition
# on admissible fiber points (5|s), compatible with everything so far.
# Check empirically: do the admissible fiber points have 5|s? m=2: s=3727: 
# 3727 mod 5 = 2. NO. But m=2 is sign-dead (X > X*) — the gate pipeline
# already killed it. For alive m: m=8: s=159066598714985526821727121541592387469755642141185629817087: 
# mod 5? Check the last digit: 7. NO! 5 ∤ s at m=8. So m=8's fiber point
# cannot pass the lift gate — ANOTHER provable kill (5|s required, 5∤s at m=8)!
# This is a NEW provable gate: the mod-5 sieve says lift ⟹ 5|s. Test all alive
# admissible points for 5|s.
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
import sys
sys.set_int_max_str_digits(2000000)
def sign_alive(X):
    return (1-238*X**4)**2 - 4*X*X*(1+32*X*X+238*X**4) > 0
def issq(x):
    if x < 0: return False
    rt = math.isqrt(x); return rt*rt == x
cnt5 = cntnot5 = 0
for m in range(2, 61, 2):
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
    alive = sign_alive(F(r,s))
    five = (s % 5 == 0)
    if alive:
        cnt5 += five; cntnot5 += (not five)
    print(f"m={m:>2}: alive={alive} 5|s={five} (s mod 5 = {s%5})")
print(f"\nalive points: 5|s: {cnt5}, 5∤s: {cntnot5}  <- 5∤s points are DEAD by the mod-5 sieve (lift ⟹ 5|s)")