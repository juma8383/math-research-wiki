#!/usr/bin/env python3
# Point counts of Z_D over F_p at the Coleman primes (11, 13) + extras.
# Z_D : V^2 = w^8 - 4w^6 - 604w^4 - 952w^2 + 56644
# Count affine solutions (w, V) mod p + the points at infinity (1 or 2 for
# even-degree models: 2 if the leading coeff (1) is a QR — leading form at
# infinity: V^2 = w^8 (monic): two points at infinity always (V = ±w^4·1):
# so +2 for every good p).
from sage.all import *
def count_points(p):
    Fp = GF(p)
    cnt = 0
    for wi in range(p):
        w = Fp(wi)
        val = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + Fp(56644)
        # count w with val a square (including 0):
        if val == 0:
            cnt += 1
        elif val**((p-1)//2) == 1:
            cnt += 2
    # points at infinity: 2 (leading coefficient 1 is a square in every F_p)
    return cnt + 2

for p in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
    print(f"#Z_D(F_{p}) = {count_points(p)}", flush=True)
print("DONE")