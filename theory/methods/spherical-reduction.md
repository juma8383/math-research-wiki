---
type: method
name: Even-exponent reduction to spherical signatures (the (3,4,5) route)
created: 2026-08-24
tags: [number-theory, descent, spherical-signatures, parametrization, chabauty]
used-in: [[beals_conjecture]]
provenance: []
---

# Even-exponent reduction to spherical signatures

The mechanism behind the sporadic solved signature $(3,4,5)$ (Siksek–Stoll),
and why it cannot reach the distinct-prime frontier. (Mechanism reconstructed
from first principles; the attribution to Siksek–Stoll and exact computational
step should be verified against their paper — flagged.)

## The trick: an even exponent hides a "2"

An exponent of the form $2k$ can be written $y^{2k}=(y^k)^2$, turning an
all-$\geq3$ equation into one with a **$2$-exponent**. For $(3,4,5)$:

$$x^3 + y^4 = z^5 \;\xrightarrow{W=y^2}\; x^3 + W^2 = z^5
\quad\text{i.e. signature } (2,3,5).$$

## Why $(2,3,5)$ is special: it is *spherical*

The **spherical** signatures — those with $1/p+1/q+1/r>1$ — are exactly
$(2,2,n)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$. Spherical signatures have
**infinitely many primitive solutions given by explicit parametrizations**
(Beukers 1998; for $(2,3,5)$, 27 two-parameter families — Edwards 2004). So
$X^2+Y^3=Z^5$ is *parametrized*.

The Siksek–Stoll step (reconstructed): take the parametrization of $(2,3,5)$,
impose the extra condition $W=y^2$ (i.e. the $W$-coordinate is a perfect square)
together with primitivity, and the surviving candidates form a finite set
governed by curves of genus $\geq 2$; resolve those by **Chabauty / Mordell–Weil
sieve** (effective when the Jacobian has rank $0$,
[[rg2024-faltings-algorithm]]). Conclusion: no non-trivial primitive solution.

## The decisive scope limit

This route requires **two** things, and $(3,5,7)$ has neither:

1. **An even exponent** (to expose a hidden $2$). $(3,5,7)$ has exponents
   $3,5,7$ — all odd primes. **No reduction to a $(2,\cdot,\cdot)$ signature
   exists.** The first step is unavailable.
2. **Landing on a spherical signature**. Even among equations with an even
   exponent, only those reducing to $(2,2,n),(2,3,3),(2,3,4),(2,3,5)$ get the
   parametrization boost. $(3,4,5)\to(2,3,5)$ ✓ (the largest spherical, the
   boundary case). But $(3,4,7)\to(2,3,7)$ is **hyperbolic**
   ($1/2+1/3+1/7<1$) — *not* parametrized — so the route fails there too. The
   parametrization window is narrow.

## Synthesis

The $(3,4,5)$ success is *doubly* special: it has an even exponent (4) **and**
it lands exactly on the boundary spherical signature $(2,3,5)$. $(3,5,7)$ has
no even exponent, so the reduction cannot even be written down. This is the
**fifth** independent structural reason (after modular method, Darmon program,
Mordell lens, descent — see attempt-06) that the distinct-odd-prime frontier is
beyond current methods.

## When to reach for it

For an all-$\geq3$ signature containing an even exponent (4, or $2k$): try
reducing to the corresponding $(2,\cdot,\cdot)$ signature and check if it is
spherical ($(2,3,5)$ and smaller). If yes → parametrize + impose-square +
Chabauty is in play. If the reduced signature is hyperbolic, or there is no
even exponent (the $(3,5,7)$ case), the route is closed.