#!/usr/bin/env python
# K34 independent computational search (independent-search agent).
# Targets: master quartics
#   M_A: V^2 = X^4 + 132X^3 - 250X^2 + 132X + 1
#   M_B: V^2 = 9X^4 - 92X^3 + 310X^2 - 92X + 9
# A K34 counterexample <=> a rational point with X = Y^2, Y > 0, X != 1
# (Y = x = a/b in lowest terms, n0 = a^2+b^2 prime 1 mod 4).
#
# Task 1 (money search): square-X genus-3 covers, coprime m,n in [1,3000], m != n:
#   A-cover: (V n^4)^2 = m^8 + 132 m^6 n^2 - 250 m^4 n^4 + 132 m^2 n^6 + n^8
#   B-cover: (V n^4)^2 = 9 m^8 - 92 m^6 n^2 + 310 m^4 n^4 - 92 m^2 n^6 + 9 n^8
# Task 2: general rational-point census X = p/q, gcd=1, |p|,q <= 5000:
#   (V q^2)^2 = c4 p^4 + c3 p^3 q + c2 p^2 q^2 + c1 p q^3 + c0 q^4
# Task 3: height-stratified report of all points found.
# Any square-X hit is verified end-to-end (Fraction re-check + A/B reconstruction).
# ASCII output only.
import math
import time
from fractions import Fraction

BASE = r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts"
LOG = open(BASE + r"\mss_k34_ptssearch.log", "w", encoding="ascii", errors="replace")


def P(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


def isq(n):
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


COV = {
    "A": lambda m8, m6n2, m4n4, m2n6, n8: m8 + 132 * m6n2 - 250 * m4n4 + 132 * m2n6 + n8,
    "B": lambda m8, m6n2, m4n4, m2n6, n8: 9 * m8 - 92 * m6n2 + 310 * m4n4 - 92 * m2n6 + 9 * n8,
}

QUART = {
    "A": (1, 132, -250, 132, 1),
    "B": (9, -92, 310, -92, 9),
}


def cover_search(kind, BND):
    """Square-X cover search: X=(m/n)^2, gcd(m,n)=1, 1<=m,n<=BND, m!=n."""
    hits = []
    t0 = time.time()
    # precomputed power tables
    T2 = [0] * (BND + 1)
    T4 = [0] * (BND + 1)
    T6 = [0] * (BND + 1)
    T8 = [0] * (BND + 1)
    for v in range(1, BND + 1):
        v2 = v * v
        v4 = v2 * v2
        T2[v] = v2
        T4[v] = v4
        T6[v] = v4 * v2
        T8[v] = v4 * v4
    f = COV[kind]
    band = 250
    for mlo in range(1, BND + 1, band):
        mhi = min(BND, mlo + band - 1)
        for m in range(mlo, mhi + 1):
            m2, m4, m6, m8 = T2[m], T4[m], T6[m], T8[m]
            for n in range(1, BND + 1):
                if m == n or math.gcd(m, n) != 1:
                    continue
                N = f(m8, m6 * T2[n], m4 * T4[n], m2 * T6[n], T8[n])
                if N > 0 and isq(N):
                    V = math.isqrt(N)
                    hits.append((m, n, V))
                    P("COVER-HIT %s: m=%d n=%d V=%d  X=%s  Y=%s"
                      % (kind, m, n, V, Fraction(m * m, n * n), Fraction(m, n)))
        P("progress cover-%s m in [%d,%d] done; hits=%d; t=%.1fs"
          % (kind, mlo, mhi, len(hits), time.time() - t0))
    P("cover-%s TOTAL pairs-with-gcd-check done, hits=%d, t=%.1fs"
      % (kind, len(hits), time.time() - t0))
    return hits


def census(kind, BND, neg=True):
    """Rational-point census X=p/q, gcd=1, 1<=q<=BND, |p|<=BND (p>=0 if not neg)."""
    c4, c3, c2, c1, c0 = QUART[kind]
    hits = []
    t0 = time.time()
    plo = -BND if neg else 0
    for q in range(1, BND + 1):
        q2 = q * q
        q3 = q2 * q
        q4 = q2 * q2
        for p in range(plo, BND + 1):
            if math.gcd(p, q) != 1:
                continue
            p2 = p * p
            N = c4 * p2 * p2 + c3 * p2 * p * q + c2 * p2 * q2 + c1 * p * q3 + c0 * q4
            if N > 0 and isq(N):
                V = math.isqrt(N)
                hits.append((p, q, V))
        if q % 500 == 0:
            P("progress census-%s q<=%d done; hits=%d; t=%.1fs"
              % (kind, q, len(hits), time.time() - t0))
    P("census-%s TOTAL: %d points, t=%.1fs" % (kind, len(hits), time.time() - t0))
    return hits


def verify_square_hit(kind, m, n, V):
    """End-to-end verification of a square-X cover hit (a=m, b=n)."""
    P("VERIFY square hit: kind=%s m=%d n=%d V=%d" % (kind, m, n, V))
    x = Fraction(m, n)
    X = x * x
    if kind == "A":
        W = X ** 4 + 132 * X ** 3 - 250 * X ** 2 + 132 * X + 1
    else:
        W = 9 * X ** 4 - 92 * X ** 3 + 310 * X ** 2 - 92 * X + 9
    ok_frac = (W == Fraction(V * V, 1))
    P("  Fraction check V^2 == quartic(X): %s (X=%s)" % (ok_frac, X))
    a, b = m, n
    n0 = a * a + b * b
    s = a * a - b * b
    t = a * b
    Y_n = 4 * t * s
    R_n = abs(a ** 4 - 6 * a * a * b * b + b ** 4)
    ok_ident = (R_n * R_n + Y_n * Y_n == n0 ** 4)
    A_val = R_n * R_n + 9 * Y_n * Y_n
    B_val = 9 * R_n * R_n + Y_n * Y_n
    okA = isq(A_val)
    okB = isq(B_val)
    pr = is_prime(n0)
    P("  a=%d b=%d n0=a^2+b^2=%d prime=%s" % (a, b, n0, pr))
    P("  R_n=%d Y_n=%d  R^2+Y^2=n0^4: %s" % (R_n, Y_n, ok_ident))
    P("  A(n0): R^2+9Y^2=%d square=%s" % (A_val, okA))
    P("  B(n0): 9R^2+Y^2=%d square=%s" % (B_val, okB))
    verdict = "REFUTES-K34" if (okA or okB) and pr and n0 % 4 == 1 else "no-refutation"
    P("  VERDICT: %s" % verdict)
    return verdict


def report_points(name, hits):
    """Height-stratified report of census points (distinct X values)."""
    P("--- %s: %d points (p,q,V with (V q^2)^2 = quartic) ---" % (name, len(hits)))
    distinct = {}
    for (p, q, V) in hits:
        X = Fraction(p, q)
        if X not in distinct:
            distinct[X] = (p, q, V)
    rows = []
    for X, (p, q, V) in distinct.items():
        h = max(abs(p), q)
        sq = ""
        if p > 0 and isq(p * q):
            sq = "SQUARE-X (Y=%s)" % Fraction(math.isqrt(p * q), q)
        rows.append((h, X, p, q, V, sq))
    rows.sort()
    for h, X, p, q, V, sq in rows:
        P("  X=%-14s V=+-%d  (p=%d,q=%d)  height=%d  %s" % (str(X), V, p, q, h, sq))
    nsq = sum(1 for r in rows if r[5])
    P("%s summary: %d distinct X values, %d with square X" % (name, len(rows), nsq))
    return rows


def main():
    P("=== K34 independent point search, start ===")
    # ---- Part 0: code sanity -- known points must be reproduced ----------
    P("--- Part 0: sanity, known points on small boxes ---")
    ka = census("A", 40, neg=False)
    kb = census("B", 45, neg=False)
    P("known-in-box M_A (expect (0,1),(1,4),(31,35),(35,31) as (p,q,Vq^2) bases):")
    for (p, q, V) in ka:
        P("   (%d,%d) V*q^2=%d" % (p, q, V))
    P("known-in-box M_B (expect (0,3),(1,12),(5,41),(41,5)):")
    for (p, q, V) in kb:
        P("   (%d,%d) V*q^2=%d" % (p, q, V))

    # ---- Task 1: square-X cover searches ---------------------------------
    P("--- Task 1: square-X (genus-3 cover) searches, m,n <= 3000 ---")
    hitsA = cover_search("A", 3000)
    hitsB = cover_search("B", 3000)
    P("cover-A square-X hits: %d ; cover-B square-X hits: %d" % (len(hitsA), len(hitsB)))
    verdicts = []
    for (m, n, V) in hitsA:
        verdicts.append(verify_square_hit("A", m, n, V))
    for (m, n, V) in hitsB:
        verdicts.append(verify_square_hit("B", m, n, V))

    # ---- Task 2: general rational-point census ---------------------------
    P("--- Task 2: general rational-point census, |p|,q <= 5000 ---")
    censA = census("A", 5000, neg=True)
    censB = census("B", 5000, neg=True)

    # ---- Task 3: height-stratified report --------------------------------
    P("--- Task 3: height-stratified point report ---")
    report_points("M_A", censA)
    report_points("M_B", censB)

    P("--- SUMMARY ---")
    P("square-X cover hits: A=%d B=%d" % (len(hitsA), len(hitsB)))
    P("census (p,q) hits: M_A=%d M_B=%d" % (len(censA), len(censB)))
    P("K34 refutation verdicts: %s" % (verdicts if verdicts else "none (no square-X hits)"))
    P("=== done ===")


if __name__ == "__main__":
    main()