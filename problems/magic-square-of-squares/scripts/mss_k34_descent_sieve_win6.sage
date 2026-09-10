# mss_k34_descent_sieve_win6.sage -- the sieve in C (via numpy): the
# second-stage filter as a boolean mask over the chunk (numpy vectorized
# mod arithmetic), the isqrt only on the ~1e6 survivors per chunk.
# Chunk = 2.5e9: numpy can't hold int64 2.5e9 array (20 GB) — use
# 1e9-chunks with uint64 arithmetic on the residue classes instead:
# iterate x in numpy arange over a FULL RESIDUE BLOCK: only the
# union2 survivors matter: iterate over SURVIVOR CLASSES directly:
# for each residue r in union2 (1.9e7), the x-values are r + k*M2:
# the sweep over k: 1e10/M2 ~ 70.6 values per residue: 1.9e7*70 ~ 1.4e9
# isqrt-tests: still too many? No: the isqrt test is per (x, cover):
# total isqrts = 2.8e8: in C-speed via numpy on int64: feasible if we
# vectorize D(x) evaluation over the x-block. D(x) at x~1e10 fits
# int64? D(x) ~ x^4 = 1e40: NO. Use Python ints for the isqrt stage
# but numpy for the filter stage. Chunked.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

import math
import numpy as np

out('=== DS6: the vectorized-residue sweep ===')
D = lambda x: x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
COVERS = [1, 238]
p1 = [3, 5, 7, 11, 13, 17]
M1 = 255255
p2 = [19, 23, 29]
M2 = M1 * 19 * 23 * 29
sq1 = [set((i*i) % p for i in range(p)) for p in p1]
sq2 = [set((i*i) % p for i in range(p)) for p in p2]

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
surv = np.array(sorted(union2), dtype=np.int64)
out('  stage-2 survivors: %d' % len(surv))

# the sweep: for each survivor class r, x in {r + k*M2}:
found = []
K = 10000000000 // M2 + 1
out('  k-range per class: %d' % K)
for k in range(K):
    xs = surv + k * M2
    # evaluate D on the batch with Python ints (the values overflow
    # int64: x^4 ~ 1e38 at x=1e10... 1e10^4 = 1e40: use object?):
    # chunk the batch: Python-int isqrt per element:
    for x in xs.tolist():
        if x > 10000000000:
            break
        for d in COVERS:
            val = D(x) * d
            if val < 0:
                continue
            s = math.isqrt(val)
            if s*s == val:
                found.append((x, d, s))
                out('  FOUND: x=%d, d=%d, w=%d' % (x, d, s))
    if k % 100 == 0:
        out('   ...k=%d (%.0fs)' % (k, time.time() - T0))
out('  TOTAL: %d' % len(found))
out('  elapsed: %.0fs' % (time.time() - T0))
out('=== DONE ===')