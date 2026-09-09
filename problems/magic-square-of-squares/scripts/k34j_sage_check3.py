print("Check descent functionality in this Sage build")
from sage.all import *

Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
C = HyperellipticCurve(fP)
J = C.jacobian()
print("curve class:", type(C).__name__)
print("jacobian class:", type(J).__name__)
print("methods on C with 'desc':", [m for m in dir(C) if 'desc' in m.lower()])
print("methods on J with 'desc':", [m for m in dir(J) if 'desc' in m.lower()])
print("methods on J with 'selmer':", [m for m in dir(J) if 'selmer' in m.lower()])
print("methods on C with 'rank':", [m for m in dir(C) if 'rank' in m.lower()])
print("L-series on J:", [m for m in dir(J) if 'L' in m][:12])