# Non-square-center patterns for the 3x3 magic-square-of-squares census.
# A config with >=7 square entries and NON-square center needs >=3 full pairs,
# i.e. center a with R(a) >= 3 representations a = u^2+v^2 (u>v>0).
# Full test: enumerate all (u,v) with u^2+v^2 <= B, group by a, and for each a
# with >=3 reps, test all (b,c) patterns whose 4 diffs {b,c,b+c,b-c} include
# >=3 of the D(a) values (plus half-pair checks via isqrt).

import math
import numpy as np

def is_sq(n):
    if n < 1:
        return False
    r = math.isqrt(n)
    return r * r == n

def entries(a, b, c):
    return (a + b, a - b - c, a + c,
            a - b + c, a, a + b - c,
            a - c, a + b + c, a - b)

def candidate_centers(B):
    """all a <= B with R(a) >= 3, returned as dict a -> list of d=2uv."""
    umax = int(math.isqrt(B))
    pairs = []
    for u in range(2, umax + 1):
        vmax = min(u - 1, int(math.isqrt(B - u * u)))
        if vmax < 1:
            continue
        v = np.arange(1, vmax + 1, dtype=np.int64)
        a = u * u + v * v
        d = 2 * u * v
        pairs.append(np.stack([a, d], axis=1))
    P = np.concatenate(pairs)
    order = np.argsort(P[:, 0], kind='stable')
    P = P[order]
    # run-length by a
    a = P[:, 0]
    bounds = np.flatnonzero(np.diff(a)) + 1
    starts = np.concatenate([[0], bounds])
    ends = np.concatenate([bounds, [len(a)]])
    lens = ends - starts
    out = {}
    for s, e, L in zip(starts, ends, lens):
        if L >= 3:
            out[int(a[s])] = [int(x) for x in P[s:e, 1]]
    return out

def test_center(a, D, B, min_squares):
    res = []
    Dset = set(D)
    for x in D:
        for y in D:
            if x == y:
                continue
            cands = [(x, y), (x, y - x), (x, x - y), (y - x, x), (x + y, x)]
            if (x + y) % 2 == 0 and (x - y) % 2 == 0:
                cands.append(((x + y) // 2, (x - y) // 2))
            for (b, c) in cands:
                if b == 0 or c == 0 or b == c or b == -c:
                    continue
                ent = entries(a, b, c)
                if any(e < 1 or e > B for e in ent):
                    continue
                nsq = sum(1 for e in ent if is_sq(e))
                if nsq >= min_squares:
                    res.append((a, b, c, nsq, ent))
    return res

if __name__ == "__main__":
    import time, sys
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
    t = time.time()
    cands = candidate_centers(B)
    t1 = time.time()
    n_c = len(cands)
    hits = []
    for a, D in cands.items():
        hits.extend(test_center(a, D, B, 7))
    t2 = time.time()
    print("B=%d: pairs-enumeration+grouping %.1fs, candidates(R>=3)=%d, pattern-testing %.1fs, hits(>=7 sq, non-square center)=%d"
          % (B, t1 - t, n_c, t2 - t1, len(hits)))
    for h in hits[:10]:
        print("   a=%d b=%d c=%d nsq=%d" % h[:4])