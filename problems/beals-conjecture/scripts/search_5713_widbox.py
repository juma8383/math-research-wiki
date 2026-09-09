"""
Signature (5,7,13) WIDER-BOX gap census (attempt-26, node beal-nearmiss-5713-widbox-verify).

Attempt-24 (box A<=6000, B<=600, C<=40) found min genuine gap 1771 at (6,3,2),
flagged to-verify. This run widens the box to

    C <= 120,   B <= 2*10^4,   A unbounded above (every A >= 1 covered),

preserving the gap definitions of search_5713.py / near_miss_package.py
EXACTLY:
  genuine near-miss gap = min |A^5 + B^7 - C^13| over coprime (gcd(A,B,C)=1)
  bases with A,B,C >= 2, excluding exact solutions (gap 0); gap-1 hits are
  enumerated separately and labeled per the T1 universal families; the
  quasi-degenerate layer (A^5==C^13 or B^7==C^13, gap = B^7 resp. A^5) is
  excluded from the genuine min and tracked separately (T3).

Scan pattern = the CORRECTED scan of near_miss_package.py: the overshoot
region B^7 > C^13 is INCLUDED (candidates A in {2,3,4} there), fixing the
break-at-BQ>CR bug that the original search_5713.py min-gap loop carried.
A best-based break cuts the B loop once overshoot gaps provably exceed the
running best (mathematically safe: B^7 is increasing in B).

Universal degenerate gap-(+1) families for (p,q,r) = (5,7,13):
  t^65 + 1 : A = t^13, B = 1, C = t^5   [lcm(5,13) = 65]
  t^91 + 1 : A = 1, B = t^13, C = t^7   [lcm(7,13) = 91]

Run:  python search_5713_widbox.py    (PYTHONIOENCODING=utf-8; no external deps)
"""
import math, time

P, Q, R = 5, 7, 13
C_MAX = 120
B_MAX = 2 * 10 ** 4

TWO_P = 2 ** P   # 32: smallest A^5 with A >= 2


def iroot(n, k):
    """Exact integer floor k-th root of n >= 0."""
    if n < 1:
        return 0
    if n < 2 ** k:
        return 1
    r = 1 << ((n.bit_length() + k - 1) // k)
    while r ** k > n:
        r = ((k - 1) * r + n // r ** (k - 1)) // k   # Newton, decreasing
    while (r + 1) ** k <= n:
        r += 1
    return r


def exact_kth(n, k):
    if n < 1:
        return None
    r = iroot(n, k)
    return r if r ** k == n else None


def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)


BQ = [b ** Q for b in range(B_MAX + 1)]   # precomputed 7th powers, B <= 2e4


def family_of(A, B, C):
    """T1 universal gap-(+1) family label, else None."""
    if B == 1:
        t = iroot(A, R)
        if t >= 1 and t ** R == A and t ** P == C:
            return "t^65+1 (t=%d)" % t
    if A == 1:
        t = iroot(B, R)
        if t >= 1 and t ** R == B and t ** Q == C:
            return "t^91+1 (t=%d)" % t
    return None


t0 = time.time()

# ---- 1. exact solutions A^5 + B^7 = C^13 -----------------------------------
exact = []
exact_coprime = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for B in range(1, B_MAX + 1):
        rem = CR - BQ[B]
        if rem < 1:
            if BQ[B] > CR:
                break
            continue
        A = exact_kth(rem, P)
        if A is not None and A >= 1:
            exact.append((A, B, C))
            if gcd3(A, B, C) == 1:
                exact_coprime.append((A, B, C))

# ---- 2. gap-1 census |A^5 + B^7 - C^13| == 1 -------------------------------
gap1 = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for s in (+1, -1):
        target = CR + s
        for B in range(1, B_MAX + 1):
            rem = target - BQ[B]
            if rem < 1:
                if BQ[B] > target:
                    break
                continue
            A = exact_kth(rem, P)
            if A is not None and A >= 1:
                gap1.append((A, B, C, s))

# ---- 3. min genuine gap (corrected scan, overshoot region included) --------
best = None            # (gap, A, B, C, val); genuine = coprime, bases>=2, gap>1
best_at_C = {}         # C -> per-column best (Corner-Principle check)
quasi = None           # min coprime quasi-degenerate gap (T3 layer)
unit = None            # min unit-base |1 + B^7 - C^13| / |A^5 + 1 - C^13|
argmins = []
n_cand = 0
TOPN = 12
top = []
for C in range(2, C_MAX + 1):
    CR = C ** R
    c_best = None
    # unit-base channel (A=1 or B=1), other bases >= 2 (T1/T2 domain)
    b0 = iroot(CR, Q)
    for B in (b0, b0 + 1):
        if 2 <= B <= B_MAX:
            val = 1 + B ** Q - CR
            t = (abs(val), 1, B, C, val)
            if unit is None or t < unit:
                unit = t
    a0 = iroot(CR - 1, P)
    for A in (a0, a0 + 1):
        if A >= 2:
            val = A ** P + 1 - CR
            t = (abs(val), A, 1, C, val)
            if unit is None or t < unit:
                unit = t
    for B in range(2, B_MAX + 1):
        bqv = BQ[B]
        rem = CR - bqv
        if best is not None and rem < TWO_P and bqv - CR + TWO_P > best[0]:
            break   # overshoot gap >= bqv-CR+32 only grows with B
        if rem >= TWO_P:
            fl = iroot(rem, P)
            cands = (fl, fl + 1)
        else:
            cands = (2, 3, 4)   # small-rem AND overshoot region (corrected scan)
        for A in cands:
            if A < 2:
                continue
            n_cand += 1
            AP = A ** P
            val = AP + bqv - CR
            g = abs(val)
            if g == 0:
                continue
            if AP == CR or bqv == CR:
                if gcd3(A, B, C) == 1:
                    t = (g, A, B, C, val)
                    if quasi is None or t < quasi:
                        quasi = t
                continue
            if g == 1:
                continue        # enumerated by the census loop
            if gcd3(A, B, C) != 1:
                continue
            t = (g, A, B, C, val)
            if best is None or t[0] < best[0]:
                best = t
                argmins = [t]
            elif t[0] == best[0] and t not in argmins:
                argmins.append(t)
            if c_best is None or t < c_best:
                c_best = t
            if len(top) < TOPN or t < top[-1]:
                top.append(t)
                top.sort()
                del top[TOPN:]
    if c_best is not None:
        best_at_C[C] = c_best

corner = None
for C in (2, 3):
    cb = best_at_C.get(C)
    if cb is not None and (corner is None or cb < corner):
        corner = cb

# ---- report -----------------------------------------------------------------
print("=== (5,7,13) WIDER-BOX GAP CENSUS ===")
print("box: C<=%d, B<=%d, A unbounded (all A>=1 covered)" % (C_MAX, B_MAX))
print("chi = 1/5+1/7+1/13-1 = -264/455 ~ -0.5802")

print()
print("--- exact solutions A^5+B^7=C^13 ---")
print("total: %d | coprime: %d" % (len(exact), len(exact_coprime)))
for t in exact[:20]:
    print("   ", t, "gcd=%d" % gcd3(*t))

print()
print("--- gap-1 census |A^5+B^7-C^13|==1 ---")
n_unit = sum(1 for (A, B, C, s) in gap1 if A == 1 or B == 1 or C == 1)
g1_genuine = [g for g in gap1 if g[0] >= 2 and g[1] >= 2 and g[2] >= 2]
g1_gen_coprime = [g for g in g1_genuine if gcd3(*g[:3]) == 1]
print("total hits: %d | unit-base (T1 domain): %d | all-bases>=2: %d | coprime: %d"
      % (len(gap1), n_unit, len(g1_genuine), len(g1_gen_coprime)))
for (A, B, C, s) in gap1:
    d = (A == 1 or B == 1 or C == 1)
    print("   A=%d B=%d C=%d gap=%+d unit-base=%s fam=%s gcd=%d"
          % (A, B, C, s, d, family_of(A, B, C), gcd3(A, B, C)))

print()
print("--- min GENUINE coprime near-miss gap (bases>=2, gap>1, quasi-degenerate excluded) ---")
print("min: %s" % (best,))
print("argmins (%d): %s" % (len(argmins), argmins[:10]))
print("smallest distinct genuine gaps (top %d):" % len(top))
for t in top:
    print("   gap=%d at (A,B,C)=(%d,%d,%d) val=%+d gcd=%d" % (t[0], t[1], t[2], t[3], t[4], gcd3(t[1], t[2], t[3])))
print("per-C minima (C: gap@(A,B,C)):")
for C in sorted(best_at_C)[:12]:
    t = best_at_C[C]
    print("   C=%d: %d @ (%d,%d,%d)" % (C, t[0], t[1], t[2], t[3]))
print("Corner Principle: corner (C<=3) min = %s | full-box min = %s | holds=%s"
      % (corner[0] if corner else None, best[0] if best else None,
         (corner is not None and best is not None and corner[0] == best[0])))

print()
print("--- quasi-degenerate layer (A^5==C^13 or B^7==C^13), coprime, in box ---")
print("min: %s  [gap equals B^7 resp. A^5]" % (quasi,))

print()
print("--- unit-base channel (A=1 or B=1), other bases >= 2 ---")
print("min: %s" % (unit,))

print()
print("candidate (A,B,C) triples evaluated: %d" % n_cand)
print("elapsed: %.1fs" % (time.time() - t0))