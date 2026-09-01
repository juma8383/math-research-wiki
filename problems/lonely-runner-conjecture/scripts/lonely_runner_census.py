#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_census.py -- exact census engine for the Lonely Runner Conjecture
================================================================================

Problem (survey form; Perarnau--Serra, "The Lonely Runner Conjecture turns 60",
arXiv:2409.20160, Conjecture 2): for every n and every set of n nonzero speeds
v_1..v_n there is a time t with  min_i ||t v_i|| >= 1/(n+1),  where ||x|| is
the distance from x to the nearest integer.

Loneliness gap of a speed set V:
    kappa(V) = sup_{t in (0,1)} min_i ||t v_i||.
LRC(n) holds  <=>  kappa(V) >= 1/(n+1) for every n-set V.
By homogeneity (Lemma L2a in problem.md) it suffices to census primitive
positive integer n-sets with distinct entries (duplicates are WLOG-removable,
signs are WLOG-positive).

Engine (Lemma L1, proved in problem.md): kappa(V) is a MAXIMUM, attained on
the finite candidate set
    C = { m/(2 v_i) : 1 <= m < 2 v_i }      (kinks of g_i(t) = ||t v_i||)
      U { m/(v_i + v_j) : 1 <= m < v_i+v_j } (an interior maximizer needs one
            rising and one falling tight runner => t(v_i+v_j) ≡ 0 mod 1).
The engine ALSO scans the redundant class { m/|v_i - v_j| } and self-checks
that the redundant class never changes the value (internal consistency check,
self-test T4).

Self-tests (run FIRST; abort on any failure):
  T1  kappa({1,...,n}) = 1/(n+1) exactly, n = 1..9        (Lemma L3)
  T2  kappa({3,8,11,19}) = 7/30 exactly  [Fan-Sun 2023, arXiv:2306.10417,
      amending Kravitz's Loneliness Spectrum Conjecture; value search-derived,
      flagged [summary] in problem.md -- this test verifies it independently]
  T3  engine value >= exact dense rational grid (200001 points) on 300 random
      primitive sets, n = 2..5, v <= 30
  T4  redundant difference-class never changes kappa

Census (all exact rational arithmetic):
  A  n = 2..6: exhaustive primitive n-subsets of [1,12].  LRC(n) is a THEOREM
     for n <= 6 (n=6: Barajas-Serra 2008, Electron. J. Combin. 15(1) R48), so
     expect 0 violations of kappa >= 1/(n+1); also a tight-set census
     (which sets attain kappa = 1/(n+1) exactly).
  B  n = 7: exhaustive primitive 7-subsets of [1,16].  Independent box check
     of LRC(7) (theorem of Barajas-Serra; also claimed by Rosenfeld 2025,
     arXiv:2509.14111, preprint).
  C  n = 8: exhaustive primitive 8-subsets of [1,15].  First open slice
     beyond Rosenfeld's claim; a bounded probe only, NO claim beyond the box.
  D  random primitive n-sets: n=7 from [1,400], n=8 from [1,300].

ASCII output only. Every number reported by this script is computed here;
external figures are cited in problem.md.
"""

import sys
import time
import itertools
import random
from fractions import Fraction
from math import gcd

import numpy as np

RANDOM_SEED = 20260901
random.seed(RANDOM_SEED)

OUT_LINES = []


def out(s=""):
    print(s)
    OUT_LINES.append(s)


def candidate_times(V, include_diff=True):
    """All candidate times t = p/q in (0,1), returned as reduced (p, q) pairs."""
    cands = set()
    for v in V:
        for m in range(1, 2 * v):
            cands.add((m, 2 * v))
    n = len(V)
    for i in range(n):
        for j in range(i + 1, n):
            s = V[i] + V[j]
            for m in range(1, s):
                cands.add((m, s))
            if include_diff:
                d = abs(V[i] - V[j])
                for m in range(1, d):
                    cands.add((m, d))
    reduced = set()
    for p, q in cands:
        g = gcd(p, q)
        reduced.add((p // g, q // g))
    return sorted(reduced, key=lambda pq: (pq[1], pq[0]))


def kappa_exact(V, include_diff=True, want_t=False):
    """Exact kappa(V) as a Fraction (Lemma L1 finite maximum)."""
    V = sorted(V)
    cands = candidate_times(V, include_diff)
    P = np.array([p for p, q in cands], dtype=np.int64)
    Q = np.array([q for p, q in cands], dtype=np.int64)
    Va = np.array(V, dtype=np.int64)
    R = (P[:, None] * Va[None, :]) % Q[:, None]
    D = np.minimum(R, Q[:, None] - R)
    m = D.min(axis=1)                      # value at candidate = m/Q
    flt = m.astype(np.float64) / Q
    j = int(np.argmax(flt))
    best = Fraction(int(m[j]), int(Q[j]))
    # exact sweep over the float-argmax neighbourhood (rationals with
    # q <= 2*max(V) are separated by > 1e-6, so a 1e-9 window is safe)
    near = np.where(flt >= flt[j] - 1e-9)[0]
    for idx in near:
        val = Fraction(int(m[idx]), int(Q[idx]))
        if val > best:
            best = val
    if want_t:
        argmax_t = None
        for idx in near:
            if Fraction(int(m[idx]), int(Q[idx])) == best:
                argmax_t = Fraction(int(P[idx]), int(Q[idx]))
                break
        return best, argmax_t
    return best


def primitive_subsets(N, n):
    """All n-subsets of [1,N] with gcd 1, as sorted tuples."""
    for c in itertools.combinations(range(1, N + 1), n):
        g = 0
        for x in c:
            g = gcd(g, x)
            if g == 1:
                break
        if g == 1:
            yield c


def random_primitive_sets(N, n, count):
    got = 0
    while got < count:
        c = tuple(sorted(random.sample(range(1, N + 1), n)))
        g = 0
        for x in c:
            g = gcd(g, x)
        if g == 1:
            got += 1
            yield c


# ---------------------------------------------------------------- self-tests

def self_test_grid(V, G=200001):
    """Exact kappa lower bound from a dense rational grid t = j/G."""
    Va = np.array(sorted(V), dtype=np.int64)
    J = np.arange(G + 1, dtype=np.int64)
    R = (J[:, None] * Va[None, :]) % G
    D = np.minimum(R, G - R)
    m = D.min(axis=1)
    return Fraction(int(m.max()), G)


def run_self_tests():
    out("=" * 78)
    out("SELF-TESTS")
    out("=" * 78)
    ok = True

    # T1: Lemma L3
    for n in range(1, 10):
        V = tuple(range(1, n + 1))
        k = kappa_exact(V)
        good = (k == Fraction(1, n + 1))
        ok &= good
        out("T1  kappa(1..%d) = %-8s expected 1/%-3d %s"
            % (n, str(k), n + 1, "OK" if good else "FAIL"))
        ok &= good

    # T2: Fan-Sun spectrum counterexample value
    k = kappa_exact((3, 8, 11, 19))
    good = (k == Fraction(7, 30))
    ok &= good
    out("T2  kappa(3,8,11,19) = %-6s expected 7/30   %s"
        % (str(k), "OK" if good else "FAIL"))

    # T3: engine vs exact dense grid
    fails = 0
    for trial in range(300):
        n = random.randint(2, 5)
        V = tuple(sorted(random.sample(range(1, 31), n)))
        g = 0
        for x in V:
            g = gcd(g, x)
        if g != 1:
            continue
        ke = kappa_exact(V)
        kg = self_test_grid(V)
        if not (ke >= kg):
            fails += 1
            out("T3  FAIL V=%s engine=%s grid=%s" % (V, ke, kg))
        if ke - kg > Fraction(max(V), 200001):
            fails += 1
            out("T3  SUSPECT V=%s engine=%s grid=%s" % (V, ke, kg))
    out("T3  engine >= dense grid on 300 random sets (n=2..5, v<=30): "
        "%d failures %s" % (fails, "OK" if fails == 0 else "FAIL"))
    ok &= (fails == 0)

    # T4: redundant difference class never changes kappa
    mism = 0
    tested = 0
    for V in random_primitive_sets(60, 5, 500):
        a = kappa_exact(V, include_diff=False)
        b = kappa_exact(V, include_diff=True)
        tested += 1
        if a != b:
            mism += 1
            out("T4  MISMATCH V=%s %s vs %s" % (V, a, b))
    out("T4  difference-class redundancy: %d sets tested, %d mismatches %s"
        % (tested, mism, "OK" if mism == 0 else "FAIL"))
    ok &= (mism == 0)

    out("SELF-TESTS: %s" % ("ALL PASSED" if ok else "FAILURE -- ABORT"))
    out("")
    if not ok:
        sys.exit(1)


# -------------------------------------------------------------------- census

def census(name, gen, n, label):
    """Census over an iterable of primitive n-sets. Returns summary dict."""
    bound = Fraction(1, n + 1)
    cnt = 0
    tight = []
    viol = []
    best = None
    bestV = None
    t0 = time.time()
    for V in gen:
        k = kappa_exact(V)
        cnt += 1
        if best is None or k < best:
            best, bestV = k, V
        if k == bound:
            tight.append(V)
        elif k < bound:
            viol.append((V, k))
    out("-" * 78)
    out("CENSUS %s  (n=%d, %s, LRC bound 1/%d)" % (name, n, label, n + 1))
    out("  sets tested           : %d" % cnt)
    out("  min kappa found       : %s  at V=%s" % (str(best), str(bestV)))
    out("  violations k < 1/(n+1): %d %s"
        % (len(viol), "  *** COUNTEREXAMPLE *** " + str(viol[:5]) if viol else ""))
    out("  tight sets k = 1/(n+1): %d" % len(tight))
    if tight:
        show = tight[:12]
        out("    first tight sets    : " + ", ".join(str(V) for V in show))
        noncons = [V for V in tight if list(V) != list(range(1, n + 1))]
        out("    tight non-{1..n}    : %d%s"
            % (len(noncons),
               ("  e.g. " + ", ".join(str(V) for V in noncons[:8])) if noncons else ""))
    out("  elapsed               : %.1f s" % (time.time() - t0))
    return {"n": n, "count": cnt, "min": best, "tight": len(tight),
            "viol": len(viol), "noncons": len(tight) - len([1 for V in tight if list(V) == list(range(1, n + 1))])}


def main():
    out("lonely_runner_census.py -- exact LRC census, seed %d" % RANDOM_SEED)
    out("python %s / numpy %s" % (sys.version.split()[0], np.__version__))
    out("")

    run_self_tests()

    summaries = []
    # A: theorem slice n = 2..6 (box check)
    for n in range(2, 7):
        summaries.append(census("A%d" % n, primitive_subsets(12, n), n,
                                "exhaustive primitive n-subsets of [1,12]"))
    # B: n = 7 (Barajas-Serra theorem; Rosenfeld preprint)
    summaries.append(census("B7", primitive_subsets(16, 7), 7,
                            "exhaustive primitive 7-subsets of [1,16]"))
    # C: n = 8 (open slice beyond Rosenfeld's claim)
    summaries.append(census("C8", primitive_subsets(15, 8), 8,
                            "exhaustive primitive 8-subsets of [1,15]"))
    # D: random probes
    summaries.append(census("D7", random_primitive_sets(400, 7, 10000), 7,
                            "10000 random primitive 7-subsets of [1,400]"))
    summaries.append(census("D8", random_primitive_sets(300, 8, 3000), 8,
                            "3000 random primitive 8-subsets of [1,300]"))

    out("=" * 78)
    out("SUMMARY (all values exact rationals from this run)")
    out("=" * 78)
    for s in summaries:
        out("  n=%d  sets=%-7d min_kappa=%-10s violations=%d  tight=%d"
            % (s["n"], s["count"], str(s["min"]), s["viol"], s["tight"]))
    out("")
    out("Legend: 'violations' = speed sets with kappa < 1/(n+1), i.e. LRC")
    out("counterexamples. Any nonzero count would be a disproof of LRC(n);")
    out("each such hit is exact-verified by construction (Lemma L1 engine).")
    out("'tight' = sets attaining kappa = 1/(n+1) exactly (extremal sets).")


if __name__ == "__main__":
    main()