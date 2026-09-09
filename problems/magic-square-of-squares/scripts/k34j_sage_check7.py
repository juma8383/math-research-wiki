print("E(K) rank via simon_two_descent over the number field")
from sage.all import *
K = QuadraticField(238, 's')
E = EllipticCurve(K, [0, 32, 0, 238, 0])
try:
    res = E.simon_two_descent()
    print("simon_two_descent:", res)
except Exception as e:
    print("failed:", str(e)[:250])
    try:
        lb, ub, gens = E.simon_two_descent(rank1_search_bound=10)
        print("with search bound:", lb, ub, gens)
    except Exception as e2:
        print("still failed:", str(e2)[:250])