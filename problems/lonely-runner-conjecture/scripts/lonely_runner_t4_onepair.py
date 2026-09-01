#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_onepair.py -- FINAL verification of the one-pair theorem
=========================================================================
THEOREM (one-pair window kill; proved on paper in problem.md, verified
here exactly): let a<b<c primitive (gcd(a,b,c)=1) and suppose every
window of {a,b} lies in a single closed arc of B_c.  Write d=gcd(a,b),
(a',b')=(a/d,b/d).  Then (a',b')=(1,2) and c/d=3, i.e. (a,b,c)=(1,2,3).

Proof ingredients verified numerically here (all exact, Fractions):
  W1  for all coprime k<=200: w0=(1/k,3/(k+1)) is EXACTLY a window of
      {k,k+1} (it appears verbatim in windows_pair(k,k+1));
  W2  for all coprime a<b<=200 with b-a>=2: ml(a,b) = 2/b exactly
      (the length kill: any c>b fails on a window of length 2/b > 2/c);
  W3  exhaustive [1,200]: the ONLY primitive triple (a,b,c) with the
      {a,b}-window condition is (1,2,3)  [re-check of pairforce V2];
  W4  the kill inequality: for (a',b')=(k,k+1), any c>d(k+1) forces
      3k <= c/d <= 2k(k+1)/(2k-1), so k=1; then window 2 forces c/d=3.
      Verified: for k=1, d=1..200, gcd(c,d)=1, c>d(k+1), c<=200: the
      condition holds iff (d,c)=(1,3).

ASCII, flushed, log file.
"""
import sys, os, time, math
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_t4_onepair.log")
OUT = []


def out(s=""):
    print(s, flush=True)
    OUT.append(s)


def flush_log():
    with open(LOGF, "a", encoding="ascii", errors="replace") as f:
        f.write("\n".join(OUT) + "\n")


def windows_pair(p, q):
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
    return wins


def all_covered(ws, r):
    """Every window in a single closed arc of B_r? (corrected predicate)"""
    for (lo, hi) in ws:
        L, H = lo * r, hi * r
        if math.ceil((H - 1) / 4) > math.floor((L + 1) / 4):
            return False
    return True


def main():
    out("lonely_runner_t4_onepair.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])
    t0 = time.time()

    # W1: w0 exact window of (k,k+1)
    bad1 = []
    for k in range(1, 201):
        W = windows_pair(k, k + 1)
        if (Fraction(1, k), Fraction(3, k + 1)) not in W:
            bad1.append(k)
    out("W1: w0=(1/k,3/(k+1)) exact window of {k,k+1} for k=1..200:"
        " violations %d %s" % (len(bad1), bad1[:10]))

    # W2: ml = 2/b for coprime b-a>=2
    bad2 = []
    n2 = 0
    for a in range(1, 201):
        for b in range(a + 2, 201):
            if math.gcd(a, b) != 1:
                continue
            n2 += 1
            ws = windows_pair(a, b)
            ml = max(w[1] - w[0] for w in ws)
            if ml != Fraction(2, b):
                bad2.append((a, b, ml))
    out("W2: coprime a<b<=200, b-a>=2 (%d pairs): ml=2/b violations %d %s"
        % (n2, len(bad2), bad2[:10]))

    # W3: exhaustive triple check [1,200]
    hits = []
    N = 200
    # (efficient pass: pair windows once, c bounded by length)
    for (a, b) in combinations_pairs(N):
        ws = windows_pair(a, b)
        ml = max((w[1] - w[0] for w in ws), default=Fraction(0))
        c_hi = min(N, math.floor(Fraction(2, 1) / ml) if ml > 0 else 0)
        for c in range(b + 1, c_hi + 1):
            if math.gcd(math.gcd(a, b), c) != 1:
                continue
            if all_covered(ws, c):
                hits.append((a, b, c))
    out("W3: primitive triples in [1,200] with {a,b}-window condition: %s"
        % hits)

    # W4: consecutive kill at k=1 over scales
    surv = []
    for d in range(1, 101):
        for c in range(d * 2 + 1, 201):
            if math.gcd(c, d) != 1:
                continue
            ws = [((Fraction(1, 1)), Fraction(3, 2)),
                  (Fraction(5, 2), Fraction(3, 1))]  # windows of {1,2}, /d
            wsd = [(lo / d, hi / d) for lo, hi in ws]
            if all_covered(wsd, c):
                surv.append((d, c))
    out("W4: pairs {d,2d} passing window condition (c>2d, gcd(c,d)=1,"
        " c<=200): %s" % surv)
    out("elapsed %.1f s" % (time.time() - t0))
    flush_log()


def combinations_pairs(N):
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            yield (a, b)


if __name__ == "__main__":
    try:
        main()
    finally:
        flush_log()