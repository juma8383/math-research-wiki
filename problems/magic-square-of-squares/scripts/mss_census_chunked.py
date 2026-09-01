# Chunked memory-bounded census engine for square-center 3x3 magic squares
# of squares.  Companion to mss_census_pythagorean.py (the W=1e6/1e7
# flagship): same validated semantics, but W >> 1e7 becomes memory-bound
# (the full D map holds ~0.05*W*ln W integers -> tens of GB at W=1e8), so
# this engine splits centers into blocks.
#
# Architecture (chunked):
#   pass 1 (count):  counts = array('I') over w <= W; one increment per
#                    (primitive triple m,n, k-scaling)  -- ~0.05*W*lnW steps.
#   pass 2 (blocks): for each block [lo, lo+Delta), walk the precomputed
#                    primitive-triple table (sorted by w0) and materialize
#                    D-lists only for w in the block; process the block,
#                    free, continue.  Per-block memory ~ total/num_blocks.
#
# Modes:
#   full : validated census semantics (>=7 squares, entry box M) --
#          reproduces the flagship output exactly (validation mode).
#   nsq9 : hunt the FULL 9-square solution via the |D|>=4 role filter --
#          all four role quantities {|b|, |c|, |b+c|, |b-c|} in D(w^2)
#          make all 8 non-center entries squares automatically, so the
#          whole test is set-membership (no isqrt per candidate); surviving
#          candidates are then verified by explicit nsq evaluation.
#          Deep hunt for the actual problem (centers <= W^2).
#
# Entry/params/canon semantics copied verbatim from the validated
# mss_census_pythagorean.py; the only new logic is chunking + the nsq9
# prefilter (both re-validated at W=1e6 against the flagship output).

import math
import sys
from array import array


def is_sq(n):
    if n < 1:
        return False
    r = math.isqrt(n)
    return r * r == n


def entries(a, b, c):
    return (a + b, a - b - c, a + c,
            a - b + c, a, a + b - c,
            a - c, a + b + c, a - b)


def canon(ent):
    g = list(ent)
    mats = []
    for _ in range(4):
        mats.append(tuple(g))
        h = [g[0], g[3], g[6], g[1], g[4], g[7], g[2], g[5], g[8]]
        mats.append(tuple(h))
        g = [g[6], g[3], g[0], g[7], g[4], g[1], g[8], g[5], g[2]]
    return min(mats)


def primitive(a, b, c):
    best = 1
    for cand in range(2, math.isqrt(min(abs(a), abs(b), abs(c))) + 1):
        cand2 = cand * cand
        if a % cand2 == 0 and b % cand2 == 0 and c % cand2 == 0:
            best = cand
    if best == 1:
        return a, b, c
    return a // (best * best), b // (best * best), c // (best * best)


BREMNER_PRIMS = {
    (180625, 138600, -41496), (180625, -41496, 138600),
    (180625, 138600, 41496), (180625, -138600, -41496),
    (180625, -138600, 41496), (180625, 41496, 138600),
    (180625, -41496, -138600), (180625, 41496, -138600),
}

CAND_FORMS = 6  # number of candidate (b,c) forms in the validated list


def build_primitive_triples(Wmax):
    """(w0, d0) for every primitive triple with hypotenuse <= Wmax, sorted
    by w0: w0 = m^2+n^2, u=|m^2-n^2|, v=2mn, d0 = 2uv."""
    ws = []
    ds = []
    m = 2
    while m * m + 1 <= Wmax:
        m2 = m * m
        for n in range(1, m):
            w0 = m2 + n * n
            if w0 > Wmax:
                break
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u0 = m2 - n * n
            v0 = 2 * m * n
            d0 = 2 * u0 * v0  # symmetric in (u,v) — no ordering needed
            ws.append(w0)
            ds.append(d0)
        m += 1
    order = sorted(range(len(ws)), key=lambda i: ws[i])
    w0s = array("q", (ws[i] for i in order))
    d0s = array("q", (ds[i] for i in order))
    return w0s, d0s


def count_pass(w0s, W, counts):
    """counts[w] += 1 for each triple multiple w = k*w0 <= W."""
    n = len(w0s)
    for i in range(n):
        w0 = w0s[i]
        if w0 > W:
            break
        for w in range(w0, W + 1, w0):
            counts[w] += 1


def block_D(w0s, d0s, lo, hi, counts, minlen):
    """Materialize D-lists for w in [lo, hi] with counts[w] >= minlen
    (counts from the count pass are an exact pre-filter on |D| — counts[w]
    IS |D(w^2)| after the count pass; minlen=0 + counts=None collects
    everything)."""
    D = {}
    n = len(w0s)
    for i in range(n):
        w0 = w0s[i]
        if w0 > hi:
            break
        # k-range with lo <= k*w0 <= hi
        k_start = (lo + w0 - 1) // w0
        k_end = hi // w0
        if k_end < k_start:
            continue
        d0 = d0s[i]
        for k in range(k_start, k_end + 1):
            w = k * w0
            if counts is not None and counts[w] < minlen:
                continue
            d = d0 * k * k
            key = w - lo
            lst = D.get(key)
            if lst is None:
                D[key] = [d]
            else:
                lst.append(d)
    return D


# ---- candidate forms (verbatim from validated mss_census_pythagorean.py) --
def candidate_pairs(x, y):
    cands = [(x, y), (x, y - x), (x, x - y), (y - x, x), (x + y, x)]
    if (x + y) % 2 == 0 and (x - y) % 2 == 0:
        cands.append(((x + y) // 2, (x - y) // 2))
    return cands


def nsq9_hit(w, a, dl, M):
    """Return (b, c) if some (b,c) has ALL FOUR roles |b|,|c|,|b+c|,|b-c|
    in D(w^2) with entries in [1,M] -> all 8 non-center entries squares."""
    Dset = set(dl)
    if len(Dset) < 4:
        return None
    for x in dl:
        for y in dl:
            if x == y:
                continue
            for (b, c) in candidate_pairs(x, y):
                if b == 0 or c == 0 or b == c or b == -c:
                    continue
                if abs(b) in Dset and abs(c) in Dset \
                        and abs(b + c) in Dset and abs(b - c) in Dset:
                    ent = entries(w * w, b, c)
                    if any(e < 1 or e > M for e in ent):
                        continue
                    nsq = sum(1 for e in ent if is_sq(e))
                    if nsq >= 8:  # >=8 of 9: report; 9 is full
                        return (b, c, nsq, ent)
    return None


def main():
    W = int(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else "nsq9"
    blockw = int(sys.argv[3]) if len(sys.argv) > 3 else 1000000
    M = int(sys.argv[4]) if len(sys.argv) > 4 else (
        4 * W * W if mode == "nsq9" else
        3000000000000000 if W >= 10**6 else 440000)
    print("chunked census: W=%d (centers <= %d) mode=%s block=%d M=%d"
          % (W, W * W, mode, blockw, M), flush=True)

    print("building primitive-triple table...", flush=True)
    w0s, d0s = build_primitive_triples(W)
    n_tr = len(w0s)
    print("primitive triples with hypotenuse <= W: %d" % n_tr, flush=True)

    if mode == "full":
        counts = None  # full mode needs no count pass (collect everything)
    else:
        counts = array("I", bytes(4 * (W + 1)))
        count_pass(w0s, W, counts)
        print("count pass done.", flush=True)

    raw = 0
    hits = {}
    discoveries = []
    for lo in range(2, W + 1, blockw):
        hi = min(W, lo + blockw - 1)
        if mode == "nsq9":
            D = block_D(w0s, d0s, lo, hi, counts, 4)
            for key, dl in D.items():
                w = lo + key
                a = w * w
                hit = nsq9_hit(w, a, sorted(dl), M)
                if hit:
                    b, c, nsq, ent = hit
                    hits[(a, b, c)] = (nsq, ent)
                    raw += 1
                    if nsq == 9:
                        print("*** FULL 9-SQUARE SOLUTION FOUND: center=%d "
                              "(w=%d) b=%d c=%d" % (a, w, b, c), flush=True)
                        print("    entries:", ent, flush=True)
        else:  # full: validated census semantics, chunked
            D = block_D(w0s, d0s, lo, hi, counts, 0)
            for key, dl in D.items():
                w = lo + key
                if len(dl) < 2:
                    continue
                a = w * w
                for x in dl:
                    for y in dl:
                        if x == y:
                            continue
                        for (b, c) in candidate_pairs(x, y):
                            if b == 0 or c == 0 or b == c or b == -c:
                                continue
                            ent = entries(a, b, c)
                            if any(e < 1 or e > M for e in ent):
                                continue
                            nsq = sum(1 for e in ent if is_sq(e))
                            if nsq >= 7:
                                hits[(a, b, c)] = (nsq, ent)
                                raw += 1

    print("done. raw configs found: %d" % len(hits), flush=True)
    for (a, b, c), (nsq, ent) in sorted(hits.items()):
        print("  config a=%d b=%d c=%d nsq=%d" % (a, b, c, nsq), flush=True)
    if mode == "nsq9" and not hits:
        print("=> no full 9-square (nsq>=8) config with center <= %d" % (W * W),
              flush=True)
    if mode == "full":
        prim = {}
        for (a, b, c), (nsq, ent) in hits.items():
            p = primitive(a, b, c)
            if p not in prim or nsq > prim[p][0]:
                prim[p] = (nsq, ent)
        classes = {}
        for (a, b, c), (nsq, ent) in prim.items():
            k = canon(ent)
            if k not in classes or nsq > classes[k][0]:
                classes[k] = (nsq, ent, (a, b, c))
        n_nonbrem = 0
        for k, (nsq, ent, abc) in sorted(classes.items(),
                                         key=lambda kv: -kv[1][0]):
            if abc not in BREMNER_PRIMS:
                n_nonbrem += 1
                print("  *** NON-BREMNER PRIMITIVE: a=%d b=%d c=%d nsq=%d"
                      % (abc + (nsq,)), flush=True)
                print("     entries:", ent, flush=True)
        print("primitive configs: %d ; dihedral classes: %d ; "
              "non-Bremner primitives: %d" % (len(prim), len(classes),
                                              n_nonbrem), flush=True)
        if n_nonbrem == 0:
            print("=> uniqueness of the Bremner/Sallows scaling orbit HOLDS"
                  " (centers <= %d)" % (W * W), flush=True)
        else:
            print("=> DISCOVERY: new primitive config(s) found", flush=True)


if __name__ == "__main__":
    main()