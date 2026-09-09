#!/usr/bin/env python3
# Extend the Z_D(Q) point search: the degenerate orbit is (0, ±238) + infinity².
# Search for non-degenerate Z_D(Q) points at much larger heights — exact integer
# arithmetic: y^2 = w^8 - 4w^6 - 604w^4 - 952w^2 + 56644 for w = a/b, a<=A, b<=B.
# (a/b in lowest terms; f(w) must be a square of a rational.)
import math
import sys
sys.set_int_max_str_digits(2000000)

def fD(a, b):
    # f(a/b) with common denominator b^8: (a^8 - 4a^6 b^2 - 604 a^4 b^4 - 952 a^2 b^6 + 56644 b^8)/b^8
    a2 = a*a; a4 = a2*a2; a6 = a4*a2; a8 = a6*a2
    b2 = b*b; b4 = b2*b2; b6 = b4*b2; b8 = b6*b2
    return a8 - 4*a6*b2 - 604*a4*b4 - 952*a2*b6 + 56644*b8

def issq(n):
    if n < 0: return False
    r = math.isqrt(n)
    return r*r == n

print("Z_D(Q) search: w = a/b, a <= 20000, b <= 200 (exact arithmetic)")
hits = []
A_LIMIT = 20000
for b in range(1, 201):
    for a in range(-A_LIMIT, A_LIMIT+1):
        if a == 0: continue
        if math.gcd(a, b) != 1: continue
        v = fD(a, b)
        if v >= 0 and issq(v):
            y = math.isqrt(v)
            # y rational? v/y_ratio: y = sqrt(v)/b^4
            hits.append((a, b, y))
            if len(hits) <= 6:
                print(f"  HIT: w = {a}/{b}, y = {y}/{b**4} (b^4={b**4})")
if not hits:
    print("no non-degenerate Z_D(Q) points in a<=20000, b<=200")
print(f"total hits: {len(hits)}")