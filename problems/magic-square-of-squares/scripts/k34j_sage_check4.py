print("Sage check: what CAN we do for genus-2 rank and for elliptic curves over K?")
from sage.all import *

Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
C = HyperellipticCurve(fP)
J = C.jacobian()

# 1. Analytic rank via Frobenius data: use hyperelliptic L-series (sage has
#    'hypellfro' via PARI for the Frobenius; the analytic rank of J is the
#    order of vanishing of the L-series at s=1, computable numerically to
#    high precision from the Dirichlet series)
try:
    from sage.interfaces.hypellfro import hypellfro
    print("hypellfro available")
except Exception as e:
    print("hypellfro:", type(e).__name__)

# 2. The decisive piece: elliptic curves over QUADRATIC fields with rank
K = QuadraticField(238, 's')
print("K =", K)
# E over K: the Res structure means the pair curves E, E^sigma; a candidate:
# find E/K with the trace data. First test 2-descent over K for an elliptic curve:
E = EllipticCurve(K, [0, 32, 0, 238, 0])
print("E over K:", E)
r = E.rank(proof=False, engine='magma') if False else E.rank()
print("E(K).rank =", r)