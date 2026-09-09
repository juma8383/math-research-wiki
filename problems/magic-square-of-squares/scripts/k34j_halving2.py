#!/usr/bin/env python3
# DEFINITIVE halving test: G(F(m)) =? m/2 for admissible m.
# F(m): (r,s,u) -> Fermat split (72 rho^4, sigma^4) -> layer-1 (sigma, rho, s) on (1,72)
# G:    A = sigma^2-32rho^2 ; P1P2 = 238 rho^4 ; 238-split P1=d1R^4, P2=d2S^4 (d1d2=238)
#       child (R,S) on x^2 = d1R^4+32R^2S^2+d2S^4 (some role arrangement)
# Compare (R,S) with the m/2 layer-2 point (r_half, s_half), both orders.
from fractions import Fraction as F
import math

A2, A4 = 32, 238
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
def f4(n): return math.isqrt(math.isqrt(n)) if n>0 else 0
def is4(n): return n>0 and f4(n)**4==n

def layer2_point(m):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    X2 = PT[0]/238
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn!=nr or rd*rd!=dr: return None
    r,s = rn,rd
    g = math.gcd(r,s); r//=g; s//=g
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    return (r,s,u)

for m in (2,4,8,10,16,20,24):
    P = layer2_point(m)
    if P is None:
        print(f"m={m}: no fiber point"); continue
    r,s,u = P
    rho = sigma = None
    s2p = s*s + 16*r*r
    h2, hp = (s2p-u)//2, (s2p+u)//2
    for cc in (72,1):
        if h2 % cc == 0:
            q = h2//cc
            if f4(q)**4 == q and f4(q)>0:
                c2 = 72//cc
                if hp % c2 == 0 and f4(hp//c2)**4 == hp//c2 and f4(hp//c2)>0:
                    rho, sigma = f4(q), f4(hp//c2); break
    if rho is None:
        print(f"m={m}: no Fermat split"); continue
    A = sigma*sigma - 32*rho*rho
    P1, P2 = (A-s)//2, (A+s)//2
    assert P1*P2 == 238*rho**4, "Germain identity"
    # 238-split: try ALL (d1,s1,d2,s2) combos
    child = None
    for d1 in (1,2,7,14,17,34,119,238):
        for s1 in (1,-1):
            if P1 % (s1*d1) != 0: continue
            q1 = P1//(s1*d1)
            if q1 <= 0 or not is4(q1): continue
            R = f4(q1)
            d2 = 238//d1
            for s2 in (1,-1):
                if P2 % (s2*d2) != 0: continue
                q2 = P2//(s2*d2)
                if q2 <= 0 or not is4(q2): continue
                S = f4(q2)
                # child equation: x^2 = d1R^4+32R^2S^2+d2S^4 (or swapped constants)
                for (e1,e2) in ((d1,d2),(d2,d1)):
                    val = e1*R**4 + 32*R*R*S*S + e2*S**4
                    if val >= 0 and math.isqrt(val)**2==val:
                        child = (R, S, e1, e2, math.isqrt(val))
                break
        if child: break
    half = layer2_point(m//2) if m % 2 == 0 else None
    if child is None:
        print(f"m={m}: NO 238-split found (P1,P2 not d*4th for d|238)")
        continue
    R,S,e1,e2,xv = child
    if half:
        rh, sh, uh = half
        match = (R==rh and S==sh) or (R==sh and S==rh)
        print(f"m={m}: child (R,S)=({str(R)[:20]},{str(S)[:20]}) consts ({e1},{e2}); "
              f"m/2 point (r,s)=({str(rh)[:20]},{str(sh)[:20]}); MATCH={match}" if False else
              f"m={m}: child R={R.bit_length()}b S={S.bit_length()}b consts=({e1},{e2}) x={'u_half' if xv==uh else '?'}; "
              f"m/2: r={rh.bit_length()}b s={sh.bit_length()}b; (R,S)==(r_h,s_h)? {R==rh and S==sh}; swapped? {R==sh and S==rh}")
    else:
        print(f"m={m}: child R={child[0].bit_length()}b S={child[2] if False else 0}")