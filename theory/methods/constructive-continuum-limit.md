---
type: method
name: Constructive QFT continuum limit, OS reconstruction, gap transport
created: 2026-08-24
tags: [mathematical-physics, qft, constructive-qft, obstruction]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Constructive QFT continuum-limit machinery

> **When to reach for it.** You want to pass from a rigorously-defined lattice
> gauge theory [[thm-lattice-gauge-constructive]] to a continuum 4D QFT
> satisfying OS/Wightman axioms [[def-wightman-os-axioms]] AND transport a
> spectral gap. This is the engine for direction (A) of the YM attack.

## The pipeline

1. **Lattice definition**: finite-dim integral over holonomies, reflection
   positive (Osterwalder-Seiler), positive transfer matrix (Lüscher).
2. **RG control across scales**: Balaban multi-scale RG + finite-range
   decomposition (Brydges-Guadagni-Mitter 2004) control the UV renormalization
   [[thm-balaban-rg]].
3. **Cluster / polymer expansion** (Kotecký-Preiss 1986) controls the
   strong-coupling regime and yields a lattice spectral gap.
4. **OS reconstruction**: convergence of Schwinger functions + OS axioms
   $\Rightarrow$ a Wightman QFT (existence).
5. **Gap transport**: prove the spectral gap survives the limit with a bound
   **uniform in $a$** (interlacing/transfer-operator estimates across RG
   scales) $\Rightarrow$ mass gap $\Delta>0$.

## The open control steps (the obstruction)

- **Convergence + full $O(4)$ covariance**: the continuum limit must satisfy
  OS1 (full Euclidean covariance), not just hypercubic $W^4$ (Eriksson 2026
  gets only $W^4$ [ym-recent-claims-unverified]).
- **Gap transport uniform in $a$**: a positive $\Delta$ independent of lattice
  spacing, across the RG from the strong-coupling (gapped) IR to the
  weak-coupling UV.
- **Gribov ambiguity**: continuum gauge-fixing non-uniqueness — a
  framework-level obstacle to even defining the measure
  [[def-wightman-os-axioms]] [ym-existence-open].

## Place in the obstruction map

This is the analog of Beal's "reduction step", BSD's "Selmer-control step",
NS's "critical-norm control": the *resolution* tools (lattice definition,
reflection positivity, cluster expansion, asymptotic freedom) all work; the gap
is the **control** of the continuum limit + the IR spectrum. The unifying lens
is dimensional transmutation [[def-yang-mills-theory]]: the continuum limit and
the mass gap are the same RG problem (fix $\Lambda_{\text{YM}}$ as $a\to0$).
See [[yang_mills]] and the cross-problem analogy [[beals_conjecture]]
[[birch_swinnerton_dyer]] [[navier_stokes]].