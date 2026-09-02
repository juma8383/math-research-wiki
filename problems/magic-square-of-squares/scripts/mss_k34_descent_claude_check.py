# mss_k34_descent_claude_check.py -- independent verification of the
# [mss-k34-descent] filing (Claude main-loop, per protocol).
#  [A] delta lemma: d = gcd(R-V', R+V') for coprime a,b <= 400 with V'
#      taken as the integer sqrt of the octic when it exists, ELSE delta
#      checked structurally: gcd(R-V', R+V') computed with V' := the
#      formal sqrt is impossible, so instead verify on all (a,b) where
#      the octic IS a square (degenerate points) + polynomial identity.
#      Simpler robust check: verify R^2 - 4608 a^4 b^4 == octic expansion
#      for all a,b <= 60 (polynomial identity, exact), and verify the
#      delta rule on the known degenerate solutions (a,b) = (0,1),(1,1).
#  [B] constant-pair exhaustiveness for j in {1,3}.
#  [C] final layer-2 kill table with CORRECTED conditions (fixes 5+6):
#      joint test over r,s mod 144 per (family, branch, split).
#  [D] census of the four final live leaves (incl. the two revived ones
#      Q-neg(119,2), N-neg(34,7), never searched in a saved script).
#  [E] layer-1 census reproduction (12 survivors, 1 full hit).
# Exact integer arithmetic. ASCII output only.
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_descent_claude_check ==")

# ---------- [A] identity + delta ----------
P("[A] polynomial identity R^2-4608a^4b^4 == a^8+132a^6b^2-250a^4b^4+132a^2b^6+b^8:")
bad = 0
for a in range(0, 61):
    for b in range(0, 61):
        R = a**4 + 66*a*a*b*b + b**4
        lhs = R*R - 4608*a**4*b**4
        rhs = a**8 + 132*a**6*b*b - 250*a**4*b**4 + 132*a*a*b**6 + b**8
        if lhs != rhs: bad += 1
P("[A] identity mismatches a,b<=60:", bad)

# delta rule on degenerate solutions: V'^2 = octic must be a perfect square
P("[A] delta rule on all coprime (a,b) <= 400 with octic a perfect square:")
degen = []
for a in range(0, 401):
    for b in range(1, 401):
        from math import gcd as g
        if g(a, b) != 1: continue
        oct_ = a**8 + 132*a**6*b*b - 250*a**4*b**4 + 132*a*a*b**6 + b**8
        if issq(oct_):
            V = isqrt(oct_)
            R = a**4 + 66*a*a*b*b + b**4
            d = gcd(R - V, R + V)
            par = (a % 2, b % 2)
            exp = 2 if (par == (1,0) or par == (0,1)) else (8 if par == (1,1) else None)
            ok = (exp is None) or (d == exp)
            degen.append((a, b, d, exp, ok))
            if not ok:
                P("[A] DELTA MISMATCH", a, b, "delta=", d, "expected", exp)
P("[A] degenerate points found:", degen[:10], " total", len(degen),
  " all ok:", all(t[4] for t in degen))

# ---------- [B] constant-pair exhaustiveness ----------
P("[B] coprime fourth-power-free constant pairs (c1*c2 = 2^(9-2j) 3^2), j=1,3:")
for j in (1, 3):
    N = 2**(9-2*j) * 9
    pairs = []
    for c1 in range(1, N+1):
        if N % c1: continue
        c2 = N // c1
        if gcd(c1, c2) != 1: continue
        # fourth-power-free
        def fpf(m):
            for p in (2, 3):
                while m % (p**4) == 0: m //= p**4
            return m
        if fpf(c1) != c1 or fpf(c2) != c2: continue
        pairs.append((c1, c2))
    P("[B] j=", j, " pairs:", sorted(pairs))

# ---------- [C] final kill table (fixes 5+6 applied) ----------
P("[C] layer-2 joint mod-144 table with corrected conditions:")
SQ9 = {0, 1, 4, 7}
SPLITS = [(d1, 238//d1) for d1 in range(1, 239) if 238 % d1 == 0
          and gcd(d1, 238//d1) == 1]
M = 144

def interval(branch, d1, d2):
    if branch == "pos":
        return (0.0, float("inf"))
    a_, b_, c_ = float(d1), -32.0, float(d2)
    disc = b_*b_ - 4*a_*c_
    if disc <= 0: return None
    return ((32 - disc**0.5) / (2*a_), (32 + disc**0.5) / (2*a_))

final = []
for fam in ("Q", "N"):
    for branch in ("pos", "neg"):
        for (d1, d2) in SPLITS:
            ok = 0
            for r in range(M):
                for s in range(M):
                    if (r*s) % 2 != 0: continue
                    if branch == "pos":
                        F = d1*r**4 + 32*r*r*s*s + d2*s**4
                    else:
                        F = 32*r*r*s*s - d1*r**4 - d2*s**4
                    if F % 16 not in (1, 9): continue
                    br = d2*s**4 - d1*r**4
                    if fam == "Q":
                        if br % 4 != 1: continue        # n = br = 1 mod 4
                        if 3 % 1 == 0 and br % 3 == 0: continue  # 3 | n dead
                        if F % 9 not in SQ9: continue
                    else:
                        if br % 4 != 3 or br % 3 != 0: continue
                        if (br//3) % 3 == 0: continue   # 3 | n dead
                        if F % 9 != 0: continue
                    ok += 1
            # sign achievability with CORRECTED bounds (fix 5):
            # pos: need x^2 < d2/d1 (br > 0); neg: F>0 interval AND x^2<d2/d1
            iv = interval(branch, d1, d2)
            sign_ok = False
            if iv is not None:
                hi = min(iv[1], (d2/d1)**0.5)
                lo = max(iv[0], 0.0)
                sign_ok = lo < hi
            if ok and sign_ok:
                final.append((fam, branch, d1, d2))
            if ok and not sign_ok:
                P("[C] mod-survivor KILLED by sign:", fam, branch, (d1, d2))
P("[C] FINAL survivors (mod conditions + corrected sign):")
for t in sorted(final): P("[C]    ", t)

# ---------- [D] census of the four final leaves ----------
P("[D] leaf census:")
tot = {}
# D1 Q-pos(238,1): u^2 = 238r^4+32r^2s^2+s^4, r even, s odd, s>=4r, r<=600
h = 0
for r in range(2, 601, 2):
    for s in range(max(4*r, 1), 1201, 2):
        if gcd(r, s) != 1: continue
        F = 238*r**4 + 32*r*r*s*s + s**4
        if issq(F): h += 1; P("[D] Q-pos(238,1) HIT", r, s)
tot["Q-pos(238,1)"] = h
# D2 Q-neg(119,2): u^2 = 32r^2s^2-119r^4-2s^4, r odd, s even,
#    r/s in (0.314,0.360), r,s <= 1500
h = 0
for s in range(2, 1501, 2):
    lo = int(0.314*s) - 2; hi = int(0.360*s) + 2
    for r in range(max(lo, 1), hi+1, 2):
        if gcd(r, s) != 1: continue
        if not (0.314 < r/s < 0.360): continue
        F = 32*r*r*s*s - 119*r**4 - 2*s**4
        if F > 0 and issq(F): h += 1; P("[D] Q-neg(119,2) HIT", r, s)
tot["Q-neg(119,2)"] = h
# D3 N-pos(17,14): 9u^2 = 17r^4+32r^2s^2+14s^4, r odd, s even, br>0, r<=300
h = 0
for r in range(1, 301, 2):
    for s in range(2, 1201, 2):
        if gcd(r, s) != 1: continue
        F = 17*r**4 + 32*r*r*s*s + 14*s**4
        br = 14*s**4 - 17*r**4
        if F % 9 == 0 and br > 0 and br % 3 == 0 and issq(F // 9):
            h += 1; P("[D] N-pos(17,14) HIT", r, s)
tot["N-pos(17,14)"] = h
# D4 N-neg(34,7): 9u^2 = 32r^2s^2-34r^4-7s^4, r even, s odd,
#    r/s in (0.588,0.674), r,s <= 1500
h = 0
for s in range(1, 1501, 2):
    lo = int(0.588*s) - 2; hi = int(0.674*s) + 2
    for r in range(max(lo, 2), hi+1, 2):
        if gcd(r, s) != 1: continue
        if not (0.588 < r/s < 0.674): continue
        F = 32*r*r*s*s - 34*r**4 - 7*s**4
        br = 7*s**4 - 34*r**4
        if F > 0 and br > 0 and br % 3 == 0 and F % 9 == 0 and issq(F // 9):
            h += 1; P("[D] N-neg(34,7) HIT", r, s)
tot["N-neg(34,7)"] = h
P("[D] totals:", tot)

# ---------- [E] layer-1 census (8 cases, max(u,v) <= 900) ----------
P("[E] layer-1 census n^2 = c1 u^4 - 64 u^2 v^2 + c2 v^4 + lift:")
LIM = 900
surv = []
for (c1, c2) in ((1, 72), (8, 9), (9, 8), (72, 1)):
    for j in (1, 3):
        for u in range(1, LIM+1):
            for v in range(1, LIM+1):
                if gcd(u, v) != 1: continue
                # parity rules: j=1 -> exactly one of u,v even; j=3 -> both odd
                if j == 1 and (u+v) % 2 != 1: continue
                if j == 3 and (u % 2 or v % 2) != 1: continue
                n2 = 2**(j-1)*(c1*u**4 + c2*v**4) - 64*u*u*v*v
                if n2 <= 0 or not issq(n2): continue
                n = isqrt(n2)
                if n % 4 != 1: continue
                m = u*v
                if issq(n + 2*m) and issq(n - 2*m):
                    surv.append((u, v, c1, c2, j, n))
P("[E] full layer-1 hits (lift ok):", surv)
# count n^2-square survivors without lift (for the 12-survivor comparison)
cnt = 0
for (c1, c2) in ((1, 72), (8, 9), (9, 8), (72, 1)):
    for j in (1, 3):
        for u in range(1, LIM+1):
            for v in range(1, LIM+1):
                if gcd(u, v) != 1: continue
                if j == 1 and (u+v) % 2 != 1: continue
                if j == 3 and (u % 2 or v % 2) != 1: continue
                n2 = 2**(j-1)*(c1*u**4 + c2*v**4) - 64*u*u*v*v
                if n2 > 0 and issq(n2):
                    n = isqrt(n2)
                    if n % 4 == 1: cnt += 1
P("[E] n^2-square survivors (no lift), all 8 cases:", cnt)

with open("mss_k34_descent_claude_check.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== done, log written ==")