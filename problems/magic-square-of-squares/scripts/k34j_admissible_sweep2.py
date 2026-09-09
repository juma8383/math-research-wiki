#!/usr/bin/env python3
# Fast sweep (no factorization): m in [-40..40], admissibility + Fermat split via
# direct c1 in {1,8,9,72} 4th-power tests (isqrt only).
from fractions import Fraction as F
import math

A2, A4 = 32, 238

def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1 == x2 and (y1+y2) == 0: return None
    if P == Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*A2*x1 + A4) / (2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - A2 - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3, y3)

def mul(P, n):
    R = None; Q = P
    while n:
        if n & 1: R = add(R, Q)
        Q = add(Q, Q); n >>= 1
    return R

T = (F(0), F(0)); Pa = (F(-14), F(14))

def issq(n):
    if n < 0: return False
    r = math.isqrt(n); return r*r == n

adm = []
for m in range(-40, 41):
    if m == 0: continue
    Q = mul(Pa, 2*m)
    PT = add(Q, T)
    if PT is None: continue
    X2 = PT[0] / 238
    if X2 <= 0: continue
    nr, dr = X2.numerator, X2.denominator
    rn, rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn != nr or rd*rd != dr: continue
    r, s = rn, rd
    g = math.gcd(r,s); r//=g; s//=g
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    admissible = (r % 6 == 0) and (s % 2 == 1) and (s**4 > 238*r**4)
    if not admissible: continue
    n = s**4 - 238*r**4
    s2p = s*s + 16*r*r
    Fm, Fp = s2p - u, s2p + u
    h2, hp = Fm//2, Fp//2
    assert h2*hp == 72*(r//2)**4
    gg = math.gcd(h2, hp)
    valid = rho = sigma = None
    for cc in (1, 8, 9, 72):
        if h2 % cc == 0:
            q = h2 // cc
            rr = math.isqrt(math.isqrt(q)) if q > 0 else 0
            if rr > 0 and rr**4 == q:
                c2p = 72 // cc
                if hp % c2p == 0:
                    q2 = hp // c2p
                    ss = math.isqrt(math.isqrt(q2))
                    if ss > 0 and ss**4 == q2:
                        valid = (cc, c2p); rho, sigma = rr, ss
                        break
    lift = None
    if valid:
        l1 = issq(s + 2*rho*sigma); l2 = issq(s - 2*rho*sigma)
        lift = (l1, l2)
    print(f"m={m:+d}: r={str(r)[:25]} s={str(s)[:25]} gcdsplit={gg} valid={valid} "
          f"rho={str(rho)[:15]} sigma={str(sigma)[:15]} n'=s mod4={s%4} lift={lift}")
    adm.append((m, r, s, valid, rho, sigma, lift))

print(f"\ntotal admissible in [-40,40]: {len(adm)}")
for (m, r, s, valid, rho, sigma, lift) in adm:
    print(f"m={m:+d}: valid={valid} rho={str(rho)[:20]} sigma={str(sigma)[:20]} n'=s mod4={s%4} lift={lift}")