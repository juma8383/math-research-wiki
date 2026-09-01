# Soundness-skeptic audit: corrected min-gap scans (overshoot region INCLUDED).
# Metric: A,B,C >= 2; gcd(A,B,C)=1; exclude exact (gap 0), gap-1, quasi-degenerate
# (A^p == C^r or B^q == C^r). No A bound (A picked as floor/ciel of rem^(1/p)).
import math

def floor_kth(n, k):
    if n < 1:
        return 0
    r = int(round(n ** (1.0 / k)))
    while (r + 1) ** k <= n:
        r += 1
    while r ** k > n:
        r -= 1
    return r

def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)

def scan(P, Q, R, C_MAX, B_MAX, label):
    best = []  # (gap, A, B, C, val)
    gap1_genuine = 0
    for C in range(2, C_MAX + 1):
        CR = C ** R
        for B in range(2, B_MAX + 1):
            BQ = B ** Q
            rem = CR - BQ
            if rem >= 2 ** P:
                fl = floor_kth(rem, P)
                cands = (fl, fl + 1)
            else:
                cands = (2, 3, 4)  # overshoot / small-rem region: small A wins
            for A in cands:
                if A < 2:
                    continue
                val = A ** P + BQ - CR
                g = abs(val)
                if g == 0:
                    continue
                if A ** P == CR or BQ == CR:
                    continue  # quasi-degenerate
                if g == 1:
                    if gcd3(A, B, C) == 1:
                        gap1_genuine += 1
                    continue
                if gcd3(A, B, C) != 1:
                    continue
                best.append((g, A, B, C, val))
    best.sort()
    print("=== %s  (C<=%d, B<=%d, corrected scan) ===" % (label, C_MAX, B_MAX))
    print("genuine gap-1 hits:", gap1_genuine)
    for t in best[:6]:
        print("  gap=%d at (A,B,C)=(%d,%d,%d)  [val=%+d]" % t)
    print()

# 1) The two bug-claim signatures, same box as the wiki scripts (C<=40, B<=600)
scan(3, 7, 11, 40, 600, "(3,7,11)")
scan(5, 7, 11, 40, 600, "(5,7,11)")

# 2) Corner spot-checks
scan(3, 5, 19, 3, 10000, "(3,5,19) CORNER (C<=3)")
scan(3, 5, 19, 60, 10000, "(3,5,19) FULL (C<=60, B<=1e4)")
scan(7, 13, 19, 3, 10000, "(7,13,19) CORNER (C<=3)")
scan(7, 13, 19, 20, 10000, "(7,13,19) PARTIAL (C<=20, B<=1e4)")

# 3) Boundary failures
scan(3, 3, 3, 40, 2000, "(3,3,3)")
scan(3, 3, 5, 40, 2000, "(3,3,5)")

# 4) Arithmetic identities from the shortlist
print("271^3+239^3 =", 271**3 + 239**3, "| 2^25-2 =", 2**25 - 2,
      "| equal:", 271**3 + 239**3 == 2**25 - 2)
print("2^5+3^7-2^11 =", 2**5 + 3**7 - 2**11)
print("2^3+3^7-2^11 =", 2**3 + 3**7 - 2**11)
print("13^3+2^7-2^11 =", 13**3 + 2**7 - 2**11)
print("11^5+4^7-3^11 =", 11**5 + 4**7 - 3**11)
print("65^3+12^5-2^19 =", 65**3 + 12**5 - 2**19)
print("7^7+2^13-2^19 =", 7**7 + 2**13 - 2**19)
print("6^3+5^3-7^3 =", 6**3 + 5**3 - 7**3)
print("6^5+3^7-2^13 =", 6**5 + 3**7 - 2**13)