from fractions import Fraction as F
import math

# Establish the quartic->Jacobian map for D and locate the class-238 fiber.
# Standard theory (mwrank's els convention): for E : y^2 = x^3 + a x^2 + b x,
# the els-class d cover is y^2 = d x^4 - 2a x^2 z^2 + (a^2-4b)/d z^4 ... 
# our D has a different shape (it came from N(x) with b=83589408-form).
# DIRECT approach: find the explicit degree-2 map D -> J_L by matching invariants
# via a Mobius/translation on x. D has rational point (0, 238).
# Classical: quartic y^2 = a x^4+b x^3+c x^2+d x+e with point (0, v0):
#   substitute x = v0*u/(...)? Use the algorithm: send (0,v0) to the point at
#   infinity; the resulting cubic has rational 2-torsion.
# Simpler: use PARI ellfromeqn on D and find the isomorphism to J_L numerically,
# then map (-33/2, 5/4) -> J_L point and identify its alpha^L class.
# We already know ellfromeqn gives SOME model; its Jacobian = J_L (by invariants).
# Actually let's get the iso via ellfromeqn + elltocompact... use gp instead.
print("Use PARI for the map. Python-side: check alpha^L-image membership of the")
print("point D=(-33/2,5/4) indirectly: J_L(Q)=<G_L>(+)<T>, so the point maps to")
print("n*G_L (+T). Its alpha^L class is then determined by n mod 2 and T-shift.")
# The quartic D point (0,238) is the degenerate point: it maps to T (alpha^L = 64498-class)
# or to O. The nontrivial point (-33/2,5/4) then maps to either G_L-class (238) or
# G_L+T (271). Either way: D IS SOLUBLE (as we found).
# Consequence for the lift gate: the gate quartic D is soluble BUT its points
# may all fail the x>0 square condition. That condition is exactly:
#   x on D is a positive rational square <=> ...
# So the gate is NOT closed by rank-0; it's a rank-1 situation again, and the
# question becomes: does the rank-1 orbit of D contain a point with x a positive
# square? This is EXACTLY parallel to the K34-A question itself on E_a (X(nG)=w^2).
# Structural conclusion: the lift gate D is another copy of the same problem type
# (quartic + rank-1 Jacobian + square-x condition), NOT a free-standing kill.
print("\n== Structural verdict ==")
print("D soluble (found (-33/2, 5/4)); rank(J_L)=1 unconditional (mwrank).")
print("The K34-A lift gate reduces to: does D(Q) contain a point with x = (s/r)^2,")
print("i.e. x a positive square != 0? Same shape as K34-A's own gate X(nG)=w^2 on E_a.")
print("The 238-recurrence: alpha^L image <238,271>; D's x=0 degenerate point maps into")
print("the T-coset. The x=(s/r)^2 condition singles out ONE alpha^L-fiber (class to identify).")