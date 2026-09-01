#!/usr/bin/env python3
# brocard_dabrowski_general.py
#
# More-general statement (Dabrowski family): n! + A = m^2 for |A| <= 12.
# Brute force over n = 2..200, exact big-int arithmetic (isqrt check).
# Also records the structural sieve facts:
#   (S1) m^2 = A (mod n!)  => m is a square root of A mod n! (B2 generalization)
#   (S2) necessary: for every prime p <= n with p not dividing A, (A|p) = +1
#   (S3) necessary for n >= 4 (v2(n!) >= 3): A mod 8 in {0,1,4}
# ASCII output only.  Log: brocard_dabrowski_general.log
import math

LOG = open("brocard_dabrowski_general.log", "w", encoding="utf-8")


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


def legendre(a, p):
    return pow(a % p, (p - 1) // 2, p) if a % p else 0


def main():
    out("brocard_dabrowski_general.py -- n! + A = m^2, |A| <= 12, n = 2..200")
    out("")
    out("Per A: solutions (n, m) found, plus structural sieve flags.")
    out("S2 = A is a QR mod every prime p<=n with p|A false (necessary).")
    out("S3 = A mod 8 in {0,1,4} (necessary for n>=4; squares mod 8).")
    out("")
    all_sols = {}
    for A in range(-12, 13):
        sols = []
        for n in range(2, 201):
            N = math.factorial(n)
            v = N + A
            if v <= 0:
                continue
            r = math.isqrt(v)
            if r * r == v:
                sols.append((n, r))
        all_sols[A] = sols

        # S3 check
        s3 = (A % 8) in (0, 1, 4)
        # S2 check at the largest solution's n (if any): verify (A|p)=+1
        s2_detail = ""
        if sols:
            nmax = max(n for (n, m) in sols)
            badp = []
            for p in primes_upto(nmax):
                if A % p == 0:
                    continue
                if legendre(A, p) != 1:
                    badp.append(p)
            s2_detail = (" S2-check at nmax=%d: %s"
                         % (nmax, "all pass" if not badp
                            else "FAIL at p=%s" % badp[:8]))
        out("A=%4d  sols(n,m)= %s   S3(=A mod 8 in {0,1,4})=%s%s"
            % (A, sols if sols else "none", s3, s2_detail))
    out("")
    out("Asymmetry check (Brocard A=+1 vs A=-1):")
    out("  A=+1 solutions: %s" % all_sols[1])
    out("  A=-1 solutions: %s" % all_sols[-1])
    out("")
    out("Cross-check of the three known Brown numbers inside the table:")
    out("  n=4 m=5 (A=1), n=5 m=11 (A=1), n=7 m=71 (A=1) -- expect in A=+1 row")
    LOG.close()


if __name__ == "__main__":
    main()