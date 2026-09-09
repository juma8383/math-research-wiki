#!/usr/bin/env python3
# Theory for the tower: C1's square-x condition as an alpha^L-fiber statement.
# C1: y^2 = 8x^4+1016x^2+9. A point with x = square: substitute x = w^2:
#   y^2 = 8w^8 + 1016w^4 + 9  — an OCTIC in w. Points on C1 with square-x
# correspond to rational points on the curve Z: y^2 = 8w^8+1016w^4+9.
# Genus of Z: degree 8 hyperelliptic => genus 3! By Faltings, Z(Q) is finite.
# The tower DOES close in principle: genus-3 curve, and its Jacobian is...?
# An 8th-degree even octic y^2 = 8w^8+1016w^4+9: bielliptic structure again —
# its Jacobian splits into elliptic factors, likely J_L-shaped again (the
# same (I,J) family at the octic level: this is the K34 structure repeating).
# The tower: height-0 = K34-A on E_a (square-X on M_A quartic), height-1 =
# square-x on C1 (genus 3), height-2 = ... Each lift adds a cover.
# KEY INSIGHT for the wiki: the tower question is a FINITE computation at
# each height (Chabauty on genus-3 Z, rank of its Jacobian). If the Jacobian
# of Z has rank < 3, Chabauty applies at a good prime — same machinery as
# the wiki's named C3_A gate!
# Compute Z's Jacobian decomposition: the octic y^2 = 8w^8+1016w^4+9 has
# involutions w->-w (quotient: y^2 = 8v^3+1016v^2+9 with v=w^2 — genus 1!)
# Actually y^2 = f(w^2) with f cubic: y^2 = 8v^3+1016v^2+9 IS the genus-1
# quotient E_Z: the cubic v-curve. Its invariants: a2=1016, a4=... 
# y^2 = 8v^3+1016v^2+9: NOT in Weierstrass form (v^3 coefficient 8).
# v = V/8? y^2 = V^3/64 + 1016V^2/64 + 9 => multiply: 64y^2 = V^3+1016V^2+576.
# Set y' = 8y: y'^2 = V^3+1016V^2+576 — Weierstrass! E_Z: y^2 = x^3+1016x^2+576.
print("The C1 square-x tower question at height 1 becomes: rational points on")
print("the genus-3 curve Z: y^2 = 8w^8+1016w^4+9.")
print("Its w->-w quotient is E_Z: y^2 = x^3+1016x^2+576 (x = 8w^2 = 8x_C1).")
print("A square-x point on C1 (x = w^2) <=> a point on E_Z with x/8 = w^2 ... ")
print("i.e. x(E_Z)/8 a square <=> x(E_Z) = 8 * square.")
print("Compute E_Z: j-invariant, torsion, rank, and the alpha-image for the")
print("square-class question. If rank(E_Z)=0: Z(Q) finite = computable ->")
print("the tower CLOSES at height 1 provably!")
E_Z = [0, 1016, 0, 576, 0]
print("E_Z:", E_Z)
# j = ... compute with integers:
a2, a4 = 1016, 576
# j = 1728*(4a4)^3 / (4a4^3+27a6^2)? for y^2 = x^3+a2x^2+a4x+a6 with a6=0:
# j = 256(a2^2-3a4)^3 / (a4^2(a2^2-4a4))
num = 256*(a2*a2-3*a4)**3
den = a4*a4*(a2*a2-4*a4)
import math
g = math.gcd(num, den)
print(f"j(E_Z) = {num//g}/{den//g} = {num/g/den*g if False else num/den:.6f}")
print(f"  compare j(J_L) = 2153685807944000/9359982009 = {2153685807944000/9359982009:.6f}")
print(f"  compare j(E_a) = 238328000/127449 = {238328000/127449:.6f}")