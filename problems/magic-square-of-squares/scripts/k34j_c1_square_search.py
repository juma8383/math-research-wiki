#!/usr/bin/env python3
# Round-4 second front: the C1 square-x tower question (named next step).
# C1: y^2 = 8x^4 + 1016x^2 + 9 — the class-1 alpha^L-cover of J_L^sh.
# "No positive-square-x point on C1" = the §2k tower question at height 1.
# C1's own structure: invariants IJ(8,0,1016,0,9) = (1033120, -2092277248) —
# same Jacobian J_L. C1 has rational points? PARI ell2cover says it's locally
# soluble; find its rational points: y^2 = 8x^4+1016x^2+9.
# x=0: y=+-3. Point (0,3)! (like D's (0,238) degenerate point.)
# The square-x question: x = (p/q)^2 > 0. Search deeper than round 2 (p<=400,q<=40):
# use the J_L group law: C1(Q) maps into J_L with image = the class-1 fiber
# = 2E(Q) = <2G^sh>. Points of <2G^sh>: n*2G^sh. The quartic points correspond
# to x = X(P)-something... The explicit map (from ell2cover output):
# C1 -> J_L^sh: (x,y) -> [(-48672/y^2)x^4 + 3106368/y^2 x^2 + (6084y^2-54756)/y^2,
#                        -222905088/y^3 x^5 + 250768224/y^3 x]
# Compute X-coordinate of image for square-x points and compare to x(2nG^sh).
# Direct: search square-x on C1 deeper (p<=3000, q<=200).
from fractions import Fraction as F
import math

found = []
q_max, p_max = 200, 3000
for q in range(1, q_max+1):
    q2 = q*q
    for p in range(1, p_max+1):
        if math.gcd(p, q) != 1: continue
        p2 = p*p
        x = F(p2, q2)
        x2 = x*x
        v = 8*x2*x2 + 1016*x2 + 9
        if v > 0 and math.isqrt(v.numerator)**2 == v.numerator and math.isqrt(v.denominator)**2 == v.denominator:
            found.append((x, F(math.isqrt(v.numerator), math.isqrt(v.denominator))))
            print(f"HIT: x = {x} = ({p}/{q})^2, y = {found[-1][1]}")
            if len(found) >= 5: break
    if len(found) >= 5: break
if not found:
    print(f"no square-x point on C1 in p<={p_max}, q<={q_max}")
# ALSO test x=0-family: x=0 gives y=3; x=0 is a square trivially (0=(0/q)^2) —
# but 0 corresponds to s=0 (degenerate, excluded). Note it.
print("note: x=0 (degenerate, y=+-3) always present; excluded from the gate.")