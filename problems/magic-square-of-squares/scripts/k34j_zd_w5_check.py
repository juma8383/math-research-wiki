#!/usr/bin/env python3
# CORRECTION CONFIRMED: my earlier "mod-5 gate" was computed on the WRONG tower
# curve (C1's octic, not Z_D). For Z_D: W_5 = {0, 1, 4} — w ≡ ±1, 0 mod 5.
# The w = s/r relation: w = s/r mod 5 with 5∤r (need r's residue):
# w ≡ ±1 or 0 mod 5 => s ≡ ±r or s ≡ 0 (mod 5).
# The alive admissible points' s mod 5: {2,3,4,1} and r mod 5 =? Need r's classes
# to test s ≡ ±r or s ≡ 0 mod 5. Compute (r mod 5, s mod 5) for alive m:
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
def sign_alive(X):
    return (1-238*X**4)**2 - 4*X*X*(1+32*X*X+238*X**4) > 0
print("m | alive | r mod 5 | s mod 5 | passes W_5 (s≡0,±r mod 5)?")
for m in range(2, 241, 2):
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
    if not alive: continue
    rm, sm = r%5, s%5
    ok = (sm == 0) or (sm == rm) or (sm == (5-rm)%5)
    print(f"m={m:>3}: r%5={rm} s%5={sm}  passes-Z_D-W5: {ok}")