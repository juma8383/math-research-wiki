"""Closed forms for the 16 piece quadratics of K10,K12-K16, machine-checked.

With v=u_p, w=u_q, P=|v^2-4|, Q=|w^2-4|, and the u-factorization
A:f=w(v^2+4), B:f=v(w^2+4), X:f=P*w, Y:f=v*Q (f=4 t_p^2 t_q^2):
each kill equation on each branch piece (sig=Q-branch, sg=g-vs-h sign)
is the quadratic (a2,a1,a0) below; checked == interpolation machinery
for all 1 mod 4 primes <= 2000. ASCII only.
"""
import sys
from fractions import Fraction
sys.path.insert(0, r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts')
from mss_two_prime_k10_16_sieve import primes1mod4, stu, piece_poly, P

T = {
 ('K10',None,1):  lambda v,Pp: (-v, 2*(v*v+4)-Pp, 4*v),
 ('K10',None,-1): lambda v,Pp: (v, 2*(v*v+4)-Pp, -4*v),
 ('K12',None,1):  lambda v,Pp: (v, -Pp, 12*v),
 ('K12',None,-1): lambda v,Pp: (3*v, -Pp, 4*v),
 ('K13',1,1):  lambda v,Pp: (-2*v, 2*Pp-v*v-4, 8*v),
 ('K13',-1,1): lambda v,Pp: (2*v, -2*Pp-v*v-4, -8*v),
 ('K13',1,-1): lambda v,Pp: (2*v, 2*Pp-v*v-4, -8*v),
 ('K13',-1,-1):lambda v,Pp: (-2*v, -2*Pp-v*v-4, 8*v),
 ('K14',1,1):  lambda v,Pp: (-3*v, 2*Pp, 4*v),
 ('K14',-1,1): lambda v,Pp: (v, -2*Pp, -12*v),
 ('K14',1,-1): lambda v,Pp: (v, 2*Pp, -12*v),
 ('K14',-1,-1):lambda v,Pp: (-3*v, -2*Pp, 4*v),
 ('K15',None,1):  lambda v,Pp: (2*v, 2*Pp-v*v-4, -8*v),
 ('K15',None,-1): lambda v,Pp: (-2*v, 2*Pp-v*v-4, 8*v),
 ('K16',None,1):  lambda v,Pp: (v, 2*Pp, -12*v),
 ('K16',None,-1): lambda v,Pp: (-3*v, 2*Pp, 4*v),
}

OUT = open(r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_two_prime_k10_16_closedforms.log', 'w', encoding='utf-8')
def Q(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); OUT.write(s + '\n'); OUT.flush()

Q('=== closed-form piece quadratics vs interpolation, primes <= 2000 ===')
def norm(c):
    a2, a1, a0 = c
    return (a1/a2, a0/a2)
bad = 0; n = 0
for p in primes1mod4(2000):
    s, t, v = stu(p)
    Pp = abs(v*v-4)
    for (k, sg, sig), f in T.items():
        want = norm(f(v, Pp))
        got = norm(piece_poly(k, sg, sig, v))
        n += 1
        if got != want:
            bad += 1
            if bad < 5: Q('MISMATCH', p, k, sg, sig, got, want)
Q(f'checks={n}, mismatches={bad}', 'PASS' if bad == 0 else 'FAIL')
Q('DONE')
OUT.close()