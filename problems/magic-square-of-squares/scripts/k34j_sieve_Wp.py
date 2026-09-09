#!/usr/bin/env python3
# The MW sieve on Z: compute W_p = {w mod p : f(w)=8w^8+1016w^4+9 is a QR mod p}
# for p up to ~200, and the CRT structure. The rational w of a non-degenerate
# Z(Q) point must reduce into W_p at every p. Key: w mod p ∈ W_p with the
# SAME w for all p — CRT on the allowed residue classes.
from fractions import Fraction as F
import math

def pow_set(p):
    return {k*k % p for k in range(p)}

def W(p):
    PS = pow_set(p)
    return [w for w in range(p) if (8*pow(w,8,p) + 1016*pow(w,4,p) + 9) % p in PS]

print("p | |W_p| | density | note")
tot_density = 1.0
sets = {}
for p in (5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97):
    if p in (17,):  # bad for f? f mod 17: 8w^8+1016w^4+9 ≡ 8w^8+... 1016 = 59*17+... 1016 mod 17 = 1016-59*17=1016-1003=13; fine, include
        pass
    wp = W(p)
    sets[p] = set(wp)
    dens = len(wp)/p
    tot_density *= dens
    print(f"{p:>3} | {len(wp):>2} | {dens:.3f}")
print(f"\nproduct of densities over p<=89: {tot_density:.2e}")
# The sieve: for a rational w = a/b (a,b ints, gcd=1), the condition is:
# f(a * b^{-1}) QR mod p for all p ∤ (b · disc?) — when p | b, w ≡ ∞ mod p:
# handle separately (the leading-coefficient character).
# The CRT sieve: start with w mod M1 = 5, allowed = W(5); lift through primes
# maintaining the allowed residue set; if it becomes empty => NO rational w.
# But w can be huge; the sieve must run on w as an integer with the
# observation that a Z(Q) point's w is a FIXED integer pair (a,b).
# Standard MW-sieve: for each prime, allowed classes mod p for the RATIO.
# Compute the survivor density; if densities compound to < 1/|search box| for
# reachable boxes, the search space is provably empty in range.
# Quick check: which p have W_p very small?
smalls = [(p, len(W(p))) for p in (5,7,11,13,19,23,29,31,37,41,43)]
print("\nsmallest |W_p|:", sorted(smalls, key=lambda t: t[1])[:5])