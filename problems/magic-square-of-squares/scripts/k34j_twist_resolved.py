#!/usr/bin/env python3
# RESOLUTION of the twist puzzle!
# ellfromeqn(C1) = [0, 1016, 0, -288, -292608] — a DIFFERENT model from J_L
# [0,0,0,-27894240,56491485696], SAME j — and its traces MATCH the C1 point
# counts (ap = 0,0,4,0,6,-6,4,0 at 13..47 = exactly my ap_C1 values shifted?
# my Python: ap_C1 = -1(13), 1(23), 3(29), 1(31), 5(37), -5(41), 3(43), 1(47).
# gp ellap(C1model): 0, 0, 4, 0, 6, -6, 4, 0.
# ap(C1-pts) = ap(model) - 1?? 13: -1 vs 0: diff -1; 23: 1 vs 0: +1; 29: 3 vs 4: -1;
# 37: 5 vs 6: -1; 41: -5 vs -6: +1; 43: 3 vs 4: -1. Consistent ±1!!
# And ap(C1model from gp) = ap(JL) EXACTLY. So the Jacobian of C1 IS J_L
# (isomorphic, same Frobenius), but #C1(F_p) = p+1-ap(JL) ± 1?? 
# THE RESOLUTION: #C1(F_p) = p+1-ap(Jac) ONLY IF the quartic has a rational
# POINT AT INFINITY. C1: y^2 = 8x^4+1016x^2+9 — the leading coeff 8 is NOT a
# square, so C1 has NO rational point at infinity: the two points at infinity
# are DEFINED OVER Q(sqrt(8))! For such quartics:
#   #C1(F_p) = p+1-ap(Jac) - chi(8)*(...) — precisely: #C(F_p) = p+1-ap - (lead-coeff character correction).
# Standard fact: for odd degree quartic (one infinity point): #C = p+1-ap.
# For even degree: TWO infinity points rational iff lead coeff is a square;
# otherwise conjugate over Q(sqrt(lead)). Then #C(F_p) = p+1-ap - chi(a4)*2
# where chi = 1 if a4 square: correction = 0 or -2.
# My counts: p=29: #C1=27, p+1-apJL = 30-4=26?? mismatch 27 vs 26. Hmm.
# p=29: #C1=27 => ap_obs = 29+1-27 = 3. apJL=4. diff -1 — NOT ±2.
# The correct even-degree correction: #C(F_p) = p+1 - ap(J) - chi(delta)*2? Let me
# just accept the empirical: ap_obs = ap(JL) + delta_p with delta ∈ {0,±1}...
# p=13: 0-0=+(-1)? ap_obs=-1, apJL=0: delta=-1. p=23: +1-0=+1. p=29: 3-4=-1.
# p=37: 5-6=-1. p=41: -5-(-6)=+1. p=43: 3-4=-1. p=47: 1-0=+1. p=31: 1-0=+1.
# p=11: -1-0=-1. p=5: -1-0=-1. p=7 (bad): -7-(-1)=-6?? p=7 is BAD for J_L.
# delta = -chi2(238)? chi_2(238 mod p)=chi(238/p?)... 238=2·7·17. chi_2(2)=(-1)^{(p^2-1)/8}.
# p=13: chi2(2)=-1: delta=-1 ✓. p=23: chi2(2)=+1 (23≡±1 mod 8? 23≡7 mod 8: chi2(2)=1? 
# (2/p)=1 iff p≡±1 mod 8: 23≡7 mod 8 => (2/23)=1 ✓ delta=+1 ✓. p=29≡5 mod8: (2/29)=-1, delta=-1 ✓.
# p=37≡5 mod 8: (2/37)=-1, delta=-1 ✓. p=41≡1 mod 8: (2/41)=+1, delta=+1 ✓!!
# p=43≡3 mod 8: (2/43)=-1, delta=-1 ✓. p=47≡7 mod 8: +1, delta=+1 ✓. p=31≡7: +1 ✓.
# p=11≡3: -1 ✓. p=5≡5: -1 ✓.
# => ap_obs = ap(JL) + (2/p): the point-at-infinity character correction, EXACT.
# CONCLUSION: Jac(C1) = J_L (isomorphic); the count formula for even-degree
# quartics carries the (2/p) correction (the 2 points at infinity are rational
# iff 8 is a square mod p). Everything CONSISTENT — my earlier "mismatch" was
# the missing infinity correction, not a twist!
print("RESOLVED: Jac(C1) = J_L exactly. ap_obs = ap(JL) + (2/p).")
print("The correction is the two-points-at-infinity character (lead coeff 8).")
print()
print("=> The earlier Z-decomposition test must use the CORRECTED traces:")
print("   tZ(p) = p+1-#Z(F_p) = ap(JL,p) + ap(EZ,p) + (2/p)? Test now.")
# Z: y^2 = 8w^8+1016w^4+9, also even degree with lead coeff 8: same (2/p) correction!
def pow_set(p):
    return {k*k % p for k in range(p)}
def count(f, p):
    PS = pow_set(p)
    cnt = 1
    for x in range(p):
        v = f(x) % p
        cnt += 1 if v == 0 else (2 if v in PS else 0)
    return cnt
from math import isqrt
def chi2(p):
    r = pow(2, (p-1)//2, p)
    return -1 if r == p-1 else (1 if r == 1 else 0)
print("\np: tZ vs apJL+apEZ (+chi2):")
for p in (13, 23, 29, 31, 37, 41, 43, 47, 53):
    cntZ = 1
    for x in range(p):
        v = (8*pow(x,8,p) + 1016*pow(x,4,p) + 9) % p
        cntZ += 1 if v == 0 else (2 if v in pow_set(p) else 0)
    cntJ = 1; cntE = 1
    for x in range(p):
        vj = (x*x*x - 27894240*x + 56491485696) % p
        cntJ += 1 if vj == 0 else (2 if vj in pow_set(p) else 0)
        ve = (x*x*x + 1016*x*x + 576*x) % p
        cntE += 1 if ve == 0 else (2 if ve in pow_set(p) else 0)
    tZ = p+1-cntZ
    pred = (p+1-cntJ) + (p+1-cntE)
    print(f"  p={p}: tZ={tZ} pred(JL+EZ)={pred} pred+chi2={pred+chi2(p)} match(tZ==pred+chi2): {tZ==pred+chi2} match(tZ==pred): {tZ==pred}")