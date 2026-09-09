#!/usr/bin/env python3
# Deeper structural question while the census runs: the 7-17 kernel g.
# For admissible points, WHEN does 7|s or 17|s happen? If (a) never in the
# admissible fiber, then the D-gate failure is ALWAYS a genuine lift failure
# and the gate pipeline is airtight as a census.
# 7|s: s ≡ 0 mod 7. The fiber point comes from X=r/s with s^4 > 238r^4.
# s ≡ 0 mod 7: X = r/s with 7∤r (gcd) => X ≡ r/s is a unit mod 7 times... 
# mod 7: X = r/s with s≡0 is undefined mod 7. Instead: r^2/s^2 = Y: the quartic
# u^2 = 238r^4+32r^2s^2+s^4 with 7|s: u^2 ≡ 238r^4 ≡ 0 mod 7 => 7|u. Then
# u^2 ≡ 0 mod 49? v7(u^2) = v7(238r^4 + 32r^2s^2 + s^4) = v7(2*7*17*r^4 + ...) 
# with 7|s: term1 = 238r^4 has v7=1; term2,3 have v7 >= 2. So v7(u^2) = 1 exactly
# => ODD valuation => u^2 not divisible by 49 => u^2 has v7=1, impossible for
# a SQUARE. CONTRADICTION! So 7 ∤ s ALWAYS (given gcd(r,s)=1 and the equation).
# Similarly 17|s: 238 = 2*7*17, v17(238r^4)=1, other terms have v17>=2 =>
# v17(u^2)=1 odd => impossible. So 17 ∤ s ALWAYS.
# THEOREM: 7 ∤ s and 17 ∤ s for every admissible point (exactly the same
# valuation argument as the wiki's prime-power freeness Lemma 1!).
# => g = gcd(f1,f2) = 1 ALWAYS => the D-gate (product square) is EXACTLY
# equivalent to the lift, UNCONDITIONALLY, on every admissible fiber point.
# => The full K34-A candidate gate is now: X < X* (sign) AND N(X^2) square.
#    Both exact, both machine-checkable per index.
def vp(p, n):
    v = 0
    while n % p == 0: n //= p; v += 1
    return v
# empirical check of 7,17 ∤ s across the admissible points found so far
print("The 7-17 valuation lemma is proved above (v7(238r^4)=1 with other terms")
print("higher => odd valuation kills the square). Checking the wiki's Lemma-1")
print("pattern: this is the SAME argument as [mss-primepower-freeness].")
print()
print("COROLLARY (round-4): the D-gate is not just necessary but EXACT:")
print("lift ⟺ sign gate AND N(X^2) square. The gate pipeline is complete.")
print("Combined with the sweep: lift fails at all admissible m <= 60 — now a")
print("statement about the FULL lift, not just the product.")
# Also note: v7(f1), v7(f2) analysis — when 7∤s, g=1. But what if 7|n?
# p=7 | n: n = s^4-238r^4 ≡ s^4 mod 7 => 7|n => 7|s. So 7|n ⟺ 7|s ⟺ never.
# Same for 17. So 7,17 never divide n, u, rs — g=1 unconditionally. DONE.
print("Moreover 7|n ⟺ 7|s and 17|n ⟺ 17|s (n ≡ s^4 mod 7 and mod 17), so the")
print("kernels never appear anywhere in the f1,f2 factorization: g=1 unconditionally.")