#!/usr/bin/env python
# K34 round 2, part 5: B-side. E~_B: y^2=x^3+256x^2-2048x (E_B shifted by 18),
# G=(-128,1536), T=(0,0); inverse quartic X = (6y-92x)/(x(x-36)); poles x=0,36.
# Verified: X(G)=1 (table (1,12)->G_B), X(-G)=5/41 ((5/41)->-G_B),
#           X(2G)=(36,-552) pole ((0,3)->2G_B+T_B is the C point), 2G_B=(36,-552).
# Floor t=0: {0 (O), 1 (G, X=1), +2/-2 (2G/-2G, pole)}; -1 (X=5/41 nsq) dies.
import sys, math, json, time
def out(*a): print(*a); sys.stdout.flush()

A,B2 = 256, -2048
G=(-128,1536); T=(0,0)
exec(open('mss_k34_sieve2_p2.py').read().split('A, B2 =')[0].split('import sys')[1].split('def out')[1].split('\n',1)[1]) if False else None

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
def factorize(n):
    fs={}; d=2
    while d*d<=n and d<=200000:
        while n%d==0: fs[d]=fs.get(d,0)+1; n//=d
        d += 1 if d==2 else 2
    if n>1: fs[n]=fs.get(n,0)+1
    return fs
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
def ord_of_G(p):
    N = group_order_brute(p) if p<=20000 else bsgs_order(p)
    if N is None: return None
    fs=factorize(N); o=N
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G,o//q,p) is None: o//=q
            else: break
    return o
def qr_set(p): return {i*i%p for i in range(p)}
def Xq(P,p):
    x,y=P
    if x%p==0 or x%p==36%p: return None
    return (6*y-92*x)*pow(x*(x-36)%p,p-2,p)%p
def allowed(p,kill):
    N=ord_of_G(p)
    if N is None: return None,None
    QRS=qr_set(p); OK=set(); P=None
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

def primes_upto(B):
    sv=[True]*(B+1); sv[0]=sv[1]=False
    for i in range(2,int(B**0.5)+1):
        if sv[i]:
            for j in range(i*i,B+1,i): sv[j]=False
    return [i for i in range(2,B+1) if sv[i]]

if __name__=="__main__":
    t0=time.time()
    # sanity: exact rational checks of floor classes
    from fractions import Fraction as F
    def addE(P,Q):
        if P is None: return Q
        if Q is None: return P
        x1,y1=P; x2,y2=Q
        if x1==x2 and y1==-y2: return None
        lam=(F(y2-y1)/F(x2-x1) if P!=Q else F(3*x1*x1+2*A*x1+B2, 2*y1))
        x3=lam*lam-A-x1-x2
        return (x3, lam*(x1-x3)-y1)
    def mulE(P,n):
        R=None; Q=P
        while n:
            if n&1: R=addE(R,Q)
            Q=addE(Q,Q); n>>=1
        return R
    def Xrat(P):
        x,y=P
        if x==0 or x==36: return None
        return F(6*y-92*x, x*(x-36))
    G2=mulE(G,2)
    out("2G_B=(%s,%s) pole-branch x=36: %s ; X(-G)=%s (5/41? %s)"%(
        G2[0],G2[1],G2[0]==36, Xrat((G[0],-G[1])), Xrat((G[0],-G[1]))==F(5,41)))
    out("X(3G)=%s (41/5? %s); X(4G)=%s (414/209? %s)"%(
        Xrat(mulE(G,3)), Xrat(mulE(G,3))==F(41,5),
        Xrat(mulE(G,4)), Xrat(mulE(G,4))==F(414,209)))
    # killing primes brute force on C3_B: W^2=9x^8-92x^6+310x^4-92x^2+9
    out("== killing primes C3_B ==")
    KP=[]
    for p in primes_upto(300):
        if p in (2,3): continue
        sol=set()
        for x in range(p):
            v=(9*pow(x,8,p)-92*pow(x,6,p)+310*pow(x,4,p)-92*x*x+9)%p
            if v==0 or pow(v,(p-1)//2,p)==1: sol.add(x)
        if sol<= {0,1,p-1}: KP.append(p)
    out("killing primes (x in {0,+-1} only):",KP)
    # p=3 vacuity check
    sol3=sum(1 for x in range(3) if (9*pow(x,8,3)-92*pow(x,6,3)+310*pow(x,4,3)-92*x*x+9)%3 in (0,1))
    out("p=3 solvable classes: %d/3 (vacuous if 3)"%sol3)
    # sieve: kill primes then grow (count-shrinking) then hunt
    KP=[p for p in KP if not singular(p)]
    M,S=1,{0}
    for p in KP:
        N,OK=allowed(p,True)
        if N is None: continue
        M,S=crt_merge(M,S,N,OK)
        out("kill p=%2d ord=%4d |OK|=%3d -> %d mod %d"%(p,N,len(OK),len(S),M))
    for p in primes_upto(400):
        if p in KP or p in (2,3) or singular(p): continue
        N,OK=allowed(p,False)
        if N is None: continue
        g=math.gcd(M,N)
        if len(S)*len(OK)//max(g,1) > 300000: continue
        M2,S2=crt_merge(M,S,N,OK)
        if len(S2)<len(S): M,S=M2,S2
    out("after grow: %d classes mod %d support %s (%.0fs)"%(len(S),M,sorted(factorize(M)),time.time()-t0))
    # hunt M-smooth ord primes up to 2e5
    for p in primes_upto(200000):
        if p<=400 or p in (2,3) or singular(p): continue
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
            out("hunt p=%6d ord=%6d -> %d classes mod %d (%.0fs)"%(p,o,len(S),M,time.time()-t0))
            if len(S)<=4: break
    json.dump({"M":M,"S":sorted(S),"curve":"B","coset":"t=0"},open("mss_k34_sieve2_stateB.json","w"))
    out("FINAL B t=0: %d classes mod %d density %.3e"%(len(S),M,len(S)/M))
    out("survivors:",sorted(S)[:40])
    out("floor {0,1,2,-2} present: %s"%str(tuple((c%M) in S for c in (0,1,2,-2))))
    out("elapsed %.0fs"%(time.time()-t0))