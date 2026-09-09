#!/usr/bin/env python3
# Brute-force search for the Prym curve E/K: y^2 = x^3 + A x^2 + B x with
# A = a0 + a1*s, B = b0 + b1*s (s^2 = 238), small coefficients.
# For each split prime p with residues r1, r2 for s: traces at the two ideals.
# Targets: 23: (-4,-4); 29: (0,-2); 37: (10,-10); 41: (-6,-6).
import math

def ap_curve(a, b, p):
    cnt = 1
    for u in range(p):
        v = (u**3 + a*u*u + b*u) % p
        if v == 0: cnt += 1
        elif pow(v, (p-1)//2, p) == 1: cnt += 2
    return p + 1 - cnt

def sqrts_mod(a, p):
    return [r for r in range(p) if (r*r - a) % p == 0]

# split data: residues of s mod p at the two ideals:
data = {}
for p in (23, 29, 37, 41):
    rs = sqrts_mod(238, p)
    data[p] = rs
print("residues:", data)

targets = {23: (-4, -4), 29: (0, -2), 37: (10, -10), 41: (-6, -6)}

found = []
R = 12  # coefficient bound
for a0 in range(-R, R+1):
    for a1 in range(-R, R+1):
        for b0 in range(-R, R+1):
            for b1 in range(-R, R+1):
                ok = True
                for p in (23, 29, 37, 41):
                    r1, r2 = data[p]
                    t1 = ap_curve((a0 + a1*r1) % p, (b0 + b1*r1) % p, p)
                    t2 = ap_curve((a0 + a1*r2) % p, (b0 + b1*r2) % p, p)
                    if (t1, t2) != targets[p] and (t2, t1) != targets[p]:
                        ok = False; break
                if ok:
                    found.append((a0, a1, b0, b1))
                    print("MATCH: A = %d + %d*s, B = %d + %d*s" % (a0, a1, b0, b1))
print("total matches:", len(found))