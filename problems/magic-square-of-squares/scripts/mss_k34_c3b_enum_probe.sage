# mss_k34_c3b_enum_probe.sage -- the B-side mirror probe: |x| <= 1e6 on the
# C3_B octic 9x^8 - 92x^6 + 310x^4 - 92x^2 + 9 -- the filed known Q*_B
# points {inf, (0,+-12), (+-2,+-8)}: verify + hunt for new.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== C3B-ENUM: the B-octic direct sweep |x| <= 1e6 ===')
g = lambda x: 9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9
found = []
for x in range(0, 1000001):
    val = g(x)
    if val < 0:
        continue
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
        if x != 0:
            found.append((-x, s))
out('  points found |x| <= 1e6: %d' % len(found))
for pt in found[:24]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('=== DONE ===')