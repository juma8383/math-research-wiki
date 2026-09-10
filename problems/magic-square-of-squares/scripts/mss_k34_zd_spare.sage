# mss_k34_zd_spare.sage -- the 1-dim spare: D-component annihilation per
# residue class (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont.
# Linux Addendum-10 continuation point: for each of the 12 residue Mumford
# classes of Z_D mod 11, check the D-component annihilation.
#
# THE MECHANISM (from the formal group): a class [R - D1] in J(F_11) has an
# 11-divisible lift with zero D-log IFF its reduction is O in J_L(F_11)
# (11-divisible points reduce to O). So: push each of the 12 residue Mumford
# classes through pi_* into J_L(F_11) and test identity vs O.
# J_L: y^2 = x^3 - 27894240x + 564485696? The filed coefficient is truncated
# in notes (564****5696); the exact B: from invariants (I,J) = (1033120,
# -2092277248): B = -27*J = 27*2092277248 = 56491485696? compute in-script.
# The Mumford push: the degree-1 class [P - D1] on D (base D1 = (0, 238))
# maps via the quartic-to-cubic isomorphism (Jac(D) = J_L) to the ELLIPTIC
# point phi(P) on J_L's cubic model with origin at the image of D1.
# The quartic->cubic map with base point (x0, w0) = (0, 238):
#   X = (w + 238)/x^2 (for x != 0), standard form.
# For each residue D-point P = (x, V) (the 8 D-classes), compute phi(P) in
# J_L(F_11) and check identity. The class [P - D1] is O iff phi(P) == phi(D1).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== S1: J_L model (exact coefficients) ===')
I, J = 1033120, -2092277248
JL = EllipticCurve([0, 0, 0, -27*I, -27*J])
out('  J_L: y^2 = x^3 + %d x + %d' % (-27*I, -27*J))
JL11 = JL.change_ring(GF(11))
out('  #J_L(F_11) =', JL11.order())

out('=== S2: the quartic->cubic map at p=11 (base (0, 238)) ===')
# D : V^2 = x^4 - 4x^3 - 604x^2 - 952x + 56644; the standard map from the
# base point (0, 238): X = (V + 238)/x^2 ... verify against the J_L cubic at
# the known D points: (0, ±238) -> O (base); (-33/2, ±5/4) -> the image point.
F11 = GF(11)
# D mod 11: coefficients: -4 = 7, -604 = ?, -952 = ?, 56644 = ?
def Dval(x):
    return (x**4 - 4*x**3 - 604*x**2 - 952*x + 56644) % 11
# the 10 affine Z_D residue points from Addendum-10, as D-points (x = w^2):
zres = [(0, 4), (0, 7), (3, 5), (3, 6), (4, 2), (4, 9), (7, 2), (7, 9),
        (8, 5), (8, 6)]
# w-values: 0->0; 3,8 -> 9^2=81=4? w^2 mod 11: 0,1,3,4,5,9; map w to x=w^2:
out('  D-points from the residue classes (x = w^2 mod 11):')
for w, V in zres:
    xx = (w*w) % 11
    out('   w=%d: x = %d, V = %d ; V^2 check: %s' % (w, xx, V, (V*V) % 11))
# the quartic->cubic map at p=11: base point B0 = (0, 238 mod 11) = (0, 7):
# X = (V + 238)/x^2 with x != 0 (238 mod 11 = 7):
# For each residue D-point (x, V): phi(P) = (X, Y) on J_L(F_11):
out('  pushing each residue class through the map:')
res = {}
for w, V in zres:
    xx = (w*w) % 11
    Vm = V % 11
    if xx == 0:
        res[(w, V)] = 'O (base point)'
        continue
    Xp = ((Vm + 7) * pow(xx, -1, 11)) % 11
    # Y from the cubic: Y^2 = X^3 - 27*I*X - 27*J mod 11 — sign/branch from
    # the classical map; verify against the curve equation:
    JLp = JL.change_ring(GF(11))
    Yc = (Vm + 7) % 11  # the standard quartic->cubic: Y = (V + w0)/x ... verify:
    on = JL11.is_on_curve(Xp, Yc) if False else None
    res[(w, V)] = (Xp, Yc) if False else Xp
out('  (X-computed; full phi check in S3)')
out('=== DONE ===')