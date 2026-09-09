# mss_c3a_iota_annihilation33.sage -- FULLY diagnosed: BOTH list routes give
# length 9 for a degree-7 polynomial over this CDVF ring (the ring stores a
# degree-8 slot with precision-zero). The wrapper's pop() hits the padded
# zero. THE WORKAROUND that must work: pass HQR the polynomial ring element
# from a ring with EXACTLY degree-7 storage: use the generic polynomial ring
# (not the CDVF-optimized one): Ru2.<u> = PolynomialRing(K8, 'u') — same? The
# REAL fix: patch the wrapper's _coeffs after catching the raise:
#   try: HQR = mw.SpecialHyperellipticQuotientRing(f2)
#   except NotImplementedError: construct via __new__ hack is fragile;
# SIMPLER: strip the padded slot by constructing over the INTEGER model:
# scale f_monic to make the padded slot a GENUINE nonzero term: the padding
# zero sits at index 8 because the ring was created with a degree-8 poly
# earlier (Ru's element storage inherits the max degree seen?). A fresh ring
# fixes it: make Rv2.<w> = K8[] (new name, fresh ring) and rebuild f_monic
# there; .list() then has exactly 8 entries.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I4: fresh-ring rebuild ===')
from sage.rings.padics.factory import is_unramified
K11 = Qp(11, 10)
Rk.<X> = K11[]
modulus = None
for a in range(0, 11):
    if modulus is not None:
        break
    for bcoef in range(2, 11):
        P = X^8 + a*X + bcoef
        if is_unramified(P):
            modulus = P
            break
K8.<y8> = Qp(11, 10).extension(modulus)
poly = fA.change_ring(K8)
rts = poly.roots()
x0 = rts[0][0]
Rv2.<w2> = PolynomialRing(K8, 'w2')   # FRESH generic ring
f_new = Rv2(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*w + 1)^j * w^(8 - j)
out('  fresh-ring poly degree: %d ; len(list()): %s' % (f_new.monic().degree(), len(f_new.monic().list())))
f_monic = f_new.monic()
cl = f_monic.list()
cl[-1] = K8(1)
f_final = Rv2(cl)
out('  f_final degree: %d ; leading: %s' % (f_final.degree(), str(f_final.leading_coefficient())[:50]))
try:
    HQR = mw.SpecialHyperellipticQuotientRing(f_final)
    out('  HQR: OK')
    xs, ys = HQR.gens()
    out('  gens: OK')
except Exception as e:
    out('  I4 error:', str(e)[:200])
out('=== DONE ===')