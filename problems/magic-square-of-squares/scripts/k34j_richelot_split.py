#!/usr/bin/env python3
# No match with rational-2-torsion (a,b small). Widen: general Weierstrass
# y^2 = x^3 + A x^2 + B x + C (4 K-coefficients = 8 rational params) is too
# wide; instead normalize by translations: any E/K has a model y^2 = x^3 + A x^2
# + B x + C; if E has a K-rational point it can be moved... the 2-torsion family
# assumed a rational point of order 2 — the Prym E/K may NOT have rational
# 2-torsion! Widen: y^2 = x^3 + A x + B with A, B in K (4 params: A0,A1,B0,B1),
# then y^2 = x^3 + A x^2 + B x + C would be 6 params (too wide).
# Try the short form first: y^2 = x^3 + A x + B, A = A0+A1 s, B = B0+B1 s.
# NOTE: any curve over K can be put in short form ONLY if 2 is invertible and
# char != 2,3 — always true over K. The a1=a2=a3=0 short form requires a
# K-rational point to translate to infinity — not always available!
# The full general Weierstrass form has 5 K-coefficients = 10 rational params:
# too wide for brute force. Instead: use Sage's EllipticCurve over K with the
# j-invariant matching! Compute j(E/K) from the Res data? The j-invariant is
# determined by the traces? Not directly.
# ALTERNATIVE (the right one): Richelot/2-isogeny decomposition of Jac(P):
# for a genus-2 curve with a rational Weierstrass point y^2 = x^5+..., there
# is a classical 2-isogeny Jac(P) ~ E1 x E2 IF the quintic has a rational
# quadratic factor structure... Actually the classical result: y^2 = x*g(x)
# with deg g = 4: the curve has TWO involutions iff g is of the form
# g = h(x)^2 - c*x^2 (a square plus c*x^2): then the curve covers
# E1: y^2 = x*(h(x) + sqrt(c) x) and E2: y^2 = x*(h(x) - sqrt(c) x) over
# Q(sqrt(c)). Compute: N(x) = x^4-4x^3-604x^2-952x+56644 = h(x)^2 - c*x^2?
# h quadratic: h = x^2+ux+v: h^2 = x^4 + 2u x^3 + (u^2+2v)x^2 + 2uv x + v^2.
# h^2 - N = (2u+4)x^3 + (u^2+2v+604)x^2 + (2uv+952)x + (v^2-56644).
# Need h^2 - N = c x^2: 2u = -4 => u = -2; 2uv + 952 = 0 => -4v = -952 => v = 238!
# v^2 - 56644 = 238^2 - 56644 = 56644 - 56644 = 0 ✓!! and c = -(u^2+2v+604) =
# -(4+476+604) = -1084. So N = h^2 + 1084 x^2 with h = x^2-2x+238.
# VERIFY: (x^2-2x+238)^2 + 1084x^2 =? x^4-4x^3-604x^2-952x+56644:
# (x^2-2x+238)^2 = x^4 - 4x^3 + (4+476)x^2 - 952x + 56644 = x^4-4x^3+480x^2-952x+56644.
# + 1084x^2 = x^4-4x^3+1564x^2-952x+56644 ≠ N (coefficient 1564 ≠ -604). ✗!
# So v = 238 gives c = -(480+604)... recompute: u^2+2v+604 with u=-2, v=238:
# 4 + 476 + 604 = 1084: h^2 - N = (2u+4)x^3 + (u^2+2v+604)x^2 + (2uv+952)x + (v^2-56644)
# = 0 + 1084x^2 + 0 + 0 = 1084x^2. So h^2 - N = 1084x^2 => N = h^2 - 1084x^2.
# CHECK: h^2 - 1084x^2 = x^4-4x^3+480x^2-952x+56644 - 1084x^2 = x^4-4x^3-604x^2-952x+56644 ✓!!
# YES! N(x) = (x^2-2x+238)^2 - 1084·x^2. THE STRUCTURE EXISTS!
# => P: y^2 = x*(h^2 - 1084x^2) with h = x^2-2x+238: the two involutions:
# P covers E±: over Q(sqrt(1084)) = Q(sqrt(271)): y^2 = x(h ± sqrt(1084) x).
# Over Q: Jac(P) ~ Res(E1/Q(sqrt(271)))?? Wait — the ±pair splitting field was
# K = Q(sqrt(238)), not Q(sqrt(271))... but the 2-isogeny class: the curves
# E±: y^2 = x(h ± sqrt(1084)x) are defined over Q(sqrt(271)); their Jac pair
# over Q... hmm the correct classical statement: for y^2 = x(g^2 + d·x^2)-type
# (d a square times?), Jac splits into E1 x E2 over Q when the form is
# y^2 = x·(quadratic in x)^2 - d·x^3: the two elliptic curves:
# E1: y^2 = x(h(x) + x·sqrt(d))... over Q if d is a square; over Q(sqrt(d)) otherwise.
# Our d = -1084 = -4·271: sqrt(-1084) = 2·sqrt(-271): the splitting field of the
# INVOLUTION is Q(sqrt(-271)). But we measured K = Q(sqrt(238))!? Both structures
# can coexist: the ±pair (t,-t) at 11 primes suggests the splitting over ONE field;
# the (t,t) pairs at 23, 41 suggest splitting over another. Two different
# involutions: one over Q(sqrt(271)), one over Q(sqrt(238))? A genus-2 curve has
# at most... it can have multiple involutions (bielliptic). VERIFY: E1: y^2 =
# x(h + 2 sqrt(-271) x) over Q(sqrt(-271)): compute its ap at a few primes and
# compare with the P-factor data!
print("N(x) = (x^2-2x+238)^2 - 1084x^2 with 1084 = 4*271: VERIFIED")
print("=> P: y^2 = x(h^2 - 1084x^2), h = x^2-2x+238")
print("=> Jac(P) splits over Q(sqrt(-271)) into E±: y^2 = x(h ± 2sqrt(-271)x)")
print("The pair E± are quadratic TWISTS of each other by -271!")
print("Their traces at split primes of... the base field is Q(sqrt(-271)): a")
print("curve and its twist by the character of Q(sqrt(-271))/Q? no — E± are")
print("conjugate over Q(sqrt(-271)), defined over it. Their Jac over Q(sqrt(-271))")
print("... but Jac(P) over Q = Res? The measured K was Q(sqrt(238)) — different!")
print("Resolution: Jac(P) over Q is SIMPLE; over Q(sqrt(-271)) it splits E+ x E-;")
print("over Q(sqrt(238)) it ALSO splits (as any simple surface splits over some")
print("quadratic field if it has a 2-isogeny structure). The measured K = the")
print("SMALLEST splitting field = Q(sqrt(238)).")
print("NEXT: construct E+ over Q(sqrt(-271)) and test its ap against the P-data!")