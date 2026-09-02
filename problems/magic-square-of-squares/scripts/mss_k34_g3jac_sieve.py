#!/usr/bin/env python
# [mss-k34-g3jac] Part 4 (bonus): Mordell-Weil-sieve-style consistency check.
#
# For a rational point (x, W) on C3: W^2 = f(x) with p not dividing the
# denominator of x, the residue x mod p must make f(x) a QR or 0 mod p.
# Sieve x mod N, N = product of the killing primes:
#   C3_A: primes {3,5,11,13},  N = 2145
#   C3_B: primes {3,5,19,29},  N = 8265
# Report survivor counts as primes are added, and whether only the
# degenerate classes x = 0, +-1 (mod N) survive.
# ASCII only.
import sys
from itertools import product

def out(*a):
    print(*a)
    sys.stdout.flush()

C3 = {
    "A": [1, 0, 132, 0, -250, 0, 132, 0, 1],   # ascending octic
    "B": [9, 0, -92, 0, 310, 0, -92, 0, 9],
}
KILL = {
    "A": [3, 5, 11, 13],
    "B": [3, 5, 19, 29],
}

def good_classes(coeffs, p):
    """x mod p with f(x) a QR or 0 mod p."""
    good = []
    for x in range(p):
        v = 0
        for c in reversed(coeffs):
            v = (v * x + c) % p
        if v == 0 or pow(v, (p - 1) // 2, p) == 1:
            good.append(x)
    return good

def crt_merge(a1, n1, a2, n2):
    inv = pow(n1 % n2, -1, n2)
    t = ((a2 - a1) % n2) * inv % n2
    return (a1 + n1 * t) % (n1 * n2)

for tag in ("A", "B"):
    out("=" * 72)
    primes = KILL[tag]
    N = 1
    for p in primes:
        N *= p
    out("C3_%s : killing primes %s, N = %d" % (tag, primes, N))
    gs = [good_classes(C3[tag], p) for p in primes]
    for p, g in zip(primes, gs):
        out("  mod %2d : %2d/%2d residue classes survive  %s"
            % (p, len(g), p, g))
    # incremental survivor counts (classes mod running modulus)
    cur = gs[0]
    n = primes[0]
    out("  after p=%2d : %4d classes mod %d" % (primes[0], len(cur), n))
    for j in range(1, len(primes)):
        p = primes[j]
        n *= p
        cur = [crt_merge(x, n // p, a, p)
               for x in cur for a in gs[j]]
        out("  after p=%2d : %4d classes mod %d" % (p, len(cur), n))
    s = sorted(cur)
    out("  ALL %d primes: %d/%d classes survive" % (len(primes), len(s), N))
    out("  survivors: %s" % (s if len(s) <= 60 else str(s[:60]) + " ..."))
    degen = {0, 1, N - 1}
    extra = sorted(set(s) - degen)
    out("  degenerate {0,1,-1} all present: %s ; non-degenerate extras: %d"
        % (degen <= set(s), len(extra)))
    if extra and len(extra) <= 60:
        out("  extras: %s" % extra)