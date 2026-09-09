from fractions import Fraction as F
import math

# m=10 admissible point: test the layer-1 lift condition exactly.
A2, A4 = 32, 238
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2) = P,Q
    if x1==x2 and (y1+y2)==0: return None
    if P==Q or (x1==x2 and y1==y2):
        lam = (3*x1*x1 + 2*A2*x1 + A4)/(2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    x3 = lam*lam - A2 - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3,y3)
def mul(P,n):
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q)
        Q=add(Q,Q); n>>=1
    return R
T=(F(0),F(0)); Pa=(F(-14),F(14))
def issq(n):
    if n<0: return False
    r=math.isqrt(n); return r*r==n

for m in (10, 12, 14, 16, 6, 4):
    Q = mul(Pa, 2*m); PT = add(Q,T)
    if PT is None: continue
    X2 = PT[0]/238
    if X2 <= 0: continue
    nr,dr = X2.numerator, X2.denominator
    rn,rd = math.isqrt(nr), math.isqrt(dr)
    if rn*rn!=nr or rd*rd!=dr: continue
    r,s = rn,rd
    g = math.gcd(r,s); r//=g; s//=g
    if not (r%6==0 and s%2==1 and s**4 > 238*r**4): continue
    u = math.isqrt(238*r**4 + 32*r*r*s*s + s**4)
    s2p = s*s + 16*r*r
    Fm, Fp = s2p - u, s2p + u
    h2, hp = Fm//2, Fp//2
    ok = None
    for c1 in (72, 1):   # even m: h2 = 72*rho^4 (observed), hp = sigma^4
        if h2 % c1 == 0:
            q1 = h2//c1
            if issq(q1) and issq(math.isqrt(q1)):
                rho = math.isqrt(math.isqrt(q1))
                c2 = 72//c1
                if hp % c2 == 0:
                    q2 = hp//c2
                    if issq(q2) and issq(math.isqrt(q2)):
                        sigma = math.isqrt(math.isqrt(q2))
                        ok = (c1, rho, c2, sigma)
                        break
    if not ok: 
        print(f"m={m}: no clean split"); continue
    c1, rho, c2, sigma = ok
    n = s**4 - 238*r**4
    prod = rho*sigma
    l1 = issq(s + 2*prod)
    l2 = issq(s - 2*prod)
    print(f"m={m}: n'=s mod4={s%4}, |2 rho sigma| vs s: 2rho sigma = {str(2*prod)[:20]}... s = {str(s)[:20]}")
    print(f"      lift: s+2rho*sigma square? {l1}   s-2rho*sigma square? {l2}"
          + (f"  (s+2rs = {math.isqrt(s+2*prod)}, s-2rho*sigma = {math.isqrt(s-2*prod)})" if l1 and l2 else ""))
    # also verify the regenerated layer-1 quartic membership exactly:
    uu, vv = sigma, rho
    v1 = uu**4 - 64*uu*uu*vv*vv + 72*vv**4
    print(f"      (1,72) check: s^2 == u^4-64u^2v^2+72v^4? {s*s == v1}")
    v2 = uu**4*72 - 64*uu*uu*vv*vv + vv**4 if False else 72*uu**4 - 64*uu*uu*vv*vv + vv**4
    print(f"      (72,1) check (u,v swapped roles): {vv*vv == 72*vv**4 - 64*uu*uu*vv*vv + uu**4}" if False else f"      (72,1) mirror: s^2 == 72u^4-64u^2v^2+v^4? {s*s == v2}")