# mss_c3b_annihilator_p11p13.sage -- B-side annihilator mirror (hermes-win,
# 2026-09-09). [mss-k34-c3ab-prep] cont. The B-side E_G-torsion annihilation
# at both tight primes (p=11 and p=13). B-side objects:
#   Q*_B: w^2 = 9v^4 - 56v^2 + 144 (Jac = E_G, same as A side).
#   E_G torsion: Z/4 + Z/2 (same curve). The B-side annihilator conditions are
#   the SAME integrals (same E_G!) — but the B-side MW lattice lives on
#   E'_iota = the C3_B/iota-quotient Jacobian (y^2 = x^3 - 1935360x + 1031648?
#   filed: I_1 = 71680 -> cubic y^2 = x^3 - 27*71680 x - 27*(-38273024)):
#   E'_iota: y^2 = x^3 - 1935360x + 1032916248? compute: -27*71680 = -1935360;
#   -27*(-38273024) = +1033571648? compute exactly below.
# The B-side annihilation: omega_G integrates to 0 over the B-side MW cycle's
# E_G-pushed image. The B-side E_G-torsion is the same torsion; the annihilation
# of the E_G MW part is IDENTICAL to A (same curve, same torsion). The
# B-specific content is the E'_iota-side generator and its pushed cycle.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

out('=== B1: E\'_iota exact model and rank ===')
I1, I2 = 71680, -38273024
EIOTA_B = EllipticCurve([0, 0, 0, -27*I1, -27*I2])
out('  E\'_iota: y^2 = x^3 + %d x + %d' % (-27*I1, -27*I2))
out('  j =', EIOTA_B.j_invariant())
try:
    rB = EIOTA_B.rank()
except RuntimeError:
    rB = 'unproven'
out('  rank:', rB, ' torsion:', EIOTA_B.torsion_subgroup())
out('  (filed: isogenous to master E_B, rank 1)')

out('=== B2: E_G torsion annihilation at p=11 (B-side = same curve) ===')
K = Qp(11, 8)
EGp = EG.change_ring(K) if (EG := EllipticCurve([0, 0, 0, -504576, 131604480])) else None
wG = EGp.invariant_differential()
Oinf = EGp(0)
for label, pt in [('(480,0)', EGp(480, 0)), ('(48,10368)', EGp(48, 10368)),
                  ('(336,0)', EGp(336, 0))]:
    try:
        val = wG.coleman_integral(Oinf, pt)
        out('  ∫_O^{%s} ω_G = %s' % (label, val))
    except Exception as e:
        out('  %s: %s' % (label, str(e)[:120]))

out('=== B3: E\'_iota generator and its period at p=11 ===')
try:
    EIBp = EIOTA_B.change_ring(K)
    gens = EIOTA_B.gens()
    if gens:
        Gb = EIpB = EIBp([QQ(gens[0][0]), QQ(gens[0][1])])
        wE = EIBp.invariant_differential()
        v = wE.coleman_integral(EIBp(0), Gb)
        out('  ∫_O^{G\'} ω_{E\'} =', v, ' (G\' =', gens[0], ')')
except Exception as e:
    out('  B3 error:', str(e)[:200])
out('=== DONE ===')