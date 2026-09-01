"""
Strengthen the (3,5,7) near-miss analysis (attempt-12 / cycle 10).

Goals:
  1. Enumerate ALL gap-1 near-misses |A^3 + B^5 - C^7| == 1 over a range and
     classify each as degenerate (a base == 1) or genuine.
  2. Check whether every gap-1 hit lies on a universal degenerate family:
        t^21 + 1 : A=t^7, B=1, C=t^3  (A^3+B^5 = t^21+1 = C^7 + 1)
        t^35 + 1 : A=1, B=t^7, C=t^5  (A^3+B^5 = 1+t^35 = C^7 + 1)
     plus the symmetric C^7 - 1 = t^21 - 1 style (gap 1 the other way).
  3. Find the smallest NON-degenerate (all bases >= 2) coprime near-miss gap.

Run:  python search_357_nearmiss.py
"""
import math

A_MAX = 6000
B_MAX = 600
C_MAX = 200


def is_perfect_cube(n):
    if n < 1:
        return False
    r = round(n ** (1.0 / 3.0))
    for cand in (r - 1, r, r + 1):
        if cand >= 1 and cand * cand * cand == n:
            return True
    return False


def cube_root_exact(n):
    r = round(n ** (1.0 / 3.0))
    for cand in (r - 1, r, r + 1):
        if cand >= 1 and cand * cand * cand == n:
            return cand
    return None


def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)


# ---- gap-1 enumeration ---------------------------------------------------
# For each C and each sign s in {+1,-1}, for each B, A^3 = C^7 + s*1 - B^5.
gap1 = []
for C in range(1, C_MAX + 1):
    C7 = C ** 7
    for s in (+1, -1):
        target = C7 + s  # we want A^3 + B^5 = target, i.e. gap = A^3+B^5-C^7 = s
        for B in range(1, B_MAX + 1):
            B5 = B ** 5
            rem = target - B5
            if rem < 1:
                if B5 > target:
                    break  # B^5 only grows; further B only increases
                continue
            if rem > A_MAX ** 3:
                continue
            A = cube_root_exact(rem)
            if A is not None and A <= A_MAX:
                gap1.append((A, B, C, s))

# ---- classify degenerate & family membership ----------------------------
def family_of(A, B, C, s):
    # t^21 family: A=t^7, B=1, C=t^3, gap = +1 (t^21+1 - t^21)
    # t^35 family: A=1, B=t^7, C=t^5, gap = +1
    # also gap = -1 versions: C^7 - 1 vs ... but t^21-1 is not a sum of cube+fifth
    #   unless... check explicitly.
    if s == 1:
        # t^21 family
        if B == 1 and A >= 1:
            t = round(A ** (1.0 / 7.0))
            for tt in (t - 1, t, t + 1):
                if tt >= 1 and tt ** 7 == A and tt ** 3 == C:
                    return "t^21+1 (t=%d)" % tt
        # t^35 family
        if A == 1 and B >= 1:
            t = round(B ** (1.0 / 7.0))
            for tt in (t - 1, t, t + 1):
                if tt >= 1 and tt ** 7 == B and tt ** 5 == C:
                    return "t^35+1 (t=%d)" % tt
    return None


classified = []
unclassified_gap1 = []
for (A, B, C, s) in gap1:
    deg = (A == 1 or B == 1 or C == 1)
    fam = family_of(A, B, C, s)
    coprime = (gcd3(A, B, C) == 1)
    classified.append((A, B, C, s, deg, fam, coprime))
    if fam is None:
        unclassified_gap1.append((A, B, C, s, deg, coprime))

print("=== gap-1 near-misses |A^3+B^5-C^7|==1 over A<=%d B<=%d C<=%d ===" % (A_MAX, B_MAX, C_MAX))
print("total gap-1 hits:", len(gap1))
deg_count = sum(1 for r in classified if r[4])
gen_count = len(classified) - deg_count
print("degenerate (a base==1):", deg_count)
print("genuine (all bases>=2):", gen_count)
print("all gap-1 on a universal family:", all(r[5] is not None for r in classified))
print("unclassified gap-1 hits:", len(unclassified_gap1))
for r in unclassified_gap1[:30]:
    print("   UNCLASSIFIED:", r)

print()
print("=== sample gap-1 hits (first 20) ===")
for r in classified[:20]:
    print("   A=%d B=%d C=%d gap=%+d deg=%s fam=%s coprime=%s" % r)

# ---- smallest non-degenerate near-miss gap -------------------------------
def floor_cbrt(n):
    if n < 1:
        return 0
    r = int(round(n ** (1.0 / 3.0)))
    while (r + 1) ** 3 <= n:
        r += 1
    while r ** 3 > n:
        r -= 1
    return r


# Search |A^3 + B^5 - C^7| = g for increasing g, all bases >=2, coprime.
print()
print("=== smallest NON-degenerate (bases>=2) COPRIME near-miss ===")
best = None
for C in range(2, C_MAX + 1):
    C7 = C ** 7
    for B in range(2, B_MAX + 1):
        B5 = B ** 5
        rem = C7 - B5          # we want A^3 close to rem
        if rem < 8:
            continue
        fl = floor_cbrt(rem)   # largest A with A^3 <= rem
        for Atry in (fl, fl + 1):
            if Atry < 2 or Atry > A_MAX:
                continue
            val = Atry ** 3 + B5 - C7
            g = abs(val)
            if g == 0:
                continue
            if best is None or g < best[0]:
                if gcd3(Atry, B, C) == 1:
                    best = (g, Atry, B, C, val)
print("min non-degenerate coprime gap:", best)