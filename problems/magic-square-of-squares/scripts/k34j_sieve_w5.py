#!/usr/bin/env python3
# W_5 = {w mod 5 : f(w) QR mod 5} has size 1 — WHICH class? If W_5 = {0},
# then every rational point has w ≡ 0 mod 5! Combined with other primes:
# w ≡ 0 mod 5 AND the point structure might force w = 0 exactly.
from fractions import Fraction as F
import math

def pow_set(p):
    return {k*k % p for k in range(p)}

def W(p):
    PS = pow_set(p)
    return sorted(w for w in range(p) if (8*pow(w,8,p) + 1016*pow(w,4,p) + 9) % p in PS)

print("W_5 =", W(5))
print("W_11 =", W(11))
print("W_29 =", W(29))
print("W_13 =", W(13))
# f mod 5: 8w^8+1016w^4+9 ≡ 3w^8+w^4+4. w=0: 4 = QR (2^2) ✓.
# w=1: 3+1+4=8≡3: non-QR. w=2: w^4=16≡1: 3+w^4+4 with w^2=4,w^4=1: 3+1+4=8≡3 ✗.
# w=3: w^2=9≡4, w^4=1: 3+1+4=8≡3 ✗. w=4: w^2=1,w^4=1: 3+1+4=3 ✗.
# So W_5 = {0} ONLY! Every rational point of Z has w ≡ 0 mod 5!!
# Then w = 5w1. Substitute: f(5w1) = 8*5^8 w1^8 + 1016*5^4 w1^4 + 9.
# For the y^2 equation: y^2 = 8*5^8 w1^8+1016*5^4 w1^4+9.
# mod 5: y^2 ≡ 9 ≡ 4 mod 25? Compute v5: y^2 = 9 + 5^4(8*5^4w1^8 + 1016 w1^4).
# v5(y^2) = 0 (since 9 ≢ 0 mod 5 and the rest is divisible by 5^4): y ≡ ±3 mod 5.
# No contradiction yet — w ≡ 0 mod 5 is allowed for rationals (w = 5w1).
# BUT: the point (w,y) on Z with w=5w1: does it descend? The map w->5w1 is just
# a rational point with w divisible by 5. Iterate: is w1 ≡ 0 mod 5 again?
# The condition was on w mod 5 only — w1 unconstrained. NO infinite descent from
# this alone. BUT combine with the QUOTIENT structure: w ≡ 0 mod 5 means the
# C1-point x = w^2 has x ≡ 0 mod 25 — and x_C1 = X^2 of the leaf fiber with
# X = r/s in lowest terms... X^2 ≡ 0 mod 25 => 5 | X => 5 | r (and 5 ∤ s? or both?).
# gcd(r,s)=1: 5|r. But the admissibility has 3|r, r even; 5|r is NEW info!
# Hmm wait — I need to recheck what maps where. C1 square-x point x=w^2 came
# from the C1 cover of J_L; the C1 point corresponds to a leaf fiber point
# (r,s,u) with X = r/s and N(X^2) square... and x_C1 = (s/r)^2-ish? The exact
# relation between x_C1 and X matters. If x_C1 = (s/r)^2, then w = s/r (a
# rational) and w ≡ 0 mod 5 => 5 | s (5 ∤ r since gcd=1). New: 5|s!
# Then the same valuation argument as 7-17: v5(238 r^4) = 0 — no odd-valuation
# contradiction (238 = 2·7·17, no factor 5). So 5|s is NOT killed by valuations.
# The sieve continues: w ≡ 0 mod 5 => 5|s. Other primes' W_p constrain w further.
print("\nW_5 = {0} => 5 | w (the numerator? w=a/b: w≡0 mod 5 with 5∤b => 5|a)")
print("w = s/r form: 5 | s. NOT a contradiction (238 has no factor 5).")
print("Next: iterate the sieve on other primes to shrink w's residue classes; if")
print("w must be divisible by INFINITELY many primes => w = 0 => contradiction.")
print("The densities product 1.9e-7 over p<=89 suggests the sieve has real power")
print("on bounded boxes, but 'w ≡ 0 mod p for all p' needs W_p = {0} at infinitely")
print("many primes — check which primes have W_p = {0}:")
special = []
for p in range(5, 300):
    if math.gcd(p, 6*238*5*35*17) != 1 and p not in (5,7,11,13,17,19,23,29,31,37,41,43):
        continue
    if p in (17,): continue
    if p < 5 or p in (17,): continue
    wp = W(p)
    if len(wp) <= 2:
        special.append((p, wp))
print("primes p<300 with |W_p| <= 2:", special[:20])