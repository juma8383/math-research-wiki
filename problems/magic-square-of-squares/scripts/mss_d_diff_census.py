#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Difference census + difference-side window validation.
Question: are there pairs x < y in D(w^2) with y - x in D(w^2)?
(the A2 census tested sums only). If yes, they are REAL data on which
the difference-triple window theorem can be validated (no sum triple
exists anywhere, so the theorem has so far been untestable).
"""
from math import isqrt, gcd

W = 10**6
dmap = {}
M = isqrt(W)
for m in range(2, M+1):
    mm = m*m
    for n in range(1, m):
        c = mm + n*n
        if c > W: break
        if (m-n) % 2 == 0 or gcd(m,n) != 1: continue
        ab2 = 2*(mm-n*n)*(2*m*n)
        k = 1
        while k*c <= W:
            dmap.setdefault(k*c, set()).add(ab2*k*k)
            k += 1
assert len(dmap[425]) == 7

n_diff = 0
examples = []
win_viol = 0
pairs_checked = 0
for w, Dset in dmap.items():
    if len(Dset) < 2: continue
    ww = w*w
    D = sorted(Dset)
    reps = {}
    for d in D:
        su = isqrt(ww-d); sd = isqrt(ww+d)
        reps[d] = ((su+sd)//2, (sd-su)//2)
    for i in range(len(D)):
        x = D[i]
        for j in range(i+1, len(D)):
            y = D[j]
            d2 = y - x
            if d2 in Dset:
                n_diff += 1
                if len(examples) < 10:
                    examples.append((w, x, y, d2))
                # window validation on the REAL difference triple
                # {y-x, x, y}: x-role = min(x, d2), partner = max(x, d2)
                small, large = (x, d2) if x < d2 else (d2, x)
                us, vs = reps[small]
                if not (2*(us+vs)+1 <= large <= (us-vs)**2 - 1):
                    win_viol += 1
                    if win_viol <= 5:
                        print("WINDOW VIOLATION w=%d small=%d large=%d" % (w, small, large))
    pairs_checked += len(D)*(len(D)-1)//2

print("pairs total: %d" % pairs_checked)
print("pairs with y-x in D(w^2): %d" % n_diff)
if examples:
    print("first examples (w, x, y, y-x):")
    for e in examples:
        print("  ", e)
print("difference-window violations on real triples: %d" % win_viol)
