# Robustness run for the Corner Principle: wider box C<=100, B<=10^5.
import math, time
from importlib import util
spec = util.spec_from_file_location("nmp", "near_miss_package.py")
# We only need scan_sig; avoid re-running the whole package by copying the helpers.

def iroot(n, k):
    if n < 1:
        return 0
    if n < 2**k:
        return 1
    r = 1 << ((n.bit_length() + k - 1) // k)
    while r ** k > n:
        r = ((k - 1) * r + n // r**(k - 1)) // k
    while (r + 1) ** k <= n:
        r += 1
    return r

def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)

def scan_sig(p, q, r, C_MAX, B_MAX):
    best = None
    gap1_genuine = 0
    two_pow_p = 2 ** p
    for C in range(2, C_MAX + 1):
        CR = C ** r
        for B in range(2, B_MAX + 1):
            BQ = B ** q
            rem = CR - BQ
            if rem >= two_pow_p:
                fl = iroot(rem, p)
                cands = (fl, fl + 1)
            else:
                cands = (2, 3, 4)
            for A in cands:
                if A < 2:
                    continue
                AP = A ** p
                val = AP + BQ - CR
                g = abs(val)
                if g == 0 or AP == CR or BQ == CR:
                    continue
                if g == 1:
                    if gcd3(A, B, C) == 1:
                        gap1_genuine += 1
                    continue
                if gcd3(A, B, C) != 1:
                    continue
                t = (g, A, B, C, val)
                if best is None or t < best:
                    best = t
    return best, gap1_genuine

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23]
triples = [(p, q, r) for i, p in enumerate(PRIMES) for q in PRIMES[i+1:]
           for r in PRIMES[PRIMES.index(q)+1:]]
t0 = time.time()
viol = 0
for (p, q, r) in triples:
    corner, _ = scan_sig(p, q, r, 3, 10**5)
    full, g1 = scan_sig(p, q, r, 100, 10**5)
    hold = corner[0] == full[0]
    if not hold:
        viol += 1
    print("(%d,%d,%d) corner=%s full=%s holds=%s gap1g=%d  [%.0fs]"
          % (p, q, r, corner[:4], full[:4], hold, g1, time.time() - t0), flush=True)
print("VIOLATIONS of corner==full in the wider box (C<=100, B<=1e5): %d / 56" % viol)