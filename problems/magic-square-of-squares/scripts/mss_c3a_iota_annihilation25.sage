# mss_c3a_iota_annihilation25.sage -- unramified quartic with a VERIFIED
# irreducible modulus (X^4 - 2 factors over F_11 into two quadratics since
# every F_11 element is a square in F_121 — found by reasoning; test
# candidates in-script with the factory's own is_unramified check).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3s: find an irreducible quartic mod 11 ===')
from sage.rings.padics.factory import is_unramified
K11 = Qp(11, 8)
Rk.<X> = K11[]
modulus = None
for cand_poly in [X^4 + X + 2, X^4 + X + 3, X^4 + 2*X + 3, X^4 + 3*X + 7,
                  X^4 + X + 5, X^4 + 5*X + 2, X^4 + 2*X + 2, X^4 + X + 9]:
    if is_unramified(cand_poly):
        modulus = cand_poly
        out('  unramified quartic found: %s' % cand_poly)
        break
if modulus is None:
    # try more systematically: all X^4 + aX^2 + b with irreducible
    for a in range(11):
        for bcoef in range(1, 11):
            P = X^4 + a*X^2 + bcoef
            if is_unramified(P):
                modulus = P
                out('  unramified quartic: %s' % P)
                break
        if modulus is not None:
            break
if modulus is not None:
    K4.<y4> = Qp(11, 8).extension(modulus)
    out('  K4 = %s' % K4)
    poly = fA.change_ring(K4)
    rts = poly.roots()
    out('  roots over K4: %d' % len(rts))
    x0 = rts[0][0]
    Rv.<u> = K4[]
    f_new = Rv(0)
    for j in range(poly.degree() + 1):
        aj = poly[j]
        f_new += aj * (x0*u + 1)^j * u^(8 - j)
    fp = f_new.leading_coefficient()
    t = fp^((11^4 - 1)//2)
    out('  fp square in K4? %s' % (t == 1))
    if t == 1:
        Fq = K4.residue_field()
        s_res = Fq(fp).sqrt()
        z = K4(s_res)
        for _ in range(6):
            z = (z + fp/z) / 2
        out('  sqrt(fp) ok; on-curve check next')
        f_mon2 = f_new.monic()
        lst2 = f_mon2.list()
        lst2[-1] = K4(1)
        f_final = Rv(lst2)
        Codd = HyperellipticCurve(f_final)
        w = Codd.invariant_differential()
        uu = 1/(0 - x0)
        vv = uu^4 / z
        diff = f_final(uu) - vv^2
        out('  on-curve check: %s' % str(diff)[:80])
        P = Codd(uu, vv)
        Q = Codd(uu, -vv)
        val = Codd.coleman_integral(w, P, Q)
        out('  INTEGRAL = %s' % val)
out('=== DONE ===')