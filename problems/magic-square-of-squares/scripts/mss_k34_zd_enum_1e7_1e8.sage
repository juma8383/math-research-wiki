# mss_k34_zd_enum_1e7_1e8.sage -- the quartic band [1e7, 1e8]: one tier
# deeper (the isqrt-based direct sweep; ~1.8e7 iterations, ~2 min).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== E3: the Z_D quartic band |x| in [1e7, 1e8] ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
found = []
for x in range(-100000000, 100000001):
    val = D(x)
    if val < 0:
        continue
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
out('  points found in band (both signs): %d' % len(found))
for pt in found[:24]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')