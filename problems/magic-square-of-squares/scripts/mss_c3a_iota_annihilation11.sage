# mss_c3a_iota_annihilation11.sage -- sanity integral between the two
# INFINITY-point images at u = 0 on the odd model: P = Codd(0, 1),
# Q = Codd(0, -1) (both K2-rational, no sqrt needed — f_monic(0) = 1 exactly).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3d: integral between the infinity images (u=0) ===')
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
out('  f_monic(0) = %s (expect the transformed constant: f(0)/lc·...)' % str(f_monic(0))[:90])
try:
    P = Codd(K2(0), K2(1))
    Q = Codd(K2(0), K2(-1))
    out('  points P=(0,1), Q=(0,-1) constructed OK')
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
    out('  (this is the sanity integral: two K2-rational points, same u)')
except Exception as e:
    out('  I3d error:', str(e)[:250])
out('=== DONE ===')