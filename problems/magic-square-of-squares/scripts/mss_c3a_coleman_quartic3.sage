# mss_c3a_coleman_quartic3.sage -- Q*(Q) determination via SAGE's own
# genus-1 handling (no hand-derived maps) (hermes-win, 2026-09-09).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fQ = x^4 + 136*x^2 + 16
CQ = HyperellipticCurve(fQ)

out('=== X1: Sage native genus-1 elliptic model ===')
try:
    E1 = CQ.elliptic_curve()
    out('  CQ.elliptic_curve():', E1)
    out('  rank:', E1.rank(), ' torsion:', E1.torsion_subgroup())
    out('  E1 gens:', E1.gens() if E1.rank() > 0 else 'none (rank 0)')
except Exception as e:
    out('  X1 error:', str(e)[:250])

out('=== X2: points() on the quartic curve directly ===')
try:
    pts = CQ.points() if hasattr(CQ, 'points') else None
except Exception as e:
    pts = None
try:
    # Sage supports rational_points with bound on genus-1:
    allQ = CQ.rational_points(bound=100)
    out('  CQ.rational_points(bound=100):', allQ)
except Exception as e:
    out('  rational_points error:', str(e)[:200])

out('=== X3: cross-check with the integer search ===')
cnt = 0
for vv in range(-100, 101):
    val = vv**4 + 136*vv**2 + 16
    s = isqrt(val)
    if s*s == val:
        cnt += 1
out('  integer (v, w=+s) points |v| <= 100: %d pairs (each gives ±w)' % cnt)

out('=== X4: the isomorphism Q* ~= E1 pulled back to E_G side ===')
try:
    E1 = CQ.elliptic_curve()
    out('  E1 j:', E1.j_invariant())
    EG = EllipticCurve([0, 0, 0, -504576, 131604480])
    out('  E_G j:', EG.j_invariant(), ' same isogeny class?', E1.j_invariant() == EG.j_invariant())
except Exception as e:
    out('  X4 error:', str(e)[:200])
out('=== DONE ===')