# mss_c3a_iota_annihilation32.sage -- the decisive diagnostic, with the
# import restored (v31 lost it in the rewrite).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3z: the two coefficient-list routes ===')
from sage.rings.padics.factory import is_unramified
K11 = Qp(11, 10)
Rk.<X> = K11[]
modulus = None
for a in range(0, 11):
    if modulus is not None:
        break
    for bcoef in range(2, 11):
        P = X^8 + a*X + bcoef
        if is_unramified(P):
            modulus = P
            break
K8.<y8> = Qp(11, 10).extension(modulus)
poly = fA.change_ring(K8)
rts = poly.roots()
x0 = rts[0][0]
Rv.<u> = K8[]
f_new = Rv(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
f_tw = f_new.monic()
d = f_tw.degree()
out('  degree: %d' % d)
out('  len(.list()): %s' % len(f_tw.list()))
cfl = f_tw.coefficients(sparse=False)
out('  len(coefficients(sparse=False)): %s' % len(cfl))
Codd = HyperellipticCurve(f_tw)
f_c, h_c = Codd.hyperelliptic_polynomials()
out('  curve poly degree: %s' % f_c.degree())
out('  curve poly len(list()): %s' % len(f_c.list()))
out('  curve poly leading: %s' % str(f_c.leading_coefficient())[:60])
Q2 = f_c.change_ring(K8)
c2 = Q2.coefficients(sparse=False)
out('  wrapper-replica: len = %s ; popped == 1? %s' % (len(c2), c2.pop() == 1))
f2l = f_c.list()
f2l[-1] = K8(1)
f2 = Rv(f2l)
out('  rebuilt: degree %d ; leading %s' % (f2.degree(), f2.leading_coefficient()))
try:
    HQR = mw.SpecialHyperellipticQuotientRing(f2)
    out('  HQR on rebuilt poly: OK')
except Exception as e:
    out('  HQR still failing: %s' % str(e)[:150])
out('=== DONE ===')