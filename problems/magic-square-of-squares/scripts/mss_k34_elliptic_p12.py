#!/usr/bin/env python
# Part 12: origin-based conversion (origin (0,1) for M_A, (0,3) for M_B),
# verification on ALL known rational points, torsion orders, rank-2 witness.
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
    def neg(s, P):
        return 'O' if P == 'O' else (P[0], -P[1])
    def mul(s, P, n):
        R = 'O'; Q = P
        while n:
            if n & 1: R = s.add(R, Q)
            Q = s.add(Q, Q); n >>= 1
        return R

EA = EC(-250, 17420, 35848)
EB = EC(310, 8140, 51912)

# quartic verification: (V*q^2)^2 = q^4 * f(p/q)
def fA(X): return X**4 + 132*X**3 - 250*X**2 + 132*X + 1
def fB(X): return 9*X**4 - 92*X**3 + 310*X**2 - 92*X + 9
def on_quartic(f, p, q, Vq):
    X = F(p, q)
    return F(Vq*Vq, q**4) == f(X)

ptsA = [(0,1,1),(0,1,-1),(1,1,4),(1,1,-4),(31,35,4604),(31,35,-4604),
        (35,31,4604),(35,31,-4604),(66,1151,3693311),(66,1151,-3693311),
        (1151,66,3693311),(1151,66,-3693311)]
ptsB = [(0,1,3),(0,1,-3),(1,1,12),(1,1,-12),(5,41,2508),(5,41,-2508),
        (41,5,2508),(41,5,-2508),(209,414,943587),(209,414,-943587),
        (414,209,943587),(414,209,-943587)]

out("=== S1: all 12 known M_A points on the quartic (exact) ===")
for p,q,Vq in ptsA:
    out("  A(%d/%d, +-%d/..) on M_A: %s" % (p,q,abs(Vq), on_quartic(fA,p,q,Vq)))
for p,q,Vq in ptsB:
    out("  B(%d/%d, +-%d/..) on M_B: %s" % (p,q,abs(Vq), on_quartic(fB,p,q,Vq)))

# ---- maps (as verified in part 3) ----
def mapA(Xq, V):   # origin (0,-1) at infinity
    xE = (V - 1 - 66*Xq)/(Xq*Xq)
    return (-2*xE, 2*(xE*xE-1)*Xq + 132*(xE-1))
def mapB(Xq, V):
    xE = (V - 3 + F(46,3)*Xq)/(Xq*Xq)
    c2 = xE*xE - 9
    c1 = F(-92,3)*(xE - 3)
    return (-6*xE, 3*(2*c2*Xq + c1))
def chiA(Xq, V):   # origin (0,1) at infinity: chi = -psi o (V -> -V)
    P = mapA(Xq, -V)
    return 'O' if P == 'O' else (P[0], -P[1])
def chiB(Xq, V):
    P = mapB(Xq, -V)
    return 'O' if P == 'O' else (P[0], -P[1])

out("=== S2: map all non-degenerate points to E_A / E_B (origin (0,-1)/(0,-3) maps) ===")
okA = okB = True
imgA = {}
imgB = {}
for p,q,Vq in ptsA:
    if p == 0: continue
    P = mapA(F(p,q), F(Vq,q*q))
    good = EA.on(P)
    okA &= good
    imgA[(p,q,Vq)] = P
    out("  M_A (%d/%d,%s) -> E_A %s on:%s" % (p,q,Vq,P,good))
for p,q,Vq in ptsB:
    if p == 0: continue
    P = mapB(F(p,q), F(Vq,q*q))
    good = EB.on(P)
    okB &= good
    imgB[(p,q,Vq)] = P
    out("  M_B (%d/%d,%s) -> E_B %s on:%s" % (p,q,Vq,P,good))
out("all finite images on-curve: A=%s B=%s" % (okA, okB))

out("=== S3: degenerate-point images ===")
# limits Xq -> 0: (0,1)->(4606,-304128) on E_A ; (0,-1)->O
out("  E_A (4606,-304128) on:", EA.on((F(4606), F(-304128))))
xE = F(-674,9); PB = (xE, F(-23552,27))
out("  E_B (-674/9,-23552/27) on:", EB.on(PB))
# origin (0,1) model check: chi maps (0,1)->O
out("  chiA(1,4) = ", chiA(F(1), F(4)), " (should be -mapA(1,-4))")
out("  chiA(0,1) -> O by construction; chiA(0,-1) -> -mapA(0,1) = (4606,304128)")

out("=== S4: torsion orders of all images (torsion group = {O, 2-torsion}) ===")
def is_2tors(E, P):
    return P == 'O' or (P[1] == 0 and E.on(P))
out("  E_A 2-torsion point (-2,0):", EA.on((F(-2), F(0))))
for k, P in imgA.items():
    out("  E_A img %s: torsion=%s" % (k, is_2tors(EA, P)))
for k, P in imgB.items():
    out("  E_B img %s: torsion=%s" % (k, is_2tors(EB, P)))
out("  E_B 2-torsion: solve x^3+310x^2+8140x+51912=0 over Q:")
import sympy as sp
x = sp.symbols('x')
out("   roots:", sp.factor(x**3 + 310*x**2 + 8140*x + 51912))
out("  E_A cubic:", sp.factor(x**3 - 250*x**2 + 17420*x + 35848))

out("=== S5: independence of E_B generators (rank 2 witness) ===")
# E~_B model for modular arithmetic: y^2 = x^3+256x^2-2048x ; shift from E_B?
# Instead work directly on E_B mod p (long Weierstrass, same formulas).
def mod_pt(E, P, p):
    def red(z):
        n, d = z.numerator % p, z.denominator % p
        return (n * pow(d, -1, p)) % p
    return (red(P[0]), red(P[1]))
def ec_add_mod(P, Q, a2, a4, p):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and (y1+y2) % p == 0: return None
    if P == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*a2*x1 + a4) * pow(2*y1, -1, p) % p
    else:
        lam = (y2-y1) * pow(x2-x1, -1, p) % p
    x3 = (lam*lam - a2 - x1 - x2) % p
    y3 = (-(y1 + lam*(x3-x1))) % p
    return (x3, y3)
def ec_mul_mod(P, n, a2, p):
    R = None; Q = P
    while n:
        if n & 1: R = ec_add_mod(R, Q, a2, p)
        Q = ec_add_mod(Q, Q, a2, p); n >>= 1
    return R
P1 = imgB[(1,1,12)]
P2 = imgB[(209,414,943587)]
found = False
DELTA_B = 4947802324992
for p in (13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
    if DELTA_B % p == 0: continue
    a2m = 310 % p; a4m = 8140 % p
    try:
        Q1 = mod_pt(EB, P1, p); Q2 = mod_pt(EB, P2, p)
    except ValueError:
        continue
    # subgroup <Q1> union coset +T
    T2 = None
    S = set()
    R = None
    for n in range(0, 400):
        S.add(R)
        R = ec_add_mod(R, Q1, a2m, a4m, p)
        if R is None: break
    cyc = S
    # 2-torsion roots mod p:
    # 2-torsion roots of x^3+310x^2+8140x+51912 mod p
    twos = [xx for xx in range(p) if (xx**3 + 310*xx*xx + 8140*xx + 51912) % p == 0]
    ok = True
    for t2 in twos:
        coset = set(ec_add_mod(s, (t2, 0), a2m, a4m, p) for s in cyc)
        if Q2 in coset: ok = False
    if ok:
        print("  p=%d: P2 not in <P1,T> ; #<P1>=%d ; 2-torsion roots mod p: %s" % (p, len(cyc), twos))
        found = True
        break
if not found:
    out("  no distinguishing prime found in list")