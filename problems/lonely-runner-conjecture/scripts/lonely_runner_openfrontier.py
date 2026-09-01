#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_openfrontier.py -- census at the first OPEN frontier
==================================================================
CONTINUE block 2026-09-01. LRC is PROVEN for n <= 9 speeds (Rosenfeld
Math. Comp. 2026 n=7; Trakulthongchai ELJC 33(2) #P2.46 n=8,9) and
CLAIMED for n = 10..12 (arXiv:2604.23906, preprint).  The first OPEN
case is n = 13 speeds (14 runners).  This scan runs the exact integer
engine (Lemma L1, cross-validated lineage) on the largest feasible
exhaustive boxes at n = 11, 12, 13:
  n=11 [1,20], n=12 [1,18], n=13 [1,18]
recording violations of kappa >= 1/(n+1) (real LRC evidence at the
frontier), tight sets, and the T1 condition.  Small boxes -- this is a
first probe of open territory, not a deep census; stated as such.
ASCII output, flushed.
"""
import sys, os, time, math
from fractions import Fraction
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import kappa_exact  # noqa: E402


def out(s=""):
    print(s, flush=True)


def dist_res(v, q):
    r = v % q
    return min(r, q - r)


def kappa_int(V):
    """Exact kappa(V), integer arithmetic (Lemma L1)."""
    V = list(V)
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
    return Fraction(best_num, best_den)


def tight_check(V, n):
    """1 tight (kappa = 1/(n+1)), 0 not, -1 counterexample."""
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


def passes_filters(V, n):
    """Proved necessary conditions: T3 (multiple of every M=2..n) and
    the t0-attainment check (some v = 0,+-1 mod n+1)."""
    qn = n + 1
    for M in range(2, n + 1):
        if not any(v % M == 0 for v in V):
            return False
    if not any(dist_res(v, qn) <= 1 for v in V):
        return False
    return True


def main():
    out("lonely_runner_openfrontier.py -- first-open-frontier probe, %s"
        % time.ctime())
    out("python %s" % sys.version.split()[0])
    # cross-validation
    bad = 0
    for V in combinations(range(1, 13), 5):
        if kappa_int(V) != kappa_exact(V, include_diff=False):
            bad += 1
    out("cross-validation n=5 [1,12]: %d mismatches (must be 0)" % bad)
    if bad:
        return
    out("")

    for (n, N) in [(11, 20), (12, 18), (13, 18)]:
        t0 = time.time()
        tight = []
        viol = 0
        cnt = 0
        full = 0
        for V in combinations(range(1, N + 1), n):
            g = 0
            for v in V:
                g = math.gcd(g, v)
            if g != 1:
                continue
            cnt += 1
            if not passes_filters(V, n):
                continue
            full += 1
            r = tight_check(V, n)
            if r == 1:
                tight.append(V)
                out("  TIGHT: %s" % (V,))
            elif r < 0:
                viol += 1
                out("  *** COUNTEREXAMPLE *** V=%s" % (V,))
        out("OPEN-FRONTIER n=%d [1,%d]: %d primitive %d-subsets, %d full evals"
            % (n, N, cnt, n, full))
        out("  tight sets: %d %s" % (len(tight), tight[:10]))
        out("  violations (kappa < 1/(n+1)): %d" % viol)
        withmult = [V for V in tight if any(v % (n + 1) == 0 for v in V)]
        nonc = [V for V in tight if V != tuple(range(1, n + 1))]
        out("  tight with (n+1)|v (T1): %d   tight non-{1..n} (T2): %d"
            % (len(withmult), len(nonc)))
        out("  elapsed: %.1f s" % (time.time() - t0))
        out("")
    out("NOTE: n=11,12 overlap the preprint CLAIMS (unrefereed); n=13 is")
    out("genuinely open territory. Small boxes -- first probes only.")


if __name__ == "__main__":
    main()