# mss_k34_descent_sieve_win4.sage -- the sieve SPLIT into chunks: the
# v3 run was killed by the 1700s timeout mid-sweep (no final line).
# v4: chunked progress with flushing so partial results survive; the
# chunk count reports live progress. Run 1e10 in 4 chunks of 2.5e9.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== DS4v2: the chunked x-sieve to 1e10 ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
COVERS = [1, 238]
primes = [3, 5, 7, 11, 13, 17]
M = 255255
sq = [set((i*i) % p for i in range(p)) for p in primes]
union = set()
for d in COVERS:
    for x in range(M):
        ok = True
        for i, p in enumerate(primes):
            val = (D(x) * d) % p
            if val != 0 and val not in sq[i]:
                ok = False
                break
        if ok:
            union.add(x)
out('  union residues: %d' % len(union))
found = []
CHUNK = 2500000000
for c in range(4):
    lo = c * CHUNK
    hi = lo + CHUNK
    cnt = 0
    for x in range(lo, hi):
        if x % M not in union:
            continue
        cnt += 1
        for d in COVERS:
            val = D(x) * d
            if val < 0:
                continue
            s = math.isqrt(val)
            if s*s == val:
                found.append((x, d, s))
                out('  FOUND: x=%d, d=%d, w=%d' % (x, d, s))
    out('  chunk %d [%d, %d): %d candidates, %d found, %.0fs'
        % (c, lo, hi, cnt, len(found), time.time() - T0))
out('  TOTAL found: %d' % len(found))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')