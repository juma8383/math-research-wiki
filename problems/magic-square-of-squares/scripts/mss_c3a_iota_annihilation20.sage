# mss_c3a_iota_annihilation20.sage -- resolve the twist: is f'(x0) a square
# in K2? If yes: v_final = W u^4 / sqrt(f'(x0)) lands on the monic model.
# If no: the odd model over K2 is a nontrivial twist; then construct the
# odd model over the ramified quadratic extension K2(sqrt(f'(x0))) where
# the transform is exact.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3n: the twist check ===')
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
fp = f_new.leading_coefficient()     # ~ f'(x0) up to the unit normalization
out('  lc (= f\'(x0)-unit) = %s' % str(fp)[:80])
try:
    s = fp.sqrt()
    out('  sqrt(fp) = %s' % str(s)[:80])
    out('  => lc IS a K2-square; the monic model point images:')
    uu = 1/(0 - x0)
    vv = 1 * uu^4 / s
    diff = f_new.monic()(uu) - vv^2
    out('  on-curve check (monic model): %s' % str(diff)[:80])
    f_final = f_new.monic()
    lst = f_final.list(); lst[-1] = K2(1)
    f_final = Ru(lst)
    Codd = HyperellipticCurve(f_final)
    w = Codd.invariant_differential()
    P = Codd(uu, vv)
    Q = Codd(uu, -vv)
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
except Exception as e:
    out('  I3n error:', str(e)[:250])
out('=== DONE ===')