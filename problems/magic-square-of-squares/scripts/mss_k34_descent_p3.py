# mss_k34_descent_p3.py -- K34-A descent part 3:
# layer-3 checks on the Germain splits of cases (1,72), (9,8).
# Exact integer arithmetic. ASCII output only.
import sys
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_descent_p3 ==")

SPLITS = [(d1, 238//d1) for d1 in range(1,239) if 238 % d1 == 0
          and gcd(d1, 238//d1) == 1]

# ---------------------------------------------------------------
# L1 (case 1,72): 9u^2 = d1 r^4 + 32 r^2 s^2 + d2 s^4 ... wait: u^2 =
#   d1 r^4 + 32 r^2 s^2 + d2 s^4,  n = d2 s^4 - d1 r^4 = a^2+b^2 odd, 1 mod 4,
#   v = rs even, u odd.  (Layer-2 of case (1,72).)
# L2 (case 9,8):  W=9u^2-32v^2, (W-3n)/2 = d1 r^4, (W+3n)/2 = d2 s^4,
#   d1 d2 = 238, rs = v, W = d1 r^4 + d2 s^4, 3n = d2 s^4 - d1 r^4,
#   9 u^2 = W + 32 v^2 = d1 r^4 + 32 r^2 s^2 + d2 s^4, 3 | d2 s^4 - d1 r^4,
#   u odd (case (9,8): u odd, v even).
# Projective local test of  F(r,s) = d1 r^4 + 32 r^2 s^2 + d2 s^4 = square
# over F_p, with the extra integrality: value must be a square (u^2) resp.
# 9*square, plus 3 | d2 s^4 - d1 r^4 for L2 (only meaningful mod 3).
# ---------------------------------------------------------------
def quartic_square_locally(d1, d2, p, mult=1):
    # does there exist (r,s) != (0,0) in F_p^2 with d1 r^4+32 r^2 s^2+d2 s^4
    # in mult*QRs (mult=1: squares; for L2 the value 9u^2 is a square anyway)
    qs = {(x*x) % p for x in range(p)}
    for r in range(p):
        for s in range(p):
            if r == 0 and s == 0: continue
            val = (d1*pow(r,4,p) + 32*r*r*s*s + d2*pow(s,4,p)) % p
            if val in qs:
                return True
    return False

P("[L3a] projective local solubility of d1 r^4 + 32 r^2 s^2 + d2 s^4 = square")
PRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
          97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
          181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,
          271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367]
for (d1, d2) in SPLITS:
    kills = [p for p in PRIMES if not quartic_square_locally(d1, d2, p)]
    P("    (d1,d2)=", (d1,d2), " killing primes:", kills)

# mod-16 + parity refinements for each split, both L1 and L2 constraints
P("[L3b] parity/mod-16 table per split (classes (r%2,s%2)):")
for (d1, d2) in SPLITS:
    rows = []
    for rp in range(2):
        for sp in range(2):
            r, s = rp, sp
            val = (d1*(r**4) + 32*r*r*s*s + d2*(s**4)) % 16
            n3 = (d2*(s**4) - d1*(r**4)) % 3  # 3n=... for L2
            n4 = (d2*(s**4) - d1*(r**4)) % 4
            rows.append((rp, sp, val, n4 % 2, n4, n3))
    P("    (d1,d2)=", (d1,d2), " (r,s)->(F%16, n%2, n%4, 3n|3):", rows)

# ---------------------------------------------------------------
# Third layer on surviving split (238,1) of case (1,72):
#   u^2 = 238 r^4 + 32 r^2 s^2 + s^4, r even, s odd
#       = (s^2 + 16 r^2)^2 - 18 r^4  =>  (F-)(F+) = 18 r^4,
#   F- = s^2+16r^2-u, F+ = s^2+16r^2+u.  Verified by brute force that for
#   every candidate (r,s,u) found in ranges, gcd(F-,F+)=2*g, odd part g | 9
#   and 3 | g impossible => g=1... we check numerically the claim
#   gcd(F-,F+) is a power of 2 (times possibly 3) for all hit candidates.
P("[L3c] numeric spot-check of F- F+ = 18 r^4 structure, split (238,1):")
found = 0
for r in range(2, 60, 2):
    for s in range(1, 200, 2):
        val = 238*r**4 + 32*r*r*s*s + s**4
        if issq(val):
            u = isqrt(val)
            Fm, Fp = s*s + 16*r*r - u, s*s + 16*r*r + u
            assert Fm*Fp == 18*r**4
            from math import gcd as g2
            g = g2(Fm, Fp)
            odd = g
            while odd % 2 == 0: odd //= 2
            P("    (r,s,u)=", (r,s,u), " F-=", Fm, " F+=", Fp,
              " gcd odd part =", odd, " 3|g:", g % 3 == 0)
            found += 1
P("[L3c] hits:", found)

# same for split (14,17)/(17,14)/(1,238) quick numeric sweep of layer-2 form
P("[L3d] numeric sweep u^2 = d1 r^4+32r^2s^2+d2 s^4, rs even, |r|,|s|<=60:")
for (d1, d2) in SPLITS:
    pts = []
    for r in range(1, 61):
        for s in range(1, 61):
            if (r*s) % 2 != 0: continue
            val = d1*r**4 + 32*r*r*s*s + d2*s**4
            if issq(val):
                pts.append((r, s, isqrt(val), (d2*s**4 - d1*r**4)))
    P("    (d1,d2)=", (d1,d2), " hits (r,s,u,n):", pts[:10], " total", len(pts))

with open("mss_k34_descent_p3.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p3 done, log written ==")