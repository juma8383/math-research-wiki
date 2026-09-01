# mss_two_prime_k58_branch.py -- 2026-09-01
# Attack on kill-equations K5-K8 (filed in notes.md [mss-two-prime-freeness]):
#   K5 : A+D0 = B          -> Y_q (p^2 + R_p) = Y_p (q^2 - R_q)   sign combo (+,-)
#   K6a/b: A+C = B sign-split:
#        X>Y (C=X-Y)       -> Y_q (p^2 + R_p) = Y_p (q^2 + R_q)   sign combo (+,+)
#        Y>X (C=Y-X)       -> Y_q (p^2 - R_p) = Y_p (q^2 - R_q)   sign combo (-,-)
#   K7a/b, K8: B-side mirrors:
#        B+D0 = A          -> Y_q (p^2 - R_p) = Y_p (q^2 + R_q)   sign combo (-,+)
#        B+C = A (Y>X)     -> sign combo (-,+)   ; (X>Y) -> (-,-)
#
# KEY LEMMA (branch split). For prime n = a^2+b^2 (1 mod 4), a>b>0, put
#   s = a^2-b^2, t = ab, Y = 4 s t, R = |a^4-6a^2b^2+b^4| = |Re(pi^4)|,
#   re = a^4-6a^2b^2+b^4 (signed), u = s/t = x - 1/x with x = a/b.
# Then n^2 = s^2 + 4t^2 and
#   {n^2+R, n^2-R} = { 2 s^2, 8 t^2 },
#   n^2+R = 2s^2  <=>  re > 0  <=>  u > 2   (since re = s^2 - 4t^2 = n^2-8t^2).
# Call 2s^2 the "S-branch" and 8t^2 the "T-branch" of prime n.
#
# Each K5-K8 equation is  Y_q * alpha_p = Y_p * beta_q  with
# alpha in {n^2 +/- R_n}, beta in {q^2 +/- R_q}. Substituting Y=4st:
#   same branch  (both S or both T):  s_p t_q = s_q t_p  <=>  u_p = u_q
#                                     <=>  a_p/b_p = a_q/b_q <=> p = q  (DEAD)
#   cross branch (one S one T):       s_p s_q = 4 t_p t_q <=> u_p u_q = 4
#     unique positive solution: x_q = (x_p+1)/(x_p-1) = (a_p+b_p)/(a_p-b_p),
#     and gcd(a_p+b_p, a_p-b_p)=1 (a,b opposite parity, both sums odd),
#     so (c_q,d_q) = (a_p+b_p, a_p-b_p) and q = c_q^2+d_q^2 = 2(a_p^2+b_p^2)
#     = 2p -- impossible for distinct odd primes (DEAD).
# => THEOREM K58: none of the four equations holds for any 1 mod 4 pair p<q.

import time
from math import isqrt, gcd

LOG = r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_two_prime_k58_branch.log"
out = open(LOG, "w", encoding="utf-8")
def w(line=""):
    out.write(line + "\n")
    out.flush()

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(range(i*i, n+1, i)))
    return [i for i in range(2, n + 1) if sieve[i]]

def rep(p):
    """primitive rep a>b>0 of prime p = a^2+b^2"""
    for a in range(isqrt(p - 1), 0, -1):
        b = isqrt(p - a*a)
        if b >= 1 and b*b == p - a*a and a != b:
            return (max(a, b), min(a, b))
    return None

t0 = time.time()

# ---------- Part 1: per-prime branch-split lemma, all 1 mod 4 primes <= 50000 ----------
P1 = 50000
pr = [p for p in primes_upto(P1) if p % 4 == 1]
w("=== Part 1: branch-split lemma, 1 mod 4 primes <= %d ===" % P1)
w("count = %d" % len(pr))

bad_split = 0
bad_branch = 0
prime_data = {}
for p in pr:
    a, b = rep(p)
    s = a*a - b*b
    t = a*b
    Y = 4 * s * t
    re = a**4 - 6*a*a*b*b + b**4
    R = abs(re)
    p2 = p * p
    # split check: {p^2+R, p^2-R} == {2s^2, 8t^2}
    got = {p2 + R, p2 - R}
    want = {2*s*s, 8*t*t}
    if got != want:
        bad_split += 1
        if bad_split <= 5:
            w("SPLIT FAIL p=%d" % p)
    # branch rule: p^2+R == 2s^2 <=> re>0 <=> u>2 (u = s/t, s,t>0)
    lhs = (p2 + R == 2*s*s)
    rhs = (re > 0) and (s > 2*t)
    if lhs != rhs:
        bad_branch += 1
        if bad_branch <= 5:
            w("BRANCH FAIL p=%d lhs=%s rhs=%s" % (p, lhs, rhs))
    prime_data[p] = (Y, R, p2, s, t, re > 0)
w("split violations   = %d" % bad_split)
w("branch violations  = %d" % bad_branch)
w("part 1 time %.1fs" % (time.time() - t0))

# ---------- Part 2: pair-level iff verification + census, all p<q <= 30000 ----------
t1 = time.time()
P2 = 30000
pr2 = [p for p in primes_upto(P2) if p % 4 == 1]
w("")
w("=== Part 2: pair iff-check + census, 1 mod 4 primes <= %d ===" % P2)
w("count = %d primes, %d pairs" % (len(pr2), len(pr2)*(len(pr2)-1)//2))

mismatch = 0          # equation vs branch-prediction mismatches
hits_eq = 0           # pairs where some sign combo actually holds
hits_same_u = 0       # same-branch with s_p t_q = s_q t_p
hits_cross4 = 0       # cross-branch with s_p s_q = 4 t_p t_q
rel_hits = {}         # K5-K8 relation census
for name in ("K5_A+D0=B", "K6a_A+C=B(X>Y)", "K6b_A+C=B(Y>X)",
             "K7_B+D0=A", "K8_B+C=A"):
    rel_hits[name] = 0

npairs = 0
for i in range(len(pr2)):
    p = pr2[i]
    Yp, Rp, p2, sp, tp, repos = prime_data[p]
    for j in range(i + 1, len(pr2)):
        q = pr2[j]
        Yq, Rq, q2, sq, tq, reqos = prime_data[q]
        npairs += 1
        X = Rp * Yq
        Yel = Yp * Rq
        A = p2 * Yq
        B = q2 * Yp
        C = X - Yel
        if C < 0:
            C = -C
        D0 = X + Yel
        # K5-K8 relation census (direct, from the set elements)
        if A + D0 == B:
            rel_hits["K5_A+D0=B"] += 1
        if X > Yel and A + C == B:
            rel_hits["K6a_A+C=B(X>Y)"] += 1
        if Yel > X and A + C == B:
            rel_hits["K6b_A+C=B(Y>X)"] += 1
        if B + D0 == A:
            rel_hits["K7_B+D0=A"] += 1
        if B + C == A:
            rel_hits["K8_B+C=A"] += 1
        # four sign combos: Yq*(p2 +/- Rp) == Yp*(q2 +/- Rq)
        for sp_sig in (1, -1):
            ap = p2 + sp_sig * Rp
            bp_s = (sp_sig == repos)      # alpha is S-branch?
            for sq_sig in (1, -1):
                bq = q2 + sq_sig * Rq
                bq_s = (sq_sig == reqos)  # beta is S-branch?
                eq = (Yq * ap == Yp * bq)
                if bp_s == bq_s:
                    pred = (sp * tq == sq * tp)          # same-branch: u_p = u_q
                    if eq and pred:
                        hits_same_u += 1
                else:
                    pred = (sp * sq == 4 * tp * tq)      # cross: u_p u_q = 4
                    if eq and pred:
                        hits_cross4 += 1
                if eq != pred:
                    mismatch += 1
                    if mismatch <= 10:
                        w("IFF MISMATCH p=%d q=%d sig=%d,%d eq=%s pred=%s"
                          % (p, q, sp_sig, sq_sig, eq, pred))
                if eq:
                    hits_eq += 1

w("pairs tested          = %d" % npairs)
w("iff mismatches        = %d" % mismatch)
w("sign-combo equations holding = %d" % hits_eq)
w("same-branch u_p=u_q hits     = %d" % hits_same_u)
w("cross-branch u_p*u_q=4 hits  = %d" % hits_cross4)
for k in rel_hits:
    w("relation %-16s hits = %d" % (k, rel_hits[k]))
w("part 2 time %.1fs" % (time.time() - t1))

# ---------- Part 3: q=2p lemma direct probe ----------
# If u_p*u_q = 4 then x_q = (a_p+b_p)/(a_p-b_p), q = 2p. Corroborate the
# identity x_q=(x_p+1)/(x_p-1) <=> u_p u_q = 4 on rational x values.
w("")
w("=== Part 3: identity check x'=(x+1)/(x-1) <=> (x-1/x)(x'-1/x')=4 ===")
import random
from fractions import Fraction
random.seed(1)
bad = 0
trials = 0
while trials < 2000:
    an = random.randint(2, 10**6)
    bn = random.randint(1, an - 1)
    if gcd(an, bn) != 1 or an - bn <= 0:
        continue
    x = Fraction(an, bn)
    xp = Fraction(an + bn, an - bn)     # x' = (x+1)/(x-1)
    if xp <= 1:
        continue
    u = x - 1 / x
    up = xp - 1 / xp
    trials += 1
    if u * up != 4:
        bad += 1
        if bad <= 5:
            w("IDENT FAIL x=%s u*up=%s" % (x, u * up))
w("identity violations (of %d trials) = %d" % (trials, bad))

# ---------- Part 4: extended relations-only census, p<q <= 100000 ----------
t2 = time.time()
P4 = 100000
pr4 = [p for p in primes_upto(P4) if p % 4 == 1]
w("")
w("=== Part 4: relations-only census, 1 mod 4 primes <= %d ===" % P4)
w("count = %d primes, %d pairs" % (len(pr4), len(pr4)*(len(pr4)-1)//2))
prime_data4 = {}
for p in pr4:
    a, b = rep(p)
    s = a*a - b*b
    prime_data4[p] = (4*s*a*b, abs(a**4-6*a*a*b*b+b**4), p*p)
tot4 = 0
hits4 = 0
for i in range(len(pr4)):
    p = pr4[i]
    Yp, Rp, p2 = prime_data4[p]
    for j in range(i + 1, len(pr4)):
        q = pr4[j]
        Yq, Rq, q2 = prime_data4[q]
        tot4 += 1
        X = Rp * Yq
        Yel = Yp * Rq
        A = p2 * Yq
        B = q2 * Yp
        C = X - Yel
        if C < 0:
            C = -C
        D0 = X + Yel
        if A + D0 == B or B + D0 == A or A + C == B or B + C == A:
            hits4 += 1
            w("HIT p=%d q=%d" % (p, q))
w("pairs = %d, relation hits = %d" % (tot4, hits4))
w("part 4 time %.1fs" % (time.time() - t2))

w("")
w("TOTAL time %.1fs" % (time.time() - t0))
w("ALL CHECKS COMPLETE")
out.close()
print("done")