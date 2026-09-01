"""Two-prime (omega_1 = 2) structure: closed form for D((pq)^2) and census.

For w = pq (p, q distinct primes 1 mod 4), reps of p^2 q^2 give
|D((pq)^2)| = ((2*1+1)(2*1+1) - 1)/2 = 4, with closed form
    D((pq)^2) = { p^2*Y_q, q^2*Y_p, |Im((pi*rho)^4)|, |Im(pi_bar^4 rho^4)| }
where pi = a+bi (a^2+b^2=p), rho = c+di (c^2+d^2=q), Y_p = Im(pi^4) =
4ab(a^2-b^2).  (Derivation: zeta = z^2 for the 9 reps z = pi^j pi_bar^{2-j}
rho^a rho_bar^{2-a}; j in {0,1,2} gives zeta-factor in
{pi_bar^4, p^2, pi^4} x {rho_bar^4, q^2, rho^4}; Im(p^2 q^2) = 0 trivial;
conjugate pairing collapses 9 -> 4.)

This script: (1) verifies the closed form against the general builder;
(2) census: sum-freeness / AP / parallelogram for all p < q <= 3000;
(3) p-valuation profile of the four elements (tests what survives of the
prime-power argument).
"""
import math

def reprs2(n):
    """All (a,b), a>=b>=0, a^2+b^2=n."""
    out = []
    for a in range(int(math.isqrt(n)) + 1):
        b2 = n - a * a
        b = math.isqrt(b2)
        if b >= 0 and a * a + b * b == n:
            out.append((a, b))
    return out

def Y4(a, b):
    """|Im((a+bi)^4)| = |4ab(a^2-b^2)|."""
    return abs(4 * a * b * (a * a - b * b))

def im_prod4(u, v):
    """|Im((u*v)^4)| where u=(a,b), v=(c,d) gaussian ints."""
    x = u[0] * v[0] - u[1] * v[1]
    y = u[0] * v[1] + u[1] * v[0]
    return abs(4 * x * y * (x * x - y * y))

def im_cross4(u, v):
    """|Im((u_bar*v)^4)| = |Im((conj(u)*v)^4)|."""
    ub = (u[0], -u[1])
    x = ub[0] * v[0] - ub[1] * v[1]
    y = ub[0] * v[1] + ub[1] * v[0]
    return abs(4 * x * y * (x * x - y * y))

def d_pq_closed(p, q):
    ap, bp = reprs2(p)[1]        # nontrivial rep (a>b>0) for p 1 mod 4
    aq, bq = reprs2(q)[1]
    return sorted({p * p * Y4(aq, bq),
                   q * q * Y4(ap, bp),
                   im_prod4((ap, bp), (aq, bq)),
                   im_cross4((ap, bp), (aq, bq))})

def dset_general(w):
    ds = set()
    for m in range(2, int(math.isqrt(w)) + 1):
        mm = m * m
        for n in range(1, m):
            s = mm + n * n
            if s > w:
                break
            if w % s:
                continue
            d0 = 2 * (mm - n * n) * (2 * m * n)
            k = w // s
            ds.add(d0 * k * k)
    return sorted(ds)

# self-test: closed form == general builder for several w = p*q
for (p, q) in [(5, 13), (5, 17), (13, 17), (5, 29), (17, 41)]:
    dc = d_pq_closed(p, q)
    dg = dset_general(p * q)
    assert dc == dg, (p, q, dc, dg)
print("self-test PASS: closed form == general builder for 5 pairs (w=pq)")

PRIMES = [p for p in range(5, 3001, 4) if all(p % r for r in range(3, int(p ** .5) + 1, 2))]
print(f"primes 1 mod 4 up to 3000: {len(PRIMES)}")

A2 = A3 = AP = 0
tested = 0
val_profiles = {}
for i in range(len(PRIMES)):
    p = PRIMES[i]
    for j in range(i + 1, len(PRIMES)):
        q = PRIMES[j]
        ds = d_pq_closed(p, q)
        tested += 1
        dset_ = set(ds)
        L = len(ds)
        for a in range(L):
            for b in range(a + 1, L):
                x, y = ds[a], ds[b]
                if (x + y) in dset_:
                    A2 += 1; print("A2 HIT", p, q, x, y, x + y)
                if (y - x) in dset_:
                    AP += 1; print("AP HIT", p, q, x, y)
                    if (x + y) in dset_:
                        A3 += 1; print("A3 HIT (parallelogram!)", p, q, x, y)
print(f"w=pq pairs tested: {tested}")
print(f"A2={A2}, A3={A3}, AP={AP}")

# valuation profile at p for a few w=pq: how many elements share v_p?
print("\nv_p profiles (elements mod p-adic valuation):")
for (p, q) in [(5, 13), (5, 17), (13, 17), (5, 41)]:
    ds = d_pq_closed(p, q)
    prof = []
    for d in ds:
        v = 0
        t = d
        while t % p == 0:
            v += 1; t //= p
        prof.append(v)
    print(f"  p={p}, q={q}: v_p = {sorted(prof)}  (distinct: {len(set(prof))} of {len(ds)})")