#!/usr/bin/env python3
# Mumford rep of the J_L-lift generator on Z_D, and the pullback map.
# Setup from the filed rounds (§2j/§2k/§2m):
#   D : V^2 = x^4 - 4x^3 - 604x^2 - 952x + 56644  (the lift-gate quartic)
#   J_L : y^2 = x^3 - 27894240x + 56491485696   (rank 1, G_L, torsion T)
#   J_L^sh : y^2 = X^3 - 18288 X^2 + 83589408 X, T^sh = (0,0), G^sh = (8568, 51408)
#   (the shift x = X - 6096: -27894240 = -18288^2/4? verify: 18288^2/4 = 83611536
#    vs 27894240 — NOT equal, so the shift is a different translation: from
#    §2k: x = X - 6096 with -27894240 = a4-of-J_L: the two models are
#    y^2 = x^3 - 27894240 x + 56491485696 and shifted y^2 = X^3 - 18288X^2 +
#    83589408X: substitute X = x + 6096: (x+6096)^3 - 18288(x+6096)^2 + 83589408(x+6096)
#    = x^3 + 3*6096x^2 + ... - 18288(x^2 + 2*6096x + ...) + 83589408x + ...
#    x^2: 3*6096 - 18288 = 18288 - 18288 = 0 ✓ (so X = x + 6096 works)
#    x: 3*6096^2 - 18288*2*6096 + 83589408 = 3*37161216 - 36576*6096 + 83589408
#      = 111483648 - 226940416 + 83589408 = -27894240 ✓ matches J_L's a4!
#    const: 6096^3 - 18288*6096^2 + 83589408*6096 = 56491485696? compute:
#    6096^3 = 226624476096; 18288*6096^2 = 18288*37161216 = 679470960648;
#    83589408*6096 = 509581511136; total: 2265024476096 - 679584... let me:
#    226465411096 - 679583... just assert in code.)
# The map D -> J_L^sh: from the quartic D: y^2 = f(x) quartic, the Jacobian
# J_L is the elliptic QUOTIENT of Jac(D) via the 2-cover (J_L = Jac of the
# quartic's...). The relation: D's two-cover structure (§2m): the tower
# Z_D over D over J_L: the generator of the free part of Jac(Z_D) = the
# pullback of the phi-descent-generator from the quartic layer.
# The Mumford rep ON Z_D of the lift of the known point: the known
# D-points: (0, ±238), (-33/2, ±5/4): their images in J_L^sh: (8568, ±51408).
# The Z_D tower map: (w, V) -> (x, V)?? with x = ?: Z_D : V^2 = w^8-4w^6-604w^4
# -952w^2+56644 = D(w^2)?? CHECK: D(x) = x^4-4x^3-604x^2-952x+56644 has ODD
# terms: D(w^2) = w^8 - 4w^6 - 604w^4 - 952w^2 + 56644 ✓ — Z_D is the curve
# of x = w^2 points on D! So Z_D = the "square-x" cover of D.
# The generator question: the J_L-lift generator as a Mumford rep on Z_D.
# Strategy: compute in Sage the Jacobian of Z_D's structure: the map
# Z_D -> D: (w, V) -> (w^2, V): a degree-2 cover; the pullback on Jac:
# Jac(D) ~ E-part x J_L: the J_L part pulls back to Z_D: the Mumford rep
# of the pullback of a J_L-generator divisor: find points of Z_D over the
# x-coordinates of the J_L generator's x: G^sh = (8568, 51408): pull back:
# x = 8568 = w^2: w = ±sqrt(8568): sqrt(8568) = 92.56...: NOT a square!
# The J_L generator does NOT lift to Z_D directly — the tower map's
# image is the alpha^L-fiber structure (§2m): the lift exists only over
# the D-gate points. The Mumford rep of the ACTUAL free generator:
# from §2o-era: P(Q) = {(0,0)} and the census found NO non-degenerate
# lifts... the free part of Jac(Z_D) might come from the DIFFERENCE of
# points at infinity or the octic's own rational points beyond the
# degenerate orbit: zd_point_search found none (a<=20000, b<=200).
# The correct Mumford rep: use the TOWER MAP data from direct_lift:
from sage.all import *
# verify the shift first:
x, X = var('x', 'X') if False else (None, None)
R = PolynomialRing(QQ, 'x')
xr = R.gen()
lhs = (6096 + x)**3 - 18288*(6096 + x)**2 + 83589408*(6096 + x)
print("shifted model equals J_L:", lhs == 6096**3 - 18288*6096**2 + 83589408*6096 + (-27894240)*x + 56491485696)
# J_L^sh in Weierstrass: y^2 = X^3 - 18288X^2 + 83589408X
EL_sh = EllipticCurve(QQ, [0, -18288, 0, 83589408, 0])
print("E^sh:", EL_sh)
print("torsion:", EL_sh.torsion_points() if hasattr(EL_sh,'torsion_points') else EL_sh.torsion_subgroup())
print("rank (mwrank/ellrank):", EL_sh.rank(), EL_sh.gens())
print("G^sh on curve check:", (8568**3 - 18288*8568**2 + 83589408*8568), "vs 51408^2 =", 51408**2)
print("DONE")