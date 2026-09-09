# mss_k34_residue_groundwork.sage -- residue-bound groundwork (hermes-win,
# 2026-09-09). [mss-k34-c3ab-prep] cont. The last named computation: the
# Coleman/residue bound on C3_A. Groundwork = assemble at a chosen good prime:
#   (1) the Frobenius/annihilator period data for the rank-2 MW lattice,
#   (2) the residue-disc data (#C3_A(F_p) and the reduction types of the 8
#       known points) at a prime where the structure is simplest.
# Prime selection heuristic: p where the annihilator kernel is maximally
# decoupled — try several primes, print the period-matrix condition data.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1
C3A = HyperellipticCurve(fA)
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])

out('=== R1: candidate primes with #C3_A(F_p) == 8 (tight bound) ===')
tight = []
for p in prime_range(7, 500):
    Fp = GF(p)
    fAp = fA.change_ring(Fp)
    sq = set(Fp(i)^2 for i in range(p))
    c = 2
    for xv in Fp:
        val = int(fAp(xv)) % p
        if val == 0: c += 1
        elif val in sq: c += 2
    if c == 8:
        tight.append(p)
out('  primes <= 500 with #C3_A(F_p) = 8: %s' % tight)
out('  (at these, #C3_A(Q) <= 8 + 2g - 2 = 12 by Chabauty count; tightest gate)')

out('=== R2: reduction of the 8 known Q-points at the tight primes ===')
# known C3_A(Q) points: (x, W) = (0, ±1), (±1, ±4), infinities ×2 = 8 total.
# Verify each reduces to a DISTINCT C3_A(F_p) point at p=11 (and other tight
# primes): the residue bound needs the known points to account for all 8.
out('  at p=11: reductions of (0,±1), (1,±4), (-1,±4), inf±:')
Fp11 = GF(11)
f11 = fA.change_ring(Fp11)
sq11 = set(Fp11(i)^2 for i in range(11))
for xv in [0, 1, -1]:
    val = int(fA(xv)) % 11
    w = isqrt(val) if val >= 0 else None
    # exact check:
    vals = [Fp11(t) for t in range(11) if (Fp11(t)^2 == Fp11(val))]
    out('   x=%d: W^2 = %s -> W = %s' % (xv, val % 11, vals))

out('=== R3: period-matrix data at p=13 (second tight prime candidate) ===')
K13 = Qp(13, 8)
try:
    EIp13 = EIOTA.change_ring(K13)
    Gi = EIp13([QQ(384), QQ(13824)])
    wE = EIp13.invariant_differential()
    v13 = wE.coleman_integral(EIp13(0), Gi)
    out('  ∫_O^{G_iota} ω_E at p=13:', v13)
except Exception as e:
    out('  R3 integral error:', str(e)[:200])
out('=== DONE ===')