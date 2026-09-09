# mss_c3a_iota_annihilation3.sage -- odd model via GF(11^2) default modulus
# (hermes-win, 2026-09-09). Fix of v2: no hand-rolled modulus (the preparser
# mangled it); use Sage's default Conway polynomial for GF(11^2).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2c: roots of f in GF(11^2) ===')
F2.<b> = GF(11^2)
fb = fA.change_ring(F2)
roots2 = [r for r in F2 if fb(r) == 0]
out('  roots of f in F_121: %d found' % len(roots2))
if roots2:
    out('  sample: %s' % roots2[:4])
    out('=== I2d: lift to the unramified quadratic extension of Q_11 ===')
    K2.<c> = Qp(11, 8).extension(x^2 + 7) if False else Qp(11, 8).extension(polygen(GF(11)) .minpoly() if False else None)
    # simpler: construct Qp-extension by its defining polynomial directly:
    K2 = Qp(11, 8).extension([x^2 + 7], 'c') if False else None
    # Sage: Qp(11,8).extension(11^2) gives the unramified degree-2 extension:
    try:
        K2 = Qp(11, 8).extension(2, 'c')
        out('  K2 =', K2)
    except Exception as e:
        out('  K2 construction note:', str(e)[:150])
        K2 = None
    if K2 is not None:
        poly = fA.change_ring(K2)
        rts = poly.roots()
        out('  roots over Qp(11^2): %d found' % len(rts))
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
                out('  I3 error:', str(e)[:200])
out('=== DONE ===')