#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sharp partner-window theorem -- numerics + corrected hourglass heuristic.

Theorem (proved 2026-09-01, notes.md): if {x, y, x+y} subseteq D(w^2) with
x = 2uv (u > v > 0 the rep of x), then
        2(u+v) + 1  <=  y  <=  (u-v)^2 - 1 ,
and the same holds with roles swapped.  Since the derivation of the LOWER
bound uses only  x in D, x+y in D, y > 0  (it does NOT need y in D), it
applies to every pair x < d' in D(w^2) with y = d' - x:

  Corollary A (spacing): any two elements x < d' of D(w^2) satisfy
        d' - x >= 2*sqrt(w^2 + x) + 1        (equivalently d' >= (u+v+1)^2).

This script:
  1. builds D(w^2) for all w <= W exactly (primitive-triple sweep);
  2. verifies rep extraction (isqrt) for every element;
  3. tests Corollary A on every consecutive pair (worst case) of every w;
  4. counts admissible pairs (both window conditions, theorem form) and
     computes the corrected hourglass heuristic
         H2 = sum_w #{admissible pairs} * |D| / w^2   (and strict |D|-2),
     compared against the naive all-pairs partial (filed: 1.0086 at W=1e6).
"""
import time
from math import isqrt, gcd

W = 10 ** 6
OUT = "window_spacing_W1e6.log"


def main():
    t0 = time.time()
    # ---- build D(w^2) for all w <= W ------------------------------------
    # rep (u,v) of w^2 <-> primitive (a,b,c=m^2+n^2) scaled by k: u=ka, v=kb
    dmap = {}
    M = isqrt(W)
    n_triples = 0
    for m in range(2, M + 1):
        mm = m * m
        for n in range(1, m):
            c = mm + n * n
            if c > W:
                break
            if (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            n_triples += 1
            # rep of w^2=c^2 is (a, b) = (m^2-n^2, 2mn); d = 2ab k^2
            a = mm - n * n
            b = 2 * m * n
            ab2 = 2 * a * b
            k = 1
            kc = c
            while kc <= W:
                w = kc
                d = ab2 * k * k
                s = dmap.get(w)
                if s is None:
                    dmap[w] = {d}
                else:
                    s.add(d)
                k += 1
                kc += c
    print("built D-sets: %d w-values, %d primitive triples, %.1fs"
          % (len(dmap), n_triples, time.time() - t0), flush=True)
    # builder self-test: known exact values
    assert sorted(dmap[5]) == [24], dmap.get(5)
    assert len(dmap[425]) == 7, sorted(dmap.get(425, []))

    # ---- per-w checks ----------------------------------------------------
    w_with = sorted(dmap)
    rep_bad = 0
    reps_done = 0
    spacing_viol = 0
    spacing_checked = 0
    min_ratio = 1e18  # (d' - x) / (2*sqrt(w^2+x)) over all consecutive pairs
    args_min = None
    pairs_all = 0
    adm_pairs = 0
    H2 = 0.0
    H2s = 0.0
    Hn = 0.0  # naive partial (all pairs), to reproduce the filed 1.0086
    lopsided_el = 0
    total_el = 0
    thr = 3 + 2 * (2 ** 0.5)  # u/v must exceed this for a nonempty window

    for w in w_with:
        D = sorted(dmap[w])
        nD = len(D)
        ww = w * w
        reps = []
        for d in D:
            su = isqrt(ww - d)
            sd = isqrt(ww + d)
            u = (su + sd) // 2
            v = (sd - su) // 2
            reps_done += 1
            if 2 * u * v != d or u * u + v * v != ww or u <= v:
                rep_bad += 1
            reps.append((u, v))
            total_el += 1
            if u > thr * v:
                lopsided_el += 1
        # Corollary A: consecutive pairs are the worst case
        for i in range(nD - 1):
            x = D[i]
            dx = D[i + 1] - x
            u, v = reps[i]
            lb = 2 * (u + v) + 1
            spacing_checked += 1
            if dx < lb:
                spacing_viol += 1
                if spacing_viol <= 5:
                    print("SPACING VIOLATION w=%d x=%d next=%d lb=%d"
                          % (w, x, D[i + 1], lb), flush=True)
            r = dx / (2 * ((ww + x) ** 0.5))
            if r < min_ratio:
                min_ratio = r
                args_min = (w, x, D[i + 1], lb, dx)
        # naive partial heuristic (all pairs, density |D|) to compare
        if nD >= 2:
            Hn += (nD * (nD - 1) // 2) * (nD / ww)
    # clean second pass for H2 (theorem form: both windows)
    H2 = 0.0
    H2s = 0.0
    adm_total = 0
    for w in w_with:
        D = sorted(dmap[w])
        nD = len(D)
        if nD < 2:
            continue
        ww = w * w
        reps = []
        for d in D:
            su = isqrt(ww - d)
            sd = isqrt(ww + d)
            reps.append(((su + sd) // 2, (sd - su) // 2))
        adm = 0
        for i in range(nD):
            x = D[i]
            ux, vx = reps[i]
            lo_y = 2 * (ux + vx) + 1
            hi_y = (ux - vx) * (ux - vx) - 1
            # early exit: window upper end is w^2 - x - 1; if x's rep is not
            # lopsided the window is empty
            if hi_y < lo_y:
                continue
            for j in range(i + 1, nD):
                y = D[j]
                if y < lo_y or y > hi_y:
                    continue
                uy, vy = reps[j]
                lo_x = 2 * (uy + vy) + 1
                hi_x = (uy - vy) * (uy - vy) - 1
                if lo_x <= x <= hi_x:
                    adm += 1
        adm_total += adm
        H2 += adm * (nD / ww)
        H2s += adm * ((nD - 2) / ww)

    lines = []
    lines.append("== window/spacing W=%d ==" % W)
    lines.append("reps verified: %d checked, %d bad" % (reps_done, rep_bad))
    lines.append("spacing (Corollary A): checked=%d violations=%d"
                 % (spacing_checked, spacing_viol))
    if args_min:
        lines.append("min gap ratio (d'-x)/(2*sqrt(w^2+x)) = %.4f at w=%d "
                     "x=%d next=%d lb=%d dx=%d"
                     % ((min_ratio,) + args_min))
    lines.append("elements: total=%d lopsided(u/v>3+2sqrt2)=%d (%.3f)"
                 % (total_el, lopsided_el, lopsided_el / max(1, total_el)))
    lines.append("heuristic: naive-pairs H_partial=%.6f (filed 1.0086)"
                 % Hn)
    lines.append("admissible pairs (both windows): %d" % adm_total)
    lines.append("H2 (window-corrected, density |D|)   = %.6f" % H2)
    lines.append("H2s (window-corrected, density |D|-2) = %.6f" % H2s)
    lines.append("x24 (density 24|D|, filed convention): naive=%.6f "
                 "H2=%.6f H2s=%.6f" % (24 * Hn, 24 * H2, 24 * H2s))
    lines.append("time=%.1fs" % (time.time() - t0))
    txt = "\n".join(lines)
    print(txt)
    with open(OUT, "w") as f:
        f.write(txt + "\n")


if __name__ == "__main__":
    main()