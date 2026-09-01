---
type: problem
slug: yang-mills
title: Yang-Mills existence and mass gap
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [mathematical-physics, qft, gauge-theory, constructive-qft]
tools: [[def-yang-mills-theory], [def-wightman-os-axioms], [def-mass-gap-confinement], [thm-asymptotic-freedom], [thm-lattice-gauge-constructive], [thm-balaban-rg], [thm-seiberg-witten-supersymmetric], [method-constructive-continuum-limit]]
related: [[beals_conjecture], [birch_swinnerton_dyer], [navier_stokes], [hodge_conjecture], [collatz_conjecture]]
target-frontier: rigorous 4D quantum YM existence + mass gap
---

# Yang-Mills existence and mass gap

## Statement (Jaffe-Witten / Clay, 2000)

Prove that for any **compact simple** gauge group $G$, a non-trivial **quantum
Yang-Mills theory exists on $\mathbb R^4$** and has a **mass gap $\Delta>0$**
[ym-clay-jaffe-witten].

- **Existence**: construct a QFT satisfying axioms at least as strong as the
  Wightman / Osterwalder-Schrader axioms [[def-wightman-os-axioms]] (Poincaré
  covariance, spectral condition, unique vacuum, local commutativity; OS
  positivity + Euclidean covariance).
- **Mass gap**: the two-point function decays as
  $\langle\phi(0,t)\phi(0,0)\rangle\sim\sum_n A_n e^{-\Delta_n t}$ with
  $\Delta_0>0$ — the lightest excitation (glueball) has strictly positive mass
  [[def-mass-gap-confinement]].

Compact simple $G$ (e.g. $SU(3)$ for QCD) is chosen because **asymptotic
freedom** [[thm-asymptotic-freedom]] makes non-abelian YM the simplest
nontrivial constructive QFT in 4D (most other 4D interacting QFTs have Landau
poles and would be trivial). $1{,}000{,}000$ prize.

## Known partial results (frontier)

- **Classical YM** [[def-yang-mills-theory]]: well-defined, scale-invariant in
  4D (dimensionless coupling).
- **Asymptotic freedom** [[thm-asymptotic-freedom]] [ym-asymptotic-freedom]:
  perturbative UV control (Gross-Wilczek-Politzer 1973); the IR (confinement)
  is where it fails.
- **Lattice YM** [[thm-lattice-gauge-constructive]] [ym-lattice-constructive]:
  rigorously defined at finite lattice spacing (Wilson; Osterwalder-Seiler
  reflection positivity; Lüscher transfer matrix; strong-coupling area law).
  Mass gap **confirmed numerically**, not proven in the continuum.
- **RG machinery** [[thm-balaban-rg]] [ym-balaban-rg]: Balaban 1984-89
  multi-scale RG (UV stability); Magnen-Rivasseau-Sénéor 1993 (YM₄ with IR
  cutoff); AFS 1982 infrared bound — the continuum-limit control machinery,
  incomplete.
- **Supersymmetric YM** [[thm-seiberg-witten-supersymmetric]]
  [ym-supersymmetric]: Seiberg-Witten 1994 (N=2), Nekrasov instantons —
  mass-gap-like results in a DIFFERENT (supersymmetric) theory, not the
  original.

## The obstruction

The uniquely hard feature: **even a precise non-perturbative definition of 4D
quantum gauge theory is open** [ym-existence-open] — Jaffe-Witten: "one does
not yet have a mathematically complete example... nor even a precise
definition." Unlike NS/BSD/Beal (where the object is defined), here
establishing the *framework* is part of the problem.

Structurally, the gap is a **control step**, parallel to the other three
Millennium problems:
- **Continuum-limit control**: prove the lattice theory converges as the
  spacing $a\to0$ to a non-trivial 4D QFT satisfying OS/Wightman axioms —
  including full $O(4)$ Euclidean covariance (Eriksson 2026 explicitly does
  NOT prove this) [[method-constructive-continuum-limit]].
- **IR mass-gap control**: prove $\Delta>0$ survives the limit (a positive
  bound uniform in $a$) in the strongly-coupled IR where asymptotic freedom
  gives no expansion parameter.

The unifying lens is **dimensional transmutation + the UV→IR bridge**
[ym-dimensional-transmutation]: the classical 4D action is scale-invariant;
the mass gap is a quantum-generated scale $\Lambda_{\text{YM}}\sim
\tfrac1a e^{-\text{const}/g^2}$ (from the β-function), so the continuum limit
and the gap are the same RG problem — controlling the running coupling from
the perturbative UV into the non-perturbative IR.

## Status

in-progress. Frontier = (i) rigorous existence of 4D quantum YM (axioms) +
(ii) mass gap $\Delta>0$. Toolbox and obstruction map under construction; see
`progress.md` and `attempts/`.

## Honesty note on recent claims

Several 2025-2026 preprints (Faizal-Shabir; Gutierrez Ule; Agawa — addendum
retracted; Eriksson) claim full or partial solutions
[ym-recent-claims-unverified]. **None is peer-accepted**; each relies on
unverified technical hypotheses (Balaban RG bounds, AFS infrared bound for
$SU(N)$, Gribov-ambiguity resolution) and Eriksson concedes $O(4)$ covariance
is not proved. They are treated here as *attempts to study*, not solutions.