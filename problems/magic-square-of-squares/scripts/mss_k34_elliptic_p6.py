#!/usr/bin/env python
# Part 6: rank pin-down.
#  E~_A: alpha Selmer = {1,2} (rigorous), both realized -> |alpha|=2.
#  E'_A: alpha' Selmer <= {+-1,+-2} -> |alpha'| <= 4.
#    => 2^(r_A+2) = |alpha||alpha'| <= 8 -> r_A <= 1; (128,512) non-torsion -> r_A = 1. PROVED.
#  E~_B: alpha Selmer = {1,-2} -> |alpha| = 2.
#  E'_B: alpha' Selmer <= {1,2,3,6} -> |alpha'| <= 8 -> r_B <= 2.
#  Need: independence of (16,192),( -128,1536) on E~_B  (indep -> r_B=2)
#        else r_B=1.
#  Also: realize classes 3,6 on E'_B <=> points on C_3, C_6 (search).
from fractions import Fraction as F
import sys, math
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

EAsh = EC(-256, 18432, 0)
EBsh = EC(256, -2048, 0)
EPB  = EC(-512, 73728, 0)

# independence test on E~_B: is m*P + n*Q == O or torsion for small |m|,|n|?
P = (F(16), F(192)); Q = (F(-128), F(1536)); T = (F(0), F(0))
rel = None
for m in range(-8, 9):
    for n in range(-8, 9):
        R = EBsh.add(EBsh.mul(P, m), EBsh.mul(Q, n))
        if R == 'O' or R == T:
            rel = (m, n, R)
if rel and rel[0:2] != (0,0):
    out("E~_B: P,Q DEPENDENT:", rel, "-> r_B = 1")
else:
    out("E~_B: no small relation mP+nQ in torsion for |m|,|n|<=8 -> r_B = 2 (given Selmer r<=2)")

# same for E~_A: is (4,264) in <(128,512)>+torsion?
P2 = (F(128), F(512)); Q2 = (F(4), F(264)); T2 = (F(0), F(0))
found = None
for m in range(-12, 13):
    for t in (0, 1):
        R = EAsh.mul(P2, m)
        if t: R = EAsh.add(R, T2)
        if R == Q2 or R == EAsh.add(Q2, 'O'):
            found = (m, t)
out("E~_A: (4,264) = m*(128,512)+t*(0,0)?", found)

# realize squareclasses 3,6 on E'_B via C_d: N^2 = d M^4 - 512 M^2 e^2 + (73728/d) e^4
def search_cd(d, B, name):
    hits = []
    bd = 73728 // d
    for M in range(0, B+1):
        M2 = M*M; M4 = M2*M2
        for e in range(1, B+1):
            if math.gcd(M, e) != 1: continue
            if M == 0 and d not in (1,): pass
            N2 = d*M4 - 512*M2*e*e + bd*e**4
            if N2 >= 0:
                r = math.isqrt(N2)
                if r*r == N2:
                    hits.append((M, e, r))
    out(name, "hits (M,e,N) up to", B, ":", hits[:12])

search_cd(3, 60, "C_3 for E'_B")
search_cd(6, 60, "C_6 for E'_B")
# also class 1 and 2 sanity on E'_B (should be soluble):
search_cd(2, 30, "C_2 for E'_B")