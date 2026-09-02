#!/usr/bin/env python
# K34 refine4 part 1 (background): depth-parity table for ALL good primes.
# For each good prime q <= BMAX: d = ord_q(G), vq_d = v_q(d),
# b_d = v_q(W_d) (base depth, Shipsey engine), kill = b_d odd.
# Kill condition (q does not divide the index n): n = kM + c with d | n and
# odd total depth => n not a square-X index.  Saved to parityA/parityB.json.
import sys, time, json
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
from mss_k34_refine3 import (exact_W, vp_of_W, ord_of_G, primes_upto, out)

MA = 42078090600
MB = 264

def build(tag, A2, A4, G, BMAX):
    Wex = exact_W(A2, A4, G, 60)
    rows = []
    t0 = time.time()
    for i, p in enumerate(primes_upto(BMAX)[2:]):
        o = ord_of_G(G, p, A2, A4)
        vd = 0; oo = o
        while oo % p == 0: vd += 1; oo //= p
        b = vp_of_W(A2, A4, G, Wex, o, p)
        if b is None:
            out("  %s: PRECISION FAIL p=%d ord=%d" % (tag, p, o)); continue
        rows.append((p, o, vd, b))
        if (i % 2000) == 0:
            out("  %s: %d primes (%.0fs)" % (tag, i, time.time()-t0))
    out("=== %s: %d primes <= %d (%.0fs) ===" % (tag, len(rows), BMAX, time.time()-t0))
    nb = {}
    for p, o, vd, b in rows: nb[b] = nb.get(b, 0) + 1
    out("  base-depth histogram: %s" % dict(sorted(nb.items())))
    return rows

if __name__ == "__main__":
    t0 = time.time()
    rowsA = build("A", -256, 18432, (128, 512), 300000)
    json.dump({"M": MA, "rows": rowsA},
              open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\parityA.json", "w"))
    rowsB = build("B", 256, -2048, (-128, 1536), 200000)
    json.dump({"M": MB, "rows": rowsB},
              open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\parityB.json", "w"))
    out("total %.0fs" % (time.time()-t0))