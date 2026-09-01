"""Disc-square census: for each 1 mod 4 prime p<=3e5 and each of the 16 piece
quadratics of K10,K12-K16 (closed forms), is disc = a1^2-4*a2*a0 a rational
square? Also, for pieces with square disc, extract region-valid roots and test
admissibility (U^2+4 rational square) + prime q. Independent of the
interpolation machinery (uses the verified closed-form table directly).

ASCII only, flush=True.
"""
import sys
from fractions import Fraction
import math
sys.path.insert(0, r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts')
from mss_two_prime_k10_16_closedforms import T
from mss_two_prime_k10_16_sieve import primes1mod4, stu, is_square_rat, \
    is_probable_prime, admissible, PIECES

OUT = open(r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_two_prime_k10_16_discsq.log', 'w', encoding='utf-8')
def Q(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); OUT.write(s + '\n'); OUT.flush()

def region_ok(k, sg, sig, v, w):
    if sig > 0 and w <= 2: return False
    if sig < 0 and (w <= 0 or w >= 2): return False
    Pp = abs(v*v-4)
    Qq = w*w-4 if sig > 0 else 4-w*w
    g = Pp*w; h = v*Qq
    if sg is not None:
        if sg > 0 and g < h: return False
        if sg < 0 and h < g: return False
    return True

Q('=== disc-square census, primes <= 3e5, 16 closed-form pieces + K1 ===')
# K1: p^2 Y_q = 2 Y_p R_q  <=>  w(v^2+4) = 2 v Q  (X<Y side: h>g region)
K1PIECES = [  # (sg,sig, coeffs f(v,Pp)) ; K1 = w(v^2+4) - 2 v Q = 0
 (None, 1, lambda v,Pp: (-2*v, v*v+4, 8*v)),
 (None,-1, lambda v,Pp: ( 2*v, v*v+4, -8*v)),
]
def k1_region_ok(sig, v, w):
    # K1's equation p^2 Y_q = 2 Y_p R_q has NO g-vs-h sign constraint
    # (it appears in the case tree under both sign cases), so only the
    # w-branch (which defines Q) constrains w.
    if sig > 0 and w <= 2: return False
    if sig < 0 and (w <= 0 or w >= 2): return False
    return True

stats = {k: {'discsq':0,'roots':0,'adm':0,'prime':0,'verified':0}
         for k in list(PIECES) + ['K1']}
BOUND = 300000
PR = primes1mod4(BOUND)
Q('primes:', len(PR))
hits = []
for idx, p in enumerate(PR):
    s, t, v = stu(p)
    Pp = abs(v*v-4)
    for (k, sg, sig), f in T.items():
        a2, a1, a0 = f(v, Pp)
        disc = a1*a1 - 4*a2*a0
        z = is_square_rat(disc)
        if z is None: continue
        stats[k]['discsq'] += 1
        for sgn in (1, -1):
            w = (-a1 + sgn*z) / (2*a2)
            if not region_ok(k, sg, sig, v, w): continue
            stats[k]['roots'] += 1
            mn = admissible(w)
            if mn is None: continue
            stats[k]['adm'] += 1
            m, n = mn
            q = m*m + n*n
            if q % 2 == 0 or not is_probable_prime(q): continue
            stats[k]['prime'] += 1
            # exact integer verification
            sp, tp, _ = stu(p); sq, tq, _ = stu(q)
            Yp, Yq = 4*sp*tp, 4*sq*tq
            Rp, Rq = abs(sp*sp-4*tp*tp), abs(sq*sq-4*tq*tq)
            A, B = p*p*Yq, q*q*Yp
            X, Y = Rp*Yq, Yp*Rq
            C, D0 = abs(X-Y), X+Y
            rel = {'K10': 2*A==D0, 'K12': 2*B==D0, 'K13': 2*C==A,
                   'K14': 2*C==B, 'K15': 2*D0==A, 'K16': 2*D0==B}
            if rel[k]:
                stats[k]['verified'] += 1
                hits.append((k, p, q, str(w)))
                Q('FULL HIT', k, p, q, 'w=', str(w))
    # K1 pieces (gated by region h>g)
    for sg_, sig_, f1 in K1PIECES:
        a2, a1, a0 = f1(v, Pp)
        disc = a1*a1 - 4*a2*a0
        z = is_square_rat(disc)
        if z is None: continue
        stats['K1']['discsq'] += 1
        for sgn in (1, -1):
            w = (-a1 + sgn*z) / (2*a2)
            if not k1_region_ok(sig_, v, w): continue
            stats['K1']['roots'] += 1
            mn = admissible(w)
            if mn is None: continue
            stats['K1']['adm'] += 1
            m, n = mn
            q = m*m + n*n
            if q % 2 == 0 or not is_probable_prime(q): continue
            stats['K1']['prime'] += 1
            sp2, tp2, _ = stu(p); sq2, tq2, _ = stu(q)
            Yp2, Yq2 = 4*sp2*tp2, 4*sq2*tq2
            Rp2, Rq2 = abs(sp2*sp2-4*tp2*tp2), abs(sq2*sq2-4*tq2*tq2)
            if p*p*Yq2 == 2*Yp2*Rq2:
                stats['K1']['verified'] += 1
                hits.append(('K1', p, q, str(w)))
                Q('FULL HIT', 'K1', p, q, 'w=', str(w))
    if (idx+1) % 2000 == 0:
        Q('progress', idx+1, {k: dict(stats[k]) for k in stats})

Q('census complete:')
for k in list(PIECES) + ['K1']:
    Q(' ', k, stats[k])
Q('total fully-verified hits:', len(hits))
Q('DONE')
OUT.close()