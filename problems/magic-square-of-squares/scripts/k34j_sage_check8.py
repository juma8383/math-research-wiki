print("E(K) rank descent with larger search + saturation; also gens search")
from sage.all import *
K = QuadraticField(238, 's')
E = EllipticCurve(K, [0, 32, 0, 238, 0])
lb, ub, gens = E.simon_two_descent(rank1_search_bound=20)
print("2-descent: rank lower bound", lb, " upper", ub, " gens:", gens)
# point search on E(K) for generators
try:
    g = E.gens()
    print("gens:", g)
except Exception as e:
    print("gens:", str(e)[:150])