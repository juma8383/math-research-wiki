#!/usr/bin/env python
# Part 8 (fast): relations mod p first, exact verification only for candidates.
# Also: integral points on the shifted curves; generator identification.
import sys, math
def out(*a): print(*a); sys.stdout.flush()

def ec_add(A, B2, P, Q, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if P == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*A*x1 + B2) * pow(2*y1, p-2, p) % p
    else:
        lam = (y2-y1) * pow(x2-x1, p-2, p) % p
    x3 = (lam*lam - A - x1 - x2) % p
    return (x3, (lam*(x1-x3) - y1) % p)

def ec_mul(A, B2, P, n, p):
    if n < 0:
        Pn = (P[0], (-P[1]) % p) if P else None
        return ec_mul(A, B2, Pn, -n, p)
    R = None; Q = P
    while n:
        if n & 1: R = ec_add(A, B2, R, Q, p)
        Q = ec_add(A, B2, Q, Q, p); n >>= 1
    return R

# candidate dependence mP+nQ = torsion(=O or (0,0)); test mod several p
def relation_test(A, B2, P, Q, rng=16):
    cands = None
    for p in (10007, 10009, 10037, 65537):
        oP = ec_mul(A, B2, P, 10**9, p)  # not needed
        # group order
        n = ec_order(A, B2, P, p)
        mP = {}
        for m in range(-rng, rng+1):
            mP[m] = ec_mul(A, B2, P, m % n if m >= 0 else m, p) if m != 0 else None
        # compute set of (m,n) with mP+nQ in {O,(0,0)} mod p
        ok = set()
        for m in range(-rng, rng+1):
            Rm = ec_mul(A, B2, P, m, p)
            for nn in range(-rng, rng+1):
                R = ec_add(A, B2, Rm, ec_mul(A, B2, Q, nn, p), p)
                if R is None or R == (0, 0):
                    ok.add((m, nn))
        cands = ok if cands is None else (cands & ok)
        if cands == {(0,0)}: return set()
    return cands

def ec_order(A, B2, P, p):
    R = P; n = 1
    while R is not None:
        R = ec_add(A, B2, R, P, p); n += 1
    return n

A, B2 = 256, -2048
P = (16 % 10007, 192 % 10007); Q = (-128 % 10007, 1536)
c = relation_test(A, B2, P, Q)
out("E~_B relation candidates mod p:", c)

# exact check for the candidate set
from fractions import Fraction as F
class EC:
    def __init__(s, a2, a4, a6): s.a2,s.a4,s.a6 = F(a2),F(a4),F(a6)
    def on(s,P):
        if P=='O': return True
        x,y=P; return y*y==x**3+s.a2*x*x+s.a4*x+s.a6
    def add(s,P,Q):
        if P=='O': return Q
        if Q=='O': return P
        x1,y1=P; x2,y2=Q
        if x1==x2 and y1==-y2: return 'O'
        if P==Q:
            if y1==0: return 'O'
            lam=(3*x1*x1+2*s.a2*x1+s.a4)/(2*y1)
        else: lam=(y2-y1)/(x2-x1)
        x3=lam*lam-s.a2-x1-x2
        return (x3,-(y1+lam*(x3-x1)))
    def mul(s,P,n):
        R='O';Q=P
        n=int(n)
        if n<0: return s.mul((P[0],-P[1]),-n)
        while n:
            if n&1: R=s.add(R,Q)
            Q=s.add(Q,Q); n>>=1
        return R
EB = EC(256,-2048,0)
P=(F(16),F(192)); Q=(F(-128),F(1536)); T=(F(0),F(0))
for (m,n) in sorted(c):
    if (m,n)==(0,0): continue
    R = EB.add(EB.mul(P,m), EB.mul(Q,n))
    if R=='O' or R==T:
        out("EXACT relation on E~_B:", m, "* P +", n, "* Q =", R, "-> r_B = 1")
        break
else:
    out("no exact relation among mod-p candidates -> r_B = 2 (Selmer r<=2)")

# integral points on E~_A: y^2 = x^3 -256x^2+18432x, |x|<=20000
hits=[]
for x in range(0, 20001):
    v = x**3 - 256*x*x + 18432*x
    if v >= 0:
        r = math.isqrt(v)
        if r*r == v: hits.append((x, r))
out("E~_A integral points (x<=20000):", hits)
hits=[]
for x in range(0, 20001):
    v = x**3 + 256*x*x - 2048*x
    if v >= 0:
        r = math.isqrt(v)
        if r*r == v: hits.append((x, r))
out("E~_B integral points (x<=20000):", hits)