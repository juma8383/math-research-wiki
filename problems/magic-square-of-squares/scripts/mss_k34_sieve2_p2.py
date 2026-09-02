#!/usr/bin/env python
# K34 round 2, part 2: deepened Mordell-Weil sieve on E~_A (square-X cond).
# Corrections/findings vs round 1 (p9/p10):
#  (i)  p=3 is VACUOUS as a killing prime: C3_A mod 3 is W^2=(x^4+1)^2, all x
#       solvable; and E~_A is SINGULAR mod 3 (T=(0,0) singular).  Excluded.
#  (ii) the t=1 coset is the exact flip of t=0: flip(n,t)=(-2-n,1-t) on E~_A
#       (C=-2G+T, verified on rational points); reduced-point evaluation of X
#       at the pole classes (n=+-2 mod ord: points (4,+-264)) is 0/0, so sieve
#       t=0 only and obtain t=1 by the exact flip.
#  (iii) count-shrinking primes: ord_p(G) | M  =>  count *= |OK|/ord ~ 1/2 at
#       zero modulus cost.  Hunt via BSGS order + support check.
#  (iv) sieve floor (t=0): classes 0 (O, X=0), +2/-2 (2G/-2G, X=pole=inf),
#       -1 (-G, X=1): degenerate points, protected at every prime.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()

A, B2 = -256, 18432
G = (128, 512); T = (0, 0)

def ec_add(P,Q,p):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0: return None
    if P==Q:
        if y1%p==0: return None
        lam=(3*x1*x1+2*A*x1+B2)*pow(2*y1%p,p-2,p)%p
    else:
        lam=(y2-y1)*pow((x2-x1)%p,p-2,p)%p
    x3=(lam*lam-A-x1-x2)%p
    return (x3,(lam*(x1-x3)-y1)%p)

def ec_mul(P,n,p):
    if n<0: return ec_mul((P[0],(-P[1])%p),-n,p)
    R=None; Q=P
    while n:
        if n&1: R=ec_add(R,Q,p)
        Q=ec_add(Q,Q,p); n>>=1
    return R

def singular(p):
    for x in range(p):
        if (x*x*x+A*x*x+B2*x)%p==0 and (3*x*x+2*A*x+B2)%p==0: return True
    return False

def group_order_brute(p):
    n=1
    for x in range(p):
        v=(x*x*x+A*x*x+B2*x)%p
        if v==0: n+=1
        elif pow(v,(p-1)//2,p)==1: n+=2
    return n

def bsgs_order(p):
    lo=p+1-int(2*math.isqrt(p))-2; hi=p+1+int(2*math.isqrt(p))+3
    m=math.isqrt(hi-lo)+1
    baby={}; P=None
    for j in range(m):
        if P is not None: baby[P]=j
        P=G if j==0 else ec_add(P,G,p)
    mG=ec_mul(G,m,p); Q=ec_mul(G,lo,p)
    for i in range((hi-lo)//m+2):
        if Q in baby:
            N=lo+i*m-baby[Q]
            if N>0: return N
        Q=ec_add(Q,mG,p)
    return None

def factorize(n):
    fs={}; d=2
    while d*d<=n and d<=200000:
        while n%d==0: fs[d]=fs.get(d,0)+1; n//=d
        d += 1 if d==2 else 2
    if n>1: fs[n]=fs.get(n,0)+1
    return fs

def ord_of_G(p):
    N = group_order_brute(p) if p<=20000 else bsgs_order(p)
    o=N
    for q in factorize(o):
        for _ in range(factorize(o)[q]): pass
    fs=factorize(N)
    o=N
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G,o//q,p) is None: o//=q
            else: break
    return o

def qr_set(p): return {i*i%p for i in range(p)}

def Xq(P,p):
    x,y=P
    if x%p==0 or x%p==4%p: return None
    return 2*(y+66*x)*pow(x*(x-4)%p,p-2,p)%p

def allowed(p,kill):
    """(ord_p(G), OK set of n mod ord) for t=0 coset; pole classes (x=0,4) and
    O are unconstrained (sound escapes)."""
    N=ord_of_G(p); QRS=qr_set(p)
    OK=set(); P=None
    for n in range(N):
        if n==1: P=G
        elif n>1: P=ec_add(P,G,p)
        if P is None: OK.add(n); continue
        X=Xq(P,p)
        if X is None: OK.add(n); continue
        if kill:
            if X==0 or X==1: OK.add(n)
        else:
            if X==0 or X in QRS: OK.add(n)
    return N,OK

def crt_merge(M,S,N,OK):
    g=math.gcd(M,N); M2=M*N//g
    mg,ng=M//g,N//g
    inv=pow(mg%ng,-1,ng) if ng>1 else 0
    OKg={}
    for n in OK: OKg.setdefault(n%g,[]).append(n)
    S2=set()
    for c in S:
        for n in OKg.get(c%g,()):
            k=((n-c)//g%ng)*inv%ng if ng>1 else 0
            S2.add((c+M*k)%M2)
    return M2,S2

def killing_primes_check(PMAX=300):
    """brute force: primes p where C3_A solvable x-classes = {0,1,2} only"""
    res=[]
    for p in range(5,PMAX):
        if singular_p_c3(p): continue
        sol=set()
        for x in range(p):
            v=(pow(x,8,p)+132*pow(x,6,p)-250*pow(x,4,p)+132*x*x+1)%p
            if v==0 or pow(v,(p-1)//2,p)==1: sol.add(x)
        if sol<= {0,1,p-1}: res.append(p)
    return res

def singular_p_c3(p):
    # crude: skip; C3_A is a smooth curve mod p for most p; not needed
    return False

if __name__=="__main__":
    t0=time.time()
    out("== killing prime re-verification (C3_A solvable classes) ==")
    KP=killing_primes_check(300)
    out("primes with only x in {0,+-1} solvable:",KP)
    out("== phase 1: killing primes {5,11,13} + ordinary primes (count-shrinking only) ==")
    M,S=1,{0}
    log=[]
    for p in [5,11,13]:
        N,OK=allowed(p,True)
        M,S=crt_merge(M,S,N,OK)
        out("kill p=%2d ord=%3d |OK|=%2d -> %d classes mod %d"%(p,N,len(OK),len(S),M))
        log.append((p,N,len(OK),len(S),M))
    # ordinary primes <= 400: add only if count shrinks
    for p in range(7,400,2):
        if p in (3,5,11,13) or singular(p): continue
        N,OK=allowed(p,False)
        # expected new count
        g=math.gcd(M,N)
        exp=len(S)*len(OK)//max(g,1)
        if exp>=len(S)*2: continue
        M2,S2=crt_merge(M,S,N,OK)
        if len(S2)<len(S):
            M,S=M2,S2
            log.append((p,N,len(OK),len(S),M))
    out("after ordinary phase: %d classes mod %d (density %.3e)"%(len(S),M,len(S)/M))
    json.dump({"M":M,"S":sorted(S)},open("mss_k34_sieve2_stateA.json","w"))
    out("state saved; elapsed %.1fs"%(time.time()-t0))