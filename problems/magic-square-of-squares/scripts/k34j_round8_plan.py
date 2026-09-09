#!/usr/bin/env python3
# ROUND 8: root number (rank parity) of Jac(P) via local factors.
# P : y^2 = x*N(x), N = x^4-4x^3-604x^2-952x+56644.
# disc(N) = 2^11 * 3^4 * 7 * 17 (computed earlier: 167856039493632 factored).
# Actually the earlier factorization: disc of the quartic N: 1678560394943632? We had
# disc = [2, 11; 3, 4; 7, 1; 17, 1] from the poldisc of the dehomogenized quartic.
# For y^2 = x*N(x): the bad primes include the disc primes AND primes from the
# x=0 branch: the sextic x*N(x) has degree 5 (odd) -> one infinity point (rational).
# Global root number = -prod_p W_p (local signs), with W_p = -1 for primes where
# the reduction type contributes odd... For odd-degree hyperelliptic curves the
# global sign can be computed from the reduction types (Dokchitser algorithms) —
# heavy by hand. ALTERNATIVE: parity via the functional equation's behavior of
# the flat sum: analytic rank 0 (even) => W = +1. Self-consistent with the flat sum.
# The rigorous statement we can make NOW: the sum being flat is strong evidence.
# For unconditional: compute the 2-Selmer rank via Stoll's mwrank-style descent
# — PARI has 'genus2red' but not a full Selmer computation. Magma's RankBounds
# would do it (not available). 
# INTERMEDIATE rigorous step: verify the L-series sum to much larger X with
# better smoothing — the flatness through p=5000 with amplitude ~0.15 is already
# strong evidence (rank 1 sums grow by +1.0 per loglog unit: from loglog(5000)=2.14
# a rank-1 curve's sum should be ≈ +1.0·2.14 + C... the flatness rules it out
# convincingly at the heuristic level).
# ALSO: cross-check via the BSD-conditional route: L(1) ≠ 0 numerically:
# compute L(Jac(P), 1) via the convergent series with Gamma factors cancelled —
# the standard approximate-functional-equation method: L(1) = sum_n a_n/n · w(n)
# with a smooth cutoff. Implement: get charpolys to N=100000 via PARI, compute
# the exponential sum, check |L(1)| >> 0.
print("Route: numerical L(1) of Jac(P) via smooth cutoff; |L(1)| > 0 with error")
print("bounds => analytic rank 0 PROVABLE (L(1) nonvanishing is decidable to")
print("precision). Implement in PARI with the charpoly data.")