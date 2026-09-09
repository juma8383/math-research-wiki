print("Jac(P) simplicity test + rank bounds")
from sage.all import *
Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
fP = x**5 - 4*x**4 - 604*x**3 - 952*x**2 + 56644*x
C = HyperellipticCurve(fP)
J = C.jacobian()
sp = 0; tot = 0
for p in [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]:
    cp = C.frobenius_polynomial(p)
    tot += 1
    if len(factor(cp)) >= 2:
        sp += 1
    print("p=%d: %s" % (p, factor(cp)))
print("split at %d/%d primes" % (sp, tot))