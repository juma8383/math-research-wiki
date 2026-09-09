# mss_k34_sieve_stress_1e6_3e6.sage -- A-side filtered stress extension to 3e6
# (hermes-win, 2026-09-09). [mss-k34-c3ab-prep] cont. Resumes the time-capped
# run (§2ab D1) from ~1.67e6 up to 3e6; discharges the filed "hunt to 3e6" tier.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

MA = 42078090600
claim = [0, 2, MA//2 - 1, MA - 2, MA - 1]
EA = EllipticCurve([0, -256, 0, 18432, 0])
nvalid = 0
bad = []
t0 = time.time()
TIME_CAP = 1500
lastp = 0
for p in prime_range(1668479, 3000001):
    Ep = EllipticCurve(GF(p), [0, -256, 0, 18432, 0])
    Gp = Ep(128, 512)
    o = Gp.order()
    if MA % o != 0:
        lastp = p
        continue
    nvalid += 1
    K = p in (5, 11, 13)
    sq = set(GF(p)(i)^2 for i in range(1, p))
    for c in claim:
        P = (c % o) * Gp
        if P.is_zero():
            continue
        xP, yP = P[0], P[1]
        if xP == 0 or xP == 4:
            continue
        v = (2*(yP + 66*xP)) / (xP*(xP - 4))
        ok = (v in (0, 1)) if K else (v == 0 or v in sq)
        if not ok:
            bad.append((p, c))
            break
    if time.time() - T0 > TIME_CAP:
        out('  (time cap at p=%d)' % p)
        break
out('  primes 1.67e6..3e6: valid=%d elapsed=%s violations: %s'
    % (nvalid, el(), bad if bad else 'NONE'))
out('  (resumable from p > %d)' % (lastp if lastp else p))
out('=== DONE ===')