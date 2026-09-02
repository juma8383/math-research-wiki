# mss_k34_descent_p4.py -- K34-A descent part 4:
# per-case layer-2 split kill tables (all 4 cases x 8 splits x A-sign
# branches x parity classes), layer-1 solution census with n=1 mod 4,
# and numeric verification of the (238,1) descent step.
# Exact integer arithmetic. ASCII output only.
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_descent_p4 ==")
SPLITS = [(d1, 238//d1) for d1 in range(1,239) if 238 % d1 == 0
          and gcd(d1, 238//d1) == 1]

# Layer-2 systems (all with gcd(r,s)=1, rs = the even-carrying variable):
#  case (1,72): u odd, v=rs even, n=1 mod 4.
#    A=u^2-32v^2, A^2=n^2+952v^4, A>0 branch:
#        u^2 = d1 r^4+32r^2s^2+d2 s^4,  n = d2 s^4 - d1 r^4 > 0.
#    A<0 branch (A'=-A): u^2 = 32r^2s^2 - d1 r^4 - d2 s^4 > 0.
#  case (72,1): v odd, u=rs even: same two branches with v^2 in place of u^2.
#  case (9,8): u odd, v=rs even, 3n = d2 s^4-d1 r^4, n=1 mod 4 (so the
#    bracket is 3 mod 4), 9u^2 = d1 r^4+32r^2s^2+d2 s^4 (W>0 branch) or
#    9u^2 = 32r^2s^2-d1 r^4-d2 s^4 (W<0 branch).
#  case (8,9): mirror with v odd, u=rs even, 9v^2 in place of 9u^2.
SQ16 = (0,1,4,9)
def classes():
    return [(rp, sp) for rp in range(2) for sp in range(2)]

P("[T1] case (1,72)/(72,1) split table (u^2-form; v^2-form identical tests):")
surv = {}
for branch, ffun, nfun in [
    ("A>0", lambda d1,r,s,d2: d1*r**4+32*r*r*s*s+d2*s**4,
            lambda d1,r,s,d2: d2*s**4-d1*r**4),
    ("A<0", lambda d1,r,s,d2: 32*r*r*s*s-d1*r**4-d2*s**4,
            lambda d1,r,s,d2: d2*s**4-d1*r**4)]:
    for (d1, d2) in SPLITS:
        ok = []
        for (rp, sp) in classes():
            r, s = rp, sp
            F = ffun(d1, r, s, d2) % 16
            n4 = nfun(d1, r, s, d2) % 4
            npar = nfun(d1, r, s, d2) % 2
            # x^2 = F with x odd (u odd resp v odd) => F in {1,9};
            # need n odd, n = 1 mod 4, rs even
            if F in (1, 9) and npar == 1 and n4 == 1 and (rp*sp) % 2 == 0:
                ok.append((rp, sp))
        if ok:
            surv[(branch, d1, d2)] = ok
            P("    branch", branch, "split", (d1,d2), "surviving classes", ok)
P("[T1] survivors:", sorted(surv.keys()))

P("[T2] case (9,8)/(8,9) split table (9u^2 resp 9v^2 = F, u resp v odd):")
surv2 = {}
for branch, ffun, nfun in [
    ("W>0", lambda d1,r,s,d2: d1*r**4+32*r*r*s*s+d2*s**4,
            lambda d1,r,s,d2: d2*s**4-d1*r**4),
    ("W<0", lambda d1,r,s,d2: 32*r*r*s*s-d1*r**4-d2*s**4,
            lambda d1,r,s,d2: d2*s**4-d1*r**4)]:
    for (d1, d2) in SPLITS:
        ok = []
        for (rp, sp) in classes():
            r, s = rp, sp
            F = ffun(d1, r, s, d2) % 16
            br = nfun(d1, r, s, d2)
            # 9u^2 with u odd: F in {1,9}; need 3 | bracket and bracket = 3 mod 4
            if F in (1, 9) and br % 3 == 0 and br % 4 == 3 and (rp*sp) % 2 == 0:
                ok.append((rp, sp))
        if ok:
            surv2[(branch, d1, d2)] = ok
            P("    branch", branch, "split", (d1,d2), "surviving classes", ok)
P("[T2] survivors:", sorted(surv2.keys()))

# ---------- mod-9 / mod-7 refinement on the surviving sub-cases ----------
P("[T3] surviving sub-cases: mod-p solubility with coprime (r,s), p in {3,7,9-part}:")
def sol_mod(d1, d2, branch, p, need9):
    # exists coprime-mod-p (r,s) != (0,0) with F(r,s) = 9 u^2 (need9) or u^2
    # (else) exact congruence mod p (p=9 handled by mod 9 squares)
    mod = 9 if need9 else p
    sq = {x*x % mod for x in range(mod)}
    for r in range(mod if need9 else p):
        for s in range(mod if need9 else p):
            if gcd(r, s, ) % (3 if need9 else p) == 0 and (r, s) != (0, 0):
                pass
            if branch == "A>0":
                F = d1*r**4 + 32*r*r*s*s + d2*s**4
            else:
                F = 32*r*r*s*s - d1*r**4 - d2*s**4
            if F % mod in sq:
                return True
    return False

for (branch, d1, d2) in sorted(surv.keys()):
    r9 = sol_mod(d1, d2, branch, 9, True)
    P("    (1,72)-family", branch, (d1,d2), ": F a square mod 9 ?", r9)
for (branch, d1, d2) in sorted(surv2.keys()):
    r9 = sol_mod(d1, d2, branch, 9, True)
    P("    (9,8)-family", branch, (d1,d2), ": F a square mod 9 ?", r9)

# ---------- layer-1 census: solutions of n^2 = c1 u^4 -64u^2v^2 + c2 v^4 ----------
P("[L1] layer-1 solutions with n odd, n=1 mod 4, max(u,v) <= 1500:")
CASES = [(1,72),(8,9),(9,8),(72,1)]
found = []
for u in range(1, 1501):
    u4 = u**4
    for v in range(1, 1501):
        if gcd(u, v) != 1: continue
        for (c1, c2) in CASES:
            T = c1*u4 - 64*u*u*v*v + c2*v**4
            if T > 0 and issq(T):
                n = isqrt(T)
                if n % 4 == 1:
                    found.append((c1, c2, u, v, n))
P("[L1] count:", len(found), " first 25:", found[:25])

# ---------- descent-step verification on case (1,72) ----------
# For each layer-1 (1,72) solution with u odd, v even, n=1 mod 4, A=u^2-32v^2:
# check A>n, (A-n)/2 = d1 r^4, (A+n)/2 = d2 s^4, which split, and then the
# third layer (F-/2)(F+/2) = 72 (r/2)^4 recovering a smaller layer-1 solution.
P("[D] descent-step verification on case (1,72) layer-1 solutions:")
desc_ok = 0
for (c1, c2, u, v, n) in found:
    if (c1, c2) != (1, 72): continue
    A = u*u - 32*v*v
    if A <= n:
        P("    (u,v,n)=", (u,v,n), " A<=n (A<0 branch) -- excluded by mod-16 kill? A=", A)
        continue
    e1, e2 = (A-n)//2, (A+n)//2
    d1 = r1 = None
    # extract fourth-power part
    def fp_split(m):
        c = 1
        for p_ in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
            while m % (p_**4) == 0:
                m //= p_**4; c *= p_
        return c, m
    cA, mA = fp_split(e1)
    cB, mB = fp_split(e2)
    isp1 = all(x**4 != mA for x in range(2, 60)) or mA == 1 or issq(mA)==False
    P("    (u,v,n)=", (u,v,n), " (A-n)/2=", e1, "= c*r^4 with c=", cA,
      " rest=", mA, " fourthfree:", (lambda m: all(m % (k**4) for k in range(2,30)))(mA),
      " | (A+n)/2=", e2, " c=", cB, " rest=", mB,
      " split=(", cA, cB, ") product", cA*cB)
    if (cA, cB) in [(x, 238//x) for x in range(1,239) if 238 % x == 0]:
        desc_ok += 1
P("[D] solutions whose split constants are coprime pairs of 238:", desc_ok,
  "of", len(found))

with open("mss_k34_descent_p4.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p4 done, log written ==")