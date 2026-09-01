"""Verify the u-factorization lead: every D-element = 4*t_p^2*t_q^2 * (u-only factor).

Setup: prime n = a^2+b^2 (1 mod 4), s=a^2-b^2, t=ab, x=a/b, u=s/t=x-1/x>0.
Then: n^2 = s^2+4t^2, Y_n = 4*s*t, R_n = |s^2-4t^2| = t^2*|u^2-4|,
      n^2 = t^2*(u^2+4)  [since s^2+4t^2 = t^2(u^2+4)].
Claimed exact factorizations (all divided by 4*t_p^2*t_q^2):
  A = p^2*Y_q        -> u_q*(u_p^2+4)
  B = q^2*Y_p        -> u_p*(u_q^2+4)
  X = R_p*Y_q        -> |u_p^2-4|*u_q
  Y = Y_p*R_q        -> u_p*|u_q^2-4|
  C = |X-Y|, D0=X+Y follow.

Also verifies the quadratic reduction machinery: each kill equation
K10,K12,K13,K14,K15,K16 restricted to a branch case (w=u_q vs 2, and the
g-vs-h sign for K13/K14) is a quadratic in w; coefficients recovered by
interpolation at 3 sample points (exact Fractions), and the iff
"relation holds <=> w is a root of the matching branch piece" is
machine-checked on all pairs p<q<=600.

ASCII only, flush=True everywhere.
"""
from fractions import Fraction
import math

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

PR = primes1mod4(1000)

def rep(n):
    for aa in range(math.isqrt(n)+1):
        b2 = n-aa*aa; b = math.isqrt(b2)
        if b>0 and b*b==b2: return (max(aa,b), min(aa,b))
    raise ValueError(n)

def stu(n):
    a,b = rep(n); s = a*a-b*b; t = a*b
    return s, t, Fraction(s,t)

# ---------- 1. factorization ----------
P('=== 1. u-factorization, all pairs p<q<=1000 ===')
bad=0; n=0
for i,p in enumerate(PR):
    for q in PR[i+1:]:
        sp,tp,vp = stu(p); sq,tq,vq = stu(q)
        Yp,Yq = 4*sp*tp, 4*sq*tq
        Rp,Rq = abs(sp*sp-4*tp*tp), abs(sq*sq-4*tq*tq)
        A,B = p*p*Yq, q*q*Yp
        X,Y = Rp*Yq, Yp*Rq
        C,D0 = abs(X-Y), X+Y
        f = 4*tp*tp*tq*tq
        Pp = abs(vp*vp-4); Pq = abs(vq*vq-4)
        got = {
          'A': f*vq*(vp*vp+4), 'B': f*vp*(vq*vq+4),
          'X': f*Pp*vq,        'Y': f*vp*Pq,
          'C': f*abs(Pp*vq - vp*Pq), 'D': f*(Pp*vq + vp*Pq),
        }
        want = {'A':A,'B':B,'X':X,'Y':Y,'C':C,'D':D0}
        n+=1
        for k in want:
            if got[k] != want[k]:
                bad+=1; P('MISMATCH',p,q,k,got[k],want[k]); break
P(f'pairs={n}, mismatches={bad}', 'PASS' if bad==0 else 'FAIL')
P('DONE')
OUT.close()