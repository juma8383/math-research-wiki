#!/usr/bin/env python
# K34 refine4 extension (background): extend the depth-parity table for
# curve A to 1e6 (W2b recount caveat: the filed "231 valid primes in
# (3e5,1e6]" used bsgs_order which silently skipped primes).  Also recount
# valid primes (ord | M_A) in (3e5,1e6] with complete order-finding.
import sys, time, json, math
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
from mss_k34_refine3 import (exact_W, vp_of_W, ord_of_G, primes_upto, out)

MA = 42078090600

if __name__ == "__main__":
    A2, A4, G = -256, 18432, (128, 512)
    Wex = exact_W(A2, A4, G, 60)
    rows = []
    nvalid = 0
    t0 = time.time()
    ps = [p for p in primes_upto(1000000) if p > 300000]
    for i, p in enumerate(ps):
        o = ord_of_G(G, p, A2, A4)
        vd = 0; oo = o
        while oo % p == 0: vd += 1; oo //= p
        b = vp_of_W(A2, A4, G, Wex, o, p)
        if b is None:
            out("  PRECISION FAIL p=%d ord=%d" % (p, o)); continue
        rows.append((p, o, vd, b))
        if MA % o == 0: nvalid += 1
        if (i % 2000) == 0:
            out("  %d/%d primes (%.0fs), valid so far %d" % (i, len(ps), time.time()-t0, nvalid))
    out("=== A extension 3e5..1e6: %d primes, valid %d (%.0fs) ===" % (len(rows), nvalid, time.time()-t0))
    json.dump({"M": MA, "rows": rows},
              open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\parityA_ext.json", "w"))
    out("saved parityA_ext.json")