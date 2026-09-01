"""Numerical verification of the gate lemmas used in the K1/K10/K12 kills.

G_K1(n):  p^4 + 4 Y_p^2 = square      (K1 necessary condition) -- proved impossible
G_K12(n): R_p^2 - 3 Y_p^2 = square    (K12 necessary condition) -- proved impossible
G3(n):    s^4 + 4 s^2 t^2 + 16 t^4 = square   (K14/K16 gate on n)
          mod-9 lemma: G3(n) requires 3 | s_n (equivalently n = 2 mod 3)
D1a(n):   p^2 + 32 t^2 = square  (K13/K15 gate, branch-dependent)
D1b(n):   9 p^2 - 32 t^2 = square
D2(n):    9 s^2 + 64 t^2 = square
Also verifies R^2 + Y^2 = p^4 exactly for all primes tested.

ASCII only, flush=True.
"""
import sys, math
sys.path.insert(0, r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts')
from mss_two_prime_k10_16_sieve import primes1mod4, stu

OUT = open(r'C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_two_prime_k1_k12_gates.log', 'w', encoding='utf-8')
def Q(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); OUT.write(s + '\n'); OUT.flush()

def sq(n):
    if n < 0: return False
    r = math.isqrt(n); return r*r == n

BOUND = 100000
PR = primes1mod4(BOUND)
Q('=== gate lemma verification, primes <=', BOUND, '===')
cnt = {'G_K1':0,'G_K12':0,'G3':0,'D1a':0,'D1b':0,'D2':0}
rybad = 0; g3mod9bad = 0; g3tested = 0; mod3agree = 0; mod3bad = 0
for p in PR:
    s, t, v = stu(p)
    Y = 4*s*t; R = abs(s*s-4*t*t)
    if R*R + Y*Y != p**4: rybad += 1
    if sq(p**4 + 4*Y*Y): cnt['G_K1'] += 1; Q('G_K1 HIT', p)
    if sq(R*R - 3*Y*Y): cnt['G_K12'] += 1; Q('G_K12 HIT', p)
    if sq(s**4 + 4*s*s*t*t + 16*t**4): cnt['G3'] += 1; Q('G3 HIT', p)
    if sq(p*p + 32*t*t): cnt['D1a'] += 1; Q('D1a HIT', p)
    if sq(9*p*p - 32*t*t): cnt['D1b'] += 1; Q('D1b HIT', p)
    if sq(9*s*s + 64*t*t): cnt['D2'] += 1; Q('D2 HIT', p)
    # mod-9 lemma: 3|s <=> p==2 mod 3 ; G3 value ≡ 3 mod 9 when 3∤st
    if (s % 3 == 0) != (p % 3 == 2): mod3bad += 1
    else: mod3agree += 1
    if s % 3 and t % 3:
        g3tested += 1
        if (s**4 + 4*s*s*t*t + 16*t**4) % 9 != 3: g3mod9bad += 1
Q('R^2+Y^2=p^4 violations:', rybad)
Q('3|s <=> p=2 mod 3: agree', mod3agree, 'bad', mod3bad)
Q('G3 mod-9 check (3∤st): tested', g3tested, 'bad', g3mod9bad)
Q('gate hits:', cnt)
Q('DONE')
OUT.close()