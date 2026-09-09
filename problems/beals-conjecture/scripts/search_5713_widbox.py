"""
Signature (5,7,13) WIDER-BOX gap census (attempt-26, node beal-nearmiss-5713-widbox-verify).

Attempt-24 (box A<=6000, B<=600, C<=40) found min genuine gap 1771 at (6,3,2),
flagged to-verify. This run widens the box to

    C <= 120,   B <= 2*10^4,   A unbounded above (every A >= 1 covered),

preserving the gap definitions of search_5713.py / near_miss_package.py
EXACTLY:
  genuine near-miss gap = min |A^5 + B^7 - C^13| over coprime (gcd(A,B,C)=1)
  bases with A,B,C >= 2 and gap > 1; excluded from the genuine min: exact
  solutions (gap 0), gap-1 hits (enumerated separately, labeled per the T1
  universal families), and the quasi-degenerate layer (A^5==C^13 or
  B^7==C^13, gap = B^7 resp. A^5; tracked separately, T3).

Scan pattern (final-review fix): the overshoot region B^7 > C^13 stays
INCLUDED (fixing the break-at-BQ>CR bug of the original search_5713.py
min-gap loop), and the best-based break is REMOVED so the distinct-gaps
readout is complete over the whole box. Candidate window per (C,B):
for rem = C^13 - B^7 >= 2^5 the candidates are {fl-1, fl, fl+1}
(fl = floor(rem^(1/5)), clamped to A >= 2) -- the window contains the
unrestricted minimizer of |A^5-rem| (unimodality in A), and the
coprime-restricted column min too when fl is non-coprime (realized:
4939 @ (A,B,C)=(5,2,2)); for rem in [1,31] and overshoot the small-A
pattern is consecutive bases {2,3,4,5} (corrected-scan {2,3,4} extended
by one more A).

Universal degenerate gap-(+1) families for (p,q,r) = (5,7,13):
  t^65 + 1 : A = t^13, B = 1, C = t^5   [lcm(5,13) = 65]
  t^91 + 1 : A = 1, B = t^13, C = t^7   [lcm(7,13) = 91]

Run:  python search_5713_widbox.py    (PYTHONIOENCODING=utf-8; no external deps)
"""
import math, time

P, Q, R = 5, 7, 13
C_MAX = 120
B_MAX = 2 * 10 ** 4

TWO_P = 2 ** P   # 32: smallest A^5 with A >= 2


def iroot(n, k):
    """Exact integer floor k-th root of n >= 0."""
    if n < 1:
        return 0
    if n < 2 ** k:
        return 1
    r = 1 << ((n.bit_length() + k - 1) // k)
    while r ** k > n:
        r = ((k - 1) * r + n // r ** (k - 1)) // k   # Newton, decreasing
    while (r + 1) ** k <= n:
        r += 1
    return r


def exact_kth(n, k):
    if n < 1:
        return None
    r = iroot(n, k)
    return r if r ** k == n else None


def gcd3(a, b, c):
    return math.gcd(math.gcd(a, b), c)


BQ = [b ** Q for b in range(B_MAX + 1)]   # precomputed 7th powers, B <= 2e4


def family_of(A, B, C):
    """T1 universal gap-(+1) family label, else None."""
    if B == 1:
        t = iroot(A, R)
        if t >= 1 and t ** R == A and t ** P == C:
            return "t^65+1 (t=%d)" % t
    if A == 1:
        t = iroot(B, R)
        if t >= 1 and t ** R == B and t ** Q == C:
            return "t^91+1 (t=%d)" % t
    return None


t0 = time.time()

# ---- 1. exact solutions A^5 + B^7 = C^13 -----------------------------------
exact = []
exact_coprime = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for B in range(1, B_MAX + 1):
        rem = CR - BQ[B]
        if rem < 1:
            if BQ[B] > CR:
                break
            continue
        A = exact_kth(rem, P)
        if A is not None and A >= 1:
            exact.append((A, B, C))
            if gcd3(A, B, C) == 1:
                exact_coprime.append((A, B, C))

# ---- 2. gap-1 census |A^5 + B^7 - C^13| == 1 -------------------------------
gap1 = []
for C in range(1, C_MAX + 1):
    CR = C ** R
    for s in (+1, -1):
        target = CR + s
        for B in range(1, B_MAX + 1):
            rem = target - BQ[B]
            if rem < 1:
                if BQ[B] > target:
                    break
                continue
            A = exact_kth(rem, P)
            if A is not None and A >= 1:
                gap1.append((A, B, C, s))

# ---- 3. min genuine gap (corrected scan, overshoot region included) --------
best = None            # (gap, A, B, C, val); genuine = coprime, bases>=2, gap>1
best_at_C = {}         # C -> per-column best (Corner-Principle check)
quasi = None           # min coprime quasi-degenerate gap (T3 layer)
unit = None            # min unit-base |1 + B^7 - C^13| / |A^5 + 1 - C^13|
argmins = []
n_cand = 0
TOPN = 12
top = []
for C in range(2, C_MAX + 1):
    CR = C ** R
    c_best = None
    # unit-base channel (A=1 or B=1), other bases >= 2 (T1/T2 domain)
    b0 = iroot(CR, Q)
    for B in (b0, b0 + 1):
        if 2 <= B <= B_MAX:
            val = 1 + B ** Q - CR
            t = (abs(val), 1, B, C, val)
            if unit is None or t < unit:
                unit = t
    a0 = iroot(CR - 1, P)
    for A in (a0, a0 + 1):
        if A >= 2:
            val = A ** P + 1 - CR
            t = (abs(val), A, 1, C, val)
            if unit is None or t < unit:
                unit = t
    for B in range(2, B_MAX + 1):
        bqv = BQ[B]
        rem = CR - bqv
        # NO best-based break (final-review fix): the distinct-gaps readout
        # must stay complete over the whole box -- the old break truncated
        # small-C overshoot entries.
        if rem >= TWO_P:
            fl = iroot(rem, P)
            # Widened candidate window (final-review fix): |A^5-rem| is
            # unimodal in A (rem-A^5 decreasing for A<=fl, A^5-rem increasing
            # for A>=fl+1), so the UNRESTRICTED minimizer of |A^5-rem| lies
            # in {fl-1, fl, fl+1} (clamped to A >= 2), and every A outside
            # the window has |A^5-rem| >= the envelope value on its side
            # (left: g(fl-1); right: g(fl+1)). The coprime-restricted column
            # min can sit at fl-1 when fl is non-coprime (realized:
            # 4939 @ (A,B,C)=(5,2,2), beating 8743 @ (7,2,2)). COMPLETENESS
            # RESIDUAL (flagged, not overclaimed): if the in-window
            # candidates all share a factor with (B,C), the restricted min
            # is not PROVED to lie in the window -- it would then sit at the
            # nearest coprime layer beyond, with gap >= its side's envelope
            # value; the reviewer's independent census found no such further
            # miss in-box.
            cands = (fl - 1, fl, fl + 1)
        else:
            # small-rem (1 <= rem < 2^5) AND overshoot (rem < 0): val grows
            # with A, so the honest pattern is consecutive small bases from 2
            # -- corrected-scan {2,3,4} extended by one more A (final-review
            # fix) so the readout is not truncated at the small-C edge.
            cands = (2, 3, 4, 5)
        for A in cands:
            if A < 2:
                continue
            n_cand += 1
            AP = A ** P
            val = AP + bqv - CR
            g = abs(val)
            if g == 0:
                continue
            if AP == CR or bqv == CR:
                if gcd3(A, B, C) == 1:
                    t = (g, A, B, C, val)
                    if quasi is None or t < quasi:
                        quasi = t
                continue
            if g == 1:
                continue        # enumerated by the census loop
            if gcd3(A, B, C) != 1:
                continue
            t = (g, A, B, C, val)
            if best is None or t[0] < best[0]:
                best = t
                argmins = [t]
            elif t[0] == best[0] and t not in argmins:
                argmins.append(t)
            if c_best is None or t < c_best:
                c_best = t
            if len(top) < TOPN or t < top[-1]:
                top.append(t)
                top.sort()
                del top[TOPN:]
    if c_best is not None:
        best_at_C[C] = c_best

corner = None
for C in (2, 3):
    cb = best_at_C.get(C)
    if cb is not None and (corner is None or cb < corner):
        corner = cb

# ---- report -----------------------------------------------------------------
print("=== (5,7,13) WIDER-BOX GAP CENSUS ===")
print("box: C<=%d, B<=%d, A unbounded (all A>=1 covered)" % (C_MAX, B_MAX))
print("chi = 1/5+1/7+1/13-1 = -264/455 ~ -0.5802")

print()
print("--- exact solutions A^5+B^7=C^13 ---")
print("total: %d | coprime: %d" % (len(exact), len(exact_coprime)))
for t in exact[:20]:
    print("   ", t, "gcd=%d" % gcd3(*t))

print()
print("--- gap-1 census |A^5+B^7-C^13|==1 ---")
n_unit = sum(1 for (A, B, C, s) in gap1 if A == 1 or B == 1 or C == 1)
g1_genuine = [g for g in gap1 if g[0] >= 2 and g[1] >= 2 and g[2] >= 2]
g1_gen_coprime = [g for g in g1_genuine if gcd3(*g[:3]) == 1]
print("total hits: %d | unit-base (T1 domain): %d | all-bases>=2: %d | coprime: %d"
      % (len(gap1), n_unit, len(g1_genuine), len(g1_gen_coprime)))
for (A, B, C, s) in gap1:
    d = (A == 1 or B == 1 or C == 1)
    print("   A=%d B=%d C=%d gap=%+d unit-base=%s fam=%s gcd=%d"
          % (A, B, C, s, d, family_of(A, B, C), gcd3(A, B, C)))

print()
print("--- min GENUINE coprime near-miss gap (bases>=2, gap>1, quasi-degenerate excluded) ---")
print("min: %s" % (best,))
print("argmins (%d): %s" % (len(argmins), argmins[:10]))
print("smallest distinct genuine gaps (top %d):" % len(top))
for t in top:
    print("   gap=%d at (A,B,C)=(%d,%d,%d) val=%+d gcd=%d" % (t[0], t[1], t[2], t[3], t[4], gcd3(t[1], t[2], t[3])))
print("per-C minima (C: gap@(A,B,C)):")
for C in sorted(best_at_C)[:12]:
    t = best_at_C[C]
    print("   C=%d: %d @ (%d,%d,%d)" % (C, t[0], t[1], t[2], t[3]))
print("Corner Principle: corner (C<=3) min = %s | full-box min = %s | holds=%s"
      % (corner[0] if corner else None, best[0] if best else None,
         (corner is not None and best is not None and corner[0] == best[0])))

print()
print("--- quasi-degenerate layer (A^5==C^13 or B^7==C^13), coprime, in box ---")
print("min: %s  [gap equals B^7 resp. A^5]" % (quasi,))

print()
print("--- unit-base channel (A=1 or B=1), other bases >= 2 ---")
print("min: %s" % (unit,))

print()
print("candidate (A,B,C) triples evaluated: %d" % n_cand)
print("elapsed: %.1fs" % (time.time() - t0))