#!/usr/bin/env python3
# P(Q) = {(0,0)} in a sizable box (x=p/q, p<=3000, q<=40; integers to 3000).
# Next: Z_D(Q) points beyond degenerate — the sieve compound: W_5 x W_7 x W_11...
# For the ratio w = a/b (lowest terms): conditions per prime p (p∤b): a/b mod p ∈ W_p(Z_D).
# For p|b: the infinity character (leading coeff 1 at w^8 — square! so the two
# infinity points of Z_D ARE rational — degree 8 with lead coeff 1 = square).
# So for any p|b: w = ∞ and the point at infinity IS rational: no condition.
# The sieve on (a, b): the CRT intersection over primes must contain (a,b).
# For the leaf fiber: w = s/r. The admissible alive points must satisfy:
# s/r mod p ∈ W_p for all p ∤ r. Compute the compound test at m<=240:
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

# precompute W_p for p up to 500
Wp = {}
for p in range(5, 500):
    if p in (17,): continue  # 17 bad prime for J_L family? fD mod 17: check singularity
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

def sieve_verdict(r, s):
    """check w = s/r against W_p for all primes p <= 499 (p ∤ r); p | r allowed (infinity)."""
    for p, W in Wp.items():
        if r % p == 0:
            continue  # w = infinity mod p: allowed (rational infinity points exist)
        g = math.gcd(r % p, p)
        if g != 1:
            continue  # shouldn't happen for prime p unless p|r
        w = (s * pow(r, -1, p)) % p
        if w not in W:
            return False, p
    return True, None

alive = 0
killed = 0
surv = []
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
    if not sign_alive(F(r,s)): continue
    ok, badp = sieve_verdict(r, s)
    if ok:
        surv.append(m); alive += 1
    else:
        killed += 1
print(f"alive admissible points m<=240 tested against W_p (p<=499):")
print(f"  surviving the full sieve: {alive} (m values: {surv})")
print(f"  killed: {killed}")
print("\n(the survivor list needs deeper primes/structure; each survivor is a")
print(" candidate requiring the Jac(P) rank gate)")