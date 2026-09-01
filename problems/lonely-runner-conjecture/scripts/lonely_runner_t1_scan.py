#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t1_scan.py -- Conjecture T1 deep-box scan
=======================================================
CONTINUE block 2026-09-01. Conjecture T1 (problem.md): every tight n-set
(kappa = 1/(n+1) exactly) satisfies (n+1) | no v in V.  Evidence so far:
11/11 tight sets in boxes to [1,60] (n<=5), [1,22] (n=6,8), [1,21] (n=9),
[1,16] (n=7).  This scan widens the boxes flagged "Testable next":
  n=6 beyond [1,22] -> [1,30]
  n=7 beyond [1,16] -> [1,22]
  n=10 first scan   -> [1,14]
and records the T1 condition ("tight with (n+1)|v") plus the T2 pattern
(non-{1..n} tight sets).

Engine: exact (Lemma L1 -- kappa = max over candidate times
t in {m/2v_i} union {m/(v_i+v_j)}), but with an all-integer fast path:
for t = p/q,  ||t*v|| = dist(p*v, q*Z)/q, so f(t) = g/q with g = min_i
dist(p*v_i, q*Z) an integer; tightness comparisons are cross-multiplied.
Two PROVED filters run before the full evaluation:
  (T3, Lemma T3)   every tight n-set contains a multiple of every M=2..n;
  (t0 check)       f(1/(n+1)) <= kappa = 1/(n+1) forces some v = 0,+-1
                   (mod n+1).
Cross-validation: the integer engine must agree with the Fraction-based
kappa_exact (imported from lonely_runner_census.py) on ALL sets of a
small box (n=4, [1,14]) before the deep boxes run.
ASCII output, flushed (piped stdout block-buffers on Windows).
"""

import sys
import os
import time
import math
from fractions import Fraction
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import kappa_exact  # noqa: E402


def out(s=""):
    print(s, flush=True)


def dist_res(v, q):
    """dist(v, qZ) for v >= 0 integer, q > 0: min_k |v - k q|."""
    r = v % q
    return min(r, q - r)


def kappa_int(V):
    """Exact kappa(V) as Fraction, all-integer arithmetic (Lemma L1)."""
    V = list(V)
    n = len(V)
    best = Fraction(0)
    cands = set()
    for v in V:
        for m in range(0, 2 * v + 1):
            cands.add((m, 2 * v))
    for i in range(n):
        for j in range(i + 1, n):
            s = V[i] + V[j]
            for m in range(0, s + 1):
                cands.add((m, s))
    for (p, q) in cands:
        g = min(dist_res(p * v, q) for v in V)
        val = Fraction(g, q)
        if val > best:
            best = val
    return best


def passes_filters(V, n):
    """Proved necessary conditions for tightness (cheap, run first)."""
    qn = n + 1
    # T3: a multiple of every M = 2..n
    for M in range(2, n + 1):
        if not any(v % M == 0 for v in V):
            return False
    # t0 check: some v = 0, +-1 (mod n+1)
    if not any(dist_res(v, qn) <= 1 for v in V):
        return False
    return True


def main():
    out("lonely_runner_t1_scan.py -- Conjecture T1 deep box scan, %s"
        % time.ctime())
    out("python %s" % sys.version.split()[0])
    out("")

    # ---- cross-validation: integer engine vs kappa_exact ----------------
    bad = 0
    checked = 0
    for n, N in [(4, 14)]:
        for V in combinations(range(1, N + 1), n):
            k_ref = kappa_exact(V, include_diff=False)
            k_int = kappa_int(V)
            checked += 1
            if k_ref != k_int:
                bad += 1
                out("  MISMATCH V=%s ref=%s int=%s" % (V, k_ref, k_int))
    out("cross-validation: %d sets checked, %d mismatches (must be 0)"
        % (checked, bad))
    if bad:
        out("ABORT: integer engine disagrees with reference.")
        return
    out("")

    for (n, N) in [(10, 14), (7, 22), (6, 30)]:
        bound = Fraction(1, n + 1)
        t0 = time.time()
        tight = []
        viol = 0
        cnt = 0
        full_evals = 0
        for V in combinations(range(1, N + 1), n):
            g = 0
            for v in V:
                g = math.gcd(g, v)
            if g != 1:
                continue
            cnt += 1
            if not passes_filters(V, n):
                # not tight: some t has f > 1/(n+1)?  No -- filters are
                # necessary conditions; failing them proves NOT tight only
                # via T3 (proved).  The t0 check is also necessary given
                # kappa = 1/(n+1) is attained; failing it means kappa > bound
                # or kappa unattained-impossible (f continuous), so also
                # not tight.  Safe to skip the full evaluation.
                continue
            full_evals += 1
            r = tight_check_int(V, n)
            if r == 1:
                tight.append(V)
            elif r < 0:
                viol += 1
                out("  *** COUNTEREXAMPLE *** V=%s" % (V,))
        withmult = [V for V in tight if any(v % (n + 1) == 0 for v in V)]
        nonc = [V for V in tight if V != tuple(range(1, n + 1))]
        out("T1-SCAN  n=%d  [1,%d]  (primitive %d-subsets, bound 1/%d)"
            % (n, N, n, n + 1))
        out("  sets tested           : %d" % cnt)
        out("  full kappa evals      : %d (filters rejected the rest)" % full_evals)
        out("  violations k < bound  : %d" % viol)
        out("  tight sets            : %d" % len(tight))
        out("  tight non-{1..n}      : %d%s"
            % (len(nonc), ("  " + ", ".join(str(V) for V in nonc[:15]))
               if nonc else ""))
        out("  tight with (n+1)|v    : %d   <-- T1 says this must be 0"
            % len(withmult))
        for V in withmult:
            out("      T1 VIOLATION: %s" % (V,))
        out("  elapsed               : %.1f s" % (time.time() - t0))
        out("")
    out("Legend: 'tight with (n+1)|v' is the direct Conjecture T1 test.")
    out("All-zero = T1 evidence extended to the widened boxes.")


def tight_check_int(V, n):
    """0/1/-1 = kappa >, ==, < 1/(n+1)  (integer engine, early exit)."""
    V = list(V)
    qn = n + 1
    best_num, best_den = 0, 1
    cands = set()
    for v in V:
        for m in range(0, 2 * v + 1):
            cands.add((m, 2 * v))
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            s = V[i] + V[j]
            for m in range(0, s + 1):
                cands.add((m, s))
    for (p, q) in cands:
        g = min(dist_res(p * v, q) for v in V)
        if g * best_den > best_num * q:
            best_num, best_den = g, q
        if best_num * qn > best_den:
            return 0
    if best_num * qn == best_den:
        return 1
    if best_num * qn > best_den:
        return 0
    return -1


if __name__ == "__main__":
    main()