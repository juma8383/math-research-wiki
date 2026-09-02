#!/usr/bin/env python
# K34 round 2, part 7: A-side, attempt to kill the extra survivor class
# (n ~ -1 mod M/2, n ~ 3 mod 8) via modulus-GROWING primes 400..3000,
# then another M-smooth hunt.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()
exec(open('mss_k34_sieve2_p2.py').read().split('if __name__')[0])

st=json.load(open("mss_k34_sieve2_stateA.json")); M,S=st["M"],set(st["S"])
out("start: %d classes mod %d"%(len(S),M))
def primes_upto(B):
    sv=[True]*(B+1); sv[0]=sv[1]=False
    for i in range(2,int(B**0.5)+1):
        if sv[i]:
            for j in range(i*i,B+1,i): sv[j]=False
    return [i for i in range(2,B+1) if sv[i]]
t0=time.time()
# grow pass: allow count up to 3e5
for p in primes_upto(3000):
    if p<=400 or p in (2,3,5,11,13) or singular(p): continue
    N,OK=allowed(p,False)
    g=math.gcd(M,N)
    if len(S)*len(OK)//max(g,1) > 300000: continue
    M2,S2=crt_merge(M,S,N,OK)
    if len(S2)<len(S):
        M,S=M2,S2
        out("grow2 p=%5d ord=%6d -> %d classes mod %d (%.0fs)"%(p,N,len(S),M,time.time()-t0))
        json.dump({"M":M,"S":sorted(S),"curve":"A","coset":"t=0"},open("mss_k34_sieve2_stateA.json","w"))
        if len(S)<=4: break
out("after grow2: %d classes mod %d (%.0fs)"%(len(S),M,time.time()-t0))
if len(S)>4:
    # second smooth hunt up to 1e6
    for p in primes_upto(1000000):
        if p<=200000 or p in (2,3,5,11,13) or singular(p): continue
        N=bsgs_order(p)
        if N is None: continue
        fs=factorize(N); o=N
        for q in fs:
            for _ in range(fs[q]):
                if ec_mul(G,o//q,p) is None: o//=q
                else: break
        if M%o: continue
        _,OK=allowed(p,False)
        M2,S2=crt_merge(M,S,o,OK)
        if len(S2)<len(S):
            M,S=M2,S2
            out("hunt2 p=%7d ord=%7d -> %d classes mod %d (%.0fs)"%(p,o,len(S),M,time.time()-t0))
            json.dump({"M":M,"S":sorted(S),"curve":"A","coset":"t=0"},open("mss_k34_sieve2_stateA.json","w"))
            if len(S)<=4: break
json.dump({"M":M,"S":sorted(S),"curve":"A","coset":"t=0"},open("mss_k34_sieve2_stateA.json","w"))
out("FINAL: %d classes mod %d: %s"%(len(S),M,sorted(S)))
out("elapsed %.0fs"%(time.time()-t0))