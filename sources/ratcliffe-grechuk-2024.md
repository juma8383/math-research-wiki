---
type: source
id: rg2024
title: "Generalised Fermat equation: a survey of solved cases"
author: Ratcliffe, Luke; Grechuk, Bogdan
date: 2024
provenance: https://arxiv.org/abs/2412.11933 (arXiv:2412.11933)
tags: [rg2024-fc-vs-beal, rg2024-10-solns, rg2024-solved-sigs, rg2024-357-smallest, rg2024-comp-bound, rg2024-faltings-algorithm]
---

# Source — Ratcliffe & Grechuk (2024), "Generalised Fermat equation: a survey of solved cases"

> arXiv:2412.11933. Survey of solved cases of $ax^p+by^q=cz^r$.
> Claim tags below are the stable join keys; cite them from wiki pages.
> Extracted via the survey's HTML; individual paper-level references (labelled
> [n] as in the survey) should be checked against primary sources before
> heavy reliance, but the aggregate claims and the survey's own propositions
> are the authoritative unit here.

## [rg2024-fc-vs-beal] Fermat–Catalan ≠ Beal
- **Fermat–Catalan conjecture**: equation $x^p+y^q=z^r$ has only *finitely many*
  coprime solutions with $1/p+1/q+1/r<1$ (exponents may vary; $\min\{p,q,r\}$ may
  be 2).
- **Beal's conjecture** (Beal prize, 1997, \$1M): equation has *no* coprime
  solutions when $\min\{p,q,r\}\geq 3$.
- Beal is **strictly stronger** in the $\geq 3$ regime (asserts zero, not
  finiteness). The two are distinct conjectures.

## [rg2024-10-solns] The 10 known primitive Fermat–Catalan solutions
Up to exchanging $(x,p)\leftrightarrow(y,q)$, all have $\min\{p,q,r\}=2$:

| $(p,q,r)$ | $(x,y,z)$ |
|---|---|
| $(p,3,2)$, $p\ge6$ | $(1,2,3)$ |
| $(8,2,3)$ | $(33,1549034,15613)$ |
| $(5,2,4)$ | $(2,7,3)$ |
| $(3,2,7)$ | $(1414,2213459,65)$ |
| $(9,2,3)$ | $(9262,15312283,113)$ |
| $(7,3,2)$ | $(2,17,71)$ and $(17,76271,21063928)$ |
| $(5,4,2)$ | $(3,11,122)$ |
| $(8,3,2)$ | $(43,96222,30042907)$ |

**All have a $2$ among the exponents** → none is a Beal counterexample (Beal
needs all $\geq 3$). This is the empirical heart of why Beal may be true while
Fermat–Catalan is the weaker finiteness statement.

## [rg2024-solved-sigs] Solved Beal-relevant signatures (zero primitive solns)
From the survey's Table 1.1, signatures with all exponents $\geq 3$ that are
completely solved (no coprime solutions), with survey reference labels:
- $(p,p,p)$, all $p\ge3$ — Wiles [FLT].
- $(n,n,3)$, $n\ge3$ — Darmon–Merel.
- $(3,3,n)$, $3\le n\le 10^9$ — Chen–Siksek, Kraus, Bruin, Dahmen [44,91,30,48,13].
- $(5,5,7)$ and $(5,5,19)$ — Dahmen–Siksek [50].
- $(7,7,5)$ — Dahmen–Siksek [50].
- $(3,4,5)$ — Siksek–Stoll [133].
- $(2j,2k,n)$, $j,k\ge5$ prime, $n\in\{3,5,7,11,13\}$ — Anni–Siksek [1,20]
  (here all exponents $\geq 6$).

(Signatures involving a $2$, e.g. $(n,n,2),(2,3,n),(2,4,n)$, are also solved but
are **not** Beal-relevant — they have an exponent $<3$.)

## [rg2024-357-smallest] Smallest open Beal signature
> "The smallest triple for which Beal's conjecture remains open is
> $(p,q,r)=(3,5,7)$."

This is the target of attempt-02. Note $1/3+1/5+1/7 = 71/105 < 1$ (hyperbolic),
all exponents prime and $\geq 3$, and pairwise distinct.

## [rg2024-comp-bound] Computational verification
**Proposition 1.3.** The only coprime solutions to $x^p+y^q=z^r$ with
$z^r \le 2^{100}$ are the 10 listed in [rg2024-10-solns]. (Earlier Sikera bound
$2^{71}$.) So Beal is computationally verified for $z^r \le 2^{100}$.

## [rg2024-faltings-algorithm] Effective genus-≥2 point computation
**Theorem 3.1.** There is an algorithm to compute all rational solutions of any
  genus-$\geq2$ curve whose Jacobian has rank $0$. (Faltings gives finiteness
  ineffectively in general; rank-0 Jacobians make it effective.)