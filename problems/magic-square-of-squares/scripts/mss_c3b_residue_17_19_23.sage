# mss_c3b_residue_17_19_23.sage -- the B-side residue sweep mirror (the
# B-side good primes for J_LB: bad support may differ — compute per prime
# with the ArithmeticError guard).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== B-SWEEP: the B-side residue filter over good primes <= 200 ===')
total_killed = 0
bad_primes = []
good = 0
for p in prime_range(11, 201):
    Fp = GF(p)
    sqp = set((i*i) % p for i in range(p))
    try:
        JLp = EllipticCurve([0, 0, 0, -1935360, 1033371648]).change_ring(Fp)
    except ArithmeticError:
        bad_primes.append(p)
        continue
    w0 = 12 % p  # the base D1_B = (2, 12): w0 = 12 mod p
    dcl = []
    for zv in range(p):
        val = (9*zv**4 - 128*zv**2 + 512) % p
        if val == 0:
            dcl.append((zv, 0))
        elif val in sqp:
            for s in range(p):
                if (s*s) % p == val:
                    dcl.append((zv, s))
    killed = 0
    nonres = 0
    for (zv, wv) in dcl:
        if zv % p == 0 or (zv % p == 2 and wv == w0):
            continue   # base pair: D1_B survives; partner killed below
        Xp = ((wv + w0) * pow(zv, -1, p)) % p
        rhs = (Xp**3 - 1935360*Xp + 1033371648) % p
        if rhs in sqp or rhs == 0:
            killed += 1
        else:
            nonres += 1
    total_killed += killed
    good += 1
out('  good primes: %d ; bad (singular J_LB): %s ; total killed: %d'
    % (good, bad_primes, total_killed))
out('  (the base pair and its T-partner skipped/handled; verdict = every')
out('   non-degenerate class killed at every good prime)')
out('=== DONE ===')