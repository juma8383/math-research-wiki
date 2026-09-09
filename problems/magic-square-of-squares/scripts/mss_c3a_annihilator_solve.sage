# mss_c3a_annihilator_solve.sage -- Coleman gate step 2: solve for omega
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] continuation of §2ab.
#
# SETUP (filed §2ab): J(C3_A)(Q) = <(G_iota,0,0), (0,G_rho,0)> rank 2;
# H0(Omega) = <dx/W, x dx/W, x^2 dx/W> dim 3. The annihilating omega is the
# kernel of the 2x3 period matrix M_ij = int_{gamma_j}(omega_i) evaluated
# p-adically at p = 11 via Abel-Jacobi: int_{base}^{Abel(basis-point)} omega_i.
#
# The Abel-Jacobi image of a J-point (D - deg(D)*inf) integrates each omega_i
# from the infinity divisor to the divisor D. For the iota-side basis point
# (G_iota, 0, 0): realized as div(P) - div(inf) for the C3_A-point P lying
# over G_iota. Constructing that C3_A point EXACTLY: the iota-quotient maps
# C3_A -> Q_iota (v = x^2). A point (v0, w0) on Q_iota lifts to C3_A points
# (x, W) with x^2 = v0: over Q only when v0 is a square. G_iota = (384, 13824):
# v0 = 384 = 64*6 not a rational square -> the iota-side basis point is not
# liftable to a single C3_A point; the Abel-Jacobi integration on the genus-3
# curve must go through the CORRESPONDENCE, or be done intrinsically via
# Coleman integration on C3_A itself (even degree, no odd model).
#
# PRACTICAL RESOLUTION (this script): the even-degree obstruction is real but
# the COLEMAN INTEGRATION on C3_A over Qp is still possible via Sage's
# C.coleman_integral with an odd differential choice -- we probe whether the
# Sage API accepts even-degree curves at all (filed §2aa E: constructs OK).
# If not, the gate runs on the QUOTIENT curves where everything is classical:
#   - E_iota-side annihilation is VACUOUS (omega_i = the pullback of the
#     quotient differential; its integrals against iota-side MW classes are
#     the classical elliptic integrals, computable at any precision).
#   - The REAL content: omega_G (the E_G-side differential) must annihilate
#     the FULL MW lattice: int(omega_EG) over (G_iota,0,0) = 0 AND
#     int(omega_EG) over (0,G_rho,0) = 0. On the E_G side rank is 0, so
#     omega_EG automatically annihilates the E_G part; the conditions are
#     the two integrals above -- computable via the CORRESPONDENCE
#     (divisor-level pullback): int_{C3_A}(pullback eta) over gamma =
#     deg * int_{Q}(eta) over the pushed cycle. EXACTLY computable.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])

out('=== S1: does Sage coleman_integral accept the EVEN-degree C3_A? ===')
K = Qp(11, 8)
try:
    C3Ap = HyperellipticCurve(fA).change_ring(K)
    try:
        w = C3Ap.invariant_differential()
        out('  invariant_differential:', w)
    except Exception as e:
        out('  invariant_differential error:', str(e)[:160])
    try:
        # affine C3_A points with rational coords: x=0 -> W^2=1 -> (0, ±1)
        P = C3Ap(K(0), K(1))
        Q = C3Ap(K(0), K(-1))
        xw, yw = C3Ap.monsky_washnitzer_gens()
        wdx = C3Ap.coleman_integral(w, P, Q)
        out('  ∫ dx/W from (0,1) to (0,-1) at p=11:', wdx)
    except Exception as e:
        out('  even-degree integral error:', str(e)[:250])
except Exception as e:
    out('  construct error:', str(e)[:200])

out('=== S2: classical quotient-side integrals (E_iota, p=11) ===')
try:
    EIp = EIOTA.change_ring(K)
    Gi = EIp([QQ(384), QQ(13824)])
    Oinf = EIp(0)
    wE = EIp.invariant_differential()
    v1 = wE.coleman_integral(Oinf, Gi)
    out('  ∫_O^{G_iota} ω_E =', v1)
    v2 = wE.coleman_integral(Oinf, 2*Gi)
    out('  ∫_O^{2G_iota} ω_E =', v2, ' (linearity check: =', 2*v1, ')')
except Exception as e:
    out('  S2 error:', str(e)[:200])

out('=== S3: E_G torsion integrals (should be torsion multiples => zero) ===')
try:
    EGp = EG.change_ring(K)
    wG = EGp.invariant_differential()
    for label, pt in [('T2=(480,0)', EGp(480, 0)), ('T2b=(-816,0)', EGp(-816, 0))]:
        try:
            OinfG = EGp(0)
            val = wG.coleman_integral(OinfG, pt)
            out('  ∫_O^{%s} ω_G = %s (expect O(11^8): Weierstrass endpoints need odd w)' % (label, val))
        except Exception as e:
            out('  %s: %s' % (label, str(e)[:150]))
    # order-4 point (48, 10368):
    try:
        P4 = EGp(48, 10368)
        val4 = wG.coleman_integral(EGp(0), P4)
        out('  ∫_O^{(48,10368)} ω_G =', val4, '(expect 0: order-4 point)')
    except Exception as e:
        out('  order-4 integral error:', str(e)[:200])
except Exception as e:
    out('  S3 error:', str(e)[:200])
out('=== DONE ===')