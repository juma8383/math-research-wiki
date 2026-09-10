# mss_k34_zd_residue_p17.sage -- extend the residue filter to p = 17 (good
# for both towers; #Z_D(F_17) = 19 filed, #C3_A: compute): the dual-prime
# pattern becomes multi-prime; also compute p = 19, 23 in one script.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== R17: the residue filter at p in {17, 19, 23} (both towers) ===')
def D13(x):
    return (x**4 - 4*x**3 - 604*x**2 - 952*x + 56644) % 13

for p in [17, 19, 23]:
    out('--- p = %d ---' % p)
    Fp = GF(p)
    sqp = set((i*i) % p for i in range(p))
    # A-side: C3_A count:
    fa = lambda x: (x**8 + 132*x**6 - 250*x**4 + 132*x**2 + 1) % p
    na = 2
    for xv in range(p):
        val = fa(xv)
        if val == 0:
            na += 1
        elif val in sqp:
            na += 2
    # A-side D classes:
    dcl = []
    for xv in range(p):
        val = D13(xv) if False else (xv**4 - 4*xv**3 - 604*xv**2 - 952*xv + 56644) % p
        if val == 0:
            dcl.append((xv, 0))
        elif val in sqp:
            for s in range(p):
                if (s*s) % p == val:
                    dcl.append((xv, s))
    JLp = EllipticCurve([0, 0, 0, -27894240, 56491485696]).change_ring(GF(p))
    njl = JLp.order()
    # base D1 = (0, 238 mod p):
    w0 = 238 % p
    # the identity test: classes with x = 0 and V = w0 push to O:
    surv = [(0, w0)]
    killed = 0
    nonres = 0
    for (xv, Vm) in dcl:
        if xv % p == 0:
            continue  # base pair handled: D1 survives; the T partner killed
        Xp = ((Vm + w0) * pow(xv, -1, p)) % p
        rhs = (Xp**3 - 27894240*Xp + 56491485696) % p
        if rhs in sqp or rhs == 0:
            killed += 1
        else:
            surv.append((xv, Vm, 'X=%d nonres push' % Xp))
    out('  A: #C3_A=%d ; #J_L=%d ; D classes=%d ; killed=%d ; exceptions=%s'
        % (na, njl, len(dcl), killed, surv))
out('=== DONE ===')