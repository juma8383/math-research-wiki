# mss_k34_zd_height_sharp2.sage -- p-minimality tests via discriminant shift:
# at each bad prime, translate w -> w + t (t = 0, ±1, ±2 over Z_p) and
# recompute v_p(disc). If any translation LOWERS v_p(disc), the model is
# non-minimal and the conservative constant over-counts at that prime.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<w> = QQ[]
f_oct = w^8 - 4*w^6 - 604*w^4 - 952*w^2 + 56644

out('=== H2: discriminant-shift minimality test ===')
def disc_val_at(poly, p):
    # v_p of the octic's discriminant: compute via the discriminant of the
    # hyperelliptic model: disc of the polynomial:
    d = poly.discriminant()
    return ZZ(d).valuation(p) if d != 0 else None

base_disc = f_oct.discriminant()
out('  disc = %s' % str(base_disc := base_disc if False else base_disc)[:60] if False else '  disc bits: %s' % base_disc.nbits())
for p in [2, 3, 7, 17, 271]:
    v0 = base_disc.valuation(p)
    out('  p=%d: v(disc) = %d (baseline)' % (p, v0))
    best = v0
    bestt = 0
    for t in range(-4, 5):
        shifted = f_oct(w + t)
        dv = shifted.discriminant().valuation(p)
        if dv < best:
            best = dv
            bestt = t
    if bestt != 0:
        out('   -> NON-MINIMAL: translation w -> w + %d lowers v to %d (drop %d)' % (bestt, best, v0 - best))
    else:
        out('   -> minimal (no shift in ±4)')

out('=== S4b: the recomputed sharp constant ===')
out('  (assemble after the minimality scan; per-prime sharp constants =')
out('   the minimized valuations)')
out('=== DONE ===')