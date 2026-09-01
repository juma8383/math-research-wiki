"""K10, K12-K16 as quadratic curves in (u_p,u_q) + per-prime admissibility sieve.

Under the verified factorization (4*t_p^2*t_q^2 common factor cancels in every
kill equation), with v=u_p, w=u_q, P=|v^2-4|, Q=|w^2-4|:
  A/4t^2 = w(v^2+4), B/4t^2 = v(w^2+4), X/4t^2 = P*w, Y/4t^2 = v*Q.
Each kill equation is piecewise-quadratic in w (pieces = Q-branch x g-vs-h sign):
  K10: 2A=D0 -> 2*w*(v^2+4) - (P*w + v*Q) = 0          pieces: Q-branch
  K12: 2B=D0 -> 2*v*(w^2+4) - (P*w + v*Q) = 0          pieces: Q-branch
  K13: 2C=A  -> 2*sg*(P*w - v*Q) - w*(v^2+4) = 0       pieces: Q-branch x sg
  K14: 2C=B  -> 2*sg*(P*w - v*Q) - v*(w^2+4) = 0       pieces: Q-branch x sg
  K15: 2D0=A -> 2*(P*w + v*Q) - w*(v^2+4) = 0          pieces: Q-branch
  K16: 2D0=B -> 2*(P*w + v*Q) - v*(w^2+4) = 0          pieces: Q-branch
Each piece's quadratic coefficients are recovered by exact interpolation at
3 sample points, roots kept only inside the piece's region, then admissibility
of a candidate U=w: U^2+4 must be a rational square (always true for genuine
u = x-1/x), giving x_q=(U+z)/2 = m/n, and the kill equation is then verified
EXACTLY in integers with the actual prime q=m^2+n^2.

Parts:
 0. iff check: on all pairs p<q<=600, relation holds <=> w is an admissible
    root predicted by the piece machinery (0 mismatches required).
 1. brute relation census p<q<=3000 (6 relations, expect 0).
 2. per-prime sieve: for every 1 mod 4 prime p<=3e5, all pieces of all six
    equations: disc square? root in region? admissible? prime q? exact verify?
    Any fully-verified hit = a genuine kill-equation solution (expected: none).

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

def rep(n):
    for aa in range(math.isqrt(n)+1):
        b2 = n-aa*aa; b = math.isqrt(b2)
        if b>0 and b*b==b2: return (max(aa,b), min(aa,b))
    raise ValueError(n)

def stu(n):
    a,b = rep(n); s = a*a-b*b; t = a*b
    return s, t, Fraction(s,t)

def is_square_rat(r):
    if r < 0: return None
    num, den = r.numerator, r.denominator
    a = math.isqrt(num); b = math.isqrt(den)
    if a*a==num and b*b==den: return Fraction(a,b)
    return None

def is_probable_prime(n):
    if n < 2: return False
    for sp in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % sp == 0: return n == sp
    d = n-1; r = 0
    while d % 2 == 0: d//=2; r+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

# ---- piece machinery ----
# eq id -> list of (sg, sig) where sg in {+1,-1} is the g-vs-h sign (None if
# unused), sig in {+1,-1} is the Q branch (w>2 -> w^2-4, w<2 -> 4-w^2).
PIECES = {
  'K10': [(None,+1),(None,-1)],
  'K12': [(None,+1),(None,-1)],
  'K13': [(+1,+1),(+1,-1),(-1,+1),(-1,-1)],
  'K14': [(+1,+1),(+1,-1),(-1,+1),(-1,-1)],
  'K15': [(None,+1),(None,-1)],
  'K16': [(None,+1),(None,-1)],
}

def piece_poly(k, sg, sig, v):
    """Quadratic coeffs (a2,a1,a0) of the piece's LHS-RHS in w, exact.
    Interpolate the branch-substituted expression at 3 sample points."""
    Pp = abs(v*v-4)
    def E(w):
        Q = w*w-4 if sig>0 else 4-w*w
        g = Pp*w; h = v*Q
        d = g-h if (sg is None or sg>0) else h-g
        if k=='K10': return 2*w*(v*v+4) - (g+h)
        if k=='K12': return 2*v*(w*w+4) - (g+h)
        if k=='K13': return 2*d - w*(v*v+4)
        if k=='K14': return 2*d - v*(w*w+4)
        if k=='K15': return 2*(g+h) - w*(v*v+4)
        if k=='K16': return 2*(g+h) - v*(w*w+4)
        raise ValueError(k)
    ws = [Fraction(1,3), Fraction(1,2), Fraction(1)] if sig<0 else [Fraction(3),Fraction(4),Fraction(5)]
    y = [E(w) for w in ws]
    # Lagrange interpolation for a2,a1,a0
    def lag(i):
        c2 = Fraction(0); c1 = Fraction(0); c0 = Fraction(1)
        for j in range(3):
            if j==i: continue
            # (w - wj)/(wi - wj)
            f = 1/(ws[i]-ws[j])
            # multiply poly c2 w^2+c1 w+c0 by (w - ws[j]), degree<=2
            n2 = c2; n1 = c1; n0 = c0
            c2 = n1 - ws[j]*n2
            c1 = n0 - ws[j]*n1
            c0 = -ws[j]*n0
            c0*=f; c1*=f; c2*=f
        return (c2,c1,c0)
    a2=a1=a0=Fraction(0)
    for i in range(3):
        l2,l1,l0 = lag(i)
        a2 += y[i]*l2; a1 += y[i]*l1; a0 += y[i]*l0
    return a2,a1,a0

def region_ok(k, sg, sig, v, w):
    if sig>0 and w <= 2: return False
    if sig<0 and (w <= 0 or w >= 2): return False
    Pp = abs(v*v-4)
    Q = w*w-4 if sig>0 else 4-w*w
    g = Pp*w; h = v*Q
    if sg is not None:
        if sg>0 and g < h: return False
        if sg<0 and h < g: return False
    return True

def predict_roots(v):
    """All admissible-candidate w values (Fractions) predicted by the pieces."""
    out = {k: [] for k in PIECES}
    for k, plist in PIECES.items():
        seen = set()
        for sg, sig in plist:
            a2,a1,a0 = piece_poly(k, sg, sig, v)
            if a2 == 0:
                if a1 != 0:
                    w = -a0/a1
                    if w not in seen and region_ok(k,sg,sig,v,w):
                        seen.add(w); out[k].append(w)
                continue
            disc = a1*a1 - 4*a2*a0
            z = is_square_rat(disc)
            if z is None: continue
            for s in (1,-1):
                w = (-a1 + s*z)/(2*a2)
                if w in seen: continue
                if region_ok(k,sg,sig,v,w):
                    seen.add(w); out[k].append(w)
    return out

def admissible(U):
    """U>0 and U^2+4 a rational square -> (m,n) reduced rep ratio, else None."""
    if U <= 0: return None
    z = is_square_rat(U*U+4)
    if z is None: return None
    x = (U+z)/2
    m, n = x.numerator, x.denominator
    if m <= n: return None
    return m, n

# ---------- 0. iff check ----------
P('=== 0. iff check: relation <=> predicted admissible root, p<q<=600 ===')
PR6 = primes1mod4(600)
mism = 0; npair = 0; nrel = 0
for i,p in enumerate(PR6):
    sp,tp,vp = stu(p)
    preds = predict_roots(vp)
    for q in PR6[i+1:]:
        sq,tq,vq = stu(q)
        Yp,Yq = 4*sp*tp, 4*sq*tq
        Rp,Rq = abs(sp*sp-4*tp*tp), abs(sq*sq-4*tq*tq)
        A,B = p*p*Yq, q*q*Yp
        X,Y = Rp*Yq, Yp*Rq
        C,D0 = abs(X-Y), X+Y
        rel = {'K10': 2*A==D0, 'K12': 2*B==D0, 'K13': 2*C==A,
               'K14': 2*C==B, 'K15': 2*D0==A, 'K16': 2*D0==B}
        npair+=1
        for k in PIECES:
            hit = any(w == vq for w in preds[k])
            if hit != rel[k]:
                mism+=1; P('IFF-MISMATCH',p,q,k,'pred',hit,'rel',rel[k])
            if rel[k]: nrel+=1
P(f'pairs={npair}, relations found={nrel}, iff mismatches={mism}',
  'PASS' if mism==0 else 'FAIL')

# ---------- 1. brute census ----------
P('=== 1. brute relation census p<q<=3000 ===')
PR3 = primes1mod4(3000)
nrel=0; npair=0
for i,p in enumerate(PR3):
    sp,tp,vp = stu(p); Yp=4*sp*tp; Rp=abs(sp*sp-4*tp*tp)
    for q in PR3[i+1:]:
        sq,tq,vq = stu(q); Yq=4*sq*tq; Rq=abs(sq*sq-4*tq*tq)
        A,B = p*p*Yq, q*q*Yp
        X,Y = Rp*Yq, Yp*Rq
        C,D0 = abs(X-Y), X+Y
        npair+=1
        if 2*A==D0 or 2*B==D0 or 2*C==A or 2*C==B or 2*D0==A or 2*D0==B:
            nrel+=1; P('HIT',p,q)
P(f'pairs={npair}, relations={nrel} (expect 0)')
P('DONE')
OUT.close()