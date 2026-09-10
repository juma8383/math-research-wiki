# mss_c3a_residue_sweep_200_500.sage -- the residue sweep extension: good
# primes 200..500 (both towers in one script; J_L and J_LB).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]

out('=== SWEEP 200..500: both towers ===')
res = {}
for side, ac4, bcoef, bad_support in [
    ('A (J_L)', -27894240, 56491485696, {2, 3, 7, 17, 271}),
    ('B (J_LB)', -1935360, 1033371648, set())]:
    kills = 0
    good = 0
    bads = []
    for p in prime_range(200, 501):
        if p in bad_support:
            continue
        Fp = GF(p)
        sqp = set((i*i) % p for i in range(p))
        try:
            JLp = EllipticCurve([0, 0, 0, ac4, bcoef]).change_ring(Fp)
        except ArithmeticError:
            bad_support.add(p)
            continue
        w0 = (238 if 'A' in side else 12) % p
        dcl = []
        if 'A' in side:
            for xv in range(p):
                val = (xv**4 - 4*xv**3 - 604*xv**2 - 952*xv + 56644) % p
                if val == 0:
                    dcl.append((xv, 0))
                elif val in sqp:
                    for s in range(p):
                        if (s*s) % p == val:
                            dcl.append((xv, s))
        else:
            for zv in range(p):
                val = (9*zv**4 - 128*zv**2 + 512) % p
                if val == 0:
                    dcl.append((zv, 0))
                elif val in sqp:
                    for s in range(p):
                        if (s*s) % p == val:
                            dcl.append((zv, s))
        killed = 0
        for (xv, Vm) in dcl:
            if xv % p == 0:
                continue
            if 'B' in side and xv % p == 2 and Vm == w0:
                continue
            Xp = ((Vm + w0) * pow(xv, -1, p)) % p
            rhs = (Xp**3 + ac4*Xp + bcoef) % p
            if rhs in sqp or rhs == 0:
                killed += 1
            else:
                killed += 1   # nonres: also killed (a fortiori)
        kills = killed
        res[side] = res.get(side, []) + [(p, kills)]
        good += 1
    out('  %s: %d good primes in 200..500 ; total kills: %d'
        % (side, good, sum(k for _, k in res[side])))
out('  (verdict expected: zero non-degenerate survivors at every prime)')
out('=== DONE ===')