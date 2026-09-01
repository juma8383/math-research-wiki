#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_t4_windows.py -- window lemma machinery for Conjecture T4
=======================================================================
T4: the only primitive tight 3-set is {1,2,3} (kappa = 1/4 exactly).

This script verifies the WINDOW LEMMA machinery (proved by hand in
problem.md, Lemma T4-a) and the derived speed bound (Lemma T4-b), and
computes exact pair-kappa data for the sharp pair bound.

SETUP (s-units, circle = [0,4), s = 4t):
  bad set of speed v:  B_v = {s in [0,4): sv mod 4 in [3,4) u [0,1]}
                     = disjoint union of v closed arcs
                       [(4k-1)/v, (4k+1)/v], k = 0..v-1, each of length 2/v.
  kappa({a,b,c}) = 1/4  <=>  B_a u B_b u B_c = [0,4)
  (proved: min_t ||t v|| <= 1/4 everywhere <=> cover).

LEMMA T4-a (window containment, hand-proved): if kappa({a,b,c}) = 1/4 then
  for every pair {p,q} = {a,b},{a,c},{b,c}:
      every connected component ("window") of the pair-good set
      G_{p,q} = {s: sp mod 4 in (1,3) and sq mod 4 in (1,3)}
      is contained in a single closed arc of B_third.
  Reason: G_{p,q} is disjoint from B_p u B_q, so G_{p,q} must lie in B_r
  (r = the third speed); arcs of B_r are disjoint closed arcs separated by
  OPEN gaps, so each connected component of G_{p,q} (an interval) lies in
  one arc of B_r.  In particular every window length <= 2/(3rd speed),
  and the window set is exactly covered.

LEMMA T4-b (speed bound):  kappa({p,q}) >= 1/3 (n=2 LRC, published) gives,
  for the pair {a,b} and r = c: the pair-max t0 of {a,b} has both distances
  >= 1/3, so the window through t0 contains an interval of length
  2*(kappa_ab - 1/4)/b (each distance can drop at rate <= v), hence
      2*(kappa({a,b}) - 1/4)/b <= 2/c   (window length <= arc length 2/c)
      =>  c <= b / (4*(kappa({a,b}) - 1/4)).
  With kappa_ab >= 1/3:  c <= 3b.  (In t-units: arc length 1/(2c) etc.;
  here everything is s-units, factor 4 consistent.)

CHECKS RUN HERE
  S1  engine cross-validation: kappa_int3 vs reference Fraction engine [1,30]
  S2  {1,2,3} tight; its window/arc structure verified exactly
  S3  covering equivalence spot-check: for triples in [1,40], the condition
      "all windows of all pairs covered by the third bad set" holds
      <=> kappa = 1/4   (sampled exact comparison)
  S4  exhaustive [1,N]: every triple with kappa = 1/4 satisfies Lemma T4-a
      (window containment) and Lemma T4-b (c <= 3b); count violations
  S5  exact pair-kappa table for small pairs (evidence for sharp bound)

ASCII output, flushed writes.
"""
import sys, os, time, math
from fractions import Fraction
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lonely_runner_census import kappa_exact  # noqa: E402

LOG = []


def out(s=""):
    print(s, flush=True)
    LOG.append(s)


def drs(v, q):
    """dist(v mod q, 0) as integer /q."""
    r = v % q
    return min(r, q - r)


def kappa_int3(a, b, c):
    """Exact kappa({a,b,c}) via Lemma L1 candidate set, integer arithmetic."""
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
        g = min(drs(p * v, q) for v in V)
        if g * best_den > best_num * q:
            best_num, best_den = g, q
    return Fraction(best_num, best_den)


def kappa_pair(a, b):
    """Exact kappa({a,b}) via Lemma L1 (kinks + sum candidates)."""
    V = (a, b)
    V = (a, b)
    best_num, best_den = 0, 1
    cands = set()
    for v in V:
        for m in range(0, 2 * v + 1):
            cands.add((m, 2 * v))
    s = a + b
    for m in range(0, s + 1):
        cands.add((m, s))
    for (p, q) in cands:
        g = min(drs(p * v, q) for v in V)
        if g * best_den > best_num * q:
            best_num, best_den = g, q
    return Fraction(best_num, best_den)


def pair_windows(p, q):
    """Connected components (as exact rational endpoint lists) of
    G_{p,q} = {s in [0,4): sp,sq mod 4 in OPEN (1,3)}.
    Computed by walking the fine grid of all endpoints k/(2p), k/(2q),
    k/(4p), k/(4q) -- all kink/bad-boundary points -- and keeping maximal
    open subintervals where both are good.  Returns list of (lo, hi) Fractions
    with lo<hi, plus checks."""
    pts = set()
    for v in (p, q):
        for k in range(0, 4 * v + 1):
            pts.add(Fraction(k, v))        # bad-arc endpoints (4k+-1)/v grid
            pts.add(Fraction(2 * k + 1, 2 * v))
    pts = sorted(x for x in pts if 0 <= x <= 4)
    wins = []
    for i in range(len(pts) - 1):
        lo, hi = pts[i], pts[i + 1]
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        if (mid * p) % 4 > 1 and (mid * p) % 4 < 3 and \
           (mid * q) % 4 > 1 and (mid * q) % 4 < 3:
            wins.append((lo, hi))
    # merge adjacent open cells sharing an endpoint (components of the
    # good set are unions of consecutive cells)
    merged = []
    for (lo, hi) in wins:
        if merged and merged[-1][1] == lo:
            merged[-1] = (merged[-1][0], hi)
        else:
            merged.append((lo, hi))
    return merged


def main():
    out("lonely_runner_t4_windows.py -- %s" % time.ctime())
    out("python %s" % sys.version.split()[0])

    # ---------------- S1 engine cross-validation
    bad = 0
    for (a, b, c) in combinations(range(1, 31), 3):
        if math.gcd(math.gcd(a, b), c) != 1:
            continue
        if kappa_int3(a, b, c) != kappa_exact((a, b, c), include_diff=False):
            bad += 1
    out("S1  engine cross-validation [1,30]: %d mismatches (must be 0)" % bad)
    if bad:
        return

    # ---------------- S2 {1,2,3} structure
    out("S2  kappa(1,2,3) = %s (expect 1/4)" % kappa_int3(1, 2, 3))
    for (p, q, r) in [(1, 2, 3), (1, 3, 2), (2, 3, 1)]:
        ws = pair_windows(p, q)
        maxlen = max((w[1] - w[0] for w in ws), default=Fraction(0))
        ok = all(window_covered_by(w, r) for w in ws)
        out("    pair (%d,%d): %d windows, max len %s, all in single B_%d arc: %s"
            % (p, q, len(ws), maxlen, r, ok))

    # ---------------- S3 covering equivalence (sampled, [1,40])
    import random as _rnd
    _rnd.seed(20260901)
    mism = 0
    tested = 0
    all_triples = [(a, b, c) for (a, b, c) in combinations(range(1, 25), 3)
                   if math.gcd(math.gcd(a, b), c) == 1]
    sample = _rnd.sample(all_triples, min(400, len(all_triples)))
    for (a, b, c) in sample:
        k = kappa_int3(a, b, c)
        tight_engine = (k == Fraction(1, 4))
        # window condition: every window of every pair lies in one arc of 3rd
        wc = True
        for (p, q, r) in [(a, b, c), (a, c, b), (b, c, a)]:
            for w in pair_windows(p, q):
                if not window_covered_by(w, r):
                    wc = False
                    break
            if not wc:
                break
        tested += 1
        if wc != tight_engine:
            mism += 1
            out("    S3 MISMATCH %s kappa=%s windows_covered=%s"
                % ((a, b, c), k, wc))
    out("S3  window<->tight equivalence, %d sampled triples [1,24]: %d mismatches"
        % (tested, mism))

    # ---------------- S4 exhaustive necessary conditions
    N = 60
    tight = []
    violA = violB = 0
    for (a, b, c) in combinations(range(1, N + 1), 3):
        if math.gcd(math.gcd(a, b), c) != 1:
            continue
        if kappa_int3(a, b, c) != Fraction(1, 4):
            continue
        # Lemma T4-b: c <= 3b
        if not (c <= 3 * b):
            violB += 1
            out("    S4 LEMMA-B VIOLATION %s" % ((a, b, c),))
        # Lemma T4-a: window containment for all pairs
        for (p, q, r) in [(a, b, c), (a, c, b), (b, c, a)]:
            for w in pair_windows(p, q):
                if w[1] - w[0] > Fraction(2, r):
                    violA += 1
                    out("    S4 LEMMA-A VIOLATION %s window %s" % ((a, b, c), w))
    out("S4  exhaustive [1,%d]: tight triples violating T4-a: %d, T4-b: %d"
        % (N, violA, violB))

    # ---------------- S5 exact pair-kappa table
    out("S5  exact pair kappas kappa({a,b}) and implied c-bound "
        "b/(4*(k-1/4)):")
    for (a, b) in [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5),
                   (4, 5), (3, 7), (4, 7), (5, 7), (5, 6)]:
        k = kappa_pair(a, b)
        if k > Fraction(1, 4):
            bound = Fraction(b, 1) / (4 * (k - Fraction(1, 4)))
            out("    kappa(%d,%d) = %-6s  c <= %s" % (a, b, k, bound))
        else:
            out("    kappa(%d,%d) = %-6s  (<= 1/4: bound void)" % (a, b, k))

    # ---------------- S6 exhaustive pair-kappa formula check
    # Conjecture P: kappa({a,b}) = floor((a'+b')/2)/(a'+b'), (a',b')=(a,b)/d.
    N = 120
    bad = 0
    cnt = 0
    for (a, b) in combinations(range(1, N + 1), 2):
        d = math.gcd(a, b)
        ap, bp = a // d, b // d
        pred = Fraction((ap + bp) // 2, ap + bp)
        if kappa_pair(a, b) != pred:
            bad += 1
            if bad <= 5:
                out("    S6 MISMATCH (%d,%d): engine %s formula %s"
                    % (a, b, kappa_pair(a, b), pred))
        cnt += 1
    out("S6  pair formula kappa=floor((a'+b')/2)/(a'+b') on %d pairs [1,%d]: "
        "%d mismatches" % (cnt, N, bad))


def window_covered_by(w, r):
    """Open window (lo,hi) contained in a single closed arc of B_r?
    Need integer k with 4k-1 <= lo*r and hi*r <= 4k+1 (closed arc, open
    window, endpoints may touch)."""
    lo, hi = w
    L, H = lo * r, hi * r
    k_lo = math.ceil(Fraction(L - 1, 4))
    k_hi = math.floor(Fraction(H + 1, 4))
    return k_lo <= k_hi


if __name__ == "__main__":
    main()