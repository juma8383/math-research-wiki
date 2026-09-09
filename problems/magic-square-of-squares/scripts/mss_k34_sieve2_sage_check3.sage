# mss_k34_sieve2_sage_check3.sage -- extended verification round 3 (hermes-win, 2026-09-09)
#  A3: filtered stress to 3e5 (§6ii parity: 624 valid primes claim) + extension 3e5..1e6
#      (§6ii claims 231 more valid primes, zero violations)
#  B3: B-side mirror (filtered): 5 classes {0,1,2,134,262} mod M_B=264 vs all
#      good primes <= 2e5 with ord(G_B) | 264 (claim: 33 valid, 0 violations)
#  NOTE on map: B uses X_B = (6y - 92x)/(x(x-36)) [NOT the 2*(y+66x) A-map].
def out(*a):
    print(*a); sys.stdout.flush()

import time
t0 = time.time()

MA = 42078090600
MB = 264
KILL_A = [5, 11, 13]
KILL_B = [5, 19, 29]

out('=== A3: A-side filtered stress, primes <= 3e5, then 3e5..1e6 ===')
claimA = [0, 2, MA//2 - 1, MA - 2, MA - 1]
nvalid = 0
bad = []
def stress_A(lo, hi):
    global nvalid
    b = []
    for p in prime_range(lo, hi):
        Ep = EllipticCurve(GF(p), [0, -256, 0, 18432, 0])
        Gp = Ep(128, 512)
        o = Gp.order()
        if MA % o != 0:
            continue
        nvalid += 1
        K = p in KILL_A
        sq = set(GF(p)(i)^2 for i in range(1, p))
        for c in claimA:
            P = (c % o) * Gp
            if P.is_zero():
                continue
            xP, yP = P[0], P[1]
            if xP == 0 or xP == 4:
                continue
            v = (2*(yP + 66*xP)) / (xP*(xP - 4))
            ok = (v in (0, 1)) if K else (v == 0 or v in sq)
            if not ok:
                b.append((p, c))
                break
    return b

bad += stress_A(5, 300001)
out('  A <= 3e5: valid=%d elapsed=%.0fs violations=%s'
    % (nvalid, time.time()-t0, bad if bad else 'NONE'))
nv3e5 = nvalid
bad += stress_A(300009, 1000003)
out('  A 3e5..1e6: +valid=%d elapsed=%.0fs violations(addnl)=%s'
    % (nvalid - nv3e5, time.time()-t0, bad[len(bad):] if bad else 'NONE'))
out('  A TOTAL: valid=%d ; violations: %s' % (nvalid, bad if bad else 'NONE'))

out('=== B3: B-side filtered stress, primes <= 2e5 ===')
GBQ = (-128, 1536)
claimB = [0, 1, 2, 134, 262]
nvalidB = 0
badB = []
for p in prime_range(5, 200001):
    Ep = EllipticCurve(GF(p), [0, 256, 0, -2048, 0])
    Gp = Ep(-128, 1536)
    o = Gp.order()
    if MB % o != 0:
        continue
    nvalidB += 1
    K = p in KILL_B
    sq = set(GF(p)(i)^2 for i in range(1, p))
    for c in claimB:
        P = (c % o) * Gp
        if P.is_zero():
            continue
        xP, yP = P[0], P[1]
        if xP == 0 or xP == 36:
            continue
        v = (6*yP - 92*xP) / (xP*(xP - 36))
        ok = (v in (0, 1)) if K else (v == 0 or v in sq)
        if not ok:
            badB.append((p, c))
            break
out('  B: valid=%d elapsed=%.0fs violations=%s'
    % (nvalidB, time.time()-t0, badB if badB else 'NONE'))
out('=== DONE ===')