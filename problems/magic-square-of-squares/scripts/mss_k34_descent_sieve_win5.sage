# mss_k34_descent_sieve_win5.sage -- the FAST sieve: second-stage modular
# filter (3 more primes, M2 = 255255*19*23*29) applied before isqrt:
# pass rate drops ~100x, the sweep becomes viable. Chunked, flushing.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math

out('=== DS5: the two-stage sieve ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
COVERS = [1, 238]
p1 = [3, 5, 7, 11, 13, 17]
M1 = 255255
p2 = [19, 23, 29]
M2 = M1 * 19 * 23 * 29
sq1 = [set((i*i) % p for i in range(p)) for p in p1]
sq2 = [set((i*i) % p for i in range(p)) for p in p2]

# stage 1: the union filter mod M1:
union1 = set()
for x in range(M1):
    ok = True
    for i, p in enumerate(p1):
        val = (D(x) * 1) % p
        if val != 0 and val not in sq1[i]:
            ok = False
            break
    if ok:
        union1.add(x)
out('  stage-1 residues (d=1 covers all via D(x)*d QR check at stage 2): %d' % len(union1))

# stage 2: for stage-1 survivors, test mod p2 (both covers):
union2 = set()
for x in union1:
    for cls2 in range(M2 // M1):
        xx = (x + cls2 * M1) % M2
        ok = True
        for i, p in enumerate(p2):
            any_ok = False
            for d in COVERS:
                val = (D(xx) * d) % p
                if val == 0 or val in sq2[i]:
                    any_ok = True
                    break
            if not any_ok:
                ok = False
                break
        if ok:
            union2.add(xx)
out('  stage-2 residues mod M2 = %d: %d survive' % (M2, len(union2)))
out('  effective pass rate: %.2f%%' % (100.0*len(union2)/M2))

found = []
CHUNK = 2500000000
for c in range(4):
    lo = c * CHUNK
    hi = lo + CHUNK
    cnt = 0
    for x in range(lo, hi):
        if x % M2 not in union2:
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
    out('  chunk %d [%d, %d): %d candidates, found %d, %.0fs'
        % (c, lo, hi, cnt, len(found), time.time() - T0))
out('  TOTAL: %d' % len(found))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')