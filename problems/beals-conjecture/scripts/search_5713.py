"""
Signature (5,7,13) probe (attempt-24 / cross-problem loop cycle 22): A^5 + B^7 = C^13.

Tests the prediction from attempt-19 (counting heuristic), confirmed at
(3,7,11) attempt-20 and (5,7,11) attempt-23: the min non-degenerate COPRIME
near-miss gap should grow monotonically as chi = 1/p+1/q+1/r-1 grows more
negative. The (5,7,11) run (attempt-23) found a DECELERATION: the largest
-chi jump (+0.133) gave the smallest gap increase (277->288, +11). This fifth
point tests whether the deceleration continues or reverses.
  (3,5,7):  chi = -34/105  ~ -0.324  -> min gap 29
  (3,5,11): chi = -62/165  ~ -0.376  -> min gap 77
  (3,7,11): chi = -100/231 ~ -0.433  -> min gap 277
  (5,7,11): chi = -218/385 ~ -0.566  -> min gap 288  (deceleration, attempt-23)
  (5,7,13): chi = -264/455 ~ -0.580  -> PREDICTION: min gap > 288  [this run]

Universal degenerate gap-1 families for (p,q,r)=(5,7,13):
  t^65 + 1 : A=t^13, B=1, C=t^5  (A^5=t^65, C^13=t^65, gap +1) [lcm(5,13)=65]
  t^91 + 1 : A=1, B=t^13, C=t^7  (B^7=t^91, C^13=t^91, gap +1) [lcm(7,13)=91]

Run:  python search_5713.py
"""
import math

P, Q, R = 5, 7, 13
A_MAX = 6000
B_MAX = 600
C_MAX = 40   # C^13 grows very fast; 40^13 ~ 2.7e20 (over-cover; min sits small)


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


# ---- exact solutions A^5 + B^7 = C^13 ------------------------------------
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
        if rem > A_MAX ** P:
            continue
        A = exact_kth(rem, P)
        if A is not None and 1 <= A <= A_MAX:
            exact.append((A, B, C))
            if gcd3(A, B, C) == 1:
                exact_coprime.append((A, B, C))

print("=== exact solutions A^5+B^7=C^13 over A<=%d B<=%d C<=%d ===" % (A_MAX, B_MAX, C_MAX))
print("total exact:", len(exact), "| coprime:", len(exact_coprime))
for t in exact[:30]:
    print("   ", t, "gcd=%d" % gcd3(*t))

# ---- gap-1 near-misses |A^5+B^7-C^13|==1 --------------------------------
def family_of(A, B, C, s):
    if s != 1:
        return None
    # t^65 family: A=t^13, B=1, C=t^5
    if B == 1 and A >= 1:
        t = floor_kth(A, 13)
        if t >= 1 and t ** 13 == A and t ** 5 == C:
            return "t^65+1 (t=%d)" % t
    # t^91 family: A=1, B=t^13, C=t^7
    if A == 1 and B >= 1:
        t = floor_kth(B, 13)
        if t >= 1 and t ** 13 == B and t ** 7 == C:
            return "t^91+1 (t=%d)" % t
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
print("=== gap-1 near-misses |A^5+B^7-C^13|==1 ===")
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
        if rem < 32:  # A>=2 => A^5>=32
            if BQ > CR:
                break
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
print()
print("chi values: (3,5,7)=%.4f (gap 29) | (3,5,11)=%.4f (gap 77) | (3,7,11)=%.4f (gap 277) | (5,7,11)=%.4f (gap 288) | (5,7,13)=%.4f"
      % (-34/105, -62/165, -100/231, -218/385, -264/455))