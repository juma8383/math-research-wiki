# mss_k34_zd_c3a_band_1e6_1e8.sage -- the C3_A octic bands [1e6, 1e8]:
# the same two tiers on the gate curve (the even symmetry halves the work).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== E4: the C3_A octic band |x| in [1e6, 1e8] ===')
f = lambda x: x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1
found = []
for x in range(1000001, 100000001):
    val = f(x)
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
out('  positive-x points in band: %d (mirror to -x by evenness)' % len(found))
for pt in found[:12]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')