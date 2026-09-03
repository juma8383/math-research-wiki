# mss_k34_leaf_census_ext.py -- extension of the [mss-k34-descent] leaf
# census (2026-09-03 continuation round).
# The four live layer-2 leaf quartics, exact integer arithmetic, extended
# ranges + the sliver s in [ceil(238^(1/4) r), 4r) the filed census skipped
# (claude_check D1 used s >= 4r; the true condition is s^4 > 238 r^4).
# Conditions verbatim from notes.md sec 6 / claude_check [D]:
#  D1 Q-pos(238,1):  u^2      = 238r^4+32r^2s^2+s^4, r even, 3|r, s odd,
#                    s^4 > 238 r^4, gcd(r,s)=1
#  D2 Q-neg(119,2):  u^2      = 32r^2s^2-119r^4-2s^4,  r odd, s even,
#                    F>0 and br=2s^4-119r^4>0 (exact interval, no floats),
#                    gcd(r,s)=1
#  D3 N-pos(17,14):  9u^2     = 17r^4+32r^2s^2+14s^4,  r odd, s even,
#                    br=14s^4-17r^4>0, br%3==0, F%9==0, gcd(r,s)=1
#  D4 N-neg(34,7):   9u^2     = 32r^2s^2-34r^4-7s^4,  r even, s odd,
#                    F>0 and br=7s^4-34r^4>0, br%3==0, F%9==0, gcd(r,s)=1
# A HIT would be a layer-2 solution -> candidate K34-A material (then the
# lift condition n+-2uv=(a+-b)^2 must be checked). ASCII output only.
from math import gcd, isqrt
import time

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_leaf_census_ext ==")
P("extension ranges: D1 r<=610 (6|r), s<=2400; D2 s<=3000; D3 r<=1000, s<=4000;"
  " D4 s<=3000")

tot = {}

# ---------- D1 Q-pos(238,1) ----------
h = 0; scanned = 0
for r in range(6, 611, 6):            # r even and 3|r -> 6|r, r<=610
    r2 = r*r; r4 = r2*r2
    # s odd, s^4 > 238 r^4, s <= 2400, gcd(r,s)=1
    smin = isqrt(isqrt(238*r4))       # floor((238 r^4)^(1/4))
    while smin**4 <= 238*r4: smin += 1
    if smin % 2 == 0: smin += 1
    for s in range(smin, 2401, 2):
        if gcd(r, s) != 1: continue
        scanned += 1
        s2 = s*s; s4 = s2*s2
        F = 238*r4 + 32*r2*s2 + s4
        if issq(F):
            h += 1; P("[D1] Q-pos(238,1) HIT", r, s, "u=", isqrt(F))
tot["D1 Q-pos(238,1)"] = (h, scanned)

# ---------- D2 Q-neg(119,2) ----------
h = 0; scanned = 0
for s in range(2, 3001, 2):           # s even
    s2 = s*s; s4 = s2*s2
    # r odd, F = 32r^2s^2-119r^4-2s^4 > 0, br = 2s^4-119r^4 > 0
    # br>0 -> r < (2/119)^(1/4) s = 0.36031 s ; F>0 -> r/s in (0.31433,0.41244)
    rmax = int(0.3604*s) + 1
    rmin = int(0.3140*s) - 1
    if rmin % 2 == 0: rmin += 1
    for r in range(max(rmin, 1), rmax + 1, 2):
        if gcd(r, s) != 1: continue
        r2 = r*r; r4 = r2*r2
        br = 2*s4 - 119*r4
        if br <= 0: continue
        F = 32*r2*s2 - 119*r4 - 2*s4
        if F <= 0: continue
        scanned += 1
        if issq(F):
            h += 1; P("[D2] Q-neg(119,2) HIT", r, s, "u=", isqrt(F))
tot["D2 Q-neg(119,2)"] = (h, scanned)

# ---------- D3 N-pos(17,14) ----------
h = 0; scanned = 0
for r in range(1, 1001, 2):           # r odd
    r2 = r*r; r4 = r2*r2
    for s in range(2, 4001, 2):       # s even
        if gcd(r, s) != 1: continue
        s2 = s*s; s4 = s2*s2
        br = 14*s4 - 17*r4
        if br <= 0 or br % 3 != 0: continue
        F = 17*r4 + 32*r2*s2 + 14*s4
        if F % 9 != 0: continue
        scanned += 1
        if issq(F // 9):
            h += 1; P("[D3] N-pos(17,14) HIT", r, s, "u=", isqrt(F//9))
tot["D3 N-pos(17,14)"] = (h, scanned)

# ---------- D4 N-neg(34,7) ----------
h = 0; scanned = 0
for s in range(1, 3001, 2):           # s odd
    s2 = s*s; s4 = s2*s2
    # r even, F = 32r^2s^2-34r^4-7s^4 > 0, br = 7s^4-34r^4 > 0
    # br>0 -> r/s < (7/34)^(1/4) = 0.67503 ; F>0 -> r/s in (0.58803,0.77158)
    rmax = int(0.6751*s) + 1
    rmin = int(0.5870*s) - 1
    if rmin % 2 == 1: rmin += 1
    for r in range(max(rmin, 2), rmax + 1, 2):
        if gcd(r, s) != 1: continue
        r2 = r*r; r4 = r2*r2
        br = 7*s4 - 34*r4
        if br <= 0 or br % 3 != 0: continue
        F = 32*r2*s2 - 34*r4 - 7*s4
        if F <= 0 or F % 9 != 0: continue
        scanned += 1
        if issq(F // 9):
            h += 1; P("[D4] N-neg(34,7) HIT", r, s, "u=", isqrt(F//9))
tot["D4 N-neg(34,7)"] = (h, scanned)

P("[TOTALS] (hits, scanned-after-filters):")
for k, v in sorted(tot.items()): P("   ", k, v)
P("== done ==")

with open("mss_k34_leaf_census_ext.log", "w") as fh:
    fh.write("\n".join(out) + "\n")