---
type: source
id: ym-survey
title: "Yang-Mills status — compiled from web-search summaries"
author: "(compiled, not a primary source)"
date: 2026-08-24
provenance: "web searches; URLs below; NOT verbatim primary sources — flagged [summary]"
tags: [ym-clay-jaffe-witten, ym-existence-open, ym-mass-gap, ym-confinement-area-law, ym-asymptotic-freedom, ym-dimensional-transmutation, ym-lattice-constructive, ym-balaban-rg, ym-supersymmetric, ym-recent-claims-unverified, ym-spectral-gap-undecidable]
used-in: [[yang_mills]]
---

# Yang-Mills status survey (compiled from web searches)

> Compiled 2026-08-24 from two web searches; **not a verbatim primary
> source**. Each `[summary]` claim should be re-verified against primary
> sources before load-bearing use. URLs:
> https://www.claymath.org/millennium/yang-mills-the-maths-gap/ (Jaffe-Witten);
> https://www.claymath.org/library/annual_report/ar2003/03report_douglas.pdf
> (Douglas 2003 status report);
> https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_existence_and_mass_gap;
> https://ncatlab.org/nlab/show/Yang-Mills+mass+gap;
> https://doi.org/10.1002/prop.70097 (Faizal-Shabir);
> https://doi.org/10.31219/osf.io/hnw5p_v1 (Gutierrez Ule).

## [ym-clay-jaffe-witten] Clay Millennium problem (Jaffe-Witten 2000)
[summary] One of 7 Millennium problems ($1M). Prove for any compact simple $G$,
a non-trivial quantum YM exists on $\mathbb R^4$ (axioms at least as strong as
Wightman / Osterwalder-Schrader) AND has a mass gap $\Delta>0$. [used-in: [[yang_mills]] [[def-wightman-os-axioms]]]

## [ym-existence-open] Existence is itself open
[summary] "One does not yet have a mathematically complete example of a
quantum gauge theory in four-dimensional space-time, nor even a precise
definition" (Jaffe-Witten). No 4D interacting QFT satisfies the axioms.
UNIQUELY hard: the framework itself is part of the problem. [used-in: [[def-wightman-os-axioms]]]

## [ym-mass-gap] Mass gap Δ>0
[summary] Two-point function $\sim\sum A_n e^{-\Delta_n t}$, $\Delta_0>0$;
lightest excitation (glueball) massive. Confirmed numerically on the lattice,
no rigorous analytic proof in the continuum. [used-in: [[def-mass-gap-confinement]]]

## [ym-confinement-area-law] Confinement
[summary] Color flux tubes, linear potential $V(r)\sim\sigma r$, Wilson-loop
area law $\langle W(C)\rangle\sim e^{-\sigma\,\mathrm{Area}(C)}$; no isolated
color charges/massless gluons; color-neutral glueballs are massive.
[used-in: [[def-mass-gap-confinement]]]

## [ym-asymptotic-freedom] Asymptotic freedom (Gross-Wilczek-Politzer 1973)
[summary] $\beta(g)=-\beta_0 g^3+\cdots$, $\beta_0=11N/(48\pi^2)>0$ for $SU(N)$;
$g(\mu)\to0$ at UV, grows at IR. Nobel 2004. Makes non-abelian YM the simplest
nontrivial constructive 4D QFT. [used-in: [[thm-asymptotic-freedom]] [[def-yang-mills-theory]]]

## [ym-dimensional-transmutation] Dimensional transmutation
[summary] Classical 4D YM scale-invariant ($g$ dimensionless); quantum
β-function generates $\Lambda_{\text{YM}}=\mu e^{-1/(2\beta_0 g^2)}$; expected
$\Delta\sim\Lambda_{\text{YM}}>0$. Continuum limit (fix $\Lambda_{\text{YM}}$,
$g_0\to0$) and mass gap are the same RG problem. [used-in: [[def-yang-mills-theory]]]

## [ym-lattice-constructive] Lattice YM rigorous at finite spacing
[summary] Wilson lattice (finite-dim holonomy integrals); Osterwalder-Seiler
1978 reflection positivity; Lüscher 1977 positive transfer matrix;
strong-coupling cluster expansion $\Rightarrow$ area law + gap at finite $a$.
[used-in: [[thm-lattice-gauge-constructive]]]

## [ym-balaban-rg] Continuum-limit RG machinery (incomplete)
[summary] Balaban 1984-89 multi-scale RG (UV stability); Magnen-Rivasseau-Sénéor
1993 (YM₄ with IR cutoff); Aizenman-Fröhlich-Spencer 1982 (infrared bound);
Kotecký-Preiss 1986 (cluster expansion); Brydges-Guadagni-Mitter 2004
(finite-range decomposition). Full control (convergence + $O(4)$ covariance +
uniform gap transport) NOT proved. [used-in: [[thm-balaban-rg]] [[method-constructive-continuum-limit]]]

## [ym-supersymmetric] Supersymmetric YM (solved RELATED problem)
[summary] Seiberg-Witten 1994 (N=2 SUSY SU(2): exact low-energy theory via
Seiberg-Witten curve, monopole condensation, mass gap in some vacua); Nekrasov
instanton counting rederived rigorously. NOT the original (pure, non-SUSY)
problem. [used-in: [[thm-seiberg-witten-supersymmetric]]]

## [ym-recent-claims-unverified] Recent claimed solutions (NOT peer-accepted)
[summary] Faizal-Shabir 2026 (Fortschr. Phys., 4-part: reflection positivity +
FRD + cluster expansions + gap transport, claims $O(4)$/area-law/universality);
Gutierrez Ule 2025 (Balaban+AFS, assumes RG bounds + AFS as hypothesis);
Agawa 2025 (holonomy-based; **addendum retracted**); Eriksson 2026 (Balaban +
KP + decoupling; **explicitly $O(4)$ covariance NOT proved**, only hypercubic
$W^4$). NONE accepted by the community; all rely on unverified hypotheses
(Balaban bounds, AFS for $SU(N)$, Gribov resolution). Treated as
attempts-to-study, NOT solutions. [used-in: [[method-constructive-continuum-limit]]]

## [ym-spectral-gap-undecidable] Spectral-gap undecidability (general)
[summary] Cubitt-Pérez-García-Wolf 2015: the spectral-gap problem is
undecidable in general (no universal algorithm). Does NOT preclude a
YM-specific proof (analogous to specific undecidable instances being
resolvable). [used-in: [[yang_mills]]]