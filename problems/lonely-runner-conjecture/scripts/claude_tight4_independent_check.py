#!/usr/bin/env python
# Independent tight-4 census [1,45] (Claude, fresh code, integer engine).
# kappa exact via Lemma L1: sup over t = m/2v_i and t = m/(v_i+v_j).
import math
from fractions import Fraction

def dist(v, q):
    r = v % q
    return min(r, q - r)

def kappa_exact_int(V):
    n = len(V)
    cands = set()
    for v in V:
        for m in range(1, 2*v):
            cands.add(Fraction(m, 2*v))
        for i in range(n):
            for j in range(i+1, n):
                s = V[i] + V[j]
                for m in range(1, s):
                    cands.add(Fraction(m, s))
    best = Fraction(0)
    for t in cands:
        p, q = t.numerator, t.denominator
        d = min(dist(v*p, q) for v in V)
        # min over runners of ||t*v|| = dist(v*p, q)/q
        if d * best.denominator > best.numerator * q:
            best = Fraction(d, q)
    return best

# all primitive 4-sets in [1,45]
tight = []
lo_viol = 0
nsets = 0
S = range(1, 46)
import itertools
for V in itertools.combinations(S, 4):
    g = 0
    for v in V: g = math.gcd(g, v)
    if g != 1:
        continue
    nsets += 1
    k = kappa_exact_int(list(V))
    if k == Fraction(1, 5):
        print("TIGHT:", V)
    elif k < Fraction(1, 5):
        lo_viol += 1
        print("VIOLATION:", V, k)
print("sets checked:", nsets, "violations:", lo_viol)

# spot-check the two claimed tight sets + Fan-Sun
for V in ([1,2,3,4], [1,3,4,7], [3,8,11,19]):
    print(V, kappa_exact_int(V))