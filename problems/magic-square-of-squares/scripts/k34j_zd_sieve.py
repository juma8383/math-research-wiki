#!/usr/bin/env python3
# MAJOR: the mod-5 sieve (W_5 = {0} — PROVED by direct QR computation mod 5)
# forces 5|w for any Z(Q) point, hence 5|s for any leaf fiber point passing
# the lift. ALL 13 alive admissible points (m=8..60) have 5∤s — ALL DEAD.
# This is a PROVABLE kill (W_5 = {0} is a finite exact computation, not a census).
# Now: is this a FULL proof structure? The sieve argument needs:
#   Z(Q) non-degenerate point (w≠0) => w ≡ 0 mod 5 => 5|s.
#   All admissible alive fiber points have 5∤s => their lifts fail.
#   For the FULL K34-A closure: need "every admissible fiber point fails the
#   lift" — the mod-5 condition handles alive points with 5∤s. Points WITH
#   5|s would need deeper analysis — but note 5|s combined with the fiber
#   structure: the m=2 fiber had 5∤s... do ANY admissible fiber points have
#   5|s? Census to m=240 showed 0 with 5|s? Check: (the direct_lift log has
#   v7s/v17s but not v5s). Extend: compute s mod 5 for all admissible m<=240.
# ALSO: the mod-5 condition is on Z-points; the lift gate quartic D x=(s/r)^2
# connection: D(Q) point with x=(s/r)^2 <=> Z(Q) point (w,y) with w = s/r?
# VERIFY this correspondence exactly (it's the tower structure): the D-point
# (x, V) with x = w^2 and V = y? The C1 quartic is y^2 = 8x^4+1016x^2+9 and
# the gate quartic is V^2 = N(x) with x=(s/r)^2. C1 and D have the same
# Jacobian but are DIFFERENT quartics (D is not C1!). Let me recheck which
# quartic the gate is: §2k: the lift ⟺ N((s/r)^2) = square: the quartic
# D: V^2 = N(x). C1: y^2 = 8x^4+1016x^2+9 is a DIFFERENT quartic (the class-1
# fiber of alpha^L). The Z curve I built (y^2=8w^8+1016w^4+9) = C1's square-x
# tower, NOT D's! For D: the square-x tower is y^2 = N(w^2) = 8w^16... no:
# D-square-x tower: V^2 = N(w^2) with w = s/r: V^2 = w^8-4w^4... compute:
# N(w^2) = w^8 - 4w^4·? N(x)=x^4-4x^3-604x^2-952x+56644; N(w^2) = w^8-4w^6-604w^4-952w^2+56644.
# So the D-tower curve is Z_D: V^2 = w^8-4w^6-604w^4-952w^2+56644 (genus 3).
# The W_5 = {0} computation was for the C1-tower f=8w^8+1016w^4+9, NOT for
# Z_D! The mod-5 gate applies to the C1-tower. For Z_D, compute W_5 for
# Z_D: f_D(w) = w^8-4w^6-604w^4-952w^2+56644 mod 5: = w^8 + w^6 + w^4 - 2w^2 + 4
# (−604≡1, −952≡−2≡3, 56644≡4, −4≡1 mod 5). Compute W_5 for Z_D now.
print("CORRECTION in progress: the mod-5 sieve was computed for the C1-tower")
print("octic 8w^8+1016w^4+9, but the lift-gate tower is Z_D: w^8-4w^6-604w^4-952w^2+56644.")
print("Recompute W_5 for Z_D before claiming the gate:")
def pow_set(p):
    return {k*k % p for k in range(p)}
def W(p, f):
    PS = pow_set(p)
    return sorted(w for w in range(p) if f(w) % p in PS)
fD = lambda w: pow(w,8) - 4*pow(w,6) - 604*pow(w,4) - 952*pow(w,2) + 56644
for p in (5, 7, 11, 13, 19, 23, 29):
    print(f"W_{p}(Z_D) = {W(p, fD)}")
# also for completeness the relation: is the D-tower curve even the right object?
# The lift ⟺ N((s/r)^2) square ⟺ the point (w=s/r, V) on Z_D: V^2 = N(w^2).
# So YES, Z_D is the right object, and its W_5 may differ!