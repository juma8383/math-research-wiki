# mss_k34_zd_height_sharp3.sage -- fix of v2: Rational has no .nbits (use
# .numer().nbits() or just print); the minimality scan unchanged.
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<w> = QQ[]
f_oct = w^8 - 4*w^6 - 604*w^4 - 952*w^2 + 56644

out('=== H2b: discriminant-shift minimality test (fixed) ===')
base_disc = f_oct.discriminant()
out('  disc sign/size: %s (numerator %s digits)' %
    ('+' if base_disc > 0 else '-', len(str(abs(base_disc.numerator())))))
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
        out('   -> NON-MINIMAL: w -> w + %d lowers v to %d (drop %d)' % (bestt, best, v0 - best))
    else:
        out('   -> minimal in ±4 (no translation lowers v)')

out('=== S4b: sharp-constant assembly ===')
out('  (per-prime minimized valuations above; sharp C_finite uses them)')
out('=== DONE ===')