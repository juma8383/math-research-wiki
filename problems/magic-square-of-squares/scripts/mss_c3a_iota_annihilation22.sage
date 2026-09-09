# mss_c3a_iota_annihilation22.sage -- K4 = K2(sqrt(fp)) construction: the odd
# model over the unramified quartic extension of Q_11. Route: build the
# degree-4 unramified extension directly over Q_11 with an explicit quartic
# modulus (an irreducible quartic whose reduction is the compositum), lift
# the same root x0, rebuild the transform (monic), and integrate.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I3p: unramified quartic extension ===')
K11 = Qp(11, 8)
Rk.<X> = K11[]
# irreducible quartic mod 11 containing both sqrt(7) and sqrt(fp) residues:
# try a generic quartic and check irreducibility: X^4 - 2 (2 is a NR mod 11?
# QRs mod 11: {1,3,4,5,9}: 2 NOT a QR; also need the quartic to CONTAIN the
# unramified quadratic subfield: X^4 - 2: F_11^2 inside? The splitting field
# of X^4-2 over F_11: deg = order of 2 in (Z/11)^*/gcd? x^4=2: 2 is a NR;
# the roots live in F_{11^2} iff 2^{(121-1)/2} = 1 i.e. 2 is a square in
# F_121 — squares of F_11 are squares of F_121? (11^2-1)/2 = 60: 2^60 in
# F_121: since F_121 = F_11(b): the norm map... simply: X^4 - 2 is
# irreducible mod 11 iff 2 is not a 4th power and X^2-2 is irreducible:
# 2 is a NR mod 11 => X^2-2 irreducible over F_11; X^4-2: either splits in
# F_121 (if 2 is a square in F_121) or irreducible (quartic). In F_121 =
# F_11(sqrt(7))... compute directly in Sage.
Rk2.<T> = GF(11)[]
for cand in [2, 5, 6, 7]:
    P4 = T^4 - cand
    try:
        f2 = F2.(b^2+7)
    except Exception:
        pass
    fac = (T^4 - cand).factor()
    if list(fac)[0][0].degree() == 4:
        out('  X^4 - %d irreducible mod 11 -> contains F_11^4' % cand)
        break
K4 = Qp(11, 8).extension(X^4 - 2) if False else None
Rq.<Y> = K11[]
K4 = Qp(11, 8).extension(Y^4 - 2, 'y')
out('  K4 = %s' % K4)
poly = fA.change_ring(K4)
rts = poly.roots()
out('  roots over Qp(11^4): %d' % len(rts))
x0 = rts[0][0]
Rv.<u> = K4[]
f_new = Rv(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
fp = f_new.leading_coefficient()
# now sqrt via residue: F_{11^4}^* order (11^4-1): square test:
t = fp^((11^4 - 1)//2)
out('  fp^((11^4-1)/2) == 1? %s' % (t == 1))
if t == 1:
    Fq = K4.residue_field()
    s_res = Fq(fp).sqrt()
    z = K4(s_res)
    for _ in range(5):
        z = (z + fp/z) / 2
    out('  sqrt(fp) = %s' % str(z)[:70])
    f_monic = f_new.monic()
    lst = f_monic.list(); lst[-1] = K4(1)
    f_mon2 = Rv(lst)
    Codd = HyperellipticCurve(f_mon2 := f_mon2 if False else f_mon2 if False else f_mon2 if False else Rv(lst))
    Codd = HyperellipticCurve(Rv(lst))
    w = Codd.invariant_differential()
    uu = 1/(0 - x0)
    vv = uu^4 / z
    diff = f_mon2(uu) - vv^2
    out('  on-curve check: %s' % str(diff)[:80])
    P = Codd(uu, vv)
    Q = Codd(uu, -vv)
    val = Codd.coleman_integral(w, P, Q)
    out('  ∫_{P}^{Q} dx/(2v) = %s' % val)
out('=== DONE ===')