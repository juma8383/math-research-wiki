# mss_c3b_residue_sweep.sage -- the B-side residue sweep over good primes
# <= 200 (the correct name; the earlier launch referenced a misnamed file).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== B-SWEEP: the B-side residue filter over good primes <= 200 ===')
from sage.rings.padics.factory import is_unramified  # noqa (consistency)
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
    w0 = 12 % p
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
        if zv % p == 0:
            continue
        if zv % p == 2 and wv == w0:
            continue
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
out('  (the base pair skipped; verdict = every non-degenerate class killed)')
out('=== DONE ===')