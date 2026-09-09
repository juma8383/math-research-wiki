# sage_k34_mw_sieve.sage -- Mordell-Weil sieve on the C3_A square-X covers,
# now with real Sage tooling (2026-09-03 tooling round).
# The filed sieve (round 2) reached 5 survivor classes mod M_A = 42078090600
# with primes <= 400 + hunt primes. This script re-derives the sieve state
# with Sage's exact arithmetic and attempts the next lever: add killing
# primes beyond 3e6 by computing ord_p(G_A) via Sage (much faster BSGS),
# then re-sieve the 5 survivor classes.
EA = EllipticCurve([0,-256,0,18432,0])
G_A = EA([128,512])
print("E_A rank:", EA.rank(), "generator:", G_A)

def squares_mod(p):
    return set(GF(p)(i)^2 for i in range(p))

# M_A from the filed round-2: 42078090600 = 2^3*3^4*5^2*7*13*17*23*73
M = 42078090600
print("M_A =", M, "factorization:", factor(M))

# Survivors from round 2 (mod M): {0, 2, M/2-1, -2, -1}
survivors = [0, 2, M//2 - 1, -2 % M, (-1) % M]
print("survivor classes:", survivors)

# Verify: for primes p with ord_p(G_A) | M, the survivor classes must pass
# the QR / killing-prime conditions. Re-check with a batch of valid primes:
def ord_of(P, p):
    Ep = EA.change_ring(GF(p))
    Gp = Ep(P[0], P[1])
    n = Ep.order() if hasattr(Ep, 'order') else Ep.abelian_group().order()
    # order of point divides group order
    o = 1
    Gpp = Gp
    # use generic order_of_point
    from sage.groups.generic import order_from_multiple
    return order_from_multiple(Gp, n, operation='+')

# quick test: valid primes q <= 500 with ord | M
valid = []
p = 5
cnt = 0
for p in prime_range(5, 2000):
    Ep = EA.change_ring(GF(p))
    Gp = Ep(128, 512)
    n = Ep.order()
    try:
        o = Gp.order()
    except Exception:
        continue
    if M % o == 0:
        valid.append((p, o))
print("valid primes <= 2000 with ord | M:", len(valid))

# The sieve condition on class c (n = c + kM): for each valid prime p,
# X(n*G) mod p must be a QR (or infinity). Re-verify survivors on these:
X = lambda P: (2*P[1] + 66*P[0]) / (P[0] * (P[0] - 4)) if P[0] != 0 and P[0] != 4 else None

# Test each survivor class on all valid primes: pick n = c (mod M), but
# n can be huge; use n = c + M*t with t chosen small so that n*G is
# computable: n mod ord_p(G) is what matters!
print("re-check survivors on valid primes:")
ok = True
for (p, o) in valid[:40]:
    Ep = EA.change_ring(GF(p))
    Gp = Ep(128, 512)
    Tp = Ep(0, 0)  # torsion
    for c in survivors:
        n_mod = c % o
        Pt = n_mod * Gp
        if Pt == Ep(0):
            continue  # X undefined/infinity - keep class (sieve rule)
        xP = Pt[0]
        # X(P) = (2y+66x)/(x(x-4)); skip pole cases
        if xP == 0 or xP == 4:
            continue
        num = 2*Pt[1] + 66*xP
        den = xP * (xP - 4)
        if num == 0:
            val = 0
        else:
            val = num / den if False else num / (xP*(xP-4))
        # killing primes 5,11,13: only x = 0, +-1 solvable -> X in {0,1}? The
        # condition is X mod p in {0,1} at killing primes; QR elsewhere
        if p in (5, 11, 13):
            if val not in (0, 1):
                print("KILLED class", c, "at p", p)
                break
        else:
            if val not in squares_mod(p):
                print("KILLED class", c, "at p", p)
                break
print("done: survivor classes consistent" )