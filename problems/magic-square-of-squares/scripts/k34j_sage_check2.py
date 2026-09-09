print("=== Sage check 2: correct two-descent entry points ===")
from sage.all import *

Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
C = HyperellipticCurve(fP)
J = C.jacobian()

# two_descent lives on the CURVE for odd-degree models (Stoll), not on J
try:
    res = C.two_descent(verbose=False, proof=False)
    print("C.two_descent:", res)
except Exception as e:
    print("C.two_descent failed:", type(e).__name__, str(e)[:120])

# alternative: the Magma-style entry point
try:
    res = J.curve().two_descent(verbose=False, proof=False)
    print("J.curve().two_descent:", res)
except Exception as e:
    print("fallback failed:", str(e)[:120])