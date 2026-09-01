import itertools, math
from collections import Counter

def fermat_char_census(m, n, limit=None):
    """Shioda character census for Fermat X^n_m subset P^{n+1} (n+2 coords).
    Chars: a_i in {1..m-1}, sum(a) == (p+1)*m gives Hodge type (p, n-p), 1 dim each.
    Returns dict p -> count."""
    # DP over coordinates: track sum of a_i exactly
    # sum must be a multiple of m: sum = (p+1)*m for p = 0..n
    # (primitive middle cohomology; the complementary p and n-p identified by conjugation)
    nd = n + 2
    counts = Counter()
    # DP on integer sum
    sums = Counter({0: 1})
    for _ in range(nd):
        new = Counter()
        for s, c in sums.items():
            for a in range(1, m):
                new[s + a] += c
        sums = new
    for s, c in sums.items():
        if s % m == 0:
            p = s // m - 1
            if 0 <= p <= n:
                counts[p] += c
    return counts

for (m, n) in [(4,2),(4,4),(6,4),(3,4),(5,4)]:
    c = fermat_char_census(m, n)
    print("X^%d_%d:" % (n, m), "p-type -> char count:", dict(sorted(c.items())), " total prim b_%d:" % n, sum(c.values()))
