---
type: attempt
problem: yang-mills
attempt: 07
date: 2026-08-31
approach: breakthrough-hunt scan of the YM folder; two corrections filed + three new candidate directions recorded (no proof move)
outcome: partial
tags: [correction, hierarchical-ym, migdal-kadanoff, wilson-flow, preprint-watch]
---

# Attempt 07 — hunt-scan corrections + the hierarchical-program lead

*(breakthrough-hunt session 2026-08-31; the YM scan was one of two hunt
agents that completed before the quota cap)*

## Corrections (append-only)

1. **arXiv:2505.16585 is NOT a Chatterjee follow-up.** Attempt-05 recorded
   it as "Chatterjee 2021 line has a 2025 follow-up (arXiv:2505.16585
   'Expanded regimes of area law', Bonn workshop 2025-07)". The hunt scan
   identifies the authors as **Cao–Nissim–Sheffield** with an active,
   crowded follow-up line (arXiv:2509.04688) — making area-law-regime
   expansion a *bad* attack surface (crowded, resolution-side). [to-verify
   against the arXiv listing before load-bearing use; attempt-05 text left
   in place.]
2. **New unverified claim to watch:** a 2025 Zenodo preprint claiming an
   SU(3) mass gap via functional-geometric methods / Gamma-convergence.
   Add to the preprint-wave watchlist alongside Faizal–Shabir (IJGMMP),
   Agawa (retracted), Eriksson (viXra). Zenodo = unreviewed; flag stands.

## The missing literature: the 1980s hierarchical Migdal–Kadanoff program

The scan surfaced a rigorous line entirely absent from the wiki's 6 attempts
and theory pages: **Kupiainen** (PRL 55:558 (1985); CMP 95:247 (1984)) — the
MK-exact hierarchical 4D YM model; **Kupiainen CMP (1987)** — hierarchical
SU(2) *continuum limit*; **Müller–Schiemann** (LMP 15:289 (1988)) —
convergence rates, string tension and mass-gap lower bounds for the 4D
hierarchical model. This is **the unique 4D object where the full program
(continuum limit + asymptotic freedom + confinement + gap) succeeded**, and
it is the natural comparison object for the UV→IR bridge. [All four citations
summary-level; to-verify against the papers before use.]

## Three new candidate directions recorded from the scan (ranked)

- **(D) Single-inequality MK reduction (feas 4/10, highest ceiling).** Fix
  $G=\mathrm{SU}(N)$; let $A_k$ = the single-bond effective action of the
  $k$-fold dyadic Balaban blocking after coupling renormalization, $M_k$ =
  the $k$-th Migdal–Kadanoff iterate with matched $A_0$. Target theorem: in
  an explicit weighted character-coefficient norm, IF
  $\sum_k\|A_k-M_k\|_*<\infty$ THEN continuum Schwinger functions converge
  to a nontrivial OS-positive limit with $\sigma\ge c_2\Lambda_{\rm YM}>0$,
  $\xi\le c_1/\Lambda_{\rm YM}$ — i.e. Jaffe–Witten existence + gap follow
  from one named summability inequality. Main proof obligation: a stability
  lemma (iterated contraction with summable additive noise). Refuter attack:
  exhibit a summable perturbation of the MK flow restoring a Coulomb phase.
- **(E) Wilson-flow oscillation summability (feas 6/10, lemma-scale).** An
  independent, correctly-proven version of the *unreviewed* Eriksson
  viXra "Thm 3.11" (blocking-map squared-oscillation summability, uniform in
  $\beta,a$) via Kato-type domination of the Lüscher-flow Jacobian by the
  scalar heat kernel on the 4D link lattice. U(1) unconditionally, SU(2)
  numerically + conditional on a stated domination hypothesis. Session-
  runnable falsification: integrate the linearized flow on $6^4$/$8^4$
  lattices and test Jacobian domination. Publishable as a math-physics note
  either way (proves or refutes the one resolution-side improvement in the
  preprint wave).
- **(F) The $g^2$-vs-$g^4$ defect-threshold conjecture (feas 6/10,
  measurable).** Along the AF trajectory, with Balaban's marginal-operator
  subtraction at each step: $\delta_k=\|A_k-M_k\|_*= \Theta(g_k^4)$
  (summable; the $g^2$ terms cancel by one-loop exactness of the MK
  recursion); WITHOUT the subtraction $\Theta(g_k^2)$ (log-divergent —
  matching Eriksson's conceded $O(1/k)$ rate and the Balaban–Imbrie–Jaffe /
  Gallavotti folklore). Certified P1 computation runnable in python
  (character-expansion MK recursion with certifiable tail truncation; P2
  small heat-bath Monte Carlo). Refutation criterion: fitted exponent near
  2. If true: the continuum-limit obstruction is the crossover
  constants/entropy (large-field regions), NOT the defect exponent.

**Filing note:** these are recorded, not attacked — the session's development
budget went to the winning Beal candidate. (D) is the highest-value target
for a future session; it is the constructive-QFT instantiation of the
wiki's "control step" thesis: one quantitative inequality *is* the
Millennium problem.

## Honesty / confidence

Corrections filed on scan evidence (search-derived; to-verify). Citations
for the hierarchical program summary-level. No proof move; YM frontier
(continuum limit + uniform gap) unchanged.