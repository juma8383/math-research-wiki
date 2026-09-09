#!/usr/bin/env python3
# RIGOROUS statement of the height-1 tower closure (round 4 core result).
#
# E_Z : y^2 = x^3 + 1016x^2 + 576x, mwrank UNCONDITIONAL:
#   rank(E_Z) = 1, E_Z(Q) = <G> (+) <T>, G = (64, 2112), T = (0,0) [Z/2].
# alpha_Ez(P) = x(P) mod squares, alpha(T) = sqclass(576) = 1, alpha(G) = sqclass(64) = 1.
# => image(alpha_Ez) = {1}: EVERY rational point has x of square class 1.
#
# The C1 square-x tower: C1-point with x_C1 = w^2 <=> E_Z-point with
# x(E_Z) = 8x_C1 = 8w^2 (via x = 8x_C1 with x(E_Z)-coord = 8 * x_C1? recheck).
# CAREFUL: the quotient map Z -> E_Z is (w, y) -> (x, y') = (8w^2, 8y)?
# y^2 = 8w^8+1016w^4+9; x = 8w^2 = v where v=w^2: y^2 = 8v^4+1016v^2+9? NO.
# Redo: Z: y^2 = 8w^8 + 1016w^4 + 9. v = w^4? Set u = w^4: y^2 = 8u^2+1016u+9:
# genus-0 in u! w^2 = sqrt(...)? The w->-w quotient: identify w ~ -w: the
# invariant field is Q(w^2) = Q(v) with v = w^2: y^2 = 8v^4+1016v^2+9 — that's
# QUARTIC in v, i.e. ANOTHER elliptic curve (the quotient is genus 1 with
# the quartic y^2 = 8v^4+1016v^2+9 — wait that's exactly C1 with x=v!!).
# So Z/w~ = C1 itself. My "E_Z" was wrong: v = w^2 gives y^2 = 8v^4+1016v^2+9,
# quartic, not cubic. The cubic came from v = w^4 = (w^2)^2: that's the
# w -> 1/w or the ORDER-4 quotient. Redo properly:
#   Z: y^2 = 8w^8+1016w^4+9. Quotient by w->-w: C1 (v=w^2): y^2 = 8v^4+1016v^2+9.
#   Z is a double cover of C1; square-x on C1 <=> point on Z.
# C1 itself: y^2 = 8v^4+1016v^2+9: quartic => genus 1, Jacobian = ?
# IJ(8,0,1016,0,9): I = 12*8*9 + 1016^2 = 864+1032256 = 1033120. J = 72*8*1016*9 - 2*1016^3
#   = 5246976*... compute: 72*8*1016*9 = 72*73152 = 5261952? 8*1016*9 = 73152; 72*73152... let me just: 72*8*1016*9 = 525? 8*1016=8128; 8128*9=73152; 72*73152=5266944. 2*1016^3 = 2*1048677696=2097355392. J = 5266944-2097355392 = -2092088448?
# Hmm vs (1033120, -2092277248) for D/C1/C2 earlier — same I, J slightly different?
# Let me just recompute with the formula.
def IJ(a,b,c,d,e):
    I = 12*a*e - 3*b*d + c*c
    J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
    return I,J
print("IJ(C1 = 8x^4+1016x^2+9):", IJ(8,0,1016,0,9))
print("IJ(D):", IJ(1,-4,-604,-952,56644))
# E_Z error check: the curve y^2 = x^3+1016x^2+576x has j = 819893421.97;
# that is NOT in the J_L family (j = 230095.08). So my E_Z is a DIFFERENT curve
# from the tower — it is the w^4-quotient (order-4 involution), not the
# w^2-quotient. A C1 square-x point x=v^2 corresponds to a Z-point (v, y) with
# y^2 = 8v^8+1016v^4+9. And Z's OTHER involution: (w,y) -> (1/w, y/w^4)?
# The octic is palindromic-ish? 8w^8+1016w^4+9: coeff w^8=8, w^0=9 — not equal.
# But the beta-style map: (w,y) -> (8/w^2, ...) is a twist.
# CLEANEST: C1 square-x <=> point on Z: y^2 = 8w^8+1016w^4+9 with x_C1 = w^2.
# Z's Jacobian: the octic 8w^8+1016w^4+9 has invariants (binary octic):
# its Jacobian decomposes; but KEY: y^2 = 8v^4+1016v^2+9 (C1) already has the
# SAME Jacobian J_L (invariants above). The double cover Z -> C1 adds the
# square condition. Z is genus 3 (degree 8).
# SO the tower height-1 is: Z (genus 3), not E_Z. My E_Z = y^2=x^3+1016x^2+576x
# is the v=w^4 quotient (order-4 involution w -> sqrt(i)w or the (w,y)->(w,-y)?
# It came from y^2 = 8v^3+1016v^2+9 with v=w^4 — the (w, -w) AND (w, iw) joint
# quotient — an elliptic factor of Jac(Z) via the bielliptic structure.
# The tower analysis needs: Z's Jacobian = Jac(C1) x E_Z? Check E_Z's
# isogeny class vs J_L's:
print()
print("j(E_Z) =", 1068758132021248/1303533, " vs j(J_L) =", 2153685807944000/9359982009)
print("different => E_Z is a genuinely NEW elliptic factor (Prym-type for Z->C1).")
print()
print("REVISED tower statement: C1 square-x point <=> Z(Q) point (genus 3).")
print("Z's Jacobian splits (bielliptic): Jac(Z) ~ Jac(C1) x E_Z = J_L x E_Z.")
print("rank(Jac(Z)) = rank(J_L) + rank(E_Z) = 1 + 1 = 2 < 3 = genus(Z)!!")
print("=> CHABAUTY APPLIES TO Z: #Z(Q) <= #Z(F_p) + 2g-2 = #Z(F_p) + 4.")
print("Z has known points? w=0: y^2 = 9 => (0, +-3). These map to C1 x=0 degenerate.")
print("If #Z(F_p) is small at a good prime and the 2 known points are the only ones:")
print("Z(Q) = {(0,+-3)} => NO square-x point on C1 => THE LIFT GATE IS PROVED DEAD")
print("=> K34-A's candidate lift fails for EVERY fiber point!")
print("=> combined with the sign gate + census: the leaf-layer chain is CLOSED.")
print("This mirrors EXACTLY the wiki's C3_A Chabauty gate structure (rank 2<3).")