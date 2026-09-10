# mss_c3b_residue_13.sage -- the B-side residue filter at p = 13 (the second
# tight prime; #C3_B(F_13) filed as 20): same program as p=11.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== B13: C3_B at p = 13 ===')
def fB(x):
    return (9*x**8 - 92*x**6 + 310*x**4 - 92*x**2 + 9) % 13
sq13 = set((i*i) % 13 for i in range(13))
affine = []
for xv in range(13):
    val = fB(xv)
    if val == 0:
        affine.append((xv, 0))
    elif val in sq13:
        for s in range(13):
            if (s*s) % 13 == val:
                affine.append((xv, s))
out('  #C3_B(F_13) = 2 + %d = %d (filed 24 -> recheck: filed says 24 at 11,' % (len(affine), 2 + len(affine)))
out('   20 at 13? the filed table: 11->12? recheck against Addendum-2)')
out('=== B14: D_B(F_13) classes and pushes (J_LB(F_13)) ===')
JLB13 = EllipticCurve([0, 0, 0, -1935360, 1033371648]).change_ring(GF(13))
out('  #J_LB(F_13) =', JLB13.order())
dcls = []
for zv in range(13):
    val = (9*zv**4 - 128*zv**2 + 512) % 13
    if val == 0:
        dcls.append((zv, 0))
    elif val in sq13:
        for s in range(13):
            if (s*s) % 13 == val:
                dcls.append((zv, s))
out('  D_B(F_13) affine: %d' % len(dcls))
# base D1_B = (2, 12) mod 13 = (2, 12):
killed = 0
surv = []
for (zv, wv) in dcls:
    if (zv, wv) in [(2, 12)]:
        surv.append((zv, wv))
        continue
    if zv % 13 == 0:
        continue
    Xp = ((wv + 12) * pow(zv, -1, 13)) % 13
    rhs = (Xp**3 - 1935360*Xp + 1033371648) % 13
    if rhs in sq13 or rhs == 0:
        killed += 1
    else:
        surv.append((zv, wv, 'X=%d not on curve' % Xp))
out('  killed (finite on-curve pushes): %d' % killed)
out('  survivors/not-on-curve: %s' % surv)
out('=== DONE ===')