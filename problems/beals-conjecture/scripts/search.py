#!/usr/bin/env python3
"""
Beal's conjecture computational probe.

Conjecture (coprime form): there are NO positive-integer solutions to
    A^x + B^y = C^z   with   x, y, z >= 3   and   A, B, C pairwise coprime.

This script, over a chosen base bound N and exponent set S:
  1. Verifies the conjecture (finds zero pairwise-coprime exact solutions).
  2. Reports any exact solutions that DO exist (these must have gcd(A,B,C)>1,
     consistent with Beal -- useful as witnesses/counterexamples-to-the-naive-form).
  3. Collects the closest near-misses among pairwise-coprime (A,B,C):
     |A^x + B^y - C^z| small, to study the obstruction structure.
"""

from math import gcd, isqrt
from collections import defaultdict

N = 120                      # base bound for A and B
S = [3, 4, 5, 7]             # exponent set (odd primes + 4, per the reduction)

def perfect_power_check(n, S):
    """Return (C, z) if n is a perfect z-th power for some z in S, else None."""
    if n <= 1:
        return None
    for z in S:
        # integer z-th root
        c = int(round(n ** (1.0 / z)))
        for cc in (c - 1, c, c + 1, c + 2):
            if cc >= 1 and cc ** z == n:
                return (cc, z)
    return None

def main():
    # Precompute perfect powers C^z up to the max possible sum.
    max_pow = max(A ** x for A in range(1, N + 1) for x in S)
    max_sum = 2 * max_pow

    # Build set of perfect powers {value: (C, z)} for z in S, C up to root of max_sum.
    pp = {}
    for z in S:
        C = 1
        while True:
            v = C ** z
            if v > max_sum:
                break
            pp.setdefault(v, (C, z))   # keep smallest-base representation
            C += 1
    print(f"base bound N={N}, exponents S={S}")
    print(f"max base power={max_pow}, max possible sum={max_sum}")
    print(f"perfect-power table size={len(pp)}")

    exact_coprime = []     # would refute Beal
    exact_noncoprime = []  # consistent with Beal (gcd>1)
    near = []              # (gap, A,x,B,y,C,z) pairwise-coprime near-misses

    for A in range(1, N + 1):
        for x in S:
            ax = A ** x
            for B in range(1, N + 1):
                for y in S:
                    s = ax + B ** y
                    hit = pp.get(s)
                    if hit:
                        C, z = hit
                        g = gcd(gcd(A, B), C)
                        triple = (A, x, B, y, C, z, g)
                        if g == 1:
                            exact_coprime.append(triple)
                        else:
                            exact_noncoprime.append(triple)
                    else:
                        # near-miss: closest perfect power in S to s
                        # only record if A,B would be coprime with the nearby C
                        # find nearest perfect power value
                        # (cheap: binary search over sorted keys)
                        pass
    # near-miss pass (separate, with sorted keys)
    keys = sorted(pp.keys())
    def nearest(v):
        lo, hi = 0, len(keys) - 1
        # linear-ish via bisect
        import bisect
        i = bisect.bisect_left(keys, v)
        best = None
        for j in (i - 1, i):
            if 0 <= j < len(keys):
                d = abs(keys[j] - v)
                if best is None or d < best[0]:
                    best = (d, keys[j])
        return best

    for A in range(1, N + 1):
        for x in S:
            ax = A ** x
            for B in range(A, N + 1):   # A<=B to avoid dup symmetry; keep all for exactness above though
                for y in S:
                    s = ax + B ** y
                    d, val = nearest(s)
                    C, z = pp[val]
                    if gcd(gcd(A, B), C) == 1 and d > 0:
                        near.append((d, A, x, B, y, C, z, s, val))
    near.sort()

    print("\n=== EXACT pairwise-coprime solutions (would refute Beal) ===")
    print(f"count = {len(exact_coprime)}")
    for t in exact_coprime[:50]:
        A, x, B, y, C, z, g = t
        print(f"  {A}^{x} + {B}^{y} = {C}^{z}   gcd={g}   ({A**x}+{B**y}={C**z})")

    print("\n=== EXACT non-coprime solutions (consistent with Beal, gcd>1) ===")
    print(f"count = {len(exact_noncoprime)}")
    for t in exact_noncoprime[:30]:
        A, x, B, y, C, z, g = t
        print(f"  {A}^{x} + {B}^{y} = {C}^{z}   gcd={g}   ({A**x}+{B**y}={C**z})")

    print("\n=== CLOSEST pairwise-coprime near-misses (gap smallest) ===")
    print(f"total near-miss records = {len(near)}")
    for t in near[:25]:
        d, A, x, B, y, C, z, s, val = t
        print(f"  gap={d:>6}  {A}^{x}+{B}^{y}={s}  ~ {C}^{z}={val}  (z={z})  coprime")

    # distribution of near-miss gaps
    print("\n=== near-miss gap distribution (pairwise-coprime) ===")
    buckets = defaultdict(int)
    for t in near:
        d = t[0]
        if d == 1: buckets["1"] += 1
        elif d <= 5: buckets["2-5"] += 1
        elif d <= 50: buckets["6-50"] += 1
        elif d <= 500: buckets["51-500"] += 1
        else: buckets[">500"] += 1
    for k in ["1", "2-5", "6-50", "51-500", ">500"]:
        print(f"  gap {k:>7}: {buckets[k]}")

if __name__ == "__main__":
    main()