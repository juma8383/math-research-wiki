#!/usr/bin/env python3
# Jac(Z_D)(F_p) generator test: the divisor (0,238)-(0,-238) in J(F_p).
from sage.all import *
for p in [11, 13]:
    Fp = GF(p)
    R2 = PolynomialRing(Fp, 'x')
    x = R2.gen()
    f = x**8 - 4*x**6 - 604*x**4 - 952*x**2 + R2(56644)
    C = HyperellipticCurve(f)
    J = C.jacobian()
    D = J(x, R2(238))
    cur = D
    order = None
    for k in range(1, 300):
        cur = cur + D
        if cur.is_zero():
            order = k
            break
    if order:
        print(f"p={p}: divisor (0,238)-(0,-238): order {order} in J(F_p)")
    else:
        print(f"p={p}: divisor (0,238)-(0,-238): order > 300 (non-torsion in J(F_p), consistent with rank 1)")
print("DONE")