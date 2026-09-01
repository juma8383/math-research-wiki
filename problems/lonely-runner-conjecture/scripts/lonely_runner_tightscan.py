#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_tightscan.py -- wide-box tight-set scan for small n
================================================================
CONTINUE block 2026-09-01 (Task 3). Companion to lonely_runner_census_v2.py:
exhaustive primitive n-subsets of [1,N] for n = 2..5 with WIDER boxes than
v1, enumerating ALL tight sets (kappa = 1/(n+1) exactly) to test the
tight-set structure conjectures filed in problem.md. Same exact engine,
imported from lonely_runner_census.py (Lemma L1). ASCII output, flushed.
"""

import sys
import os
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import kappa_exact, primitive_subsets  # noqa: E402


def out(s=""):
    print(s, flush=True)


def main():
    out("lonely_runner_tightscan.py -- wide-box tight-set scan, %s" % time.ctime())
    out("python %s" % sys.version.split()[0])
    out("engine imported unchanged from lonely_runner_census.py (Lemma L1);")
    out("difference-class omitted (redundant, self-test T4 in v1/v2: 0/800 mismatches).")
    out("")
    for (n, N) in [(2, 60), (3, 40), (4, 30), (5, 26)]:
        bound = Fraction(1, n + 1)
        t0 = time.time()
        tight = []
        viol = 0
        cnt = 0
        for V in primitive_subsets(N, n):
            k = kappa_exact(V, include_diff=False)
            cnt += 1
            if k == bound:
                tight.append(V)
            elif k < bound:
                viol += 1
                out("  *** COUNTEREXAMPLE *** V=%s kappa=%s" % (str(V), str(k)))
        nonc = [V for V in tight if V != tuple(range(1, n + 1))]
        withmult = [V for V in tight if any(v % (n + 1) == 0 for v in V)]
        nopm1 = [V for V in tight
                 if not (any(v % (n + 1) == 1 for v in V)
                         and any(v % (n + 1) == n for v in V))]
        noT3 = [V for V in tight
                if not all(any(v % M == 0 for v in V) for M in range(2, n + 1))]
        out("CENSUS W%d  (n=%d, exhaustive primitive %d-subsets of [1,%d], "
            "bound 1/%d)" % (n, n, n, N, n + 1))
        out("  sets tested           : %d" % cnt)
        out("  violations k < 1/(n+1): %d" % viol)
        out("  tight sets k = 1/(n+1): %d" % len(tight))
        out("  tight non-{1..n}      : %d%s"
            % (len(nonc), ("  " + ", ".join(str(V) for V in nonc[:15]))
               if nonc else ""))
        out("  tight with (n+1)|v   : %d" % len(withmult))
        out("  tight missing +/-1 res: %d" % len(nopm1))
        out("  tight failing T3      : %d" % len(noT3))
        out("  elapsed               : %.1f s" % (time.time() - t0))
        out("")
    out("Legend: '(n+1)|v' / 'missing +/-1 res' / 'failing T3' are the three")
    out("structural conditions of the Tight-set structure section in")
    out("problem.md. All zero here = every tight set found satisfies all three.")


if __name__ == "__main__":
    main()