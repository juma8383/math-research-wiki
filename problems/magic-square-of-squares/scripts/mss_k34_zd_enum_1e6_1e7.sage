# mss_k34_zd_enum_1e6_1e7.sage -- the quartic-band extension |x| <= 1e7:
# the |x|<=1e6 band found only the degenerate orbit; extend one tier
# (the sieve stress precedent: fresh height tiers until the box).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== E2: the Z_D quartic band |x| in [1e6, 1e7] ===')
# only positive band (even x -> x^2 symmetries: D(x) has the x^3 term:
# NOT even: sweep both signs):
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
found = []
start = 1000001
for x in range(start, 10000001):
    val = D(x)
    if val < 0:
        continue
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
out('  points found in [1e6, 1e7] (both signs): %d' % len(found))
for pt in found[:24]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('=== DONE ===')