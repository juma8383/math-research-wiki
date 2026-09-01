#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_consecutive.py -- (L) exact + good-x-set for (k,k+1)
=====================================================================
Part B: verify on all coprime a<b<=120:
    ml(a,b) = 2/b          if b-a >= 2
    ml(k,k+1) = (2k-1)/(k(k+1))   (consecutive)
Part C: for each consecutive reduced ratio (k,k+1), k=1..KMAX, compute the
GOOD-X-SET  G_k = { x = c/d (gcd(c,d)=1, c > d(k+1)) : every window w of
(k,k+1) fits in a single arc [4j-1,4j+1] after scaling by x }, as a union
of closed intervals with Fraction endpoints, then intersect with Q-reachable
points.  T4-f for this ratio <=> G_k has no rational point except the
known {3} at k=1.

Note x range: window lengths <= m_k = (2k-1)/(k(k+1)) force x <= 2/m_k
= 2k(k+1)/(2k-1) ~ k+1.5, so G_k lives in the SHORT interval
(k+1, 2k(k+1)/(2k-1)] -- the position problem is a bounded interval per k.

ASCII, flushed, log file.
"""
import sys, os, time, math
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_t4_consecutive.log")
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


def iv_union(ivs):
    """Merge closed intervals [(a,b),...] sorted."""
    ivs = sorted(ivs)
    res = []
    for lo, hi in ivs:
        if hi < lo:
            continue
        if res and lo <= res[-1][1]:
            if hi > res[-1][1]:
                res[-1] = (res[-1][0], hi)
        else:
            res.append((lo, hi))
    return res


def iv_inter(A, B):
    """Intersection of two unions of closed intervals."""
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            res.append((lo, hi))
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return iv_union(res)


def main():
    out("lonely_runner_t4_consecutive.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])
    t0 = time.time()

    # ---------------- Part B: exact ml formulas
    BND = 120
    bad = []
    n = 0
    for a in range(1, BND + 1):
        for b in range(a + 1, BND + 1):
            if math.gcd(a, b) != 1:
                continue
            n += 1
            ws = windows_pair(a, b)
            ml = max((w[1] - w[0] for w in ws), default=Fraction(0))
            if b - a >= 2:
                if ml != Fraction(2, b):
                    bad.append((a, b, ml, "want 2/b"))
            else:
                k = a
                if ml != Fraction(2 * k - 1, k * (k + 1)):
                    bad.append((a, b, ml, "want (2k-1)/(k(k+1))"))
    out("Part B: coprime pairs a<b<=%d: %d checked, violations of exact"
        " formulas: %d" % (BND, n, len(bad)))
    out("  violations: %s" % bad[:20])

    # ---------------- Part C: good-x-set for consecutive (k,k+1)
    K = 40
    out("Part C: G_k for consecutive ratios, k=1..%d" % K)
    for k in range(1, K + 1):
        W = windows_pair(k, k + 1)
        mx = max(w[1] - w[0] for w in W)
        xmax = Fraction(2, 1) / mx
        # universe: x in (k+1, xmax]; use closed [k+1, xmax] then trim
        G = [(Fraction(k + 1), xmax)]
        for (lo, hi) in W:
            Xw = []
            j = 0
            while True:
                a_lo = Fraction(4 * j - 1, 1) / lo
                if a_lo > xmax:
                    break
                a_hi = Fraction(4 * j + 1, 1) / hi
                Xw.append((a_lo, a_hi))
                j += 1
            G = iv_inter(G, iv_union(Xw))
        out("  k=%2d: #windows=%2d maxlen=%s x<=%s  G_k=%s"
            % (k, len(W), mx, xmax,
               [(str(a), str(b)) for a, b in G]))
    out("elapsed %.1f s" % (time.time() - t0))
    flush_log()


if __name__ == "__main__":
    try:
        main()
    finally:
        flush_log()