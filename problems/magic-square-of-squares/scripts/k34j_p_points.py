#!/usr/bin/env python3
# ROUND 5: (1) P(Q) point search (P: y^2 = x*N(x)); (2) deepen the Z_D sieve.
import math
import sys
sys.set_int_max_str_digits(2000000)
from fractions import Fraction as F

N = lambda x: x**4 - 4*x**3 - 604*x*x - 952*x + 56644

def issq(n):
    if n < 0: return False
    r = math.isqrt(n)
    return r*r == n

print("== 1. integer points on P: y^2 = x*N(x), x in [-300, 3000] ==")
hits = []
for x in range(-300, 3001):
    v = x * N(x)
    if v >= 0 and issq(v):
        hits.append((x, math.isqrt(v)))
print("integer hits:", hits)

print("\n== 2. rational points on P, x = p/q, q <= 30, p in [-200, 2000] ==")
rhits = []
for q in range(1, 41):
    q8 = q*q  # y^2 = p*N(p/q)/q^4 * q^4? y^2 = (p/q)*N(p/q) -> denominator q^4·? compute exactly:
    for pp in range(-300, 3001):
        if math.gcd(pp, q) != 1 and q != 1: continue
        xv = F(pp, q)
        v = xv * N(xv)   # Fraction
        if v >= 0 and math.isqrt(v.numerator)**2 == v.numerator and math.isqrt(v.denominator)**2 == v.denominator:
            rhits.append((xv, F(math.isqrt(v.numerator), math.isqrt(v.denominator))))
            if len(rhits) <= 10:
                print(f"  HIT: x = {xv}, y = {rhits[-1][1]}")
print(f"rational hits (q<=40): {len(rhits)}")