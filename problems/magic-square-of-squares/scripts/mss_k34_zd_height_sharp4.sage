# mss_k34_zd_height_sharp4.sage -- the sharp-constant assembly + scaling test:
# the translations were minimal, but the OTHER non-minimality move for even
# models is the SCALING w -> p*w (coefficient scaling): test v(disc(f(p*w)))
# and the general integral-model condition. Then assemble the comparison.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<w> = QQ[]
f_oct = w^8 - 4*w^6 - 604*w^4 - 952*w^2 + 56644

out('=== H3: scaling tests + comparison assembly ===')
base_disc = f_oct.discriminant()
for p in [2, 3, 7, 17, 271]:
    v0 = base_disc.valuation(p)
    out('  p=%d: baseline v = %d' % (p, v0))
    # scaling: f(p*w)*p^{-8} has disc scaled by p^{-56}: v -> v - 56? test:
    # f(p*w) = sum a_j p^j w^j: the disc of the scaled model:
    scaled = (p^8) * f_oct(w/p)
    dv = scaled.discriminant().valuation(p)
    out('   scaling w -> w/p: v = %d (%s)' % (dv, 'LOWER — model non-minimal under scaling' if dv < v0 else 'no gain'))
logs = {2: log(2).n(), 3: log(3).n(), 7: log(7).n(), 17: log(17).n(), 271: log(271).n()}
C_cons = sum(disc_val * logs[p] for p, disc_val in {2:44, 3:4, 7:6, 17:6, 271:4}.items()) / 2
out('  conservative C_finite = %.3f (Linux 42.99: agreement check)' % C_cons)
rts = f_oct.roots(CDF, multiplicities=False)
mmax = max(abs(r) for r in rts)
out('  archimedean: max|root| = %.4f, C_inf = %.3f (Linux 3.605)' % (mmax, 2*log(1+mmax)))
out('  TOTAL conservative: %.3f (Linux 46.59)' % (C_cons + 2*log(1+mmax)))
out('=== DONE ===')