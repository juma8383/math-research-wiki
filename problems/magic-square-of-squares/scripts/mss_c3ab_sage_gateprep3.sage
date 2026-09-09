# mss_c3ab_sage_gateprep3.sage -- final corrected gate-prep (hermes-win, 2026-09-09)
# Root cause of v1/v2 failures: the filed J(C3_A) decomposition is
#   J(C3_A) ~ E_iota x E_rho x E_G with
#   E_iota = E_rho = Jac of the QUOTIENT QUARTICS with invariants (10240, -8912896)
#     -> cubic y^2 = x^3 - 276480x + 240648192  (Q-isogenous to master E_A, j=-8000/81)
#   E_G = y^2 = x^3 - 504576x + 131604480 (iota_rho quotient; j=1556068/81).
# The ~E_A/~E_B shifted models I used in v2 are isogenous to E_iota but the
# PRIME-level Frobenius product test needs the EXACT quotient cubics (2-isogenous
# copies have different Frobenius traces at a given p unless you use the right one).
# This script: (B') product check with the EXACT filed cubics;
# (C') quotient trace identification (q1 = v=x^2 quartic; q2 = u=x-1/x NOTE FILED
#      convention: rho quotient is u = x - 1/x per notes script identity g = x^4 G(x-1/x));
# (D') #C3_A(F_p) table; (E') coleman probe. Part A (B-hunt) filed separately.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1
C3A = HyperellipticCurve(fA)
# EXACT quotient cubics from the filed invariants:
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])   # = both iota and rho quotients
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])
out('=== setup v3 (exact filed cubics) ===')
out('  EIOTA j:', EIOTA.j_invariant(), ' (expect -8000/81)')
out('  EG j:', EG.j_invariant(), ' (expect 1556068/81)')

out("=== B': Jac(C3_A) = E_iota x E_rho x E_G product check (exact cubics) ===")
bad = []
skipped = []
for p in prime_range(7, 401):
    P6 = C3A.change_ring(GF(p)).frobenius_polynomial()
    try:
        P1 = EIOTA.change_ring(GF(p)).frobenius_polynomial()
        P2 = EIOTA.change_ring(GF(p)).frobenius_polynomial()
        P3 = EG.change_ring(GF(p)).frobenius_polynomial()
    except ArithmeticError:
        skipped.append(p)
        continue
    if P1 * P2 * P3 != P6:
        bad.append(p)
out('  skipped (singular mod p): %s' % (skipped if skipped else 'NONE'))
out('  mismatches: %s' % (bad if bad else 'NONE — decomposition CONFIRMED at all %d good primes 7..397'
    % (len(prime_range(7, 401)) - len(skipped))))

out("=== C': quotient identification (iota: v=x^2; rho: u=x-1/x) ===")
Rv.<v> = QQ[]
g_iota = v^4 + 132*v^3 - 250*v^2 + 132*v + 1          # C3_A / (x->-x)
# rho quartic: ascending [-512, 0, 128, 0, 1] => deg-first (1, 0, 128, 0, -512):
# W'^2 = (x-1/x)^4*... identity g = x^4 * D(x-1/x); the quartic itself is
# 1 - 512z^2 + 128z^4 (ascending), i.e. in v (deg-first): -512 v^4 + 128 v^2 + 1
g_rho_real = -512*v^4 + 128*v^2 + 1
mism_iota = []
mism_rho = []
for p in prime_range(7, 212):
    Hi = HyperellipticCurve(g_iota.change_ring(GF(p)))
    t_i = p + 1 - len(Hi.points())
    tE = p + 1 - len(EIOTA.change_ring(GF(p)).points())
    if t_i != tE:
        mism_iota.append((p, t_i, tE))
    Hr = HyperellipticCurve(g_rho_real.change_ring(GF(p)))
    t_r = p + 1 - len(Hr.points())
    if t_r != tE:
        mism_rho.append((p, t_r, tE))
out('  iota-quotient vs E_iota trace mismatches: %s' % (mism_iota if mism_iota else 'NONE'))
out('  rho-quotient vs E_iota trace mismatches: %s' % (mism_rho if mism_rho else 'NONE'))

out('=== D: #C3_A(F_p) for good primes <= 200 ===')
cntA = {}
for p in prime_range(7, 201):
    Fp = GF(p)
    fAp = fA.change_ring(Fp)
    sq = set(Fp(i)^2 for i in range(p))
    c = 2
    for xv in Fp:
        val = int(fAp(xv)) % p
        if val == 0: c += 1
        elif val in sq: c += 2
    cntA[p] = c
out('  #C3_A(F_11) = %s (filed: 8)' % cntA.get(11))
out('  p<=40: %s' % {p: cntA[p] for p in sorted(cntA) if p <= 40})
mism2 = []
for p in prime_range(7, 201):
    P6 = C3A.change_ring(GF(p)).frobenius_polynomial()
    # Sage frobenius_polynomial().list() is ascending: [a0..a6]; T^5 coefficient is
    # P6[5] = -s1 where s1 = sum of Frobenius eigenvalues = 2*t_iota + t_G.
    # For even degree with 2 rational points at infinity:
    # #C(F_p) = p + 1 - s1  (verified p=7: 8-(-8)=16 ✓, p=11: 12-4=8 ✓, p=13: 14-6=8 ✓)
    s1 = -P6[5]
    pred = p + 1 - s1
    if pred != cntA[p]:
        mism2.append((p, cntA[p], pred))
out('  #C vs p+1-(2*t_iota+t_G) mismatches: %s' % (mism2 if mism2 else 'NONE — point-count formula confirmed'))

out('=== E: coleman machinery probe ===')
Kp = Qp(11, 10)
try:
    Ct = HyperellipticCurve(x^3 - x).change_ring(Kp)
    out('  odd-degree Qp hyperelliptic OK; coleman API:', hasattr(Ct, 'coleman_integrals'))
except Exception as e:
    out('  probe error:', str(e)[:200])
try:
    Ce = HyperellipticCurve(fA).change_ring(Kp)
    out('  even-degree C3_A over Qp(11): constructed OK')
except Exception as e:
    out('  even-degree Qp note:', str(e)[:150])
out('=== ALL DONE ===')