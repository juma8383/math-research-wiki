# mss_c3a_iota_annihilation14.sage -- the working sanity integral: use the
# FROBENIUS-matrix route directly (matrix_of_frobenius_hyperelliptic), which
# the Sage docs show working even on curves the wrapper objects struggle with.
# The odd model f_monic (degree 7 over K2): compute the Frobenius matrix and
# the invariant differential, then the integral via coleman_integral on the
# curve object (the earlier failure was the (1+O(11^8))*y^2 rescale inside the
# HyperellipticCurve constructor: it appears when the leading coeff isn't
# literal 1; force it via the 'check=False'... simplest: divide f by its
# leading coefficient INSIDE the same ring that made it (Ru), using
# .monic() — Sage polynomial .monic() divides by lc cleanly):
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3g: Frobenius-matrix route on the odd model ===')
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
f_monic = f_new.monic()          # <- .monic() divides by lc properly
out('  f_monic degree: %d ; leading: %s' % (f_monic.degree(), str(f_monic.leading_coefficient())[:60]))
Codd = HyperellipticCurve(f_monic)
out('  curve: %s' % str(Codd)[:100])
try:
    w = Codd.invariant_differential()
    out('  differential OK')
    P = Codd(K2(0), K2(1))
    Q = Codd(K2(0), K2(-1))
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
except Exception as e:
    out('  I3g integral error:', str(e)[:200])
# independent route: Frobenius matrix directly:
try:
    from sage.schemes.hyperelliptic_curves import monsky_washnitzer as mw
    M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(Codd)
    out('  Frobenius matrix computed: %s' % str(M_frob)[:120])
except Exception as e:
    out('  Frobenius-matrix route error:', str(e)[:200])
out('=== DONE ===')