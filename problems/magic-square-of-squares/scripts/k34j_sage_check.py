print("=== Sage capability check for the K34 gates ===")
from sage.all import *

# 1. Elliptic curve over Q with 2-descent
E = EllipticCurve([0, 32, 0, 238, 0])   # E_a
print("E_a:", E)
print("  rank =", E.rank())

# 2. Genus-2 hyperelliptic curve + Jacobian 2-descent
Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
P = HyperellipticCurve(fP)
print("P =", P)
J = P.jacobian()

# Stoll 2-descent on the Jacobian
res = J.two_descent(verbose=False)
print("two_descent result:", res)

# 3. Genus-3 curve Z_D
w = PolynomialRing(QQ, 'w').gen()
fZ = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + 56644
Z = HyperellipticCurve(fZ)
print("Z =", Z, " genus =", Z.genus())