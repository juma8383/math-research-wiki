#!/usr/bin/env python
# K34 refine3 part 2 (background): full valid-prime depth census.
# Valid primes for (E~_A, G_A): ord_p(G) | M_A = 42078090600, p <= 3e5.
# Valid primes for (E~_B, G_B): ord_p(G_B) | M_B = 264, p <= 2e5.
# For each: b_p = depth of (ord)-multiple = v_p(W_ord) via the Shipsey engine.
# Outputs: validA_primes.json / validB_primes.json, R0 products (valid primes
# with ODD b_p -- these force p | k in the class-0 square-X condition),
# and the per-prime parity constraint v_p(k) = b_p + v_p(M) + v_p(d) mod 2.
import sys, time, json, math
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
from mss_k34_refine3 import (exact_W, vp_of_W, ord_of_G, primes_upto, out)

MA = 42078090600
MB = 264

def census(tag, A2, A4, G, M, BMAX):
    Wex = exact_W(A2, A4, G, 60)
    rows = []
    t0 = time.time()
    for i, p in enumerate(primes_upto(BMAX)[2:]):
        o = ord_of_G(G, p, A2, A4)
        if M % o: continue
        b = vp_of_W(A2, A4, G, Wex, o, p)
        if b is None:
            out("  %s: PRECISION FAIL p=%d ord=%d" % (tag, p, o)); continue
        vm = 0; mm = M
        while mm % p == 0: vm += 1; mm //= p
        vd = 0; oo = o
        while oo % p == 0: vd += 1; oo //= p
        # constraint: v_p(k) = b + v_p(M) + v_p(d) (mod 2)  [even-depth total]
        par = (b + vm + vd) % 2
        rows.append((p, o, b, par))
        if (i % 2000) == 0:
            out("  %s: %d primes scanned (%.0fs)" % (tag, i, time.time()-t0))
    hist = {}; R0 = 1; forced = []
    for p, o, b, par in rows:
        hist[b] = hist.get(b, 0) + 1
        if b % 2 == 1:
            R0 *= p; forced.append(p)
    out("=== %s: %d valid primes <= %d ===" % (tag, len(rows), BMAX))
    out("  depth histogram: %s" % dict(sorted(hist.items())))
    even = [(p, o, b) for p, o, b, par in rows if b % 2 == 0]
    out("  odd-Wieferich (even depth) valid primes: %s" % (even if even else "NONE"))
    out("  R0 = product of odd-depth valid primes: %d primes, log10(R0) = %.1f"
        % (len(forced), math.log10(R0) if R0 > 1 else 0.0))
    out("  forced k-divisibility: k = R0 * k' with v_p(k') even-or-free per above")
    return rows, forced

if __name__ == "__main__":
    t0 = time.time()
    rowsA, fA = census("A", -256, 18432, (128, 512), MA, 300000)
    json.dump({"M": MA, "rows": rowsA, "R0_forced": fA},
              open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\validA_primes.json", "w"))
    rowsB, fB = census("B", 256, -2048, (-128, 1536), MB, 200000)
    json.dump({"M": MB, "rows": rowsB, "R0_forced": fB},
              open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\validB_primes.json", "w"))
    out("total %.0fs" % (time.time()-t0))