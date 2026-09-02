#!/usr/bin/env python
# K34 refine3 part 3: (a) re-verify the 5 survivor classes on ALL 640 valid
# primes from validA_primes.json (the sieve2 W2 count of 624 silently skipped
# 16 primes where bsgs_order returned None -- recount + class re-check here);
# (b) same for curve B's 34 valid primes vs its 5 classes mod 264.
import sys, json
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
from mss_k34_refine3 import ec_mul_mod, primes_upto, out

A2, A4, G = -256, 18432, (128, 512)
B2, B4, GB = 256, -2048, (-128, 1536)
MA = 42078090600
MB = 264

def Xq_A(P, p):
    x, y = P
    d = x*(x-4) % p
    if d == 0: return None
    n = 2*(y + 66*x) % p
    if n == 0: return 0
    return n * pow(d, -1, p) % p

def Xq_B(P, p):
    x, y = P
    d = x*(x-36) % p
    if d == 0: return None
    n = (6*y - 92*x) % p
    if n == 0: return 0
    return n * pow(d, -1, p) % p

def qr_set(p):
    return set(t*t % p for t in range(1, p))

def check(tag, A2, A4, G, M, classes, kill, jsonfile):
    rows = json.load(open(jsonfile))["rows"]
    out("=== %s: %d valid primes, classes %s ===" % (tag, len(rows), classes))
    bad = 0
    for p, o, b, par in rows:
        ok = qr_set(p)
        for c in classes:
            P = ec_mul_mod(G, c % o, p, A2, A4)
            if P is None:
                continue                       # kernel point: X undefined (0/0)
            X = Xq_A(P, p) if tag == "A" else Xq_B(P, p)
            if X is None:
                continue
            good = (X == 0 or X == 1) if p in kill else (X == 0 or X in ok)
            if not good:
                bad += 1
                out("  VIOLATION p=%d ord=%d c=%d X=%s" % (p, o, c, X))
    out("  violations: %d" % bad)

if __name__ == "__main__":
    check("A", A2, A4, G, MA, [0, 2, MA//2-1, MA-2, MA-1], (5, 11, 13),
          r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\validA_primes.json")
    check("B", B2, B4, GB, MB, [0, 1, 2, 134, 262], (5, 19, 29),
          r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\validB_primes.json")