#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Independent Legendre-symbol sieve for Brocard's problem n! + 1 = m^2.

For a prime p > n: n! mod p != 0, and if n! + 1 = m^2 then
    (n! + 1 | p) = 1   (it is a square mod p).
So any n with (n! + 1 | p) = -1 for SOME prime p > n is excluded.
Using many primes p > N sieves all n <= N at once.  Survivors (expected
~ N / 2^#primes) get an exact integer check.

Self-test: the exact-check hits must be exactly the known Brown numbers
(4,5), (5,11), (7,71) for n <= N.
"""
import sys
import time
from array import array
from math import isqrt, factorial

import numpy as np
from sympy import primerange

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
NPRIME = int(sys.argv[2]) if len(sys.argv) > 2 else 20
OUT = "brocard_sieve_N%d.log" % N


def legendre_all(vals, p):
    """Vectorized (a|p): returns array of 1 (QR) or p-1 (nonresidue)."""
    p64 = np.uint64(p)
    e = (p - 1) // 2
    base = np.asarray(vals, dtype=np.uint64) % p64
    result = None
    cur = base.copy()
    while e:
        if result is None:
            result = cur.copy() if (e & 1) else np.ones_like(cur)
        elif e & 1:
            result = (result * cur) % p64
        cur = (cur * cur) % p64
        e >>= 1
    return result if result is not None else np.ones_like(base)


def main():
    t0 = time.time()
    primes = []
    for p in primerange(N + 1, 4 * N):
        primes.append(p)
        if len(primes) >= NPRIME:
            break
    assert len(primes) >= 12
    log = []
    log.append("== Brocard Legendre sieve, N=%d, %d primes p in (%d, %d] =="
               % (N, len(primes), N, primes[-1]))
    alive = np.ones(N, dtype=bool)
    for p in primes:
        # n! mod p for n = 1..N  (n < p always, so nonzero)
        fac = array("I", bytes(4 * N))
        f = 1
        for n in range(1, N + 1):
            f = f * n % p
            fac[n - 1] = f
        fa = np.frombuffer(fac, dtype=np.uint32).astype(np.uint64) + 1
        ls = legendre_all(fa, p)
        alive &= ls != np.uint64(p - 1)
        log.append("prime %d: alive %d" % (p, int(alive.sum())))
        if not alive.any():
            log.append("  (all excluded at prime %d)" % p)
            break
    surv = np.nonzero(alive)[0] + 1
    log.append("after sieving: %d survivors" % len(surv))
    hits = []
    for n in surv:
        n = int(n)
        fn = factorial(n)
        r = isqrt(fn + 1)
        if r * r == fn + 1:
            hits.append((n, r))
    log.append("exact square hits: %s" % (hits,))
    log.append("time=%.1fs" % (time.time() - t0))
    txt = "\n".join(log)
    print(txt)
    with open(OUT, "w") as fh:
        fh.write(txt + "\n")


if __name__ == "__main__":
    main()