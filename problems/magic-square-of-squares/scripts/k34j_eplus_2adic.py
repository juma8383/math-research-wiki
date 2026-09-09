#!/usr/bin/env python3
# EXACT 2-adic local solubility for the C_d quartics at the two primes over 2.
# O_L = Z[t]/(t^2 + 271). P = (2, 1/2 t - 1/2) means: t ≡ 1 mod P (t-1 in P:
# (t-1)/2: t ≡ 1 mod P ✓). P2b: t ≡ -1 = 1 mod 2 — same mod 2! Both primes
# reduce t ≡ 1 mod 2; they differ mod 4: t ≡ 1 vs t ≡ 3 mod 4 (P2a: (t-1)/2
# in P => t = 1 + 2u: u ∈ P: mod P^n: t ≡ 1 mod 2 exactly; to distinguish,
# work with the P-adic structure: P2a = (2, t-1), P2b = (2, t+1).
# Exact local ring model: O_L/P^n with P = (2, t - c): elements a + b t,
# (a, b) in Z/2^n, t ≡ c mod P. Mod P^n: the ideal P^n = (2^n, (t-c)^n).
# An element a + bt ≡ 0 mod P^n iff (a + b*c) ≡ 0 mod 2^n AND b ≡ 0 mod 2^{n-1}?
# (t - c)^n ∈ P^n: expansion: (a + bt) = (a + bc) + b(t - c): for this to be in
# P^n = (2^n, (t-c)^n): need a + bc ≡ 0 mod 2^n and b(t-c) ∈ P^n iff b ∈ P^{n-1}
# (t-c) part: b*(t-c) with b = b1*2^k...: standard: (a + bt) ∈ P^n iff
# a + b*c ≡ 0 mod 2^n and b ≡ 0 mod 2^{n-1}?? For n=1: a + bc ≡ 0 mod 2 ✓ (P=(2,t-c)).
# Simplest exact approach: work in Z/2^n with t ≡ c: elements ARE pairs (a,b)
# mod 2^n; two pairs (a,b), (a',b') represent the same element mod P^n iff
# (a-a') + (b-b')*c ≡ 0 mod 2^n and (b-b') ≡ 0 mod 2^{n-1}*?? — no: P^n ⊇
# (2^n) and P^n = (2, t-c)^n: (t-c)^n ∈ P^n: elements (a+bt) - (a'+b't) =
# (a-a') + (b-b')t: in P^n iff it's a Z-combination of 2^n and (t-c)^n·O_L:
# canonical: O_L/P^n ≅ Z/2^n [u]/(u^n) with u = t - c: since (t-c)^2 = -271 - 2c t
# + c^2 - ... = -(c^2+271) - 2c u: c^2 + 271 ≡ 0 mod 2: = 2*m0: so
# u^2 = -2*m0... wait mod 2^n: u^2 = -(c^2 + 271) - 2cu = -2*m0*?? c^2 + 271 = 2*m0
# (c odd => c^2 + 271 = c^2 + 271: 271 ≡ 7 mod 8: c^2 ≡ 1 mod 8: c^2+271 ≡ 0 mod 8:
# m0 = (c^2+271)/2 EVEN? c^2 + 271 ≡ 1 + 7 = 8 ≡ 0 mod 8 => m0 = (c^2+271)/2 ≡ 0 mod 4:
# u^2 = -2*m0 - 2c u with 2*m0 ≡ 0 mod 8: u^2 ≡ 0 mod 8 - 2c u: u is nilpotent mod P^n
# with u^2 ≈ -2c u mod 8-ish: exact: O_L/P^n = Z/2^n[u]/(u^2 + 2c u + 2 m0).
# Enumerate (A, B) in (Z/2^n)^2, ring ops with the reduction u^2 = -2c u - 2 m0.
# n = 5 (P^5): 1024 elements => (Z,W) pairs 1M per class-prime: 4 survivors x
# 2 primes x 1M = 8M ring ops in Python — slow but OK (~minutes). n=4: 65k pairs, fast.
# CORRECTNESS: solubility over L_P iff soluble mod P^n for ALL n; if a solution
# exists mod P^4 with the Hensel condition (nonsingular) => done. Singular
# solutions need deeper analysis, but for p=2 with quartic: solutions mod
# P^4 with v(derivs) small still lift if the gradient has valuation < n/2...
# use: soluble mod P^{2k+1} with a solution whose gradient is a UNIT mod P^k
# => lifts to all n (Hensel for p=2 needs care: gradient unit suffices).
# Implement: n = 5, require solution with gradient unit mod P => SOLUBLE;
# solution with gradient valuation 1..: try mod P^{n+1} with the same solution
# pattern... to keep it bounded: n = 6 for the 4 survivors only.
from sage.all import *
import itertools, time, sys
L = QuadraticField(-271, 't'); t = L.gen()
a = 2*t-2; b = L(238)

def ring_setup(P, n):
    mn = 2**n
    Kp = P.residue_field()
    c = int(Kp(t))
    m0 = (c*c + 271) // 2
    def mul(x, y):
        A1,B1 = x; A2,B2 = y
        A = (A1*A2 - 2*m0*B1*B2) % mn
        B = (A1*B2 + A2*B1 - 2*c*B1*B2) % mn
        return (A, B)
    def evpoly(el):
        co = el.polynomial().list() + [0,0]
        return ((int(co[0]) + int(co[1])*c) % mn, int(co[1]) % mn)
    return mul, ev, mn, c

def soluble_2adic(c, P, n=5):
    mul, ev, mn, c0 = ring_setup(P, n)
    crep = ev(c)
    # a = 2t - 2: (A,B) = (0 + 2c, 2)?? ev handles.
    arep = ev(a); brep = ev(b)
    # equation: c*W^2 = c^2*Z^4 + a*c*Z^2 + b  (in O_L/P^n)
    def sq(x): return mul(x, x)
    def add(x, y): return ((x[0]+y[0]) % mn, (x[1]+y[1]) % mn)
    def muli(x, k): return ((x[0]*k) % mn, (x[1]*k) % mn)
    ac = mul(arep, crep)
    cc = mul(crep, crep)
    rng = range(mn)
    sols = []
    for za in range(mn):
        for zb in range(mn):
            Z = (za, zb)
            Z2 = sq(Z); Z4 = sq(Z2)
            acZ2 = mul(ac := mul(arep, crep), Z2)
            rhs = add(mul(cc, Z4), add(acZ2, brep))
            for wa in range(mn):
                for wb in range(mn):
                    W = (wa, wb)
                    lhs = mul(crep, sq(W))
                    if lhs == rhs:
                        # gradient check for lifting:
                        # F = cW^2 - c^2Z^4 - acZ^2 - b; dF/dZ = -4c^2Z^3 - 2acZ;
                        # dF/dW = 2cW: nonsingular iff gradient not ≡ 0 mod P (i.e. mod 2)
                        gA = (-(4*cc[0]//1)*0)  # placeholder
                        # compute gradient in ring: dF/dZ = -(4 c^2 Z^3 + 2 a c Z)
                        z3 = mul(Z2, Z)
                        gz = muli(add(muli(mul(cc, z3), -1), muli(mul(arep, crep), 0)), 0)
                        # do it cleanly:
                        gz = add(muli(mul(cc, z3), -4), muli(mul(arep, mul(crep, Z)), -2))
                        gw = muli(mul(crep, W), -2)
                        # unit check mod P: reduce mod 2: (A,B) mod 2:
                        def mod2(x): return (x[0] % 2, x[1] % 2)
                        if mod2(gz) != (0,0) or mod2(gw) != (0,0):
                            return True, (Z, W), "nonsingular"
                        sols.append((Z, W))
    if sols:
        return False, f"singular-only ({len(sols)} sols), e.g. {sols[0]}"
    return False, "no solution mod P^%d" % n

divs = [1, 7, 34, 238]
t0 = time.time()
for d in divs:
    for dd in (d, -d):
        res = []
        for P in L.primes_above(2):
            ok, info = soluble_2adic(dd, P)
            res.append((str(P), ok, info))
        print(f"c = {dd}:", res, flush=True)
print("elapsed:", round(time.time()-t0,1), flush=True)
print("DONE", flush=True)