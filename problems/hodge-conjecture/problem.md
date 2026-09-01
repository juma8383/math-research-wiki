---
type: problem
slug: hodge-conjecture
title: Hodge Conjecture
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [algebraic-geometry, hodge-theory, algebraic-cycles, motives]
tools: [[def-hodge-class-cycle-map], [thm-lefschetz-1-1], [thm-hard-lefschetz-reduction], [thm-integral-hodge-fails], [thm-absolute-hodge-motivated], [thm-cattani-deligne-kaplan], [thm-standard-conjectures-motives], [method-analytic-algebraic-bridge], [conj-generalized-hodge]]
related: [[beals_conjecture], [birch_swinnerton_dyer], [navier_stokes], [yang_mills], [collatz_conjecture]]
target-frontier: codimension-2 Hodge classes on a 4-fold
---

# Hodge Conjecture

## Statement (Deligne / Clay, 2000) [hodge-clay-deligne] [hodge-statement]

Let $X$ be a non-singular complex projective variety (compact Kähler, algebraic).
The Hodge decomposition $H^n(X,\mathbb C)=\bigoplus_{p+q=n}H^{p,q}$ defines the
**Hodge classes** of codimension $p$:
$$\mathrm{Hdg}^p(X):=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)\subset H^{2p}(X,\mathbb C).$$
Every codimension-$p$ algebraic cycle $Z$ has a cohomology class
$\mathrm{cl}(Z)\in H^{2p}(X,\mathbb Z)$ of type $(p,p)$ [[def-hodge-class-cycle-map]].

**Hodge Conjecture (Hodge 1950, as stated by Deligne):** On a non-singular
projective variety over $\mathbb C$, every Hodge class is a $\mathbb Q$-linear
combination of classes $\mathrm{cl}(Z)$ of algebraic cycles. Equivalently the
cycle class map $\mathrm{cl}:\mathrm{CH}^p(X)\otimes\mathbb Q\to\mathrm{Hdg}^p(X)$
is **surjective** for all $p$.

## Known partial results

- **Divisors ($p=1$, degree $2$) — PROVEN.** The Lefschetz theorem on $(1,1)$-classes:
  every integral $(1,1)$ class is $\mathbb Z$-linear combination of divisor classes
  [[thm-lefschetz-1-1]] [hodge-lefschetz-1-1]. Via the exponential sequence;
  the working engine.
- **Hard Lefschetz reduction** [[thm-hard-lefschetz-reduction]]: HC in degree
  $2p$ follows from degree $2(n-p)$. Hence the only general cases known are
  degrees $0,2,2n-2,2n$ — i.e. $p\in\{0,1,n-1,n\}$
  [hodge-known-degrees-0-2-2n] [hodge-hard-lefschetz-reduction].
- **Integral version FAILS** [[thm-integral-hodge-fails]]: Atiyah–Hirzebruch
  and Kollár constructed varieties where integral Hodge classes are not
  algebraic — only the $\mathbb Q$-version is conjectured
  [hodge-integral-fails]. The $\mathbb Z$-statement is false; the obstruction
  is torsion / divisibility.
- **Algebraicity is essential** [hodge-algebraicity-essential]: Zucker gave
  Kähler (non-projective) tori with Hodge classes not from analytic cycles;
  the projective hypothesis cannot be dropped.
- **Abelian varieties** [hodge-abelian-cases]: HC known for products of
  elliptic curves (Tate/Murty), Fermat type of prime degree or $\le20$
  (Shioda), simple of prime dimension (Tankeev/Ribet), fourfolds of types
  I/II (Moonen–Zarhin), some Weil-type fourfolds (Schoen). But open for general
  abelian varieties (notably Weil type, type III).
- **Absolute Hodge** [[thm-absolute-hodge-motivated]]: every Hodge class on an
  abelian variety is **absolute Hodge** (Deligne) — the strongest known
  evidence (they behave well under all field automorphisms of $\mathbb C$)
  [hodge-absolute-hodge]. André's **motivated cycles** extend this.
- **Hodge locus algebraic** [[thm-cattani-deligne-kaplan]]: the Hodge locus of
  a Hodge class in a family is a countable union of closed algebraic subsets
  (Cattani–Deligne–Kaplan) — Hodge classes behave "as if" algebraic
  [hodge-cattani-deligne-kaplan].
- **Standard conjectures / motives** [[thm-standard-conjectures-motives]]
  [hodge-standard-conjectures]: if the Künneth components of the diagonal and
  the inverse Lefschetz operators were algebraic (Grothendieck B, C) — known
  for surfaces, abelian varieties, hyper-Kähler $K3^{[n]}$ (Charles–Markman
  2013) — the category of motives becomes Tannakian and HC reduces to a
  functor being fully faithful. The motive reduction.
- **Generalized Hodge Conjecture** [[conj-generalized-hodge]]
  [hodge-generalized-conjecture]: Grothendieck's coniveau version; Hodge's
  original stronger form is false (Grothendieck); GHC = usual HC at $k=2r$.

## The obstruction (control step, not resolution step) [hodge-codim-2-open]

The resolution tools all exist: Chow groups and the cycle class map
$\mathrm{cl}:\mathrm{CH}^p\to H^{2p}$ are well-defined in all codimensions;
Hodge classes are computable via Hodge theory; for $p=1$ the **exponential
sequence + Lefschetz $(1,1)$** converts a Hodge class into an algebraic
divisor (the bridge works). The gap is the **control over the
analytic→algebraic conversion in codimension $\ge2$**: given an arbitrary
Hodge class of codimension $\ge2$, there is no known mechanism producing a
$\mathbb Q$-combination of algebraic cycles mapping to it. The Abel–Jacobi /
normal-function machinery that bridged analytic and algebraic for divisors
has no effective analogue producing cycles in higher codimension
[[method-analytic-algebraic-bridge]].

**Frontier (exact):** by hard Lefschetz only the "middle" codimensions
$2\le p\le n-2$ are genuinely new; the smallest open case is **codimension-2
Hodge classes on a smooth projective 4-fold** (a $(2,2)$ class in $H^4$ not
hit by divisors/Lefschetz). Deligne: "known when the solution set has
dimension $<4$; open in dimension $4$ and higher." This is the Hodge analog of
Beal's $(3,5,7)$, BSD's analytic rank $\ge2$, NS's large 3D data, YM's
continuum limit.

## Status

In-progress; open content = "Hodge class (analytic) → algebraic cycle" in
codimension $\ge2$. Outcome attempt-01 = partial (frontier + obstruction
mapped, no proof). Honesty: a 2024–25 preprint flurry claiming solutions
(Shimizu 2025, Bouali 2024, Abdelgalil 2025, Mounda 2025, Hajebi & Hajebi
2025) is flagged `hodge-recent-claims-unverified` — NONE peer-reviewed or
community-accepted; several carry acknowledged gaps (Abdelgalil: conditional
on unproven "algebraicity of limits"; Mounda: a conjecture not a proof;
Hajebi: asserts an unproved "spanning property"; Shimizu: zero citations)
[hodge-recent-claims-unverified]. The $\ell$-adic analogue (Tate conjecture)
is open even for $H^2$ [hodge-tate-analogue].