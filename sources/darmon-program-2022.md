---
type: source
id: dv2022
title: "On Darmon's program for the generalized Fermat equation, I"
author: Billerey, N.; Chen, I.; Dieulefait, L.; Freitas, N.
date: 2022
provenance: https://arxiv.org/abs/2205.15861 (arXiv:2205.15861)
tags: [dv2022-frey-av, dv2022-irreduc-conjecture, dv2022-repeated-only, dv2022-55p-cartan, dv2022-1111n]
---

# Source — Billerey–Chen–Dieulefait–Freitas (2022), "On Darmon's program for the generalized Fermat equation, I"

> arXiv:2205.15861. Develops Darmon's program: replaces Frey elliptic curves by
> higher-dimensional Frey abelian varieties of GL₂-type. Claim tags below.

## [dv2022-frey-av] Frey abelian varieties of GL₂-type
A Frey abelian variety is an abelian variety $A/L$ with an embedding of a number
field $F$, $[F:\mathbb Q]=\dim A$, into $\mathrm{End}_L(A)\otimes\mathbb Q$.
Concretely, the Jacobian $J_r$ of Kraus' hyperelliptic curve $C_r(a,b)$ has
dimension $(r-1)/2$ and becomes of GL₂-type over
$K=\mathbb Q(\zeta_r)^+$ (maximal totally real subfield of the $r$-th cyclotomic
field). Residual 2-dimensional Galois representations with bounded conductor
are attached to putative solutions for **all signatures** (Theorem 2.8:
determinant = $p$-adic cyclotomic character → trivial-character modularity).

## [dv2022-irreduc-conjecture] The blocking irreducibility conjecture
**Darmon's Conjecture 1.2:** there should exist $C(L,F)$ such that for all
primes $\mathfrak p$ in $F$ above rational primes $p$ of norm $>C(L,F)$, the
image of the mod-$\mathfrak p$ representation contains $\mathrm{SL}_2(\mathbb F_{\mathfrak p})$.
**Status: "still wide open."** This is the analog of **Mazur's theorem** (which
classifies mod-$p$ images for elliptic curves over $\mathbb Q$, giving
irreducibility for large $p$) — but **no analogous general theorem exists for
abelian varieties of GL₂-type over totally real fields.** Irreducibility is
proved only conditionally (large $p$ + principal-series/supercuspidal local
image). This is the crux of the crux for the whole program.

## [dv2022-repeated-only] Repeated exponents only
The paper treats signatures **$(r,r,p)$ and $(p,p,r)$** ($r\ge5$ prime fixed,
$p$ varying) — i.e. signatures with a **repeated exponent**. **Remark 2.4:**
Darmon also classified Frey representations of signature $(p,q,r)$ for **three
distinct prime exponents**, but "these are not considered in this work." So the
three-distinct-prime case (incl. Beal's $(3,5,7)$) has a *classification* of Frey
varieties but **no developed modular method** — and is blocked by the same
[dv2022-irreduc-conjecture].

## [dv2022-55p-cartan] The $(5,5,p)$ reduction
**Theorem 1.8:** for $r=5$ the construction reduces to CM forms, so only the
**Cartan case** of the conjecture (Conjecture 1.3) is needed, not the full Borel
case. **Corollary 1.9** (conditional on Conjecture 1.3): no non-trivial primitive
solutions to $x^5+y^5=z^p$ for $p$ sufficiently large.

## [dv2022-1111n] An unconditional partial result
**Theorem 1.5:** for all $n\ge2$, no non-trivial primitive solutions to
$x^{11}+y^{11}=z^n$ when $2\mid a+b$ or $11\mid a+b$ (uses Frey elliptic curves
to "propagate" irreducibility). Second volume studies $x^7+y^7=dz^p$, $d\in\{1,3\}$.