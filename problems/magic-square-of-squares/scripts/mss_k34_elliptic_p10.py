#!/usr/bin/env python
# Part 10: MW sieve v2. At killing primes K = {3,5,11,13} (C3_A has only
# degenerate solution classes), a non-degenerate square-X point must satisfy
# X = (a/b)^2 with a = 0 or +-b mod p, i.e. X in {0,1} mod p (or X at infinity:
# p | b, i.e. xE == 1, x_~E == 0 -> no constraint, keep).
# At ordinary primes: X must be a QR (or 0) mod p.
# Then combine classes; report survivors.
import sys, math
def out(*a): print(*a); sys.stdout.flush()
exec(open('mss_k34_elliptic_p9.py').read().split("sieve = {}")[0])  # reuse helpers

KILL = (3, 5, 11, 13)
ORD = [q for q in range(7, 400) if all(q % r for r in (2,3,5,7,11,13,17,19))]

def allowed_classes_v2(p):
    N = group_order(A, B2, p)
    QRS = qr_set(p)
    res = {}
    for t in (0, 1):
        ok = set()
        for n in range(N):
            P = ec_mul(A, B2, G, n, p)
            if t: P = ec_add(A, B2, P, T, p)
            if P is None: ok.add(n); continue
            X = Xq_mod(P, p)
            if X is None: ok.add(n); continue
            if p in KILL:
                if X == 0 or X == 1: ok.add(n)
            else:
                if X == 0 or X in QRS: ok.add(n)
        res[t] = (N, ok)
    return res

def crt_merge(M, S, N, ok):
    g = math.gcd(M, N)
    if (M*N)//g > 10**13: return None
    M2 = M*N // g
    S2 = set()
    m1, m2 = M//g, N//g
    inv = pow(m1 % m2, -1, m2) if m2 > 1 else 0
    for c in S:
        for n in ok:
            if (c - n) % g: continue
            k = ((n - c)//g % m2) * inv % m2 if m2 > 1 else 0
            S2.add((c + M*k) % M2)
    return M2, S2

# order primes by constraint density (strongest first), then sieve
def density(p):
    N, ok = allowed_classes_v2(p)[0]
    return len(ok) / N
plist = KILL + tuple(sorted(ORD, key=density))
for t in (0, 1):
    M, S = 1, {0}
    dead = False
    for p in plist:
        N, ok = allowed_classes_v2(p)[t]
        r = crt_merge(M, S, N, ok)
        if r is None:
            out("t=%d: modulus overflow at p=%d with %d classes; stop" % (t, p, len(S)))
            dead = True; break
        M, S = r
        out("t=%d p=%3d: N=%4d |ok|=%4d -> classes mod %d: %d" % (t, p, N, len(ok), M, len(S)))
        if len(S) == 0:
            out("t=%d SIEVE EMPTY at p=%d" % (t, p)); dead = True; break
    if not dead:
        out("t=%d FINAL: survivors %d mod %d" % (t, len(S), M))
        import json
        json.dump({"M": M, "S": sorted(S), "t": t}, open("mss_k34_sieve_t%d.json" % t, "w"))