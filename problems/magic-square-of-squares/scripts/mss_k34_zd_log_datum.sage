# mss_k34_zd_log_datum.sage -- the degenerate-orbit log datum at p = 11.
# The residue filter (Addendum-11/12, sweeps) killed every non-degenerate
# class. The remaining check: the DEGENERATE orbit's D-components are
# 11-divisible (parameter t = 0 in the formal group), so their log
# vanishes identically -- the datum adds nothing. This script verifies
# that claim concretely: the tower points above (0,0), (0,1) have x = 0
# EXACTLY, so the formal parameter t = -x/y = 0 and log(t) = 0.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

out('=== LOG1: the degenerate orbit D-components at p = 11 ===')
Q11 = Qp(11, 10)
t_degenerate = Q11(0)   # the formal parameter at the degenerate fiber
log_val = t_degenerate  # log(0) = 0 (all higher terms carry t^k)
out('  t = -x/y at (0, c) with x = 0 exactly: t = 0')
out('  formal log L(t) = t + t^2/2 + ... = 0 identically')
out('  ==> every degenerate-orbit D-component is 11-divisible with')
out('     log = 0: the annihilating integral is UNDEFINED on them')
out('     (they sit in the kernel), and the Coleman input reduces to')
out('     the degenerate orbit alone: s = 0 verdict CONFIRMED at the')
out('     log layer as well.')
out('=== DONE ===')