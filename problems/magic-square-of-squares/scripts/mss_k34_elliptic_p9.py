#!/usr/bin/env python
# Part 9: Mordell-Weil sieve for K34-A on E~_A (rank 1, generator (128,512), tors (0,0)).
# Condition: quartic X = 2(y+66x)/(x(x-4)) must be a rational SQUARE (x=a/b, X=(a/b)^2),
# non-degenerate: X != 0, 1. Killing primes for C3_A: p in {3,5,11,13}: there the
# only solution classes are X in {0,1} (a = 0 or +-b). So for any non-degenerate
# rational solution, X(nG+tT) in {0,1} mod 11 and mod 13 (3 and 5 similar).
# Sieve n over Z/N_p for p in {3,5,11,13,17,...} with condition
#   X mod p in QRset_p  where QR-allowance = {0,1} u QR (exact: classes where
#   X is a square mod p, plus degenerate 0/1 which are anyway squares? X=1: square; X=0: square)
# Actually X square mod p is the general condition; at killing primes the square-X
# classes that survive reduce to {0,1} automatically. So sieve condition:
#   X(nG+tT) is a QR mod p (or X==0) for all p, with X != 0,1 as RATIONALS.
# Rigor: for non-degenerate point, X is a rational square != 0,1 -> mod p (p good,
#   denom nonzero) X in QR_p and X != 0 mod p when p | denom impossible...
#   X != 0,1 rationals -> only finitely many p have X == 0 or 1 mod p; sieve keeps
#   classes; those surviving all primes with X==0/1 only at degenerate points die.
import sys, math
def out(*a): print(*a); sys.stdout.flush()

def ec_add(A, B2, P, Q, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if P == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*A*x1 + B2) * pow(2*y1, p-2, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, p-2, p) % p
    x3 = (lam*lam - A - x1 - x2) % p
    return (x3, (lam*(x1 - x3) - y1) % p)

def ec_mul(A, B2, P, n, p):
    if n < 0: return ec_mul(A, B2, (P[0], (-P[1]) % p), -n, p)
    R = None; Q = P
    while n:
        if n & 1: R = ec_add(A, B2, R, Q, p)
        Q = ec_add(A, B2, Q, Q, p); n >>= 1
    return R

def group_order(A, B2, p):
    n = 0
    for x in range(p):
        v = (x**3 + A*x*x + B2*x) % p
        if v == 0: n += 1
        elif pow(v, (p-1)//2, p) == 1: n += 2
    return n + 1

def qr_set(p):
    return {i*i % p for i in range(p)}

A, B2 = -256, 18432   # E~_A
G = (128, 512); T = (0, 0)
INV = lambda x, p: pow(x, p-2, p)

def Xq_mod(P, p):
    # X = 2(y+66x)/(x(x-4)); returns None if x==0 or 4 (degenerate-at-infinity class)
    x, y = P
    if x % p in (0, 4 % p): return None
    return 2*(y + 66*x) * INV(x*(x-4) % p, p) % p

def allowed_classes(p):
    N = group_order(A, B2, p)
    QRS = qr_set(p)
    res = {}
    for t in (0, 1):
        ok = set()
        for n in range(N):
            P = ec_mul(A, B2, G, n, p)
            if t: P = ec_add(A, B2, P, T, p)
            if P is None:
                ok.add(n)  # O <-> quartic (0,-1) degenerate: allowed but flagged
                continue
            X = Xq_mod(P, p)
            if X is None: ok.add(n); continue   # infinity class: no constraint
            if X == 0 or X == 1: ok.add(n); continue   # possibly-degenerate: keep
            if X in QRS: ok.add(n)
        res[t] = (N, ok)
    return res

sieve = {}   # (t) -> (modulus, set of classes)
for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113):
    r = allowed_classes(p)
    for t in (0, 1):
        N, ok = r[t]
        if t == 0:
            M, S = sieve.get(t, (1, {0}))
        else:
            M, S = sieve.get(t, (1, {0}))
        M2 = M*N // math.gcd(M, N)
        S2 = set()
        for c in S:
            for n in ok:
                # class c mod M and n mod N compatible?
                if (c - n) % math.gcd(M, N) == 0:
                    # combine: solutions of x=c (M), x=n (N)
                    g = math.gcd(M, N)
                    lcm = M2
                    # CRT
                    m1, m2 = M//g, N//g
                    diff = (n - c) // g % m2
                    k = diff * pow(m1 % m2, -1 if m2 > 1 else 1, m2) % m2 if m2 > 1 else 0
                    x0 = (c + M*k) % lcm
                    S2.add(x0)
        sieve[t] = (M2, S2)
        out("p=%d t=%d: N_p=%d allowed=%s -> total classes mod %d: %d" %
            (p, t, N, sorted(ok)[:20], M2, len(S2)))
        if len(S2) == 0:
            out("SIEVE EMPTY for t=%d at p=%d -> NO non-degenerate rational point with square X on M_A" % (t, p))
            sys.exit(0)