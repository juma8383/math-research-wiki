# mss_k34_descent_p5.py -- K34-A descent part 5: CORRECTED layer-2 kill
# tables. p4's T2 wrongly tied the mod-3 condition to parity classes.
# Here all conditions are tested jointly over r,s mod 144 = lcm(16,9):
#   Family Q ((1,72),(72,1)):  F := d1 r^4+32r^2s^2+d2 s^4 = x^2 with x odd
#     (branch A>0) or F = 32r^2s^2-d1r^4-d2s^4 = x^2 > 0 (branch A<0);
#     n = d2 s^4 - d1 r^4, need n = 1 mod 4, n odd; rs even; gcd(r,s)=1.
#   Family N ((9,8),(8,9)): 9x^2 = F (same two branches), 3n = br,
#     n = 1 mod 4 => br = 3 mod 4, 3 | br, and F = 0 mod 9.
# Also sign-achievability: br > 0 and F > 0 must be simultaneously possible
# for real magnitudes (interval overlap in x = r^2/s^2).
# Exact integer arithmetic. ASCII output only.
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

P("== mss_k34_descent_p5 (corrected layer-2 tables) ==")
SPLITS = [(d1, 238//d1) for d1 in range(1,239) if 238 % d1 == 0
          and gcd(d1, 238//d1) == 1]
M = 144
SQ9 = {0,1,4,7}

def table(fam):
    res = {}
    for branch in ("pos", "neg"):
        for (d1, d2) in SPLITS:
            ok = []
            for r in range(M):
                for s in range(M):
                    if (r*s) % 2 != 0:      # rs even
                        continue
                    if gcd(r, s) % 3 == 0 and (r % 3 or s % 3):
                        pass
                    if branch == "pos":
                        F = d1*r**4 + 32*r*r*s*s + d2*s**4
                    else:
                        F = 32*r*r*s*s - d1*r**4 - d2*s**4
                    if F % 16 not in (1, 9):
                        continue            # x odd
                    br = d2*s**4 - d1*r**4
                    if fam == "Q":
                        if br % 4 != 1:     # n = br = 1 mod 4
                            continue
                        if F % 9 not in SQ9:
                            continue
                    else:
                        if br % 4 != 3 or br % 3 != 0:
                            continue
                        if F % 9 != 0:
                            continue
                    ok.append((r % 16, s % 16, r % 9, s % 9))
            if ok:
                res[(branch, d1, d2)] = ok[:6]
    return res

P("[Q] family Q (cases (1,72),(72,1)) surviving residues:")
rq = table("Q")
for k in sorted(rq): P("   ", k, "->", rq[k][0], " nclasses", len(rq[k]))
P("[Q] survivors:", sorted(rq.keys()))

P("[N] family N (cases (9,8),(8,9)) surviving residues:")
rn = table("N")
for k in sorted(rn): P("   ", k, "->", rn[k][0], " nclasses", len(rn[k]))
P("[N] survivors:", sorted(rn.keys()))

# sign achievability: for each survivor, x = r^2/s^2 must satisfy
#   pos branch: x < d2/d1   (br > 0)   [F > 0 automatic]
#   neg branch: 2x^2-32x+d1*d2... F>0 iff 34x^2-32x+d1*d2 < 0 form:
#   F>0 iff -(d1 x^2 - 32 x + d2) > 0 iff d1 x^2 -32x + d2 < 0;
#   br>0 iff x < d2/d1.
import math
def interval(branch, d1, d2):
    # x-interval where F > 0 (neg branch) ; pos branch: all x>0
    if branch == "pos":
        return (0.0, float("inf"))
    a, b, c = d1, -32.0, d2
    disc = b*b - 4*a*c
    if disc <= 0: return None
    lo = (32 - math.sqrt(disc)) / (2*a)
    hi = (32 + math.sqrt(disc)) / (2*a)
    return (lo, hi)
P("[S] sign achievability (need br>0 i.e. x < d2/d1, plus F>0 interval):")
for fam, tab in (("Q", rq), ("N", rn)):
    for (branch, d1, d2) in sorted(tab):
        iv = interval(branch, d1, d2)
        if iv is None:
            P("   ", fam, branch, (d1,d2), " F>0 empty -> KILLED")
            continue
        ok = iv[0] < d2/d1 and iv[1] > 0
        P("   ", fam, branch, (d1,d2), " F>0 x-interval",
          (round(iv[0],4), round(iv[1],4)), " br>0 needs x<", round(d2/d1,4),
          " -> achievable:", ok)

# QR refinement: for prime p | r (gcd(r,s)=1 => p !| s):
#   pos branch: F = x^2 (fam Q) or 9x^2 (fam N) => d2 s^4 = F mod p
#   => (d2/p) = 1;  neg branch: -d2 s^4 = F => (-d2/p) = 1 (fam Q),
#   fam N: F = 9x^2 => (-d2/p) = 1 as well (9 square). Similarly p | s.
# Any split where some prime p | d1 or d2 has (±d/p) = -1 and the split
# forces p | that variable is constrained but NOT killed (p need not divide
# r or s). Report the QR characters for the record.
P("[QR] Legendre symbols (d/p) for p | 238*... reference:")
for (d1, d2) in SPLITS:
    row = []
    for p_ in (7, 17):
        for dd, nm in ((d1, "d1"), (d2, "d2")):
            if d1 % p_ and d2 % p_: continue
        row.append((p_, d1 % p_, d2 % p_))
    # (d/p) via Euler
    def leg(d, p_):
        d = d % p_
        if d == 0: return 0
        return 1 if pow(d, (p_-1)//2, p_) == 1 else -1
    P("   ", (d1,d2), " (d1/7)=", leg(d1,7), " (d2/7)=", leg(d2,7),
      " (d1/17)=", leg(d1,17), " (d2/17)=", leg(d2,17),
      " (-d1/17)=", leg(-d1,17), " (-d2/17)=", leg(-d2,17))

with open("mss_k34_descent_p5.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p5 done, log written ==")