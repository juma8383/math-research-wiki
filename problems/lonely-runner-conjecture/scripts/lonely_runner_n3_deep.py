#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_n3_deep.py -- deep tight-triple scan (n=3)
========================================================
CONTINUE block 2026-09-01 (companion to lonely_runner_t1_scan.py).
Question: is {1,2,3} the ONLY primitive tight 3-set (kappa = 1/4)?
Previous box [1,40] (tightscan W3) said yes within it.  This scan runs
[1,200] (1,313,400 primitive triples) with the proved filters + integer
engine.  T1 (no multiple of n+1 = 4 in a tight set) is checked too.
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


def kappa_int3(a, b, c):
    """Exact kappa of {a,b,c}, integer arithmetic (Lemma L1)."""
    V = (a, b, c)
    best_num, best_den = 0, 1
    cands = set()
    for v in V:
        for m in range(0, 2 * v + 1):
            cands.add((m, 2 * v))
    for i in range(3):
        for j in range(i + 1, 3):
            s = V[i] + V[j]
            for m in range(0, s + 1):
                cands.add((m, s))
    for (p, q) in cands:
        g = min(dist_res(p * v, q) for v in V)
        if g * best_den > best_num * q:
            best_num, best_den = g, q
    return Fraction(best_num, best_den)


def tight3(a, b, c):
    """1 tight (kappa = 1/4), 0 not, -1 counterexample (kappa < 1/4)."""
    V = (a, b, c)
    best_num, best_den = 0, 1
    cands = set()
    for v in V:
        for m in range(0, 2 * v + 1):
            cands.add((m, 2 * v))
    for i in range(3):
        for j in range(i + 1, 3):
            s = V[i] + V[j]
            for m in range(0, s + 1):
                cands.add((m, s))
    for (p, q) in cands:
        g = min(dist_res(p * v, q) for v in V)
        if g * best_den > best_num * q:
            best_num, best_den = g, q
        if best_num * 4 > best_den:      # early exit: kappa > 1/4
            return 0
    if best_num * 4 == best_den:
        return 1
    if best_num * 4 > best_den:
        return 0
    return -1


def main():
    out("lonely_runner_n3_deep.py -- tight-triple deep scan, %s" % time.ctime())
    out("python %s" % sys.version.split()[0])
    # cross-validation on [1,14]
    bad = 0
    for (a, b, c) in combinations(range(1, 15), 3):
        if kappa_int3(a, b, c) != kappa_exact((a, b, c), include_diff=False):
            bad += 1
    out("cross-validation [1,14]: %d mismatches (must be 0)" % bad)
    if bad:
        return

    N = 200
    t0 = time.time()
    tight = []
    viol = 0
    cnt = 0
    full = 0
    for (a, b, c) in combinations(range(1, N + 1), 3):
        if math.gcd(math.gcd(a, b), c) != 1:
            continue
        cnt += 1
        # filters (proved necessary): T3 for M=2,3; t0=1/4 attainment
        if not any(v % 2 == 0 for v in (a, b, c)):
            continue
        if not any(v % 3 == 0 for v in (a, b, c)):
            continue
        if not any(dist_res(v, 4) <= 1 for v in (a, b, c)):
            continue
        full += 1
        r = tight3(a, b, c)
        if r == 1:
            tight.append((a, b, c))
            out("  TIGHT: %s" % ((a, b, c),))
        elif r < 0:
            viol += 1
            out("  *** COUNTEREXAMPLE *** %s" % ((a, b, c),))
    out("n=3 deep box [1,%d]: %d primitive triples, %d full evals" % (N, cnt, full))
    out("tight sets: %d %s" % (len(tight), tight))
    out("violations (kappa < 1/4): %d" % viol)
    withmult = [V for V in tight if any(v % 4 == 0 for v in V)]
    out("tight with 4|v (T1 violations): %d" % len(withmult))
    out("elapsed: %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()