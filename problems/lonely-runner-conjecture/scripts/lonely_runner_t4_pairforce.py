#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_pairforce.py -- T4-f: ONE pair condition suffices?
===================================================================
CLAIM T4-f (census target): for primitive a<b<c, if every window of the
pair {a,b} lies in a single closed arc of B_c (c = third, LARGEST speed),
then (a,b,c) = (1,2,3).

If true, T4 follows at once from Lemma T4-a (tight => all three pairs'
windows contained; in particular the {a,b} one).  This REPLACES the filed
stall framing: the "{2,4,5}-type candidates that die only on the other
pairs" were an artifact of a buggy containment predicate (k-bounds
swapped; see problem.md correction).  With the corrected predicate the
{a,b}-condition alone is drastically stronger.

Corrected containment: window (lo,hi) in arc k of B_c  <=>
    4k-1 <= c*lo  and  c*hi <= 4k+1
    <=>  ceil((c*hi-1)/4) <= k <= floor((c*lo+1)/4).

Checks here (all exact, s-units, circle [0,4)):
  V1  self-test: {1,2,3} passes; {1,2,4},{1,3,4},{2,3,4},{2,4,5} fail.
  V2  exhaustive [1,N]: every primitive triple with the {a,b}-window
      condition is listed.  Expect exactly (1,2,3).
  V3  pair-level census: for each coprime pair a<b<=N, the set of
      c in (b, N] with gcd(a,b,c)=1 passing the condition; report pairs
      admitting any c (expect only {1,2} -> c in {3,4}) and the max
      window length pattern (for the write-up).

ASCII, flushed, log file.
"""
import sys, os, time, math
from fractions import Fraction
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_t4_pairforce.log")
OUT = []


def out(s=""):
    print(s, flush=True)
    OUT.append(s)


def flush_log():
    with open(LOGF, "w", encoding="ascii", errors="replace") as f:
        f.write("\n".join(OUT) + "\n")


def windows_pair(p, q):
    """Components of G_p n G_q on [0,4), exact (Fraction endpoints)."""
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
    """Every window in a single B_r arc? (corrected predicate)"""
    for (lo, hi) in ws:
        L, H = lo * r, hi * r
        if math.ceil((H - 1) / 4) > math.floor((L + 1) / 4):
            return False
    return True


def main():
    out("lonely_runner_t4_pairforce.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])

    # ---------------- V1 self-tests
    w12 = windows_pair(1, 2)
    ok = (w12 == [(Fraction(1, 1), Fraction(3, 2)),
                  (Fraction(5, 2), Fraction(3, 1))])
    ok = ok and all_covered(w12, 3) and not all_covered(w12, 4)
    ok = ok and all_covered(windows_pair(1, 3), 2)
    ok = ok and all_covered(windows_pair(2, 3), 1)
    ok = ok and not all_covered(windows_pair(1, 3), 4)   # {1,3,4} fails
    ok = ok and not all_covered(windows_pair(2, 4), 5)   # {2,4,5} fails
    ok = ok and not all_covered(windows_pair(2, 3), 4)   # {2,3,4} fails
    out("V1 self-tests: %s" % ("PASS" if ok else "FAIL"))
    if not ok:
        flush_log()
        return

    # ---------------- V2/V3 exhaustive
    N = 200
    t0 = time.time()
    hits = []
    pair_hits = {}
    maxlen = {}
    for (a, b) in combinations(range(1, N + 1), 2):
        ws = windows_pair(a, b)
        ml = max((w[1] - w[0] for w in ws), default=Fraction(0))
        maxlen[(a, b)] = ml
        # c must satisfy c > b and (length cond) c <= 2/max_window_len
        c_hi = min(N, math.floor(Fraction(2, 1) / ml) if ml > 0 else 0)
        for c in range(b + 1, c_hi + 1):
            if math.gcd(math.gcd(a, b), c) != 1:
                continue
            if all_covered(ws, c):
                hits.append((a, b, c))
                pair_hits.setdefault((a, b), []).append(c)
    out("V2 exhaustive [1,%d]: primitive triples with {a,b}-window cond: %d"
        % (N, len(hits)))
    out("    hits: %s" % hits[:50])
    out("V3 pairs (a,b) admitting any c>b: %d; detail %s"
        % (len(pair_hits), dict(list(pair_hits.items())[:20])))
    out("V3 max window lengths: (1,2)=%s (1,3)=%s (2,3)=%s (1,4)=%s (3,4)=%s"
        % (maxlen[(1, 2)], maxlen[(1, 3)], maxlen[(2, 3)],
           maxlen[(1, 4)], maxlen[(3, 4)]))
    # distribution of max window length: is it always >= 2/(b+1)?
    ge = sum(1 for (a, b) in maxlen if maxlen[(a, b)] >= Fraction(2, b + 1))
    out("V3 pairs with maxlen >= 2/(b+1) (=> no c>b by length alone): "
        "%d/%d" % (ge, len(maxlen)))
    ex = [(a, b) for (a, b) in maxlen if maxlen[(a, b)] < Fraction(2, b + 1)]
    out("V3 exceptions (maxlen < 2/(b+1)): %d; first 30: %s"
        % (len(ex), ex[:30]))
    out("elapsed %.1f s" % (time.time() - t0))
    flush_log()


if __name__ == "__main__":
    try:
        main()
    finally:
        flush_log()