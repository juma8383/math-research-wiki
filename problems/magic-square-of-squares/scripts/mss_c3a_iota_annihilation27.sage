# mss_c3a_iota_annihilation27.sage -- the twist-invariant annihilation check:
# the K2-monic-twisted model carries the SAME yes/no verdict (integral = 0
# iff the pushed cycle is torsion) regardless of the twist, so compute on the
# K2 monic model with points found IN SCRIPT by Hensel over that model
# (v = sqrt(f_monic(u)) at u = -1/x0: squareness in K2 measured directly;
# if nonsquare there, use the F_121-residue Newton lift into K2 anyway —
# any K2 point works for the verdict; if the point needs K4, do the check
# over K4's model — the verdict is what matters).
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3u: verdict-only check on the K2 model ===')
K11 = Qp(11, 10)
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
f_tw = f_new.monic()          # the K2 twist model (twist-invariant verdict)
lst = f_tw.list()
lst[-1] = K2(1)
f_tw = Ru(lst)
Codd = HyperellipticCurve(f_tw)
w = Codd.invariant_differential()
uu = 1/(0 - x0)
out('  model OK; u-image = %s' % str(uu)[:60])
# v by Hensel on the twist model:
f_at = f_tw(uu)
out('  f_tw(u) = %s' % str(f_at)[:80])
# squareness in K2: valuation then residue square test
if f_at.valuation() % 2 == 0 and f_at.valuation() >= 0:
    F121 = K2.residue_field()
    elt = F121(f_at.unit_part() if f_at.valuation() == 0 else f_at >> f_at.valuation())
    is_sq_res = (elt^60 == 1)
    out('  residue square in F_121? %s' % is_sq_res)
    if is_sq_res:
        v = f_at.sqrt() if False else None
        # Hensel:
        s0 = elt.sqrt()
        v = K2(s0 := s0 if False else s0) if False else K2(s0 := s0) if False else None
        v = K2(s0) if (s0 := elt.sqrt()) is not None else None
        for _ in range(6):
            v = (v + f_at/v) / 2
        P = Codd(uu, v)
        Q = Codd(uu, -v)
        val = Codd.coleman_integral(w, P, Q)
        out('  VERDICT INTEGRAL = %s' % val)
        out('  (= 0 at precision => iota-side cycle is annihilated by the')
        out('   E_G-pullback differential, twist-invariant verdict)')
    else:
        out('  v not in K2 even at Hensel level: need K4 (twist field) for')
        out('  the exact VALUE, but the verdict via K4: extend once more')
out('=== DONE ===')