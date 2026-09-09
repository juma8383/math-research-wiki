# mss_c3a_iota_annihilation30.sage -- fix of v29's ring clash: the Newton
# iteration for the sqrt of the TOP coefficient mixed the Rk (X) and Rv (u)
# polynomial rings. Do the sqrt of the top coefficient in the RESIDUE FIELD
# + a clean K8-element Newton using only K8 scalars (not polynomials).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3x: clean monic normalization (all in K8 scalars) ===')
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
out('  true degree: %s' % d)
lc = f_tw.leading_coefficient()      # a K8 scalar
out('  lc type: %s' % type(lc).__name__)
# sqrt of the SCALAR lc via residue + Newton, all K8 scalars:
Fq = K8.residue_field()
s_res = Fq(lc).sqrt()
z = K8(s_res)
for _ in range(8):
    z = (z + lc/z) / 2
out('  sqrt(lc) = %s' % str(z)[:70])
ok = (z^2 - lc).valuation()
out('  check z^2 - lc valuation: %s (expect >= 9)' % ok)
f_final = f_tw / z        # divide the polynomial by the SCALAR sqrt(lc)
d2 = f_final.degree()
out('  after scalar division: degree %d ; leading %s' % (d2, str(f_final.leading_coefficient())[:50]))
# leading should now be exactly 1; verify:
if f_final.leading_coefficient() != K8(1):
    cl = f_final.list()
    cl = cl[:d2+1]
    cl[d2] = K8(1)
    f_final = Rv(cl)
out('  final degree: %d ; leading == 1: %s' % (f_final.degree(), f_final.leading_coefficient() == K8(1)))
Codd = HyperellipticCurve(f_final)
out('  is_ramified: %s' % Codd.is_ramified())
w = Codd.invariant_differential()
uu = 1/(0 - x0)
f_at = f_final(uu)
out('  f(u) valuation: %s' % f_at.valuation())
if f_at.valuation() == 0:
    s2_res = Fq(f_at).sqrt()
    v = K8(s2_res)
    for _ in range(8):
        v = (v + f_at/v) / 2
    P = Codd(uu, v)
    Q = Codd(uu, -v)
    val = Codd.coleman_integral(w, P, Q)
    out('  VERDICT INTEGRAL = %s' % val)
out('=== DONE ===')