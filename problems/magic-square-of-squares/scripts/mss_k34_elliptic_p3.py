#!/usr/bin/env python
# Part 3: E_A, E_B models, maps, torsion tests (exact rationals).
from fractions import Fraction as F
import sys
def out(*a): print(*a); sys.stdout.flush()

# E_A: Y^2 = X^3 - 250X^2 + 17420X + 35848   (from M_A, xE=(V-1-66Xq)/Xq^2, X=-2xE)
# E_B: Y^2 = X^3 + 310X^2 + 8140X + 51912    (from M_B, xE=(V-3+46Xq/3)/Xq^2, X=-6xE, Y=3YE)

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

EA = EC(-250, 17420, 35848)
EB = EC(310, 8140, 51912)

# maps M -> E (quartic point (Xq,V) -> E point), derived above.
def mapA(Xq, V):
    xE = (V - 1 - 66*Xq) / (Xq*Xq)
    X = -2*xE
    Y = 2*(xE*xE - 1)*Xq + 132*(xE - 1)
    return (X, Y)
def mapB(Xq, V):
    xE = (V - 3 + F(46,3)*Xq) / (Xq*Xq)
    X = -6*xE
    Y = 3*(2*(xE*xE - 9)*Xq + sp.none if False else 0)  # placeholder
    return None

# For M_B the Y-formula: quadratic in Xq: c2 Xq^2 + c1 Xq + c0 = 0 with
# c2 = xE^2-9, c1 = -92(xE-3)/3, c0 = 2(27xE-337)/9
# root Xq = [-c1 +- Y]/(2 c2) with Y^2 = D; so Y = 2*c2*Xq + c1
def mapB2(Xq, V):
    xE = (V - 3 + F(46,3)*Xq) / (Xq*Xq)
    c2 = xE*xE - 9
    c1 = F(-92,3)*(xE - 3)
    Y = 2*c2*Xq + c1          # this is YE (on D-curve)
    X = -6*xE
    return (X, 3*Y)           # E_B point (scaled: (3y)^2 = ... verified below)

# verify models: check E_B model against map on known point
out("EA on-curve checks:")
for (Xq, V) in [(F(1), F(4)), (F(31), F(35))]:
    Xq = F(Xq, V) if False else None
# known M_A points as (Xq, V) with V the TRUE quartic value (not q^2 scaled):
ptsA = [(F(0), F(1)), (F(0), F(-1)), (F(1), F(4)), (F(1), F(-4)),
        (F(31,35), F(4604,1225)), (F(31,35), F(-4604,1225))]
for P in ptsA:
    Xq, V = P
    if Xq == 0:
        out("  (0,+-1): maps to pole/regular special cases, handled separately")
        continue
    Q = mapA(Xq, V)
    out("  M_A", P, "-> E_A", Q, "on curve:", EA.on(Q))
out("EB on-curve checks:")
ptsB = [(F(1), F(12)), (F(1), F(-12)), (F(5,41), F(2508,1681)), (F(5,41), F(-2508,1681))]
for P in ptsB:
    Xq, V = P
    Q = mapB2(Xq, V)
    out("  M_B", P, "-> E_B", Q, "on curve:", EB.on(Q))
# also verify E_B model derivation numerically: (X,Y)=( -146, +-1536 ) from (1,12)
out("E_B (-146,1536) on:", EB.on((F(-146), F(1536))))
# E_A: (0,1) should map to finite point; (0,-1) to O; infinity points:
out("E_A (2,264) on:", EA.on((F(2), F(264))), " (-2,0) on:", EA.on((F(-2), F(0))))

# torsion order tests
def order(E, P, nmax=24):
    Q = 'O'
    for n in range(1, nmax+1):
        Q = E.add(Q, P)
        if Q == 'O': return n
    return None

for nm, E, pts in (("E_A", EA, [(F(126), F(512)), (F(2), F(264)), (F(-2), F(0))]),
                   ("E_B", EB, [(F(-146), F(1536))])):
    for P in pts:
        out(nm, "point", P, "order:", order(E, P))