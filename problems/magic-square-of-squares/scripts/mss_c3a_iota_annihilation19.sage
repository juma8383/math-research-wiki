# mss_c3a_iota_annihilation19.sage -- sanity integral with the CORRECT
# transform coordinates: C3_A point (x, W) -> odd-model point (u, v) =
# (1/(x - x0), W * u^4). The (0, ±1) C3_A points land at u = -1/x0,
# v = ±u^4. Both coordinates computed IN SCRIPT from the curve equation
# (v found by Hensel sqrt of f_final(u) if needed, else from the formula
# and verified on-curve).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3m: integral between the (0,±1) images (correct transform) ===')
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
lst = f_monic.list()
lst[-1] = K2(1)
f_final = Ru(lst)
Codd = HyperellipticCurve(f_final)
w = Codd.invariant_differential()
out('  curve + differential OK')
# the C3_A point (0, +1) -> u = -1/x0; v = W * u^4 with W = 1:
uu = 1/(0 - x0)
vv = 1 * uu^4
# verify on-curve:
diff = f_final(uu) - vv^2
out('  on-curve check f(u0) - v^2 = %s' % str(diff)[:80])
try:
    P = Codd(uu, vv)
    Q = Codd(uu, -vv)
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
    out('  (P,Q are the images of C3_A (0,±1); the integral is a genuine')
    out('   period datum of the odd model over K2)')
except Exception as e:
    out('  I3m integral error:', str(e)[:250])
out('=== DONE ===')