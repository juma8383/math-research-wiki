#!/usr/bin/env python
# Claude independent verification of the [mss-k34-elliptic] image table (v2,
# signed multiples handled correctly, exact equality).
from fractions import Fraction as F

class EC:
    def __init__(s, a2, a4, a6): s.a2,s.a4,s.a6 = F(a2),F(a4),F(a6)
    def on(s,P):
        if P=='O': return True
        x,y=P; return y*y==x**3+s.a2*x*x+s.a4*x+s.a6
    def add(s,P,Q):
        if P=='O': return Q
        if Q=='O': return P
        x1,y1=P; x2,y2=Q
        if x1==x2 and y1==-y2: return 'O'
        if P==Q: lam=(3*x1*x1+2*s.a2*x1+s.a4)/(2*y1)
        else: lam=(y2-y1)/(x2-x1)
        x3=lam*lam-s.a2-x1-x2
        return (x3,-(y1+lam*(x3-x1)))
    def neg(s,P): return 'O' if P=='O' else (P[0],-P[1])
    def mul(s,P,n):
        # signed multiple, double-and-add
        if n==0: return 'O'
        if n>0:
            R='O'; Q=P
            while n:
                if n&1: R=s.add(R,Q)
                Q=s.add(Q,Q); n>>=1
            return R
        return s.neg(s.mul(P,-n))

EA=EC(-250,17420,35848); EB=EC(310,8140,51912)
GA=(F(126),F(512)); TA=(F(-2),F(0))
GB=(F(-146),F(1536)); TB=(F(-18),F(0))

def mapA(Xq,V):
    xE=(V-1-66*Xq)/(Xq*Xq)
    return (-2*xE, 2*(xE*xE-1)*Xq+132*(xE-1))
def mapB(Xq,V):
    xE=(V-3+F(46,3)*Xq)/(Xq*Xq)
    return (-6*xE, 3*(2*(xE*xE-9)*Xq+F(-92,3)*(xE-3)))

ptsA=[(0,1,1),(0,1,-1),(1,1,4),(1,1,-4),(31,35,4604),(31,35,-4604),
      (35,31,4604),(35,31,-4604),(66,1151,3693311),(66,1151,-3693311),
      (1151,66,3693311),(1151,66,-3693311)]
ptsB=[(0,1,3),(0,1,-3),(1,1,12),(1,1,-12),(5,41,2508),(5,41,-2508),
      (41,5,2508),(41,5,-2508),(209,414,943587),(209,414,-943587),
      (414,209,943587),(414,209,-943587)]

# precompute table { (m,eps): point } exactly
def table(E,G,T,mmax):
    tab={}
    for m in range(-mmax,mmax+1):
        base = E.mul(G,m)
        for eps in (0,1):
            R = E.add(base,T) if eps else base
            tab[(m,eps)]=R
    return tab

def classify(E,tab,P):
    if P=='O': return [k for k,v in tab.items() if v=='O']
    return [k for k,v in tab.items() if v!='O' and v[0]==P[0] and v[1]==P[1]]

print("== M_A images vs m*GA+eps*TA (psi convention, origin (0,-1)->O) ==")
tabA=table(EA,GA,TA,8)
allok=True
for p,q,Vq in ptsA:
    if p==0: continue
    P=mapA(F(p,q), F(Vq,q*q))
    ok=EA.on(P); c=classify(EA,tabA,P)
    allok &= (ok and len(c)>0)
    print("A(%d/%d,%+d): on=%s class=%s"%(p,q,Vq,ok,c))
print("  (0,1) limit -> (4606,-304128) on=%s class=%s"%(
    EA.on((F(4606),F(-304128))), classify(EA,tabA,(F(4606),F(-304128)))))
print("== M_B images vs m*GB+eps*TB ==")
tabB=table(EB,GB,TB,8)
for p,q,Vq in ptsB:
    if p==0: continue
    P=mapB(F(p,q), F(Vq,q*q))
    ok=EB.on(P); c=classify(EB,tabB,P)
    allok &= (ok and len(c)>0)
    print("B(%d/%d,%+d): on=%s class=%s"%(p,q,Vq,ok,c))
print("  (0,3) limit -> (-674/9,-23552/27) on=%s class=%s"%(
    EB.on((F(-674,9),F(-23552,27))), classify(EB,tabB,(F(-674,9),F(-23552,27)))))
print("ALL IMAGE CLAIMS REPRODUCED:", allok)