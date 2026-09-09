# mss_c3a_iota_annihilation8.sage -- MW monic check workaround: after dividing
# by the leading unit, REBUILD the polynomial from its coefficient list with
# the leading coefficient replaced by the literal integer 1 (the MW wrapper's
# monic check is exact `pop() != 1`; a padded p-adic unit (1+O(11^8)) fails it).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2i: monic rebuild with literal top coefficient ===')
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
lc = f_new.leading_coefficient()
f_div = f_new / lc
# rebuild with literal 1 as leading coefficient:
coeffs = f_div.coefficients(sparse=False)   # ascending
# verify the top entry is a unit ~1:
out('  top coeff before rebuild: %s' % coeffs[-1])
coeffs[-1] = K2(1)                          # literal exact 1
f_monic = Ru(coeffs)
out('  rebuilt leading: %s' % f_monic.leading_coefficient())
Codd = HyperellipticCurve(f_monic)
out('  MONIC ODD model: OK')
w = Codd.invariant_differential()
out('  invariant differential: %s' % str(w)[:120])
out('=== I3: sanity coleman integral (images of (0,±1)) ===')
try:
    xm0 = -1/x0
    v = (1/x0^4).sqrt()
    P1 = Codd(xm0, v)
    P2 = Codd(xm0, -v)
    val = Codd.coleman_integral(w, P1, P2)
    out('  ∫ dx/(2v) between the (0,±1) images: %s' % val)
except Exception as e:
    out('  I3 error:', str(e)[:250])
out('=== DONE ===')