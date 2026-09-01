# Prototype: exhaustive search for 3x3 magic squares with many square entries.
#
# Structure (derived):
#   Every 3x3 magic square of integers = (a,b,c) parametrization:
#     row1: a+b,     a-b-c, a+c
#     row2: a-b+c,   a,     a+b-c
#     row3: a-c,     a+b+c, a-b
#   Opposite pairs through center: a±b, a±c, a±(b+c), a±(b-c).
#   A pair a±d of SQUARES exists iff a = u^2+v^2 (u>v>0) with d = 2uv,
#   the pair being ((u-v)^2, (u+v)^2).

import math

def is_sq(n):
    if n < 1:
        return False
    r = math.isqrt(n)
    return r * r == n

def entries(a, b, c):
    return (a + b, a - b - c, a + c,
            a - b + c, a, a + b - c,
            a - c, a + b + c, a - b)

def search(B, min_squares=7):
    """Enumerate centers a = n^2 <= B (all configs with SQUARE center).
    Returns list of (a,b,c,nsq,ent) with nsq >= min_squares, all entries in [1,B]."""
    results = []
    n = 1
    while n * n <= B:
        a = n * n
        D = []
        for v in range(1, int(n / math.sqrt(2)) + 1):
            u2 = a - v * v
            u = math.isqrt(u2)
            if u * u == u2 and u > v:
                D.append(2 * u * v)
        if len(D) >= 2:
            for x in D:
                for y in D:
                    if x == y:
                        continue
                    # ordered pair (x,y) plays two of the roles {b, c, b+c, b-c}
                    cands = [(x, y)]                                  # (b, c) = (x, y)
                    cands.append((x, y - x))                          # (b, b+c) = (x, y)
                    cands.append((x, x - y))                          # (b, b-c) = (x, y)
                    cands.append((y - x, x))                          # (c, b+c) = (x, y)
                    cands.append((x + y, x))                          # (c, b-c) = (x, y)
                    if (x + y) % 2 == 0 and (x - y) % 2 == 0:         # (b+c, b-c) = (x, y)
                        cands.append(((x + y) // 2, (x - y) // 2))
                    for (b, c) in cands:
                        if b == 0 or c == 0 or b == c or b == -c:
                            continue
                        ent = entries(a, b, c)
                        if any(e < 1 or e > B for e in ent):
                            continue
                        nsq = sum(1 for e in ent if is_sq(e))
                        if nsq >= min_squares:
                            results.append((a, b, c, nsq, ent))
        n += 1
    return results

def canon(ent):
    # canonical form under the 8 dihedral symmetries of the square
    g = list(ent)
    mats = []
    for r in range(4):
        mats.append(tuple(g))
        h = [g[0], g[3], g[6], g[1], g[4], g[7], g[2], g[5], g[8]]
        mats.append(tuple(h))
        g = [g[6], g[3], g[0], g[7], g[4], g[1], g[8], g[5], g[2]]
    return min(mats)

if __name__ == "__main__":
    import sys
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    res = search(B, min_squares=7)
    seen = {}
    for (a, b, c, nsq, ent) in res:
        k = canon(ent)
        if k not in seen or nsq > seen[k][3]:
            seen[k] = (a, b, c, nsq, ent)
    print("B =", B, "; square-center configs with >=7 square entries:", len(seen))
    for k, (a, b, c, nsq, ent) in sorted(seen.items(), key=lambda kv: -kv[1][3]):
        print("  a=%d b=%d c=%d nsq=%d" % (a, b, c, nsq))
        print("   entries:", ent)
        roots = []
        for e in ent:
            r = math.isqrt(e)
            roots.append(str(r) + "^2" if r * r == e else str(e) + "(ns)")
        print("   ", roots)