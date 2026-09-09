# mss_c3a_iota_annihilation29.sage -- THE BLOCK IDENTIFIED: Sage's
# coleman_integral requires the p-adic curve to be RAMIFIED (one point at
# infinity = odd degree). The even->odd transform exists only over fields
# containing a branch point AND the odd model must also be RAMIFIED over
# that field — degree-7 f IS ramified (one infinity). v28's error came from
# is_ramified() being False?? For degree 7 with unit leading coeff: ONE
# infinity point: ramified True... unless the leading coefficient's square
# class matters: degree-7 f with leading coeff a unit: the infinity point is
# rational iff lc is a square in K8! lc = the monic-normalized leading is 1:
# rational infinity ✓ ramified ✓. So is_ramified should be True. The v28
# raise: line 941 in coleman_integral -> 661 coleman_integrals_on_basis ->
# the is_ramified() check FAILED => the curve's internal degree is EVEN!
# The list rebuild: f_tw.list() length for degree 7 = 8; forcing lst[-1] = 1
# again hit the same padding issue in the K8 CDVF ring: 9 entries, top
# O(11^10) zero; setting it to 1 made degree 8!! Same bug as v12. FIX:
# strip the polynomial to its TRUE degree first: use f_tw.list() then trim
# trailing zeros BEFORE appending the 1:
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3w: degree-trimmed monic ===')
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
Rv.<u> = K8[]
f_new = Rv(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
f_tw = f_new.monic()
d = f_tw.degree()
out('  true degree of the twist model: %s' % d)
lst = f_tw.list()
# trim to exactly d+1 entries:
lst = lst[:d+1]
out('  trimmed list length: %d ; top: %s' % (len(lst), str(lst[-1])[:60]))
if lst[-1] != 1:
    s_top = lst[-1].sqrt() if lst[-1].valuation() == 0 else None
    if s_res := True:
        Fq = K8.residue_field()
        s_res = Fq(lst[-1]).sqrt()
        lst[-1] = K8(s_res)
        for _ in range(7):
            lst[-1] = (lst[-1] + (f_tw.leading_coefficient())/lst[-1]) / 2
    # now force the top to EXACTLY 1: divide the whole list by lst[-1]:
    top = lst[-1]
    lst = [e / top for e in lst]
    lst[-1] = K8(1)
f_final = Rv(lst)
out('  final degree: %d ; leading: %s' % (f_final.degree(), f_final.leading_coefficient()))
Codd = HyperellipticCurve(f_final)
out('  is_ramified (should be True for odd degree): %s' % Codd.is_ramified())
w = Codd.invariant_differential()
uu = 1/(0 - x0)
# points: the images of C3_A (0, ±1) under the twist: v via Hensel on this model:
f_at = f_final(uu)
out('  f_final(u) valuation: %s' % f_at.valuation())
Fq = K8.residue_field()
elt = Fq(f_at)
is_sq = (elt^((11^8 - 1)//2) == 1)
out('  residue square? %s' % is_sq)
if is_sq and f_at.valuation() == 0:
    v = K8(Fq(f_at).sqrt())
    for _ in range(7):
        v = (v + f_at/v) / 2
    P = Codd(uu, v)
    Q = Codd(uu, -v)
    val = Codd.coleman_integral(w, P, Q)
    out('  VERDICT INTEGRAL = %s' % val)
out('=== DONE ===')