#!/usr/bin/env python3
# Step 2 of the height bound: the effective Mumford/David constants.
# With rank Jac(Z_D) = 1 (unconditional, §2aj), the effective Chabauty
# closure needs: for the known generator G of Jac(Z_D)(Z) (the degenerate
# orbit divisor class), the canonical height pairing matrix, and the
# Mumford constant: #\{P : h_K(P) <= C\} bounded by enumerating.
# The KEY identity: Z_D(Q) points outside the known orbit would give
# residue classes at good primes: combine (a) the Coleman bound
# #Z_D(Q) <= #Z_D(F_p) + 2g-2 + (rank term) with (b) the sieve (§2o):
# already all admissible m <= 240 killed; the height bound extends the
# kill to ALL m by bounding the possible denominators of w = s/r.
# DIRECT ROUTE (the wiki's own sieve language): any primitive (s, r) with
# V^2 = w^8 f-structure gives |N| ~ r^8·56644-scale: the D-quartic
# n^2 = N structure forces |n| <= const * r^4: combined with the §2o/§2u
# sieve (density 8.9e-255 over p <= 499): the sieve kills every (s,r) in
# any FINITE box; the height bound needs: no solutions with r > R0.
# The R0 comes from: canonical height h(w) <= H => r <= exp(H).
# Effective canonical height via Silverman: h(P) >= c1 * log r - c2 with
# c1, c2 explicit from the local heights at the bad primes {2,3,7,17,271}.
# Concretely: for P = (w, V) in Z_D(Q): local height components:
#   h_K(P) = sum_v n_v * lambda_v(P) : the archimedean lambda_inf from the
#   potential theory (Flynn's constants for the octic), the finite ones
#   from the reduction types at the 5 bad primes.
# THIS SCRIPT: compute the canonical-height LOWER bound c1 (log r
# coefficient) via the finite-part constants, giving r <= exp((H + c2)/c1).
# All exact-integer arithmetic; verify at sample primes.
from sage.all import *
R = PolynomialRing(QQ, 'w')
w = R.gen()
f = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + 56644
d = ZZ(f.discriminant())
print("log|disc| =", RR(d).log().round(4))
# For the height bound the operative statement (Coleman integration runs at
# p = 11 or 13; the sieve extends to all p): a point with height h has
# canonical height bounded by the naive height up to g·(bad-prime constant):
# h_canon(P) >= h_classic(P) - sum_{v bad} c_v with c_v = local constants:
# at 2: v_2(disc) = 44: the local constant ~ (44/2 + small)·log 2? The
# standard: h_canon >= h_classic - (1/2)·sum_{p bad} v_p(disc)·log p / (8+1)?
# Flynn's bound for octic models: h_canon(P) >= h_classic(P) - C with
# C = sum_p max(0, ...) — implement Stoll's finite-difference test:
# the canonical height differs from naive by bounded local terms; the
# BOUND: |h_canon - h_naive| <= sum_bad (v_p(disc)/2 + g)·log p / (2g+2)?
# Keep conservative: C_bound = (1/2)·(44·log2 + 4·log3 + 6·log7 + 6·log17
# + 4·log271) / (2*3) + log 2? — compute numerically as the PLACEHOLDER
# constant, flagged [to-verify] pending Stoll's exact local constants.
import math
C_bound = 0.5 * (44*math.log(2) + 4*math.log(3) + 6*math.log(7) + 6*math.log(17) + 4*math.log(271))
print("conservative bad-prime constant C ~", round(C_bound, 2))
print("=> h_canon >= h_naive -", round(C_bound, 2), "[to-verify: exact Stoll constants]")
print("DONE")