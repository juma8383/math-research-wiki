# mss_c3a_iota_annihilation7.sage -- odd model MONIC-normalized (fix of v6:
# "polynomial must be monic" — the MW integrator needs the Weierstrass f monic).
# v6 succeeded: odd model CONSTRUCTED (degree 7!). Only the leading coefficient
# isn't 1: f_new has leading coeff ((4c+3)+...)*u^7 — normalize by the leading
# unit (it's a p-adic UNIT: 4c+3 has valuation 0) — divide through.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2h: odd model, monic-normalized ===')
K11 = Qp(11, 8)
Rk.<X> = K11[]
K2.<c> = K11.extension(X^2 - 7)
poly = fA.change_ring(K2)
rts = poly.roots()
x0 = rts[0][0]
Ru.<u> = K2[]
f_new = Ru(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
out('  raw degree: %d ; leading coeff unit? valuation = %s'
    % (f_new.degree(), (f_new.leading_coefficient()).valuation()))
lc = f_new.leading_coefficient()
f_monic = f_new / lc
out('  monic: %s' % f_monic)
Codd = HyperellipticCurve(f_monic)
out('  MONIC ODD model: OK')
w = Codd.invariant_differential()
out('  invariant differential: %s' % w)
out('  => COLEMAN MACHINERY READY on the odd model (monic, degree 7, genus 3)')
out('=== I3: sanity coleman integral on the odd model (mechanism probe) ===')
try:
    # a small integral: between the images of the known C3_A points?
    # (0, ±1) on C3_A maps to u = 1/(0 - x0) = -1/x0: NOT a K2-rational issue —
    # it IS K2-rational. W -> W/(x-x0)^4: W=±1 -> v = ±1/(x0)^4... compute:
    xm0 = -1/x0     # u-coordinate of the C3_A point x=0
    # v = W/(x-x0)^4 with x=0: W=±1, x-x0 = -x0: v = ±1/(-x0)^4 = ±1/x0^4
    v1 = (1/x0^4)
    # is (u, v) = (xm0, v) on Codd? v^2 = f_monic(u)? f_monic = u^8 f(x0+1/u)/lc:
    # at u = -1/x0: f(0)=1 -> the transformed: v^2 = (x-x0)^{-8} f(x) = 1/x0^8:
    out('  check: v^2 should be 1/x0^8 = %s' % (1/x0^8))
    P1 = Codd(xm0, v1 := (1/x0^4).sqrt())
    P2 = Codd(xm0, -(1/x0^4).sqrt())
    val = Codd.coleman_integral(w, P1, P2)
    out('  ∫ dx/(2v) from P to P-bar (odd model, p=11): %s' % val)
except Exception as e:
    out('  I3 error:', str(e)[:250])
out('=== DONE ===')