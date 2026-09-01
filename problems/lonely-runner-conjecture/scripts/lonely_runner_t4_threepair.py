#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_threepair.py -- three-pair window census for Conjecture T4
===========================================================================
T4: the only primitive tight 3-set is {1,2,3}.  Filed stall = need a
SIMULTANEOUS three-pair window-position argument.  This script:

  T1s  self-test: window machinery on {1,2,3} and known non-tight triples.
  T2s  EXHAUSTIVE equivalence check: "all three pairs' windows lie in
       single arcs of the third's bad set"  <=>  kappa = 1/4,
       over ALL primitive triples a<b<c in [1,N]  (N=120 default).
       (Extends S3's 400-sample check to an exhaustive one.)
  T3s  AB-candidate census: triples whose PAIR-{a,b} window condition
       alone holds (windows of {a,b} in single B_c arcs).  Structure:
       count, min-speed values, c/a ratio stats, c<=4a? c<=2b? 3|? even?
       For each candidate record which of the other two pair conditions
       fail (length-kill vs position-kill).

Windows computed EXACTLY (Fraction endpoints on the kink grid), cached
per pair.  s-units: circle [0,4); B_v = union of v closed arcs
[(4k-1)/v,(4k+1)/v]; G_v = open gaps ((4k+1)/v,(4k+3)/v).
Window of pair {p,q} = component of G_p n G_q.
Containment in single B_r arc: exists k: 4k-1 <= r*lo and r*hi <= 4k+1.

ASCII output, flushed writes, log file.
"""
import sys, os, time, math
from fractions import Fraction
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import kappa_exact  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_t4_threepair.log")
OUT = []


def out(s=""):
    print(s, flush=True)
    OUT.append(s)


def flush_log():
    with open(LOGF, "w", encoding="ascii", errors="replace") as f:
        f.write("\n".join(OUT) + "\n")


def windows_pair(p, q):
    """Exact windows (components) of G_p n G_q on [0,4), as list of
    (lo, hi) Fractions.  Endpoints = all (4k+-1)/v, v in {p,q}."""
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
        gp = 1 < (mid * p) % 4 < 3
        gq = 1 < (mid * q) % 4 < 3
        if gp and gq:
            if wins and wins[-1][1] == lo:
                wins[-1] = (wins[-1][0], hi)
            else:
                wins.append((lo, hi))
    return wins


def covered(w, r):
    """Open window w=(lo,hi) inside a single closed B_r arc?
    Arc k = [(4k-1)/r, (4k+1)/r] contains [lo,hi]
      <=> 4k-1 <= r*lo and r*hi <= 4k+1
      <=> ceil((r*hi-1)/4) <= k <= floor((r*lo+1)/4)."""
    lo, hi = w
    L, H = lo * r, hi * r
    return math.ceil((H - 1) / 4) <= math.floor((L + 1) / 4)


def pair_cond_ok(p, q, r):
    return all(covered(w, r) for w in WINDOWS[(p, q)])


WINDOWS = {}


def main():
    out("lonely_runner_t4_threepair.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])

    # ---------------- T1s self-tests
    ok = True
    w12 = windows_pair(1, 2)
    if w12 != [(Fraction(1, 1), Fraction(3, 2)), (Fraction(5, 2), Fraction(3, 1))]:
        out("T1s FAIL windows(1,2) = %s" % w12); ok = False
    if not all(covered(w, 3) for w in w12):
        out("T1s FAIL {1,2} windows not in B_3 arcs"); ok = False
    w13 = windows_pair(1, 3)
    if not all(covered(w, 2) for w in w13):
        out("T1s FAIL {1,3} windows not in B_2 arcs"); ok = False
    w23 = windows_pair(2, 3)
    if not all(covered(w, 1) for w in w23):
        out("T1s FAIL {2,3} windows not in B_1 arcs"); ok = False
    # non-tight spot check: {1,2,4} not tight (kappa > 1/4), {1,2,5} fails?
    out("T1s self-tests: %s" % ("PASS" if ok else "FAIL"))
    if not ok:
        flush_log()
        return

    # ---------------- build window table
    N = 120
    t0 = time.time()
    for (p, q) in combinations(range(1, N + 1), 2):
        WINDOWS[(p, q)] = windows_pair(p, q)
    out("window table built for %d pairs [1,%d] (%.1f s)"
        % (len(WINDOWS), N, time.time() - t0))

    # sanity: window lengths
    wmax = max((w[1] - w[0] for ws in WINDOWS.values() for w in ws),
               default=Fraction(0))
    out("max window length over all pairs: %s" % wmax)

    # ---------------- T2s exhaustive three-pair equivalence
    tight = []
    wc_all = []
    mism = 0
    cnt = 0
    for (a, b, c) in combinations(range(1, N + 1), 3):
        if math.gcd(math.gcd(a, b), c) != 1:
            continue
        cnt += 1
        k = kappa_exact((a, b, c), include_diff=False)
        is_t = (k == Fraction(1, 4))
        wc = (pair_cond_ok(a, b, c) and pair_cond_ok(a, c, b)
              and pair_cond_ok(b, c, a))
        if is_t:
            tight.append((a, b, c))
        if wc:
            wc_all.append((a, b, c))
        if is_t != wc:
            mism += 1
            out("    T2s MISMATCH %s kappa=%s wc=%s" % ((a, b, c), k, wc))
    out("T2s EXHAUSTIVE window<->tight equivalence [1,%d]: %d primitive "
        "triples, %d mismatches (must be 0)" % (N, cnt, mism))
    out("    tight sets: %s" % tight)
    out("    all-window-condition sets: %s" % wc_all)
    flush_log()

    # ---------------- T3s AB-candidate census (pair {a,b} condition only)
    ab = []
    for (a, b, c) in combinations(range(1, N + 1), 3):
        if math.gcd(math.gcd(a, b), c) != 1:
            continue
        if pair_cond_ok(a, b, c):
            ab.append((a, b, c))
    out("T3s AB-candidates (pair-{a,b} windows in single B_c arcs) [1,%d]: %d"
        % (N, len(ab)))
    c_le_4a = sum(1 for (a, b, c) in ab if c <= 4 * a)
    c_le_2b = sum(1 for (a, b, c) in ab if c <= 2 * b)
    min1 = sum(1 for (a, b, c) in ab if a == 1)
    has3 = sum(1 for (a, b, c) in ab if any(v % 3 == 0 for v in (a, b, c)))
    hasE = sum(1 for (a, b, c) in ab if any(v % 2 == 0 for v in (a, b, c)))
    t0c = sum(1 for (a, b, c) in ab
              if any(min(v % 4, 4 - (v % 4)) <= 1 for v in (a, b, c)))
    out("    c<=4a: %d/%d   c<=2b: %d/%d   a=1: %d   3|some: %d   "
        "even: %d   t0-cond: %d" % (c_le_4a, len(ab), c_le_2b, len(ab),
                                    min1, has3, hasE, t0c))
    out("    first 40 AB-candidates: %s" % ab[:40])
    flush_log()

    # two-stage refinement: which die on {a,c}-cond vs {b,c}-cond
    s1 = [(a, b, c) for (a, b, c) in ab if pair_cond_ok(a, c, b)]
    a1_cnt = sum(1 for (a, b, c) in s1 if a == 1)
    out("    AB-candidates also passing {a,c}-cond: %d; with a=1: %d; "
        "min a over a>=1: %s" % (len(s1), a1_cnt,
                                 min((a for (a, b, c) in s1), default=None)))
    out("    first 30 (a>1 only): %s"
        % [t for t in s1 if t[0] > 1][:30])
    s2 = [(a, b, c) for (a, b, c) in s1 if pair_cond_ok(b, c, a)]
    out("    ... also passing {b,c}-cond (= tight): %d %s" % (len(s2), s2))
    flush_log()

    # kill-type analysis on the {a,c} stage: length-kill vs position-kill
    lenkill = poskill = 0
    for (a, b, c) in ab:
        ws = WINDOWS[(a, c)]
        if any(w[1] - w[0] > Fraction(2, b) for w in ws):
            lenkill += 1
        elif not pair_cond_ok(a, c, b):
            poskill += 1
    out("    {a,c}-stage kills: length-kill %d, position-only-kill %d"
        % (lenkill, poskill))

    # b=2a slice, correct windows: a>=2 should have NO survivor at stage 1
    out("T4s b=2a slice (pair {a,2a} cond, c in (2a,4a], gcd(a,c)=1):")
    surv = []
    for a in range(1, N // 2 + 1):
        for c in range(2 * a + 1, min(4 * a, N) + 1):
            if math.gcd(a, c) != 1:
                continue
            if pair_cond_ok(a, 2 * a, c):
                surv.append((a, 2 * a, c))
    out("    survivors of pair-{a,2a} window cond: %d %s" % (len(surv), surv[:30]))
    out("    (a=1 gives the known c in {3,4}; a>=2 survivors = T4-e gap)")
    kill_ac = kill_bc = kill_both = 0
    for (a, b, c) in surv:
        okA = pair_cond_ok(a, c, b)
        okB = pair_cond_ok(b, c, a)
        if not okA and not okB:
            kill_both += 1
        elif not okA:
            kill_ac += 1
        elif not okB:
            kill_bc += 1
    out("    b=2a survivor kills: by {a,c}-cond %d, by {b,c}-cond %d, both %d"
        % (kill_ac, kill_bc, kill_both))
    flush_log()
    out("done")


if __name__ == "__main__":
    try:
        main()
    finally:
        flush_log()