# mss_k34_c3a_enum_probe.sage -- the SAME direct probe on C3_A itself:
# |x| <= 1e6 on the octic f(x) = x^8 + 132x^6 - 250x^4 + 132x^2 + 1 --
# the 8 known points {inf, (0,+-1), (+-1,+-4)}: verify + hunt for new.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== C3A-ENUM: the octic direct sweep |x| <= 1e6 ===')
f = lambda x: x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1
found = []
# f(x) > 0 for large |x| (leading 1); the even symmetry: f(-x) = f(x):
for x in range(0, 1000001):
    val = f(x)
    s = math.isqrt(val)
    if s*s == val:
        found.append((x, s))
        if x != 0:
            found.append((-x, s))
out('  points found |x| <= 1e6: %d' % len(found))
for pt in found[:24]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('=== DONE ===')