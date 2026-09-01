#!/usr/bin/env python
# Independent verification of T4-f / Theorem L claims (Claude, fresh code).
# Convention (per filed scripts): T-units, circle [0,4); windows of {a,b} =
# components of {1 < aT mod 4 < 3} intersect {1 < bT mod 4 < 3};
# B_c arcs = closed [(4k-1)/c, (4k+1)/c]; window fits <=> exists k with
# 4k-1 <= c*lo and c*hi <= 4k+1.
import math
from fractions import Fraction

def windows(a, b, TMAX=4):
    """Boundary-event sweep, Fractions, independent implementation."""
    ev = set()
    for v in (a, b):
        k = 0
        while Fraction(4*k - 1, v) <= TMAX or Fraction(4*k + 1, v) <= TMAX:
            for e in (Fraction(4*k - 1, v), Fraction(4*k + 1, v)):
                if 0 < e < TMAX:
                    ev.add(e)
            k += 1
    pts = sorted(ev)
    wins = []
    seg = [Fraction(0)] + pts + [Fraction(TMAX)]
    for i in range(len(seg) - 1):
        lo, hi = seg[i], seg[i+1]
        if hi <= lo:
            continue
        m = (lo + hi) / 2
        if 1 < (m*a) % 4 < 3 and 1 < (m*b) % 4 < 3:
            if wins and abs(wins[-1][1] - lo) == 0:
                wins[-1] = (wins[-1][0], hi)
            else:
                wins.append((lo, hi))
    # merge nothing across boundaries handled by equality of Fractions
    return wins

def fits(w, c):
    lo, hi = w
    # exists integer k: 4k-1 <= c*lo and c*hi <= 4k+1
    k = 0
    while Fraction(4*k - 1, c) <= hi + 1:
        if 4*k - 1 <= c*lo and c*hi <= 4*k + 1:
            return True
        k += 1
        if k > 4*c + 2:
            break
    return False

def pair_cond(a, b, c):
    return all(fits(w, c) for w in windows(a, b))

# --- Test 1: T4-f statement, all primitive triples a<b<c<=50
hits = []
n = 0
for a in range(1, 51):
    for b in range(a+1, 51):
        for c in range(b+1, 61):
            if math.gcd(math.gcd(a, b), c) != 1:
                continue
            n += 1
            if pair_cond(a, b, c):
                hits.append((a, b, c))
print("TEST1 T4-f box a<b<c(<=50,60): triples checked", n)
print("  hits:", hits[:10], "... total", len(hits))

# --- Test 2: Theorem L, b-a>=2: ml == 2/b exactly (coprime a<b<=40)
bad = []
for a in range(1, 41):
    for b in range(a+2, 41):
        if math.gcd(a, b) != 1:
            continue
        ws = windows(a, b)
        ml = max((w[1]-w[0] for w in ws), default=Fraction(0))
        if ml != Fraction(2, b):
            bad.append((a, b, ml))
print("TEST2 Theorem L (b-a>=2, a<b<=40): mismatches", len(bad), bad[:5])

# --- Test 3: (1,2) windows and c=3 pass, c=4 fail (hand-check mirror)
w12 = windows(1, 2)
print("TEST3 windows(1,2):", w12)
print("  c=3:", pair_cond(1, 2, 3), "  c=4:", pair_cond(1, 2, 4),
      "  c=5:", pair_cond(1, 2, 5))