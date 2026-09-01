# Grimm census probe (2026-08-31 hunt scan; adversarially verified, novelty KILLED).
# Census of k-smooth composite runs below N=2,000,000 with Hall
# (bipartite Kuhn) matching test. Correctly-attributed reproduction of the
# known k-smooth reduction: J. van Delden, primepuzzles.net/puzzles/puzz_430.htm
# (to 1e8; Rivera to 1e9; T. D. Noe bipartite matching). The Laishram-Shorey
# 2006 (IJNT 2(2) 207-211) Hall proof covers n <= 1.92e10, i.e. this entire
# range, so a counterexample/near-miss is impossible here by theorem; kept only
# as a reproduction. Expected output: runs=148931, matching failures=0, smooth=11409.

import math, sys
N = 2_000_000
# smallest prime factor sieve
spf = list(range(N+1))
for p in range(2, int(N**0.5)+1):
    if spf[p] == p:
        for k in range(p*p, N+1, p):
            if spf[k] == k:
                spf[k] = p
# primes list
primes = [i for i in range(2, N+1) if spf[i] == i]
# collect runs of consecutive composites: between consecutive primes p, q, run = p+1..q-1, n = q-p-1
def factors(x):
    fs = set()
    while x > 1:
        f = spf[x]
        fs.add(f)
        while x % f == 0:
            x //= f
    return fs

def matching_ok(ns, fs_list):
    # bipartite matching, augmenting paths
    match = {}
    def try_k(i, seen):
        for f in fs_list[i]:
            if f not in seen:
                seen.add(f)
                if f not in match or try_k(match[f], seen):
                    match[f] = i
                    return True
        return False
    for i in range(len(ns)):
        if not try_k(i, set()):
            return False, i
    return True, None

smooth_pos_count = 0
fail_runs = []
first_smooth = []
checked = 0
total_smooth_positions = 0
for idx in range(len(primes)-1):
    p, q = primes[idx], primes[idx+1]
    n = q - p - 1
    if n < 1:
        continue
    run = list(range(p+1, q))
    fs_list = [factors(x) for x in run]
    # count positions with no prime factor > n (n-smooth composites)
    smooth_here = sum(1 for fs in fs_list if max(fs) <= n)
    total_smooth_positions += smooth_here
    if smooth_here and len(first_smooth) < 8:
        first_smooth.append((p, n, [(x, sorted(factors(x))) for x in run if max(factors(x)) <= n]))
    checked += 1
    ok, bad = matching_ok(run, fs_list)
    if not ok:
        fail_runs.append((p, n, bad))
print("runs checked:", checked)
print("runs where matching FAILS:", len(fail_runs), fail_runs[:5])
print("total positions that are n-smooth (no prime factor > n):", total_smooth_positions)
print("first runs containing an n-smooth position:")
for p, n, det in first_smooth:
    print("  after prime", p, "run length", n, "-> smooth positions:", det)
