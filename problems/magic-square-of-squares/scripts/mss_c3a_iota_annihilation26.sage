# mss_c3a_iota_annihilation26.sage -- the unramified OCTIC extension K8 of
# Q_11 (degree 8, containing K4 and sqrt(fp)): search an irreducible octic
# with is_unramified, then the FULL chain: root x0 lift, transform, monic,
# residue sqrt (in F_{11^8}, order 11^8-1: square test), Newton, on-curve,
# integral.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3t: unramified octic field ===')
from sage.rings.padics.factory import is_unramified
K11 = Qp(11, 9)
Rk.<X> = K11[]
modulus = None
for a in range(0, 11):
    if modulus is not None:
        break
    for bcoef in range(1, 11):
        P = X^8 + a*X^4 + bcoef
        if is_unramified(P):
            modulus = P
            out('  unramified octic: %s' % P)
            break
if modulus is None:
    for a in range(0, 11):
        if modulus is not None:
            break
        for bcoef in range(1, 11):
            P = X^8 + a*X + bcoef
            if is_unramified(P):
                modulus = P
                out('  unramified octic: %s' % P)
                break
if modulus is not None:
    K8.<y8> = Qp(11, 9).extension(modulus)
    out('  K8 = %s' % K8)
    poly = fA.change_ring(K8)
    rts = poly.roots()
    out('  roots over K8: %d' % len(rts))
    x0 = rts[0][0]
    Rv.<u> = K8[]
    f_new = Rv(0)
    for j in range(poly.degree() + 1):
        aj = poly[j]
        f_new += aj * (x0*u + 1)^j * u^(8 - j)
    fp = f_new.leading_coefficient()
    t = fp^((11^8 - 1)//2)
    out('  fp square in K8? %s' % (t == 1))
    if t == 1:
        Fq = K8.residue_field()
        z = K8(Fq(fp).sqrt())
        for _ in range(7):
            z = (z + fp/z) / 2
        f_mon2 = f_new.monic()
        lst2 = f_mon2.list()
        lst2[-1] = K8(1)
        f_final = Rv(lst2)
        Codd = HyperellipticCurve(f_final)
        w = Codd.invariant_differential()
        uu = 1/(0 - x0)
        vv = uu^4 / z
        diff = f_final(uu) - vv^2
        out('  on-curve check: %s' % str(diff)[:80])
        P = Codd(uu, vv)
        Q = Codd(uu, -vv)
        val = Codd.coleman_integral(w, P, Q)
        out('  INTEGRAL = %s' % val)
out('=== DONE ===')