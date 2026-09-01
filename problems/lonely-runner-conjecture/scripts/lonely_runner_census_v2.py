#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_census_v2.py -- deeper exact LRC census (CONTINUE block 2026-09-01)
================================================================================

Extends lonely_runner_census.py (v1). Same exact engine (Lemma L1 candidate
set, rational arithmetic), imported from v1 so there is ONE engine definition:

    kappa(V) = sup_{t in (0,1)} min_i ||t v_i||   (exact Fraction, finite max)

Context update motivating v2 (verified 2026-09-01 against primary sources):
LRC is now PROVEN (computer-assisted) through 10 runners = 9 speeds --
  8 runners  (n=7 speeds): Rosenfeld, Mathematics of Computation,
      DOI 10.1090/mcom/4243 (published online 2026-08-10; arXiv:2509.14111).
  9,10 runners (n=8,9 speeds): Trakulthongchai, Electron. J. Combin. 33(2)
      (2026) #P2.46, DOI 10.37236/14972 (published 2026-06-05).
  11,12,13 runners (n=10,11,12 speeds): Sungkawichai--Trakulthongchai,
      arXiv:2604.23906 (PREPRINT, v1 2026-04-26) -- claimed, not yet
      peer-reviewed at the time of this run.
So every census block here is a box-level INDEPENDENT re-verification of a
published theorem slice (n = 6..9), plus a probe of the preprint slice (n=10).
NO claim beyond the boxes.

Blocks (all exhaustive-within-box, primitive sets only, Lemma L2a):
  A6x : n=6, exhaustive primitive 6-subsets of [1,22]  -- v1 box was [1,12];
        tests whether the "no non-consecutive tight set at n=6" finding was
        a box artifact.
  E8  : n=8, exhaustive primitive 8-subsets of [1,22]  -- v1 box was [1,15].
  F9  : n=9, exhaustive primitive 9-subsets of [1,21]  -- new slice opened.
  G9  : 2000 random primitive 9-subsets of [1,300].
  H10 : 800 random primitive 10-subsets of [1,150]     -- preprint-slice probe.

Tight-set analysis: for EVERY tight set found we record the exact witnessing
time t and structural fields (max V; residues mod n+1; whether (n+1) divides
some element; whether max V = sum of two elements; missing residues), to test
the tight-set structure conjectures filed in problem.md.

ASCII output only; every print is flushed (v1's run was buffer-invisible).
"""

import sys
import os
import time
import itertools
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import (  # noqa: E402
    kappa_exact, candidate_times, primitive_subsets, random_primitive_sets,
)

import numpy as np  # noqa: E402


def out(s=""):
    print(s, flush=True)


# ---------------------------------------------------------------- self-tests

def grid_kappa(V, G=200001):
    """Exact kappa lower bound from a dense rational grid t = j/G."""
    Va = np.array(sorted(V), dtype=np.int64)
    J = np.arange(G + 1, dtype=np.int64)
    R = (J[:, None] * Va[None, :]) % G
    D = np.minimum(R, G - R)
    return Fraction(int(D.min(axis=1).max()), G)


def run_self_tests():
    out("=" * 78)
    out("SELF-TESTS (v2)")
    out("=" * 78)
    ok = True
    # T1: Lemma L3, extended to n = 1..12 (covers the new preprint slice)
    for n in range(1, 13):
        V = tuple(range(1, n + 1))
        k, t = kappa_exact(V, want_t=True)
        good = (k == Fraction(1, n + 1))
        ok &= good
        out("T1  kappa(1..%2d) = %-6s expected 1/%-2d  witness t=%-6s %s"
            % (n, str(k), n + 1, str(t), "OK" if good else "FAIL"))
    # T2: Fan-Sun spectrum value (regression vs v1)
    k = kappa_exact((3, 8, 11, 19))
    good = (k == Fraction(7, 30))
    ok &= good
    out("T2  kappa(3,8,11,19) = %-6s expected 7/30   %s"
        % (str(k), "OK" if good else "FAIL"))
    # T3: engine vs exact dense grid, larger sets this time (n=6..8)
    fails = 0
    import random
    random.seed(20260901)
    for trial in range(200):
        n = random.randint(6, 8)
        V = tuple(sorted(random.sample(range(1, 26), n)))
        g = 0
        for x in V:
            g = np.gcd(g, x)
        if g != 1:
            continue
        ke = kappa_exact(V)
        kg = grid_kappa(V)
        if not (ke >= kg) or ke - kg > Fraction(max(V), 200001):
            fails += 1
            out("T3  FAIL/SUSPECT V=%s engine=%s grid=%s" % (V, ke, kg))
    out("T3  engine >= dense grid on 200 random sets (n=6..8, v<=25): "
        "%d failures %s" % (fails, "OK" if fails == 0 else "FAIL"))
    ok &= (fails == 0)
    # T4: difference-class redundancy (regression vs v1, 300 sets)
    mism = 0
    tested = 0
    for V in random_primitive_sets(60, 5, 300):
        if kappa_exact(V, include_diff=False) != kappa_exact(V, include_diff=True):
            mism += 1
            out("T4  MISMATCH V=%s" % (V,))
        tested += 1
    out("T4  difference-class redundancy: %d sets tested, %d mismatches %s"
        % (tested, mism, "OK" if mism == 0 else "FAIL"))
    ok &= (mism == 0)
    out("SELF-TESTS: %s" % ("ALL PASSED" if ok else "FAILURE -- ABORT"))
    out("")
    if not ok:
        sys.exit(1)


# -------------------------------------------------------------------- census

def analyze_tight(V, n, t):
    """Structural fields of a tight set (all exact)."""
    mx = max(V)
    res = sorted(set(v % (n + 1) for v in V))
    missing = [r for r in range(1, n + 1) if r not in res]
    sums = {a + b for i, a in enumerate(V) for b in V[i + 1:]}
    return {"V": V, "n": n, "t": t, "max": mx,
            "has_mult": any(v % (n + 1) == 0 for v in V),
            "residues": res, "missing_res": missing,
            "max_is_sum": mx in sums,
            "gaps": [x for x in range(1, mx + 1) if x not in V]}


def census(name, gen, n, label, collect_tight=True):
    bound = Fraction(1, n + 1)
    cnt = 0
    tight = []
    viol = []
    best, bestV = None, None
    t0 = time.time()
    last = 0
    for V in gen:
        k = kappa_exact(V)
        cnt += 1
        if best is None or k < best:
            best, bestV = k, V
        if k == bound:
            if collect_tight:
                _, t = kappa_exact(V, want_t=True)
                tight.append(analyze_tight(V, n, t))
            else:
                tight.append(V)
        elif k < bound:
            _, t = kappa_exact(V, want_t=True)
            viol.append((V, k, t))
        if time.time() - t0 - last > 60:
            last = time.time() - t0
            out("  [%s] running: %d sets, min so far %s, tight %d, viol %d "
                "(%.0f s)" % (name, cnt, str(best), len(tight), len(viol), last))
    out("-" * 78)
    out("CENSUS %s  (n=%d, %s, LRC bound 1/%d)" % (name, n, label, n + 1))
    out("  sets tested           : %d" % cnt)
    out("  min kappa found       : %s  at V=%s" % (str(best), str(bestV)))
    out("  violations k < 1/(n+1): %d %s"
        % (len(viol), "  *** COUNTEREXAMPLE *** " + str(viol[:5]) if viol else ""))
    out("  tight sets k = 1/(n+1): %d" % len(tight))
    noncons = [T for T in tight
               if (T["V"] if isinstance(T, dict) else T) != tuple(range(1, n + 1))]
    out("  tight non-{1..n}      : %d" % len(noncons))
    if noncons:
        for T in noncons[:12]:
            if isinstance(T, dict):
                out("    V=%-28s t=%-6s max=%-3d max_is_sum=%-5s "
                    "(n+1)|v in V: %s  residues mod %d: %s"
                    % (str(T["V"]), str(T["t"]), T["max"], T["max_is_sum"],
                       T["has_mult"], n + 1, T["residues"]))
            else:
                out("    " + str(T))
    out("  elapsed               : %.1f s" % (time.time() - t0))
    out("", )
    return {"n": n, "count": cnt, "min": best, "bestV": bestV,
            "tight": tight, "viol": viol}


def main():
    out("lonely_runner_census_v2.py -- deeper exact LRC census, %s" % time.ctime())
    out("python %s / numpy %s" % (sys.version.split()[0], np.__version__))
    out("engine imported unchanged from lonely_runner_census.py (Lemma L1).")
    out("")
    run_self_tests()

    summaries = []
    summaries.append(census("A6x", primitive_subsets(22, 6), 6,
                            "exhaustive primitive 6-subsets of [1,22]"))
    summaries.append(census("E8", primitive_subsets(22, 8), 8,
                            "exhaustive primitive 8-subsets of [1,22]"))
    summaries.append(census("F9", primitive_subsets(21, 9), 9,
                            "exhaustive primitive 9-subsets of [1,21]"))
    summaries.append(census("G9", random_primitive_sets(300, 9, 2000), 9,
                            "2000 random primitive 9-subsets of [1,300]"))
    summaries.append(census("H10", random_primitive_sets(150, 10, 800), 10,
                            "800 random primitive 10-subsets of [1,150]"))

    out("=" * 78)
    out("SUMMARY (all values exact rationals from this run)")
    out("=" * 78)
    for s in summaries:
        nc = len([T for T in s["tight"]
                  if (T["V"] if isinstance(T, dict) else T)
                  != tuple(range(1, s["n"] + 1))])
        out("  n=%2d  sets=%-7d min_kappa=%-8s violations=%d  tight=%d  "
            "tight_non_consecutive=%d"
            % (s["n"], s["count"], str(s["min"]), len(s["viol"]),
               len(s["tight"]), nc))
    out("")
    out("Legend: violations = sets with kappa < 1/(n+1) = LRC counterexamples;")
    out("any nonzero count is exact-verified by the Lemma L1 engine and would")
    out("disprove LRC. tight = sets with kappa = 1/(n+1) exactly.")
    out("")
    out("TIGHT-SET STRUCTURE TABLE (all tight non-consecutive sets found):")
    for s in summaries:
        for T in s["tight"]:
            if isinstance(T, dict) and T["V"] != tuple(range(1, s["n"] + 1)):
                out("  n=%d V=%-28s t=%-5s max=%-3d (n+1)|v:%-5s max=sum2:%-5s "
                    "missing_res=%s"
                    % (s["n"], str(T["V"]), str(T["t"]), T["max"],
                       T["has_mult"], T["max_is_sum"], T["missing_res"]))


if __name__ == "__main__":
    main()