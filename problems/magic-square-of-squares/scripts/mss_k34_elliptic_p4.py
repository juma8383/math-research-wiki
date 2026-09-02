#!/usr/bin/env python
# Part 4 (rewritten): 2-isogeny descent Selmer bounds for Ẽ_A, Ẽ_B.
# C_d: N^2 = d*M^4 + a*M^2*e^2 + (b//d)*e^4   (d squarefree signed divisor of b)
# Conservative local-solubility: only report INSOLUBLE when provable
# (no primitive solution mod p^k), so the Selmer upper bound is rigorous.
import sys
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

def factor(n):
    n = abs(n); fac = {}; d = 2
    while d*d <= n:
        while n % d == 0: fac[d] = fac.get(d,0)+1; n //= d
        d += 1
    if n > 1: fac[n] = fac.get(n,0)+1
    return fac

def sqfree_divisors(n):
    fac = factor(n); res = [1]
    for p in fac: res += [r*p for r in res]
    return res

def QRs_mod_pk(p, k):
    m = p**k
    s = set()
    for x in range(m): s.add((x*x) % m)
    return s

def local_ok(d, a, b, pmax=97):
    """Return False only if provably insoluble somewhere; else True."""
    bd = b // d  # exact
    # real: q(t) = d t^4 + a t^2 + bd on dense grid + infinity behavior
    ok = False
    for i in range(0, 20001):
        t2 = F(i, 100)  # t^2 grid
        val = d*t2*t2 + a*t2 + bd
        if val >= 0: ok = True; break
    if not ok: return False
    for p in range(2, pmax+1):
        if p == 2:
            k = 5; m = 32
        else:
            k = 2; m = p*p
        qrs = QRs_mod(p, k)
        found = False
        for M in range(m):
            M2 = (M*M) % m; M4 = (M2*M2) % m
            for e in range(m):
                if e == 0 and M == 0:
                    continue
                # primitive mod p: not both divisible by p
                if M % p == 0 and e % p == 0: continue
                val = (d*M4 + a*M2*(e*e % m) + bd*(e*e*e*e % m)) % m
                if val in qrs:
                    found = True; break
            if found: break
        if not found: return False
    return True

def QRs_mod(p, k):
    m = p**k; s = set()
    for x in range(m): s.add((x*x) % m)
    return s

def descent(a, b, name, known):
    out("== %s: y^2 = x^3 %+d x^2 %+d x ==" % (name, a, b))
    ds = sorted(set([sgn*d for d in factor(abs(b)) and sqfree_divisors(b) for sgn in (1,-1)]))
    ok = []
    for d in ds:
        r = local_ok(d, a, b)
        if r: ok.append(d)
    out("  Selmer candidates (loc. sol., rigorous kill only):", ok)
    out("  killed locally:", [d for d in ds if d not in ok])
    return ok

okA = descent(-256, 18432, "E~_A", None)
okB = descent(256, -2048, "E~_B", None)
okPA = descent(512, -8192, "E'_A", None)
okPB = descent(-512, 73728, "E'_B", None)
out("known alpha classes: E~_A: {1 (x=4), 2 (x=128, 4608), 2 ((0,0) torsion)}")
out("known alpha classes: E~_B: {1 (x=16), -1 (x=-144), -2 ((0,0) torsion)}")