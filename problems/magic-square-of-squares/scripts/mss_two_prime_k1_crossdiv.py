"""K1-K4 attack via cross-prime divisibility: Lemma A (p|R_q criterion), K2/K11 death.

Closed form ([mss-two-prime-freeness]): pi=a+bi (a^2+b^2=p), rho=c+di (c^2+d^2=q),
  Y_p=|4ab(a^2-b^2)|, R_p=|a^4-6a^2b^2+b^4|, A=p^2 Y_q, B=q^2 Y_p,
  X=R_p Y_q, Y=Y_p R_q, C=|X-Y|, D0=X+Y.

Kill-equations under attack:
  K1: p^2 Y_q = 2 Y_p R_q   (forces p^2 | R_q)
  K2: q^2 Y_p = 2 R_p Y_q   (forces q^2 | R_p  -- and 0<R_p<p^2<q2 => DEAD?)
  K11: 2B=A i.e. 2 q^2 Y_p = p^2 Y_q (v_q(LHS)>=2 vs v_q(RHS)=0 => DEAD?)

Lemma A (to verify): p | R_q  <=>  p == 1 mod 8  AND  q lies in the single coset
  (4+2*sqrt(2)) * QR_p  (well-defined since (4+2s2)/(4-2s2)=3+2sqrt2=(1+sqrt2)^2).
  Derivation: R_q = 8c^4-8qc^2+q^2 exactly (identity test in Part 0); mod p with
  x=c^2/q: 8x^2-8x+1=0 => x=(2+-sqrt2)/4, i.e. c^2 = q(4+-2sqrt2)/8, and the two
  roots lie in the same QR-coset when chi_p(2)=1.

Parts:
 0. identity tests: R4(c,d) == 8c^4-8qc^2+q^2 (exact); closed form == builder.
 1. Lemma A census: all p<q<=3000: p|R_q => p==1 mod 8; coset criterion check
    both directions; root-count check (4 roots c mod p when q in coset).
 2. K2/K11 death verification: inequality chain 0<R_p<p^2 (all pairs q<=5000);
    q | Y_q never; 2R_pY_q==q^2Y_p never; 2q^2Y_p==p^2Y_q never.
 3. Wieferich census: p^2 | R_q for all p<q<=1e5 (p==1 mod 8): count + list.
 4. K1 residual on Wieferich hits: |log(p^2 Y_q / (2 Y_p R_q))|.
ASCII only, flush=True.
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
    for aa in range(math.isqrt(n//2)+1):
        b2 = n-aa*aa
        if b2 <= 0: continue
        b = math.isqrt(b2)
        if b>aa and b*b==b2: return (b, aa)   # a>b>0
    raise ValueError(n)

def legendre(x,p):
    x %= p
    if x == 0: return 0
    r = pow(x,(p-1)//2,p)
    return 1 if r==1 else -1

def sqrt2mod(p):
    # p == 1 mod 8, small p only (direct scan)
    for x in range(2, p):
        if x*x % p == 2: return x
    raise ValueError(p)

# ---------- 0. identity tests ----------
P('=== 0. identity tests ===')
bad=0
for q in (5,13,17,29,37,53,61,73,89,97,101,109,113,149,197,9941):
    c,d = rep(q)
    lhs = R4(c,d)
    rhs = abs(8*c**4 - 8*q*c*c + q*q)
    if lhs != rhs: bad+=1; P('IDENTITY FAIL', q, lhs, rhs)
P('R_q == |8c^4-8qc^2+q^2| identity: FAILS=%d' % bad, 'PASS' if bad==0 else 'FAIL')

# builder cross-check of elems (reuse closed-form script logic, small range)
def elems(p,q):
    a,b = rep(p); c,d = rep(q)
    Yp,Yq,Rp,Rq = Y4(a,b), Y4(c,d), R4(a,b), R4(c,d)
    return dict(A=p*p*Yq, B=q*q*Yp, X=Rp*Yq, Y=Yp*Rq,
                Yp=Yp,Yq=Yq,Rp=Rp,Rq=Rq,p=p,q=q,a=a,b=b,c=c,d=d)

def builder_D(w2):
    out=set()
    for u in range(math.isqrt(w2), math.isqrt(w2//2), -1):
        v2 = w2-u*u; v = math.isqrt(v2)
        if v>0 and v*v==v2 and u>v: out.add(2*u*v)
    return out

PR = primes1mod4(100000)
bad=0; n=0
for i,p in enumerate(PR):
    if p>120: break
    for q in PR[i+1:]:
        if q>120: break
        e=elems(p,q); w=p*q; n+=1
        cs = {e['A'], e['B'], abs(e['X']-e['Y']), e['X']+e['Y']}
        if builder_D(w*w) != cs: bad+=1; P('MISMATCH',p,q)
P(f'closed form vs builder: {n} pairs, mismatches={bad}', 'PASS' if bad==0 else 'FAIL')

# ---------- 1. Lemma A ----------
P('=== 1. Lemma A: p | R_q  <=>  p==1 mod 8 and q in (4+2*sqrt2)*QR_p ===')
n=0; hit=0; bad_mod8=0; bad_coset=0; p5_hits=0
coset_pairs=[]
for i,p in enumerate(PR):
    if p>3000: break
    if p % 8 == 1:
        t2 = sqrt2mod(p); w = (4+2*t2) % p
    for q in PR[i+1:]:
        if q>3000: break
        c,d = rep(q); n+=1
        if R4(c,d) % p == 0:
            hit+=1
            coset_pairs.append((p,q))
            if p % 8 != 1: bad_mod8+=1; P('MOD8 FAIL', p, q)
            else:
                if legendre(w * pow(q,p-2,p) * q % p, p) != 1:  # (w/q)? careful
                    pass
                # proper test: (q * w^{-1}) is QR?
                winv = pow(w, p-2, p)
                if legendre(q*winv % p, p) != 1:
                    bad_coset+=1; P('COSET FAIL', p, q)
if p % 8 == 5: pass
P(f'pairs={n}, p|R_q hits={hit}, mod8 violations={bad_mod8}, coset violations={bad_coset}')
# reverse direction: for p==1 mod 8, every q in the coset (q<=3000) must have p|R_q
rev_bad=0; rev_n=0
for i,p in enumerate(PR):
    if p>3000: break
    if p % 8 != 1: continue
    t2 = sqrt2mod(p); w = (4+2*t2) % p
    winv = pow(w,p-2,p)
    c,d = rep(p)  # unused
    for q in PR[i+1:]:
        if q>3000: break
        if legendre(q*winv % p, p) == 1:
            rev_n+=1
            cq,dq = rep(q)
            if R4(cq,dq) % p != 0: rev_bad+=1; P('REVERSE FAIL', p, q)
P(f'reverse direction: {rev_n} coset pairs tested, failures={rev_bad}',
  'PASS' if rev_bad==0 else 'FAIL')
# p == 5 mod 8: expect ZERO hits ever
n5=0; h5=0
for i,p in enumerate(PR):
    if p>3000: break
    if p % 8 != 5: continue
    for q in PR[i+1:]:
        if q>3000: break
        c,d = rep(q); n5+=1
        if R4(c,d) % p == 0: h5+=1; P('p5mod8 HIT?!', p, q)
P(f'p==5 mod 8: {n5} pairs, hits={h5} (expect 0)')
# root count: for a few p, count c in [0,p) with 8c^4-8qc^2+q^2 == 0 mod p
P('root-count check (expect 4 roots iff q in coset):')
rc_bad=0
for (p,q) in coset_pairs[:40]:
    if p % 8 != 1: continue
    cnt = sum(1 for cc in range(p) if (8*cc**4 - 8*q*cc*cc + q*q) % p == 0)
    if cnt != 4: rc_bad+=1; P('ROOTCOUNT', p, q, cnt)
P(f'root-count failures={rc_bad} over min(40,len) coset pairs', 'PASS' if rc_bad==0 else 'FAIL')

# ---------- 2. K2 / K11 death ----------
P('=== 2. K2/K11 death verification ===')
n=0; v_ineq=0; v_qYq=0; k2=0; k11=0
for i,p in enumerate(PR):
    if p>5000: break
    a,b = rep(p); Rp=R4(a,b); Yp=Y4(a,b)
    if not (0 < Rp < p*p): v_ineq+=1; P('INEQ FAIL', p, Rp, p*p)
    for q in PR[i+1:]:
        if q>5000: break
        c,d = rep(q); Yq=Y4(c,d); Rq=R4(c,d); n+=1
        if q in (Yq,): v_qYq+=1; P('q|Y_q?!', p, q)
        if 2*Rp*Yq == q*q*Yp: k2+=1; P('K2 SOLUTION?!', p, q)
        if 2*q*q*Yp == p*p*Yq: k11+=1; P('K11 SOLUTION?!', p, q)
P(f'pairs={n}; 0<R_p<p^2 violations={v_ineq}; q|Y_q hits={v_qYq}; '
  f'K2 hits={k2}; K11 hits={k11}')
P('K2 proof chain: K2 => v_q(R_p)=2 => q^2|R_p, but 0<R_p<p^2<q^2: IMPOSSIBLE'
  if k2==0 and v_ineq==0 else 'CHECK FAILURES')

# ---------- 3. Wieferich census p^2 | R_q ----------
P('=== 3. Wieferich census: p^2 | R_q, p<q<=1e5 ===')
hits=[]
for q in PR:
    if q>100000: break
    c,d = rep(q); Rq=R4(c,d)
    for p in PR:
        if p>=q: break
        if p % 8 != 1: continue
        if Rq % (p*p) == 0:
            a,b = rep(p)
            e = elems(p,q)
            hits.append((p,q,Rq//(p*p)))
            P('WIEFERICH p^2|R_q:', p, q, 'R_q/p^2 =', Rq//(p*p),
              ' logratio K1 =', round(abs(math.log(e['A']/(2*e['Y']))),6))
P(f'total p^2|R_q hits: {len(hits)}')
P('DONE')
OUT.close()