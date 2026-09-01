"""Additive-freeness of D(p^k) for prime powers (specialization block).

Conjecture to test: for w = p^k (p = 1 mod 4 prime, k >= 1), the set
D(p^k) = {2uv : u^2+v^2 = p^(2k), u>v>0} is sum-free (no {x,y,x+y}),
AP-free, and parallelogram-free.

Builder via Gaussian integers: p = a^2+b^2 (a>b>0), pi = a+bi.  The reps
of p^k as u^2+v^2 come from z_j = pi^j * conj(pi)^(k-j), j = 0..k
(up to units and conjugation); taking u = |Re|, v = |Im| of z_j with
u > v > 0 gives the reps; d_j = 2*u_j*v_j.  |D(p^k)| = k exactly
(Lemma 1: (2k+1 - 1)/2).

Self-tests: D(5)= {24} (k=1); D(625) = D(25^2) = {336, 600} (k=2).
Cross-check against the general Pythagorean builder for a few w.
"""
import math

def gauss_mul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])

def d_prime_power(p, k):
    """D((p^k)^2): elements 2uv over reps u^2+v^2 = p^(2k)."""
    a = b = None
    for x in range(2, int(p**0.5) + 1):
        y2 = p - x * x
        y = math.isqrt(y2)
        if y * y == y2 and y > 0:
            a, b = x, y
            break
    if a is None:
        return None
    pi = (a, b)
    pc = (a, -b)
    els = set()
    for j in range(0, 2 * k + 1):
        # z = pi^j * pc^(2k-j)
        z = (1, 0)
        for _ in range(j):
            z = gauss_mul(z, pi)
        for _ in range(2 * k - j):
            z = gauss_mul(z, pc)
        u, v = abs(z[0]), abs(z[1])
        if u < v:
            u, v = v, u
        if u > v > 0:
            els.add(2 * u * v)
    return sorted(els)

# self-tests
assert d_prime_power(5, 1) == [24], d_prime_power(5, 1)
assert d_prime_power(5, 2) == [336, 600], d_prime_power(5, 2)
# cross-check with the general builder: w=25 gets elements from BOTH
# primitive s=25 (7,24 -> 336) and imprimitive s=5,k=5 (15,20 -> 600)
ds = set()
for m in range(2, 26):
    mm = m * m
    for n in range(1, m):
        s = mm + n * n
        if 25 % s:
            continue
        d0 = 2 * (mm - n * n) * (2 * m * n)
        k = 25 // s
        ds.add(d0 * k * k)
assert sorted(ds) == [336, 600], ds
print("self-tests PASS: D(25)=[336,600] both builders agree")

# census: all p = 1 mod 4, p < 2000, k with p^k <= 1e9
PRIMES = [p for p in range(5, 2000, 2) if all(p % q for q in range(3, int(p**0.5) + 1, 2)) and p % 4 == 1]
A2 = A3 = AP = 0
rows = []
worst = []
for p in PRIMES:
    k = 1
    while p**k <= 10**9:
        ds = d_prime_power(p, k)
        L = len(ds)
        assert L == k, (p, k, L)  # Lemma 1 check
        dset = set(ds)
        for i in range(L):
            for j in range(i + 1, L):
                x, y = ds[i], ds[j]
                if (x + y) in dset:
                    A2 += 1; print("A2 HIT", p, k, x, y, x + y)
                if (y - x) in dset:
                    AP += 1; print("AP HIT", p, k, x, y)
                    if (x + y) in dset:
                        pass
                if (x + y) in dset and (y - x) in dset:
                    A3 += 1; print("A3 HIT", p, k, x, y)
        if k >= 5:
            worst.append((p, k, L, ds[-1]))
        k += 1
print(f"prime powers tested: p<2000 (1 mod 4), p^k<=1e9")
print(f"A2 (additive triples)={A2}, A3 (parallelograms)={A3}, AP={AP}")
mx = max(worst, key=lambda t: t[2]) if worst else None
print("largest family:", mx)