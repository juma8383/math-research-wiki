# D-set additive-pattern census.
#
# Motivation (corrected Lemma 3, notes.md): a full 9-square solution with
# square center a=w^2 needs ALL FOUR role quantities b, c, b+c, b-c in
# D(w^2) = {2uv : u^2+v^2=w^2, u>v>0} -- an "additive parallelogram"
# {x, y, x+y, y-x} inside D.  The >=7-square (Bremner) tier needs only
# 2 complete pairs = 2 D-elements with NO additive condition.  So the
# genuine control step for the full problem is: do D-sets contain
# additive structure at all?
#
# This script censuses, for all w <= W:
#   A2  : exists x<y in D(w^2) with x+y in D(w^2)          (additive triple)
#   A3  : exists x<y in D(w^2) with x+y AND y-x in D(w^2)  (parallelogram;
#         necessary for nsq=9 with square center)
# and reports counts, smallest examples, and |D|-tier statistics.
#
# Pure D-set structure: no entry box, no squareness test -- the roles
# being in D makes all 8 non-center entries squares automatically.
# Reuses the validated builder from mss_census_chunked.py verbatim.

import sys
from mss_census_chunked import build_primitive_triples, block_D


def main():
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    blockw = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
    print("D-set additive-pattern census: W=%d (centers <= %d)"
          % (W, W * W), flush=True)

    print("building primitive-triple table...", flush=True)
    w0s, d0s = build_primitive_triples(W)
    print("primitive triples with hypotenuse <= W: %d" % len(w0s), flush=True)

    n_w = 0            # w with |D| >= 3 (A2 needs 3 distinct elements)
    n_w4 = 0           # w with |D| >= 4 (A3 needs 4)
    n_a2 = 0           # w with an additive triple
    n_a3 = 0           # w with a parallelogram
    first_a2 = []
    first_a3 = []
    mod24_bad = 0

    for lo in range(2, W + 1, blockw):
        hi = min(W, lo + blockw - 1)
        D = block_D(w0s, d0s, lo, hi, None, 0)
        for key, dl in D.items():
            w = lo + key
            if len(dl) < 3:
                continue
            n_w += 1
            if len(dl) >= 4:
                n_w4 += 1
            Dset = set(dl)
            for d in dl:
                if d % 24:
                    mod24_bad += 1
            xs = sorted(Dset)
            found2 = found3 = False
            for i in range(len(xs)):
                x = xs[i]
                for j in range(i + 1, len(xs)):
                    y = xs[j]
                    s = x + y
                    m = y - x
                    if s in Dset:
                        found2 = True
                        if len(first_a2) < 10:
                            first_a2.append((w, x, y, s, m in Dset))
                    if s in Dset and m in Dset:
                        found3 = True
                        if len(first_a3) < 10:
                            first_a3.append((w, x, y, s, m))
            if found2:
                n_a2 += 1
            if found3:
                n_a3 += 1
                print("  *** PARALLELOGRAM (A3): w=%d D=%s  example x=%d "
                      "y=%d x+y=%d y-x=%d" % (w, xs, *first_a3[-1][1:]),
                      flush=True)

    print("w with |D|>=3: %d ; |D|>=4: %d" % (n_w, n_w4), flush=True)
    print("w with additive triple (A2): %d" % n_a2, flush=True)
    for w, x, y, s, has_m in first_a2:
        print("   A2 w=%d  %d + %d = %d   (y-x=%d in D: %s)"
              % (w, x, y, s, y - x, has_m), flush=True)
    print("w with parallelogram (A3): %d" % n_a3, flush=True)
    for w, x, y, s, m in first_a3:
        print("   A3 w=%d  x=%d y=%d x+y=%d y-x=%d" % (w, x, y, s, m),
              flush=True)
    print("d not divisible by 24 (Lemma 4 check): %d" % mod24_bad, flush=True)
    if n_a3 == 0:
        print("=> NO D-set additive parallelogram with center <= %d"
              % (W * W), flush=True)
        print("   (necessary condition for a full 9-square solution with"
              " square center is NEVER met in this range)", flush=True)


if __name__ == "__main__":
    main()