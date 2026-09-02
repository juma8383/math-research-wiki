#!/usr/bin/env python
# Claude B-side verification for [mss-k34-sieve2] Section 4:
#  X_B identities (exact) + killing-prime sieve -> 5 classes mod 264.
import sys, math
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

A2B, A4B = 256, -2048
GBQ = (F(-128), F(1536))
def addQ(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 == -y2: return None
    lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2B*x1+A4B)/(2*y1)
    x3 = lam*lam - A2B - x1 - x2
    return (x3, -(y1 + lam*(x3-x1)))
def XB(P):
    if P is None: return 'inf'
    x, y = P
    if x == 0 or x == 36: return 'pole'
    return F(6*y - 92*x, x*(x-36))

P = None; pts = {}
for i in range(1, 5):
    P = addQ(P, GBQ); pts[i] = P
NG = (F(-128), -F(1536))
out("X_B(G)  =", XB(pts[1]), "expect 1      :", XB(pts[1]) == F(1,1))
out("X_B(-G) =", XB(NG), "expect 5/41:", XB(NG) == F(5,41))
out("X_B(3G) =", XB(pts[3]), "expect 41/5   :", XB(pts[3]) == F(41,5))
out("X_B(4G) =", XB(pts[4]), "expect 414/209:", XB(pts[4]) == F(414,209))
out("2G      =", pts[2], "expect (36,-552):", pts[2] == (F(36), F(-552)))
out("X_B(2G) =", XB(pts[2]), "(pole expected)")

# mod-p machinery (reuse agent's p2 conventions for B)
G = (-128, 1536); A, B2 = A2B, A4B
def ec_add(Pp,Q,p):
    if Pp is None: return Q
    if Q is None: return Pp
    x1,y1=Pp; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0: return None
    if Pp==Q:
        if y1%p==0: return None
        lam=(3*x1*x1+2*A*x1+B2)*pow(2*y1%p,p-2,p)%p
    else:
        lam=(y2-y1)*pow((x2-x1)%p,p-2,p)%p
    x3=(lam*lam-A-x1-x2)%p
    return (x3,(lam*(x1-x3)-y1)%p)
def ec_mul(Pp,n,p):
    if Pp is not None: Pp=(Pp[0]%p, Pp[1]%p)
    if n<0: return ec_mul((Pp[0],(-Pp[1])%p),-n,p)
    R=None; Q=Pp
    while n:
        if n&1: R=ec_add(R,Q,p)
        Q=ec_add(Q,Q,p); n>>=1
    return R
def group_order_brute(p):
    n=1
    for x in range(p):
        v=(x*x*x+A*x*x+B2*x)%p
        if v==0: n+=1
        elif pow(v,(p-1)//2,p)==1: n+=2
    return n
def factorize(n):
    fs={}; d=2
    while d*d<=n:
        while n%d==0: fs[d]=fs.get(d,0)+1; n//=d
        d += 1 if d==2 else 2
    if n>1: fs[n]=fs.get(n,0)+1
    return fs
def ord_of_G(p):
    o=group_order_brute(p); fs=factorize(o)
    for q in fs:
        for _ in range(fs[q]):
            if ec_mul(G,o//q,p) is None: o//=q
            else: break
    return o
def singular(p):
    for x in range(p):
        if (x*x*x+A*x*x+B2*x)%p==0 and (3*x*x+2*A*x+B2)%p==0: return True
    return False
def XqB(P,p):
    x,y=P
    if x%p==0 or x%p==36%p: return None
    return (6*y-92*x)*pow(x*(x-36)%p,p-2,p)%p
def allowedB(p,kill):
    N=ord_of_G(p); QRS={i*i%p for i in range(p)}
    OK=set(); Pp=None
    for n in range(N):
        if n==1: Pp=G
        elif n>1: Pp=ec_add(Pp,G,p)
        if Pp is None: OK.add(n); continue
        X=XqB(Pp,p)
        if X is None: OK.add(n); continue
        if kill:
            if X == 0 or X == 1: OK.add(n)
        elif X == 0 or X in QRS:
            OK.add(n)
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

out("== B killing-prime sieve ==")
M,S=1,{0}
for p in (5,19,29):
    N,OK=allowedB(p,True)
    M,S=crt_merge(M,S,N,OK)
    out("  kill p=%2d ord=%3d |OK|=%2d -> %d classes mod %d"%(p,N,len(OK),len(S),M))
out("  claim: M=264, 5 classes", M==264 and len(S)==5)
out("  survivors:", sorted(S), " claim {0,1,2,-2,134}:",
    sorted(S)==sorted([0,1,2,M-2,134]))