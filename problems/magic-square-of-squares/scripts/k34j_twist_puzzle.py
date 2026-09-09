#!/usr/bin/env python3
# ap(C1) = ap(JL) - 1 at p=29,37,43,53,59,61,67? apC = apJ - 1 at 29,37,43,53,59,61,67 (4-1=3,6-1=5,4-1=3,8-1=7,6-1=5,12-1=11,6-1=5) YES
# at 41,71: apC = apJ + 1 (-5 vs -6: apC=-5, apJ=-6, apC = apJ+1 YES; -7 vs -8: apC=apJ+1 YES)
# at 5,7,11,13,23,31,47: apJ=0 but apC=-1,1,-1,-1,1,1,1 -> not ±0.
# Pattern: apC = apJ ± 1 with sign flips, and apJ=0 -> ±1?? That's NOT a twist
# (twists preserve 0). This looks like the trace of a DIFFERENT genus-1 quotient
# or... wait. apC = apJ - chi(p)*1? chi at 13: -1 (apC=-1, apJ=0): can't be chi*apJ.
# New idea: apC vs apJ differ by exactly 1 in absolute value EXCEPT at the
# '0' primes where apC = ±1. This is the signature of a GENUS-2 curve? No...
# Actually: ap(C1's Jacobian) vs ap(JL): -1 vs 0, -7 vs -1 (p=7: apJ=-1?? apJ=-1
# means #JL(F7)=9; but 7 is a BAD prime for J_L (7 | disc!) — bad primes {2,3,7,17}.
# Restrict to good primes of J_L: {5? no wait 5 is good}. Good primes: all except 2,3,7,17.
# At good primes 29..71 the pattern apC = apJ ∓ 1 — this is EXACTLY the relation
# between an elliptic curve and its QUADRATIC TWIST at primes where... no, twist
# gives apC = chi(p) apJ (multiplicative, preserving zeros).
# apC = apJ ∓ 1 consistently = the signature of a 2-ISOGENY difference? No.
# Hmm: apC - apJ ∈ {+1, -1} alternating? 29:+(-1)? apC=3,apJ=4: -1. 37: 5,6: -1.
# 41: -5,-6: +1. 43: 3,4: -1. 53: 7,8: -1. 59: 5,6: -1. 61: 11,12: -1. 67: 5,6: -1.
# 71: -7,-8: +1.
# apJ=0 primes (13,23,31,47): apC = -1,+1,+1,+1: the "±1" is chi_2(p)*(-1)^?
# This is the trace of a curve whose H^1 is Jac(C1) = J_L's twist by a character
# that also has a component at primes splitting 2... OR my J_L model is the wrong
# twist direction for the JACOBIAN (ellfromeqn's cubic is not the Jacobian!).
# CLASSICAL FACT: the Jacobian of y^2 = quartic with invariants (I,J) is
# y^2 = x^3 - 27Ix - 27J — I verified j matches for D (mwrank confirmed rank on
# that cubic and ellfromeqn gave the same j). For C1 the same (I,J) gives the
# same cubic — but the natural map C1 -> cubic differs by the quartic's twist!
# The resolution: Jac(C1) is ISOMORPHIC to Jac(D) = J_L as a curve, but the
# Frobenius on Jac(C1) differs because... no, Frobenius is intrinsic to the curve.
# UNLESS: ellfromeqn's output for C1 is NOT [0,0,0,-27894240,56491485696]!
# Check: ellfromeqn(C1) — compute in PARI. That's the missing verification.
print("Check ellfromeqn(C1) directly — the Jacobian model may differ by a twist.")
print("If j matches but ap differs, C1's Jacobian = quadratic twist of J_L with")
print("apC = chi(p)*apJ... but apJ=0 -> apC=0 contradiction. So the (I,J)→Jacobian")
print("map must be applied with the correct TWIST normalization per quartic.")
print("Run: gp ellfromeqn on C1 and compare its ap-traces.")