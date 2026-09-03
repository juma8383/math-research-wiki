# mss_k34_layer1_recount.py -- resolve the layer-1 survivor-count discrepancy
# (2026-09-03). The saved claude_check.log reports [E] n^2-square survivors = 2
# (with its n%4==1 filter) and full hits = [], while notes.md sec "Claude
# main-loop verification" quotes 16 survivors and a (1,1,2) full hit.
# This script enumerates ALL layer-1 solutions exactly, at LIM=900 and
# LIM=2000, and reports counts under every filter variant:
#   all n^2-square survivors (no n%4 filter), with n%4 breakdown,
#   full hits (lift n+-2uv both squares, 0 allowed) with n%4 breakdown.
# Exact integers; ASCII only.
from math import gcd, isqrt

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def issq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x

P("== mss_k34_layer1_recount ==")

def census(LIM):
    rows = []
    for (c1, c2) in ((1, 72), (8, 9), (9, 8), (72, 1)):
        for j in (1, 3):
            for u in range(1, LIM+1):
                u4 = u**4
                for v in range(1, LIM+1):
                    if gcd(u, v) != 1: continue
                    if j == 1 and (u+v) % 2 != 1: continue
                    if j == 3 and (u % 2 or v % 2) != 1: continue
                    n2 = 2**(j-1)*(c1*u4 + c2*v**4) - 64*u*u*v*v
                    if n2 <= 0 or not issq(n2): continue
                    n = isqrt(n2)
                    m = u*v
                    lift = issq(n + 2*m) and issq(n - 2*m)
                    rows.append((u, v, c1, c2, j, n, n % 4, lift))
    return rows

for LIM in (900, 2000):
    rows = census(LIM)
    P(f"[LIM={LIM}] n^2-square survivors (no n%4 filter):", len(rows))
    from collections import Counter
    c4 = Counter(r[6] for r in rows)
    P(f"[LIM={LIM}] n%4 breakdown:", dict(sorted(c4.items())))
    nl = [r for r in rows if r[7]]
    P(f"[LIM={LIM}] full hits (lift ok, 0 allowed):", len(nl))
    for r in nl[:20]:
        P(f"[LIM={LIM}]    u,v,c1,c2,j,n,n%4 =", r[0], r[1], r[2], r[3], r[4], r[5], r[6])
    # the K34-A-relevant count: n%4==1 survivors (the claude_check filter)
    P(f"[LIM={LIM}] with n%4==1 filter:", sum(1 for r in rows if r[6] == 1),
      " of which lift ok:", sum(1 for r in nl if r[6] == 1))
    # non-degenerate = not (u,v)=(1,1)
    nd = [r for r in nl if (r[0], r[1]) != (1, 1)]
    P(f"[LIM={LIM}] full hits excluding degenerate (u,v)=(1,1):", len(nd))
    for r in nd[:20]:
        P(f"[LIM={LIM}]    NONDEGEN HIT:", r)

with open("mss_k34_layer1_recount.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== done ==")