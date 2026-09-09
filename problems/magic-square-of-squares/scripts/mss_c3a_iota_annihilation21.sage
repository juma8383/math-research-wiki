# mss_c3a_iota_annihilation21.sage -- manual Hensel sqrt (Sage's .sqrt() on
# capped-relative Qp-extension elements is unimplemented): squareness test
# via fp^60 == 1 (F_121^* has order 120), then Newton iteration z <- z/2*(1 +
# fp/z^2) doubling precision each step. Fully in-script, no API gaps.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3o: manual Hensel sqrt ===')
K11 = Qp(11, 8)
Rk.<X> = K11[]
K2.<c> = K11.extension(X^2 - 7)
poly = fA.change_ring(K2)
rts = poly.roots()
x0 = rts[0][0]
Ru.<u> = K2[]
f_new = Ru(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
fp = f_new.leading_coefficient()
out('  fp = %s' % str(fp)[:70])
# squareness: fp^60 in K2: == 1 => QR in F_121 (unit case)
t60 = fp^60
is_square = (t60 == 1)
out('  fp^60 == 1? %s' % is_square)
if is_square:
    # Hensel: z0 = the square root mod 11: find by brute force over F_121:
    F121 = K2.residue_field() if hasattr(K2, 'residue_field') else None
    # brute force: try all lifts? simpler: Newton from z0 = fp^30 (a sqrt mod 11
    # when fp is a QR: z0 = fp^{(120+2)/4}? standard: for odd p^f, a sqrt of a QR
    # a mod q: z0 = a^{(q+1)/4} if q ≡ 3 mod 4; F_121: 121 ≡ 1 mod 4 -> need
    # general algorithm. Use Sage's sqrt on the RESIDUE FIELD (implemented):
    F121 = K2.residue_field()
    fp_red = F121(fp.unit_part() if hasattr(fp, 'unit_part') else fp)
    s_red = fp_red.sqrt()
    out('  residue sqrt: %s' % s_red)
    # lift: z = s_red in K2 via teichmuller lift + Newton:
    z = K2(s_red)
    z = z.add_precision() if hasattr(z, 'add_precision') else z
    for _ in range(5):
        z = (z + fp/z) / 2
    out('  Newton sqrt(fp) = %s' % str(z)[:80])
    ok = (z^2 - fp).valuation()
    out('  z^2 - fp valuation: %s (expect >= 8)' % ok)
    if ok >= 7:
        uu = 1/(0 - x0)
        vv = uu^4 / z
        diff = f_new.monic()(uu) - vv^2
        out('  on-curve check: %s' % str(diff)[:80])
        f_final = f_new.monic()
        lst = f_final.list(); lst[-1] = K2(1)
        f_final = Ru(lst)
        Codd = HyperellipticCurve(f_final)
        w = Codd.invariant_differential()
        P = Codd(uu, vv)
        Q = Codd(uu, -vv)
        val = Codd.coleman_integral(w, P, Q)
        out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
out('=== DONE ===')