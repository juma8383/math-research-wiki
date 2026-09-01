from fractions import Fraction
from math import prod
small = [3,11,13,17,19,23,29,31,37]
pi_small = prod(Fraction(p+1,p) for p in small)
iv_small = sum(Fraction(1,p-1) for p in small)
print("prod(1+1/p) over 9 small =", pi_small, "=", float(pi_small))
print("sum 1/(p-1) over 9 small =", float(iv_small), "> log2:", iv_small > Fraction(6931471805599453094172321,10**25))
# window (i) with extra prime P: pi_small*(1+1/P) < 2  <=>  P > pi_small/(2-pi_small)
lim = pi_small/(2-pi_small)
print("window (i) holds iff P >", float(lim))
# check a concrete P
for P in (953, 997):
    pi = pi_small*Fraction(P+1,P)
    print("P=%d: prod=%s <2: %s" % (P, pi, pi < 2))
