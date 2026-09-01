# Pythagorean-triple census for 3x3 magic squares of squares (square center).
#
# Replaces the entry-driven brute force (scratch_mss_prototype.py, ~B work for
# box B) with a triple-driven scan: every opposite pair a±d of squares around a
# square center a = w^2 arises from a Pythagorean triple (u,v,w), d = 2uv
# (pair = ((u-v)^2, (u+v)^2)); primitive triples (m,n) scaled by k cover all
# centers w^2 <= W^2 with ~0.08*W*ln(W) work instead of O(W^2).
#
# Census claim (see problem.md): scanning w <= W, the ONLY primitive
# square-center >=7-square config is the Bremner/Sallows square — hence every
# other solution is a global scaling k^2 * Bremner, or has center > W^2 /
# max entry > W^2 (max entry >= center). Coverage: entry bound M = W^2 forces
# center = w^2 <= M => w <= W => config appears in the enumeration
# (verify-confirmed completeness of the parametrization).
#
# Semantics of entries/pairs/canon copied verbatim from the validated
# scratch_mss_prototype.py.

import math
import sys


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


def build_D(W):
    """D[w] = list {2uv : u^2+v^2 = w^2, u>v>0}, 2 <= w <= W (primitive
    triples (m,n) k-scaled; d scales as k^2)."""
    D = {}
    m = 2
    while m * m + 1 <= W:
        m2 = m * m
        for n in range(1, m):
            w0 = m2 + n * n
            if w0 > W:
                break
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u0 = m2 - n * n
            v0 = 2 * m * n
            if u0 < v0:
                u0, v0 = v0, u0
            d0 = 2 * u0 * v0
            for w in range(w0, W + 1, w0):
                k = w // w0
                d = d0 * k * k
                dw = D.get(w)
                if dw is None:
                    D[w] = [d]
                else:
                    dw.append(d)
        m += 1
    return D


def census(W, M, min_squares=7):
    """All square-center configs with center w^2 <= W^2, entries in [1, M],
    nsq >= min_squares: {(a,b,c): (nsq, ent)}."""
    D = build_D(W)
    hits = {}
    for w, dl in sorted(D.items()):
        if len(dl) < 2:
            continue
        a = w * w
        for x in dl:
            for y in dl:
                if x == y:
                    continue
                cands = [(x, y), (x, y - x), (x, x - y), (y - x, x), (x + y, x)]
                if (x + y) % 2 == 0 and (x - y) % 2 == 0:
                    cands.append(((x + y) // 2, (x - y) // 2))
                for (b, c) in cands:
                    if b == 0 or c == 0 or b == c or b == -c:
                        continue
                    ent = entries(a, b, c)
                    if any(e < 1 or e > M for e in ent):
                        continue
                    nsq = sum(1 for e in ent if is_sq(e))
                    if nsq >= min_squares:
                        hits[(a, b, c)] = (nsq, ent)
    return hits


def primitive(a, b, c):
    """Factor out the largest square k^2 dividing (a, b, c). Global scalings
    of a config are exactly k^2*(a,b,c) (entrywise scaling), so this is the
    scaling quotient."""
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


if __name__ == "__main__":
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 700
    M = int(sys.argv[2]) if len(sys.argv) > 2 else 440000
    nsqmin = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    print("census: triples-driven, W=%d (centers <= %d), entry box M=%d"
          % (W, W * W, M))
    res = census(W, M, nsqmin)
    print("raw configs:", len(res))
    prim = {}
    for (a, b, c), (nsq, ent) in res.items():
        p = primitive(a, b, c)
        if p not in prim or nsq > prim[p][0]:
            prim[p] = (nsq, ent)
    classes = {}
    for (a, b, c), (nsq, ent) in prim.items():
        k = canon(ent)  # entry-level dihedral canonical form (validated)
        if k not in classes or nsq > classes[k][0]:
            classes[k] = (nsq, ent, (a, b, c))
    n_nonbrem = 0
    for k, (nsq, ent, abc) in sorted(classes.items(), key=lambda kv: -kv[1][0]):
        if abc not in BREMNER_PRIMS:
            n_nonbrem += 1
            print("  *** NON-BREMNER PRIMITIVE: a=%d b=%d c=%d nsq=%d maxentry=%d"
                  % (abc + (nsq, max(ent))))
            print("     entries:", ent)
    print("primitive configs: %d ; dihedral classes: %d ; non-Bremner primitives: %d"
          % (len(prim), len(classes), n_nonbrem))
    if n_nonbrem == 0:
        print("=> uniqueness of the Bremner/Sallows scaling orbit HOLDS:"
              " the only square-center nsq>=%d config with center <= %d is"
              " Bremner/Sallows (up to its global scalings)"
              % (nsqmin, W * W))
    else:
        print("=> DISCOVERY: new primitive square-center config(s) found")