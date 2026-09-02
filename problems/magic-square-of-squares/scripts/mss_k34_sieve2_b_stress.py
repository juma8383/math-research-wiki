#!/usr/bin/env python
# B-side stress: the 5 survivor classes mod 264 vs all good primes p<=2e5
# with ord_p(G_B) | 264 (class-well-defined condition).
import sys, math
def out(*a): print(*a); sys.stdout.flush()
exec(open('mss_k34_sieve2_p5.py').read().split('def primes_upto')[0])

MB = 264
S = [0, 1, 2, 134, 262]
def primes_upto(B):
    sv=[True]*(B+1); sv[0]=sv[1]=False
    for i in range(2,int(B**0.5)+1):
        if sv[i]:
            for j in range(i*i,B+1,i): sv[j]=False
    return [i for i in range(2,B+1) if sv[i]]
bad=[]; nvalid=0
for p in primes_upto(200000):
    if p in (2,3) or singular(p): continue
    N = group_order_brute(p) if p<=20000 else bsgs_order(p)
    if N is None: continue
    fs=factorize(N); o=N
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G,o//q,p) is None: o//=q
            else: break
    if MB % o: continue
    nvalid += 1
    _,OK = allowed(p, p in (5,19,29))
    for c in S:
        if (c % o) not in OK:
            bad.append((p,c))
out("valid primes (ord|264) <= 2e5: %d ; violations: %s"%(nvalid, bad if bad else "NONE"))