"""Targeted beyond-Buell hourglass search [mss-hourglass-targeted].

Buell 1999 exhaustively proved: NO additive triple {b,c,b+c} in any D(w^2)
with w <= 5e12 (center < 2.5e24).  This script goes BEYOND that frontier,
but only at *targeted* centers: w with many primes p == 1 (mod 4), where
|D(w^2)| = (prod(2e_p+1)-1)/2 is largest -- exactly where the Euler-product
heuristic concentrates the little tail mass that lies past Buell's box.

Method (exact, no search heuristics):
  Every rep w^2 = u^2+v^2 with d = 2uv comes from a Gaussian integer
  z = prod pi_i^{a_i} pibar_i^{b_i}, a_i+b_i = 2e_i (norm z = w^2),
  via d = |Im(z^2)| = 2|Re z||Im z|.  So D(w^2) is computed EXACTLY by
  enumerating all exponent splits (prod(2e_i+1) of them) and multiplying
  out the Gaussian factors -- no bound on u,v is ever needed, so w can be
  astronomically large (we reach w ~ 1e30, centers ~ 1e60).

Checks per w:  A2 (additive triple: exists x<y in D with x+y in D)
               A3 (parallelogram: A2 and y-x also in D)
Also re-verifies Lemma 4 (24 | d) on every element, and Lemma 1 (|D| formula).

Primality restriction note: multiplying w by a prime q != 1 (mod 4) only
scales every d by q (reps scale), preserving all additive relations, and
even w gives 4-scalings (Lemma 2) -- so the essentially NEW centers are
exactly w = prod p_i^{e_i} with all p_i == 1 (mod 4), w odd.  We enumerate
those (mixed exponents included), sorted by |D| descending, capped.

Output: per-w lines for every hit or structural anomaly; summary counts.
"""
import sys, itertools, json, time

# ---------------------------------------------------------------- candidates
PRIMES_1MOD4 = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113]

def gen_candidates(w_cap=10**30, dcap=2600, max_cands=4000, w_floor=5 * 10**12):
    """All w = prod p^e (p in PRIMES_1MOD4, e>=1), w_floor < w <= w_cap, |D|<=dcap.
    Filter FIRST (beyond-Buell), then sort by |D| desc and cap."""
    cands = []
    P = PRIMES_1MOD4
    def rec(i, w, prod):
        if i == len(P):
            if w > w_floor:
                d = (prod - 1) // 2
                if d >= 3 and d <= dcap:
                    cands.append((w, d))
            return
        e = 0; ww = w; pp = prod
        p = P[i]
        while True:
            rec(i + 1, ww, pp)
            e += 1
            if ww > w_cap // p: break
            ww *= p; pp *= (2 * e + 1)
            if pp - 1 > 2 * dcap: break
    rec(0, 1, 1)
    cands.sort(key=lambda t: (-t[1], t[0]))          # biggest |D| first
    del cands[max_cands:]
    return cands

# ------------------------------------------------------- exact D(w^2) via Z[i]
def two_squares(p):
    """p prime == 1 mod 4 -> (a,b), a^2+b^2=p."""
    a = int(p ** 0.5)
    while a >= 1:
        r = p - a * a
        b = int(r ** 0.5)
        if b * b == r:
            return a, b
        a -= 1
    raise ValueError(p)

def D_exact(w, factors):
    """factors: list of (p, e).  Returns sorted list of distinct d = 2|Re z Im z|.
    Enumerates all exponent splits a_i in [0, 2e_i]; z = prod pi^{a} pibar^{2e-a}.
    Conjugation/unit duplicates collapse when we take the SET of d values."""
    gs = []
    scale = 1
    for p, e in factors:
        if p % 4 == 1:
            a, b = two_squares(p)
            gs.append((a, b, 2 * e))                  # pi = a+bi, exponent 2e
        else:
            # inert (p=2 or p==3 mod 4): real factor p^e, d scales by p^(2e)
            scale *= p ** (2 * e)
    dset = set()
    n = len(gs)
    # per prime: all split-products pi^k * pibar^(E-k), k = 0..E
    parts = []
    for a, b, E in gs:
        pw = [(1, 0)]
        for _ in range(E):
            pr, pi = pw[-1]
            pw.append((pr * a - pi * b, pr * b + pi * a))
        qn = [(1, 0)]
        for _ in range(E):
            pr, pi = qn[-1]
            qn.append((pr * a + pi * b, pr * (-b) + pi * a))
        parts.append([ (pw[k][0] * qn[E - k][0] - pw[k][1] * qn[E - k][1],
                        pw[k][0] * qn[E - k][1] + pw[k][1] * qn[E - k][0])
                       for k in range(E + 1) ])
    def rec(idx, re, im):
        if idx == n:
            dset.add(abs(2 * re * im))                # d = 2|Re z||Im z|
            return
        for ar, ai in parts[idx]:
            rec(idx + 1, re * ar - im * ai, re * ai + im * ar)
    rec(0, 1, 0)
    return sorted(x * scale for x in dset if x)

def D_from_w(w):
    """factor w; residual prime after the loop MUST be appended."""
    fs = []; x = w
    d = 2
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0: x //= d; e += 1
            fs.append((d, e))
        d += 1 if d == 2 else 2
    if x > 1:
        fs.append((x, 1))
    return fs, True

def check_w(w, dlist):
    """A2/A3 additive-pattern check on the exact D-set (pure Python; d can
    exceed 2^63 so int64 numpy is unsafe).  A2: x<y in D with x+y in D.
    A3: A2 and y-x in D."""
    S = set(dlist)
    L = dlist
    n = len(L)
    a2 = 0; a3 = 0; first = None
    for i in range(n):
        x = L[i]
        for j in range(i + 1, n):
            y = L[j]
            s = x + y
            if s in S:
                a2 += 1
                if y - x in S:
                    a3 += 1
                    if first is None: first = (x, y, s, y - x)
    return a2, a3, first

def main():
    W_CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 10**30
    out = []
    cands = gen_candidates(w_cap=W_CAP, dcap=3400, max_cands=2500,
                           w_floor=5 * 10**12)   # BEYOND Buell's w <= 5e12 only
    t0 = time.time()
    n_beyond = 0; n_a2 = 0; n_a3 = 0; n_lem4 = 0; n_lem1 = 0
    maxD = 0; maxw = 0
    for idx, (w, dpred) in enumerate(cands):
        # factor w properly (candidates are products of known primes, but
        # factor anyway so the run is self-contained)
        fs, _ = D_from_w(w)
        prod1 = 1
        for p, e in fs:
            if p % 4 == 1: prod1 *= (2 * e + 1)
        dlist = D_exact(w, fs)
        if len(dlist) != (prod1 - 1) // 2: n_lem1 += 1
        if any(d % 24 for d in dlist): n_lem4 += 1
        n_beyond += 1                          # all cands have w > 5e12
        maxD = max(maxD, len(dlist)); maxw = max(maxw, w)
        a2, a3, first = check_w(w, dlist)
        if a2:
            n_a2 += 1
            if a3: n_a3 += 1
            line = f"A2 w={w} |D|={len(dlist)} a2={a2} a3={a3} first={first}"
            out.append(line); print(line, flush=True)
        if idx % 250 == 0:
            print(f"...{idx}/{len(cands)} w={w} |D|={len(dlist)} "
                  f"t={time.time()-t0:.0f}s", flush=True)
    print(f"== targeted summary: cands={len(cands)} beyondBuell(w>5e12)={n_beyond} "
          f"A2={n_a2} A3={n_a3} lem4viol={n_lem4} lem1viol={n_lem1} "
          f"time={time.time()-t0:.1f}s", flush=True)
    with open("hourglass_targeted.log", "w") as f:
        f.write("\n".join(out) + "\n" if out else "no A2/A3 hits\n")
        f.write(f"cands={len(cands)} beyondBuell={n_beyond} A2={n_a2} A3={n_a3} "
                f"lem4viol={n_lem4} lem1viol={n_lem1}\n")

if __name__ == "__main__":
    main()