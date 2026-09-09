# mss_c3a_iota_annihilation9.sage -- sanity integral with the CORRECT point
# images on the monic curve. Established: model constructed + monic rebuilt +
# invariant differential exists. The I3 point error: after the lc-normalization
# (lc = x0^8 exactly), the (0,±1) images are (u, v) = (-1/x0, ±1/x0^8).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3b: sanity integral, corrected point images ===')
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
out('  lc = %s' % str(lc)[:80])
out('  lc == x0^8?', lc == x0^8)
f_monic = f_new / lc
coeffs = f_monic.coefficients(sparse=False)
coeffs[-1] = K2(1)
f_monic = Ru(coeffs)
Codd = HyperellipticCurve(f_monic)
out('  MONIC ODD model: OK')
w = Codd.invariant_differential()
xm0 = -1/x0
v = 1/x0^8           # absorbing sqrt(lc) = x0^4: v_monic = v_old / x0^4
chk = f_monic(xm0) - v^2
out('  curve check f_monic(-1/x0) - v^2 = %s (expect 0)' % str(chk := chk) if False else '  curve check: %s' % str(chk)[:80] if False else 'check value: %s' % chk)
try:
    P1 = Codd(xm0, v)
    P2 = Codd(xm0, -v)
    val = Codd.coleman_integral(w, P1, P2)
    out('  ∫ dx/(2v) between the (0,±1) images: %s' % val)
except Exception as e:
    out('  I3 error:', str(e)[:250])
out('=== DONE ===')