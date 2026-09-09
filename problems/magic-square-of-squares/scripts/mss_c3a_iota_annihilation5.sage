# mss_c3a_iota_annihilation5.sage -- odd model; the extension API needs a
# POLYNOMIAL modulus over the base (not a degree int): pass x^2 - 11? NO —
# unramified degree-2 extension of Q_11 needs an IRREDUCIBLE mod-11 lift of
# an irreducible quadric mod 11. Take the Teichmuller-lift style: modulus
# x^2 - d where d is a non-QR mod 11 lift: d = 7 (7 is a nonresidue mod 11).
# The doc example passes a polynomial over the base: R.<x> = Qp(11)[]; then
# K2 = Qp(11).extension(x^2 - 7).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2f: unramified quadratic extension via polynomial modulus ===')
K11 = Qp(11, 8)
Rk.<X> = K11[]
K2.<c> = K11.extension(X^2 - 7)   # 7 is a nonresidue mod 11 => unramified
out('  K2 =', K2)
poly = fA.change_ring(K2)
rts = poly.roots()
out('  roots of f over Qp(11^2): %d found' % len(rts))
if rts:
    x0 = rts[0][0]
    out('  branch point x0 = %s' % x0)
    Ru.<u> = K2[]
    f_new = (poly(x0 + 1/u)) * u^8
    out('  odd-model polynomial: %s' % f_new)
    Codd = HyperellipticCurve(f_new)
    out('  ODD model over Qp(11^2): OK')
    try:
        w = Codd.invariant_differential()
        out('  invariant differential:', w)
        out('  => coleman machinery ready on the odd model.')
    except Exception as e:
        out('  invariant differential error:', str(e)[:200])
out('=== DONE ===')