#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expected number of additive PARALLELOGRAMS {x, y, x+y, y-x} in D(w^2)
over the entire plane of centers -- the exact 9-square condition
(mss-parallelogram-reduction iff theorem), quantified.

Model: for a pair x < y in D(w^2), P(x+y in D) ~ 24|D|/w^2 and
independently P(y-x in D) ~ 24|D|/w^2 (the filed density convention;
24 | d lattice correction).  The partner-window theorem (provable) is a
NECESSARY condition on the pair (both sum- and difference-triples are
additive triples, so both windows apply), so

  E_A3 = sum_w sum_{admissible pairs} (24|D|/w^2)^2

is a model upper bound for the total number of 9-square-generating
parallelograms over ALL centers, sharpened by the window.  Compare with
the naive all-pairs value (no window).
"""
import time
from math import isqrt, gcd

W = 10 ** 6
OUT = "parallelogram_heuristic_W1e6.log"


def main():
    t0 = time.time()
    dmap = {}
    M = isqrt(W)
    for m in range(2, M + 1):
        mm = m * m
        for n in range(1, m):
            c = mm + n * n
            if c > W:
                break
            if (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            ab2 = 2 * (mm - n * n) * (2 * m * n)
            k = 1
            while k * c <= W:
                w = k * c
                dmap.setdefault(w, set()).add(ab2 * k * k)
                k += 1
    assert len(dmap[425]) == 7  # Bremner self-test

    E3_win = 0.0
    E3_naive = 0.0
    adm = 0
    for w, Dset in dmap.items():
        nD = len(Dset)
        if nD < 2:
            continue
        ww = w * w
        dens = 24.0 * nD / ww
        E3_naive += (nD * (nD - 1) // 2) * dens * dens
        D = sorted(Dset)
        reps = []
        for d in D:
            su = isqrt(ww - d)
            sd = isqrt(ww + d)
            reps.append(((su + sd) // 2, (sd - su) // 2))
        for i in range(nD):
            x = D[i]
            ux, vx = reps[i]
            lo_y = 2 * (ux + vx) + 1
            hi_y = (ux - vx) * (ux - vx) - 1
            if hi_y < lo_y:
                continue
            for j in range(i + 1, nD):
                y = D[j]
                if y < lo_y or y > hi_y:
                    continue
                uy, vy = reps[j]
                if not (2 * (uy + vy) + 1 <= x <= (uy - vy) * (uy - vy) - 1):
                    continue
                # difference-side necessary condition (Cor. A on the pair
                # (x, y-x), applicable when x < y-x i.e. y > 2x; needs only
                # x's rep):
                if y > 2 * x and (y - 2 * x) < 2 * isqrt(ww + x) + 1:
                    continue
                adm += 1
                E3_win += dens * dens

    lines = []
    lines.append("== parallelogram heuristic W=%d ==" % W)
    lines.append("admissible pairs (sum windows + diff Cor.A): %d" % adm)
    lines.append("(note: for y < 2x the difference-side window needs the rep")
    lines.append(" of y-x, unmodelable before y-x in D -- no filter applied)")
    lines.append("E_A3 naive (all pairs)  = %.6e" % E3_naive)
    lines.append("E_A3 window-corrected   = %.6e" % E3_win)
    lines.append("ratio = %.1f" % (E3_naive / E3_win if E3_win else 0))
    lines.append("time=%.1fs" % (time.time() - t0))
    txt = "\n".join(lines)
    print(txt)
    with open(OUT, "w") as f:
        f.write(txt + "\n")


if __name__ == "__main__":
    main()