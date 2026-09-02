# mss_k34_descent_p6.py -- K34-A descent part 6: search for actual solutions
# of the four surviving layer-2 quartics, and verify the (238,1) third-layer
# descent step on any hit. Exact integer arithmetic. ASCII output only.
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_descent_p6: surviving layer-2 quartic search ==")

# Family Q survivors (u odd, v = rs even, gcd(r,s)=1, n = br, n = 1 mod 4):
#   S1 pos(238,1): u^2 = 238 r^4 + 32 r^2 s^2 + s^4,  r even, s odd,
#      n = s^4 - 238 r^4 > 0  => s >= 4r.
#   S2 pos(14,17): u^2 = 14 r^4 + 32 r^2 s^2 + 17 s^4, r even, s odd,
#      n = 17 s^4 - 14 r^4 > 0.
#   S3 neg(7,34):  u^2 = 32 r^2 s^2 - 7 r^4 - 34 s^4 > 0, r odd, s even,
#      n = 34 s^4 - 7 r^4 > 0, with r^2/s^2 in (1.68, 2.20).
# Family N survivor:
#   S4 pos(17,14): 9 u^2 = 17 r^4 + 32 r^2 s^2 + 14 s^4, r odd, s even,
#      n = (14 s^4 - 17 r^4)/3 > 0, integer, 1 mod 4.
P("[S1] 238r^4+32r^2s^2+s^4 = u^2, r even s odd, s>=4r, r,s<=600:")
h1 = []
for r in range(2, 300, 2):
    for s in range(max(4*r, 1), 1201, 2):
        if gcd(r, s) != 1: continue
        F = 238*r**4 + 32*r*r*s*s + s**4
        if issq(F):
            u = isqrt(F)
            n = s**4 - 238*r**4
            h1.append((r, s, u, n, n % 4))
P("[S1] hits:", h1[:20], " total", len(h1))

P("[S2] 14r^4+32r^2s^2+17s^4 = u^2, r even s odd, r,s<=300:")
h2 = []
for r in range(2, 301, 2):
    for s in range(1, 1201, 2):
        if gcd(r, s) != 1: continue
        F = 14*r**4 + 32*r*r*s*s + 17*s**4
        if issq(F):
            u = isqrt(F)
            n = 17*s**4 - 14*r**4
            if n > 0:
                h2.append((r, s, u, n, n % 4, (n % 3 == 0)))
P("[S2] hits:", h2[:20], " total", len(h2))

P("[S3] 32r^2s^2-7r^4-34s^4 = u^2 > 0, r odd s even, r,s<=400:")
h3 = []
for r in range(1, 401, 2):
    for s in range(2, 801, 2):
        if gcd(r, s) != 1: continue
        F = 32*r*r*s*s - 7*r**4 - 34*s**4
        if F > 0 and issq(F):
            u = isqrt(F)
            n = 34*s**4 - 7*r**4
            h3.append((r, s, u, n, n % 4))
P("[S3] hits:", h3[:20], " total", len(h3))

P("[S4] 17r^4+32r^2s^2+14s^4 = 9u^2, r odd s even, r,s<=300:")
h4 = []
for r in range(1, 301, 2):
    for s in range(2, 1201, 2):
        if gcd(r, s) != 1: continue
        F = 17*r**4 + 32*r*r*s*s + 14*s**4
        if F % 9 == 0 and issq(F // 9):
            u = isqrt(F // 9)
            br = 14*s**4 - 17*r**4
            if br > 0 and br % 3 == 0:
                n = br // 3
                h4.append((r, s, u, n, n % 4))
P("[S4] hits:", h4[:20], " total", len(h4))

# Descent step check on S1 hits (third layer):
#   u^2 = (s^2+16r^2)^2 - 18 r^4 -> (F-/2)(F+/2) = 72 (r/2)^4,
#   F- = s^2+16r^2-u, F+ = s^2+16r^2+u, gcd(F-/2,F+/2)=1 expected,
#   F-/2 = c1' rho^4, F+/2 = c2' sig^4, rho*sig = r/2,
#   s^2 = c1' rho^4 - 64 rho^2 sig^2 + c2' sig^4  (new layer-1 solution).
P("[D] third-layer descent check on S1 hits:")
for (r, s, u, n, n4) in h1[:8]:
    Fm, Fp = s*s + 16*r*r - u, s*s + 16*r*r + u
    assert Fm * Fp == 18 * r**4
    if Fm % 2 or Fp % 2:
        P("    (r,s,u)=", (r,s,u), " F-,F+ not both even -- descent gap!"); continue
    a, b_ = Fm//2, Fp//2
    g = gcd(a, b_)
    # extract fourth-power parts
    def fp4(m):
        c = 1
        for p_ in (2,3,5,7,11,13,17,19,23,29,31,37):
            while m % (p_**4) == 0:
                m //= p_**4; c *= p_
        return c, m
    c1p, m1 = fp4(a); c2p, m2 = fp4(b_)
    P("    (r,s,u)=", (r,s,u), " (F-/2,F+/2)=", (a,b_), " gcd=", g,
      " c1'=", c1p, " rest1=", m1, " c2'=", c2p, " rest2=", m2,
      " rest1,rest2 fourth-powers:", m1 == 1, m2 == 1)

with open("mss_k34_descent_p6.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p6 done, log written ==")