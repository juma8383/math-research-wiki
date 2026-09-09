# mss_c3a_iota_annihilation28.sage -- the K4 value run: the twist field is
# K4 = K2(sqrt(f_tw(u0))) = the unramified quartic; build K4 directly over
# Q_11 with an irreducible octic (contains F_{11^4} sqrt residue), lift the
# SAME root x0, transform, monic, Hensel v (residue now in F_{11^8}: square),
# integral. The VERDICT transfers (integral = 0 iff torsion) — the value is
# over K4 but the zero/nonzero answer is the annihilation condition.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3v: K4-based verdict ===')
from sage.rings.padics.factory import is_unramified
K11 = Qp(11, 10)
Rk.<X> = K11[]
modulus = None
for a in range(0, 11):
    if modulus is not None:
        break
    for bcoef in range(1, 11):
        P = X^8 + a*X + bcoef
        if is_unramified(P):
            modulus = P
            break
if modulus is None:
    for a in range(0, 11):
        if modulus is not None:
            break
        for bcoef in range(2, 11):
            P = X^8 + a*X^4 + bcoef
            if is_unramified(P):
                modulus = P
                break
K8.<y8> = Qp(11, 10).extension(modulus)
out('  K8 = %s' % K8)
poly = fA.change_ring(K8)
rts = poly.roots()
x0 = rts[0][0]
Rv.<u> = K8[]
f_new = Rv(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
f_tw = f_new.monic()
lst = f_tw.list()
lst[-1] = K8(1)
f_tw = Rv(lst)
Codd = HyperellipticCurve(f_tw)
w = Codd.invariant_differential()
uu = 1/(0 - x0)
f_at = f_tw(uu)
out('  f_tw(u) unit? valuation = %s' % f_at.valuation())
Fq = K8.residue_field()
elt = Fq(f_at)
is_sq = (elt^((11^8 - 1)//2) == 1)
out('  residue square in F_{11^8}? %s' % is_sq_res if (is_sq_res := (elt^((11^8 - 1)//2) == 1)) is not None else '?')
if f_at.valuation() == 0 and is_sq_res:
    v = K8(Fq(f_at).sqrt())
    for _ in range(7):
        v = (v + f_at/v) / 2
    P = Codd(uu, v)
    Q = Codd(uu, -v)
    val = Codd.coleman_integral(w, P, Q)
    out('  VERDICT INTEGRAL (over K8) = %s' % val)
    zero_verdict = (val.valuation() >= 8)
    out('  ANNIHILATION VERDICT: integral %s at precision 8' %
        ('= 0 (ANNIHILATED)' if zero_verdict else 'NONZERO'))
out('=== DONE ===')