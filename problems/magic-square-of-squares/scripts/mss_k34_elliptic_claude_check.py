#!/usr/bin/env python
# Claude pre-fanout check for the K34 -> genus-1 reduction.
# Part 1: verify A(n) = t^4 (u^4+136u^2+16), B(n) = t^4 (9u^4-56u^2+144)
#         and R^2+Y^2 = n^4, on 1 mod 4 primes (exact Fractions).
# Part 2: small rational-point search on the master quartics
#         M_A: V^2 = X^4 + 132X^3 - 250X^2 + 132X + 1
#         M_B: V^2 = 9X^4 - 92X^3 + 310X^2 - 92X + 9
#         (X = (a/b)^2 must be a rational square > 1 for a real hit)
import math
from fractions import Fraction

def is_square(n):
    if n < 0: return False
    r = math.isqrt(n)
    return r*r == n

# ---- Part 1: identity check --------------------------------------------
bad = 0; cnt = 0; nmax = 20000
sieve = [True]*(nmax+1); sieve[0]=sieve[1]=False
for i in range(2, int(nmax**0.5)+1):
    if sieve[i]:
        for j in range(i*i, nmax+1, i): sieve[j] = False
primes = [p for p in range(5, nmax+1, 4) if sieve[p]]
for n in primes:
    # find a^2+b^2 = n with a > b > 0
    a = None; b = None
    for aa in range(math.isqrt(n), 0, -1):
        r = n - aa*aa
        if r > 0 and is_square(r):
            bb = math.isqrt(r)
            if aa > bb > 0:
                a, b = aa, bb
                break
    if a is None:
        bad += 1; print("REPR FAIL", n); continue
    s = a*a - b*b; t = a*b
    u = Fraction(s, t)
    Y = 4*t*t*u          # should be integer 4ab(a^2-b^2)
    R = t*t*abs(u*u - 4) # should be integer |a^4-6a^2b^2+b^4|
    if Y.denominator != 1 or R.denominator != 1:
        bad += 1; print("UFORM NONINT", n); continue
    Y = Y.numerator; R = R.numerator
    QA = u**4 + 136*u**2 + 16
    QB = 9*u**4 - 56*u**2 + 144
    if R*R + 9*Y*Y != t**4 * QA or 9*R*R + Y*Y != t**4 * QB or R*R + Y*Y != n**4:
        bad += 1; print("IDENTITY FAIL", n)
    cnt += 1
print("part1: primes tested", cnt, "failures", bad)

# ---- Part 2: rational point search on M_A, M_B --------------------------
# X = p/q lowest terms, 0 <= p,q <= BND; V^2 = (q^4*quartic(p/q)) must be square
def search(coeffs, BND, name):
    # coeffs = [c4,c3,c2,c1,c0]; (V*q^2)^2 = sum c_i p^i q^(4-i)
    hits = []
    for p in range(0, BND+1):
        p2 = p*p; p3 = p2*p; p4 = p2*p2
        for q in range(1, BND+1):
            if math.gcd(p, q) != 1: continue
            q2 = q*q
            N = coeffs[0]*p4 + coeffs[1]*p3*q + coeffs[2]*p2*q2 + coeffs[3]*p*q2*q + coeffs[4]*q2*q2
            if N >= 0 and is_square(N):
                hits.append((p, q, math.isqrt(N)))
    print(name, "hits:", hits)

search([1, 132, -250, 132, 1], 300, "M_A")
search([9, -92, 310, -92, 9], 300, "M_B")
print("done")