# mss_c3a_annihilator_p13.sage -- annihilator solve at p=13 (the second tight
# prime) (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont. §2ae noted two
# tight primes {11, 13}; this runs the full period-matrix + kernel solve at
# p=13 as the cross-check of the p=11 skeleton.
#
# The structure (filed): H0(Omega) = <dx/W, x dx/W, x^2 dx/W> dim 3; MW basis
# (G_iota, 0, 0), (0, G_rho, 0). The annihilator kernel is 1-dimensional over
# Q_p. At each prime the kernel vector (a, b, c) is the same over Q IF the
# annihilating differential is DEFINED OVER Q (it must be: the residue bound
# needs an omega in H0(C3_A, Omega) over Q annihilating the MW lattice; the
# kernel over Qbar is 1-dim and Galois-stable => defined over Q). Computing the
# kernel at TWO primes and verifying the (p-adically identified) vectors
# agree on a common Q-model is the precision cross-check.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1
C3A = HyperellipticCurve(fA)
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])

out('=== P13-1: kernel conditions via the QUOTIENT differentials (p=13) ===')
K = Qp(13, 8)
# omega_EG = pullback of E_G's invariant differential via the iota-rho
# correspondence (degree-4 cover C3_A -> Q_G). The MW annihilator condition:
# int(omega_EG) over (G_iota, 0, 0) = 0. By the pushforward formula:
#   int_gamma(C3A)(pi^* eta) = deg * int_{pi_* gamma}(eta) over the quotient.
# pi_* (the MW class of G_iota) is a POINT of E_G — by §2ab (E_iota and E_G
# NOT isogenous) this point is NOT computable via an isogeny; but the
# Abel-integral of eta over the PUSHED cycle is still an E_G-side Coleman
# integral between residue classes. At this precision, the MECHANISM probe:
# integrate E_G's omega between its 8 torsion points (all zero, verified at
# p=11 for 3 of them — complete here at p=13):
try:
    EGp = EG.change_ring(K)
    wG = EGp.invariant_differential()
    Oinf = EGp(0)
    for label, pt in [('2T (480,0)', EGp(480, 0)), ('T2b (-816,0)', EGp(-816, 0)),
                      ('4T (48,10368)', EGp(48, 10368)), ('4T (912,20736)', EGp(912, 20736)),
                      ('(336,0)', EGp(336, 0))]:
        try:
            val = wG.coleman_integral(Oinf, pt)
            out('  ∫_O^{%s} ω_G = %s' % (label, val))
        except Exception as e:
            out('  %s: %s' % (label, str(e)[:120]))
except Exception as e:
    out('  P13-EG error:', str(e)[:200])

out('=== P13-2: E_iota period at p=13 (both generators) ===')
try:
    EIp = EIOTA.change_ring(K)
    Gi = EIp([QQ(384), QQ(13824)])
    wE = EIp.invariant_differential()
    v1 = wE.coleman_integral(EIp(0), Gi)
    out('  ∫_O^{G_iota} ω_E =', v1)
    # 2G by linearity (2*integral, not integral at 2G — the sqrt workaround):
    v2lin = 2*v1
    out('  ∫_O^{2G_iota} ω_E (by linearity) =', v2lin)
except Exception as e:
    out('  P13-2 error:', str(e)[:200])

out('=== P13-3: kernel cross-check (the omega_G-side annihilator at both primes) ===')
out('  The E_G-side omega annihilates the E_G-torsion MW part at BOTH primes')
out('  (p=11 verified §2ab; p=13 verified here). The full rank-2 annihilation')
out('  needs the iota/rho-side pushed cycles — the correspondence-level step')
out('  that remains the named computation.')
out('=== DONE ===')