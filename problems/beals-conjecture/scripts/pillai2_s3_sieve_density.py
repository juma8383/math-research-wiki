#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quantify Lemma S3's sieve (beals-conjecture, odd-odd Pillai-2).

Lemma S3/S3b (proved, odd-odd-pillai-2.md): in any solution of X^u - Y^v = 2,
a prime q = 1 (mod e) with 2 NOT an e-th power residue mod q divides
NEITHER X nor Y, for e in {u, v}.  Density of such q among q = 1 (mod e)
is (e-1)/e (Chebotarev), so the surviving density of integers with no
forbidden prime factor below z should decay like C_e (log z)^{-1/e}
(Mertens for the progression, thinned by density 1/e... precisely
delta = (e-1)/e within the class 1 mod e of size phi(e)=e-1, so
sum 1/q ~ delta/(phi(e)) log log z = (1/e) log log z).

This script:
  1. computes forbidden primes q <= 2e5 for e in {3,5,7,11,13,17,19};
  2. measures the partial Euler products P_e(z) at z = 1e2..2e5 and fits
     the log-log slope against 1/e;
  3. extrapolates the sieve's reduction factor at z = 1e25 per exponent
     and for the dominant (u,v) pairs of the plane heuristic.
"""
from sympy import primerange

EBITS = [3, 5, 7, 11, 13, 17, 19]
ZS = [100, 1000, 10**4, 10**5, 2 * 10**5]
QCAP = 2 * 10**5

def main():
    out = []
    out.append("== S3 sieve quantification (forbidden primes <= %d) ==" % QCAP)
    fit = {}
    for e in EBITS:
        forb = []
        for q in primerange(2, QCAP + 1):
            if q % e != 1:
                continue
            if pow(2, (q - 1) // e, q) != 1:
                forb.append(q)
        prods = []
        p = 1.0
        idx = 0
        for z in ZS:
            while idx < len(forb) and forb[idx] <= z:
                p *= (1.0 - 1.0 / forb[idx])
                idx += 1
            prods.append(p)
        # fit slope in (log log z, log P)
        import math
        xs = [math.log(math.log(z)) for z in ZS]
        ys = [math.log(v) for v in prods]
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
        sxx = sum((a - mx) ** 2 for a in xs)
        slope = sxy / sxx
        fit[e] = (prods[-1], -slope)
        out.append("e=%2d: #forbidden=%d  P(2e5)=%.6f  fitted slope=%.4f "
                   "(theory 1/e=%.4f)" % (e, len(forb), prods[-1], -slope, 1.0 / e))
        out.append("      P(z): " + "  ".join("%.2e" % v for v in prods))
    out.append("")
    out.append("Extrapolated surviving density / reduction at the 1e25 box"
               " (log z = %.3f):" % math.log(1e25))
    L = math.log(1e25)
    Ps = {}
    for e in EBITS:
        const = fit[e][0] * ((math.log(2 * 10**5)) ** fit[e][1])
        P25 = const * L ** (-fit[e][1])
        Ps[e] = P25
        out.append("  e=%2d: P_e(1e25) ~ %.4f -> search-space reduction x%.2f"
                   % (e, P25, 1.0 / P25))
    out.append("")
    out.append("Combined (u,v) reduction ~ 1/(P_u * P_v) at the 1e25 box:")
    for (u, v) in [(5, 3), (3, 5), (7, 3), (3, 7), (5, 7)]:
        out.append("  (u,v)=(%d,%d): %.1f x %.1f = x%.1f"
                   % (u, v, 1.0 / Ps[u], 1.0 / Ps[v], 1.0 / (Ps[u] * Ps[v])))
    txt = "\n".join(out)
    print(txt)
    with open("pillai2_s3_density.log", "w") as f:
        f.write(txt + "\n")

import math
if __name__ == "__main__":
    main()