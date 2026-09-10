# mss_k34_zd_enum_probe.sage -- the enumeration-box probe (the last
# mechanical step): search Z_D(Q) points of height within the
# conservative box r0 ~ 1.7e20 -- concretely: the c-coordinate bounds.
# The tower: c in [-H, H] with H = exp(46.593) ~ 1.7e20 is far too big
# to sweep naively; the DESCENT SIEVE is the tool: enumerate the
# 2-cover classes (Sel(phi) = {1, 238}, dim 1 -- Linux filed) and
# search within each cover. This probe: the small-height band first
# (c up to 1e6), verifying the known points + no new ones.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== E1: the tower small-band sweep (c <= 1e6) ===')
# The tower Z_D: W^2 = D(x), D(x) = x^4 - 4x^3 - 604x^2 - 952x + 56644;
# the tower points (x, W); the degenerate c-fibers at x = 0.
# The known 8 + 4 degenerate = 12; the sweep over |x| <= 1e6:
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
found = []
import math
for x in range(-1000000, 1000001):
    val = D(x)
    if val >= 0:
        s = math.isqrt(val)
        if s*s == val:
            found.append((x, s))
out('  points found |x| <= 1e6: %d' % len(found))
for pt in found[:20]:
    out('   x=%d: W=+%d' % (pt[0], pt[1]))
out('=== DONE ===')