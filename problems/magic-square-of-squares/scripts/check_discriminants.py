# check_discriminants.py -- verify the discriminants filed in notes.md 2i
# against the full general-Weierstrass discriminant formula (sympy, exact).
# General curve: y^2 = x^3 + a2 x^2 + a4 x  (a1=a3=a6=0)
#   b2=4a2, b4=2a4, b6=0, b8=-a4^2
#   Disc = -b2^2*b8 - 8*b4^3 - 27*b6^2 + 9*b2*b4*b6
#        = -16*a2^2*a4^2 + 64*a4^3
# (a6=0 kills the -27b6^2 and +9b2b4b6 terms; b8 = -a4^2 exactly)
# For tE_A: a2=-256, a4=18432 -> Disc = -16*256^2*18432^2 + 64*18432^3
# For tE_B: a2= 256, a4=-2048 -> Disc = -16*256^2*2048^2 - 64*2048^3
# Compare with the values filed in notes.md 2i:
#   Delta(tE_A) = 10019299708108800
#   Delta(tE_B) =   118197499985920
from math import prod
from sympy import factorint

def disc(a2, a4):
    b2 = 4*a2; b4 = 2*a4; b6 = 0; b8 = -(a4*a4)
    return -(b2*b2*b8) - 8*(b4**3) - 27*(b6**2) + 9*b2*b4*b6

out = []
for (a2, a4, filed, label) in ((-256, 18432, 10019299708108800, "tE_A"),
                               ( 256, -2048,   118197499985920, "tE_B")):
    D = disc(a2, a4)
    # minimal model: common 2^? reduction — u-division by u means x->u^2 x:
    # a2 -> a2/u^4? no: for short-ish form the change (x,y)=(u^2 X, u^3 Y)
    # gives a4 -> a4/u^4, a2 -> a2/u^2, disc -> disc/u^12.
    # Find the largest u with u^2 | a2 and u^4 | a4.
    u = 1
    while a2 % (u+1)**2 == 0 and a4 % (u+1)**4 == 0:
        u += 1
    Dmin_theory = D // (u**12) if D % u**12 == 0 else None
    out.append((label, D, u, Dmin_theory, filed))

print("formula: Disc = -16*a2^2*a4^2 + 64*a4^3 (for y^2=x^3+a2x^2+a4x)")
for label, D, u, Dmin, filed in out:
    print(f"{label}: full Disc = {D}")
    print(f"   u-max (x->u^2 x reduction) = {u}, Disc/u^12 = {Dmin}")
    print(f"   filed in notes 2i: {filed}  match: {D == filed}")
    print(f"   factors of full Disc: {factorint(D)}")