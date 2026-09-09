# mss_c3a_iota_annihilation15.sage -- direct MW-ring construction: skip the
# HyperellipticCurve object entirely (its constructor's internal scaling is
# what breaks the wrapper's monic check) and instantiate
# SpecialHyperellipticQuotientRing on the RAW monic polynomial f_monic.
# The correct import names (from the module grep): SpecialHyperellipticQuotientRing
# exists; the differential class is SpecialCubicQuotientRingElement-based —
# differentials via HQR.gens() and the element .diff() methods.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3h: raw MW ring on the monic polynomial ===')
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
f_monic = f_new.monic()
out('  f_monic degree: %d ; leading: %s' % (f_monic.degree(), f_monic.leading_coefficient()))
from sage.schemes.hyperelliptic_curves import monsky_washnitzer as mw
try:
    HQR = mw.SpecialHyperellipticQuotientRing(f_monic)
    out('  HQR from raw polynomial: OK')
    xs, ys = HQR.gens()
    out('  gens: x = %s ; y = %s' % (str(xs)[:40], str(ys)[:40]))
    # invariant differential dx/(2y): the element (1) in the differential module:
    # the differential construction on SpecialHyperellipticQuotientElement:
    # w = dx/(2y): represented as HQR element with the .diff? Check methods:
    methods = [m for m in dir(HQR) if not m.startswith('_')]
    out('  HQR methods: %s' % methods[:20])
except Exception as e:
    out('  I3h error:', str(e)[:250])
out('=== DONE ===')