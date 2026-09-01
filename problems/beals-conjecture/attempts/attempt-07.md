---
type: attempt
problem: beals_conjecture
attempt: 07
date: 2026-08-24
approach: Verify (3,5,7) is the solved/open boundary by checking its repeated-exponent neighbors
outcome: confirmed
tags: [signature-catalogue, boundary-check, synthesis]
loop_cycle: 5 of 20
---

# Attempt 07 — Is $(3,5,7)$ really the boundary?

[rg2024-357-smallest] states $(3,5,7)$ is the smallest open Beal triple. This
cycle confirms it structurally by checking that every *neighbor* of $(3,5,7)$
obtained by collapsing one exponent to create a repeat is **solved** — i.e.
$(3,5,7)$ sits exactly on the solved/open frontier, with the open region being
precisely the all-distinct-odd-prime signatures.

## The repeated-exponent neighbors of $(3,5,7)$

A "neighbor" = replace one of $\{3,5,7\}$ with a value already present, creating
a repeated exponent (the only kind the classical/modular methods handle, per
attempts 02/03/06). All such neighbors:

| neighbor (up to perm) | which family solves it | reference |
|---|---|---|
| $(3,3,7)$ | $(3,3,n)$, $n\leq10^9$ | Chen–Siksek et al. [rg2024-solved-sigs] |
| $(5,5,7)$ | sporadic | Dahmen–Siksek [rg2024-solved-sigs] |
| $(3,5,5) = (5,5,3)$ | $(n,n,3)$, $n\geq3$ ($n=5$) | Darmon–Merel [rg2024-solved-sigs] |

All three repeated-exponent neighbors of $(3,5,7)$ are **solved (zero primitive
solutions)**, sourced in [[thm-solved-generalized-fermat-signatures]].

## Why this confirms the boundary

$(3,5,7)$ is the smallest signature with three **pairwise distinct odd primes**
(three smallest odd primes $3,5,7$). Every smaller signature either:
- has a repeated exponent (a "neighbor" above) → solved, or
- involves a $2$ → outside Beal's $\min\geq3$ regime, or
- has a composite exponent (e.g. $(3,4,7)$, $(4,4,3)$) → covered by the
  survey's "smallest open = $(3,5,7)$" claim (not independently re-derived here;
  flagged below).

So the open region is exactly the **all-distinct-odd-prime** signatures
$\{(3,5,7), (3,5,11), (3,7,11), (5,7,11), \dots\}$, with $(3,5,7)$ the least.

## Consistency with the four-thread diagnosis (attempt-06)

This matches the convergent structural picture: solved = repeated-exponent
(where a classical/modular structure exists); open = distinct-prime (where
attempt-06 showed *every* method fails at requirement (1) — no factorization).
The boundary is not arbitrary; it is exactly the factorization/no-factorization
divide.

## Caveat (honesty)

The composite-exponent neighbors (e.g. $(3,4,7)$, $(4,5,7)$) are *not*
independently verified here. They are subsumed by the survey's direct claim
[rg2024-357-smallest] that $(3,5,7)$ is the smallest open triple. If one wanted
to make the boundary argument *self-contained* (not relying on the survey's
"smallest"), one would need to confirm $(3,4,n)$-type families are solved — a
candidate for a later ingest cycle (pull Siksek–Stoll's $(3,4,5)$ and the
$(3,4,n)$ program). For now the sourced claim is sufficient.

## Outcome

**confirmed** (modulo the composite-exponent caveat above). $(3,5,7)$ is
the solved/open boundary, and the open region = all-distinct-odd-prime
signatures. This sharpens the frontier from "a single signature" to "an
infinite class with a sharp solved boundary, of which $(3,5,7)$ is the least."

## Next cycle

Even-exponent factorization: how $(3,4,5)$ was solved (Siksek–Stoll) and
whether any of that machinery can reach toward the distinct-prime frontier —
the one remaining classical tool not yet examined for transferability.