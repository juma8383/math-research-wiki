#!/usr/bin/env python3
import math

P = lambda Y: 56644*Y**4 - 952*Y**3 - 604*Y*Y - 4*Y + 1

# Integer factorization over Z: (aY^2+bY+c)(dY^2+eY+f)
pairs = [(1,56644),(2,28322),(4,14161),(7,8092),(14,4046),(17,3332),
         (28,2023),(34,1666),(49,1156),(68,833),(119,476),(238,238)]
found = None
for (a,d) in pairs:
    for c in (1,-1):
        f_ = c
        for b in range(-500, 501):
            # Y coeff: b*f + c*e = -4
            num = -4 - b*f_
            if num % c != 0: continue
            e = num // c
            if a*e + b*d != -952: continue
            if a*f_ + b*e + c*d != -604: continue
            found = (a, b, c, d, e, f_)
            break
        if found: break
    if found: break
print("factorization over Z:", found)

# numeric roots of P (all four)
import itertools
def allroots(P, lo=0.0, hi=1.0, n=4000):
    xs = [lo + (hi-lo)*i/n for i in range(n+1)]
    roots = []
    for i in range(n):
        y1, y2 = P(xs[i]), P(xs[i+1])
        if y1 == 0: roots.append(xs[i])
        if y1*y2 < 0:
            a, b = xs[i], xs[i+1]
            for _ in range(80):
                mid = (a+b)/2
                if P(a)*P(mid) <= 0: b = mid
                else: a = mid
            roots.append((a+b)/2)
    return roots
rts = allroots(P)
print("roots of P in [0,1]:", [f"{r:.10f}" for r in rts])
for r in rts:
    print(f"  Y = {r:.10f} -> X = {math.sqrt(r):.10f}")
print(f"\nX* = sqrt of the largest root in (0,1): {math.sqrt(max(rts)):.10f}" if rts else "")
print("P(0)=1, P(1)=", P(1))