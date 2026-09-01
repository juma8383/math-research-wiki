#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lonely_runner_tight4.py -- tight 4-set classification, stage 1
==============================================================
CONTINUE block 2026-09-01 (follows the resolved T4: {1,2,3} is the only
primitive tight 3-set).  Goal: enumerate ALL primitive 4-sets {a<b<c<d} in
[1,N] with kappa = 1/5 exactly, and extract structure.

Exact machinery (Lemma L1 candidate set, all-integer arithmetic):
  kappa(V) = max over t = p/q, q in {2v_i} u {v_i+v_j},
             of min_i dist(p*v_i, qZ)/q.
  kappa >= 1/5 holds automatically when 5 divides no element (t = 1/5),
  so then:  tight(V) <=> every candidate has min-dist <= 1/5.

PROVED pre-filters for tightness (run before full evaluation):
  F1 (Lemma T3, n=4): some element divisible by each of 2, 3, 4.
  F2 (Lemma T at t*=1/5, new here): if 5 divides no element, t = 1/5 is a
      maximizing time; the tight runners there are exactly the residues
      +-1 mod 5 (residue +-2 sits at 2/5, residue 0 at 0), and Lemma T(b)
      forces a rising AND a falling tight runner, every rising+falling
      pair summing to 0 mod 5 => all rising ≡ r, all falling ≡ -r (mod 5);
      distance 1/5 forces r = +-1.  Hence:
      (5 | some v) OR (some v ≡ 1 and some v ≡ 4 mod 5).
  F2 is used only in this disjunctive form: no unproved T1 is assumed, and
  tight sets with 5 | v would still be found (and reported as T1 hits).

Outputs:
  SELF-TESTS S1-S4 (abort on failure).
  A  exhaustive census, primitive 4-subsets of [1,N] (arg1, default 60),
     incremental by max element d.  All tight sets listed.
  B  per-tight-set structure: witness time, residues mod 5, nu_2 histogram,
     sum condition, {1,2,3} containment, pair/triple window conditions.
  C  families kappa({1,2,3,d}) and kappa({1,3,4,d}) for d up to 200.

ASCII only, flushed log.
"""
import sys, os, time, math
from fractions import Fraction
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = os.path.join(HERE, "lonely_runner_tight4.log")
sys.path.insert(0, HERE)
from lonely_runner_census import kappa_exact  # noqa: E402

_FH = None


def out(s=""):
    print(s, flush=True)
    if _FH is not None:
        _FH.write(s + "\n")
        _FH.flush()


def dist_res(v, q):
    r = v % q
    return r if r <= q - r else q - r


def tight4_class(V):
    """0/1/-1 = kappa >, ==, < 1/5  (integer engine, early exit)."""
    best_n, best_d = 0, 1
    cands = set()
    for v in V:
        for m in range(1, 2 * v):
            cands.add((m, 2 * v))
    for i in range(4):
        for j in range(i + 1, 4):
            s = V[i] + V[j]
            for m in range(1, s):
                cands.add((m, s))
    cl = sorted(cands, key=lambda pq: -abs(pq[0] / pq[1] - 0.2))
    for (p, q) in cl:
        g = min(dist_res(p * v, q) for v in V)
        if g * best_d > best_n * q:
            best_n, best_d = g, q
            if 5 * best_n > best_d:
                return 0
    if 5 * best_n == best_d:
        return 1
    if 5 * best_n > best_d:
        return 0
    return -1


def passes_filters(V):
    """F1 (Lemma T3) and F2 (Lemma T at t*=1/5), both proved necessary."""
    if not any(v % 4 == 0 for v in V):
        return False                      # T3, M=4 (implies M=2)
    if not any(v % 3 == 0 for v in V):
        return False                      # T3, M=3
    if all(v % 5 != 0 for v in V):
        if not (any(v % 5 == 1 for v in V) and any(v % 5 == 4 for v in V)):
            return False                  # F2
    return True


# ------------------------------------------- generalized T4-a machinery (n=4)

def windows_pair(p, q, mod=5):
    """Components of G_p n G_q on circle [0,mod), exact Fractions.
    G_v = {T : vT mod mod in (1, mod-1)}; B_v arcs are the closed
    [(mk-1)/v, (mk+1)/v]."""
    pts = set()
    for v in (p, q):
        for k in range(0, v + 1):
            pts.add(Fraction(mod * k - 1, v))
            pts.add(Fraction(mod * k + 1, v))
    pts = sorted(x for x in pts if 0 <= x <= mod)
    wins = []
    for i in range(len(pts) - 1):
        lo, hi = pts[i], pts[i + 1]
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        if 1 < (mid * p) % mod < mod - 1 and 1 < (mid * q) % mod < mod - 1:
            if wins and wins[-1][1] == lo:
                wins[-1] = (wins[-1][0], hi)
            else:
                wins.append((lo, hi))
    return wins


def windows_triple(a, b, c, mod=5):
    """Components of G_a n G_b n G_c on circle [0,mod)."""
    res = []
    for (lo, hi) in windows_pair(a, b, mod):
        pieces = []
        for k in range(c):
            glo = Fraction(mod * k + 1, c)
            ghi = Fraction(mod * (k + 1) - 1, c)
            l2, h2 = max(lo, glo), min(hi, ghi)
            if l2 < h2:
                pieces.append((l2, h2))
        for w in pieces:
            if res and res[-1][1] == w[0]:
                res[-1] = (res[-1][0], w[1])
            else:
                res.append(w)
    return res


def in_single_arc(lo, hi, r, mod=5):
    """(lo,hi) inside one closed arc [(mk-1)/r,(mk+1)/r] of B_r (exact):
    need k with mod*k - 1 <= r*lo and r*hi <= mod*k + 1,
    i.e. ceil((r*hi - 1)/mod) <= k <= floor((r*lo + 1)/mod)."""
    def ceil_fr(x):
        return -((-x.numerator) // x.denominator)

    def floor_fr(x):
        return x.numerator // x.denominator
    klo = (r * hi - 1) / mod
    khi = (r * lo + 1) / mod
    return ceil_fr(klo) <= floor_fr(khi)


def triple_condition_ok(V, mod=5):
    """Every window of every 3-subset lies in a single arc of B_fourth."""
    V = list(V)
    for miss in range(4):
        tri = [V[i] for i in range(4) if i != miss]
        for (lo, hi) in windows_triple(tri[0], tri[1], tri[2], mod):
            if not in_single_arc(lo, hi, V[miss], mod):
                return False
    return True


def max_is_sum(V):
    d = V[3]
    return any(V[i] + V[j] == d for i in range(4) for j in range(i + 1, 4))


# ------------------------------------------------------------------ parts

def part_selftest(NV=16):
    out("=" * 78)
    out("SELF-TESTS")
    out("=" * 78)
    ok = True
    bad = cnt = 0
    for V in combinations(range(1, NV + 1), 4):
        g = 0
        for x in V:
            g = math.gcd(g, x)
        if g != 1:
            continue
        cnt += 1
        kr = kappa_exact(V, include_diff=False)
        r = tight4_class(V)
        cls = 0 if kr > Fraction(1, 5) else (1 if kr == Fraction(1, 5) else -1)
        if r != cls:
            bad += 1
            out("S1 MISMATCH V=%s ref=%s int=%d" % (V, kr, r))
    out("S1  integer engine vs kappa_exact, primitive 4-sets [1,%d]: "
        "%d sets, %d mismatches %s" % (NV, cnt, bad, "OK" if bad == 0 else "FAIL"))
    ok &= (bad == 0)

    k = kappa_exact((3, 8, 11, 19))
    good = (k == Fraction(7, 30))
    ok &= good
    out("S2  kappa(3,8,11,19) = %-6s expected 7/30  %s"
        % (str(k), "OK" if good else "FAIL"))
    for V in [(1, 2, 3, 4), (1, 3, 4, 7)]:
        k = kappa_exact(V)
        good = (k == Fraction(1, 5))
        ok &= good
        out("S2  kappa%s = %-4s expected 1/5  %s"
            % (V, str(k), "OK" if good else "FAIL"))

    bad = 0
    for V in combinations(range(1, NV + 1), 4):
        g = 0
        for x in V:
            g = math.gcd(g, x)
        if g != 1:
            continue
        kr = kappa_exact(V, include_diff=False)
        tri = triple_condition_ok(V)
        if tri != (kr == Fraction(1, 5)):
            bad += 1
            out("S3 MISMATCH V=%s kappa=%s triOK=%s" % (V, kr, tri))
    out("S3  tight <=> every triple-window in single B arc [1,%d]: "
        "%d mismatches %s" % (NV, bad, "OK" if bad == 0 else "FAIL"))
    ok &= (bad == 0)

    bad = 0
    for V in combinations(range(1, NV + 1), 4):
        g = 0
        for x in V:
            g = math.gcd(g, x)
        if g != 1:
            continue
        if kappa_exact(V, include_diff=False) == Fraction(1, 5):
            if not passes_filters(V):
                bad += 1
                out("S4 FILTER-REJECTED TIGHT SET V=%s" % (V,))
    out("S4  filters never reject a tight set [1,%d]: %d violations %s"
        % (NV, bad, "OK" if bad == 0 else "FAIL"))
    ok &= (bad == 0)

    out("SELF-TESTS: %s" % ("ALL PASSED" if ok else "FAILURE -- ABORT"))
    out("")
    if not ok:
        sys.exit(1)


def part_census(N):
    out("=" * 78)
    out("PART A: exhaustive tight-4 census, primitive 4-subsets of [1,%d]" % N)
    out("=" * 78)
    tight_all = []
    t0 = time.time()
    tot = full = 0
    for d in range(4, N + 1):
        tight_d = []
        cnt_d = full_d = 0
        for c in range(3, d):
            for b in range(2, c):
                for a in range(1, b):
                    V = (a, b, c, d)
                    g = 0
                    for x in V:
                        g = math.gcd(g, x)
                        if g == 1:
                            break
                    if g != 1:
                        continue
                    cnt_d += 1
                    tot += 1
                    if not passes_filters(V):
                        continue
                    full_d += 1
                    full += 1
                    r = tight4_class(V)
                    if r == 1:
                        tight_d.append(V)
                    elif r == -1:
                        out("  *** LRC(4) VIOLATION *** V=%s" % (V,))
        if tight_d:
            tight_all.extend(tight_d)
            out("d=%3d  sets=%7d  full=%7d  tight=%2d  %s"
                % (d, cnt_d, full_d, len(tight_d), tight_d))
        else:
            out("d=%3d  sets=%7d  full=%7d  tight= 0" % (d, cnt_d, full_d))
    out("census done: sets=%d full-evals=%d tight=%d  elapsed %.1f s"
        % (tot, full, len(tight_all), time.time() - t0))
    out("")
    return tight_all


def part_struct(tight_all):
    out("=" * 78)
    out("PART B: structure of the tight 4-sets")
    out("=" * 78)
    hdr = ("V              t*     res5        #1 #4  nu2hist        "
           "{1,2,3}? max=Sum? nAB  ab-in-Bc ab-in-Bd triOK")
    out(hdr)
    for V in tight_all:
        a, b, c, d = V
        k, tstar = kappa_exact(V, want_t=True)
        assert k == Fraction(1, 5)
        res = [v % 5 for v in V]
        n1, n4 = res.count(1), res.count(4)
        nu2 = {}
        for v in V:
            x, e = v, 0
            while x % 2 == 0:
                x //= 2
                e += 1
            nu2[e] = nu2.get(e, 0) + 1
        pw = windows_pair(a, b)
        in_c = all(in_single_arc(lo, hi, c) for lo, hi in pw)
        in_d = all(in_single_arc(lo, hi, d) for lo, hi in pw)
        has123 = (V[0], V[1], V[2]) == (1, 2, 3)
        out("%-15s%-7s%-13s%2d %2d  %-14s %-8s %-8s %3d  %-8s %-8s %s"
            % (str(V), str(tstar), str(res), n1, n4, str(nu2),
               "YES" if has123 else "no", "YES" if max_is_sum(V) else "no",
               len(pw), in_c, in_d, triple_condition_ok(V)))
    out("")


def part_family(DMAX=200):
    out("=" * 78)
    out("PART C: fixed-prefix families, d = ... up to %d" % DMAX)
    out("=" * 78)
    for (x, y, z) in [(1, 2, 3), (1, 3, 4), (1, 2, 4), (1, 3, 5), (2, 3, 4)]:
        tight = []
        for d in range(z + 1, DMAX + 1):
            V = (x, y, z, d)
            g = 0
            for u in V:
                g = math.gcd(g, u)
            if g != 1:
                continue
            if tight4_class(V) == 1:
                tight.append(d)
        out("  tight members of {%d,%d,%d,d}: %s" % (x, y, z, tight))
    out("  ({1,2,3,4} consecutive; {1,3,4,7} the known sporadic.)")
    out("")


def main():
    global _FH
    _FH = open(LOGF, "w", encoding="ascii", errors="replace")
    try:
        out("lonely_runner_tight4.py -- tight 4-set census, %s" % time.ctime())
        out("python %s" % sys.version.split()[0])
        out("")
        N = int(sys.argv[1]) if len(sys.argv) > 1 else 60
        part_selftest(16)
        tight = part_census(N)
        part_struct(tight)
        part_family(200)
    finally:
        _FH.close()


if __name__ == "__main__":
    main()