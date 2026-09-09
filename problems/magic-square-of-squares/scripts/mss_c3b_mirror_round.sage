# mss_c3b_mirror_round.sage -- B-side mirror of the quartic-layer program
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont.
#
# B-side objects (filed): C3_B: W^2 = 9x^8 - 92x^6 + 310x^4 - 92x^2 + 9
# (filed C3_B octic ascending [9,0,-92,0,310,0,-92,0,9]);
# J(C3_B) ~ E'_iota x E'_rho x E_G with E'_iota = E'_rho the C3_B/iota-quotient
# Jacobian: y^2 = x^3 - 1935360x + 103****1648 (I_1 = 71680); E_G common.
# D_B: w^2 = 9z^4 - 128z^2 + 512 with K34-B <=> z^2 - 4 a nonzero square.
# Square-condition quartic (z^2 = v^2+4): w^2 = 9(v^2+4)^2 - 128(v^2+4) + 512
#   = 9v^4 + 72v^2 + 144 - 128v^2 - 512 + 512 = 9v^4 - 56v^2 + 144.
# THE B-SIDE Q*_B: w^2 = 9v^4 - 56v^2 + 144. Jacobian: invariants of
# (9, 0, -56, 0, 144) -- per the filed table: iota_rho of B: (18688, -4874240)??
# filed: 'iota_rho': [144, 0, -56, 0, 9] -> invariants I_1 = 18688?
# compute both orientations below; ALSO determine Q*_B(Q) exactly.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fBQ = 9*x^4 - 56*x^2 + 144
CQB = HyperellipticCurve(fBQ)
out('=== Z1: Q*_B = w^2 = 9v^4 - 56v^2 + 144 : native rational point set ===')
try:
    allQ = CQB.rational_points(bound=100)
    out('  Q*_B(Q) points (bound 100):', allQ)
except Exception as e:
    out('  rational_points error:', str(e)[:200])

out('=== Z2: integer cross-check ===')
pairs = []
for vv in range(-100, 101):
    val = 9*vv^4 - 56*vv^2 + 144
    if val >= 0:
        s = isqrt(val)
        if s*s == val:
            pairs = pairs + [(vv, s), (vv, -s)]
out('  integer (v, w) pairs |v| <= 100: %s' % sorted(set(pairs)))

out('=== Z3: Jacobian invariants of Q*_B (which factor?) ===')
def IJ(a,b,c,d,e):
    return (12*a*e - 3*b*d + c^2, 72*a*c*e + 9*b*c*d - 27*a*d^2 - 27*b^2*e - 2*c^3)
out('  Q*_B (9,0,-56,0,144) invariants:', IJ(9, 0, -56, 0, 144))
out('  filed: C3_B iota/rho invariants (71680, -38273024) [E_B side];')
out('  filed: iota_rho invariants (18688, -4874240) [E_G side].')
out('  => if Q*_B matches (71680, -38273024), the B square-condition layer is')
out('     E_B-covered (rank 1!) — NOT rank 0 — different structure from A side.')
out('  => if (18688, -4874240), it is E_G-covered like A.')

out('=== Z4: the lift condition on Q*_B(Q) ===')
out('  K34-B needs z^2 = v^2 + 4 rational too. On the Z1/Z2 points:')
out('  (computed below from Z1/Z2 output)')
out('=== DONE ===')