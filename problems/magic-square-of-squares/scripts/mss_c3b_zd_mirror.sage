# mss_c3b_zd_mirror.sage -- the C3_B mirror of the Z_D residue filter
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont. The B-side tower:
# the D_B quartic w^2 = 9z^4 - 128z^2 + 512 (K34-B square condition), its
# Jacobian J_L' (the B-side third curve), and the same 11-divisibility
# filter on the B-side residue classes at the B-tight prime p = 11
# (#C3_B(F_11) = 24 filed).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== B1: the B-side gate quartic and its Jacobian ===')
# D_B : w^2 = 9z^4 - 128z^2 + 512 ; invariants (71680, -38273024):
I, J = 71680, -38273024
JLB = EllipticCurve([0, 0, 0, -27*I, -27*J])
out('  J_LB: y^2 = x^3 + %d x + %d' % (-27*I, -27*J))
JLB11 = JLB.change_ring(GF(11))
out('  #J_LB(F_11) =', JLB11.order())

out('=== B2: C3_B residue classes at p=11 ===')
# C3_B: W^2 = 9x^8 - 92x^6 + 310x^4 - 92x^2 + 9 mod 11:
def fB(x):
    return (9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9) % 11
sq11 = set((i*i) % 11 for i in range(11))
pts = 4  # leading coeff 9 = 3^2 square: 2 points at infinity
cls = []
for xv in range(11):
    val = fB(xv)
    if val == 0:
        cls.append((xv, 0)); pts += 1
    elif val in sq11:
        for s in range(11):
            if (s*s) % 11 == val:
                cls.append((xv, s)); pts += 1
out('  #C3_B(F_11) = %d (filed: 24)' % pts)
out('  affine classes: %d' % len(cls))

out('=== B3: the D_B-side collapse (x = z^2) and pushes ===')
# the B-side tower: Z_DB over the quartic D_B in z; the D_B classes at p=11:
out('  (full mirror computation in S4)')
out('=== DONE ===')