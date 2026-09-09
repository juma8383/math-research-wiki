# mss_c3a_annihilator_solve3.sage -- Coleman gate step 3b: the E_iota -> E_G
# map. [mss-k34-c3ab-prep] cont. Fix of solve2: isogenies_prime_degree(2) needs
# the curve's 2-torsion present; E_iota has only ONE rational 2-torsion? Its
# cubic y^2 = x^3 - 276480x + 240648192: 2-torsion points = roots of the cubic.
# Compute exactly; also compute the CORRECT correspondence: the iota quotient
# Q_iota (genus 1, base point (0,1)) and the G-quartic Q_G = w^2 = -512u^4+128u^2+1
# (base point (0,1)) are DIFFERENT genus-1 curves with different j. The
# correspondence C3_A between them: iota pushes to Q_iota, then the SECOND
# involution rho descends to Q_iota as an involution WITHOUT fixed points?
# A genus-1 curve with a fixed-point-free involution has genus-1 quotient
# (unramified double cover). Q_iota -> Q_G is then a degree-2 ISOGENY (via the
# base points) E_iota -> E_G -- unramified, so no extra ramification. Degree-2
# isogeny exists iff 2-torsion structure allows: E_iota has full rational
# 2-torsion? x^3 - 276480x + 240648192: roots?
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

out('=== U1: 2-torsion structure of E_iota and E_G (exact) ===')
EIOTA = EllipticCurve([0, 0, 0, -276480, 240648192])
EG    = EllipticCurve([0, 0, 0, -504576, 131604480])
Ti = EIOTA.torsion_subgroup()
TG = EG.torsion_subgroup()
out('  E_iota torsion:', Ti)
out('  E_G   torsion:', TG)
for T, name in ((Ti, 'E_iota'), (TG, 'E_G')):
    for P in T.gens():
        out('  %s torsion generator: %s (order %s)' % (name, P, P.order()))

out('=== U2: isogenies E_iota -> E_G via all rational 2-isogeny chains ===')
# A degree-2 isogeny E_iota -> E_G exists iff E_G is 2-isogenous to E_iota:
# (isogenous via a 2-isogeny <=> one has a rational 2-torsion point whose
# quotient curve is the other). Try Sage's E.isogeny(kernel point):
try:
    phis = EIOTA.isogenies_prime_degree(2)
    out('  isogenies_prime_degree(2) count:', len(phis))
    for phi in phis:
        try:
            Ecod = phi.codomain()
            j = Ecod.j_invariant()
            out('   codomain j:', j)
            if j == EG.j_invariant():
                out('   MATCH: E_iota -> E_G 2-isogeny exists!')
        except Exception as e:
            out('   codomain error:', str(e)[:120])
except Exception as e:
    # fall back: construct isogeny from a kernel generator manually
    out('  isogenies_prime_degree issue:', str(e)[:150])
    try:
        tpts = [P for P in EIOTA.torsion_points() if P.order() == 2] if hasattr(EIOTA, 'torsion_points') else []
    except Exception as e2:
        out('  fallback note:', str(e2)[:120])

out('=== U3: brute-force check: is E_G 2-isogenous to E_iota at all? ===')
# Compare Frobenius traces at small primes: isogenous curves have EQUAL traces.
def t_at(a4, a6, p):
    sq = set((i*i) % p for i in range(p))
    c = 1
    for x in range(p):
        v = (x*x*x + a4*x + a6) % p
        if v == 0: c += 1
        elif v in sq: c += 2
    return p + 1 - c
agree = 0; tot = 0
for p in prime_range(7, 100):
    tI = t_at(-276480, 240648192, p)
    tG = t_at(-504576, 131604480, p)
    # isogenous curves have the same number of points at EVERY good prime
    # (for isogenies over Q of any degree; traces equal as integers)
    if tI == tG:
        agree += 1
    tot += 1
out('  trace agreement at %d good primes 7..97: %d' % (tot, agree))
out('  (equal traces at all primes <=> Q-isogenous)')

out('=== U4: the honest structural reading ===')
# If traces disagree, E_iota and E_G are NOT isogenous, and the J(C3_A)
# decomposition iota/rho/EG means the INVOLUTION-composition structure is:
# J ~ E_iota x E_rho x E_G with E_iota = E_rho the two iota-type quotients and
# E_G the PRYM = the third factor, connected to C3_A by a correspondence of
# degree > 2. The MW annihilator then lives on C3_A directly; the quotient
# shortcut does NOT close the gate. Record and route to the direct approach:
# integrate on the E_G-COVER (the square-condition quartic w^2 = v^4+136v^2+16,
# genus 1 with base point!) -- THIS curve has Jacobian E_G and IS the cover:
# its Jacobian = E_G means Coleman on THIS genus-1 curve computes everything.
out('  (route decision printed by the run results)')
out('=== DONE ===')