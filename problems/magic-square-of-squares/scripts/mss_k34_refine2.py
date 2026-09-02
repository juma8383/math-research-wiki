#!/usr/bin/env python
# 2d follow-up: (i) verify the valuation formula v_q(X(nG)) = s_q (kernel
# depth) on exact small cases; (ii) census of odd-Wieferich defects
# v_q(psi_ord) for (E~_A, G_A) at small primes -- evidence for the
# odd-depth primitive-divisor gate.
#
# Valuation claim (to verify numerically here): if P = nG is in the kernel
# of reduction at a good prime q with depth s = v_q(denom(x(P))) >= 1, then
#   v_q(y_P + 66x_P) = -3s   and   v_q(x_P(x_P-4)) = -4s
#   hence v_q(X(P)) = +s   (exactly, no cancellation).
# Reason: x_P = phi/psi^2, y_P = phi3/psi^3 with gcd(phi,psi)=gcd(phi3,psi)=1;
# v(phi3)=0 so y+66x = (phi3 + 66 phi psi)/psi^3 has valuation -3s (the
# second term has valuation >= s > -3s, no cancellation possible); and
# x-4 = (phi - 4 psi^2)/psi^2 with v(phi)=0, v(psi^2)=2s so phi-4psi^2 = phi
# mod q, valuation 0.
import sys, math
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

A2, A4 = -256, 18432
G = (F(128), F(512))
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 == -y2: return None
    lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2*x1+A4)/(2*y1)
    x3 = lam*lam - A2 - x1 - x2
    return (x3, -(y1 + lam*(x3-x1)))
def mul(P, n):
    R = None; Q = P
    while n:
        if n & 1: R = add(R, Q)
        Q = add(Q, Q); n >>= 1
    return R

def vp(fr, p):
    v = 0
    n = fr.numerator
    while n % p == 0: v += 1; n //= p
    v -= 0
    n = fr.denominator
    while n % p == 0: v -= 1; n //= p
    return v

def Xval(P):
    x, y = P
    return F(2*(y + 66*x), x*(x-4))

# (i) exact check: for small n, primes q where nG is in the kernel,
# verify v_q(X(nG)) == s_q == v_q(denom(x(nG)))/2.
out("=== (i) valuation formula v_q(X(nG)) = depth, exact check ===")
# Kernel primes of nG: q good with ord_q(G) = d | n.  Find them over small
# primes q (group order + order of G), then read off s = v_q(x(nG)) from the
# exact Fraction -- no factoring of the huge denominator.
def count_E(p):
    cnt = 1
    qrs = set((t*t) % p for t in range(1, p))
    for x in range(p):
        v = (x*x*x + A2*x*x + A4*x) % p
        if v == 0: cnt += 1
        elif v in qrs: cnt += 2
    return cnt
def ec_add_mod(Pp, Q, p):
    if Pp is None: return Q
    if Q is None: return Pp
    x1,y1 = Pp; x2,y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if Pp == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*A2*x1 + A4) * pow(2*y1, -1, p) % p
    else:
        lam = (y2-y1) * pow(x2-x1, -1, p) % p
    x3 = (lam*lam - A2 - x1 - x2) % p
    return (x3, (-(y1 + lam*(x3-x1))) % p)
def ec_mul_mod(Pp, n, p):
    if Pp is not None: Pp = (Pp[0] % p, Pp[1] % p)
    R = None; Q = Pp
    while n:
        if n & 1:
            if R is None: R = Q
            else: R = ec_add_mod(R, Q, p)
        Q = ec_add_mod(Q, Q, p) if Q is not None else None
        n >>= 1
    return R
# order of G_A mod q for every good prime q <= QMAX
ORD = {}
QMAX = 4000
for q in range(5, QMAX+1):
    isprime = True
    for d in range(2, int(q**0.5)+1):
        if q % d == 0: isprime = False; break
    if not isprime: continue
    N = count_E(q)
    fs = {}; m = N; dd = 2
    while dd*dd <= m:
        while m % dd == 0: fs[dd] = fs.get(dd,0)+1; m //= dd
        dd += 1 if dd == 2 else 2
    if m > 1: fs[m] = fs.get(m,0)+1
    o = N
    for f in sorted(fs):
        for _ in range(fs[f]):
            if ec_mul_mod((128,512), o//f, q) is None: o //= f
            else: break
    ORD[q] = o
out("  ord_q(G) computed for good primes q<=%d (%d primes)" % (QMAX, len(ORD)))

bad = 0; tested = 0
divmap = {}
for n in range(2, 61):
    divs = [d for d in range(1, n+1) if n % d == 0]
    divmap[n] = set(d for d in divs)
for n in range(2, 61):
    P = mul(G, n)
    if P is None: continue
    if P[0] == 0 or P[0] == 4: continue   # 0/0 point (2G), skip
    xP = P[0]
    X = Xval(P)
    for q, o in ORD.items():
        if o not in divmap[n]: continue
        s = vp(xP, q)
        if s >= 0: continue          # not a kernel prime
        s = -s // 2
        vX = vp(X, q)
        vN = vp(F(2*(P[1] + 66*P[0])), q)   # y + 66x
        vD = vp(P[0]*(P[0]-4), q)
        tested += 1
        ok = (vN == -3*s) and (vD == -4*s) and (vX == s)
        if not ok:
            bad += 1
            out("  MISMATCH n=%d q=%d: s=%d vN=%d vD=%d vX=%d" % (n, q, s, vN, vD, vX))
out("  exact kernel-prime checks (n<=60, q<=%d): %d tested, %d failures" % (QMAX, tested, bad))

# (ii) odd-Wieferich census: primes q with ord_q(G) = d small; depth
# s_q = v_q(psi_d) >= 2 (even depth, i.e. psi_d = 0 mod q^2) = odd-Wieferich.
# Compute psi_d(x_G) mod q^2 via the division polynomial (degree d^2, so d
# must be small) -- equivalently compute dG mod q^2 in the formal group via
# exact rational arithmetic at the point dG?  Simpler: depth of the point
# nG at q is v_q(denom(x(nG)))/2 with n = ord; compute denom(x(dG)) exactly
# for small d and read off v_q.
out("=== (ii) odd-Wieferich census: depth of ord_q(G)-multiple ===")
# odd-Wieferich prime for (E~_A, G_A): v_q(psi_ord) even (>=2), i.e. the
# base depth of the order-o point is even.  For q with o = ord_q(G) <= 60:
# compute oG exactly, s0 = v_q(denom(x(oG)))/2; s0 odd = normal (depth 1),
# s0 even = odd-Wieferich (the case that would evade the gate).
wie = []; depths = {}
Pcache = {}
for q, o in sorted(ORD.items()):
    if o > 60: continue
    if o not in Pcache: Pcache[o] = mul(G, o)
    v = vp(Pcache[o][0], q)
    if v >= 0: continue          # oG not in kernel at q??  skip
    s0 = -v // 2
    depths[q] = (o, s0)
    if s0 % 2 == 0: wie.append((q, o, s0))
out("  primes q<=%d with ord<=60: %d computed; odd-Wieferich (even depth): %s"
    % (QMAX, len(depths), wie if wie else "NONE"))
hist = {}
for q, (o, s0) in depths.items(): hist[s0] = hist.get(s0, 0) + 1
out("  depth histogram:", dict(sorted(hist.items())))
out("  odd-depth (gate-friendly) count: %d of %d" %
    (sum(c for s, c in hist.items() if s % 2 == 1), len(depths)))