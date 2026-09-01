"""Sum-freeness of D((pq)^2) on the closed form: slice theorems + kill-equations.

Closed form (verified, [mss-two-prime]): pi=a+bi (a^2+b^2=p), rho=c+di (c^2+d^2=q),
  Y_p = |Im pi^4| = |4ab(a^2-b^2)|,  R_p = |Re pi^4| = |a^4-6a^2 b^2+b^4|,
  A = p^2 Y_q,  B = q^2 Y_p,  X = R_p Y_q,  Y = Y_p R_q,
  D((pq)^2) = {A, B, C=|X-Y|, D0=X+Y}.

Parts:
 0. SELF-TEST: closed-form 4-set == brute-force builder D(w^2) for all p<q<=120.
 1. Distinctness/positivity of the 4 elements (all p<q<=1200).
 2. Slice theorems, verified numerically:
    S1: A+B > D0 always  (so A+B in set is impossible).
    S2: C+D0 = 2*max(X,Y); C+D0=A when X>=Y iff 2*R_p=p^2 (odd=even: dead);
        exactly: 2R_p=p^2 <=> a^4-14a^2b^2+b^4=0 or 3a^4-10a^2b^2+3b^4=0,
        no integer solutions (brute-forced a,b<=4000). Mirror for q.
    S3: p | Y_p and p | R_p never (p ∤ 4ab(a^2-b^2), p ∤ Re pi^4 mod p).
 3. FULL relation census: every x+y=z and 2x=y among {A,B,C,D0} for all
    p<q<=1500; each hit (expect none) is symbolically reduced to a
    kill-equation in (a,b,c,d). Outputs the deduped kill-equation list K1..Kn
    with closeness data (log2 of min |log ratio| over the census).
 4. Structured regimes for the kill-equations themselves:
    - fixed small p, q up to 5e4: track K1..K4 near-misses;
    - twin-style q=p+2 up to 1e4;
    - pairs with p | Y_q (the regime where v_p(X)>0).
ASCII only, flush=True everywhere.
"""
import math, sys
from itertools import combinations

OUT = open(__file__.replace('.py', '.log'), 'w', encoding='utf-8')
def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); OUT.write(s + '\n'); OUT.flush()

def primes1mod4(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=False
    return [k for k in range(5, n+1, 4) if s[k]]

PR = primes1mod4(20000)

def rep(n):
    """Primitive rep a>=b>0, a^2+b^2=n (n prime 1 mod 4)."""
    a = math.isqrt(n-1)
    while a*a > n//2: a -= 1
    # find any: use Cornacchia-lite scan
    for aa in range(math.isqrt(n)+1):
        b2 = n-aa*aa; b = math.isqrt(b2)
        if b>0 and b*b==b2: return (max(aa,b), min(aa,b))
    raise ValueError(n)

def Y4(a,b): return abs(4*a*b*(a*a-b*b))
def R4(a,b): return abs(a**4 - 6*a*a*b*b + b**4)

def elems(p,q):
    a,b = rep(p); c,d = rep(q)
    Yp,Yq,Rp,Rq = Y4(a,b), Y4(c,d), R4(a,b), R4(c,d)
    A,B = p*p*Yq, q*q*Yp
    X,Y = Rp*Yq, Yp*Rq
    return dict(A=A,B=B,C=abs(X-Y),D=X+Y,X=X,Y=Y,p=p,q=q,
                Yp=Yp,Yq=Yq,Rp=Rp,Rq=Rq,a=a,b=b,c=c,d=d)

def builder_D(w2):
    """All 2uv with u^2+v^2=w2, u>v>0."""
    out=set()
    for u in range(math.isqrt(w2), math.isqrt(w2//2), -1):
        v2 = w2-u*u
        v = math.isqrt(v2)
        if v>0 and v*v==v2 and u>v: out.add(2*u*v)
    return out

def closed_set(e):
    return {e['A'], e['B'], e['C'], e['D']}

# ---------- 0. self-test ----------
P('=== 0. SELF-TEST: closed form vs builder ===')
bad=0; n=0
for i,p in enumerate(PR):
    if p>120: break
    for q in PR[i+1:]:
        if q>120: break
        e=elems(p,q); w=p*q
        bd=builder_D(w*w); cs=closed_set(e); n+=1
        if bd!=cs:
            bad+=1; P('MISMATCH',p,q,sorted(bd),sorted(cs))
P(f'self-test: {n} pairs, mismatches={bad}', 'PASS' if bad==0 else 'FAIL')

# ---------- 1. distinctness ----------
P('=== 1. distinctness / positivity ===')
bad=0; n=0
for i,p in enumerate(PR):
    if p>1200: break
    for q in PR[i+1:]:
        if q>1200: break
        e=elems(p,q); n+=1
        v=sorted(closed_set(e))
        if len(set(v))<4 or min(v)<=0: bad+=1; P('BAD',p,q,v)
P(f'pairs={n}, non-distinct/nonpositive={bad}', 'PASS' if bad==0 else 'FAIL')

# ---------- 2. slice theorems ----------
P('=== 2. slice theorems (numeric verification) ===')
vS1=vS2a=vS2b=vS3=0; n=0
for i,p in enumerate(PR):
    if p>5000: break
    for q in PR[i+1:]:
        if q>5000: break
        e=elems(p,q); n+=1
        if not (e['A']+e['B'] > e['D']): vS1+=1
        # S2: C+D0=2max(X,Y); check it never equals A or B via the clean sign case
        if e['X']>=e['Y'] and e['C']+e['D']==e['A']: vS2a+=1
        if e['Y']>=e['X'] and e['C']+e['D']==e['B']: vS2b+=1
        if e['p'] in (e['Yp'],e['Rp']) or e['q'] in (e['Yq'],e['Rq']): vS3+=1
P(f'S1 A+B>D violations={vS1}; S2 C+D=A(X>=Y)={vS2a}, C+D=B(Y>=X)={vS2b}; '
  f'S3 p|Y_p or p|R_p hits={vS3}; pairs={n}')
# S2 core: 2R_p = p^2 solvable?
P('S2 check: a^4-14a^2b^2+b^4==0 or 3a^4-10a^2b^2+3b^4==0, a,b<=4000:')
cnt=0
for a in range(1,4001):
    a2=a*a
    for b in range(1,a+1):
        b2=b*b
        if a2*a2-14*a2*b2+b2*b2==0 or 3*a2*a2-10*a2*b2+3*b2*b2==0: cnt+=1
P(f'  solutions={cnt} (expect 0)')

# ---------- 3. full relation census + symbolic reduction ----------
P('=== 3. full relation census, p<q<=1500 ===')
def sign_reduce(e, xpy, target):
    """Reduce relation  2x=target among {A,B,C,D0} to kill-equation ids."""
    A,B,C,D,X,Y = e['A'],e['B'],e['C'],e['D'],e['X'],e['Y']
    Yp,Yq,Rp,Rq = e['Yp'],e['Yq'],e['Rp'],e['Rq']
    out=[]
    if xpy is None:  # double relation 2*src=target
        for src,tag in ((A,'A'),(B,'B'),(C,'C'),(D,'D')):
            if 2*src==target:
                # symbolic
                if tag=='A' and target==B: out.append('K9: 2p^2Yq=q^2Yp')
                elif tag=='B' and target==A: out.append('K11: 2q^2Yp=p^2Yq')
                elif tag=='C' and target==A: out.append('K13a/b: 2|X-Y|=p^2Yq')
                elif tag=='C' and target==B: out.append('K14a/b: 2|X-Y|=q^2Yp')
                elif tag=='C' and target==D: out.append('K3/K4: X=3Y or Y=3X')
                elif tag=='D' and target==A: out.append('K15: 2RpYq+2YpRq=p^2Yq')
                elif tag=='D' and target==B: out.append('K16: 2RpYq+2YpRq=q^2Yp')
                elif tag=='A' and target==D: out.append('K10: 2p^2Yq=RpYq+YpRq')
                elif tag=='B' and target==D: out.append('K12: 2q^2Yp=RpYq+YpRq')
        return out
    # x+y=target: identify the pair symbolically
    pairs={}
    pairs[(A,B)]='A+B'; pairs[(A,C)]='A+C'; pairs[(A,D)]='A+D'
    pairs[(B,C)]='B+C'; pairs[(B,D)]='B+D'; pairs[(C,D)]='C+D'
    for (u,v),tag in pairs.items():
        if u+v==target:
            if tag=='A+B': out.append('S1-violation?! A+B=D (proved impossible)')
            elif tag=='C+D':
                if X>=Y and target==A: out.append('S2a-violation?! (2Rp=p^2)')
                elif Y>=X and target==B: out.append('S2b-violation?! (2Rq=q^2)')
                elif X>=Y: out.append('K2: 2RpYq=q^2Yp (C+D=B, X>=Y)')
                else: out.append('K1: 2YpRq=p^2Yq (C+D=A, X<Y)')
            elif tag=='A+C':
                if X>=Y: out.append('K1: p^2Yq=2YpRq (A+C=D, X>=Y)')
                else: out.append('dead-parity: p^2=2Rp (A+C=D, X<Y)')
            elif tag=='B+C':
                if Y>=X: out.append('K2: q^2Yp=2RpYq (B+C=D, Y>=X)')
                else: out.append('dead-parity: q^2=2Rq (B+C=D, X>Y)')
            elif tag=='A+D': out.append('K5: Yq(p^2+Rp)=Yp(q^2-Rq) (A+D=B)')
            elif tag=='B+D': out.append('K8: Yp(q^2+Rq)=Yq(p^2-Rp) (B+D=A)')
            # A+C=B and B+C=A handled by target match below
    # also targets C or the 'cross' sums A+C=B etc.
    if A+C==B: out.append('K6: Yq(p^2-Rp)=Yp(q^2-Rq) (A+C=B, X>=Y)')
    if A+C==B and X<Y: out.append('K5var: Yq(p^2+Rp)=Yp(q^2+Rq)?? check')
    if B+C==A: out.append('K7: Yp(q^2-Rq)=Yq(p^2+Rp)?? (B+C=A)')
    return out

def sign_reduce_sum(e, u, v, t):
    """u+v=t among {A,B,C,D}: symbolic reduction to kill-equations."""
    A,B,C,D0,X,Y = e['A'],e['B'],e['C'],e['D'],e['X'],e['Y']
    Yp,Yq,Rp,Rq = e['Yp'],e['Yq'],e['Rp'],e['Rq']
    tag=None
    for pair,lab in (((A,B),'A+B'),((A,C),'A+C'),((A,D),'A+D'),
                     ((B,C),'B+C'),((B,D),'B+D'),((C,D),'C+D')):
        if {u,v}==set(pair): tag=lab
    out=[]
    if tag=='A+B': out.append('S1-violation?! A+B=D (proved impossible)')
    elif tag=='C+D':
        if X>=Y and t==A: out.append('S2a-violation?! (2Rp=p^2)')
        elif Y>=X and t==B: out.append('S2b-violation?! (2Rq=q^2)')
        elif X>=Y: out.append('K2: 2RpYq=q^2Yp (C+D=B, X>=Y)')
        else: out.append('K1: 2YpRq=p^2Yq (C+D=A, X<Y)')
    elif tag=='A+C':
        if X>=Y: out.append('K1: p^2Yq=2YpRq (A+C=D, X>=Y)')
        else: out.append('dead-parity: p^2=2Rp (A+C=D, X<Y)')
        if t==B:
            out.append('K6: Yq(p^2-Rp)=Yp(q^2-Rq) (A+C=B, X>=Y)' if X>=Y
                       else 'K5var: Yq(p^2+Rp)=Yp(q^2+Rq) (A+C=B, X<Y)')
    elif tag=='B+C':
        if Y>=X: out.append('K2: q^2Yp=2RpYq (B+C=D, Y>=X)')
        else: out.append('dead-parity: q^2=2Rq (B+C=D, X>Y)')
        if t==A:
            out.append('K7: Yp(q^2-Rq)=Yq(p^2+Rp)?? (B+C=A, Y>=X)' if Y>=X
                       else 'K8var: Yp(q^2+Rq)=Yq(p^2-Rp) (B+C=A, Y<X)')
    elif tag=='A+D': out.append('K5: Yq(p^2+Rp)=Yp(q^2-Rq) (A+D=B)')
    elif tag=='B+D': out.append('K8: Yp(q^2+Rq)=Yq(p^2-Rp) (B+D=A)')
    return out

hits=0; n=0; killset={}
for i,p in enumerate(PR):
    if p>1500: break
    for q in PR[i+1:]:
        if q>1500: break
        e=elems(p,q); n+=1
        S=closed_set(e)
        for x in S:
            for k in sign_reduce(e,None,2*x):
                if 'dead' not in k and 'violation' not in k:
                    hits+=1; killset[k]=killset.get(k,0)+1
        for x,y in combinations(sorted(S),2):
            for t in S:
                if x+y==t:
                    for k in sign_reduce_sum(e,x,y,t):
                        if 'dead' not in k and 'violation' not in k:
                            hits+=1; killset[k]=killset.get(k,0)+1
P(f'pairs={n}, live-relation hits={hits} (expect 0)')
P('kill-equations referenced:', killset if killset else 'NONE')

# ---------- 4. structured regimes ----------
P('=== 4. kill-equation regime probes ===')
# K3: RpYq = 3YpRq ; K1: p^2Yq=2YpRq; K2: q^2Yp=2RpYq
worst={'K1':1e9,'K2':1e9,'K3':1e9,'K4':1e9}; argw={}
for i,p in enumerate(PR):
    if p>200: break
    for q in PR:
        if q<=p: continue
        if q>200000: break
        e=elems(p,q)
        r1=abs(math.log(e['p']**2*e['Yq']/(2*e['Yp']*e['Rq'])))
        r2=abs(math.log(e['q']**2*e['Yp']/(2*e['Rp']*e['Yq'])))
        r3=abs(math.log(e['Rp']*e['Yq']/(3*e['Yp']*e['Rq'])))
        r4=abs(math.log(e['Yp']*e['Rq']/(3*e['Rp']*e['Yq'])))
        for k,r in (('K1',r1),('K2',r2),('K3',r3),('K4',r4)):
            if r<worst[k]: worst[k]=r; argw[k]=(p,q)
P('min |log ratio| over p<=200, q<=2e5:', {k:round(v,4) for k,v in worst.items()})
P('  argmin pairs:', argw)
# twins q=p+2
tw=0; twinbad=0
for p in PR:
    q=p+2
    if q in set(PR) and p<10000:
        tw+=1; e=elems(p,q); S=closed_set(e)
        for x,y in combinations(sorted(S),2):
            if x+y in S: twinbad+=1
        for x in S:
            if 2*x in S: twinbad+=1
P(f'twin pairs q=p+2 (p<1e4): {tw} pairs, relations={twinbad}')
# p | Yq regime
reg=0; regbad=0
for i,p in enumerate(PR[:60]):
    for q in PR[i+1:]:
        if q>20000: break
        e=elems(p,q)
        if e['Yq']%e['p']==0:
            reg+=1; S=closed_set(e)
            for x,y in combinations(sorted(S),2):
                if x+y in S: regbad+=1
            for x in S:
                if 2*x in S: regbad+=1
P(f'p|Yq pairs (p in first 60 primes, q<=2e4): {reg} pairs, relations={regbad}')
P('DONE')
OUT.close()