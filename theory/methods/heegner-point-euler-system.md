---
type: method
name: Heegner-point Euler system (Kolyvagin) and its rank-1 shape limit
created: 2026-08-24
tags: [number-theory, elliptic-curves, euler-systems, heegner-points]
used-in: [[birch_swinnerton_dyer]]
provenance: [[bsd-survey]]
---

# Heegner-point Euler system

> **When to reach for it.** You want to bound the Selmer group (hence the rank
> and Sha) of an elliptic curve from a *nonvanishing of an L-function
> derivative*. This is the engine that proved BSD for analytic rank $\le1$
> [[thm-kolyvagin-gross-zagier]].

## The mechanism

1. **Construct points.** For an imaginary quadratic $K$ satisfying the Heegner
   hypothesis (all primes dividing the conductor of $E$ split in $K$), CM
   points on modular curves map to a **Heegner point** $P_K\in E(K)$.
2. **Gross-Zagier bridge.** $\hat h(P_K)\propto L'(E/K,1)$: analytic
   nonvanishing $\Leftrightarrow$ the point is non-torsion $\Leftrightarrow$ an
   algebraic point exists [[thm-kolyvagin-gross-zagier]]. This is the *only*
   general bridge known from an L-value derivative to an algebraic point.
3. **Kolyvagin's Euler system.** The "derived" points $D_K P_K$ (over
   ring-class fields) form an Euler system: their traces produce cohomology
   classes that successively annihilate pieces of the Selmer group
   $\text{Sel}_p(E)$, bounding $\operatorname{rank}E(\mathbb Q)$ from above and
   forcing $\text{Sha}$ finite.

## The shape limit (the obstruction)

The Euler system is **one-dimensional** — a single Heegner point generates it.
It can therefore bound a Selmer group of rank **at most 1**. To handle analytic
rank $r_{\text{an}}\ge2$ one would need:
- **(lower bound)** $r_{\text{an}}$ independent algebraic points (a
  higher-derivative Gross-Zagier: Zhang's heights of higher Heegner points
  $\leftrightarrow L^{(r)}$), AND
- **(upper bound)** an Euler system of "rank $\ge2$ shape" bounding the full
  Selmer group to size $r_{\text{an}}$.

Neither is known in general. Candidate higher-rank Euler systems:
**Beilinson-Flach elements** (from products of modular forms), **Kato's Euler
system derivatives** (Burns-Kurihara-Sano), and **higher Heegner points**. Each
gives partial evidence (e.g. Mazur-Tate refined conjectures) but no
rank-$\ge2$ Selmer bound.

## Place in the obstruction map

This is the analog of Beal's "reduction step" obstruction: the *resolution*
machinery (descent, Tamagawa/regulator/Sha computation) works in all ranks and
finished the verified cases — the gap is the **Selmer-group *control***
mechanism, which has the right shape only up to rank 1. See
[[birch_swinnerton_dyer]] and the cross-problem analogy with
[[beals_conjecture]].