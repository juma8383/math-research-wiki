# Euler-product evaluation of the "random D-set" heuristic for hourglass
# additive triples.  v4: v3 called mp.euler (Euler numbers) instead of
# mp.zeta and dropped the (1-1/p^2) local correction.
#
# S_k := sum_w P(w)^k / w^2,  P(w) = prod_{p=1(4)} (2 v_p(w)+1).
# Exact Euler product:
#   S_k = prod_{p=1(4)} T_p(k) * prod_{p not 1(4)} (1-1/p^2)^-1
#       = zeta(2) * prod_{p=1(4)} (1-1/p^2) * T_p(k),
#   T_p(k) = sum_{e>=0} (2e+1)^k p^-2e = closed forms (k=1,2,3), x=1/p^2:
#            (1+x)/(1-x)^2 ; (1+6x+x^2)/(1-x)^3 ; (1+23x+23x^2+x^3)/(1-x)^4.
# Model hourglass count  H = sum_w C(|D|,2)*24|D|/w^2 = (3/2)(S3-5S2+7S1-3S0)
# (upper bound: pairs with x+y > w^2 are invalid and only overcounted).

import math
from mpmath import mp, mpf

mp.dps = 40


def Tp(k, p):
    x = mpf(1) / (p * p)
    if k == 1:
        return (1 + x) / (1 - x) ** 2
    if k == 2:
        return (1 + 6 * x + x * x) / (1 - x) ** 3
    if k == 3:
        return (1 + 23 * x + 23 * x * x + x ** 3) / (1 - x) ** 4
    raise ValueError(k)


def Sk(k, N=2 * 10**6):
    sieve = bytearray([1]) * (N + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= N:
        if sieve[i]:
            start = i * i
            sieve[start::i] = b"\x00" * ((N - start) // i + 1)
        i += 1
    logp = mpf(0)
    for p in range(2, N + 1):
        if sieve[p] and p % 4 == 1:
            logp += mp.log((1 - mpf(1) / (p * p)) * Tp(k, p))
    # tail: sum_{p>N, 1(4)} (3k)/p^2 ~ (3k/2)/(N ln N)
    tail = mpf(3 * k) / 2 / (N * mp.log(N))
    return mp.zeta(2) * mp.e ** (logp + mp.log(1 + tail))


S0 = mp.zeta(2)
S1, S2, S3 = Sk(1), Sk(2), Sk(3)
H = mpf(3) / 2 * (S3 - 5 * S2 + 7 * S1 - 3 * S0)
# strict variant: density (|D|-2)/... -- the sum must be a third element
# distinct from x, y (automatic since x+y > x, y, but the naive count
# reserves |D| slots for it):  C(n,2)*24(n-2) = 12 n(n-1)(n-2)
#   = (3/2)(P-1)(P-3)(P-5)/w^2, expand: P^3-9P^2+23P-15.
Hs = mpf(3) / 2 * (S3 - 9 * S2 + 23 * S1 - 15 * S0)

print("Euler-product evaluation of the hourglass heuristic (mpmath, 40 dps)")
print("  S1 = %.10f" % S1)
print("  S2 = %.10f" % S2)
print("  S3 = %.10f" % S3)
print("  S0 = zeta(2) = %.10f" % S0)
print("  H = 1.5*(S3-5S2+7S1-3S0) = %.6f" % H)
print("  H strict (density |D|-2) = %.6f" % Hs)
print()
print("  Expected total number of hourglass triples (b, c, b+c in D(w^2),")
print("  b != c) over ALL centers w^2 (unbounded), naive random model.")
print("  Upper bound: pairs with x+y > w^2 are invalid and only overcounted.")

# sanity: S_k must be increasing in k (P^k pointwise increasing)
assert S1 < S2 < S3 and S1 > S0, "Euler products failed monotonicity"
print("  monotonicity S0 < S1 < S2 < S3: OK")