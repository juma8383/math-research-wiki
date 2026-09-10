# mss_k34_c3b_band_1e6_1e8.sage -- the C3_B octic band [1e6, 1e8] (positive
# x; even symmetry): the B-side wall to the same tier.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== E5: the C3_B octic band |x| in [1e6, 1e8] ===')
g = lambda x: 9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9
found = []
for x in range(1000001, 100000001):
    val = g(x)
    if val < 0:
        continue
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
out('  positive-x points in band: %d (mirror by evenness)' % len(found))
for pt in found[:12]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')