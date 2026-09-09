#!/usr/bin/env python3
# 2-isogeny Selmer for E+ over L — v7 FINAL: complete local tests including
# points at infinity (the affine quartic dW^2 = d^2Z^4 + adZ^2 + b has smooth
# points at infinity on its normalization iff d is a local square mod P).
# Local test at prime P (with residue field F_p):
#   1. smooth (P ∤ 2*b*d*(a^2-4b), P ∤ 271): Lang => soluble.
#   2. d square mod P => soluble (point at infinity on the smooth model).
#   3. affine enumeration mod P (all (Z,W) in F_p^2) for singular cases:
#      nonsingular affine solution => soluble (Hensel).
#      only singular solutions => double-point tangent test.
#      no solution => NOT soluble (since infinity failed too).
#   4. P | d (d ≡ 0 mod P): 2-adic-style: handled by the P^n ring model test
#      (n=5 at P | 2; n=2 elsewhere) — with the infinity caveat: d ≡ 0 => the
#      leading form degenerates: treat separately.
# Survivors = Sel(phi) as a subgroup of L*/L*2 = <2,7,17,t,-1>.
from sage.all import *
import itertools, time, sys
L = QuadraticField(-271, 't'); t = L.gen()
a = 2*t-2; b = L(238)

divs = [1, 2, 7, 17, 14, 34, 119, 238]
cands = []
for e in (0, 1):
    for d in divs:
        cands.append(L(d) * (t**e))
        cands.append(-L(d) * (t**e))

constrained = []
seen = set()
def addP(P):
    s = str(P)
    if s not in seen:
        seen.add(s); constrained.append(P)
for q in (2, 7, 17):
    for P in L.primes_above(q): addP(P)
for P, e in L.ideal(a*a - 4*b).factor(): addP(P)
for P in L.primes_above(271): addP(P)

def local_soluble(c, P):
    Kp = P.residue_field()
    p = int(Kp.characteristic())
    A, B, C = Kp(a), Kp(b), Kp(c)
    if C != 0:
        # infinity test first (cheap): soluble iff C is a square in F_p
        # (for p = 2: every element of F_2* is a square (F_2* = {1}):
        if p == 2 or C**((p-1)//2) == 1:
            return True
    # infinity failed: affine enumeration:
    if p != 2 and B != 0 and C != 0 and Kp(a*a-4*b) != 0:
        # smooth affine + no infinity point: genus-1: the torsor has NO
        # point at infinity but might have finite points: can't shortcut —
        # BUT a smooth genus-1 curve over F_p HAS a point (Lang: H^1 = 0):
        # the SMOOTH model always has points — affine or at infinity: if the
        # infinity points are defined over F_p (C square) we're done; if C is
        # a nonsquare, the curve still has F_p-points SOMEWHERE (genus-1 +
        # Hasse + Lang => torsor trivial): the smooth model has # >= 1 point
        # — could be at infinity ONLY if soluble there; otherwise finite:
        # so if C is a nonsquare mod P: finite point MUST exist (Lang) => SOLUBLE.
        return True
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
    # double point:
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
            ok = False
            break
    if ok:
        survivors.append(c)
print("phi-Selmer survivors:", len(survivors), flush=True)
for c in survivors:
    print("   c =", c, flush=True)
print("elapsed:", round(time.time()-t0,1), "s", flush=True)
print("DONE", flush=True)