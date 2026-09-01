# Calibrate the Euler-product hourglass heuristic against the actual
# censused range: compute the model sum  sum_{w<=W} C(|D|,2)*24|D|/w^2
# directly for W = 1e6 (using the validated count pass for exact |D|),
# compare with the observed count (0) and with the unbounded H ~ 1.014.
# The difference H_total - H_partial estimates how much expected mass the
# model places BEYOND the censused range (Buell's w <= 5e12 included).

import math
import sys
from array import array
from mss_census_chunked import build_primitive_triples, count_pass

W = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6

w0s, d0s = build_primitive_triples(W)
counts = array("I", bytes(4 * (W + 1)))
count_pass(w0s, W, counts)

partial = 0.0
n_pairs = 0
hist = {}
for w in range(2, W + 1):
    n = counts[w]  # exact |D(w^2)|
    if n >= 2:
        c = n * (n - 1) // 2 * 24 * n  # C(|D|,2)*24|D|
        partial += c / (w * w)
        n_pairs += c
        hist[n] = hist.get(n, 0) + 1

print("model partial sum over w <= %d: %.6f" % (W, partial))
print("total (pair,slot) weight in range: %d" % n_pairs)
print("observed additive triples in range: 0 (census)")
print("|D| histogram (n: count of w):")
for n in sorted(hist):
    print("  |D|=%d : %d w" % (n, hist[n]))