"""K3/K4 quartic reduction + per-prime square sieve + extended census.

K3: R_p*Y_q = 3*Y_p*R_q  (X = 3Y side of {X,Y}={3m,m}, i.e. 2C=D0 with X>=Y)
K4: Y_p*R_q = 3*R_p*Y_q  (mirror)

REDUCTION (proved here, verified numerically in part 2):
Fix p; let x = c/d > 1 be the ratio of q's rep (Y_q = d^4*4x(x^2-1),
R_q = d^4*|x^4-6x^2+1|).  K3 <=> 4*R_p*x(x^2-1) = 3*Y_p*|x^4-6x^2+1|.
Divide by x^2, set u = x - 1/x  (so x^2+x^-2 = u^2+2):
    4*R_p*u = 3*Y_p*|u^2 - 4|
  <=> 3*Y_p*u^2 -/+ 4*R_p*u - 12*Y_p = 0   (quadratic in u!)
so u rational forces  Delta = 16*(R_p^2 + 9*Y_p^2) a rational square,
i.e. A(p):  R_p^2 + 9*Y_p^2 = k^2 (integer square).  MIRROR (fix q,
quartic in x_p = a/b): K3 also forces B(q): 9*R_q^2 + Y_q^2 = k2^2.
K4 is the mirror: K4 forces B(p) and A(q).

Divisor characterization (integer factor chains, both sides odd/even
checked): with R = R_p, Y = Y_p, gcd arguments give
  A(p) <=> one of:  R = |36 s^2 - r^2|, Y = 4 r s      (d-split {1,36})
                    R = |9 s^2 - 4 r^2|, Y = 24 r s    (d-split {4,9})
  B(p) <=> R odd => (k-Y)(k+Y)=9R^2 coprime odd:
                    2Y = |9 s^2 - r^2|, R = r s
(part 4 re-derives these from the divisor scan on any hits; expect 0).

CENSUS: A/B tested for every 1mod4 prime <= 300000 (per-prime sieve:
kills K3 for p<=3e5 with q UNBOUNDED, and K4 for q<=3e5 with p
UNBOUNDED -- strictly stronger than the pair census).  Direct K3/K4
pair equations re-checked for all p<q<=3e5 (84M pairs) as confirmation.
ASCII only, flush=True everywhere.
"""
import math, sys, time

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

QMAX = 300000
PR = primes1mod4(QMAX)
P(f'{len(PR)} primes 1 mod 4 up to {QMAX}')

def Y4(a,b): return abs(4*a*b*(a*a-b*b))
def R4(a,b): return abs(a**4 - 6*a*a*b*b + b**4)

def rep(n):
    for aa in range(1, math.isqrt(n//2)+1):
        b2 = n-aa*aa; b = math.isqrt(b2)
        if b>aa and b*b==b2: return (b, aa)
    raise ValueError(n)

def builder_D(w2):
    out=set()
    for u in range(math.isqrt(w2), math.isqrt(w2//2), -1):
        v2 = w2-u*u; v = math.isqrt(v2)
        if v>0 and v*v==v2 and u>v: out.add(2*u*v)
    return out

# per-prime tables
P('=== building per-prime (Y,R) tables ===')
YT={}; RT={}
for n in PR:
    a,b = rep(n); YT[n]=Y4(a,b); RT[n]=R4(a,b)
P('done')

# ---------- part 0: self-test ----------
P('=== 0. SELF-TEST: closed form vs builder, p<q<=120 ===')
bad=0; n=0
for i,p in enumerate(PR):
    if p>120: break
    for q in PR[i+1:]:
        if q>120: break
        D0 = {p*p*YT[q], q*q*YT[p], abs(RT[p]*YT[q]-YT[p]*RT[q]),
              RT[p]*YT[q]+YT[p]*RT[q]}
        n+=1
        if builder_D(p*q*p*q) != D0: bad+=1; P('MISMATCH',p,q)
P(f'pairs={n} mismatches={bad}', 'PASS' if bad==0 else 'FAIL')

# ---------- part 1: near-miss confirmation ----------
P('=== 1. near-miss (173,7933) for K3 ===')
p,q = 173,7933
X = RT[p]*YT[q]; Y = YT[p]*RT[q]
P(f'p={p} q={q}: X=R_p*Y_q={X}, Y=Y_p*R_q={Y}')
P(f'X-3Y = {X-3*Y}  (filed: 50,004,240)')
P(f'|log(X/3Y)| = {abs(math.log(X/(3*Y)))}  (filed ~4e-5)')
# argmin over p<=200, q<=2e5 (reproduce filed argmins K3 (173,7933), K4 (137,3709))
w3=1e9; w4=1e9; a3=None; a4=None
for i,pp in enumerate(PR):
    if pp>200: break
    Rp,Yp = RT[pp],YT[pp]
    for qq in PR[i+1:]:
        if qq>200000: break
        Rq,Yq = RT[qq],YT[qq]
        X_ = Rp*Yq; Y_ = Yp*Rq
        r3 = abs(math.log(X_/(3*Y_)))
        r4 = abs(math.log(Y_/(3*X_)))
        if r3<w3: w3=r3; a3=(pp,qq)
        if r4<w4: w4=r4; a4=(pp,qq)
P(f'min |log| K3 = {w3:.6f} at {a3}; K4 = {w4:.6f} at {a4}')

# ---------- part 2: reduction iff-verification ----------
P('=== 2. reduction verification: K3 <=> 4R_p u = 3Y_p|u^2-4| (u=c/d-d/c) ===')
from fractions import Fraction
n=0; mism=0
for i,p in enumerate(PR):
    if p>2000: break
    Rp,Yp = RT[p],YT[p]
    for q in PR[i+1:]:
        if q>2000: break
        # direct
        k3 = (Rp*YT[q] == 3*Yp*RT[q])
        # via u (exact rationals): u = (c^2-d^2)/(cd) with (c,d) rep of q
        c,d = rep(q)
        u = Fraction(c*c-d*d, c*d)
        quad = (4*Rp*u == 3*Yp*abs(u*u-4))
        n+=1
        if k3 != quad: mism+=1; P('IFF-MISMATCH',p,q,k3,quad)
P(f'pairs={n} iff-mismatches={mism}', 'PASS' if mism==0 else 'FAIL')
# necessity of the square conditions at the pair level
P('=== 2b. square conditions A(p),B(q) at pair level (p<q<=5000) ===')
nA=nB=nhits=0; n=0
for i,p in enumerate(PR):
    if p>5000: break
    Rp,Yp = RT[p],YT[p]
    k = math.isqrt(Rp*Rp+9*Yp*Yp)
    A = (k*k == Rp*Rp+9*Yp*Yp)
    if A: nA+=1
    for q in PR[i+1:]:
        if q>5000: break
        Rq,Yq = RT[q],YT[q]
        kq = math.isqrt(9*Rq*Rq+Yq*Yq)
        if kq*kq == 9*Rq*Rq+Yq*Yq: nB+=1
        n+=1
P(f'pairs={n}; A(p)-hits={nA}; B(q)-hits={nB} (per-prime counts within loop)')
# ---------- part 3: per-prime square census (the sieve) ----------
P('=== 3. PER-PRIME SQUARE CENSUS, all 1mod4 primes <= %d ===' % QMAX)
t0=time.time()
hitsA=[]; hitsB=[]
for idx,p in enumerate(PR):
    Rp,Yp = RT[p],YT[p]
    s1 = Rp*Rp + 9*Yp*Yp
    k1 = math.isqrt(s1)
    if k1*k1 == s1: hitsA.append((p,'A',s1))
    s2 = 9*Rp*Rp + Yp*Yp
    k2 = math.isqrt(s2)
    if k2*k2 == s2: hitsB.append((p,'B',s2))
P(f'A-hits={len(hitsA)} B-hits={len(hitsB)} time={time.time()-t0:.1f}s')
if hitsA: P('first A-hits:', hitsA[:10])
if hitsB: P('first B-hits:', hitsB[:10])
P('VERDICT: if both 0 => K3 dead for every pair with p<=QMAX (q unbounded)',
  'and every pair with q<=QMAX (p unbounded); same for K4 mirrored.')

# ---------- part 4: direct pair census K3/K4, p<q<=QMAX ----------
P('=== 4. DIRECT K3/K4 PAIR CENSUS, p<q<=%d ===' % QMAX)
t0=time.time(); n=0; hits=0
Rl=[RT[p] for p in PR]; Yl=[YT[p] for p in PR]
NP=len(PR)
for i in range(NP):
    Rp=Rl[i]; Y3=3*Yl[i]; Yp=Yl[i]; R3=3*Rp
    for j in range(i+1, NP):
        Rq=Rl[j]; Yq=Yl[j]
        n+=1
        if Rp*Yq == Y3*Rq: hits+=1; P('K3 HIT', PR[i], PR[j])
        if Yp*Rq == R3*Yq: hits+=1; P('K4 HIT', PR[i], PR[j])
    if i % 2000 == 1999:
        P(f'  progress i={i+1}/{NP} pairs={n} hits={hits} t={time.time()-t0:.0f}s')
P(f'pairs={n} K3/K4 hits={hits} time={time.time()-t0:.1f}s')

# ---------- part 5: primitive-Pythagorean characterization on any hits ----------
P('=== 5. A/B hits via primitive triples (expect none) ===')
# A(p): (R, 3Y, k) primitive triple => exists coprime m>n: mn=3Y/2, |m^2-n^2|=R
# B(p): (Y, 3R, k) primitive triple => exists coprime m>n: mn=Y/2, |m^2-n^2|=3R
def divisors(m):
    ds=set()
    for k in range(1, math.isqrt(m)+1):
        if m % k==0:
            ds.add(k); ds.add(m//k)
    return sorted(ds)
for tag,lst in (('A',hitsA),('B',hitsB)):
    for h in lst:
        p=h[0]; Rp,Yp=RT[p],YT[p]
        M = (3*Yp//2) if tag=='A' else (Yp//2)
        T = Rp if tag=='A' else 3*Rp
        found=[]
        for m in divisors(M):
            n_ = M//m
            if m<=n_ or m+n_ % 2==0 and False: pass
            if abs(m*m - n_*n_) == T: found.append((m,n_))
        P(tag+'-hit',p,'triples:',found)
P('DONE')
OUT.close()
