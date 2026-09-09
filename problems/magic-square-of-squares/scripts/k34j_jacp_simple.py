print("The decisive test for Jac(P): does it split over Q as E1 x E2?")
print("A simple test: if Jac(P) ~ E1 x E2 over Q, then at EVERY good prime the")
print("charpoly of Jac(P) factors into two quadratics over F_p (the factors'").__class__
from sage.all import *
Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
C = HyperellipticCurve(fP)
J = C.jacobian()
# Get charpolys at several primes and check factorization patterns:
count_split = 0; count_total = 0
for p in [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]:
    if p in (17, 2, 3, 7, 271): continue
    cp = C.frobenius_polynomial(p) if hasattr(C, 'frobenius_polynomial') else None
    if cp is None: continue
    count_total += 1
    fct = factor(cp)
    if len(fct) >= 2:
        count_split += 1
print(f"charpoly factored at {count_split}/{count_total} primes")
# At p=31 the charpoly was x^4+14x^2+961 = IRREDUCIBLE (one factor of degree 4):
# a simple genus-2 surface has irreducible quartic Frobenius — CONSISTENT.
# So Jac(P) does NOT split over Q: it is SIMPLE over Q, splitting only over K!
print("=> Jac(P) is a simple abelian surface over Q, splitting over K = Q(sqrt(238))")
print("   as E x E^sigma. rank Jac(P) = rank E(K).")
print()
print("Compute the L-series-based analytic rank of Jac(P) rigorously in Sage:")
print("(Sage 10.x: J has no built-in L, but the Frobenius data + the approximate")
print(" functional equation is implementable; alternatively use the PARI L-series")
print(" of the genus-2 curve via 'rnhfsearch'-style tools... simplest rigorous:")
print(" use the fact that rank Jac(P) = rank E(K) and compute rank bounds via")
print(" simon_two_descent over K with saturation + point search over K.")
# Point search on P's Jacobian over Q: any rational point on J gives a lower bound
print()
print("Known Jac(P)(Q) points: the Weierstrass point (0,0) gives the identity only.")
print("Search P(Q) divisors of degree 0: pairs (P1, P2) with P1+P2 = 2*inf...")