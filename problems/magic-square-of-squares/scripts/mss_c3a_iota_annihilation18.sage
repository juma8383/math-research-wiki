# mss_c3a_iota_annihilation18.sage -- HQR WORKS. Now the sanity integral on
# the MW ring directly: differential w = 1 (dx/2y), points... the MW ring
# doesn't carry points; the coleman_integral API needs the curve object for
# P, Q. Route: the docs' matrix_of_frobenius_hyperelliptic needs the curve.
# Alternative within the MW ring: compute the Frobenius matrix on H^1(MW)
# via mw.frobenius_expansion_by_newton(Q, p, M) and the REDUCTION machinery
# — this is exactly what coleman_integral does internally. The integrals
# between K2-rational points: the docs route used HK.coleman_integral on the
# curve. Our curve object CAN be built if we hand Sage the polynomial in a
# way that survives: HyperellipticCurve(f_final) raised 'must be monic'
# because the constructor ALSO does the rescale? Test: HyperellipticCurve
# with check_squarefree=False and the LIST-built f_final:
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3k: curve from f_final + integral ===')
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
lst = f_monic.list()
lst[-1] = K2(1)
f_final = Ru(lst)
try:
    Codd = HyperellipticCurve(f_final)
    out('  curve constructed: OK')
    w = Codd.invariant_differential()
    out('  differential OK')
    P = Codd(K2(0), K2(1))
    Q = Codd(K2(0), K2(-1))
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
except Exception as e:
    out('  curve/integral error:', str(e)[:250])
    # fallback: the MW-ring direct integral (no curve object):
    try:
        out('  fallback: MW-ring Frobenius route')
        HQR = mw.SpecialHyperellipticQuotientRing(f_final)
        from sage.schemes.hyperelliptic_curves import monsky_washnitzer as mwmod
        p = 11
        M_frob, forms = mwmod.frobenius_expansion_by_newton(f_final, p, 8)
        out('  Frobenius expansion: OK (matrix %sx%s)' % (len(M_frob), len(M_frob[0]) if M_frob else 0))
    except Exception as e2:
        out('  fallback error:', str(e2)[:200])
out('=== DONE ===')