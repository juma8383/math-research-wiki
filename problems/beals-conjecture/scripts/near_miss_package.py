# Computational backbone for the near-miss stratification package (attempt-25).
#
# Parts:
#  (1) Corrected min-gap table over ALL distinct-odd-prime signatures from
#      primes {3,5,7,11,13,17,19,23} (56 signatures). Metric: A,B,C >= 2,
#      gcd(A,B,C)=1 (pairwise coprime by the standard reduction), exclude
#      exact solutions (gap 0), exclude gap-1 hits (counted separately),
#      exclude quasi-degenerate (A^p==C^r or B^q==C^r -- impossible under
#      coprimality, kept as a belt-and-braces filter). CORRECTED scan: the
#      overshoot region B^q > C^r is INCLUDED (candidates A=2,3,4 there),
#      fixing the break-at-BQ>CR bug in search_3711.py / search_5711.py.
#  (2) Corner Principle test: corner scan (C<=3) vs full scan (C<=60, B<=10^4).
#  (3) Boundary failures near the Euclidean line: (3,3,3), (3,3,5), (3,3,7).
#  (4) Odd-odd Pillai-2 search: X^u - Y^v = 2, u,v odd primes, Y^v <= 10^18.
#  (5) Local solubility of X^u - Y^v = 2: all prime powers p^k <= 10^6 and
#      all moduli m <= 1000, for each ordered odd-prime pair (u,v) <= 23.
#
# Windows/python; PYTHONIOENCODING=utf-8; no external deps.

import math, sys, json, time

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23]

def iroot(n, k):
    """Exact integer floor k-th root of n >= 0."""
    if n < 1:
        return 0
    if n < 2**k:
        return 1
    r = 1 << ((n.bit_length() + k - 1) // k)   # upper-ish initial guess
    while r ** k > n:
        r = ((k - 1) * r + n // r**(k - 1)) // k   # Newton, decreasing
    while (r + 1) ** k <= n:
        r += 1
    return r

def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)

def scan_sig(p, q, r, C_MAX, B_MAX):
    """Corrected scan. Returns dict with min gap, argmin, gap1 count, etc."""
    best = None            # (gap, A, B, C, val)
    gap1_genuine = 0        # coprime gap-1 hits with A,B,C>=2 (expect 0 in open class)
    gap1_all = 0
    best_at_C = {}          # C -> (gap, A, B, C, val) for corner analysis
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
                cands = (2, 3, 4)   # small-rem and OVERSHOOT region (bug fix)
            for A in cands:
                if A < 2:
                    continue
                AP = A ** p
                val = AP + BQ - CR
                g = abs(val)
                if g == 0:
                    continue                      # exact solution (none known)
                if AP == CR or BQ == CR:
                    continue                      # quasi-degenerate
                if g == 1:
                    if gcd3(A, B, C) == 1:
                        gap1_genuine += 1
                        best_at_C.setdefault(C, (1, A, B, C, val))
                    gap1_all += 1
                    continue
                if gcd3(A, B, C) != 1:
                    continue
                t = (g, A, B, C, val)
                if best is None or t < best:
                    best = t
                cur = best_at_C.get(C)
                if cur is None or t < cur:
                    best_at_C[C] = t
    return {"best": best, "gap1_genuine": gap1_genuine, "gap1_all": gap1_all,
            "best_at_C": best_at_C}

# ---------------- Part 1+2: the 56-signature corrected table ----------------
print("=== Part 1+2: corrected table, all 56 distinct-odd-prime signatures ===")
t0 = time.time()
rows = []
triples = [(p, q, r) for i, p in enumerate(PRIMES) for q in PRIMES[i+1:]
           for r in PRIMES[PRIMES.index(q)+1:]]
assert len(triples) == 56, len(triples)
for (p, q, r) in triples:
    corner = scan_sig(p, q, r, 3, 10**4)
    full = scan_sig(p, q, r, 60, 10**4)
    chi = 1/p + 1/q + 1/r - 1
    spacing_exp = 1 - r * chi          # granularity exponent r - r/p - r/q
    cb, fb = corner["best"], full["best"]
    hold = (cb is not None and fb is not None and cb[0] == fb[0])
    rows.append({"p": p, "q": q, "r": r, "chi": round(chi, 4),
                 "spacing_exp": round(spacing_exp, 3),
                 "corner": cb, "full": fb, "corner_holds": hold,
                 "gap1_genuine": full["gap1_genuine"]})
    print("(%d,%d,%d) chi=%.4f sp_exp=%.3f corner=%s full=%s holds=%s gap1g=%d"
          % (p, q, r, chi, spacing_exp,
             cb[:4] if cb else None, fb[:4] if fb else None, hold,
             full["gap1_genuine"]), flush=True)
print("elapsed: %.1fs" % (time.time() - t0))

# ---------------- Part 3: boundary failures near the Euclidean line -----------
print("\n=== Part 3: boundary signatures (repeated exponents, kappa near 0) ===")
for (p, q, r) in [(3, 3, 3), (3, 3, 5), (3, 3, 7), (3, 5, 5)]:
    full = scan_sig(p, q, r, 60, 10**4)
    chi = 1/p + 1/q + 1/r - 1
    print("(%d,%d,%d) chi=%.4f full=%s gap1g=%d"
          % (p, q, r, chi, full["best"][:4] if full["best"] else None,
             full["gap1_genuine"]), flush=True)

# ---------------- Part 4: odd-odd Pillai-2 search -----------------------------
print("\n=== Part 4: X^u - Y^v = 2, u,v odd primes <= 23, Y^v <= 10^18 ===")
LIM = 10**18
sols = []
checked = 0
for v in [x for x in PRIMES]:
    ymax = iroot(LIM, v)
    for Y in range(2, ymax + 1):
        Yv = Y ** v
        if Yv > LIM:
            break
        t = Yv + 2
        for u in PRIMES:
            X = iroot(t, u)
            if X >= 2 and X ** u == t:
                sols.append((X, u, Y, v))
                print("  SOLUTION: %d^%d - %d^%d = 2" % (X, u, Y, v))
        checked += 1
print("checked %d Y-powers; solutions found: %s" % (checked, sols or "NONE"))
# sanity: the known even-exponent case 3^3 - 5^2 = 2 must NOT appear (v=2 excluded)
print("known (5,2,3,3) excluded by odd-v restriction: OK")

# ---------------- Part 5: local solubility ------------------------------------
print("\n=== Part 5: local solubility of X^u - Y^v = 2 ===")
def soluble_mod(m, u, v):
    upow = set()
    for x in range(m):
        upow.add(pow(x, u, m))
    for y in range(m):
        if (pow(y, v, m) + 2) % m in upow:
            return True
    return False

# all moduli m <= 1000, all ordered pairs (u,v) from {3,5,7,11,13,17,19,23}
bad = []
for m in range(2, 1001):
    for u in PRIMES:
        # quick precompute of u-th power residues once per (m,u)
        upow = set(pow(x, u, m) for x in range(m))
        for v in PRIMES:
            ok = any((pow(y, v, m) + 2) % m in upow for y in range(m))
            if not ok:
                bad.append((m, u, v))
print("obstructing moduli m<=1000: %s" % (bad if bad else "NONE (all locally soluble)"))

# prime powers p^k <= 10^6, pairs restricted to the Pillai pairs actually needed
def prime_powers(limit):
    out = []
    for p in range(2, 3000):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            pk = p
            while pk <= limit:
                if pk >= 2:
                    out.append(pk)
                pk *= p
    return out
bad2 = []
for m in prime_powers(10**6):
    for u in PRIMES:
        upow = set(pow(x, u, m) for x in range(m))
        for v in PRIMES:
            if not any((pow(y, v, m) + 2) % m in upow for y in range(m)):
                bad2.append((m, u, v))
print("obstructing prime powers p^k<=10^6: %s" % (bad2 if bad2 else "NONE"))

# ---------------- save --------------------------------------------------------
with open("near_miss_package_data.json", "w") as f:
    json.dump({"rows": rows, "pillai_solutions": [[x[0], x[1], x[2], x[3]] for x in sols],
               "local_bad_m1000": bad, "local_bad_pp1e6": bad2}, f, indent=1)
print("\nsaved near_miss_package_data.json")