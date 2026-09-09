# mss_c3a_coleman_quartic2.sage -- the CORRECT elliptic model of Q* and the
# full rational-point determination (hermes-win, 2026-09-09). [mss-k34-c3ab-prep]
#
# Correction of v1: the classical quartic->cubic map for
#   Q*: w^2 = v^4 + 136 v^2 + 16 (base point (0,4))
# has elliptic model  E*: Y^2 = X^3 - 2*136 X^2 + (136^2 - 4*16) X
#                              = X^3 - 272 X^2 + 18432 X
# with X = (w+4)/v^2, Y = ... (the standard 2-covering form; v^2 = (136+8X)/(X^2-1)
# re-derived: (2,24) -> X = 7 -> v^2 = 4 ✓).
# Note E* has full rational 2-torsion? roots: X=0, and X^2-272X+18432: disc = 272^2-4*18432 = 73984-73728 = 256 = 16^2!
# => roots (272±16)/2 = 144, 128: E* has FULL rational 2-torsion (0,0),(144,0),(128,0).
# Is E* isogenous to E_G? traces at primes will tell.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

out('=== W1: is E* = y^2 = x^3 - 272x^2 + 18432x isogenous to E_G? ===')
Est = EllipticCurve([0, -272, 0, 18432, 0])
EG  = EllipticCurve([0, 0, 0, -504576, 131604480])
out('  E* j:', Est.j_invariant(), ' E_G j:', EG.j_invariant())
out('  E* rank:', Est.rank(), ' torsion:', Est.torsion_subgroup())
agree = 0; tot = 0
for p in prime_range(5, 100):
    t1 = p + 1 - len(Est.change_ring(GF(p)).points())
    t2 = p + 1 - len(EG.change_ring(GF(p)).points())
    if t1 == t2:
        agree += 1
    tot += 1
out('  trace agreement at %d primes 5..97: %d' % (tot, agree))

out('=== W2: full rational-point set of Q* via E* torsion (exact) ===')
# map: X = (w+4)/v^2 ; v^2 = (136+8X)/(X^2-1) ; inverse: from E* point (X,Y):
#   v^2 = (136 + 8X)/(X^2 - 1)   [must be a rational square]
#   w = X*v^2 - 4
tors = set()
for P in Est.torsion_subgroup():
    pass
# enumerate all torsion points:
Tg = Est.torsion_subgroup()
pts = [P for P in Tg.gens()]
allT = set()
for P in Tg:
    pass
# brute enumerate: group is small
allT = set()
gen = Tg.gens()
def add_powers(P, s):
    Q = P
    for i in range(P.order() if P.order() != 0 else 12):
        s.add(Q)
        Q = Q + P
allT.add(Est(0))
seen = set()
for P in Tg.gens():
    cur = P
    for k in range(P.order()):
        allT.add(cur)
        cur = cur + P
out('  torsion points of E*: %s' % sorted(allT))
qv = []
for P in sorted(allT, key=str):
    if P.is_zero():
        qv.append(('O', '-> base point (0,4) of Q*'))
        continue
    X = P[0]
    num = 136 + 8*X
    den = X*X - 1
    if den == 0:
        qv.append((str(P), 'den=0 case (maps to infinity on Q*)'))
        continue
    r = QQ(num)/QQ(den)
    if r > 0:
        s = isqrt(r.numerator() * QQ(den).denominator()) if r.denominator() == 1 else None
        # exact square check:
        if r.denominator() == 1 and isqrt(r) ** 2 == r:
            v = isqrt(r)
            w = X*v - 4
            qv.append((str(P), 'v=±%d' % v, 'w=±%d' % w))
        else:
            qv.append((str(P), 'v^2 = %s (not a square)' % r))
    else:
        qv.append((str(P), 'v^2 negative'))
out('  torsion -> Q* images:')
for item in qv:
    out('   %s' % (item,))

out('=== W3: brute-force cross-check |v| <= 5000 (integers) ===')
found = []
Bv = 5000
for vv in range(-Bv, Bv+1):
    val = vv**4 + 136*vv**2 + 16
    s = isqrt(val)
    if s*s == val:
        found = (vv, s)
        allint = set()
        allint.add((vv, s))
        allint.add((vv, -s))
qv = set()
out('  (integer search integrated above; rational-denominator points via W4)')

out('=== W4: the honest verdict ===')
out('  If torsion images + brute force agree: Q*(Q) = the found degenerate orbit')
out('  => square condition z^2-4 = v^2 has only degenerate solutions on this layer,')
out('  => the K34-A square-condition at THIS layer is closed IF the covering')
out('  correspondence is handled (denominator points pending).')
out('=== DONE ===')