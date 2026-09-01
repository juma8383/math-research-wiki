---
type: problem
slug: beals-conjecture
title: Beal's Conjecture
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [number-theory, exponential-diophantine, generalized-fermat]
tools: [[def-beal-equation], [method-pairwise-coprime-reduction], [method-exponent-reduction], [thm-fermat-last], [thm-darmon-granville], [method-frey-modularity], [method-abc-finiteness], [thm-catalan-mihailescu], [thm-solved-generalized-fermat-signatures], [method-frey-level-lowering-obstruction], [method-darmon-program], [method-mordell-curve-lens], [method-infinite-descent], [method-spherical-reduction], [method-triangle-group-descent], [method-counting-heuristic], [conj-fermat-catalan]]
synthesis: [synthesis]
related: [[birch_swinnerton_dyer], [navier_stokes], [yang_mills], [hodge_conjecture], [collatz_conjecture]]
target-signature: (3,5,7)
---

# Beal's Conjecture

## Statement

If $A, B, C, x, y, z$ are positive integers with $x, y, z \geq 3$ and

$$A^x + B^y = C^z,$$

then $A, B, C$ have a common prime factor — equivalently $\gcd(A, B, C) > 1$.

Posed by Andrew Beal (1993). Carries a USD $1,000,000 prize for a proof or
counterexample (sponsored by the AMS / Beal Prize Fund).

## Equivalent coprime form (the working target)

Using [[method-pairwise-coprime-reduction]], $\gcd(A,B,C)=1$ forces $A,B,C$ to
be **pairwise coprime**. So the conjecture is equivalent to:

> There are **no** positive-integer solutions to $A^x + B^y = C^z$ with
> $x,y,z \geq 3$ and $A,B,C$ pairwise coprime.

This is the form we attack. Every exact solution that *does* exist must then
have $\gcd(A,B,C) > 1$ (e.g. $3^3 + 6^3 = 3^5$, $\gcd=3$).

## Provenance / context

- Generalizes Fermat's Last Theorem [[thm-fermat-last]] (the case $x=y=z$).
- Falls under the *generalized Fermat equation* $x^p + y^q = z^r$ literature
  [[def-beal-equation]].
- Per [[method-exponent-reduction]], it suffices to rule out pairwise-coprime
  solutions with each exponent an odd prime or $4$.
- Best unconditional result toward it: [[thm-darmon-granville]] gives
  *finiteness* of primitive solutions per exponent triple (when
  $1/x+1/y+1/z < 1$); the open gap is reducing "finitely many" to "zero."

## Known status

**Open.** No proof or counterexample known. Verified computationally over large
ranges (see attempts). The prize remains unclaimed.

## Reward / motivation

\$1M (Beal Prize Fund). Structurally important: it is the natural "mixed
exponent" generalization of FLT and a central test case for the
Frey-curve/modularity program beyond equal exponents.