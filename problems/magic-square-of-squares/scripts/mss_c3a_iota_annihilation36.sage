# mss_c3a_iota_annihilation36.sage -- HQR WORKS. Now the actual integral.
# The MW ring route: the differential w = dx/(2y) is HQR's identity element
# in the differential sense; Sage's MW machinery computes integrals via the
# Frobenius on H1: mw.frobenius_expansion_by_newton(Q, p, M) + the reduction
# functions, then the pairing between the Abel image and the differential.
# The cleanest executable route with the WORKING curve object: build the
# curve from f_final (the fresh-ring poly — its constructor rescale issue
# may vanish now that the list is honest), then C.coleman_integral.
# The POINT images: C3_A (x, W) -> (u, v) = (1/(x-x0), W*u^4/ sqrt-normalized):
# with the fresh ring's honest coefficients, compute v by Hensel on the
# curve at u = -1/x0 (image of the affine C3_A point (0, ±1)).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I5: the integral on the working model ===')
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
cl = f_monic.list()
cl[-1] = K8(1)
f_final = Rv2(cl)
Codd = HyperellipticCurve(f_final)
out('  curve: %s' % str(Codd)[:110])
out('  is_ramified: %s' % Codd.is_ramified())
try:
    w = Codd.invariant_differential()
    out('  differential OK')
    # the point at u = -1/x0 (image of C3_A (0, 1)): v from the curve:
    uu = 1/(0 - x0)
    f_at = f_final(uu)
    out('  f(u0) = %s' % str(f_at)[:80])
    Fq = K8.residue_field()
    if f_at.valuation() == 0 and (Fq(f_at)^((11^8-1)//2) == 1):
        v = K8(Fq(f_at).sqrt())
        for _ in range(7):
            v = (v + f_at/v) / 2
        P = Codd(uu, v)
        Q = Codd(uu, -v)
        val = Codd.coleman_integral(w, P, Q)
        out('  SANITY INTEGRAL = %s' % val)
    else:
        out('  v not K8-rational at this u; use the Weierstrass-point pair:')
        P = Codd(K2(0), 0) if False else None
except Exception as e:
    out('  I5 error:', str(e)[:250])
out('=== DONE ===')