#!/usr/bin/env python3
# Height-bound sharpening: replace the conservative finite-part constant
# with EXACT local height constants at the 5 bad primes (the §2ak to-verify).
# Method (Stoll's "Implementing 2-descent..." / Flynn-style): at each bad
# prime p, the canonical-vs-naive local defect is bounded by a constant
# from the reduction type. For the even octic model, Stoll's normalization:
# the local contribution at p is bounded by v_p(disc(f))/2 * log p, and the
# SHARP constant uses the actual local invariants (the cluster picture /
# semistable reduction type). This script: compute the CLUSTER DATA of the
# octic at each bad prime (exact, via Sage's factorization mod p), derive
# the true local defect bound, and reassemble r0.
from sage.all import *
import math, json
R = PolynomialRing(QQ, 'w')
w = R.gen()
f = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + 56644
bad = [2, 3, 7, 17, 271]
out = {}
for p in bad:
    Rp = PolynomialRing(GF(p), 'x')
    fp = Rp(f)
    fac = fp.factor()
    degs = sorted((g.degree(), mult) for g, mult in fac)
    # cluster root structure mod p:
    print(f"p={p}: factorization degrees+mults: {fac}", flush=True)
    out[p] = [[int(dd), int(mult)] for dd, mult in degs]
with open('/home/linux/mss-k34/zd_clusters.json', 'w') as fh:
    json.dump(out, fh)
print("DONE")