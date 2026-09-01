# Pillai-2 search-bound extension: X^u - Y^v = 2, u,v odd primes.
# Extends the near_miss_package.py Part 4 bound (Y^v <= 1e18, u,v <= 23) to
# Y^v <= 1e21 with the FULL odd-prime range on BOTH exponents: since
# X^u = Y^v + 2 > Y^v >= 2^v, any prime exponent v with 2^v > B cannot occur,
# so enumerating primes v, 3 <= v <= log2(B) + u over ALL odd primes
# 3 <= u <= log2(N) (checked per N) is EXHAUSTIVE in exponents, not just
# u,v <= 23. Exact integer arithmetic throughout.

import math
import sys


def iroot(n, k):
    """Exact integer k-th root if it exists, else None. Newton from an
    upper-bound seed descends monotonically to floor(root); neighbors checked."""
    if n < 1:
        return None
    if k == 1:
        return n
    r = 1 << ((n.bit_length() + k - 1) // k)  # 2^ceil(bl/k) >= n^(1/k) > 0
    while True:
        rn = ((k - 1) * r + n // (r ** (k - 1))) // k
        if rn >= r:
            break
        r = rn
    for cand in (r - 2, r - 1, r, r + 1, r + 2):
        if cand >= 1 and cand ** k == n:
            return cand
    return None


def main(B):
    # odd primes v with 2^v <= B  (Y >= 2 => Y^v >= 2^v)
    vs = []
    lim = int(math.log2(B)) + 1
    sieve = [True] * (lim + 2)
    for p in range(2, lim + 1):
        if sieve[p]:
            for q in range(p * p, lim + 2, p):
                sieve[q] = False
    for p in range(3, lim + 1, 2):
        if sieve[p]:
            vs.append(p)
    us = [p for p in vs]  # odd primes up to lim — per-N we take u up to log2(N)
    checked = 0
    vY_checked = 0
    print("exponent range: v in %s ; u up to log2(N) per N (full odd-prime range)"
          % (vs,))
    for v in vs:
        Y = 2
        while True:
            Yv = Y ** v
            if Yv > B:
                break
            vY_checked += 1
            N = Yv + 2
            # u bound: X >= 2 => u <= log2(N)
            umax = N.bit_length()  # 2^u <= N => u <= log2(N)
            for u in us:
                if u > umax:
                    break
                checked += 1
                X = iroot(N, u)
                if X is not None and X >= 2:
                    print("SOLUTION: %d^%d - %d^%d = 2  (Y^v=%d <= %g)"
                          % (X, u, Y, v, Yv, B))
                    return
            Y += 1
    print("NO solutions X^u - Y^v = 2 with Y^v <= %g, ALL odd primes u,v with"
          " 2^v <= %g (exhaustive in exponents)" % (B, B))
    print("N-values (v,Y pairs) checked: %d ; individual (N,u) root checks: %d"
          % (vY_checked, checked))


if __name__ == "__main__":
    main(int(float(sys.argv[1])) if len(sys.argv) > 1 else 10 ** 21)