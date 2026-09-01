#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_lengthlemma.py -- goal (L): the length lemma, exact form
=========================================================================
Setup (T-units = 4x real t; circle [0,4)).  For a pair (a,b) the WINDOWS
are the components of G_a n G_b, G_p = {T : pT mod 4 in (1,3)} (open gaps
between the closed arcs [(4k-1)/p,(4k+1)/p] of B_p).  windows_pair()
computes them exactly (Fractions).

Length kill for third speed c:  window (lo,hi) fits in one B_c arc
    [(4k-1)/c,(4k+1)/c]  <=>  4k-1 <= c*lo and c*hi <= 4k+1,
so a NECESSARY condition is hi-lo <= 2/c.  Hence if max window length
ml(a,b) >= 2/(b+1) then NO c > b works (length kill).

Here (Part A): exact ml for ALL coprime pairs a<b<=BND; determine the
exact exception set E = {coprime (a,b): ml < 2/(b+1)}; test the
hypothesis E = {(k,k+1)} (consecutive).  Also record ml >= 2/b.

ASCII, flushed, log file.
"""
import sys, os, time, math
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_t4_lengthlemma.log")
OUT = []


def out(s=""):
    print(s, flush=True)
    OUT.append(s)


def flush_log():
    with open(LOGF, "a", encoding="ascii", errors="replace") as f:
        f.write("\n".join(OUT) + "\n")


def windows_pair(p, q):
    """Components of G_p n G_q on circle [0,4), exact (Fraction endpoints)."""
    pts = set()
    for v in (p, q):
        for k in range(0, v + 1):
            pts.add(Fraction(4 * k - 1, v))
            pts.add(Fraction(4 * k + 1, v))
    pts = sorted(x for x in pts if 0 <= x <= 4)
    wins = []
    for i in range(len(pts) - 1):
        lo, hi = pts[i], pts[i + 1]
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        if 1 < (mid * p) % 4 < 3 and 1 < (mid * q) % 4 < 3:
            if wins and wins[-1][1] == lo:
                wins[-1] = (wins[-1][0], hi)
            else:
                wins.append((lo, hi))
    # circle wrap: does the pair touch T=0?  T=0 is in B (dist 0), so no.
    return wins


def maxwindow(p, q):
    ws = windows_pair(p, q)
    return max((w[1] - w[0] for w in ws), default=Fraction(0))


def main():
    out("lonely_runner_t4_lengthlemma.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])
    BND = 60
    t0 = time.time()
    exc = []          # coprime exceptions to ml >= 2/(b+1)
    exc_strict = []   # coprime exceptions to ml >= 2/b (stronger)
    nchecked = 0
    mrec = {}
    for a in range(1, BND + 1):
        for b in range(a + 1, BND + 1):
            if math.gcd(a, b) != 1:
                continue
            nchecked += 1
            ml = maxwindow(a, b)
            mrec[(a, b)] = ml
            if ml < Fraction(2, b + 1):
                exc.append((a, b, ml))
            if ml < Fraction(2, b):
                exc_strict.append((a, b, ml))
    out("Part A: coprime pairs a<b<=%d checked: %d" % (BND, nchecked))
    out("  exceptions to ml >= 2/(b+1): %d" % len(exc))
    out("  detail: %s" % exc)
    out("  exceptions to ml >= 2/b (stronger): %d" % len(exc_strict))
    out("  detail: %s" % exc_strict[:40])
    # ml for consecutive pairs (k,k+1)
    out("  ml(k,k+1): %s"
        % [(k, mrec[(k, k + 1)]) for k in range(1, BND)
           if (k, k + 1) in mrec][:30])
    out("elapsed %.1f s" % (time.time() - t0))
    flush_log()


if __name__ == "__main__":
    try:
        main()
    finally:
        flush_log()