---
type: source
id: verzobio-2023
title: "Some effectivity results for primitive divisors of elliptic divisibility sequences"
author: Matteo Verzobio
date: 2023
provenance: Pacific J. Math. 325 (2023) 331-351, DOI 10.2140/pjm.2023.325.331; arXiv:2001.02987v3
tags: [verzobio2023-effective, verzobio2023-constant, verzobio2023-model-dep, silverman1988-ineffective, cheon-hahn1999, ingram-silverman2012-uniform, emw2006-family-bounds, vy2012-j1728, eds-no-uniform-small-bound]
---

# Verzobio 2023 — effective primitive divisors for EDS (fixed curve)

VERIFIED VERBATIM 2026-09-03 from the arXiv v3 full text (abstract, Thm 1.2,
Eq. (13), Example 9.1, final paragraph of Sec 8). Used by
[[magic_square_of_squares]] §2i (attribution correction for the K34
primitive-divisor gate).

## The theorem (verbatim-anchored)

**Theorem 1.2.** Let $E$ be an elliptic curve defined over a number field $K$
and let $P\in E(K)$ be a non-torsion point. Consider the sequence
$\{B_n\}$ of integral $\mathcal O_K$-ideals, $(x(nP))\mathcal O_K=A_n/B_n$
(in lowest terms). There exists a constant $C(E/K,\mathcal M)>0$, effectively
computable and depending only on the curve $E$ over $K$ equipped with a model
$\mathcal M$, such that $B_n$ has a primitive divisor for $n>C(E/K,\mathcal M)$.

- **[verzobio2023-effective]** — existence is EFFECTIVE for a fixed
  (curve, model); this replaces the ineffective Silverman 1988 Prop 10
  (**[silverman1988-ineffective]**, J. Number Theory 30, via Siegel) and its
  number-field generalization Cheon–Hahn 1999, Acta Arith. 88, 219–222
  (**[cheon-hahn1999]**).
- **[verzobio2023-model-dep]** — the dependence on the model $\mathcal M$ is
  NECESSARY (Remark 1.3: given any $C$, a model exists with no primitive
  divisor for all $n\le C$). Remark 1.4: conjecturally, for MINIMAL models,
  $C$ should depend only on $K$; and Ingram–Silverman
  (**[ingram-silverman2012-uniform]**, *Number theory, analysis and
  geometry*, Springer 2012, 243–271) bound $|Z(P,E)|\le\min(M_1,M_2)$
  uniformly, with uniformity in twists only under abc (Szpiro ratio).
- **[vy2012-j1728]** — Voutier–Yabuta 2012 (Acta Arith. 151, 165–190,
  $y^2=x^3+ax$ fourth-power-free): Thm 1.3 — if $B_n$ has no primitive
  divisor and ($n$ odd with $x(P)$ a rational square, or $n$ even) then
  $n\le2$; Remark 5.3: two-component case + explicit Lang gives $n<14.01$,
  so $n\le13$ (Lang-conditional, restricted). Known minimal-model examples
  WITHOUT a primitive divisor: $n=18,21$ ($B_{18}=B_{21}=17^2$) and $n=39$
  (Ingram thesis, cited in Verzobio 2021) — **[eds-no-uniform-small-bound]**.
- **[emw2006-family-bounds]** — Everest–McLaren–Ward 2006 (J. Number Theory
  118, 71–89): for congruent-number twists $y^2=x^3-T^2x$,
  $Z_e\le10$, $Z_o\le21$; also first explicit elliptic-Zsigmondy examples
  (Somos-4: every term beyond the 4th has a primitive divisor). Ingram 2009
  (JTNB 21(3) 609–634, Thm 4, verified verbatim 2026-09-03): congruent
  number curves $E_N: y^2=x^3-N^2x$, $N\ge70$ squarefree ("spurious"),
  non-torsion $P$: $Z_{gd}(P,E_N)$ contains at most one value $>2$.

## The explicit constant (Eq. (13), Sec 8)

For short Weierstrass models with integer coefficients:

$$C(E/K,\mathcal M)=\max\Big\{C_1,\ V_1',\ V_2',\ e^D,\ e^{eh},\ e^{30},\
\Big(\tfrac{2C_2'+4+2C_E+\log C_4}{J_E}\Big)^{2/3}\Big\}$$

with $c_1=3.6\cdot10^{41}$ (David's Thm 2.1 at $k=2$),
$C_2'=54\,c_1D^6\log V_1'\log V_2'$,
$J_E=\dfrac{\log\|\mathbb N(\Delta_{E/K})\|}{10^{15}D^3\sigma_{E/K}^6\log^2(104613\,D\sigma_{E/K}^2)}$,
$C_E=h(j)/4+h(\Delta)/6+2.14$, $C_4=2\max|x(T)|$ over $E(\bar{\mathbb Q})[2]$.
Example 9.1 (a small-coefficient curve): $C\approx5.88\cdot10^{42}$; the
author notes the method cannot reach constants much below $\sim10^{38}$
($10^{41}$ sits inside $c_1$, $10^{15}$ inside $J_E$), and that the bound is
"too large to be computationally useful" — PARI computation covers
$4\le n\le10^5$ directly.

## Use in this wiki

Evaluated for the two K34 sieve curves
(`problems/magic-square-of-squares/scripts/mss_k34_verzobio_constant.py`,
2026-09-03): $\Delta(\tilde E_A)=10019299708108800$,
$\Delta(\tilde E_B)=118197499985920$; dominant term gives
$C\in[1.4\cdot10^{41},\,2.6\cdot10^{44}]$ ($\tilde E_A$),
$[3.7\cdot10^{41},\,6.8\cdot10^{44}]$ ($\tilde E_B$) over the unconditional
Szpiro range $\sigma\in[1,6]$ (conductor not computed; bracketed by
sensitivity). See notes.md §2i for the attribution correction it supports.