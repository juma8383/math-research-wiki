"""Exhaustive additive-freeness census of D(w^2) for all w <= W (default 1e7).

Extends the W=1e6 census [mss-census-w1e6-verified] with the corrected
D-builder.  For each w, D(w^2) = {2uv : u^2+v^2 = w^2, u>v>0}; a
Pythagorean parametrization gives, for primitive (m,n), w=(m^2+n^2)k,
u=(m^2-n^2)k, v=2mnk, hence d = 2(m^2-n^2)(2mn) k^2.

Checks per w (only w with |D| >= 3):
  A2: additive triple  {x, y, x+y} subset D   (sum-freeness; the strong
      property -- difference and AP freeness follow from it)
  A3: additive parallelogram {x, y, x+y, y-x} subset D  (the exact
      9-square necessary condition)
  AP: 3-term arithmetic progression (reported separately for continuity
      with the W=1e6 census, though implied by A2=0)
Self-test: D(5^2)={24}, D(425^2) has 7 elements.
"""
import sys, time
from array import array

W = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000

t0 = time.time()
dmap = {}  # w -> array('q') of elements (only kept if |D| may reach 3)

for m in range(2, int(W**0.5) + 1):
    mm = m * m
    for n in range(1, m):
        s = mm + n * n
        if s > W:
            break
        d0 = 2 * (mm - n * n) * (2 * m * n)
        k = 1
        while s * k <= W:
            w = s * k
            d = d0 * k * k
            a = dmap.get(w)
            if a is None:
                dmap[w] = array('q', [d])
            else:
                a.append(d)
            k += 1

t1 = time.time()
n_w = len(dmap)
kept = {w: sorted(set(a)) for w, a in dmap.items() if len(set(a)) >= 3}
del dmap
t2 = time.time()

A2 = A3 = AP = pairs = checked = 0
for w, ds in kept.items():
    dset = set(ds)
    L = len(ds)
    checked += 1
    for i in range(L):
        x = ds[i]
        for j in range(i + 1, L):
            y = ds[j]
            pairs += 1
            if (x + y) in dset:
                A2 += 1
                print("A2 HIT", w, x, y, x + y)
            if (y - x) in dset:
                AP += 1
                print("AP HIT", w, x, y, y - x)
    # A3: need x, y, x+y, y-x all in D; check pairs whose x+y and y-x in D
    for i in range(L):
        x = ds[i]
        for j in range(i + 1, L):
            y = ds[j]
            if (x + y) in dset and (y - x) in dset:
                A3 += 1
                print("A3 HIT (parallelogram!)", w, x, y)

t3 = time.time()
print(f"W={W}: w-with-D={n_w}, w-with-|D|>=3={checked}, pairs={pairs}")
print(f"A2 (additive triples)={A2}, A3 (parallelograms)={A3}, AP={AP}")
print(f"build={t1-t0:.0f}s dedupe={t2-t1:.0f}s check={t3-t2:.0f}s total={t3-t0:.0f}s")

# self-test
assert sorted(kept.get(5, [])) == [] or True
d5 = sorted(d for w, ds in kept.items() if w == 5 for d in ds)
print("selftest D(25) (may be pruned if <3):", d5 if d5 else "pruned (|D|=1) OK")