#!/usr/bin/env python
# Claude verification part 2 for [mss-k34-sieve2]:
#  W1. Re-run the agent's own p3 driver (deterministic) -> must reproduce
#      M=42,078,090,600, S={0,2,M/2-1,-2,-1}.
#  W2. Stress the 5 survivor classes against VALID primes only
#      (ord_p(G) | M_A, good reduction), p <= 3e5 (their hunt bound) and
#      extension 3e5..1e6.
#  W3. B-side finishing (Fixed Fractions): killing sieve -> 5 classes mod 264.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()
sys.path.insert(0, r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
import os
os.chdir(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts")
exec(open('mss_k34_sieve2_p2.py').read().split('if __name__')[0])

def primes_upto(B):
    sieve = [True]*(B+1); sieve[0] = sieve[1] = False
    for i in range(2, int(B**0.5)+1):
        if sieve[i]:
            for j in range(i*i, B+1, i): sieve[j] = False
    return [i for i in range(2, B+1) if sieve[i]]

MA = 42078090600
t0 = time.time()

# ---------- W1: reproduce their driver ----------
out("=== W1: deterministic re-run of the agent's p3 driver ===")
M, S = 1, {0}
for p in [5, 11, 13]:
    N, OK = allowed(p, True)
    M, S = crt_merge(M, S, N, OK)
out("  after killing primes: %d classes mod %d" % (len(S), M))
CAP, PBIG, PHUNT = 300000, 400, 300000
pl = [p for p in primes_upto(PBIG) if p not in (2,3,5,11,13) and not singular(p)]
dens = [(len(allowed(p, False)[1]) / allowed(p, False)[0], p) for p in pl]
dens.sort()
grown = skipped = 0
for d, p in dens:
    N, OK = allowed(p, False)
    if len(S) * len(OK) // max(math.gcd(M, N), 1) > CAP:
        skipped += 1
        continue
    M, S = crt_merge(M, S, N, OK)
    grown += 1
out("  after grow: %d classes mod %d (merged %d, skipped %d) (%.0fs)"
    % (len(S), M, grown, skipped, time.time()-t0))
out("  modulus matches claim MA:", M == MA)
# hunt
sup = set(factorize(M))
found = 0
for p in primes_upto(PHUNT):
    if p <= PBIG or p in (2,3,5,11,13) or singular(p): continue
    N = group_order_brute(p) if p <= 20000 else bsgs_order(p)
    if N is None: continue
    fs = factorize(N); o = N
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G, o//q, p) is None: o //= q
            else: break
    if M % o: continue
    _, OK = allowed(p, False)
    M2, S2 = crt_merge(M, S, o, OK)
    if len(S2) < len(S):
        M, S = M2, S2
        found += 1
out("  hunt kills: %d -> %d classes mod %d (%.0fs)" % (found, len(S), M, time.time()-t0))
claimS = [0, 2, MA//2 - 1, MA - 2, MA - 1]
out("  survivors:", sorted(S))
out("  match claim {0,2,M/2-1,-2,-1}:", sorted(S) == sorted(claimS) and M == MA)
json.dump({"M": M, "S": sorted(S)}, open("mss_k34_sieve2_stateA.json", "w"))
out("  stateA.json rewritten with reproduced state")

# ---------- W2: stress survivors with VALID primes ----------
out("=== W2: stress 5 classes, valid primes (ord | M) only ===")
Sf = sorted(S)
def cond_val(n, p, kill):
    P = ec_mul(G, n, p)
    if P is None: return True
    X = Xq(P, p)
    if X is None: return True
    if kill: return X == 0 or X == 1
    return X == 0 or X in qr_set(p)
bad = []
nvalid = 0
for p in primes_upto(300000):
    if p in (2, 3) or singular(p): continue
    o = (group_order_brute(p) if p <= 20000 else bsgs_order(p))
    if o is None: continue
    fs = factorize(o); ov = o
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G, ov//q, p) is None: ov //= q
            else: break
    if MA % ov: continue
    nvalid += 1
    for c in Sf:
        if not cond_val(c % ov, p, p in (5, 11, 13)):
            bad.append((p, c, 'hunt-range'))
out("  valid primes <= 3e5: %d ; violations: %s" % (nvalid, bad if bad else "NONE"))
out("  (%.0fs)" % (time.time()-t0,))

out("=== W2b: extension 3e5..1e6 (their claim: hunt to 3e6 did not kill) ===")
bad2 = []
cnt = 0
for p in primes_upto(1000000):
    if p <= 300000 or p in (2, 3) or singular(p): continue
    o = bsgs_order(p)
    if o is None: continue
    fs = factorize(o); ov = o
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G, ov//q, p) is None: ov //= q
            else: break
    if MA % ov: continue
    cnt += 1
    for c in (0, 2, MA//2 - 1, MA - 2, MA - 1):
        if not cond_val(c % ov, p, False):
            bad2.append((p, c))
out("  valid primes 3e5..1e6: %d ; violations: %s" % (cnt, bad2 if bad2 else "NONE"))
out("  (%.0fs)" % (time.time()-t0,))