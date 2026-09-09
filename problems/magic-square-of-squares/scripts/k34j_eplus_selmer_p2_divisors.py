#!/usr/bin/env python3
# Sel(phi') FINAL — E': y^2 = x^3 + ap x^2 + bp x, ap = -4t+4, bp = -2032-8t
# (bp = -8*(254+t), Norm = 2^6*17*37*103).
# Candidates: elements d with (d) | (bp), modulo squares, i.e. classes
# prod P^{f_P} principal + unit sign. Compute the exact element-divisors of
# (bp), run the v6 local tests for C'_d: d W^2 = d^2 Z^4 + ap d Z^2 + bp.
# GATE deliverable: dim Sel(phi') <= 1 => rank E+(L) <= 1.
from sage.all import *
import itertools, time, sys
sys.set_int_max_str_digits(100000)
L = QuadraticField(-271, 't'); t = L.gen()
ap = -4*t + 4
bp = L(-2032) - 8*t
assert ap == -2*(2*t-2)
E_check = (2*t-2)**2 - 4*L(238)
assert bp == E_check, f"bp mismatch: {bp} vs {E_check}"

Ibp = L.ideal(bp)
fac = Ibp.factor()
print("(bp) =", fac, flush=True)
# element divisors: d with (d) = prod P^{f_P} principal:
# find elements generating each principal product:
def element_divisors(I):
    """All d up to ±, t-powers with (d) | I exactly (exponents 0/1 on primes)."""
    fac = I.factor()
    primes = [P for P, e in fac]
    exps = [e for P, e in fac]
    out = []
    for fs in itertools.product(*[range(1) for _ in primes]):  # f in {0}: only squarefree? No:
        pass
    # divisors with f_P in {0..e_P} but mod 2 for classes: d's class in L*/L*2:
    # (d) = prod P^{f_P}: f_P can be 0..e_P but parity matters for the class;
    # the covering candidates: d with (d) | (bp): v_P(d) <= v_P(bp) for all P,
    # and d defined up to squares: classes c = d mod squares with (c) | (bp):
    # parity vectors f in prod {0..e_P} — but L*/L*2 classes of ELEMENTS:
    # c = ± 2^a 7^b 17^c t^e... no wait: elements dividing (bp) need not be
    # rational! e.g. the prime element over 37 with Norm 37 (if principal).
    # h(L) = 11: P37 principal iff P37^11 principal only => P37 NOT principal
    # => no element of norm 37. Element divisors of (bp): products prod P^{f_P}
    # that are principal. Enumerate f_P in prod {0..e_P}, test principality
    # via the class group, extract a generator element.
    results = []
    ranges = [range(0, e+1) for e in exps]
    Cl = L.class_group()
    for fs in itertools.product(*ranges):
        J = prod([P**f for P, f in zip(primes, fs)], L.ideal(1))
        if J == L.ideal(1):
            results.append((fs, L(1)))
            continue
        try:
            jc = J.ideal_class()
            if jc.is_one():
                g = J.gens_reduced()
                # J principal: generator
                gen = None
                for x in J.gens_reduced():
                    if L.ideal(x) == J:
                        gen = x; break
                if gen is None:
                    # search small generator
                    for k in range(1, 500):
                        for coefs in itertools.product(range(-k, k+1), repeat=2):
                            el = coefs[0] + coefs[1]*t
                            if L.ideal(el) == J:
                                gen = el; break
                        if gen is not None: break
                results.append((fs, gen))
        except Exception as e:
            pass
    return results

t0 = time.time()
divs = element_divisors(Ibp)
print("element-divisor count (ideal classes):", len(divs), flush=True)
for fs, gen in divs:
    print("  exponents:", fs, "gen:", gen, flush=True)
print("elapsed:", round(time.time()-t0,1), "s", flush=True)
print("DONE", flush=True)