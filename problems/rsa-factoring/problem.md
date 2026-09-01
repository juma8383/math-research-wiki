# RSA Problem (Integer Factorization)

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/RSA.htm.
> This is a computational-complexity problem; a full attack routes through
> [[PvsNP]] (one-way-function hardness).

## Statement
Given an integer $N$ that is a product of large primes (the RSA setting:
$N=pq$), the RSA / factoring problem is to recover the factors in time
polynomial in $\log N$. Equivalently: **is integer factorization in P?**

## Status
**OPEN.** No polynomial-time *classical* factoring algorithm is known.
Factoring is in $\mathrm{NP}\cap\mathrm{coNP}$ (not believed NP-complete);
Shor's algorithm factors in polynomial time on a *quantum* computer (1994).

## Frontier (one line)
Best classical: General Number Field Sieve, sub-exponential
$L_N[1/3]=\exp((c+o(1))(\ln N)^{1/3}(\ln\ln N)^{2/3})$ `[to-verify]`; the
poly-time gap to $L_N[0]$ (i.e. polynomial) is open — factoring's
super-polynomial lower bound is unproven (the natural-proofs frontier).

## Control-step framing (one line)
A direct subface of [[PvsNP]]'s `[witness-needs-explicit-lb]`: proving no
poly classical factoring algorithm is the same non-compositional
lower-bound construction problem (an explicit hard function / one-way
function), blocked by the natural-proofs barrier — the wall is control
(lower bound), not resolution (the algorithmic methods work on slices).

## See also
- [[PvsNP]] — the parent complexity problem; this is one restricted-class
  face of the same lower-bound construction (A).
- [[discrete_logarithm]], [[diffie_hellman]] — sibling algebraic one-way-
  function problems.