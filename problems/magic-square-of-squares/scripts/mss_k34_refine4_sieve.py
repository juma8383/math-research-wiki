#!/usr/bin/env python
# K34 refine4 part 2: depth-parity sieve on the nonzero coset classes.
#
# Kill condition (Lemma 2 + depth decomposition): if q is a good prime with
# d = ord_q(G) | n and q does not divide n, then v_q(X(nG)) = depth_q(nG)
# = b_d + v_q(n) - v_q(d), and X(nG) = w^2 needs this EVEN.  So n is killed
# by q iff  d | n  and  (b_d + v_q(d)) is odd  and  q does not divide n.
#
# For n = k*M + c (M = M_A resp M_B, c a nonzero survivor class):
#   d | n  <=>  k = k0 mod D,  D = d/g,  g = gcd(d, M)   (needs g | c)
#   q | n  <=>  k = e mod q   (if q does not divide M; if q | M then
#                                q | n iff q | c -> skip q entirely)
# Killed k = kill progression minus exclusion progression (per q, exact).
#
# Class 0 is NOT sieved here: valid primes there force k-divisibility
# (class-0 constraint theorem, notes.md 2f/2g), no kill.
import sys, json, math, time
def out(*a): print(*a); sys.stdout.flush()

def sieve(tag, M, classes, rows, K):
    out("=== %s: %d primes, M=%d, K=%d ===" % (tag, len(rows), M, K))
    killers = [(p, o, vd, b) for (p, o, vd, b) in rows if (b + vd) % 2 == 1]
    out("  killer primes (b_d + v_q(d) odd): %d of %d" % (len(killers), len(rows)))
    for c in classes:
        t0 = time.time()
        killed = bytearray(K + 1)
        nkill = 0
        for (p, o, vd, b) in killers:
            g = math.gcd(o, M)
            if c % g: continue
            D = o // g
            # k*M + c = 0 mod o  =>  (M/g) k = -c/g mod D;  gcd(M/g, D) = 1
            k0 = ((-c // g) * pow(M // g % D, -1, D)) % D
            # exclusion: q | n  <=>  k*M = -c mod q  (only if q does not
            # divide M; if q | M then q | n iff q | c -> no q-kill at all)
            excl = None
            if M % p == 0:
                if c % p == 0: continue
            else:
                e = (-c * pow(M % p, -1, p)) % p
                gg = math.gcd(D, p)
                if (k0 - e) % gg == 0:
                    step = p // gg
                    t = ((e - k0) // gg * pow(D // gg, -1, step)) % step if step > 1 else 0
                    excl = (k0 + D * t) % (D * step)
            if D == 1 and excl is None:
                out("  class c=%d: FULLY KILLED by q=%d (D=1, no exclusion)" % (c, p))
                killed = bytearray([1]) * (K + 1)
                nkill = K + 1
                break
            # mark kill progression, skipping exclusion sub-progression
            if excl is None:
                for k in range(k0 % D, K + 1, D):
                    if not killed[k]:
                        killed[k] = 1; nkill += 1
            else:
                L = D * (p // math.gcd(D, p))
                for k in range(k0 % D, K + 1, D):
                    if (k - excl) % L and not killed[k]:
                        killed[k] = 1; nkill += 1
        surv = [k for k in range(K + 1) if not killed[k]]
        out("  class c=%d: killed %d of %d, %d survivors (%.0fs)"
            % (c, nkill, K + 1, len(surv), time.time() - t0))
        out("    smallest survivors (k): %s" % surv[:15])
        if 0 < len(surv) <= 15:
            out("    corresponding n = k*M+c: %s" % [k * M + c for k in surv])
    return

def brute_check(M, classes, rows, K):
    """Direct per-k kill check (no progression arithmetic): validate sieve."""
    killers = [(p, o, vd, b) for (p, o, vd, b) in rows if (b + vd) % 2 == 1]
    bad = 0
    for c in classes:
        killed = bytearray(K + 1)
        for (p, o, vd, b) in killers:
            g = math.gcd(o, M)
            if c % g: continue
            D = o // g
            k0 = ((-c // g) * pow(M // g % D, -1, D)) % D
            for k in range(k0 % D, K + 1, D):
                n = k * M + c
                if n % p:                       # q does not divide n
                    killed[k] = 1
        surv = set(k for k in range(K + 1) if not killed[k])
        # compare against sieve("...") survivor sets via re-run below
        out("  brute c=%d: %d survivors" % (c, len(surv)))
        yield c, surv

if __name__ == "__main__":
    K = 200000
    sc = r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts"
    rowsA = json.load(open(sc + r"\parityA.json"))["rows"]
    MA = 42078090600
    # --- validation: curve B, primes <= 20000, K = 3000, brute vs sieve ---
    rowsB = json.load(open(sc + r"\parityB.json"))["rows"]
    rowsBk = [r for r in rowsB if r[0] <= 20000]
    KB = 3000
    out("=== validation (B, q<=20000, K=%d): sieve vs brute ===" % KB)
    # k0 correctness spot-check: k0 must satisfy d | k0*M + c
    spot = 0
    for (p, o, vd, b) in rowsBk:
        if (b + vd) % 2 == 0: continue
        for c in [1, 2, 134, 262]:
            g = math.gcd(o, 264)
            if c % g: continue
            D = o // g
            k0 = ((-c // g) * pow(264 // g % D, -1, D)) % D
            assert (k0 * 264 + c) % o == 0, (p, c, o, k0)
            spot += 1
    out("  k0 spot-checks passed: %d" % spot)
    surv_sieve = {}
    for c in [1, 2, 134, 262]:
        killed = bytearray(KB + 1)
        for (p, o, vd, b) in rowsBk:
            if (b + vd) % 2 == 0: continue
            g = math.gcd(o, 264)
            if c % g: continue
            D = o // g
            k0 = ((-c // g) * pow(264 // g % D, -1, D)) % D
            excl = None
            if 264 % p == 0:
                if c % p == 0: continue
            else:
                e = (-c * pow(264 % p, -1, p)) % p
                gg = math.gcd(D, p)
                if (k0 - e) % gg == 0:
                    step = p // gg
                    t = ((e - k0) // gg * pow(D // gg, -1, step)) % step if step > 1 else 0
                    excl = (k0 + D * t) % (D * step)
            if excl is None:
                for k in range(k0 % D, KB + 1, D):
                    killed[k] = 1
            else:
                L = D * step
                for k in range(k0 % D, KB + 1, D):
                    if (k - excl) % L: killed[k] = 1
        surv_sieve[c] = set(k for k in range(KB + 1) if not killed[k])
    for c, sb in brute_check(264, [1, 2, 134, 262], rowsBk, KB):
        ss = surv_sieve[c]
        ok = (ss == sb)
        out("  validate c=%d: sieve %d survivors, brute %d, match %s"
            % (c, len(ss), len(sb), ok))
        if not ok:
            out("    diff: %s" % sorted(ss ^ sb)[:10])
    # --- main sieves ---
    sieve("A", MA, [2, MA // 2 - 1, -2 % MA, -1 % MA], rowsA, K)
    sieve("B", 264, [1, 2, 134, 262], rowsB, K)