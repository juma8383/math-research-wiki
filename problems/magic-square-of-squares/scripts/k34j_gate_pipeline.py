#!/usr/bin/env python3
# ROUND-3 main computation: extend the admissible sweep with the new sign gate
# and the D-gate (square-x on D) to larger m. For each admissible fiber point:
#   (i) X < X* (sign condition) else DEAD;
#   (ii) N(X^2) square (the D-gate / §2k gate);
#   (iii) if both pass -> an ACTUAL K34-A candidate (a,b) exists -> test further.
# This is the full gate pipeline. N(X^2) square is a huge-numbers test: N((s/r)^2)
# = (n^2-4u^2r^2s^2)/r^8; square iff (n^2-4u^2r^2s^2) is a square (r^8 is one).
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

def sign_alive(X):
    # X a Fraction: test (1-238X^4)^2 - 4X^2(1+32X^2+238X^4) > 0
    return (1-238*X**4)**2 - 4*X*X*(1+32*X*X+238*X**4) > 0

print("Full gate sweep m=2..60 (admissible): sign + D-gate")
cands = 0
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
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    n = s**4 - 238*r**4
    X = F(r,s)
    alive = sign_alive(X)
    prod = n*n - 4*u*u*r*r*s*s     # == r^8 N(X^2); N(X^2) square iff prod square & >=0
    dg = (prod >= 0) and issq(prod)
    tag = "SIGN-DEAD" if not alive else ("D-GATE-PASS" if dg else "D-fails")
    if alive and dg: cands += 1
    print(f"m={m:>2}: X={float(X):.6f} {'DEAD' if not alive else 'alive'}  D-gate: "
          f"{'PASS' if dg else ('neg-prod' if prod<0 else 'fail')}  "
          f"prod={str(prod)[:18]}...")
print(f"\ncandidates passing BOTH gates: {cands}")