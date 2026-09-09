#!/usr/bin/env python3
# Final verification battery:
# 1. Halving identity G(F(m)) = fiber(m/2) up to transposition, for ALL even m in 2..28.
# 2. Odd-index exit: for odd m, child = (s_m, r_m, u_m) which lies on C_1 (trivial class),
#    NOT on C_238 (unless r=s) -> killed-cell exit. Verify m=1,3,5,7.
# 3. The lifted-layer-1 validity: n' = s_m mod 4 and lift s_m +- 2 rho sigma.
# Exact integer arithmetic throughout.
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
def issq(n):
    if n<0: return False
    r=math.isqrt(n); return r*r==n

def fiber(m):
    """the C_238 fiber point from T_a + 2m P_a, as (r,s,u) exact, or None"""
    Q = mul(Pa, 2*m); PT = add(Q,T)
    X2 = PT[0]/238
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn!=nr or rd*rd!=dr: return None
    r,s = rn,rd
    g = math.gcd(r,s); r//=g; s//=g
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    return (r,s,u)

def loop_child(m):
    """Fermat+Germain loop applied to the fiber(m) point; returns (consts, R, S, xval)."""
    P = fiber(m)
    if P is None: return None
    r,s,u = P
    s2p = s*s + 16*r*r
    h2, hp = (s2p-u)//2, (s2p+u)//2
    rho = sigma = None
    for cc in (72,1):
        if h2 % cc == 0:
            q = h2//cc
            if is4(q) and f4(q)>0:
                c2 = 72//cc
                if hp % c2 == 0 and is4(hp//c2) and f4(hp//c2)>0:
                    rho, sigma = f4(q), f4(hp//c2); break
    if rho is None: return None
    A = sigma*sigma - 32*rho*rho
    P1, P2 = (A-s)//2, (A+s)//2
    assert P1*P2 == 238*rho**4, "Germain identity"
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
                for (e1,e2) in ((d1,d2),(d2,d1)):
                    val = e1*R**4 + 32*R*R*S*S + e2*S**4
                    if val >= 0 and issq(val):
                        return (e1,e2,R,S,math.isqrt(val))
    return None

print("== 1. halving identity for even m ==")
for m in (2,4,6,8,10,12,14,16,18,20,22,24,26,28):
    ch = loop_child(m)
    if ch is None:
        print(f"m={m}: fiber point exists? {fiber(m) is not None}; loop child not found")
        continue
    e1,e2,R,S,xv = ch
    half = fiber(m//2)
    if half is None:
        print(f"m={m}: child consts ({e1},{e2}) (R,S) {R.bit_length()}b/{S.bit_length()}b; m/2 has NO fiber point")
        continue
    rh, sh, uh = half
    untrans = (R==rh and S==sh)
    trans = (R==sh and S==rh)
    print(f"m={m}: child consts ({e1},{e2}) (R,S) ({R.bit_length()}b,{S.bit_length()}b) | "
          f"fiber(m/2) (r,s) ({rh.bit_length()}b,{sh.bit_length()}b) | untransposed={untrans} transposed={trans} | x==u_half: {xv==uh}")

print("\n== 2. odd-index exit: child = (s_m, r_m, u_m) on C_1, NOT on C_238 ==")
for m in (1,3,5,7,9):
    P = fiber(m)
    if P is None:
        print(f"m={m}: no fiber point"); continue
    r,s,u = P
    # transposed point on C_1: s^4 + 32 s^2 r^2 + 238 r^4 == u^2 (same sum, automatic)
    onC1 = s**4 + 32*s*s*r*r + 238*r**4 == u*u
    onC238_swapped = 238*s**4 + 32*s*s*r*r + r**4 == u*u  # would be needed for a C_238 member
    ch = loop_child(m)
    tag = f"child consts ({ch[0]},{ch[1]}), (R,S)=({ch[2].bit_length()}b,{ch[3].bit_length()}b)" if ch else "no clean child"
    print(f"m={m}: (r,s)=({r.bit_length()}b,{s.bit_length()}b)  transposed-on-C_1: {onC1}  "
          f"swapped-solves-C_238: {onC238_swapped}  | {tag}")

print("\n== 3. layer-1 validity per m: n'=s mod 4, lift s+-2rho*sigma ==")
for m in (2,8,10,16,18,24):
    P = fiber(m)
    r,s,u = P
    s2p = s*s+16*r*r
    h2,hp = (s2p-u)//2,(s2p+u)//2
    for cc in (72,1):
        if h2 % cc == 0 and is4(h2//cc) and f4(h2//cc)>0:
            c2 = 72//cc
            if hp % c2 == 0 and is4(hp//c2) and f4(hp//c2)>0:
                rho, sigma = f4(h2//cc), f4(hp//c2); break
    l1 = issq(s+2*rho*sigma); l2 = issq(s-2*rho*sigma)
    print(f"m={m}: n'=s mod4={s%4}  lift+:{l1} lift-:{l2}")