# mss_c3a_iota_annihilation4.sage -- odd model over the unramified quadratic
# Qp-extension; fix of v3 (the dead code left `extension(None)` in the
# preparsered line — removed entirely). Roots ARE in GF(11^2): 8 found.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2e: the unramified quadratic extension of Q_11 ===')
K2.<c> = Qp(11, 8).extension(2)
out('  K2 =', K2)
poly = fA.change_ring(K2)
rts = poly.roots()
out('  roots of f over Qp(11^2): %d found' % len(rts))
if rts:
    x0 = rts[0][0]
    out('  branch point x0 = %s' % x0)
    u = polygen(K2, 'u')
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