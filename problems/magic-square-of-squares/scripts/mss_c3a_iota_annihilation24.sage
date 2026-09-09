# mss_c3a_iota_annihilation24.sage -- use the FACTORY's unramified constructor:
# Qp(11,8, print_mode=...) — the unramified extension ring is
# sage.rings.padics.factory.UnramifiedExtensionField: Qp(11, 8).unramified?
# Sage: from sage.rings.padics.factory import UnramifiedExtensionField as UE;
# K4 = UE(11, 4, 'y4', prec=8) — the unramified extension of degree 4.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3r: UnramifiedExtensionField factory ===')
from sage.rings.padics.factory import UnramifiedExtensionField
K4 = UnramifiedExtensionField(11, 4, 'y4', prec=8)
out('  K4 = %s' % K4)
poly = fA.change_ring(K4)
rts = poly.roots()
out('  roots over the unramified quartic: %d' % len(rts))
x0 = rts[0][0]
Rv.<u> = K4[]
f_new = Rv(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
fp = f_new.leading_coefficient()
t = fp^((11^4 - 1)//2)
out('  fp square in K4? %s' % (t == 1))
if t == 1:
    Fq = K4.residue_field()
    s_res = Fq(fp).sqrt()
    z = K4(s_res)
    for _ in range(6):
        z = (z + fp/z) / 2
    out('  sqrt(fp) = %s' % str(z)[:70])
    f_monic = f_new.monic()
    lst = f_monic.list()
    lst[-1] = K4(1)
    f_final = Rv(lst)
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