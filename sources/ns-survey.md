---
type: source
id: ns-survey
title: "Navier-Stokes status — compiled from web-search summaries"
author: "(compiled, not a primary source)"
date: 2026-08-24
provenance: "web searches; URLs below; NOT verbatim primary sources — flagged [summary]"
tags: [ns-millennium-fefferman, ns-2d-solved, ns-local-wp, ns-leray-weak, ns-bkm, ns-serrin, ns-ess-endpoint, ns-ckn, ns-tao-averaged-blowup, ns-tao-quant-l3, ns-buckmaster-vicol, ns-supercritical]
used-in: [[navier_stokes]]
---

# Navier-Stokes status survey (compiled from web searches)

> Compiled 2026-08-24 from two web searches; **not a verbatim primary
> source**. Each `[summary]` claim should be re-verified against primary
> sources before load-bearing use. URLs:
> https://www.claymath.org/millennium/navier-stokes-equation/ (Fefferman,
> official Clay write-up);
> https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness;
> https://doi.org/10.1098/rsta.2019.0526 (Robinson, *NS regularity problem*);
> https://arxiv.org/abs/1803.05569 (Luo, optimal BKM localization);
> https://arxiv.org/pdf/2209.15627 (localized quantitative blowup rates).

## [ns-millennium-fefferman] Clay Millennium problem (Fefferman 2000)
[summary] One of 7 Millennium problems ($1M). Fefferman's four statements:
(A) global smooth on $\mathbb R^3$; (B) on $\mathbb T^3$; (C) breakdown on
$\mathbb R^3$; (D) on $\mathbb T^3$. Domains WITHOUT boundary. Solutions
smooth ($C^\infty$) + bounded energy ($\int|u|^2<C$). A/C (or B/D)
complementary. [used-in: [[navier_stokes]]]

## [ns-2d-solved] 2D solved
[summary] Global smooth unique solutions (Ladyzhenskaya, 1960s). Main
difficulties absent in 2D; see [ns-supercritical]. [used-in: [[def-navier-stokes-equation]]]

## [ns-local-wp] 3D local well-posedness + small-data global
[summary] Leray 1934 (local strong, $u_0\in L^2\cap L^\infty$); Fujita-Kato
1964 ($H^1$, critical $\dot H^{1/2}$); Koch-Tataru 2001 (critical Besov).
Blow-up time $T\gtrsim C/\|u_0\|_\infty^2$ etc. Small critical-norm data
$\Rightarrow$ global. Blowup rate
$\|u(t)\|_{L^p}\gtrsim (T^*-t)^{-\frac12(1-3/p)}$, $3<p\le\infty$.
[used-in: [[thm-local-wellposedness]]]

## [ns-leray-weak] Leray-Hopf weak solutions
[summary] Leray 1934 ($\mathbb R^3$), Hopf 1951. Global weak solutions for any
$u_0\in L^2$ (divergence-free), energy inequality; singular-time set box-dim
$\le1/2$. **Uniqueness open.** [used-in: [[thm-leray-weak-solutions]]]

## [ns-bkm] Beale-Kato-Majda (1984)
[summary] $\int_0^T\|\omega\|_\infty\,dt<\infty\Leftrightarrow$ regular on
$[0,T]$ (Euler & NS). Refinements: Planchon 2003, Cheskidov-Shvydkoy 2014,
Cheskidov-Dai 2015, **Luo 2019** (optimal frequency+temporal localization,
modes below $\lambda_q=c(T-t)^{-1/2}$). [used-in: [[thm-beale-kato-majda]]]

## [ns-serrin] Ladyzhenskaya-Prodi-Serrin
[summary] $u\in L^r_tL^s_x$, $2/r+3/s\le1$, $s>3\Rightarrow$ smooth & unique.
Gallagher-Koch-Planchon 2016 (Besov extension); Chemin-Gallagher 2006
(nearly-2D large data). [used-in: [[thm-serrin-regularity]]]

## [ns-ess-endpoint] Escauriaza-Seregin-Šverák (2003)
[summary] $u\in L^\infty_tL^3_x\Rightarrow$ smooth (the critical endpoint of
Serrin, via backward uniqueness + unique continuation). A global
$L^\infty_tL^3_x$ bound would prove global regularity. [used-in: [[thm-serrin-regularity]]]

## [ns-ckn] Caffarelli-Kohn-Nirenberg (1982)
[summary] Suitable weak solutions: space-time singular set has parabolic
Hausdorff dimension $\le1$ (cannot contain a space-time curve). Does not rule
out blowup; strongest unconditional structural singularity bound.
[used-in: [[thm-caffarelli-kohn-nirenberg]]]

## [ns-tao-averaged-blowup] Tao (2016) averaged-NS blowup
[summary] Finite-time blowup for an AVERAGED (modified) 3D NS preserving
energy/scaling/dissipation. A model, NOT the true equations. Most credible
evidence true-NS blowup may exist. [used-in: [[thm-tao-averaged-blowup]]]

## [ns-tao-quant-l3] Tao quantitative L³ blowup rate
[summary] If smoothness lost at $T^*$:
$\limsup_{t\uparrow T^*}\|u\|_{L^3}(\log\log\log(1/(T^*-t)))^c=\infty$.
Improvements: Barker-Prange 2021, Palasek 2021/22 (axisymmetric, to double
log), Barker 2022 (localized $L^3$ rate). [used-in: [[thm-tao-averaged-blowup]] [[method-energy-supercriticality]]]

## [ns-buckmaster-vicol] Buckmaster-Vicol (2017)
[summary] Non-uniqueness for "very weak" solutions (additional integrations by
parts); these do NOT satisfy the energy inequality, so are NOT Leray-Hopf.
Non-uniqueness known only below the Leray-Hopf class. [used-in: [[thm-leray-weak-solutions]]]

## [ns-supercritical] The supercriticality obstruction
[summary] 3D NS supercritical: energy ($L^2$, subcritical: $\lambda^{-1/2}$
scaling) is the only global bound; regularity needs critical $L^3$
(scale-invariant). Nonlinear advection Serrin index $S_{\text{nonlin}}=d+1$
vs linear $S_{\text{lin}}=d/2+2$: equal in 2D ($3=3$, solved), $4>3.5$ in 3D
(open). [used-in: [[def-navier-stokes-equation]] [[method-energy-supercriticality]]]