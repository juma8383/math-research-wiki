# mss_c3a_iota_annihilation6.sage -- odd model, FIXED: the transformed
# polynomial is a FRACTION of polynomials (numerator has a u^15/u^8 ratio —
# i.e. f(x0+1/u)*u^8 is a rational function: the u^-8..u^15 shape means
# f(x0+1/u)*u^8 has negative powers too — because f(x0 + 1/u) = sum a_k (x0+1/u)^k
# has terms (1/u)^8: multiplying by u^8 gives a Laurent polynomial, and Sage
# printed it as a FRACTION. The FIX: use the Laurent polynomial's numerator
# after common denominator, or better: since x0 is a ROOT of f,
# f(x0 + 1/u)*u^8 = u^8 * f(...)/u^8?? f(x0+1/u) = sum_k c_k (x0+1/u)^k has
# powers u^{-8}..u^0. * u^8 => powers u^0..u^8: a genuine polynomial!
# The fraction printed is because poly.roots() returned x0 as a p-adic whose
# (x0 + 1/u) arithmetic produced the denominator (1+O(11^8))*u^8 — the
# symbolic layer didn't expand. Force expansion via .numerator() or sympy
# expansion: use the expanded form: f_new = sum of (poly.coeffs) via expand():
import sys, time
def out(*a):
    print(*a); sys.stdout.flush()
T0 = time.time()
def el():
    return '%.0fs' % (time.time() - T0)

R.<x> = QQ[]
fA = x^8 + 132*x^6 - 250*x^4 + 132*x^2 + 1

out('=== I2g: odd model with forced polynomial expansion ===')
K11 = Qp(11, 8)
Rk.<X> = K11[]
K2.<c> = K11.extension(X^2 - 7)
poly = fA.change_ring(K2)
rts = poly.roots()
x0 = rts[0][0]
out('  x0 = %s' % x0)
Ru.<u> = K2[]
# compute f(x0 + 1/u) term by term to keep it polynomial:
f_new = Ru(0)
for k in range(9):
    c_k = poly.coefficients()[::-1][k] if len(poly.coefficients()) > k else K2(0)
for k in range(9):
    # poly is degree 8: coefficients ascending [a0..a8]
    pass
# robust: build from the root form: f(x0 + z) has a root at 0 (z=0), so
# f(x0 + 1/u) * u^8 = (sum over k of a_k (x0 + 1/u)^k) * u^8. Expand term by term:
f_new = Ru(0)
for k, c_k in enumerate(reversed(poly.coefficients())):   # c_0, c_1, ...? check order
    pass
# cleanest: use polynomial arithmetic: (poly(x0 + Ru(1)/u)) returns element of
# Ru? The division happened in the p-adic fraction field. Force into Ru by
# computing the Laurent polynomial and taking its polynomial part:
tmp = poly(x0 + 1/u) * u^8
out('  type of tmp: %s' % type(tmp))
f_new = Ru(tmp.numerator() / tmp.denominator()) if False else None
# force: compute each power series coefficient: f(x0 + 1/u) = sum_j b_j u^{-j}
# then f_new = sum_j b_j u^{8-j}: the b_j are exactly the Taylor coeffs:
b = []
one_u = 1/u
val = poly(x0 + 1/u)
# express val in u via .polynomial() if Laurent:
try:
    lau = Ru(val)
    out('  Laurent form ok')
except Exception as e:
    out('  Laurent error:', str(e)[:150])
# ALTERNATIVE simpler route: compute f_new symbolically over Q with symbolic x0
# is not possible (x0 is p-adic). Use: f_new = u^8 * f(x0 + 1/u) computed as
# sum_k a_k * u^(8-k) * (x0*u + 1)^k  -- all in Ru:
coeffs = poly.coefficients()  # ascending? verify degree:
out('  poly degree:', poly.degree())
f_new = Ru(0)
for j in range(poly.degree() + 1):
    aj = poly[j]
    # f = sum_j a_j (x0 + 1/u)^j = sum_j a_j (x0 u + 1)^j / u^j
    # => u^8 f = sum_j a_j (x0 u + 1)^j u^(8-j)
    f_new += aj * (x0*u + 1)^j * u^(8 - j)
out('  odd-model polynomial (expanded): degree = %d' % f_new.degree())
out('  %s' % f_new)
Codd = HyperellipticCurve(f_new)
out('  ODD model over Qp(11^2): OK')
w = Codd.invariant_differential()
out('  invariant differential:', w)
out('=== DONE ===')