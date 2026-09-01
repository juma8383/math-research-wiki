"""Per-prime admissibility sieve for K10, K12-K16 over all 1 mod 4 primes<=3e5.

For each prime p: v=u_p, P=|v^2-4|; for every piece of every equation,
quadratic in w=u_q: (disc square? -> root in region? -> U^2+4 rational square?
-> x_q=(U+z)/2=m/n -> q=m^2+n^2 prime? -> EXACT integer verification of the
kill equation for the pair (p,q)). Counts each stage per equation.

ASCII only, flush=True everywhere.
"""
from fractions import Fraction
import math, sys
sys.path.insert(0, r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts')
from mss_two_prime_k10_16_sieve import (primes1mod4, stu, predict_roots,
                                        admissible, PIECES, P)

# reuse module's log file? No: sieve module already closed its log. Open ours.
OUT = open(r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_two_prime_k10_16_sieve3e5.log', 'a', encoding='utf-8')
def Q(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); OUT.write(s + '\n'); OUT.flush()

Q('=== 2. per-prime sieve, all 1 mod 4 primes <= 3e5 ===')
BOUND = 300000
PR = primes1mod4(BOUND)
Q('primes:', len(PR))

stats = {k: {'disc':0,'region':0,'adm':0,'prime':0,'verified':0} for k in PIECES}
hits = []
for idx, p in enumerate(PR):
    sp, tp, v = stu(p)
    preds = predict_roots(v)
    for k in PIECES:
        for w in preds[k]:
            stats[k]['region'] += 1
            mn = admissible(w)
            if mn is None: continue
            stats[k]['adm'] += 1
            m, n = mn
            q = m*m + n*n
            if q % 2 == 0 or not is_probable_prime(q):
                continue
            stats[k]['prime'] += 1
            # exact integer verification for pair (p,q)
            sp2, tp2, _ = stu(p); sq2, tq2, _ = stu(q)
            Yp, Yq = 4*sp2*tp2, 4*sq2*tq2
            Rp, Rq = abs(sp2*sp2-4*tp2*tp2), abs(sq2*sq2-4*tq2*tq2)
            A, B = p*p*Yq, q*q*Yp
            X, Y = Rp*Yq, Yp*Rq
            C, D0 = abs(X-Y), X+Y
            rel = {'K10': 2*A==D0, 'K12': 2*B==D0, 'K13': 2*C==A,
                   'K14': 2*C==B, 'K15': 2*D0==A, 'K16': 2*D0==B}
            if rel[k]:
                stats[k]['verified'] += 1
                hits.append((k,p,q))
                Q('FULL HIT', k, p, q)
    if (idx+1) % 2000 == 0:
        Q('progress', idx+1, {k: stats[k] for k in stats})

Q('sieve complete. stats:')
for k in PIECES:
    Q(' ', k, stats[k])
Q('total fully-verified hits:', len(hits))
Q('DONE')
OUT.close()