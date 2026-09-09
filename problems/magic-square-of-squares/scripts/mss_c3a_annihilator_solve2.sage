# mss_c3a_annihilator_solve2.sage -- Coleman gate step 3: the annihilating
# kernel via CORRESPONDENCE trace (hermes-win, 2026-09-09). [mss-k34-c3ab-prep].
#
# Established so far: E_G torsion integrates to 0 under omega_G (S3 passed);
# E_iota period computed; even-degree C3_A integration unsupported (S1).
#
# THE KEY INSIGHT (tested here): omega_EG = pullback of E_G's invariant
# differential through the iota*rho quotient map C3_A -> Q_G (the third
# quotient). The pullback has degree 4, so for any cycle gamma on C3_A whose
# pushforward is (deg-gamma) * gamma_Q on Q:
#     int_gamma(C3_A)(rho_* eta) = deg * int_{gamma_Q}(eta)   [pushforward]
# The MW cycle (G_iota, 0, 0) pushes through iota∘rho to E_G as a POINT of
# E_G: specifically the map J(C3_A) -> E_G (Prym idempotent) sends the
# E_iota-side generator to a point of E_G -- which must be TORSION (rank 0).
# The annihilation condition int(omega_G) over MW basis = 0 is thus EQUIVALENT
# to: the pushed point in E_G is annihilated by the covering degree... NO --
# it is equivalent to the Abel-integral of omega_G over the pushed cycle
# vanishing, which happens iff the pushed cycle is torsion IN THE ABEL sense.
# Computable: the map iota-rho_* : E_iota -> E_G (an isogeny!) sends G_iota to
# a torsion point T. Then int(omega_G) over gamma_Giota = 4 * int_EG(O, T') = 0
# iff T' is torsion -- VERIFY by computing the isogeny composition and the
# image of G_iota in E_G exactly.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

out('=== T1: the iota-rho correspondence on elliptic curves EXACTLY ===')
# Q_iota: W^2 = v^4 + 132v^3 - 250v^2 + 132v + 1 (Jac = E_iota, genus 1 itself)
# Q_G: W^2 = -512u^4 + 128u^2 + 1 (Jac = E_G)
# Both Q_iota and Q_G are the SAME genus-1 curve (C3_A's two other involutions).
# The composition iota then rho acts on Q_iota as the order-2 involution of the
# genus-1 curve Q_iota -> its quotient is E_G. Explicitly: Q_iota = C3_A/<iota>
# carries an induced involution (rho mod iota), whose quotient is Q_G.
# On elliptic curves: E_G = Q_iota/<induced involution>, an isogeny of degree 2.
# The induced involution on Q_iota: compute its fixed points (Weierstrass pts).
# Q_iota IS the curve w^2 = v^4 + 132v^3 - 250v^2 + 132v + 1 -- genus 1 with the
# rational point... v=0: w^2=1 -> (0, ±1) rational. Take O' = (0,1) as origin.
out('  Q_iota : w^2 = v^4+132v^3-250v^2+132v+1, rational base point (0,1).')
# Elliptic model of Q_iota via its invariants:
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])
out('  E_iota j:', EIOTA.j_invariant(), ' E_G j:', EG.j_invariant())
out('  same j?', EIOTA.j_invariant() == EG.j_invariant())

out('=== T2: the isogeny phi: E_iota -> E_G (composition of the two 2-isogenies?) ===')
# If Q_iota and Q_G were the same curve, j would match. They do NOT:
# E_iota j = -8000/81, E_G j = 1556068/81. The induced involution quotient map
# Q_iota -> Q_G is then a 2-isogeny between DIFFERENT elliptic curves? A genus-1
# curve with a rational point, quotiented by an involution with rational fixed
# points, is genus 0 — UNLESS the involution is fixed-point-free (then quotient
# is again genus 1 = 2-isogenous copy). The iota-rho induced map on Q_iota:
# rho acts on Q_iota with NO fixed points (generic) => quotient = E_G, a
# 2-isogeny (actually an isogeny of degree 2? the map has degree 2).
# Compute the isogeny exactly via Sage's isogenies_prime_degree:
try:
    phis = EIOTA.isogenies_prime_degree(2)
    out('  2-isogenies from E_iota:', len(phis))
    for phi in phis:
        Ecod = phi.codomain()
        out('   codomain y^2 = x^3 + %d x + %d ; j = %s' %
            (Ecod[4], Ecod[6], Ecod.j_invariant()))
        if Ecod.j_invariant() == EG.j_invariant():
            G_iota = EIOTA(384, 13824)
            img = phi(G_iota)
            out('   -> this isogeny maps to E_G-model; image of G_iota:', img)
            out('   image torsion?', img.is_torsion(), ' order:', img.order() if img.is_torsion() else 'inf')
            # THE ANNIHILATION CONDITION:
            out('   ==> if img is torsion, omega_G annihilates the iota-side MW basis.')
            out('       (torsion Abel-integrals vanish: verified computationally in S3)')
except Exception as e:
    out('  T2 error:', str(e)[:200])

out('=== T3: same for the rho side ===')
try:
    for phi in EIOTA.isogenies_prime_degree(2):
        Ecod = phi.codomain()
        if Ecod.j_invariant() == EG.j_invariant():
            G_rho_candidate = phi(2*EIOTA(384, 13824))
            out('  rho-side image of 2G_iota:', G_rho_candidate,
                ' torsion?', G_rho_candidate.is_torsion())
except Exception as e:
    out('  T3 error:', str(e)[:200])
out('=== DONE ===')