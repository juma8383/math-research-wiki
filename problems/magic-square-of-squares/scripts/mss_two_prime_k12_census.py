"""Full sum/double relation census on the closed form, extended to q<=1e5,
plus cross-prime divisibility counts (the K12 necessary condition etc.).

Closed form ([mss-two-prime-freeness], self-tested here against the builder):
  A=p^2 Y_q, B=q^2 Y_p, X=R_p Y_q, Y=Y_p R_q, D={A,B,|X-Y|,X+Y}.

Relations tested per pair: all x+y=z and 2x=y over the 4 elements
(equivalent to the full K1..K16 list by the filed iff-case-tree).

Cross-divisibility events counted:
  q|Y_p, q|R_p  (K12 forces BOTH), p|Y_q, p|R_q (K1 forces p^2|R_q),
  q^2|R_p (K2 -- expect 0 always), p^2|R_q (Wieferich).
ASCII, flush=True.
"""
import math, sys

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

PR = primes1mod4(100000)

# self-test of elems vs builder (small range)
def elems(p,q,cache={}):
    if p not in cache:
        a,b = rep(p); cache[p]=(Y4(a,b),R4(a,b))
    if q not in cache:
        c,d = rep(q); cache[q]=(Y4(c,d),R4(c,d))
    Yp,Rp = cache[p]; Yq,Rq = cache[q]
    return p*p*Yq, q*q*Yp, abs(Rp*Yq - Yp*Rq), Rp*Yq + Yp*Rq, (Yp,Yq,Rp,Rq)

P('=== self-test vs builder (p<q<=120) ===')
bad=0; n=0
for i,p in enumerate(PR):
    if p>120: break
    for q in PR[i+1:]:
        if q>120: break
        A,B,C,D,_ = elems(p,q); n+=1
        if builder_D(p*q*p*q) != {A,B,C,D}: bad+=1; P('MISMATCH',p,q)
P(f'pairs={n} mismatches={bad}', 'PASS' if bad==0 else 'FAIL')

P('=== full relation census, all p<q<=1e5 ===')
hits=0; n=0
qYp=qRp=qYp_and_qRp=pYq=pRq=p2Rq=q2Rp=0
k1near=(1e9,None)
import math as m
for i,p in enumerate(PR):
    Ap = p*p
    for j in range(i+1, len(PR)):
        q = PR[j]
        if q>100000: break
        A,B,C,D,(Yp,Yq,Rp,Rq) = elems(p,q)
        n+=1
        S=(A,B,C,D)
        for x in range(4):
            for y in range(x,4):
                s = S[x]+S[y]
                for t in range(4):
                    if s==S[t]: hits+=1; P('SUM HIT',p,q,x,y,t)
        for x in range(4):
            if 2*S[x]==S[0] or 2*S[x]==S[1] or 2*S[x]==S[2] or 2*S[x]==S[3]:
                if 2*S[x] in S: hits+=1; P('DOUBLE HIT',p,q,x)
        if Yp % q==0: qYp+=1
        if Rp % q==0: qRp+=1
        if (Yp % q==0) and (Rp % q==0): qYp_and_qRp+=1
        if Yq % p==0: pYq+=1
        if Rq % p==0:
            pRq+=1
            if Rq % Ap == 0:
                p2Rq+=1
                r = abs(m.log(Ap*Yq/(2*Yp*Rq)))
                if r < k1near[0]: k1near=(r,(p,q))
        if Rp % (q*q)==0: q2Rp+=1
P(f'pairs={n}, relation hits={hits} (expect 0)')
P(f'cross-div counts: q|Y_p={qYp}, q|R_p={qRp}, q|Y_p AND q|R_p={qYp_and_qRp}, '
  f'p|Y_q={pYq}, p|R_q={pRq}, p^2|R_q={p2Rq}, q^2|R_p={q2Rp}')
P(f'closest K1 approach among p^2|R_q pairs: |logratio|={k1near[0]:.6f} at {k1near[1]}')
P('DONE')
OUT.close()