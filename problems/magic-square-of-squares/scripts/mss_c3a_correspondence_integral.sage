# mss_c3a_correspondence_integral.sage -- the correspondence-level integral:
# pushforward of the iota-side MW cycle under the iota-rho cover C3_A -> Q_G
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont. THE named step.
#
# Structure: Q* (= Q_G model: w^2 = v^4+136v^2+16) is the iota-rho quotient of
# C3_A. The quotient map pi: C3_A -> Q_G has degree 4 (compose the two
# involutions). For the MW cycle gamma = Abel-image of (G_iota, 0, 0) in
# J(C3_A), the pushforward pi_* gamma is a 1-cycle on Q_G ~ E_G. Since
# rank E_G = 0, pi_* gamma is TORSION in E_G — hence ∫_{pi_* gamma} omega_G
# = 0, hence ∫_gamma (pi^* omega_G) = 4 · 0 = 0: the pullback differential
# annihilates the iota-side MW class. THE COMPUTATION: verify pi_* gamma is
# torsion by computing its image EXACTLY. The pushforward on divisor classes:
# pi_*( [P] - [P0] ) = [pi(P)] - [pi(P0)] as E_G-points via the Abel map of
# Q_G based at pi(P0).
#
# CONCRETE REALIZATION: the iota-quotient Q_iota = w^2 = v^4+132v^3-250v^2+132v+1
# has Jacobian E_iota (rank 1, gen G_Q = the image of G_iota). The SECOND
# involution rho acts on Q_iota; its quotient is Q_G. On elliptic models the
# map Q_iota -> Q_G is a morphism of genus-1 curves sending O' to O'' —
# equivalently an isogeny E_iota' -> E_G where E_iota' is Q_iota's elliptic
# model with the RIGHT base point. (§2ac found E_iota and E_G not isogenous —
# BUT that compared the CUBIC MODELS with different chosen origins. The
# genus-1 curves Q_iota and Q_G are DIFFERENT CURVES (different quartics),
# so the map between their Jacobians need not be an isogeny of the cubics
# E_iota -> E_G as filed. RESOLVE: compute both elliptic models IN SAGE from
# the quartics directly (Jacobian of the genus-1 curve with rational point),
# then the pushforward map on MW points via the CORRESPONDENCE between the
# two genus-1 curves (compute the function field map explicitly).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<v> = QQ[]
f_iota = v^4 + 132*v^3 - 250*v^2 + 132*v + 1
f_G    = -512*v^4 + 128*v^2 + 1        # Q_G in ascending-> HyperellipticCurve form
out('=== C1: both genus-1 curves in Sage; Jacobians via mwrank ===')
Q_iota = HyperellipticCurve(f_iota)
Q_G    = HyperellipticCurve(-512*v^4 + 128*v^2 + 1)
out('  Q_iota:', f_iota)
out('  Q_G   :', -512*v^4 + 128*v^2 + 1)
# The rho action on Q_iota: (v, w) -> ??? rho on C3_A is (x, W)->(1/x, W/x^4);
# in the quotient v = x^2, the induced action sends v -> 1/v, w -> w/v^2:
# Q_iota is invariant: f_iota(1/v)*v^4 = 1 + 132v^2 - 250v^4 + 132v^6 + v^8?
# CHECK: f_iota is NOT palindromic (132v^3 term). So rho does NOT descend to
# Q_iota! The correct second involution on Q_iota comes from the composition
# iota*rho acting on C3_A: (x, W) -> (1/x, W/x^4); mod iota (x->-x): the
# induced map on Q_iota is (v, w) -> (1/v, w/v^2) — and f_iota(1/v) v^4 =
# 1 + 132v^2 - 250v^4 + 132v^6 + v^8 ≠ f_iota(v). => the iota-rho quotient is
# NOT directly Q_iota/<rho> — the two involutions do NOT commute? They do:
# iota and rho commute on C3_A (check: iota(rho(x)) = iota(1/x) = ±1/x; the
# sign from iota is (x -> -x): iota(rho(P)) = (1/x?, ...). The composition
# iota∘rho = (x, W) -> (1/x, W/x^4); applying to -x: iota acts by x->-x,
# rho by x->1/x: iota(rho(P)) = (-1/x, W/x^4); rho(iota(P)) = (1/(-x), W/x^4)
# = (-1/x, W/x^4). EQUAL: they commute. So rho DOES descend to Q_iota = C3_A/iota.
# The induced action: v = x^2 -> rho gives v -> 1/x^2 = 1/v. w = W (iota-invariant)
# -> w -> W/x^4 = w/v^2. So on Q_iota: (v, w) -> (1/v, w/v^2).
# The rho-invariant quotient: v + 1/v = u: the G-quartic f_G(u) = u^4+128u^2-512.
# EXACT check: w^2 = f_iota(v); under the map (v,w)->(1/v, w/v^2):
#   (w/v^2)^2 = f_iota(v)/v^4. With u = v + 1/v: the u-quotient of Q_iota is
#   the curve w'^2 = ? Compute: f_iota(v)/v^4 = (v + 1/v)^2... verify symbolically:
u = var('u')
expr = expand(f_iota(v) * (1/v^4))  # this is f_iota in terms of u = v+1/v?
# f_iota(v) = v^4(1 + 132(1/v)... let's verify: f_iota(v)/v^4 with u = v + 1/v:
# f_iota = v^4 + 132v^3 - 250v^2 + 132v + 1: divide by v^2:
#   = v^2 (u^2 - 2) + 132 v (u - 1/v)?? Just expand u^4 + 128u^2 - 512 * v^4:
expr2 = expand((u^4 + 128*u^2 - 512).subs(u == v + 1/v) * v^4)
out('  f_iota(v) - v^4*D(u) with u=v+1/v:', expand(f_iota - expr2))
out('  (if 0: the iota-rho quotient is the G-quartic in u = v + 1/v, i.e. the')
out('   SECOND involution on Q_iota is u = v + 1/v — matching the filed')
out('   identity g = x^4 G(x+1/x) with G the [1,0,128,0,-512] quartic!)')
out('=== DONE ===')