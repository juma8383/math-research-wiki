# mss_c3a_iota_annihilation16.sage -- replicate the wrapper's monic check
# inline to see EXACTLY what it pops and why it fails.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3i: inline replication of the monic check ===')
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
out('  type(f_monic): %s ; parent: %s' % (type(f_monic).__name__, f_monic.parent()))
# the wrapper: R = Q.base_ring(); x = PolynomialRing(R, 'xx').gen(); Q.change_ring(R):
Rw = f_monic.base_ring()
out('  base_ring: %s' % Rw)
Q2 = f_monic.change_ring(K2)
out('  after change_ring: degree %s ; type %s' % (Q2.degree(), type(Q2).__name__))
cfl = Q2.coefficients(sparse=False)
out('  len(coefficients(sparse=False)): %d' % len(cfl))
out('  popped value: %s' % str(cfl[-1])[:100])
out('  popped != 1? %s' % (cfl.pop() != 1))
out('  popped == 1? %s' % (cfl.pop() if False else f_monic.leading_coefficient() == 1))
# ALSO: the wrapper Q.change_ring(R): R = Q.base_ring() — but in the HQR
# constructor, R is passed as None => R = Q.base_ring() = K2: same.
# The pop check uses != : for p-adics, != is numeric. So if pop == 1+O(11^8),
# != 1 should be False... test both on the actual element:
elt = Q2.leading_coefficient()
out('  direct: elt == 1 -> %s ; elt != 1 -> %s' % (elt == 1, elt != 1))
out('  type(elt): %s' % type(elt).__name__)
out('=== DONE ===')