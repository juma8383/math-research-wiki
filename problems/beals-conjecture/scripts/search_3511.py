"""
Signature (3,5,11) probe (attempt-13 / cycle 11): A^3 + B^5 = C^11.

Tests whether the rigidity found at (3,5,7) is uniform across the open class
of distinct-prime signatures, or signature-specific.

Universal degenerate gap-1 families for (p,q,r)=(3,5,11):
  t^33 + 1 : A=t^11, B=1, C=t^3   (A^3=t^33, C^11=t^33, gap +1)   [lcm(3,11)=33]
  t^55 + 1 : A=1, B=t^11, C=t^5   (B^5=t^55, C^11=t^55, gap +1)  [lcm(5,11)=55]

Run:  python search_3511.py
"""
import math

P, Q, R = 3, 5, 11
A_MAX = 6000
B_MAX = 6000
C_MAX = 40   # C^11 grows fast; A_MAX^3 ~ 2.16e14 => C^11 <= that => C<=~20 for A-dominated, ~35 with B


def floor_kth(n, k):
    if n < 1:
        return 0
    r = int(round(n ** (1.0 / k)))
    while (r + 1) ** k <= n:
        r += 1
    while r ** k > n:
        r -= 1
    return r


def exact_kth(n, k):
    if n < 1:
        return None
    r = floor_kth(n, k)
    return r if r ** k == n else None


def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)


# ---- exact solutions A^3 + B^5 = C^11 ------------------------------------
exact = []
exact_coprime = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for B in range(1, B_MAX + 1):
        BQ = B ** Q
        rem = CR - BQ
        if rem < 1:
            if BQ > CR:
                break
            continue
        A = exact_kth(rem, P)
        if A is not None and 1 <= A <= A_MAX:
            exact.append((A, B, C))
            if gcd3(A, B, C) == 1:
                exact_coprime.append((A, B, C))

print("=== exact solutions A^3+B^5=C^11 over A<=%d B<=%d C<=%d ===" % (A_MAX, B_MAX, C_MAX))
print("total exact:", len(exact), "| coprime:", len(exact_coprime))
for t in exact[:30]:
    print("   ", t, "gcd=%d" % gcd3(*t))

# ---- gap-1 near-misses |A^3+B^5-C^11|==1 --------------------------------
def family_of(A, B, C, s):
    if s != 1:
        return None
    # t^33 family: A=t^11, B=1, C=t^3
    if B == 1 and A >= 1:
        t = floor_kth(A, 11)
        if t >= 1 and t ** 11 == A and t ** 3 == C:
            return "t^33+1 (t=%d)" % t
    # t^55 family: A=1, B=t^11, C=t^5
    if A == 1 and B >= 1:
        t = floor_kth(B, 11)
        if t >= 1 and t ** 11 == B and t ** 5 == C:
            return "t^55+1 (t=%d)" % t
    return None


gap1 = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for s in (+1, -1):
        target = CR + s
        for B in range(1, B_MAX + 1):
            BQ = B ** Q
            rem = target - BQ
            if rem < 1:
                if BQ > target:
                    break
                continue
            if rem > A_MAX ** P:
                continue
            A = exact_kth(rem, P)
            if A is not None and 1 <= A <= A_MAX:
                gap1.append((A, B, C, s))

print()
print("=== gap-1 near-misses |A^3+B^5-C^11|==1 ===")
print("total gap-1:", len(gap1))
deg = sum(1 for (A, B, C, s) in gap1 if A == 1 or B == 1 or C == 1)
print("degenerate:", deg, "| genuine (all bases>=2):", len(gap1) - deg)
allfam = all(family_of(*g) is not None for g in gap1)
print("all on a universal family:", allfam)
for g in gap1[:40]:
    A, B, C, s = g
    print("   A=%d B=%d C=%d gap=%+d deg=%s fam=%s" % (A, B, C, s, (A == 1 or B == 1 or C == 1), family_of(*g)))

# ---- min non-degenerate coprime near-miss gap ----------------------------
print()
print("=== min NON-degenerate (bases>=2) COPRIME near-miss ===")
best = None
for C in range(2, C_MAX + 1):
    CR = C ** R
    for B in range(2, B_MAX + 1):
        BQ = B ** Q
        rem = CR - BQ
        if rem < 8:
            continue
        fl = floor_kth(rem, P)
        for Atry in (fl, fl + 1):
            if Atry < 2 or Atry > A_MAX:
                continue
            val = Atry ** P + BQ - CR
            g = abs(val)
            if g == 0:
                continue
            if best is None or g < best[0]:
                if gcd3(Atry, B, C) == 1:
                    best = (g, Atry, B, C, val)
print("min non-degenerate coprime gap:", best)