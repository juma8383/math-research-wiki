---
type: theorem
name: Lattice Yang-Mills (rigorous at finite spacing)
created: 2026-08-24
tags: [mathematical-physics, qft, lattice-gauge-theory]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Lattice Yang-Mills — rigorous at finite lattice spacing

Discretize $\mathbb R^4$ to a lattice spacing $a$; the gauge field becomes
**holonomies** $U_\ell\in G$ on links. Wilson's lattice YM action makes the
path integral a **finite-dimensional integral** over $\{U_\ell\}$ (Haar
measure) [ym-lattice-constructive]:
$$Z=\int\prod_\ell \mathrm dU_\ell\;e^{-S_{\text{lat}}[U]}.$$

## Rigorous results at finite $a$

- **Osterwalder-Seiler (1978)**: **reflection positivity** of lattice YM —
  the Euclidean measure satisfies OS positivity [[def-wightman-os-axioms]].
- **Lüscher (1977)**: a **positive transfer matrix** (Hamiltonian
  interpretation) for lattice gauge theory.
- **Strong-coupling cluster expansion** ($g$ large): yields the **Wilson-loop
  area law** (confinement) and a spectral gap at finite $a$
  [[def-mass-gap-confinement]].

## Role in the obstruction

Lattice YM is the *resolution* layer that works: the theory is rigorously
defined and exhibits confinement + a gap at finite spacing. The mass gap is
**numerically** confirmed in this setting. The gap is the **continuum limit**
$a\to0$: proving convergence to a non-trivial 4D QFT (existence) AND that the
spectral gap survives with a bound uniform in $a$ (mass gap) — both *control*
steps [[method-constructive-continuum-limit]]. Asymptotic freedom
[[thm-asymptotic-freedom]] fixes $\Lambda_{\text{YM}}$ as $a\to0$ ($g(a)\to0$),
so the strong-coupling (gapped) regime and the continuum limit live at
opposite ends of the RG — the gap must be transported across scales.