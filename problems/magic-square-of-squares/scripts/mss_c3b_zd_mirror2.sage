# mss_c3b_zd_mirror2.sage -- the C3_B mirror S4: full push computation.
# The v1 result had TWO surprises to resolve:
#  1. #C3_B(F_11) = 26, NOT the filed 24 — investigate (counting bug vs
#     filed error; the infinity points: leading coeff 9 = 3^2 square gives
#     TWO infinities, counted 4 base? my pts started at 4 — WRONG: 2
#     infinities for a square leading coeff, so pts started too high by 2).
#  2. The B-side push: J_LB(F_11) order 16 — the same 11-divisibility
#     filter on the B-side residue classes.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== B2b: C3_B count CORRECTED ===')
def fB(x):
    return (9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9) % 11
sq11 = set((i*i) % 11 for i in range(11))
affine = []
for xv in range(11):
    val = fB(xv)
    if val == 0:
        affine.append((xv, 0))
    elif val in sq11:
        for s in range(11):
            if (s*s) % 11 == val:
                affine.append((xv, s))
pts = 2 + len(affine)  # TWO infinity points (leading coeff 9 = 3^2)
out('  #C3_B(F_11) = 2 + %d = %d (filed 24: check)' % (len(affine), pts))

out('=== B3: the B-side D-classes and pushes ===')
# D_B : w^2 = 9z^4 - 128z^2 + 512 (z = the tower variable, x = z^2 on D_B):
# the C3_B affine points (x, W) map into D_B via the square condition — the
# same structure as A: the D_B classes at p=11: z-values with 9z^4-128z^2+512
# a square mod 11:
dcls = []
sq11b = set((i*i) % 11 for i in range(11))
for zv in range(11):
    val = (9*zv**4 - 128*zv**2 + 512) % 11
    if val == 0:
        dcls.append((zv, 0))
    elif val in sq11b:
        for s in range(11):
            if (s*s) % 11 == val:
                dcls.append((zv, s))
out('  D_B(F_11) affine points: %d' % len(dcls))
# the base point for the map: the filed known D_B point (2, ±12):
# 12 mod 11 = 1: the base D1_B = (2, 1)? The filed: D_B known point (2,±12):
# base at (2, 1) mod 11. The quartic->cubic map X = (w + w0)/z^2 with
# w0 = 1 mod 11 (the base point (2, 12) -> (2, 1)):
out('  base D1_B = (2, 1) mod 11; pushing classes:')
JLB11 = EllipticCurve([0, 0, 0, -1935360, 1033371648]).change_ring(GF(11))
for (zv, wv) in dcls:
    if zv % 11 == 0:
        out('   z=0: base fiber (the known degenerate (2,±12) has z=2?)')
        continue
    Xp = ((wv + 1) * pow(zv, -1, 11)) % 11
    on = False
    rhs = (Xp**3 - 1935360*Xp + 1033371648) % 11
    on = rhs in sq11b or rhs == 0
    out('   z=%d, w=%d: push X = %d (finite => killed unless O)' % (zv, wv, Xp))
out('=== DONE ===')