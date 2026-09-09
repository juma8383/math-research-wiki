# mss_c3a_iota_annihilation13.sage -- bypass the monic check: call
# SpecialHyperellipticQuotientRing with R = the p-adic base and Q = a REBUILT
# polynomial whose coefficients list ends in the LITERAL 1 AND whose length
# is exactly 8 (degree 7). The wrapper scales internally? The KeyError trace
# showed the curve rescaled by (1+O(11^8)): pass the curve object directly
# (the HyperellipticCurve branch) — C.hyperelliptic_polynomials()[0] — that's
# f as given. The pop() got (1+O(11^8))? The print of the curve shows
# '(1+O(11^8))*y^2 = ...' — the CURVE ITSELF stores the equation with the
# (1+O(11^8)) factor on y^2: i.e. the constructor turned my f_monic into
# (1+O(11^8))*y^2 = f_monic — the hyperelliptic_polynomials()[0] is then
# f_monic/(1+O(11^8)) = f_monic — hmm. Try the DIRECT route: skip the curve;
# pass the polynomial Q directly to SpecialHyperellipticQuotientRing (it
# accepts a polynomial!) — then build the MW cohomology from it.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3f: direct SpecialHyperellipticQuotientRing route ===')
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
f_monic = f_new / f_new.leading_coefficient()
d = f_monic.degree()
c_list = f_monic.coefficients(sparse=False)
c_list[d] = K2(1)
f_monic = Ru(c_list)
out('  f_monic degree: %d ; leading: %s' % (f_monic.degree(), str(f_monic.leading_coefficient())[:60]))
from sage.schemes.hyperelliptic_curves.monsky_washnitzer import (
    SpecialHyperellipticQuotientRing, SpecialMonskyWashnitzerDifferential)
try:
    HQR = SpecialHyperellipticQuotientRing(f_monic)
    out('  HQR constructed DIRECTLY from the monic polynomial: OK')
    out('  HQR = %s' % str(HQR)[:120])
    # the invariant differential in the MW ring:
    x, y = HQR.gens()
    w = SpecialMonskyWashnitzerDifferential(HQR, HQR.one())
    out('  MW differential 1 dx/2y:', w)
    out('  => MW ring ready WITHOUT the HyperellipticCurve constructor')
except Exception as e:
    out('  direct HQR error:', str(e)[:250])
out('=== DONE ===')