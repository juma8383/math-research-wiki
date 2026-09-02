#!/usr/bin/env python
# K34 round 2, part 4: continue hunt from saved state; try to kill extra class.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()
exec(open('mss_k34_sieve2_p2.py').read().split('if __name__')[0])

st=json.load(open("mss_k34_sieve2_stateA.json")); M,S=st["M"],set(st["S"])
HI=int(sys.argv[1]) if len(sys.argv)>1 else 2000000
out("start: %d classes mod %d: %s"%(len(S),M,sorted(S)))

def primes_upto(B):
    sieve=[True]*(B+1); sieve[0]=sieve[1]=False
    for i in range(2,int(B**0.5)+1):
        if sieve[i]:
            for j in range(i*i,B+1,i): sieve[j]=False
    return [i for i in range(2,B+1) if sieve[i]]

t0=time.time()
cand=0
for p in primes_upto(HI):
    if p<=200000: continue
    if singular(p): continue
    N=bsgs_order(p)
    if N is None: continue
    fs=factorize(N); o=N
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G,o//q,p) is None: o//=q
            else: break
    if M%o: continue
    cand+=1
    _,OK=allowed(p,False)
    M2,S2=crt_merge(M,S,o,OK)
    if len(S2)<len(S):
        M,S=M2,S2
        out("kill p=%7d ord=%7d |OK|=%6d -> %d classes mod %d (%.0fs)"%(p,o,len(OK),len(S),M,time.time()-t0))
        json.dump({"M":M,"S":sorted(S),"curve":"A","coset":"t=0"},open("mss_k34_sieve2_stateA.json","w"))
        if len(S)<=4: break
out("done: %d classes mod %d, %d M-smooth candidates tried (%.0fs)"%(len(S),M,cand,time.time()-t0))
out("survivors:",sorted(S))
for c in (0,2,-2,-1):
    out("  floor %d present: %s"%(c,(c%M) in S))