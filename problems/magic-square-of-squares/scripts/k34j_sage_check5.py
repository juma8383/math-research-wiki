print("E over K rank test (2-descent over quadratic field)")
from sage.all import *
K = QuadraticField(238, 's')
E = EllipticCurve(K, [0, 32, 0, 238, 0])
try:
    r = E.rank()
    print("E(K).rank =", r)
except Exception as e:
    print("E.rank failed:", type(e).__name__, str(e)[:200])
    try:
        r = E.rank(proof=False)
        print("rank(proof=False) =", r)
    except Exception as e2:
        print("rank(proof=False) failed:", type(e2 := e).__name__, str(e)[:200])