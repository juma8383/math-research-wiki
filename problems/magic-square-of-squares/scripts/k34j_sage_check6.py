print("Test: E(K).rank with more descent effort; and the analytic rank over K")
from sage.all import *
K = QuadraticField(238, 's')
E = EllipticCurve(K, [0, 32, 0, 238, 0])
# push the 2-descent with saturation/point search
r1 = E.rank(proof=False, only_use_mwrank=True)
print("rank via mwrank:", r1)
# analytic rank over number fields:
try:
    ar = E.analytic_rank()
    print("analytic rank =", ar)
except Exception as e:
    print("analytic_rank failed:", str(e)[:150])
# gens found so far
try:
    g = E.gens()
    print("gens:", g)
except Exception as e:
    print("gens failed:", str(e)[:200])