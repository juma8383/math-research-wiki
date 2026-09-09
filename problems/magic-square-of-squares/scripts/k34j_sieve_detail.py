#!/usr/bin/env python3
# THE FULL SIEVE KILLED ALL 50 ALIVE ADMISSIBLE FIBER POINTS (m <= 240).
# Verify this is airtight: the sieve condition is per-prime necessary for
# Z_D(Q) points, and the lift gate point (s/r, V) IS a Z_D(Q) point.
# Double-check a couple of kills by hand (the first few killed m's) — print
# which prime killed each and the exact residue mismatch.
from fractions import Fraction as F
import math
import sys
sys.set_int_max_str_digits(2000000)

fD = lambda w, p: (pow(w,8,p) - 4*pow(w,6,p) - 604*pow(w,4,p) - 952*pow(w,2,p) + 56644) % p

def pow_set(p):
    return {k*k % p for k in range(p)}

def Wset(p):
    PS = pow_set(p)
    return {w for w in range(p) if fD(w, p) in PS}

Wp = {}
for p in range(5, 120):
    if p == 17: continue
    Wp[p] = Wset(p)

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

print("m | first-killing prime | r%p | s/r mod p | W_p sample")
for m in (8, 10, 16, 18, 24, 26, 34, 36, 42):
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
    if not sign_alive(F(r,s)): continue
    kill = None
    for p in sorted(Wp):
        if r % p == 0: continue
        if math.gcd(r % p, p) != 1: continue
        w = (s * pow(r, -1, p)) % p
        if w not in Wp[p]:
            kill = (p, w)
            break
    p, w = kill
    print(f"m={m:>3}: killed at p={p}: w = {w} not in W_{p} (size {len(Wp[p])})")