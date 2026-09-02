#!/usr/bin/env python
# K34 round 2, part 3: full sieve driver for E~_A (t=0 coset; t=1 by flip).
# Strategy: alternate
#   GROW: ordinary primes p<=PBIG ordered by |OK|/ord; merge while count<=CAP
#   SHRINK: primes with ord_p(G) | M (support check) -> count *= |OK|/ord ~1/2
# Report final survivors, modulus, density; verify survivors are the
# degenerate floor classes {0,+-2,-1} mod M.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()
exec(open('mss_k34_sieve2_p2.py').read().split('if __name__')[0])

CAP = int(sys.argv[1]) if len(sys.argv)>1 else 300000
PBIG = int(sys.argv[2]) if len(sys.argv)>2 else 400
PHUNT = int(sys.argv[3]) if len(sys.argv)>3 else 200000

t0=time.time()
def primes_upto(B):
    sieve=[True]*(B+1); sieve[0]=sieve[1]=False
    for i in range(2,int(B**0.5)+1):
        if sieve[i]:
            for j in range(i*i,B+1,i): sieve[j]=False
    return [i for i in range(2,B+1) if sieve[i]]

M,S=1,{0}
# phase A: killing primes
for p in [5,11,13]:
    N,OK=allowed(p,True)
    M,S=crt_merge(M,S,N,OK)
    out("kill p=%2d ord=%3d |OK|=%2d -> %d mod %d"%(p,N,len(OK),len(S),M))

support=set(factorize(M).keys())
out("initial support:",sorted(support))

# phase B: grow with ordinary primes
pl=[p for p in primes_upto(PBIG) if p not in (2,3,5,11,13) and not singular(p)]
dens=[(len(allowed(p,False)[1])/allowed(p,False)[0], p) for p in pl]
dens.sort()
for d,p in dens:
    N,OK=allowed(p,False)
    if len(S)*len(OK)//max(math.gcd(M,N),1) > CAP:
        continue
    M,S=crt_merge(M,S,N,OK)
    out("grow p=%3d ord=%4d |OK|=%4d -> %d mod %d (dens %.2e)"%(p,N,len(OK),len(S),M,len(S)/M))
out("after grow: %d classes mod %d, support %s (%.1fs)"%(len(S),M,sorted(factorize(M)),time.time()-t0))

# phase C: smooth-ord hunt
def hunt(lo,hi):
    global M,S
    sup=set(factorize(M))
    found=0
    for p in primes_upto(hi):
        if p<=lo: continue
        if p in (2,3,5,11,13) or singular(p): continue
        N=group_order_brute(p) if p<=20000 else bsgs_order(p)
        if N is None: continue
        fs=factorize(N)
        o=N
        for q in fs:
            for _ in range(fs[q]):
                if ec_mul(G,o//q,p) is None: o//=q
                else: break
        if M % o: continue
        _,OK=allowed(p,False)
        M2,S2=crt_merge(M,S,o,OK)
        if len(S2)<len(S):
            M,S=M2,S2
            found+=1
            out("hunt p=%6d ord=%6d |OK|=%5d -> %d mod %d (%.1fs)"%(p,o,len(OK),len(S),M,time.time()-t0))
            if len(S)<=4: break
    return found

f=hunt(PBIG,PHUNT)
out("hunt found %d shrinking primes; now %d classes mod %d"%(f,len(S),M))
json.dump({"M":M,"S":sorted(S),"curve":"A","coset":"t=0"},open("mss_k34_sieve2_stateA.json","w"))
out("FINAL A: survivors=%d mod M=%d, density %.3e"%(len(S),M,len(S)/M))
out("survivors (first 40):",sorted(S)[:40])
out("floor classes 0,2,-2,-1 in S: %s"%str(tuple(((c%M) in S) for c in (0,2,-2,-1))))
out("elapsed %.1fs"%(time.time()-t0))