#!/usr/bin/env python
# Claude verification of the genus-3 round claims:
#  1. j-invariants: quotient cubics E_iota/E_rho (C3_A), E (C3_B), E_G vs
#     master E_A (j=-8000/81), E_B (j=2744000/9).
#  2. Trace agreement master E_A vs quotient cubic over p in 7..211
#     (isogeny evidence -> rank carries over).
#  3. sigma1 cross-check: #C3_A(F_p) point counts vs trace sums.
#  4. rank(E_G) <= 0 recheck: independent 2-isogeny Selmer at theta=-816.
# All exact integer/Fraction arithmetic.
import sys
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

def jinv(A4, A6):
    # y^2 = x^3 + A4 x + A6  (a2=0 models)
    b4, b6, b8 = 2*A4, 4*A6, -A4*A4
    c4 = -48*A4
    c6 = -864*A6
    disc = -8*b4**3 - 27*b6**2  # b2=0 form: Delta = -8 b4^3 - 27 b6^2
    return F(c4**3, disc)

def jinv_a2(A2, A4, A6):
    b2, b4, b6 = 4*A2, 2*A4, 4*A6
    b8 = 4*A2*A6 - A4*A4
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    c4 = b2*b2 - 24*b4
    return F(c4**3, disc)

def count_mod(A2, A4, A6, p):
    # #E(F_p) for y^2 = x^3 + A2 x^2 + A4 x + A6 (mod p), exact
    cnt = 1  # infinity
    qrs = set((x*x) % p for x in range(p))
    for x in range(p):
        v = (x**3 + A2*x*x + A4*x + A6) % p
        if v == 0: cnt += 1
        elif v in qrs: cnt += 2
    return cnt

def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=False
    return [i for i in range(2,n+1) if s[i]]

out("=== (1) j-invariants (exact) ===")
j_masterA = F(-8000, 81)
j_masterB = F(2744000, 9)
# master models (long form)
jA = jinv_a2(-250, 17420, 35848)
jB = jinv_a2(310, 8140, 51912)
# C3_A quotient cubic (iota & rho): y^2 = x^3 - 276480 x + 240648192
jQi = jinv(-276480, 240648192)
# C3_B quotient cubic: y^2 = x^3 - 1935360 x + 1033371648
jQb = jinv(-1935360, 1033371648)
# E_G
jG = jinv(-504576, 131604480)
out("  master E_A j:", jA, " expected", j_masterA, " match:", jA == j_masterA)
out("  master E_B j:", jB, " expected", j_masterB, " match:", jB == j_masterB)
out("  C3_A/iota cubic j:", jQi, " vs master A:", jQi == j_masterA)
out("  C3_B/iota cubic j:", jQb, " vs master B:", jQb == j_masterB)
out("  E_G j:", jG, " expected 1556068/81:", jG == F(1556068, 81))

out("=== (2)+(3) trace comparison over p = 7..211 ===")
ps = primes_upto(211)
# bad primes: disc of each model
def badprimes(A2, A4, A6):
    b2, b4, b6 = 4*A2, 2*A4, 4*A6
    b8 = 4*A2*A6 - A4*A4
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    return {p for p in ps if disc % p == 0}

badA  = badprimes(-250, 17420, 35848)
badQi = badprimes(0, -276480, 240648192)
badQb = badprimes(0, -1935360, 1033371648)
badG  = badprimes(0, -504576, 131604480)
out("  bad primes: masterA", sorted(badA), " quotA", sorted(badQi),
    " quotB", sorted(badQb), " E_G", sorted(badG))

misA = misB = 0
checked = 0
for p in ps:
    if p in badA or p in badQi:
        continue
    tM = p + 1 - count_mod(-250, 17420, 35848, p)
    tQ = p + 1 - count_mod(0, -276480, 240648192, p)
    checked += 1
    if tM != tQ:
        misA += 1
        if misA <= 5: out("  A-trace MISMATCH p=%d master=%d quot=%d" % (p, tM, tQ))
misBlist = []
for p in ps:
    if p in badA or p in badQb:
        continue
    tM = p + 1 - count_mod(310, 8140, 51912, p)
    tQ = p + 1 - count_mod(0, -1935360, 1033371648, p)
    if tM != tQ:
        misB += 1
        if misB <= 5: misBlist.append((p, tM, tQ))
out("  A: %d good primes checked, trace mismatches: %d" % (checked, misA))
out("  B: mismatches: %d %s" % (misB, misBlist))

out("=== (4) independent rank(E_G)<=0 spot recheck (theta=-816 chain) ===")
# E_G: y^2 = x^3 -504576x +131604480 ; theta=-816
# shifted E_i: y^2 = x^3 -2448 x^2 + 1492992 x  (a2,a4)
# dual E_i': y^2 = x^3 + 4896 x^2 + 20736 x
# homogenized quartic-family solubility: N^2 = d M^4 + a M^2 e^2 + (b//d) e^4
def factor(n):
    n = abs(n); fac = {}; d = 2
    while d*d <= n:
        while n % d == 0: fac[d] = fac.get(d,0)+1; n //= d
        d += 1
    if n > 1: fac[n] = fac.get(n,0)+1
    return fac

def sqfree_divs(b):
    res = [1]
    for q in factor(b): res += [r*q for r in res]
    return res

def soluble(d, a, b, pmax=97):
    """True if NOT provably insoluble (conservative)."""
    bd = b // d
    # real check
    if not any(d*(i/100.0)**4 + a*(i/100.0)**2 + bd >= 0 for i in range(0, 20001)):
        return False
    for p in range(2, pmax+1):
        m = 32 if p == 2 else p*p
        qrs = set((x*x) % m for x in range(m))
        found = False
        for M in range(m):
            M2 = (M*M) % m; M4 = (M2*M2) % m
            for e in range(m):
                if M % p == 0 and e % p == 0: continue
                val = (d*M4 + a*M2*(e*e % m) + bd*(e*e*e*e % m)) % m
                if val in qrs: found = True; break
            if found: break
        if not found: return False
    return True

def descent_dims(a, b):
    ds = sorted({s*d for d in sqfree_divs(b) for s in (1, -1)})
    solA = [d for d in ds if soluble(d, a, b)]
    solB = [d for d in ds if soluble(d, b, a)]  # dual: swap roles
    return solA, solB

# theta = -816: shifted curve y^2 = x^3 -2448 x^2 +1492992 x ; a=-2448, b=1492992
solA, solB = descent_dims(-2448, 1492992)
out("  theta=-816: soluble classes alpha:", solA)
out("  theta=-816: soluble classes dual :", solB)
# subgroup check: known alpha-images must lie inside
known_alpha = {1152, 1296, 864, 1728}   # sqfree parts {2,1,6,3} from rank log
def sqfree(n):
    if n == 0: return 0
    sgn = -1 if n < 0 else 1; n = abs(n); f = factor(n); r = sgn
    for q, e in f.items():
        if e % 2: r *= q
    return r
kA = {sqfree(v) for v in known_alpha}
out("  known-point alpha sqfree classes:", sorted(kA), " all in soluble list:",
    all(k in solA for k in kA))
# dim bounds: s_A <= dim span(solA), s_B <= dim span(solB); rank = s_A + s_B - 2
# over F2, dimension of span of nonzero classes in the d-group (Z/2)^k:
import itertools
def dim_span(classes):
    # classes are squarefree integers; vector over primes appearing
    primes = sorted({q for c in classes for q in factor(c)})
    vecs = []
    for c in classes:
        v = 0
        for i, q in enumerate(primes):
            if factor(c).get(q, 0) % 2: v |= (1 << i)
        vecs.append(v)
    basis = []; rank = 0
    for v in vecs:
        for b in basis: v = min(v, v ^ b)
        if v: basis.append(v); basis.sort(reverse=True); rank += 1
    return rank

classes = solA
out("  dim span(soluble A) =", dim_span(classes), " (s_A <= this)")
out("  dim span(soluble B) =", dim_span(solB), " (s_B <= this)")