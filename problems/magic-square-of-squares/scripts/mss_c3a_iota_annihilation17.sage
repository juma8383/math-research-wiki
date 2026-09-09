# mss_c3a_iota_annihilation17.sage -- THE fix, fully diagnosed:
# coefficients(sparse=False) returns 9 entries for a degree-7 poly (a zero
# O(11^8) at index 8 — a CDVF padding quirk) so .pop() grabs the zero,
# which != 1 raises even though the true leading (index 7) IS 1.
# FIX: build the polynomial through a parent whose coefficient list has no
# padding: construct the HQR with Q as a LIST-based poly of exact degree 7 —
# i.e. ensure f_monic has NO zero at index 8: strip: f2 = Ru(f_monic.list())
# where .list() gives exactly degree+1 entries; then HQR(f2).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3j: list()-based degree hygiene + HQR ===')
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
f_monic = f_new.monic()
# .list() gives exactly degree+1 coefficients (index 0..degree):
lst = f_monic.list()
out('  f_monic.list() length: %d (degree %d)' % (len(lst), f_monic.degree()))
out('  last entry: %s' % str(lst[-1])[:60])
# force the top to literal 1 AND rebuild with exactly 8 entries:
lst[-1] = K2(1)
f_final = Ru(lst)
out('  f_final degree: %d ; leading: %s' % (f_final.degree(), str(f_final.leading_coefficient())[:40]))
from sage.schemes.hyperelliptic_curves import monsky_washnitzer as mw
HQR = mw.SpecialHyperellipticQuotientRing(f_final)
out('  HQR constructed: OK')
out('  HQR: %s' % str(HQR)[:100])
xs, ys = HQR.gens()
out('  gens OK: x, y')
out('=== DONE ===')