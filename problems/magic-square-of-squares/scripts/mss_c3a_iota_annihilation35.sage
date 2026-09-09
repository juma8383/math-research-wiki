# mss_c3a_iota_annihilation35.sage -- fix of v34: the `mw` module alias was
# never imported in the rewrites. Importing it explicitly at the top.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I4c: full chain with imports fixed ===')
from sage.rings.padics.factory import is_unramified
from sage.schemes.hyperelliptic_curves import monsky_washnitzer as mw
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
Rv2.<w2> = PolynomialRing(K8, 'w2')
f_new = Rv2(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*w2 + 1)^j * w2^(8 - j)
f_monic = f_new.monic()
out('  degree: %d ; len(list()): %s' % (f_monic.degree(), len(f_monic.list())))
cl = f_monic.list()
cl[-1] = K8(1)
f_final = Rv2(cl)
try:
    HQR = mw.SpecialHyperellipticQuotientRing(f_final)
    out('  HQR: OK')
    xs, ys = HQR.gens()
    out('  gens: OK')
except Exception as e:
    out('  I4 error:', str(e)[:250])
out('=== DONE ===')