#!/usr/bin/env python3
# brocard_rootofunity_exact.py
#
# EXACT enumeration of all square roots of unity modulo n! for n = 4..60.
#
# Lemma B2: if n!+1 = m^2 then m^2 = 1 (mod n!), i.e. m is a square root of
# unity mod n!.  For n >= 4 (so v2(n!) >= 3) the roots of x^2 = 1 (mod n!) are
# exactly the CRT combinations of
#   - 2-part 2^b, b = v2(n!) >= 3: four classes {1, -1, 1+2^(b-1), -(1+2^(b-1))}
#   - each odd prime power p^a || n!: two classes {+1, -1}
# so R(n) = 4 * 2^(pi(n)-1) = 2^(pi(n)+1).
#
# A solution m must additionally satisfy sqrt(n!) < m <= 2*sqrt(n!) (window),
# since m^2 = n! + 1 and (m+1)^2 = n! + 2m + 2 > n! + 1 forces m < 2 sqrt(n!)
# for all n >= 1 (2m + 2 > 0).  We enumerate ALL roots exactly and count the
# window hits, then exact-check every hit against math.factorial/isqrt and
# against m^2 == n!+1.
#
# ASCII output only.  Log: brocard_rootofunity_exact.log
import math
import sys
import time
import random

LOG = open("brocard_rootofunity_exact.log", "w", encoding="utf-8")


def out(s):
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def vp_factorial(n, p):
    s = 0
    q = p
    while q <= n:
        s += n // q
        q *= p
    return s


def components(n):
    """CRT components for x^2 = 1 mod n! as list of (modulus, [residues])."""
    comps = []
    b = vp_factorial(n, 2)
    M2 = 2 ** b
    comps.append((M2, [1, M2 - 1, 1 + (M2 >> 1), (M2 >> 1) - 1]))
    for p in primes_upto(n):
        if p == 2:
            continue
        a = vp_factorial(n, p)
        m = p ** a
        comps.append((m, [1, m - 1]))
    return comps


def enumerate_roots(comps):
    """All CRT combinations, folded incrementally with cached prefix inverses."""
    roots = [0]
    M = 1
    for (m, ress) in comps:
        inv = pow(M % m, -1, m)
        new = []
        ap = new.append
        for x in roots:
            rm = x % m
            for c in ress:
                t = ((c - rm) * inv) % m
                ap(x + M * t)
        roots = new
        M *= m
    return roots


def brute_roots(N):
    return [x for x in range(N) if x * x % N == 1]


def main():
    out("brocard_rootofunity_exact.py -- exact roots-of-unity window verification")
    out("window = (isqrt(n!), 2*isqrt(n!)];  R(n) expected = 2^(pi(n)+1) for n>=4")
    out("")

    # ---------- SELF-TEST 1: brute force vs CRT, n = 4..10 ----------
    out("SELF-TEST 1: CRT enumeration vs brute force (x*x mod N == 1), n=4..10")
    ok_all = True
    for n in range(4, 11):
        N = math.factorial(n)
        t0 = time.time()
        mine = sorted(enumerate_roots(components(n)))
        bf = brute_roots(N)
        ok = (mine == bf)
        ok_all = ok_all and ok
        out("  n=%2d  N=%9d  R_crt=%3d  R_brute=%3d  match=%s  (%.1fs)"
            % (n, N, len(mine), len(bf), ok, time.time() - t0))
        if not ok:
            out("    MISMATCH detail: crt-only=%s brute-only=%s"
                % (set(mine) - set(bf), set(bf) - set(mine)))
    out("SELF-TEST 1 RESULT: %s" % ("PASS" if ok_all else "FAIL"))
    out("")

    # ---------- SELF-TEST 2: every root satisfies x^2 = 1 mod n! ----------
    out("SELF-TEST 2: x^2 mod n! == 1 for ALL enumerated roots (n<=14), "
        "random sample of 64 for n>13")
    rng = random.Random(20260901)
    ok2 = True
    for n in range(4, 61):
        N = math.factorial(n)
        roots = enumerate_roots(components(n))
        if len(roots) <= 5000:
            bad = [x for x in roots if x * x % N != 1]
            cnt = len(roots)
        else:
            samp = rng.sample(roots, 64)
            bad = [x for x in samp if x * x % N != 1]
            cnt = 64
        if bad:
            ok2 = False
            out("  n=%2d FAIL: %d/%d bad roots" % (n, len(bad), cnt))
    out("SELF-TEST 2 RESULT: %s" % ("PASS" if ok2 else "FAIL"))
    out("")

    # ---------- MAIN: exact window census, n = 4..60 ----------
    out("MAIN CENSUS: n, pi(n), R(n) [exact count of roots], window hits, notes")
    brown = {4: 5, 5: 11, 7: 71}
    surprise = []
    t_start = time.time()
    for n in range(4, 61):
        t0 = time.time()
        N = math.factorial(n)
        pi_n = len(primes_upto(n))
        roots = enumerate_roots(components(n))
        R = len(roots)
        assert R == 2 ** (pi_n + 1), (n, R, pi_n)
        lo = math.isqrt(N)
        hits = [x for x in roots if lo < x <= 2 * lo]
        # exact-check every hit: m^2 == n!+1 ?
        exact_sols = [x for x in hits if x * x == N + 1]
        notes = []
        if n in brown:
            notes.append("known Brown m=%d present=%s"
                         % (brown[n], brown[n] in hits))
        if exact_sols:
            notes.append("*** EXACT SOLUTION m^2=n!+1: %s ***" % exact_sols)
            surprise.append((n, exact_sols))
        if hits and n >= 8:
            notes.append("UNEXPECTED window hit at n>=8 (not a solution "
                         "unless listed above)")
            surprise.append((n, hits))
        out("  n=%2d pi=%2d R=%7d win=%2d  hits=%s%s  (%.1fs)"
            % (n, pi_n, R, len(hits), hits,
               ("  [" + "; ".join(notes) + "]") if notes else "",
               time.time() - t0))
        sys.stdout.flush()
    out("")
    out("TOTAL elapsed: %.1f s" % (time.time() - t_start))
    out("")
    out("SUMMARY: window hits for n>=8 (would contradict clean equidistribution):")
    ns8 = [(n, h) for (n, h) in surprise if n >= 8 and
           not any(x * x == math.factorial(n) + 1 for x in h)]
    if not ns8:
        out("  NONE -- window occupancy occurs ONLY at n=4,5,7 through n=60.")
    else:
        for (n, h) in ns8:
            out("  n=%d hits=%s  exact-check m^2==n!+1: %s"
                % (n, h, [x * x == math.factorial(n) + 1 for x in h]))
    out("")
    out("SUMMARY: exact solutions m^2 = n!+1 found among all roots:")
    sols = [(n, h) for (n, h) in surprise
            if any(x * x == math.factorial(n) + 1 for x in h)]
    if not sols:
        out("  none beyond the known Brown numbers (which are confirmed above "
            "at n=4,5,7).")
    else:
        for (n, h) in sols:
            out("  n=%d m=%s" % (n, h))
    LOG.close()


if __name__ == "__main__":
    main()