#!/usr/bin/env python3
# Sel(phi') FINAL — candidates: classes c = ±2^i·17^j (i∈{0,1} parity, j∈{0,1}),
# i.e. {±1, ±2, ±17, ±34} (8 classes). Covering: c W^2 = c^2 Z^4 + ap c Z^2 + bp,
# ap = -4t+4, bp = -2032-8t (rational-part check: ap^2-4bp = 3808 = 2^5·7·17 RATIONAL).
# Singular primes: P | 2, P | bp (over 2, 17, 37, 103), P | (ap^2-4bp) (over 2,7,17), P | c, (t).
# rank E+(L) = dim Sel(phi) + dim Sel(phi') - 2 = 2 + dim Sel(phi') - 2.
# GATE: dim Sel(phi') <= 1 => rank <= 1.
from sage.all import *
import itertools, time, sys
L = QuadraticField(-271, 't'); t = L.gen()
ap = -4*t + 4; bp = -2032 - 8*t
assert (2*t-2)**2 - 4*L(238) == bp

cands = []
for j in (0, 1):
    for i in (0, 1):
        for d in (1, 2, 17, 34):
            pass
cands = [L(1), L(-1), L(2), L(-2), L(17), L(-17), L(34), L(-34)]

constrained = []
seen = set()
def addP(P):
    s = str(P)
    if s not in seen:
        seen.add(s); constrained.append(P)
for q in (2, 7, 17, 37, 103):
    for P in L.primes_above(q): addP(P)
for P in L.primes_above(271): addP(P)
print("constrained:", [str(P) for P in constrained], flush=True)

def local_soluble(c, P):
    Kp = P.residue_field()
    p = int(Kp.characteristic())
    A, B, C = Kp(ap), Kp(bp), Kp(c)
    # infinity: C square in F_p => soluble
    if C != 0:
        if p == 2 or C**((p-1)//2) == 1:
            return True
    if p != 2 and B != 0 and C != 0 and Kp(ap*ap - 4*bp) != 0:
        return True   # smooth => Lang
    found = None
    for z in range(p):
        for w in range(p):
            Z, W = Kp(z), Kp(w)
            if C*W*W == C*C*Z**4 + A*C*Z*Z + B:
                gz = -(4*C*C*Kp(z)**3 + 2*A*C*Kp(z))
                gw = 2*C*Kp(w)
                if (gz, gw) != (0, 0):
                    return True
                if found is None:
                    found = (z, w)
    if found is None:
        return False
    Z0, W0 = found
    alpha = -12*C*C*Kp(Z0)**2 - 2*A*C
    beta = C
    if alpha == 0 or beta == 0:
        return True
    val = -alpha/beta
    if val == 0:
        return True
    return Kp(val)**((p-1)//2) == 1

t0 = time.time()
survivors = []
for c in cands:
    ok = True
    for P in constrained:
        if not local_soluble(c, P):
            ok = False; break
    if ok:
        survivors.append(c)
print("phi'-Selmer survivors:", len(survivors), flush=True)
for c in survivors:
    print("   c =", c, flush=True)
print("elapsed:", round(time.time()-t0,1), "s", flush=True)
print("DONE", flush=True)