#!/usr/bin/env python3
"""
Signature (3,5,7) probe: A^3 + B^5 = C^7, pairwise coprime.

Beal predicts: NO pairwise-coprime exact solutions.
We verify over a range and study the near-miss structure:
  * exact coprime solutions (would refute Beal) -> expect 0
  * exact non-coprime solutions -> Beal-consistent
  * closest pairwise-coprime near-misses |A^3 + B^5 - C^7| smallest
    -> is the "tight by 1" phenomenon present for a distinct-prime signature?
"""

from math import gcd
import bisect

A_MAX = 6000     # A^3 grows slowly -> A can be large
B_MAX = 600      # B^5 grows fast  -> B smaller
C_MAX = 200      # 200^7 ~ 1.28e16 > max possible sum

# Precompute the table of 7th powers C^7
pow7 = {}
for C in range(1, C_MAX + 1):
    v = C ** 7
    pow7[v] = C
keys = sorted(pow7.keys())
max_sum = A_MAX**3 + B_MAX**5
print(f"A<= {A_MAX}, B<= {B_MAX}, C<= {C_MAX}")
print(f"max A^3={A_MAX**3:.3e}, max B^5={B_MAX**5:.3e}, max sum~{max_sum:.3e}")
print(f"largest C^7 in table = {keys[-1]:.3e} (C={pow7[keys[-1]]})")

exact_coprime = []
exact_noncoprime = []
near = []  # (gap, A, B, C, s, nearest_C7)

for A in range(1, A_MAX + 1):
    a3 = A * A * A
    for B in range(1, B_MAX + 1):
        s = a3 + B ** 5
        hit = pow7.get(s)
        if hit:
            C = hit
            g = gcd(gcd(A, B), C)
            triple = (A, B, C, g)
            if g == 1:
                exact_coprime.append(triple)
            else:
                exact_noncoprime.append(triple)
        else:
            # nearest 7th power
            i = bisect.bisect_left(keys, s)
            best = None
            for j in (i - 1, i):
                if 0 <= j < len(keys):
                    d = abs(keys[j] - s)
                    if best is None or d < best[0]:
                        best = (d, keys[j])
            d, val = best
            C = pow7[val]
            if gcd(gcd(A, B), C) == 1 and d > 0:
                near.append((d, A, B, C, s, val))

near.sort()

print("\n=== EXACT pairwise-coprime solutions (would refute Beal) ===")
print(f"count = {len(exact_coprime)}")
for t in exact_coprime[:20]:
    A, B, C, g = t
    print(f"  {A}^3 + {B}^5 = {C}^7   gcd={g}  ({A**3}+{B**5}={C**7})")

print("\n=== EXACT non-coprime solutions (Beal-consistent, gcd>1) ===")
print(f"count = {len(exact_noncoprime)}")
for t in exact_noncoprime[:15]:
    A, B, C, g = t
    print(f"  {A}^3 + {B}^5 = {C}^7   gcd={g}")

print("\n=== CLOSEST pairwise-coprime near-misses (gap smallest) ===")
print(f"total coprime near-miss records = {len(near)}")
for d, A, B, C, s, val in near[:20]:
    print(f"  gap={d:>8}  {A}^3+{B}^5={s}  ~ {C}^7={val}")

print("\n=== gap distribution (pairwise-coprime) ===")
from collections import defaultdict
b = defaultdict(int)
for d, *_ in near:
    if d == 1: b["1"] += 1
    elif d <= 10: b["2-10"] += 1
    elif d <= 100: b["11-100"] += 1
    elif d <= 10000: b["101-1e4"] += 1
    else: b[">1e4"] += 1
for k in ["1", "2-10", "11-100", "101-1e4", ">1e4"]:
    print(f"  gap {k:>9}: {b[k]}")

print(f"\nmin coprime gap found: {near[0][0] if near else 'n/a'}")