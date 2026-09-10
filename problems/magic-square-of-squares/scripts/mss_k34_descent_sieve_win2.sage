# mss_k34_descent_sieve_win2.sage -- the modular-filter sieve over the two
# 2-cover classes d in {1, 238}: soluble residue classes of D(x)*d mod
# small primes, CRT-bucket the survivors, isqrt-test the survivors'
# x-values in [0, 1e10]. The direct test per candidate is one isqrt.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math
from sympy import primerange

out('=== DS2: the sieve over the covers ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
COVERS = [1, 238]
# the modular filter: for each small prime p, keep x mod p with D(x)*d a QR:
primes = list(primerange(3, 60))
out('  filter primes: %s' % primes[:10])
filters = {}
for d in COVERS:
    keep = []
    # CRT over the prime set: product M:
    M = 1
    for p in primes:
        M *= p
    sq = [set((i*i) % p for i in range(p)) for p in primes]
    cnt = 0
    for x in range(M):
        ok = True
        for i, p in enumerate(primes):
            val = (D(x) * d) % p
            if val != 0 and val not in sq[i]:
                ok = False
                break
        if ok:
            keep.append(x)
            cnt += 1
    filters[d] = (keep, M)
    out('  cover d=%d: %d/%d residues survive (M = %d)' % (d, cnt, M, M))

out('=== DS3: the x-sweep with the filter ===')
LIMIT = 10**10
residues = {d: set(v[0]) for d, v in filters.items()}
M = filters[1][1]
total_cand = 0
found = []
step = 0
for x in range(0, LIMIT := 10000000000):
    step += 1
    if x % M not in residues[1] and x % M not in residues[238]:
        continue
    for d in COVERS:
        val = D(x) * d
        if val < 0:
            continue
        s = math.isqrt(val)
        if s*s == val:
            found.append((x, d, s))
            out('  FOUND: x=%d, cover d=%d: w=%d' % (x, d, s))
    if step % 2000000000 == 0:
        out('   ...x = %d (%.0fs)' % (x, time.time() - T0))
out('  candidates tested; found: %d' % len(found))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')