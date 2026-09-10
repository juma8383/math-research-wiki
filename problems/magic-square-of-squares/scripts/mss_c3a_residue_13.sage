# mss_c3a_residue_13.sage -- the A-side residue filter at p = 13 (the second
# tight prime; #C3_A(F_13) = 8 from the §2aa table): the same program.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== A13: C3_A at p = 13 ===')
def fA13(x):
    return (x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1) % 13
sq13 = set((i*i) % 13 for i in range(13))
affine = []
for xv in range(13):
    val = fA13(xv)
    if val == 0:
        affine.append((xv, 0))
    elif val in sq13:
        for s in range(13):
            if (s*s) % 13 == val:
                affine.append((xv, s))
out('  #C3_A(F_13) = 2 + %d = %d (filed: 8)' % (len(affine), 2 + len(affine)))
out('=== A14: the D-classes and pushes (J_L(F_13)) ===')
JL13 = EllipticCurve([0, 0, 0, -27894240, 56491485696]).change_ring(GF(13))
out('  #J_L(F_13) =', JL13.order())
# the D-side classes: x = w^2 with W^2 = D(x) = x^4 - 4x^3 - 604x^2 - 952x + 56644:
dcls = []
def D13(x):
    return (x**4 - 4*x**3 - 604*x**2 - 952*x + 56644) % 13
for xv in range(13):
    val = D13(xv)
    if val == 0:
        dcls.append((xv, 0))
    elif val in sq13:
        for s in range(13):
            if (s*s) % 13 == val:
                dcls.append((xv, s))
out('  D(F_13) affine: %d' % len(dcls))
# base D1 = (0, 238) mod 13 = (0, 4):
killed = 0
excep = []
for (xv, Vm) in dcls:
    if xv % 13 == 0:
        if Vm == 4:
            excep.append((xv, Vm, 'D1 itself - O'))
        else:
            excep.append((xv, Vm, 'the T pair (involution)'))
        continue
    Xp = ((Vm + 4) * pow(xv, -1, 13)) % 13
    rhs = (Xp**3 - 27894240*Xp + 56491485696) % 13
    if rhs in sq13 or rhs == 0:
        killed += 1
    else:
        excep.append((xv, Vm, 'X=%d not on curve' % Xp))
out('  killed (finite on-curve): %d' % killed)
out('  exceptions: %s' % excep)
out('=== DONE ===')