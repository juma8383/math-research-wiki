# mss_k34_descent_sieve_win3.sage -- the sieve with a MANAGEABLE modulus:
# 6 filter primes (M = 255255): the residue enumeration is 255k steps,
# then the x-sweep tests survivors only (a few percent of x).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== DS3: the sieve (M = 255255, 6 primes) ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
COVERS = [1, 238]
primes = [3, 5, 7, 11, 13, 17]
M = 255255
sq = [set((i*i) % p for i in range(p)) for p in primes]
filters = {}
for d in COVERS:
    keep = []
    for x in range(M):
        ok = True
        for i, p in enumerate(primes):
            val = (D(x) * d) % p
            if val != 0 and val not in sq[i]:
                ok = False
                break
        if ok:
            keep.append(x)
    filters[d] = set(keep)
    out('  cover d=%d: %d/%d residues survive' % (d, len(keep), M))

out('=== DS4: the x-sweep to 1e10 with the filter ===')
found = []
res1 = filters[1]
res238 = filters[238]
union = res1 | res238
out('  union residues: %d (%.1f%% of x-values pass the filter)'
    % (len(union), 100.0*len(union)/M))
for x in range(0, 10000000000):
    if x % M not in union:
        continue
    for d in COVERS:
        val = D(x) * d
        if val < 0:
            continue
        s = math.isqrt(val)
        if s*s == val:
            found.append((x, d, s))
            out('  FOUND: x=%d, d=%d, w=%d' % (x, d, s))
out('  found: %d' % len(found))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')