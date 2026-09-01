---
type: theorem
name: Catalogue of solved generalized-Fermat signatures (Beal-relevant)
created: 2026-08-24
tags: [number-theory, exponential-diophantine, generalized-fermat]
used-in: [[beals_conjecture]]
provenance: [[rg2024]]
---

# Solved generalized-Fermat signatures (Beal-relevant, all exponents ≥ 3)

Aggregate result (from [rg2024-solved-sigs]): the following signatures
$(p,q,r)$, all with $p,q,r\geq 3$, have been **proven to have zero primitive
(pairwise-coprime) solutions** to $x^p+y^q=z^r$ (up to permutation):

| signature | scope | method / reference |
|---|---|---|
| $(p,p,p)$ | all $p\geq 3$ | Frey + modularity + Ribet — Wiles (FLT) [[thm-fermat-last]] |
| $(n,n,3)$ | all $n\geq 3$ | Darmon–Merel |
| $(3,3,n)$ | $3\leq n\leq 10^9$ (+ residue classes) | Chen–Siksek, Kraus, Bruin, Dahmen |
| $(5,5,7)$, $(5,5,19)$ | — | Dahmen–Siksek |
| $(7,7,5)$ | — | Dahmen–Siksek |
| $(3,4,5)$ | — | Siksek–Stoll |
| $(2j,2k,n)$, $j,k\ge5$ prime, $n\in\{3,5,7,11,13\}$ | — | Anni–Siksek |

## What this tells us about Beal's structure

Every solved Beal-relevant signature **has a repeated exponent**: $(p,p,p)$,
$(n,n,3)$, $(3,3,n)$, $(5,5,*)$, $(7,7,*)$. The lone sporadic exception
$(3,4,5)$ (Siksek–Stoll) and the $(2j,2k,n)$ family have even-exponent
factorizations enabling descent. **No solved Beal signature has three pairwise
distinct odd-prime exponents.** That is not a coincidence: see
[[method-frey-level-lowering-obstruction]], which shows the classical Frey /
level-lowering method is structurally blocked precisely for pairwise-distinct
odd-prime signatures.

## The smallest open case
[rg2024-357-smallest]: the smallest open Beal signature is **$(3,5,7)$** —
three pairwise distinct odd primes. This is the frontier attacked in
attempt-02 of [[beals_conjecture]].

## Provenance caveat
References here follow the survey [[rg2024]]'s internal labels; the individual
primary papers (Chen–Siksek 2009, Darmon–Merel, Dahmen–Siksek, Siksek–Stoll,
Anni–Siksek) should be ingested directly before relying on exact scope claims
(e.g. the $10^9$ bound). The aggregate "these are solved" status is solidly
sourced.