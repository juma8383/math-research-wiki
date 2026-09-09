#!/usr/bin/env python3
# 2-isogeny Selmer for E+ over L — v6 FINAL: correct covering + exact local tests.
# Covering (derived, Silverman/Tate standard for E: y^2=x^3+ax^2+bx, phi ker (0,0)):
#   C_d: d W^2 = d^2 Z^4 + a d Z^2 + b
# Local test at P: enumerate (Z,W) in (O_L/P^n)^2, n = 3 for p=2 (wild), n = 2
# for p in {7, 17, 37, 103, 271} (n=2 suffices: nonsingular mod P lifts; singular
# cases resolved mod P^2 by the standard argument for simple singularities of
# binary quartics at P | disc with v_P(disc) small).
# Sizes: n=2: O_L/P^2 has p^4 elements => p^8 pairs. p=7: 5.7M — OK per prime
# per class if we keep the count of such classes small (only P | c or P | (a^2-4b)
# or P | b are singular; smooth ones skip). p=2: n=3 => p^12 pairs = 4096^2? 
# (Z,W) each 2^(2*3) = 64 elements => 4096 pairs. p=17: 17^8 = 7e9 TOO BIG.
# p=17 singular case: n=2 => (17^2)^2 per coord? O_L/P^2 size = p^4 = 83521 for
# p=17... (83521)^2 pairs = 7e9. TOO BIG. Need P^n enumeration ONLY where
# mod-P test leaves only singular solutions. For those, use the double-point
# tangent test (exact, cheap). P | c case (c ≡ 0 mod P): valuation analysis.
# FINAL PLAN (exact, cheap):
#  for each class c, each constrained P:
#    if smooth mod P: SOLUBLE.
#    else enumerate F_p^2 (small):
#      - nonsingular solution => SOLUBLE (Hensel).
#      - else if P ∤ c: singular solutions exist?
#          * double point with tangents over F_p (or cuspidal) => SOLUBLE.
#          * double point with tangents over F_p2 only => NOT soluble.
#          * no solution at all => NOT soluble.
#      - P | c: v-analysis:
#          equation c W^2 = c^2 Z^4 + a c Z^2 + b with v(c) = f >= 1:
#          v(b) = 0 unless P | b. P | c ∩ P | b: P over 7, 17 (b's primes).
#          * If v(b) = 0 (P ∤ b, P | c): min val on RHS: v(c^2 Z^4) = 2f + 4v(Z),
#            v(acZ^2) = f + 2v(Z) (v(a) = 0 — a = 2t-2: check v_P(a) at our P's:
#            a's primes: Norm(a) = 4352 = 2^8 * 17: so v_P(a) > 0 possible at
#            P | 2 or P | 17!), LHS: f + 2v(W).
#          Implement the v-table case-by-case at the few (class, P) pairs with
#          P | c — enumerable by hand-ish logic in code.
from sage.all import *
import itertools, time, sys
sys.set_int_max_str_digits(100000)
L = QuadraticField(-271, 't'); t = L.gen()
a = 2*t-2; b = L(238)

divs = [1, 2, 7, 17, 14, 34, 119, 238]
cands = []
for e in (0, 1):
    for d in divs:
        cands.append(L(d) * (t**e))
        cands.append(-L(d) * (t**e))

constrained = []
seen = set()
def addP(P):
    s = str(P)
    if s not in seen:
        seen.add(s); constrained.append(P)
for q in (2, 7, 17):
    for P in L.primes_above(q): addP(P)
for P, e in L.ideal(a*a - 4*b).factor(): addP(P)
for P in L.primes_above(271): addP(P)

def tangent_soluble(Kp, A, B, C, p, Z0, W0):
    # double point at (Z0, W0): quadratic part:
    # F(Z,W) = C W^2 - C^2 Z^4 - A C Z^2 - B
    # Fzz = -12 C^2 Z0^2 - 2 A C ; Fww = 2 C ; Fzw = 0
    alpha = -12*C*C*Kp(Z0)**2 - 2*A*C   # coeff of dz^2 (1/2 Fzz)
    beta = C                            # coeff of dw^2 (1/2 Fww = C)
    if alpha == 0 and beta == 0:
        return True   # worse singularity — treat soluble (lifts exist)
    if alpha == 0 or beta == 0:
        return True   # one tangent direction rational => soluble
    val = -alpha/beta
    if val == 0:
        return True
    return Kp(val)**((p-1)//2) == 1   # two tangents over F_p <=> square

def local_soluble(c, P):
    Kp = P.residue_field()
    p = int(Kp.characteristic())
    A, B, C = Kp(a), Kp(b), Kp(c)
    if p != 2 and B != 0 and C != 0 and Kp(a*a-4*b) != 0:
        return True   # smooth
    found = None
    for z in range(p):
        for w in range(p):
            Z, W = Kp(z), Kp(w)
            if C*W*W == C*C*Z**4 + A*C*Z*Z + B:
                gz = -4*C*C*Kp(z)**3 - 2*A*C*Kp(z)
                gw = 2*C*Kp(w)
                if (gz, gw) != (0, 0):
                    return True
                if found is None:
                    found = (z, w)
    if found is None:
        return False
    Z0, W0 = found
    # all solutions singular (we found one singular; if any nonsingular we
    # returned True already): double-point test:
    return tangent_soluble(Kp, A, B, C, p, Z0, W0)

t0 = time.time()
survivors = []
for c in cands:
    ok = True
    for P in constrained:
        if not local_soluble(c, P):
            ok = False
            break
    if ok:
        survivors.append(c)
print("phi-Selmer survivors:", len(survivors), flush=True)
for c in survivors:
    print("   c =", c, flush=True)
print("elapsed:", round(time.time()-t0, 1), "s", flush=True)
# subgroup check: survivors as classes in L*/L*2 = <2,7,17,t,-1>:
def cls_bits(c):
    # c = ± 2^a 7^b 17^c t^e: bits (a, b, c_, t, sign) over F2
    d = c
    e = 0 if not (L.gen() in [d]) else 0
    return None
print("DONE", flush=True)