#!/usr/bin/env python3
# While waiting: also verify the Jac(P) vs Jac(Z_D) split at p=53, 59 etc.
# Actually re-verify the K=Q(sqrt(238)) claim robustly with more split primes
# using zd_product_test.gp-style data — extend to p=61..300 (split ones).
# The key data: Jac(P) charpoly at p in the SPLIT list must factor into two
# quadratics with rational-trace-like structure matching E_a/E_a-conjugate;
# at INERT primes the palindromic form. Already verified at 27 primes.
# Extra verification: at split prime 101: cpP = x^4-6x^3-14x^2-606x+10201:
# factors? (x^2+ax+101)(x^2+bx+101) with a+b = -6, ab+202 = -14 => ab = -216:
# a,b roots of z^2+6z-216 = 0: disc = 36+864 = 900: a,b = (-6±30)/2 = 12, -18.
# So traces: ap = -a = -12 and ap = -b = 18: Jac(P) at 101 = E1(ap=-12), E2(ap=18)?
# charpoly x^4 - 6x^3 - 14x^2 - 606x + 10201 = (x^2+12x+101)(x^2-18x+101):
# traces -12 and 18. apEa(101) = 10?? E_a ap(101) = 10 from jacP_vs_ea output.
# MISMATCH: factors' traces are -12 and +18, neither is 10!! So E_a does NOT
# match Jac(P) at 101 — E_a is NOT the factor (or the pair assignment differs
# per prime — impossible for a fixed curve E/K).
# => E_a was a coincidence at 6 primes; Jac(P)'s split-prime factor pair is
# (-12, +18) at 101, (-4,-4) at 23, (0,-2) at 29, (10,-10) at 37, (-6,-6) at 41.
# A FIXED E/K over K: ap(E, 23) and ap(E^σ, 23) = -4 both; ap(E,29)=(0 or -2);
# ap(E,37) = ±10; ap(E,41) = -6; ap(E,101) = -12 or 18.
# The pair (−12, +18) at 101: sum 6 ≠ 0: NOT palindromic — consistent with
# 101 being split (needs checking (238/101) = ?): 238 mod 101 = 36: (36/101) = +1
# (6^2/101): split ✓. The two traces -12, 18: for E/K and conjugate at split p:
# ap(E, 101) and ap(E^σ, 101) = the σ-conjugate's trace — genuinely different
# curves; both rational at split primes ✓ consistent with the Res structure.
print("p=101 consistency: Jac(P) factors' traces (-12, +18) — NOT a ±pair;")
print("this is FINE for Res(E/K): the conjugate curve has a different trace.")
print("The K = Q(sqrt(238)) identification stands (27/27); E/K's exact model")
print("still needs the descent. The analytic rank (model-independent) is running.")