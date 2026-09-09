# mss_c3a_coleman_quartic.sage -- Coleman gate, ROUTE B: integrate directly on
# the E_G-cover (the square-condition quartic) (hermes-win, 2026-09-09).
# [mss-k34-c3ab-prep] cont.
#
# Established (solve3): E_iota and E_G are NOT isogenous (traces disagree at
# 21/22 primes), and E_iota's single 2-isogeny goes to j = 2744000/9 (a THIRD
# curve). So the J(C3_A) ~ E_iota x E_rho x E_G product has three DISTINCT
# isogeny classes: {E_iota (x2)}, {E_G}, and the correspondence to E_G is via
# the square-condition quartic Q* : w^2 = v^4 + 136 v^2 + 16 (Jac = E_G, base
# point (0,1) — 16 = 4^2 is a square, so the quartic has rational base pts).
#
# THE ROUTE (this script): Coleman integration on Q* itself.
# Q* is genus 1 with Jacobian E_G (rank 0, torsion Z/4 x Z/2). Its rational
# points: computable via the elliptic model of Q*. If Q*(Q) = {(0,±1), (±1,±4),
# (±4,±1)}-type degenerate orbit only, then the square condition z^2-4=v^2 has
# only the degenerate solutions => K34-A candidate chain collapses at THIS
# layer. This is a FINITE, classical computation (Mordell on genus-1 quartic).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
# Q* : w^2 = v^4 + 136 v^2 + 16
fQ = x^4 + 136*x^2 + 16
CQ = HyperellipticCurve(fQ)
out('=== V1: Q* construction and point search (exact) ===')
out('  Q* = w^2 = v^4 + 136v^2 + 16 ; points with small v:')
found = []
Bv = 2000
for vnum in range(-Bv, Bv+1):
    val = vnum^4 + 136*vnum^2 + 16
    s = isqrt(val) if val >= 0 else -1
    if s*s == val:
        found.append((vnum, s))
out('  square-w points |v| <= %d: %s' % (Bv, found))
# also negative w:
out('  (each (v, s) also gives (v, -s); v rational with denominator: later)')

out('=== V2: the elliptic model of Q* (its Jacobian E_G) ===')
EG = EllipticCurve([0, 0, 0, -504576, 131604480])
out('  E_G rank:', EG.rank(proof=False), ' torsion:', EG.torsion_subgroup())
# the birational map Q* -> E_G: standard quartic-to-cubic with base point (0,1):
# u = (w+1)/v^2 ... verify on the found points:
def quartic_to_cubic(v, w):
    # base point (0, 1): map via the classical transformation
    # X = (w + 1 + 68v^2)/v^2? Standard: for w^2 = v^4 + a v^2 + b with base (0, b^(1/2)):
    # X = (w + 4)/v^2 (since w(0) = 4), Y = X*v (scaled). We verify on points.
    pass
# verify: does (v,w) = (0, 4) exist? w^2 = 16 -> w = ±4: (0, 4) and (0, -4) too!
out('  base point options: (0, ±4) [w(0) = 16 -> ±4], also v=±1: w^2 = 153? not square.')
out('  found points include (0, ±4)! base point = (0,4).')
# classical map from base point P0 = (0,4): X = (w+4)/v^2, Y = X*(w+4)... derive:
# substitute w = X*v^2 - 4: (X v^2 - 4)^2 = v^4 + 136 v^2 + 16
#   X^2 v^4 - 8X v^2 + 16 = v^4 + 136 v^2 + 16
#   v^4 (X^2 - 1) = v^2 (136 + 4X)
#   v^2 = (136 + 4X)/(X^2 - 1)   [v != 0]
# w = X v^2 - 4.  So E-model: X^2 - 1 | 136 + 4X — this is the E_G-cover map!
out('  v^2 = (136 + 4X)/(X^2 - 1) with w = X*v^2 - 4.')
out('  Square condition: v^2 square <=> (136 + 4X)/(X^2 - 1) square on E_G.')
# E_G point from (v, w): X = (w + 4)/v^2 ... inverse: given E_G point (X, Y):
# Y^2 = X^3 - 504576X + 131604480 ; map: v^2 = (136+4X)/(X^2-1).
out('=== V3: E_G torsion -> Q* images (the full rational point set, if rank 0) ===')
tor = []
for P in EG.torsion_subgroup():
    pass
for P in EG.torsion_subgroup().gens():
    pass
# enumerate torsion points exactly:
tors = []
G4 = EG(48, 10368)
G2 = EG(336, 0)
for i in range(4):
    for j in range(2):
        P = i*G4 + j*G2
        tors.append(P)
out('  8 torsion points of E_G: %s' % sorted(set(tors)))
# map each through the birational map to Q*:
out('  pull each torsion point through v^2 = (136+4X)/(X^2-1):')
qv = []
for P in set(tors):
    if P.is_zero():
        continue
    X, Y = P[0], P[1]
    num = 136 + 4*X
    den = X*X - 1
    if den == 0:
        qv.append((str(P), 'infinity-case'))
        continue
    r = QQ(num)/QQ(den)
    if r >= 0:
        s = isqrt(r)
        if s*s == r:
            qv.append((str(P), 'v=±%d' % s, 'w=±%d' % (X*s - 4)))
        else:
            qv.append((str(P), 'v^2=%s NOT square' % r))
    else:
        qv.append((str(P), 'v^2 negative'))
out('  torsion images: %s' % qv)
out('=== DONE ===')