"""Brocard root-of-unity heuristic (Corollary to Lemma B2).

A solution n!+1=m^2 forces m^2 = 1 (mod n!), i.e. m is a square root of
unity mod n!.  The number of such roots is 2^(pi(n)+1) for n >= 4 (two for
each odd prime power p^a || n!, and 4 for the 2-part since v_2(n!) >= 3).
The solution additionally satisfies m ~ sqrt(n!), so it must lie in the
narrow window [sqrt(n!), 2*sqrt(n!)) of relative width ~ 1/sqrt(n!).

Heuristic: roots of unity mod n! are equidistributed in [0, n!), so the
expected number of roots in the window is
    E(n) = R(n) * sqrt(n!) / n!,   R(n) = number of roots of unity mod n!
which decays superexponentially.  This script enumerates roots exactly via
CRT for n <= 12 and compares the observed window count with E(n).
"""
import math
from sympy import primerange

def count_roots_mod(n):
    """Number of square roots of unity mod n! via the CRT product formula."""
    total = 1
    fac = math.factorial(n)
    # 2-part: v_2(n!) >= 3 for n >= 4 -> 4 roots
    v2 = 0
    t = fac
    while t % 2 == 0:
        v2 += 1
        t //= 2
    total *= 4 if v2 >= 3 else 2 ** (v2 + 1) if v2 >= 1 else 1
    # odd part
    odd = t
    for p in primerange(3, n + 1):
        if odd % p == 0:
            total *= 2
    return total

def roots_of_unity_mod(n):
    """All square roots of unity mod n!, n <= 12 (n! < 4.8e8), by brute force
    over CRT classes built from prime-power components."""
    fac = math.factorial(n)
    if fac > 10**9:
        raise ValueError("brute force only for n <= 12")
    return [x for x in range(1, fac) if (x * x) % fac == 1]

print("== Brocard root-of-unity heuristic ==")
print(f"{'n':>3} {'roots':>8} {'sqrt(n!)':>12} {'window hits':>12} {'E(n)':>10}")
for n in range(4, 13):
    fac = math.factorial(n)
    roots = roots_of_unity_mod(n) if n <= 12 else None
    nR = count_roots_mod(n)
    assert len(roots) == nR, (n, len(roots), nR)
    s = math.isqrt(fac)
    # window [sqrt(n!), 2*sqrt(n!)):  m^2 = n!+1 means m > sqrt(n!) exactly
    hits = [r for r in roots if s < r <= 2 * s]
    E = nR * math.sqrt(fac) / fac
    print(f"{n:>3} {nR:>8} {s:>12} {len(hits):>12} {E:>10.4f}")
    if hits:
        print(f"     hits: {hits}")

# decay of E(n) for large n (asymptotic, no enumeration)
print("\nasymptotic E(n) = 2^(pi(n)+1) * sqrt(n!) / n!:")
from sympy import primepi
from math import lgamma
for n in [10, 20, 50, 100, 1000]:
    logE = (primepi(n) + 1) * math.log(2) - 0.5 * lgamma(n + 1)
    print(f"  n={n:>5}: log10 E(n) = {logE / math.log(10):.1f}")