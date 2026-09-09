# mss_c3a_iota_annihilation12.sage -- monic fix v2: replace the coefficient at
# index = f_monic.degree() (not coeffs[-1], which is padding-sensitive).
# Also print the degree and leading coefficient before/after.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3e: correct monic normalization ===')
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
out('  f_new degree: %d ; f\'(x0) = leading = %s' % (f_new.degree(), str(f_new.leading_coefficient())[:80]))
f_monic = f_new / f_new.leading_coefficient()
d = f_monic.degree()
out('  f_monic degree: %d' % d)
out('  f_monic leading (index %d): %s' % (d, f_monic.coefficient(d)))
out('  f_monic leading == 1?', f_monic.coefficient(d) == 1)
if f_monic.coefficient(d) != 1:
    # replace just that coefficient via the polynomial constructor:
    c_list = f_monic.coefficients(sparse=False)
    d_idx = d
    c_list[d_idx] = K2(1)
    f_monic = Ru(c_list)
    out('  replaced coefficient at index %d with literal 1' % d_idx)
    out('  new degree: %d ; new leading: %s' % (f_monic.degree(), f_monic.coefficient(f_monic.degree())))
Codd = HyperellipticCurve(f_monic)
w = Codd.invariant_differential()
out('  model + differential OK')
P = Codd(K2(0), K2(1))
Q = Codd(K2(0), K2(-1))
val = Codd.coleman_integral(w, P, Q)
out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
out('=== DONE ===')