# mss_c3a_iota_annihilation10.sage -- v computed IN SCRIPT from the curve:
# v = sqrt(f_monic(u)) at the image point u = -1/x0 (no hand-derived
# x0^8 assumption: lc is NOT x0^8 exactly — the printed lc differs).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3c: integral with in-script v ===')
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
f_monic = f_new / lc
coeffs = f_monic.coefficients(sparse=False)
coeffs[-1] = K2(1)
f_monic = Ru(coeffs)
Codd = HyperellipticCurve(f_monic)
w = Codd.invariant_differential()
out('  model OK, differential OK')
xm0 = -1/x0
# in-script point: v = a square root of f_monic(xm0):
f_at = f_monic(xm0)
out('  f_monic(xm0) = %s' % str(f_at)[:100])
vsq = f_at
# sqrt in K2 (Hensel if the residue is a square in the residue field F_121):
v = vsq.sqrt()
out('  v = %s' % str(v)[:100])
P1 = Codd(xm0, v)
P2 = Codd(xm0, -v)
val = Codd.coleman_integral(w, P1, P2)
out('  ∫ dx/(2v) between the (0,±1) images: %s' % val)
out('=== DONE ===')