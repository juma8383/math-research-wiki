"""Pillai-2 local residue sieve [pillai2-local-sieve].

For X^u - Y^v = 2 (u,v odd primes), quantify how much each small modulus
constrains (X,Y): for each modulus m, the surviving fraction of residue
pairs is f_m(u,v) = #{(x,y) mod m : x^u - y^v = 2 (mod m)} / m^2.

Item 2 of the page says no modulus OBSTRUCTS (f > 0 everywhere tested);
this script MEASURES f over the full odd-prime exponent range u,v <= 83 --
the per-(u,v) product of local fractions is the first quantitative
"which (u,v) is most congruence-constrained" table, a targeting tool for
future per-curve work (genus >= 4 superelliptic curves).
"""
import sys, itertools
from math import gcd

PRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83]
MODS = [8, 3, 5, 7, 9, 11, 13, 25, 17]

def classes(u, m):
    """c[r] = #{x mod m : x^u = r mod m}."""
    c = [0] * m
    for x in range(m):
        c[pow(x, u, m)] += 1
    return c

def frac(u, v, m):
    cu = classes(u, m); cv = classes(v, m)
    n = 0
    for r in range(m):
        s = r - 2                       # x^u = r, y^v = r - 2
        n += cu[r] * cv[s % m]
    return n / (m * m)

def main():
    print("pair u v   product-of-local-fractions (mods 8,3,5,7,9,11,13,25,17)")
    rows = []
    for u, v in itertools.product(PRIMES, repeat=2):
        if u == v: continue
        f = 1.0
        for m in MODS:
            f *= frac(u, v, m)
        rows.append((f, u, v))
    rows.sort()
    print("most constrained pairs:")
    for f, u, v in rows[:15]:
        print(f"  u={u:3d} v={v:3d}  f={f:.6f}")
    print("least constrained pairs:")
    for f, u, v in rows[-5:]:
        print(f"  u={u:3d} v={v:3d}  f={f:.6f}")
    fs = [r[0] for r in rows]
    import statistics
    print(f"n={len(rows)} min={min(fs):.6f} med={statistics.median(fs):.6f} "
          f"max={max(fs):.6f} mean={statistics.mean(fs):.6f}")
    # sanity: every pair locally soluble at every modulus (f_m > 0)?
    bad = []
    for u, v in itertools.product(PRIMES, repeat=2):
        if u == v: continue
        for m in MODS:
            if frac(u, v, m) == 0: bad.append((u, v, m))
    print("locally-obstructing (u,v,m) found:", bad if bad else "NONE")

if __name__ == "__main__":
    main()