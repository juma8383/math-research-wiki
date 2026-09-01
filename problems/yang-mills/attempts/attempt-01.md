---
type: attempt
problem: yang_mills
attempt: 1
date: 2026-08-24
approach: First attack — state YM, locate the exact frontier (existence + mass gap, both open), name the open content, map the obstruction to continuum-limit + IR-gap control via the dimensional-transmutation / UV->IR lens; flag recent claims honestly
outcome: partial
tags: [frontier, obstruction-map, constructive-qft, dimensional-transmutation, cross-problem]
---

# Attempt 01 — Establish the frontier and obstruction for Yang-Mills

First cycle on YM. Mirrors the other three problems' attempt-01: get the
clean form, locate the exact frontier, name the open content, map the
obstruction.

## Statement established [[def-yang-mills-theory]]

Jaffe-Witten [ym-clay-jaffe-witten]: for any compact simple $G$, a non-trivial
quantum YM on $\mathbb R^4$ EXISTS (Wightman/OS axioms
[[def-wightman-os-axioms]]) and has a MASS GAP $\Delta>0$
[[def-mass-gap-confinement]]. Two coupled required pieces.

## The exact frontier

| piece | status |
|---|---|
| classical YM (4D, scale-invariant) | known [[def-yang-mills-theory]] |
| asymptotic freedom (perturbative UV) | known [[thm-asymptotic-freedom]] [ym-asymptotic-freedom] |
| lattice YM (finite spacing) | rigorous [[thm-lattice-gauge-constructive]] [ym-lattice-constructive] |
| mass gap — numerical (lattice) | confirmed |
| **4D quantum YM existence (axioms)** | **open** [ym-existence-open] |
| **mass gap Δ>0 (continuum, rigorous)** | **open** [ym-mass-gap] |
| supersymmetric YM mass-gap-like | solved (related theory) [[thm-seiberg-witten-supersymmetric]] [ym-supersymmetric] |

## Open content (analog of Beal's "finitely many → zero", BSD's "rank ≤1 → arbitrary rank", NS's "small data → arbitrary large-data")

**"lattice-discretized + numerically confirmed → continuum-rigorous 4D QFT with
a proven spectral gap"**, equivalently **"asymptotic freedom (perturbative UV) →
confinement (non-perturbative IR) rigorously."**

## The obstruction: control step, not resolution step

The *resolution* layer works and finished the verified base: lattice YM is
rigorously defined (Wilson holonomies; OS reflection positivity; Lüscher
transfer matrix; strong-coupling area law), and asymptotic freedom gives
perturbative UV control [[thm-asymptotic-freedom]]
[[thm-lattice-gauge-constructive]].

The gap is a **control step** — two coupled pieces:
- **(1) Continuum-limit control**: convergence as $a\to0$ to a non-trivial 4D
  QFT satisfying OS/Wightman axioms, including FULL $O(4)$ Euclidean covariance
  (Eriksson 2026 gets only hypercubic $W^4$ [ym-recent-claims-unverified]).
  This IS the "existence" piece.
- **(2) IR mass-gap control**: $\Delta>0$ with a bound uniform in $a$, in the
  strongly-coupled IR where asymptotic freedom gives no expansion parameter.

Both are *control* (of the limit / of the IR spectrum); the lattice object is
built. The reusable engine is [[method-constructive-continuum-limit]] (OS
reconstruction + cluster expansions + finite-range decomposition + gap
transport).

## The uniquely-hard wrinkle

Unlike the other three problems, **a precise non-perturbative definition of 4D
quantum gauge theory is itself open** [ym-existence-open] (Jaffe-Witten: "nor
even a precise definition"). The **Gribov ambiguity** (gauge-fixing
non-uniqueness) is a framework-level obstacle. So the attack must partly
*construct the framework*, not just prove a theorem in it.

## The unifying lens: dimensional transmutation [ym-dimensional-transmutation]

Classical 4D YM is scale-invariant ($g$ dimensionless). The mass gap is a
quantum-generated scale $\Lambda_{\text{YM}}\sim\tfrac1a e^{-\text{const}/g^2}$
(1-loop β-function, $\beta_0=11N/(48\pi^2)$). Hence the continuum limit (fix
$\Lambda_{\text{YM}}$ as $a\to0$, $g(a)\to0$ by asymptotic freedom) and the
mass gap ($\Delta\sim\Lambda_{\text{YM}}$) are the **same RG problem**:
controlling the running coupling from the perturbative UV into the
non-perturbative IR. The obstruction is precisely this UV→IR bridge — the
"where control runs out" boundary, structurally analogous to NS's
supercriticality, BSD's rank-≥2 Euler-system shape, Beal's distinct-odd-prime
class.

## Cross-problem compounding [[beals_conjecture]] [[birch_swinnerton_dyer]] [[navier_stokes]]

The "obstruction at the control/reduction step, not the resolution step" lens
is now **4-for-4**:
- **Beal** — reduction-to-finite-curves step.
- **BSD** — Selmer-group-control step.
- **NS** — critical-norm-control step.
- **YM** — continuum-limit + IR-gap-control step (+ framework-existence
  wrinkle).

The common spine: each problem has a "where control runs out" boundary.
Methodology page now clearly warranted (4 independent instances). `related`
links added across all four problems.

## Forward directions

- **(A) Lattice → continuum constructive** [[method-constructive-continuum-limit]]:
  Balaban RG + cluster expansions + OS reconstruction; transport a lattice
  spectral gap to the continuum, uniform in $a$. The recent attempts are this
  direction but conditional [ym-recent-claims-unverified].
- **(B) Non-lattice / geometric**: AdS-CFT (holographic QCD);
  Seiberg-Witten/Nekrasov (SUSY, solved related model); N=4 SYM integrability.
- **(C) Probabilistic / stochastic**: Chatterjee confinement mechanism (2021);
  regularity-structure / SPDE measure construction (Hairer).

## Theory toolbox filed this cycle

`def-yang-mills-theory`, `def-wightman-os-axioms`, `def-mass-gap-confinement`,
`thm-asymptotic-freedom`, `thm-lattice-gauge-constructive`, `thm-balaban-rg`,
`thm-seiberg-witten-supersymmetric`, `method-constructive-continuum-limit`;
source `ym-survey` (search-compiled, flagged [summary] / to-verify).

## Honesty / to-verify

Status facts from web-search summaries, **not primary sources**; flagged in
`ym-survey` and `progress.md`: the exact Jaffe-Witten wording, what Balaban's
RG proves vs leaves open, the peer-review status of each 2025-26 preprint
(Eriksson O(4) caveat, retracted Agawa addendum), Seiberg-Witten/Nekrasov
scope. **Critical**: the recent preprints are flagged
[ym-recent-claims-unverified] as attempts-to-study, NOT solutions — the same
discipline that caught the Beal (2,3,7) mislabel and kept PSS flagged until
verified.

## Next

Verify the load-bearing facts against primary sources (Jaffe-Witten Clay
write-up; Balaban's RG papers; the 2025-26 preprints' actual claims), then
deepen direction (A): what concretely blocks transporting a lattice spectral
gap to the continuum uniformly in $a$, and where does $O(4)$ covariance fail?