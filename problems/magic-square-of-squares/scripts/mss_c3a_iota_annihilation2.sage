# mss_c3a_iota_annihilation2.sage -- the odd model via the CORRECT branch
# data: f mod 11 has NO roots in F_11 (verified: values 1,5,8,7,8,10,10,8,7,8,5
# — never 0). The branch points live in quadratic extensions of Q_11. The
# odd-degree transform needs a branch point x0 with f(x0) = 0: over the
# unramified quadratic extension K2 = Q_11(sqrt(d)) for a root d in F_121.
# The 8 branch points pair as x and -x (f even); pick any F_121 root.
# IMPORTANT: the odd model over K2 computes K2-rational Coleman integrals;
# the Q-structure annihilation is recovered because the cycles are defined
# over Q (the pairing is Galois-invariant) — the annihilation check at the
# level of the PULLBACK differential remains valid over K2 (integrals of a
# K2-differential over a K2-defined cycle = 0 iff the corresponding class
# is torsion in the K2-Jacobian; the MW lattice is defined over Q, so
# base change preserves the condition).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2b: find a root of f in F_121 = GF(11^2) ===')
F2.<a> = GF(121, modulus=x^2 + 3)   # x^2+3 irreducible mod 11? 3 is a nonresidue mod 11? 5^2=3? no: QRs mod 11: 1,3,4,5,9. 3 IS a QR (5^2=25=3). pick x^2+7 (7 is NR mod 11: QRs 1,3,4,5,9 -> 7 not there)
F2b.<b> = GF(121, modulus=x^2 + 7)
fb = fA.change_ring(F2b)
roots2 = [r for r in F2b if fb(r) == 0]
out('  roots of f in F_121: %d found' % len(roots2))
if roots2:
    out('  sample roots: %s' % roots2[:4])
    out('=== I2c: lift to Qp extension and construct the odd model ===')
    K2 = Qp(11, 8).extension(x^2 + 7, 'c')
    poly = fA.change_ring(K2)
    rts = poly.roots()
    out('  roots over Qp(11^2): %d found' % len(rts))
    if rts:
        x0 = rts[0][0]
        out('  branch point x0 = %s' % x0)
        u = polygen(K2, 'u')
        f_new = (poly(x0 + 1/u)) * u^8
        out('  odd-model polynomial (deg should be 7): %s' % f_new)
        Codd = HyperellipticCurve(f_new)
        out('  ODD model over Qp(11^2): %s' % Codd)
        out('  genus:', Codd.genus() if hasattr(Codd, 'genus') else 'n/a')
        out('=== I3: coleman_integral available on the odd model? ===')
        try:
            w = Codd.invariant_differential()
            out('  invariant differential:', w)
            out('  => READY for the iota-side annihilation integral.')
        except Exception as e:
            out('  I3 error:', str(e)[:200])
else:
    out('  no roots in F_121 either? unexpected — check irreducible factors')
    out('  factorization of f mod 11: %s' % f11.factor())
out('=== DONE ===')