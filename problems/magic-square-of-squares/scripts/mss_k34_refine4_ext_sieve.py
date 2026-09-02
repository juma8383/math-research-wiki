# mss_k34_refine4_ext_sieve.py -- re-run the depth-parity sieve on curve A
# with the extended parity table (parityA.json <= 3e5 + parityA_ext.json
# (3e5,1e6], complete order-finding). Same kill logic as refine4_sieve.py.
import sys, json, math, time
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
from mss_k34_refine4_sieve import sieve

sc = r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts"
rowsA = json.load(open(sc + r"\parityA.json"))["rows"]
rowsX = json.load(open(sc + r"\parityA_ext.json"))["rows"]
allrows = rowsA + rowsX
MA = 42078090600

if __name__ == "__main__":
    nv = sum(1 for (p, o, vd, b) in allrows if MA % o == 0)
    hist = {}
    for (p, o, vd, b) in allrows:
        if MA % o == 0:
            hist[b] = hist.get(b, 0) + 1
    print("=== A extended table: %d + %d = %d primes <= 1e6 ==="
          % (len(rowsA), len(rowsX), len(allrows)))
    print("  valid primes (ord | M_A): %d ; base-depth hist: %s" % (nv, hist))
    t0 = time.time()
    sieve("A-ext", MA, [2, MA // 2 - 1, -2 % MA, -1 % MA], allrows, 200000)
    print("total %.0fs" % (time.time() - t0))