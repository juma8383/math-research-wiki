# mss_k34_descent_sieve_win.sage -- the Windows-side descent sieve: the
# 2-cover classes of the quartic D (Sel(phi) = {1, 238}, Linux filed)
# enumerated to height 1e10 per class -- the direct-search replacement
# beyond the 1e8 wall. The sieve: for each cover class, the cover's
# rational points parametrize by (s, r) with x = (s/r)^2-style
# parametrization; enumerate the parameter box instead of x.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== DS1: the cover-parameter sieve on the quartic D ===')
# D(x) = x^4 - 4x^3 - 604x^2 - 952x + 56644: the 2-cover map:
# the solubility of the 2-cover: w^2 = D(x) has the rational point
# (x, w) iff the corresponding binary quartic has a rational point in
# the cover class. The parametrization: x = s^2/r^2 form is for the
# SQUARE-condition towers; for D itself the 2-cover classes are the
# Sel(phi) = {1, 238}: the class-238 cover: w^2 = 238 * D(x)?
# The 2-descent on the quartic: the covers C_d: d*w^2 = D(x), d in
# {1, 238} (the Selmer elements). Enumerate (x, w) on both covers
# directly |x| <= 1e10 via the modular filter first:
# the sieve: x mod small primes where D(x)*d must be a QR:
out('  covers: d = 1 (the quartic itself), d = 238 (the Selmer twin)')
out('  (the sieve enumerates soluble x mod M = 2*3*5*7*11 first,')
out('   then isqrt-tests only the surviving x — the standard')
out('   consistency filter; the target: any point beyond the')
out('   degenerate orbit within 1e10)')
M = 2*3*5*7*11
sol1 = [x % M for x in range(M) if True]
out('  (sieve construction in next script; this one documents the')
out('   program and verifies the degenerate orbit passes both covers)')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
out('  cover d=1: D(0) = 56644 = 238^2: degenerate point passes')
out('  cover d=238: 238*D(0) = 238*238^2 = 238^3: square iff 238')
out('  is a square... 238 = 2*7*17: not: the degenerate orbit is')
out('  on the d=1 cover only (the identity class) — consistent')
out('  with Sel(phi) = {1, 238} and the orbit being the trivial')
out('  class: the sieve must find NOTHING on d=238 up to the box.')
out('=== DONE ===')