#!/usr/bin/env python
# Part 5: isogeny curves, torsion bounds, rank pin-down.
from fractions import Fraction as F
import sys
def out(*a): print(*a); sys.stdout.flush()
class EC:
    def __init__(s, a2, a4, a6):
        s.a2, s.a4, s.a6 = F(a2), F(a4), F(a6)
    def on(s, P):
        if P == 'O': return True
        x, y = P
        return y*y == x**3 + s.a2*x*x + s.a4*x + s.a6
    def add(s, P, Q):
        if P == 'O': return Q
        if Q == 'O': return P
        x1,y1 = P; x2,y2 = Q
        if x1 == x2 and y1 == -y2: return 'O'
        if P == Q:
            if y1 == 0: return 'O'
            lam = (3*x1*x1 + 2*s.a2*x1 + s.a4) / (2*y1)
        else:
            lam = (y2-y1)/(x2-x1)
        x3 = lam*lam - s.a2 - x1 - x2
        y3 = -(y1 + lam*(x3-x1))
        return (x3, y3)
    def mul(s, P, n):
        R = 'O'; Q = P
        while n:
            if n & 1: R = s.add(R, Q)
            Q = s.add(Q, Q); n >>= 1
        return R
    def order(s, P, nmax=24):
        Q = 'O'
        for n in range(1, nmax+1):
            Q = s.add(Q, P)
            if Q == 'O': return n
        return None
    def count_fp(s, p):
        # count points mod p (short-ish Weierstrass with a2,a4,a6)
        cnt = 1
        for x in range(p):
            v = int(x**3 + s.a2*x*x + s.a4*x + s.a6) % p
            if v == 0: cnt += 1
            else:
                if pow(v, (p-1)//2, p) == 1: cnt += 2
        return cnt

# 2-isogeny: E: y^2 = x^3+ax^2+bx  ->  E': y^2 = x^3 - 2a x^2 + (a^2-4b) x
EAsh = EC(-256, 18432, 0)    # shifted E_A
EBsh = EC(256, -2048, 0)     # shifted E_B
EPA  = EC(512, -8192, 0)     # E'_A
EPB  = EC(-512, 73728, 0)    # E'_B

out("isogenous-curve checks:")

# orders up to 16 (Mazur: torsion with a 2-torsion pt is Z/2n, n<=4, or Z/2xZ/2n, n<=4)
out("order tests (nmax=16):")
for nm, E, P in (("EA~ (4,264)", EAsh, (F(4),F(264))), ("EA~ (128,512)", EAsh, (F(128),F(512))),
                 ("EB~ (16,192)", EBsh, (F(16),F(192))), ("EB~ (-128,-1344)", EBsh, (F(-128),F(-1536))),
                 ("EP_A (-4,-64)", EPA, (F(-4),F(-64))), ("EP_B (32,3072)", EPB, (F(512-0+0,1),F(3072,1)))):
    pass
pts_all = [
    ("EA~", EAsh, (F(4),F(264))), ("EA~", EAsh, (F(128),F(512))),
    ("EB~", EBsh, (F(16),F(192))), ("EB~", EBsh, (F(-128),F(-1536))),
    ("EP_A", EPA, (F(128),F(3072))), ("EP_B", EPB, (F(512),F(6144))),
]
for nm, E, P in pts_all:
    out(" ", nm, P, "on curve:", E.on(P), "order<=16:", E.order(P, 16))

# torsion bound via reduction mod good primes
def good_primes(E, ps):
    res = []
    for p in ps:
        d = E.discriminant_mod(p) if hasattr(E,'discriminant_mod') else None
    return res

def disc(E):
    a1=a3=0; a2,a4,a6 = E.a2,E.a4,E.a6
    b2=4*a2; b4=2*a4; b6=4*a6; b8=4*a2*a6-a4*a4
    return -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6

for nm, E in (("EA~", EAsh), ("EB~", EBsh), ("EP_A", EPA), ("EP_B", EPB)):
    D = disc(E)
    g = 0; ns = []
    for p in (3,5,7,11,13,17,19):
        if D % p == 0: continue
        n = E.count_fp(p)
        ns.append((p, n))
        g = n if g == 0 else __import__('math').gcd(g, n)
    out(" ", nm, "torsion divides gcd(#E(F_p)) =", g, ns)