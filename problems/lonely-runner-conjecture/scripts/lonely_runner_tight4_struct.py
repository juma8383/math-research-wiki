#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_tight4_struct.py -- deep structure of the known tight 4-sets
==========================================================================
For V = (1,2,3,4) and (1,3,4,7) (the only primitive tight 4-sets found in
[1,80], see lonely_runner_tight4.log):
  1. all maximizing times t* (does t=1/5 uniquely maximize?);
  2. full pair-window table: for each pair {p,q} and each r in V\{p,q}:
       nwin = number of windows of {p,q} (circle [0,5), bound 1/5),
       n1   = windows inside a single closed arc of B_r,
       cov  = all windows covered by B_r alone,
       and (for r = the two speeds not in the pair) whether every window
       is covered by B_r u B_s (the tightness requirement).
ASCII, flushed log.
"""
import sys, os, time, math
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_tight4_struct.log")
sys.path.insert(0, HERE)
from lonely_runner_tight4 import (windows_pair, in_single_arc, dist_res)  # noqa
from lonely_runner_census import candidate_times  # noqa

_FH = None


def out(s=""):
    print(s, flush=True)
    if _FH is not None:
        _FH.write(s + "\n")
        _FH.flush()


def all_max_times(V):
    """All t in the Lemma L1 candidate set attaining kappa = 1/5."""
    hits = []
    for (p, q) in candidate_times(V, include_diff=False):
        g = min(dist_res(p * v, q) for v in V)
        if 5 * g == q:
            hits.append(Fraction(p, q))
    return sorted(set(hits))


def covered_by(lo, hi, rs, mod=5):
    """Is (lo,hi) covered by the union of B_r, r in rs?  Exact check on a
    fine rational partition induced by all endpoints."""
    pts = set()
    for r in rs:
        for k in range(0, r + 1):
            for e in (mod * k - 1, mod * k + 1):
                x = Fraction(e, r)
                if lo < x < hi:
                    pts.add(x)
    pts = sorted(pts)
    cur = lo
    for x in pts:
        mid = (cur + x) / 2
        if not any((mid * r) % mod <= 1 or (mid * r) % mod >= mod - 1
                   for r in rs):
            return False
        cur = x
    mid = (cur + hi) / 2
    return any((mid * r) % mod <= 1 or (mid * r) % mod >= mod - 1 for r in rs)


def main():
    global _FH
    _FH = open(LOGF, "w", encoding="ascii", errors="replace")
    try:
        out("lonely_runner_tight4_struct.py -- %s" % time.ctime())
        out("")
        for V in [(1, 2, 3, 4), (1, 3, 4, 7)]:
            out("=" * 74)
            out("V = %s" % (V,))
            ts = all_max_times(V)
            out("  maximizing times (Lemma L1 candidates at kappa=1/5): %s"
                % ([str(t) for t in ts][:20]))
            out("  (count %d%s)" % (len(ts), "  -- t=1/5 IS the unique witness"
                                      if ts == [Fraction(1, 5)] else ""))
            out("")
            out("  pair {p,q} vs r: nwin  n_single_arc  all_in_single  "
                "all_cov_by_{r,s}(other speeds)")
            for i in range(4):
                for j in range(i + 1, 4):
                    p, q = V[i], V[j]
                    others = [V[m] for m in range(4) if m != i and m != j]
                    ws = windows_pair(p, q)
                    for r in others:
                        n1 = sum(1 for lo, hi in ws if in_single_arc(lo, hi, r))
                        s = [m for m in others if m != r]
                        covr = all(covered_by(lo, hi, [r, s[0]] if s else [r])
                                   for lo, hi in ws)
                        out("    {%d,%d} vs B_%-2d: nwin=%2d  single=%2d  "
                            "all_single=%-5s  cov_by_B_{%d,%d}=%s"
                            % (p, q, r, len(ws), n1, n1 == len(ws),
                               r, s[0] if s else 0, covr))
            out("")
            # n=3-window version of the T4-f one-pair condition (bound 1/4,
            # circle [0,4)): windows of {p,q} inside single arcs of the
            # n=3-style B_r.  Theorem T4-f: all single-arc => (p,q,r)=(1,2,3).
            out("  T4-f one-pair condition, n=3 windows (bound 1/4):")
            for i in range(4):
                for j in range(i + 1, 4):
                    p, q = V[i], V[j]
                    ws3 = windows_pair(p, q, mod=4)
                    for r in [V[m] for m in range(4) if V[m] > q]:
                        n1 = sum(1 for lo, hi in ws3
                                 if in_single_arc(lo, hi, r, mod=4))
                        out("    {%d,%d} vs B_%d: nwin=%d single=%d all=%s  "
                            "(T4-f forces all_single => (p,q,r)=(1,2,3))"
                            % (p, q, r, len(ws3), n1, n1 == len(ws3)))
            out("")
    finally:
        _FH.close()


if __name__ == "__main__":
    main()