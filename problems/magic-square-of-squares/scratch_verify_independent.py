# Independent adversarial re-check of scratch_mss_prototype.py.
# DIFFERENT architecture: build 3-term APs of squares by scanning the square
# list directly (no u^2+v^2=n^2 parametrization); for each center collect all
# pair-differences D; then for every 3-subset of D assign values+signs to 3 of
# the 4 roles {b, c, b+c, b-c}, solve for (b,c), and verify magicness and
# square-count on the final entries (never trusting the construction).
import math, sys

B = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
MINQ = int(sys.argv[2]) if len(sys.argv) > 2 else 7

sqs = [i * i for i in range(1, math.isqrt(2 * B) + 1) if i * i <= 2 * B]
sqset = set(sqs)

def is_sq(n):
    return n >= 1 and math.isqrt(n) ** 2 == n

ROLES = ('b', 'c', 's', 't')  # b, c, b+c, b-c

def entries(a, b, c):
    return (a + b, a - b - c, a + c, a - b + c, a, a + b - c,
            a - c, a + b + c, a - b)

def is_magic(ent):
    s = ent[4] * 3
    return (ent[0] + ent[1] + ent[2] == s and ent[3] + ent[4] + ent[5] == s
            and ent[6] + ent[7] + ent[8] == s and ent[0] + ent[3] + ent[6] == s
            and ent[1] + ent[4] + ent[7] == s and ent[2] + ent[5] + ent[8] == s
            and ent[0] + ent[4] + ent[8] == s and ent[2] + ent[4] + ent[6] == s)

def canon(ent):
    g = list(ent); best = None
    for _ in range(4):
        t = tuple(g)
        best = t if best is None or t < best else best
        h = (g[0], g[3], g[6], g[1], g[4], g[7], g[2], g[5], g[8])
        best = min(best, tuple(h))
        g = [g[6], g[3], g[0], g[7], g[4], g[1], g[8], g[5], g[2]]
    return best

results = {}
ndegenerate = 0
for a in sqs:
    if a > B:
        break
    # all d with a-d, a+d both positive squares (scan squares directly)
    D = []
    for s in sqs:
        if s >= 2 * a:
            break
        t = 2 * a - s
        if t in sqset and s != a:
            d = abs(s - a)
            if d > 0:
                D.append(d)
    D = sorted(set(D))
    if len(D) < 3:
        continue
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            for k in range(j + 1, len(D)):
                trip = (D[i], D[j], D[k])
                for omit in range(4):
                    others = [r for r in range(4) if r != omit]
                    for perm in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
                        for signs in range(8):
                            sg = [(signs >> m) & 1 and -1 or 1 for m in range(3)]
                            val = {others[m]: sg[m] * trip[perm[m]] for m in range(3)}
                            # roles: b, c, s=b+c, t=b-c
                            if omit == 0:      # b unknown; know c, b+c
                                c = val[1]; b = val[2] - c
                            elif omit == 1:    # c unknown
                                b = val[0]; c = val[2] - b
                            elif omit == 2:    # b+c unknown
                                b = val[0]; c = val[1]
                            else:              # b-c unknown
                                b = val[0]; c = val[1]
                            if b == 0 or c == 0:
                                continue
                            ent = entries(a, b, c)
                            if any(e < 1 or e > B for e in ent):
                                continue
                            if not is_magic(ent):
                                print("MAGIC FAIL", a, b, c); sys.exit(1)
                            nlen = len(set(ent))
                            if nlen < 9:
                                ndegenerate += 1
                                continue
                            nsq = sum(1 for e in ent if is_sq(e))
                            if nsq >= MINQ:
                                key = canon(ent)
                                if key not in results or nsq > results[key][1]:
                                    results[key] = ((a, b, c), nsq, ent)

print("B=%d  independent distinct-entry square-center >=%d-square census: %d canonical classes"
      % (B, MINQ, len(results)))
for key, ((a, b, c), nsq, ent) in sorted(results.items(), key=lambda kv: -kv[1][1]):
    print("  a=%d b=%d c=%d nsq=%d" % (a, b, c, nsq))
    print("    roots:", ["%d^2" % math.isqrt(e) if is_sq(e) else str(e) for e in ent])
print("degenerate (repeated-entry) configs skipped:", ndegenerate)