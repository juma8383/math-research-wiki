---
type: theorem
slug: bfh-murty-nonvanishing
title: Bump–Friedberg–Hoffstein / Murty–Murty nonvanishing
created: 2026-08-24
last-updated: 2026-08-24
tags: [nonvanishing, l-functions, heegner-points, rank-one, bsd]
used-in: [[birch_swinnerton_dyer]]
---

# Bump–Friedberg–Hoffstein / Murty–Murty nonvanishing

## Statement

Let $f$ be a cuspidal newform of even weight $k$, trivial character, for
$\Gamma_0(N)$, with functional-equation sign $\varepsilon=+1$. Then there
exist **infinitely many** imaginary quadratic fields $K=\mathbb Q(\sqrt D)$
($D<0$, prime to $N$) such that:

- every prime in a prescribed finite set $S\supseteq\{p\mid N\}$ **splits** in
  $K$ (the **Heegner hypothesis**), and
- $L'(k/2,\,f\otimes\chi_D)\neq0$ (a first-order zero of the quadratic twist).

## Sources (primary)

- Bump, Friedberg, Hoffstein, *Nonvanishing theorems for L-functions of
  modular forms and their derivatives*, **Inventiones Math. 102** (1990),
  543–618. DOI [10.1007/bf01233440](https://doi.org/10.1007/bf01233440).
- M. R. Murty, V. K. Murty, *Mean Values of Derivatives of Modular L-Series*,
  **Annals Math. 133** (1991), 447–475. DOI [10.2307/2944316](https://doi.org/10.2307/2944316).

Method: Eisenstein series on the **metaplectic group** (double cover of
$\mathrm{GSp}(4)$); a Novodvorsky-type integral gives a Dirichlet series in an
auxiliary variable whose pole at $u=1$ forces $L'(k/2,f\otimes\chi_D)\neq0$ for
infinitely many $D$. Extends Goldfeld–Hoffstein–Patterson (CM) to the non-CM
case.

## Why it matters (the load-bearing role)

This theorem is the **analytic input that makes BSD rank $\le1$
unconditional**. Without it, the Gross–Zagier–Kolyvagier argument would need
an *ad-hoc* imaginary quadratic field $K$ satisfying the Heegner hypothesis
*and* the nonvanishing $L'(E/K,1)\neq0$. BFH/Murty–Murty guarantee such $K$
exist unconditionally, so:

- **Gross–Zagier** (1986) gives $L'(E/K,1)\neq0 \iff$ Heegner point $P_K$
  non-torsion [[thm-kolyvagin-gross-zagier]].
- **Kolyvagin** (1989) then gives $E(K)$ rank $1$ and $\Sha(E/K)$ finite
  [[method-heegner-point-euler-system]].
- $\Sha(E/K)$ finite $\Rightarrow$ $\Sha(E/\mathbb Q)$ finite.

Hence BSD rank $+$ Sha-finiteness hold **unconditionally** for analytic rank
$\le1$. This is the verified base the BSD attack rests on; verifying it
against primary sources was the cycle-1 to-verify item
`[bsd-rank-le-1-proven]` (resolved — see
[[birch_swinnerton_dyer]] attempt-02).

## Cross-problem note

This is the "nonvanishing existence" that supplies the **single** Heegner point
the rank-1 engine consumes — the one-dimensional input behind the
"one-dimensional engine stops" sub-pattern. A higher-rank analogue (a supply
of $r_{\rm an}$ independent points with nonvanishing $L^{(r)}$) has no
unconditional analogue of this strength; its absence is exactly the
direction-(A) block.