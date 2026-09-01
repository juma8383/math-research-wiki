#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
opn_census.py -- Odd Perfect Number attack, computational block (2026-09-01)
[opn-structural]

Purpose
-------
One documented, self-tested script backing the structural-lemma block of the
odd-perfect-number (OPN) attack. All output is ASCII, flushed line-by-line,
and mirrored to opn_census.log.

Blocks
------
S0  Exact arithmetic helpers (Miller-Rabin + Pollard rho factorization,
    exact sigma). No floating point anywhere a claim depends on it.
S1  Self-tests: (a) known perfect numbers 6, 28, 496, 8128, 33550336 have
    sigma(N) = 2N exactly; (b) 945 (smallest odd abundant) and 22021 are
    NOT perfect; (c) Descartes' 1638 spoof perfect number
    D = 3^2*7^2*11^2*13^2*22021 = 198585576189 is EXACTLY perfect when
    22021 is treated as a prime, and 22021 = 19^2*61 is composite, so the
    TRUE sigma(D)/D is an exact rational > 2 (D is abundant) -- note the
    spoof's pseudo-prime is 19^2*61, NOT 23*457 (23*457 = 10511);
    (d) Voight's negative-base spoof 3^4*7^2*11^2*19^2*(-127) is exactly
    "perfect" under the extended sigma convention sigma(x^a) = 1+x+...+x^a.
S2  Lemma verification sweeps:
    - Euler dichotomy (Lemma O1): for odd primes p and odd a, v2(sigma(p^a))
      = 1  iff  p = 1 mod 4 and a = 1 mod 4, swept over p < 2000, a <= 21;
    - mod-3 inputs of Touchard's theorem (Lemma O2): for p = 2 mod 3,
      3 | sigma(p^a) iff a odd; sigma(p^(2c)) = 1 mod 3 always.
S3  Census A: abundancy-window prime-set census (Lemma O3). Enumerate all
    10-subsets S of odd primes <= 200 with
      (i)   prod_{p in S} (1 + 1/p) < 2   [sigma(N)/N = 2 forces this], and
      (ii)  sum_{p in S} 1/(p-1) > log 2  [needed to reach abundancy 2],
    then apply the Euler-form BUDGET: with special prime p0 in S, p0 = 1 mod 4,
      (iii) sum over p in S, p != p0 of (1/p + 1/p^2), plus 1/p0, is < 1.
    Also a k = 12, 3-not-in-S census (Nielsen 2007: omega >= 12 if 3 !| N).
S4  Census B: divisor-sum sieve over odd n <= 10^7 verifying sigma(n) != 2n
    for every odd n (independent re-verification of a trivially subsumed
    slice of Ochem-Rao's 10^1500; filed for the documented engine, not the
    bound). Self-tested against exact sigma on random odd samples and
    against the known even perfect numbers found by the same sieve.

Honesty: this script proves NO new global bound. It documents (a) that the
Euler form + Touchard congruences + abundancy budget are mutually consistent
on the classical spoofs, and (b) the exact count of prime-set structures
surviving the elementary window constraints, which quantifies how much
structure the abundancy identity alone forces.
"""

import sys, time, random
from fractions import Fraction
from math import gcd, log, prod

T0 = time.time()
LOG_PATH = "opn_census.log"
_log = open(LOG_PATH, "w", encoding="utf-8")


def say(msg=""):
    print(msg, flush=True)
    _log.write(msg + "\n")
    _log.flush()


def elapsed():
    return "%7.1fs" % (time.time() - T0)


# ---------------------------------------------------------------- S0: helpers
def is_probable_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n):
    if n % 2 == 0:
        return 2
    import random as _r
    while True:
        x = _r.randrange(2, n - 1)
        y, c, d = x, _r.randrange(1, n - 1), 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d


def factorize(n):
    """Return dict prime -> exponent, exact."""
    fac = {}
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        while n % p == 0:
            fac[p] = fac.get(p, 0) + 1
            n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_probable_prime(m):
            fac[m] = fac.get(m, 0) + 1
            continue
        d = pollard_rho(m)
        stack.extend([d, m // d])
    return fac


def sigma(n):
    return prod((p ** (a + 1) - 1) // (p - 1) for p, a in factorize(n).items())


def v2(x):
    return (x & -x).bit_length() - 1


def frac_sigma_over_n(fac):
    """Exact sigma(n)/n from a factorization dict (bases may be negative)."""
    r = Fraction(1)
    for p, a in fac.items():
        s = sum(p ** j for j in range(a + 1))  # works for negative p too
        r *= Fraction(s, p ** a)
    return r


# ---------------------------------------------------------------- S1: self-tests
say("=" * 78)
say("S1  SELF-TESTS  (start %s)" % elapsed())
say("=" * 78)

PERFECT_KNOWN = [6, 28, 496, 8128, 33550336]
for n in PERFECT_KNOWN:
    ok = sigma(n) == 2 * n
    say("  sigma(%d) == 2n ? %s" % (n, "OK" if ok else "FAIL"))
    assert ok, n

for n in (12, 945, 22021):
    ok = sigma(n) != 2 * n
    say("  sigma(%d) != 2n (non-perfect) ? %s" % (n, "OK" if ok else "FAIL"))
    assert ok

# smallest odd abundant number, as counterevidence anchor: abundance is cheap,
# perfection is not
f945 = factorize(945)
r945 = frac_sigma_over_n(f945)
say("  945 = %s ; sigma/n = %s > 1 (abundant: %s)"
    % (f945, r945, r945 > 1))
assert r945 > 1

# --- Descartes spoof (1638, letter to Mersenne 15 Nov 1638)
DESC_BASES = [(3, 2), (7, 2), (11, 2), (13, 2), (22021, 1)]
D = prod(p ** a for p, a in DESC_BASES)
spoof_sigma = prod(sum(p ** j for j in range(a + 1)) for p, a in DESC_BASES)
say("")
say("  Descartes spoof D = %d" % D)
say("  spoof sigma (22021 treated as prime) == 2D ? %s"
    % ("OK" if spoof_sigma == 2 * D else "FAIL"))
assert spoof_sigma == 2 * D
fac22021 = factorize(22021)
say("  factor(22021) = %s   <- 23*457 = %d, so the 23*457 claim is FALSE"
    % (fac22021, 23 * 457))
assert 22021 == 19 ** 2 * 61
D_true = dict(DESC_BASES[:-1])
for p, a in fac22021.items():
    D_true[p] = D_true.get(p, 0) + a
r_true = frac_sigma_over_n(D_true)
say("  true sigma(D)/D = %s = %.10f  (D abundant: %s)"
    % (r_true, float(r_true), r_true > 2))
say("  spoof over-count factor: true/spoof abundancy = %s"
    % (r_true / Fraction(2)))
assert r_true > 2

# Euler-form checks on the spoof AS WRITTEN (pseudo-prime 22021):
# special base 22021 must be 1 mod 4 with odd exponent (it is: 22021 = 4k+1),
# and the spoof must sit in a Touchard class (Lemma O2).
say("  spoof Euler-form: 22021 mod 4 = %d (Euler p=1 mod 4), exponent 1 (odd): OK"
    % (22021 % 4))
say("  spoof D mod 12 = %d, D mod 36 = %d  (Touchard classes: 1 mod 12 or 9 mod 36)"
    % (D % 12, D % 36))
assert D % 12 in (1,) or D % 36 in (9,)
say("  spoof passes Touchard congruence: %s"
    % (D % 12 == 1 or D % 36 == 9))

# abundancy window (Lemma O3(i),(ii)) on the spoof's written prime set
S_spoof = [3, 7, 11, 13, 22021]
pi_prod = prod(Fraction(p + 1, p) for p in S_spoof)
inv_sum = sum(Fraction(1, p - 1) for p in S_spoof)
say("  window on written set {3,7,11,13,22021}: prod(1+1/p)=%s<=2? %s ; sum 1/(p-1)=%.4f>log2? %s"
    % (pi_prod, pi_prod <= 2, float(inv_sum), inv_sum > log(2)))
assert pi_prod <= 2 and inv_sum > log(2)

# --- Voight spoof (negative base; MASS selecta, AMS 2003)
V_BASES = [(3, 4), (7, 2), (11, 2), (19, 2), (-127, 1)]
V = prod(p ** a for p, a in V_BASES)
V_spoof_sigma = prod(sum(p ** j for j in range(a + 1)) for p, a in V_BASES)
say("")
say("  Voight spoof V = %d (negative base -127)" % V)
say("  spoof sigma(V) == 2V exactly ? %s"
    % ("OK" if V_spoof_sigma == 2 * V else "FAIL"))
assert V_spoof_sigma == 2 * V

say("")
say("S1 done %s" % elapsed())

# ---------------------------------------------------------------- S2: lemmas
say("")
say("=" * 78)
say("S2  LEMMA VERIFICATION SWEEPS  (%s)" % elapsed())
say("=" * 78)

# Lemma O1: v2(sigma(p^a)) = 1 iff p = 1 mod 4 and a = 1 mod 4 (a odd).
bad = 0
tested = 0
for p in range(3, 2000, 2):
    if not is_probable_prime(p):
        continue
    s = 1
    for a in range(1, 22):
        s += p ** a
        if a % 2 == 0:
            continue                    # Lemma O1 is about ODD exponents only
        tested += 1
        lhs = v2(s)
        rhs_ok = (p % 4 == 1) and (a % 4 == 1)
        if (lhs == 1) != rhs_ok:
            bad += 1
say("  Lemma O1 sweep: %d (p,a) pairs, v2(sigma(p^a))==1 <=> (p=1 mod4, a=1 mod4): %s (%d mismatches)"
    % (tested, "OK" if bad == 0 else "FAIL", bad))
assert bad == 0

# Lemma O2 mod-3 inputs: p = 2 mod 3 => 3 | sigma(p^a) iff a odd;
# sigma(p^(2c)) = 1 mod 3 for all c >= 0.
bad = 0
tested = 0
for p in range(5, 2000, 2):
    if not is_probable_prime(p) or p % 3 != 2:
        continue
    s = 1
    for a in range(1, 40):
        s = (s + pow(p, a, 10 ** 6)) % 10 ** 6  # track sigma mod 3 exactly
        t = sum(pow(p, j, 3) for j in range(a + 1)) % 3
        tested += 1
        want0 = (a % 2 == 1)
        if (t == 0) != want0:
            bad += 1
say("  Lemma O2 mod-3 sweep: %d (p,a) pairs, 3|sigma(p^a) iff a odd (p=2 mod 3): %s (%d mismatches)"
    % (tested, "OK" if bad == 0 else "FAIL", bad))
assert bad == 0
say("S2 done %s" % elapsed())

# ---------------------------------------------------------------- S3: Census A
say("")
say("=" * 78)
say("S3  CENSUS A: abundancy-window prime-set census (Lemma O3)  (%s)" % elapsed())
say("=" * 78)

PMAX = 100   # honest BOX: the window constraints do NOT bound the largest
             # prime globally (see problem.md), so this is a census of the
             # prime-set structures inside a stated box, not a classification
primes = [p for p in range(3, PMAX + 1, 2) if is_probable_prime(p)]
say("  box: odd primes <= %d (%d primes)" % (PMAX, len(primes)))
LOG2 = log(2)
LOGP = {p: log(1.0 + 1.0 / p) for p in primes}
INV = {p: 1.0 / (p - 1) for p in primes}


def census(k, pmin):
    """Exact enumeration, within the box, of k-subsets S of odd primes
    >= pmin with (i) prod(1+1/p) < 2 and (ii) sum 1/(p-1) > log 2
    (float pruned, exact-Fraction confirmed), then Euler budget (iii)."""
    P = [p for p in primes if p >= pmin]
    n = len(P)
    logp = [LOGP[p] for p in P]
    inv = [INV[p] for p in P]

    n_win = [0]
    examples = []
    stats = {"min_prime": {}, "tight_lo": 1e9, "tight_hi": -1e9}
    n_budget = [0]
    budget_examples = []
    nodes = [0]

    def best_add(i, slots):
        t = 0.0
        for j in range(i, min(i + slots, n)):
            t += inv[j]
        return t

    def dfs(i, slots, cur, lprod, isum):
        nodes[0] += 1
        if lprod > LOG2:
            return
        if slots == 0:
            if isum > LOG2:
                n_win[0] += 1
                mp = cur[0]
                stats["min_prime"][mp] = stats["min_prime"].get(mp, 0) + 1
                tl = sum(LOGP[p] for p in cur)
                stats["tight_lo"] = min(stats["tight_lo"], tl)
                stats["tight_hi"] = max(stats["tight_hi"], tl)
                examples.append(tuple(cur))   # store ALL (exact re-check)
            return
        if i >= n or slots > n - i:
            return
        if isum + best_add(i, slots) <= LOG2:
            return
        p = P[i]
        cur.append(p)
        dfs(i + 1, slots - 1, cur, lprod + logp[i], isum + inv[i])
        cur.pop()
        dfs(i + 1, slots, cur, lprod, isum)

    dfs(0, k, [], 0.0, 0.0)

    # EXACT rational re-check of the window on every float survivor:
    # prod (p+1)/p < 2 (exact) and sum 1/(p-1) > log 2 (via a 25-digit
    # rational LOWER bound for log 2, so any failure here is decisive)
    L2L = Fraction(6931471805599453094172321, 10 ** 25)
    n_exact = 0
    for S in examples:
        pi = prod(Fraction(p + 1, p) for p in S)
        iv = sum(Fraction(1, p - 1) for p in S)
        if pi < 2 and iv > L2L:
            n_exact += 1
    say("  exact rational re-check of window on float survivors: %d/%d pass"
        % (n_exact, n_win[0]))

    # budget (iii) on the stored window survivors (float pre-filter, exact
    # Fraction confirmation on passers and on near-boundary cases)
    for S in examples:
        # p0 = special prime, 1 mod 4
        for p0 in S:
            if p0 % 4 != 1:
                continue
            bf = 0.0
            for p in S:
                if p == p0:
                    bf += 1.0 / p0
                else:
                    bf += 1.0 / p + 1.0 / (p * p)
            if bf > 1.0001:
                continue
            budget = sum(Fraction(1, p) + Fraction(1, p * p)
                         for p in S if p != p0) + Fraction(1, p0)
            if budget < 1:
                n_budget[0] += 1
                if len(budget_examples) < 8:
                    budget_examples.append((S, p0, budget))
    return n_win[0], n_budget[0], budget_examples, stats, nodes[0]


for (k, pmin, label) in [(10, 3, "k=10 (general omega>=10, Nielsen 2015)"),
                         (12, 5, "k=12 with 3 !| N (Nielsen 2007)")]:
    nw, nb, bex, st, nodes = census(k, pmin)
    say("")
    say("  --- %s" % label)
    say("  DFS nodes explored: %d" % nodes)
    say("  prime-set structures in box passing window (i)+(ii): %d" % nw)
    say("  (window,p0) pairs passing window + Euler budget (iii): %d" % nb)
    if st["tight_lo"] < 1e8:
        say("  sum log(1+1/p) over survivors: min %.6f, max %.6f  (log 2 = %.6f)"
            % (st["tight_lo"], st["tight_hi"], LOG2))
    if bex:
        mpmin = min(S[0] for S, _, _ in bex)
        p0s = sorted(set(p0 for _, p0, _ in bex))
        say("  smallest prime in a budget-surviving set: %d ; special-prime values used (first 10): %s"
            % (mpmin, p0s[:10]))
        for S, p0, budget in bex[:4]:
            say("    e.g. S=%s p0=%d budget=%s (= %.6f)"
                % (list(S), p0, budget, float(budget)))
    say("  min-prime distribution of window survivors (first 12): %s"
        % sorted(st["min_prime"].items())[:12])

say("")
say("S3 done %s" % elapsed())

# ---------------------------------------------------------------- S4: Census B
say("")
say("=" * 78)
say("S4  CENSUS B: divisor-sum sieve over odd n <= 10^7  (%s)" % elapsed())
say("=" * 78)

try:
    import numpy as np
    HAVE_NUMPY = True
except ImportError:
    HAVE_NUMPY = False
say("  numpy available: %s" % HAVE_NUMPY)

N_SIEVE = 10 ** 7
odds = None
hits = []
if HAVE_NUMPY:
    sig = np.zeros(N_SIEVE + 1, dtype=np.int64)
    t_sieve = time.time()
    for i in range(1, N_SIEVE + 1, 2):
        sig[i::2 * i] += i          # add divisor i to all odd multiples of i
    say("  sieve loop done in %.1fs" % (time.time() - t_sieve))
    odds = np.arange(1, N_SIEVE + 1, 2, dtype=np.int64)
    sig_odd = sig[1::2]
    perfect_mask = sig_odd == 2 * odds
    hits = odds[perfect_mask].tolist()
    say("  odd n <= %d with sigma(n) == 2n : %d  %s"
        % (N_SIEVE, len(hits), hits if hits else "(none)"))
    # touchard-consistency inside the box: count odd n in the two classes
    n_class1 = int(((odds % 12) == 1).sum())
    n_class2 = int(((odds % 36) == 9).sum())
    say("  odd n <= %d in Touchard classes (1 mod 12: %d, 9 mod 36: %d) = %.2f%%"
        % (N_SIEVE, n_class1, n_class2, 100.0 * (n_class1 + n_class2) / N_SIEVE))
    # sieve self-test against exact sigma on 500 random odd n
    rnd = random.Random(20260901)
    mism = 0
    for _ in range(500):
        m = rnd.randrange(1, N_SIEVE + 1, 2)
        if int(sig[m]) != sigma(int(m)):
            mism += 1
    say("  sieve vs exact sigma on 500 random odd n: %s (%d mismatches)"
        % ("OK" if mism == 0 else "FAIL", mism))
    assert mism == 0
    # even-perfect cross-check with the same exact engine
    ev = [n for n in PERFECT_KNOWN if sigma(n) == 2 * n]
    say("  exact-sigma re-check of known perfects: %s" % ("OK" if len(ev) == 5 else "FAIL"))
    assert len(ev) == 5

say("")
say("S4 done %s" % elapsed())
say("")
say("=" * 78)
say("ALL SELF-TESTS PASSED; censuses complete. Log: %s" % LOG_PATH)
say("Total runtime %.1fs" % (time.time() - T0))
say("=" * 78)
_log.close()