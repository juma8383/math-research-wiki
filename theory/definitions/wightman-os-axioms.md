---
type: definition
name: Wightman and Osterwalder-Schrader axioms (the existence target)
created: 2026-08-24
tags: [mathematical-physics, qft, axiomatic-qft]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Wightman / Osterwalder-Schrader axioms

Jaffe-Witten require "existence" to mean a QFT satisfying axioms at least as
strong as these [ym-clay-jaffe-witten].

## Wightman axioms (Minkowski; Streater-Wightman 1964)

- **W0** Poincaré covariance + spectral condition (energy-momentum in the
  forward cone); unique translation-invariant vacuum.
- **W1** Fields as operator-valued tempered distributions on a dense domain;
  cyclicity of the vacuum.
- **W2** Covariant transformation under the Poincaré group.
- **W3** Local commutativity (microcausality) for spacelike-separated fields.

## Osterwalder-Schrader axioms (Euclidean; OS 1973, 1975)

The Euclidean counterpart — a measure on fields satisfying:
- **OS0** Reflection positivity (recovers a positive Hilbert space).
- **OS1** Full $O(4)$ Euclidean covariance.
- **OS2** Regularity of Schwinger functions.
- **OS3** Cluster property (uniqueness of vacuum).

OS reconstruction: OS axioms $\Leftrightarrow$ Wightman axioms — the
Euclidean↔Minkowski bridge.

## Why this is the frontier

No 4D interacting QFT is known to satisfy these [ym-existence-open]; even a
precise non-perturbative *definition* of 4D quantum gauge theory is open. The
"existence" part of the Millennium problem is precisely constructing such a
measure/operator realization for YM [[method-constructive-continuum-limit]]. A
key open sub-step: **full $O(4)$ covariance** (Eriksson 2026 gets only
hypercubic $W^4$ [ym-recent-claims-unverified]).