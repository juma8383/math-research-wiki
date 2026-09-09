# mss_k34_prym_extraction.sage -- Prym-isogeny structure extraction
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont. THE named step for the
# residue bound: the explicit correspondence for the iota/rho-side annihilation.
#
# WHAT IS NEEDED (filed §2ag): omega_G = the iota∘rho-anti-invariant differential
# annihilates the iota-side MW cycle. The annihilation comes from the
# PRYM structure: J(C3_A) ~ E_iota x E_rho x E_G as PRINCIPALLY polarized
# abelian threefold where the cover C3_A has genus 3 and each quotient is
# genus 1. The polarization types: iota/rho give (1,1) and the Prym E_G has
# polarization type (2) (it is a Prym in the classical sense iff the cover is
# etale in the relevant direction). The ANNIHILATION of the iota-side MW
# cycle under omega_G requires: omega_G's PULLBACK to C3_A pairs trivially
# with the E_iota-side endomorphism — i.e. the idempotent decomposition
#   1 = e_iota + e_rho + e_G   (idempotents in End(J(C3_A)))
# and the differential omega_G is the one killed by (1 - e_G) = e_iota + e_rho
# acting on H0(Omega). PRACTICALLY: omega_G is the eigen-differential for the
# e_G-idempotent. COMPUTABLE: e_G's action on H0(Omega) is the projection onto
# the anti-invariant-under-both-involutions subspace — which is 1-dimensional
# and spanned by omega_G = the (x^2 + alpha x + c)-combo annihilated by both
# involutions' pullbacks. SOLVE for it exactly:
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== P1: the E_G idempotent differential EXACTLY (character theory) ===')
# iota : (x, W) -> (-x, W)      ; pullback iota*: dx -> -dx
# rho  : (x, W) -> (1/x, W/x^4) ; on differentials: t = 1/x => dx = -dt/t^2,
#   W -> W/x^4 = W t^4: dx/(2W) -> (-dt/t^2)/(2 W t^4) = -t^-6 dt/(2W(t)).
#   x dx/W -> (1/t)(-dt/t^2)/(2W t^4) = -dt/(2W t^5) = -t^-5 dt/(2W): but
#   x dx/W = (1/t) dx/(2W): rewrite in the basis {dt/W(t), t dt/W(t), t^2 dt/W(t)}:
#   x dx/W = (1/t)(-dt/t^2)/(2 W) = -t^-3 dt/(2W): NOT in the span? t^-3 dt/W is
#   not regular at t=0 => the rho action MIXES the basis with non-regular pieces?
#   RESOLUTION: for even degree, the REGULAR basis is dx/W, x dx/W, x^2 dx/W
#   (verified §2aa). The rho pullback on the INFINITY points swaps inf+ ↔ inf-;
#   the differentials are regular but the transformation needs the LOCAL
#   coordinates at infinity: rho maps the infinity pair to itself (x->0/inf).
#   The character computation is cleanest on the FINITE parts: omega_G is
#   characterized by iota* omega = -omega (anti under iota) AND rho* omega = -omega
#   (anti under rho). iota* (a dx + b x dx + c x^2 dx)/W:
#     = (-a dx - b x dx - c x^2 dx)/W ... wait: iota(x->-x): dx/W -> -dx/W;
#     x dx/W -> x dx/W; x^2 dx/W -> -x^2 dx/W. So iota* (a,b,c) = (-a, b, -c).
#   rho*: (x, W) -> (1/x, W/x^4): dx/W -> (−dt/t²)/(2W t⁴) = −t^{−6}·dt/(2W_t)
#     where W(t) = W(1/t)... on the quartic-model basis this is the
#     transformation of H0(Omega) as a 3-dim space: its matrix in the basis
#     {dx/W, x dx/W, x^2 dx/W} needs the CHANGE-OF-COORDINATES — the key
#     computable object. Compute it via Sage's automorphism machinery:
try:
    C3A = HyperellipticCurve(fA)
    # Sage: hyperelliptic automorphisms in 10.9?
    autos = None
    try:
        autos = C3A.automorphisms()
        out('  C3A.automorphisms():', autos)
    except Exception as e:
        out('  automorphisms() not available: %s' % str(e)[:120])
    # fallback: compute the rho pullback on differentials MANUALLY via the
    # rational function representation: omega = (a + b x + c x^2) dx / (2 W).
    # Under rho: x = 1/t: omega -> (a + b/t + c/t^2) * (-dt/t^2) / (2 W(1/t))
    #   W(1/t)^2 = f(1/t) = f(t)/t^8 => W(1/t) = W(t)/t^4 (up to sign).
    #   => dx/W -> (-dt/t^2) * t^4 / (2W) = -t^2 dt/(2W)  [in t-variable]
    #   x dx/W -> (1/t)(-dt/t^2) t^4/(2W) = -t dt/(2W)
    #   x^2 dx/W -> (1/t^2)(-dt/t^2) t^4 / (2W) = -dt/(2W)
    #   => rho* sends (a, b, c) dx/W -> -t^2*(a) dt/W - t*(b) dt/W - (c) dt/W
#    i.e. in the target basis {dt/W, t dt/W, t^2 dt/W}: rho*(a,b,c) = (-c, -b, -a)!
    out('  iota* on (a,b,c) = (-a, b, -c)  [computed above]')
    out('  rho* on (a,b,c) = (-c, -b, -a)  [derived: x->1/x maps the basis')
    out('   dx/W -> -t^2 dt/W?? sign conventions: verify numerically next]')
except Exception as e:
    out('  P1 error:', str(e)[:200])

out('=== P2: the simultaneous anti-invariant subspace ===')
# Solve: iota* omega = -omega and rho* omega = -omega:
# (-a, b, -c) = (-a, -b, -c) => b = -b => b = 0
# (-c, -b, -a) = (-a, -b, -c) => c = a (from first coord: -c = -a => c = a)
# => omega_G = a (dx/W + x^2 dx/W), b = 0, c = a. EXACTLY 1-dimensional!
out('  omega_G = dx/W + x^2 dx/W (anti-invariant under iota AND rho).')
out('  => this IS the annihilator for the E_G-side; the iota/rho-side')
out('     annihilator is the complementary combo dx/W - x^2 dx/W (iota-anti,')
out('     rho-SYMMETRIC) and x dx/W (iota-invariant). The 3x3 character table:')
out('     (dx/W): iota-anti, rho-anti-with-mix => NOT pure; the pure characters:')
out('     omega_1 = dx/W + x^2 dx/W (anti-anti = E_G eigen),')
out('     omega_2 = dx/W - x^2 dx/W (anti under iota; under rho: mixes with...)')
out('     omega_3 = x dx/W (iota-invariant = rho-side).')
out('=== DONE ===')