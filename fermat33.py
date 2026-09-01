from math import gcd
from itertools import combinations_with_replacement

m, n = 33, 4
# (2,2)-chars: 6-tuples in {1..32} with sum == 99 (since p=2 <=> sum(a)/33 == 3, sum(a)=99)
# enumerate sorted representatives (mod S_6), then fold by scaling with units (Z/33)^*
units = [c for c in range(1,33) if gcd(c,33)==1]

def norm(t):
    best = None
    for c in units:
        s = tuple(sorted((c*a) % 33 for a in t))
        if 0 in s: continue
        if best is None or s < best: best = s
    return best

# generate sorted 6-tuples with sum 99
reps = set()
import itertools
for t in combinations_with_replacement(range(1,33), 6):
    if sum(t) == 99:
        reps.add(norm(t))
print("total (2,2)-chars (by inclusion-exclusion check below)")
# exact total count by inclusion-exclusion
from math import comb
tot = sum((-1)**j * comb(6,j) * comb(99-33*j+5-1, 5-1+1) for j in range(0,6) if 99-33*j >= 6)
# careful: number of solutions a_i in [1,32], sum 99 = coeff of x^93 in ((1-x^32)/(1-x))^6
tot = sum((-1)**j*comb(6,j)*comb(93-32*j+5,5) for j in range(0,6) if 93-32*j >= 0)
print("count of (2,2)-chars:", tot)
print("number of G-orbits ((Z/33)^* x S_6) on (2,2)-chars:", len(reps))

# the "zeta_3-decomposable" chars: two orbits {a,a+11,a+22},{b,b+11,b+22}, a+b=11
z3 = set()
for a in range(1,33):
    for b in range(1,33):
        t = tuple(sorted([a%33 or 33,(a+11)%33 or 33,(a+22)%33 or 33,
                           b%33 or 33,(b+11)%33 or 33,(b+22)%33 or 33]))
        # require actual sum (reduced entries in 1..32) == 99
        tt = [x if x != 0 else 33 for x in t]
        # entries must be nonzero mod 33 to be chars
        if any(x % 33 == 0 for x in [a%33,(a+11)%33,(a+22)%33,b%33,(b+11)%33,(b+22)%33]): continue
        tt = sorted([x % 33 for x in [a,a+11,a+22,b,b+11,b+22]])
        if sum(tt) == 99:
            z3.add(norm(tt))
print("zeta_3-decomposable orbit reps:", len(z3))
print(sorted(z3)[:12])
