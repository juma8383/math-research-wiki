"""Stratify the window-corrected hourglass expectation by omega_1(w).

Question (from the freeness theorem's corollary): omega_1(w) >= 2 is the
proved necessary condition for a 9-square center.  How much stronger is
it, under the window-corrected probabilistic model?  For each w <= W we
compute the expected additive-triple (hourglass) count
  H2(w) = (# pairs passing the partner-window test) * 24|D(w^2)| / w^2
where the partner-window theorem says: for x = 2uv in a triple {x,y,x+y},
the partner y must lie in [2(u+v)+1, (u-v)^2-1] in BOTH roles (y in
win(x) and x in win(y)) -- the two-sided intersection is what reproduces
the filed window-corrected H2 ~ 0.0775 (one-sided gives ~1.05).

Buckets by omega_1(w) = # distinct 1-mod-4 primes of w.  The omega_1 = 1
stratum is PROVED hourglass-free (prime-power freeness theorem), so we
also report the theorem-conditioned total (omega_1 >= 2 only): the model
mass that actually survives the proved necessary condition.

Self-tests: D(25) = {24}; |D(425^2)| = 7.
"""
import math, sys
from sympy import factorint
from collections import defaultdict, Counter

W = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000

dmap = {}
for m in range(2, int(math.isqrt(W)) + 1):
    mm = m * m
    for n in range(1, m):
        s = mm + n * n
        if s > W:
            break
        d0 = 2 * (mm - n * n) * (2 * m * n)
        k = 1
        while s * k <= W:
            w = s * k
            a = dmap.get(w)
            if a is None:
                dmap[w] = [d0 * k * k]
            else:
                a.append(d0 * k * k)
            k += 1

assert sorted(set(dmap[5])) == [24]
assert len(set(dmap[425])) == 7

def omega1(w):
    return sum(1 for p in factorint(w) if p % 4 == 1)

H2_stratum = defaultdict(float)
H2n_stratum = defaultdict(float)
wD_stratum = Counter()
nD2plus = 0

for w, lst in dmap.items():
    ds = sorted(set(lst))
    nD = len(ds)
    if nD < 2:
        continue
    nD2plus += 1
    o1 = omega1(w)
    wD_stratum[o1] += 1
    w2 = w * w
    dens = 24 * nD / w2
    H2n_stratum[o1] += nD * (nD - 1) / 2 * dens
    # window per element: (lo, hi) or None; rep is unique for each d
    wins = []
    for x in ds:
        rp = math.isqrt(w2 + x)   # u+v
        rm = math.isqrt(w2 - x)   # u-v
        if rp * rp != w2 + x or rm * rm != w2 - x:
            wins.append(None)
            continue
        lo, hi = 2 * rp + 1, rm * rm - 1   # hi = (u-v)^2-1 = w^2-x-1
        wins.append((lo, hi) if lo <= hi else None)
    adm = 0
    for i in range(nD):
        wi = wins[i]
        if wi is None:
            continue
        for j in range(i + 1, nD):
            wj = wins[j]
            if wj is None:
                continue
            x, y = ds[i], ds[j]
            # two-sided: y in win(x) and x in win(y)
            if wi[0] <= y <= wi[1] and wj[0] <= x <= wj[1]:
                adm += 1
    H2_stratum[o1] += adm * dens

print(f"W={W}  centers_with_|D|>=2 = {nD2plus}")
print(f"{'omega1':>6} {'centers':>9} {'H2 naive':>12} {'H2 window':>12} {'share%':>8}")
keys = sorted(set(H2n_stratum) | set(H2_stratum))
tot_n = sum(H2n_stratum.get(o, 0.0) for o in keys)
tot_w = sum(H2_stratum.get(o, 0.0) for o in keys)
for o1 in keys:
    hn = H2n_stratum.get(o1, 0.0)
    h = H2_stratum.get(o1, 0.0)
    share = 100 * h / tot_w if tot_w else 0.0
    print(f"{o1:>6} {wD_stratum.get(o1, 0):>9} {hn:>12.5f} {h:>12.5f} {share:>7.2f}%")
cond_w = sum(H2_stratum.get(o, 0.0) for o in keys if o >= 2)
cond_n = sum(H2n_stratum.get(o, 0.0) for o in keys if o >= 2)
print(f"TOTAL naive={tot_n:.5f}  window={tot_w:.5f}")
print(f"THEOREM-CONDITIONED (omega1>=2, proved-free strata removed): "
      f"naive={cond_n:.5f}  window={cond_w:.5f}")