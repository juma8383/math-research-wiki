# mss_k34_zd_residue_p17b.sage -- p = 17 is a BAD prime for J_L (the curve
# reduces to x^3+6x+6, singular mod 17 — consistent with the filed bad-prime
# support {2,3,7,17,271}). Restrict to the GOOD primes 19 and 23.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== R19/R23: the residue filter at the good primes 19, 23 ===')
for p in [19, 23]:
    out('--- p = %d ---' % p)
    Fp = GF(p)
    sqp = set((i*i) % p for i in range(p))
    fa = lambda x: (x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1) % p
    na = 2
    for xv in range(p):
        val = fa(xv)
        if val == 0:
            na += 1
        elif val in sqp:
            na += 2
    dcl = []
    for xv in range(p):
        val = (xv**4 - 4*xv**3 - 604*xv**2 - 952*xv + 56644) % p
        if val == 0:
            dcl.append((xv, 0))
        elif val in sqp:
            for s in range(p):
                if (s*s) % p == val:
                    dcl.append((xv, s))
    JLp = EllipticCurve([0, 0, 0, -27894240, 56491485696]).change_ring(GF(p))
    njl = JLp.order()
    w0 = 238 % p
    surv = [(0, w0)]
    killed = 0
    nonres = 0
    for (xv, Vm) in dcl:
        if xv % p == 0:
            continue
        Xp = ((Vm + w0) * pow(xv, -1, p)) % p
        rhs = (Xp**3 - 27894240*Xp + 56491485696) % p
        if rhs in sqp or rhs == 0:
            killed += 1
        else:
            surv.append((xv, Vm, 'X=%d nonres push' % Xp))
    out('  A: #C3_A=%d ; #J_L=%d ; D classes=%d ; killed=%d ; exceptions=%s'
        % (na, njl, len(dcl), killed, surv))
out('=== DONE ===')