# D-set 3-term-AP census.
#
# Sibling question to the A2/A3 census (mss_d_additive_patterns.py): the
# hourglass asks whether D(w^2) contains an ADDITIVE TRIPLE {x, y, x+y}.
# The natural next pattern is a 3-term ARITHMETIC PROGRESSION
# {x, y, z} in D(w^2) (x+z = 2y) -- a different additive relation, with
# the same order of expected rarity under the Euler-product model
# (expected APs over the plane ~ H ~ 1).  For the cubic sibling the
# answer is trivially "AP-free" (D is empty -- see square-of-cubes
# `[cubic-dset-vanishes]`), so this asks whether the square D-sets are
# AP-free too in the searched range.
#
# Reuses the validated builder from mss_census_chunked.py verbatim.

import sys
from mss_census_chunked import build_primitive_triples, block_D


def main():
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    blockw = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
    print("D-set 3-term-AP census: W=%d (centers <= %d)" % (W, W * W),
          flush=True)

    print("building primitive-triple table...", flush=True)
    w0s, d0s = build_primitive_triples(W)
    print("primitive triples with hypotenuse <= W: %d" % len(w0s), flush=True)

    n_w = 0            # w with |D| >= 3 (an AP needs 3 elements)
    n_ap = 0
    first_ap = []

    for lo in range(2, W + 1, blockw):
        hi = min(W, lo + blockw - 1)
        D = block_D(w0s, d0s, lo, hi, None, 0)
        for key, dl in D.items():
            w = lo + key
            if len(dl) < 3:
                continue
            n_w += 1
            Dset = set(dl)
            xs = sorted(Dset)
            found = False
            for i in range(len(xs)):
                x = xs[i]
                for j in range(i + 1, len(xs)):
                    z = xs[j]
                    s = x + z
                    if s % 2:
                        continue
                    m = s // 2                    # the middle term
                    if m in Dset and m != x:
                        found = True
                        n_ap += 1
                        if len(first_ap) < 10:
                            first_ap.append((w, x, m, z))
            if found:
                print("  *** 3-AP: w=%d  %d, %d, %d in D"
                      % (first_ap[-1][0], *first_ap[-1][1:]), flush=True)

    print("w with |D|>=3: %d" % n_w, flush=True)
    print("w with a 3-term AP in D(w^2): %d" % n_ap, flush=True)
    for w, x, m, z in first_ap:
        print("   AP w=%d  %d, %d, %d" % (w, x, m, z), flush=True)
    if n_ap == 0:
        print("=> D-sets are 3-AP-free for all w <= %d (centers <= %d)"
              % (W, W * W), flush=True)


if __name__ == "__main__":
    main()