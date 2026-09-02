# mss_k34_descent_p2.py -- K34-A descent part 2:
#  (A) (u,v)-driven exact census over the 8 constant cases
#  (B) local solubility (mod p) of the master quartics and layer-2 forms
#  (C) mod-16 kill table for the (1,72) second-layer Germain splits
#  (D) integer/rational point search on the master quartics
# Exact integer arithmetic. ASCII output only.
import sys
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x)
    return r*r == x

P("== mss_k34_descent_p2 ==")

# Setup recap (proved in p1 + notes): a K34-A solution (a,b coprime, X=(a/b)^2
# nondegenerate square-X point) forces, with R=a^4+66a^2b^2+b^4, n=a^2+b^2,
# delta=gcd(R-V',R+V')=2^j, j=1 if exactly one of a,b even (the prime-n case),
# j=3 if both odd, and (c1,c2) in {(1,72),(8,9),(9,8),(72,1)} with
#   R = 2^(j-1) (c1 u^4 + c2 v^4),  u v = ab, gcd(u,v)=1,
#   V' = 2^(j-1) (c2 v^4 - c1 u^4),  U=(R-V')/delta=c1u^4 < W=c2v^4.
# Parity: j=1 => exactly one of u,v even; j=3 => u,v both odd.

CASES = [(1,72),(8,9),(9,8),(72,1)]

# ---------- (A) census ----------
# Chain per (u,v,c1,c2,j): R=2^(j-1)(c1u^4+c2v^4); n^2=R-64u^2v^2;
# then a,b exist iff (n+2uv) and (n-2uv) are both squares (a+b,|a-b|).
# Additionally need uv=ab consistent and U<W i.e. c1u^4<c2v^4.
P("[A] census over coprime (u,v), max(u,v) <= B")
B = 900
hits = []
cnt_chain = 0
for u in range(1, B+1):
    for v in range(1, B+1):
        if gcd(u, v) != 1: continue
        for (c1, c2) in CASES:
            for j in (1, 3):
                # parity bookkeeping
                if j == 1:
                    if (u % 2 == 0) == (v % 2 == 0):  # both odd or both even
                        continue
                else:
                    if u % 2 == 0 or v % 2 == 0:
                        continue
                R = (2**(j-1))*(c1*u**4 + c2*v**4)
                T = R - 64*u*u*v*v
                if T <= 0: continue
                if not issq(T): continue
                nn = isqrt(T)
                if nn % 2 != (0 if j == 3 else 1): continue
                cnt_chain += 1
                if issq(nn + 2*u*v) and issq(nn - 2*u*v):
                    if c1*u**4 >= c2*v**4: continue
                    hits.append((u, v, c1, c2, j, nn))
P("[A] chain survivors (n^2 square):", cnt_chain, " full hits:", hits)

# ---------- (B) local solubility ----------
def qr_set(p):
    return {x*x % p for x in range(p)}

def locally_soluble_quad_in_z2(c, e, d, p):
    # N^2 = c w^4 + e w^2 + d over F_p (projective: also w=inf i.e. c square,
    # and w=0). Return True if some F_p point exists.
    if c % p == 0:
        # point at infinity exists iff leading coeff square after deg check
        pass
    qs = qr_set(p)
    for w in range(p):
        val = (c*pow(w,4,p) + e*w*w + d) % p
        if val in qs:
            return True
    # w = infinity: c must be a square (leading term) -- counts as point
    if c % p != 0 and (c % p) in qs:
        return True
    return False

P("[B] killing primes (no F_p point at all) for N^2 = c w^4 -64 w^2 + d:")
for (c, d) in CASES:
    kills = []
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
              83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,
              167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,
              251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,
              347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,
              433,439,443,449,457,461,463,467,479,487,491,499,503,509]:
        if not locally_soluble_quad_in_z2(c, -64, d, p):
            kills.append(p)
    P("    (c,d)=", (c,d), " killing primes <=509:", kills)

# layer-2 forms: (n,v,w) with
#   L1 (case 8,9):  n^2 + 119 v^4 = 8 w^2
#   L2 (case 9,8):  9 n^2 + 952 v^4 = W^2
#   L3 (cases 1,72 / 72,1):  n^2 + 952 t^4 = A^2   (t = v resp. u)
def local_L(c1f, c2f, c3f, p, nonz=None):
    # c1f n^2 + c2f v^4 = c3f w^2 solvable mod p with v not 0 (if nonz)
    qs = qr_set(p)
    v0s = range(1, p) if nonz else range(p)
    for vv in v0s:
        rhs = (c3f - c2f*pow(vv,4,p)) % p
        # need c1f n^2 = rhs
        if c1f % p == 0:
            if rhs % p == 0: return True
            continue
        tgt = (rhs * pow(c1f, p-2 if p>2 else 0, p)) % p if p > 2 else (rhs % 2)
        if tgt in qs: return True
    return False

P("[B2] layer-2 local solubility (v nonzero mod p):")
for name, (A, Bc, C) in [("L1 n^2+119v^4=8w^2", (1,119,8)),
                         ("L2 9n^2+952v^4=W^2", (9,952,1)),
                         ("L3 n^2+952t^4=A^2", (1,952,1))]:
    kills = []
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
              83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,
              167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,
              251,257,263,269,271,277,281,283,293]:
        if not local_L(A, Bc, C, p, nonz=True):
            kills.append(p)
    P("    ", name, " killing primes (v!=0):", kills)

# ---------- (C) mod-16 kill table for the (1,72) Germain layer ----------
# Case (1,72): n^2 + 952 v^4 = A^2, A = u^2-32v^2, v even, u odd, gcd(n,v)=1
# => (A-n)/2 = d1 r^4, (A+n)/2 = d2 s^4, d1*d2 = 238, gcd(d1,d2)=1, rs=v.
# Then n = d2 s^4 - d1 r^4 must be = a^2+b^2 with n odd, n = 1 mod 4, and
# u^2 = d1 r^4 + 32 r^2 s^2 + d2 s^4 with u odd.
P("[C] (1,72) second-layer splits d1*d2=238, mod-16 / parity kills:")
splits = [(d1, 238//d1) for d1 in range(1,239) if 238 % d1 == 0
          and gcd(d1, 238//d1) == 1]
for (d1, d2) in splits:
    reasons = []
    ok_n = False
    for rp in range(2):
        for sp in range(2):
            r, s = rp, sp  # parity classes only
            # n = d2 s^4 - d1 r^4, need n odd and n = 1 mod 4
            n4 = (d2*(s**4) - d1*(r**4)) % 4
            if n4 % 2 == 1:
                ok_n = True
    if not ok_n:
        reasons.append("n never odd")
    ok_u = False
    for rp in range(2):
        for sp in range(2):
            r, s = rp, sp
            u2 = (d1*(r**4) + 32*r*r*s*s + d2*(s**4)) % 16
            if u2 in (0,1,4,9):
                ok_u = True
    if not ok_u:
        reasons.append("u^2 never a square mod 16")
    # v = rs must be even (case (1,72) forces v even, u odd)
    ok_v = False
    for rp in range(2):
        for sp in range(2):
            r, s = rp, sp
            n4 = (d2*(s**4) - d1*(r**4)) % 4
            u2 = (d1*(r**4) + 32*r*r*s*s + d2*(s**4)) % 16
            if (r*s) % 2 == 0 and n4 % 2 == 1 and u2 in (0,1,4,9):
                ok_v = True
    if not ok_v:
        reasons.append("no parity class with v even + n odd + u^2 square")
    P("    (d1,d2)=", (d1,d2), " -> ", ("SURVIVES parity/mod16" if not reasons
      else "KILLED: " + "; ".join(reasons)))

# ---------- (D) search integer points on master quartics ----------
P("[D] integer search N^2 = c w^4 - 64 w^2 + d, |w| <= 400:")
for (c, d) in CASES:
    pts = []
    for w in range(-400, 401):
        val = c*w**4 - 64*w*w + d
        if val >= 0 and issq(val):
            pts.append((w, isqrt(val)))
    P("    (c,d)=", (c,d), " integer points:", pts)

P("[D2] rational search w=r/s, 1<=s<=40, |r|<=40*maxs, on same quartics:")
for (c, d) in CASES:
    pts = []
    for s in range(1, 41):
        for r in range(-40*s, 40*s+1):
            if gcd(abs(r), s) != 1: continue
            num = c*r**4 - 64*r*r*s*s + d*s**4
            if num >= 0 and issq(num):
                pts.append((r, s, isqrt(num)))
    P("    (c,d)=", (c,d), " rational points (r,s,N):", pts[:12],
      " total", len(pts))

with open("mss_k34_descent_p2.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p2 done, log written ==")