---
type: problem
slug: birch-swinnerton-dyer
title: Birch and Swinnerton-Dyer Conjecture
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [number-theory, elliptic-curves, L-functions, arithmetic-geometry]
tools: [[def-elliptic-curve-L-function], [thm-mordell-weil], [thm-modularity], [thm-kolyvagin-gross-zagier], [method-heegner-point-euler-system], [thm-parity]]
related: [[beals_conjecture], [navier_stokes], [yang_mills], [hodge_conjecture], [collatz_conjecture]]
target-frontier: analytic rank >= 2
---

# Birch and Swinnerton-Dyer Conjecture

## Statement

Let $E/\mathbb Q$ be an elliptic curve with Hasse-Weil L-function $L(E,s)$
[[def-elliptic-curve-L-function]], Mordell-Weil rank $r_{\text{alg}}$
[[thm-mordell-weil]], and analytic rank $r_{\text{an}}=\operatorname{ord}_{s=1}L(E,s)$.

**BSD (rank part):** $r_{\text{alg}}=r_{\text{an}}$.

**BSD (refined):**
$$\frac{L^{(r_{\text{an}})}(E,1)}{r_{\text{an}}!}=
\frac{\Omega_E\,R_E\,|\text{Sha}(E/\mathbb Q)|\,\prod_p c_p}
{|E(\mathbb Q)_{\text{tors}}|^2}.$$

## Provenance and context

Posed by Birch and Swinnerton-Dyer in the 1960s from computational
observations (the "BSD ratio" $L(E,s)/(\Omega\prod c_p)$ near $s=1$ tracking
the rank). One of the seven Clay Mathematics Institute **Millennium Prize
Problems** ($1{,}000{,}000$). Unlike most Millennium problems, a large piece
(analytic rank $\le1$) is already a **theorem** [[thm-kolyvagin-gross-zagier]].

## Known partial results (frontier)

- **Analytic rank $\le1$ — BSD proven** (rank equality + $\text{Sha}$
  finiteness): Gross-Zagier + Kolyvagin + modularity + nonvanishing
  [[thm-kolyvagin-gross-zagier]] [bsd-rank-le-1-proven].
- **Parity — proven** ($r_{\text{alg}}\equiv r_{\text{an}}\pmod2$;
  $p$-parity unconditionally): [[thm-parity]] [bsd-parity-proven].
- **Refined leading-coefficient — open in general** (even at rank 0),
  verified computationally for conductor $<5000$ [bsd-refined-open]
  [bsd-comp-verified].
- **Analytic rank $\ge2$ — open**: no curve has full BSD proven
  [bsd-rank-ge-2-open]; Kolyvagin's higher-rank conjectures unproven
  [bsd-kolyvagin-conj].

## Status

in-progress. Frontier = analytic rank $\ge2$ (rank equality) + the refined
leading-coefficient formula. The shared toolbox and obstruction map are being
built; see `progress.md` and `attempts/`.