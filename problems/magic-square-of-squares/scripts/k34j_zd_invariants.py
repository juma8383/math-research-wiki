#!/usr/bin/env python3
# Step 1 of the height bound: Z_D invariants + local data at bad primes.
# Z_D : V^2 = w^8 - 4w^6 - 604w^4 - 952w^2 + 56644  (genus 3 hyperelliptic)
# from sage.all import *
# R.<w> = PolynomialRing(QQ)
# f = w^8 - 4*w^6 - 604*w^4 - 952*w^2 + 56644
# C = HyperellipticCurve(f)
# print("genus:", C.genus())
# for p in [2,3,7,17,271]:
#     print(p, C.local_data(p) if hasattr(C,'local_data') else 'n/a')
# Sage: hyperelliptic local data not direct; use the discriminant of the
# sextic-octic model + Stoll's local invariants via the odd-degree model?
# The degree-8 model: use HyperellipticCurve(f, 0) — Sage computes the
# discriminant; for the height bound the KEY datum is the discriminant's
# valuation at each bad prime (reduction type input).
from sage.all import *
R = PolynomialRing(QQ, 'w')
w = R.gen()
f = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + 56644
print("disc of f:", f.discriminant())
for p in [2, 3, 7, 17, 271, 11, 13]:
    d = f.discriminant()
    print(f"v_{p}(disc) =", ZZ(d).valuation(p))
print("DONE")