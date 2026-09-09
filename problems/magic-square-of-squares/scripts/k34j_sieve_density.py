#!/usr/bin/env python3
# Next front: deepen the Z_D sieve for the DEGENERATE-ORBIT closure itself.
# The sieve says: a Z_D(Q) point with w = a/b (lowest terms) must satisfy
# a/b mod p ∈ W_p for all p ∤ (b · 271-ish exclusions). For the degenerate
# orbit w = 0: a = 0. For non-degenerate: a ≠ 0. The sieve at each prime p
# imposes: a·b^{-1} ∈ W_p (p ∤ b) OR p | b (infinity allowed).
# A rational w with w ≡ ∞ mod infinitely many primes is impossible (b fixed).
# So for a non-degenerate point: b is divisible by NO prime p with the
# property "w ≡ ∞ forced"... actually b is a FIXED integer: only finitely
# many p divide it. For all other p: a/b ∈ W_p.
# The compound test for a candidate (a,b): check all p ≤ 499.
# The stronger structural question: can a ≠ 0 at all? The sieve density
# product over p ≤ 499: compute the survival density for a random a/b.
# If the density product is < 1/(any reasonable bound), the sieve is
# "conditionally exhaustive" — combined with a height bound it closes.
# Height-bounded closure: for b ≤ B, a ≤ A, the expected survivors = A·2B·ρ
# where ρ = product of densities. If A·2B·ρ < 1 for a provable (A,B) from
# a height bound (e.g. from the Coleman bound itself!), the sieve CLOSES.
# The Coleman bound gives #Z_D(Q) <= #Z_D(F_p) + 4 — a COUNT bound, not a
# height bound. Height bounds need elliptic logarithms... the honest loop:
# the sieve density is the quantitative input.
# Compute the density product over p <= 499 exactly:
from fractions import Fraction as F
import math

fD = lambda w, p: (pow(w,8,p) - 4*pow(w,6,p) - 604*pow(w,4,p) - 952*pow(w,2,p) + 56644) % p

def pow_set(p):
    return {k*k % p for k in range(p)}

def W(p):
    PS = pow_set(p)
    return {w for w in range(p) if fD(w, p) in PS}

rho = 1.0
details = []
for p in range(5, 500):
    if p == 17: continue
    wp = W(p)
    d = len(wp)/p
    rho *= d
    details.append((p, len(wp), round(d, 4)))
print("sieve densities (p, |W_p|, density):")
for d_ in details[:20]: print("  ", d_)
print(f"\nproduct density over p in [5,499] (excl 17): {rho:.3e}")
print(f"=> expected non-degenerate survivors in a box of N candidates: N·{rho:.3e}")
print(f"  (e.g. N = 10^6 candidates -> {1e6*rho:.2e} expected)")
print("The density compounds multiplicatively — the MW sieve on Z_D has real")
print("closure power for any height bound that becomes available.")