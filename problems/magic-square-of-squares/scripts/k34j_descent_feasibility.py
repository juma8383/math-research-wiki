#!/usr/bin/env python3
# While the L-series evaluates: the rigorous 2-Selmer route for Jac(P) needs
# Stoll's implementation. Check whether the PARI/GP version has any genus-2
# descent (e.g. via 'polredbest' no...). PARI has 'hyperellpadicfrobenius' and
# 'hyperellcharpoly' but NO genus-2 Selmer. Magma not available.
# The realistic unconditional completion: implement Gordon-Grant 2-descent
# manually? The 72 Type-I equations per d1..d4 quadruple over D4 (the 2^4
# d-product group) — for our curve the Weierstrass points: x=0 rational, and
# the 4 roots of N(x) over the splitting field (NOT all rational — disc has
# 7, 17 with inertia). The Gordon-Grant machinery REQUIRES all 5 Weierstrass
# points rational! N(x)'s roots: x^4-4x^3-604x^2-952x+56644 — the Galois group
# of the quartic: check whether all roots are rational: N(x) rational roots:
# tested ±small divisors of 56644 = 2^2·7·17·238? 56644 = 4·14161 = 2^2·7^2·17^2:
# rational root candidates ±{1,2,4,7,14,17,28,34,49,68,119,136,238,289,...}:
for_cands = [1,2,4,7,14,17,28,34,49,68,119,238,289,578,833,1666,2023,476,3332,4046,8092,14161,28322,56644]
def N(x): return x**4 - 4*x**3 - 604*x*x - 952*x + 56644
rational_roots = [c for c in for_cands if N(c) == 0 or N(-c) == 0]
print("rational roots of N(x):", rational_roots if rational_roots else "NONE")
# N has NO rational roots => the 4 non-zero Weierstrass points are not rational
# => the full rational-Weierstrass descent doesn't directly apply; the Galois
# descent from Q(J[2]) is needed (Gordon-Grant explicitly defer this).
# => the hand 2-descent is substantially harder than hoped.
# The remaining rigorous options:
# (a) numerical L(1) ≠ 0 with explicit error bounds (the approximate functional
#     equation with conductor bound: provable nonvanishing at working precision —
#     this IS accepted as rigorous when done carefully, e.g. via Dokchitser's
#     computel-style algorithms with interval arithmetic);
# (b) 2-descent over the Galois closure (heavy);
# (c) conditional on BSD (the wiki's standard flag).
# For the wiki: file the analytic rank 0 as "conditional on BSD/numerical",
# with the Coleman gate structured as conditional — honest flagging per protocol.
print()
print("Decision for the wiki: rank Jac(P) = 0 filed as ANALYTIC/CONDITIONAL")
print("(BSD-conditional), with the rigorous completion listed as: numerical")
print("L(1)-nonvanishing with error bounds (a), or Galois-descent 2-descent (b).")
print("The Chabauty-on-Z_D gate is then CONDITIONALLY closed pending that proof")
print("plus the Coleman computation itself. Honest status maintained.")