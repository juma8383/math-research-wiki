---
type: attempt
problem: yang_mills
attempt: 4
date: 2026-08-24
approach: Verify Chatterjee 2021 probabilistic confinement (direction C, named but unverified) + flag the 2025-26 preprint wave claiming full 4D YM construction
outcome: confirmed
tags: [verification, primary-source, confinement, center-symmetry, mass-gap, recent-claims, cross-problem]
---

# Attempt 04 — Verify Chatterjee 2021 (direction C) + flag the 2025-26 preprint wave

Cycle-14 Continue on YM (cross-problem loop, second pass; green zone 7.4%
session / 53.7% weekly, 0 subagents — fresh budget after the session
reset). Attempts 02-03 resolved every load-bearing to-verify item
(Jaffe-Witten, Balaban, Eriksson-status, supersymmetric). The remaining
named-but-unverified item was **direction (C): Chatterjee's probabilistic
confinement (2021)**, plus the open question of whether *any* nontrivial
4D YM continuum-limit result exists beyond Balaban's UV half. This cycle
verifies Chatterjee against the primary source and flags a **2025-26
preprint wave** claiming the full construction. Same discipline that
flagged Eriksson (viXra, conditional) and the Hodge/Collatz recent claims.

## Verification: Chatterjee 2021 — CONFIRMED (the mass gap is the hypothesis, not the conclusion)

Sourav Chatterjee (Stanford), *A Probabilistic Mechanism for Quark
Confinement*, **Communications in Mathematical Physics** (2021), DOI
[10.1007/s00220-021-04086-y](https://doi.org/10.1007/s00220-021-04086-y).

- **Theorem 2.2 (unbroken center symmetry ⟹ confinement):** for a lattice
  gauge theory with gauge group $G$ (closed connected subgroup of $U(n)$)
  on $\mathbb Z^d$ with unbroken center symmetry (rigorously defined via
  center transforms on slab configurations), any irreducible unitary
  representation $\pi$ acting nontrivially on the center of $G$ has Wilson
  loop expectations $|\langle W_\ell\rangle|\le e^{-V(R)T}$ with
  $V(R)\to\infty$ as $R\to\infty$ — **confinement / area law**.
- **Theorem 2.4 (exponential decay ⟹ unbroken center symmetry):** if the
  theory satisfies **exponential decay of correlations under arbitrary
  boundary conditions** (a strong condition), then center symmetry is
  unbroken, and hence (by Thm 2.2) Wilson's area law holds.
- **The rigorous definition of center symmetry** for lattice gauge theories
  is itself the contribution — previously only a 't Hooft physics heuristic.

### The crucial sharpening (the load-bearing fact for the obstruction map)

The implication chain is:
$$\text{exponential decay (mass gap)} \;\Longrightarrow\; \text{unbroken center symmetry} \;\Longrightarrow\; \text{confinement (area law)}.$$

**The mass gap (exponential decay of correlations) is the HYPOTHESIS, not
the CONCLUSION.** Chatterjee proves *confinement follows from the mass
gap* — he does **not** prove the mass gap exists. The paper's own caveat:
it does **not** prove that 4D SU($N$) lattice gauge theory satisfies the
exponential-decay condition at all coupling strengths. The mass gap is
easy to establish at **strong** coupling (cluster expansion) but is
**widely believed, not proven, at weak coupling**.

### What this means for direction (C) and the obstruction map

- Direction (C) is **NOT an escape** from the control step; it
  *relocates* it. Chatterjee gives a rigorous **resolution**-side tool
  (center symmetry ⟹ confinement, given exponential decay), but the
  **control** step — proving exponential decay (the mass gap) at weak
  coupling — remains open and is exactly the UV→IR bridge of attempts
  02-03. In lattice QFT, exponential decay of correlations **IS** the mass
  gap; so Chatterjee's result reads "**mass gap ⟹ confinement**," making
  the mass gap the single load-bearing open piece, now triangulated from
  a third angle (after Balaban's UV half and the SUSY dual-Meissner
  mechanism).
- **Control-step echo (6-for-6):** Chatterjee's center-symmetry engine
  **controls** the "center-symmetry ⟹ confinement" slice (resolution); the
  mass-gap-at-weak-coupling slice is where it **stops** and needs an input
  it cannot supply. Same "one-dimensional engine stops" shape — parallel
  to NS's Seregin (controls the self-similar slice, stops at the
  non-self-similar slice, attempt-04) and BSD's cyclotomic/anticyclotonic
  disjointness (attempt-04). YM's instance is now sharpest of the three:
  the *named mechanism* (confinement) is the *consequence*, and the
  *cause* (mass gap) is the open control step.

## Flagging the 2025-26 preprint wave (honesty discipline)

The search surfaced a recent wave of preprints claiming the full 4D YM
construction. **NONE peer-reviewed; each with identified limitations.**
Flagged `ym-recent-claims-unverified` (extension of the attempt-02 list):

- **Shabir & Faizal 2026**, arXiv:2606.19362, *Reflection-Positive
  Construction of a Four-Dimensional SU($N$) Yang-Mills Theory with Mass
  Gap and Confinement* (~200+ pages): reflection-positive lattice + OS
  axioms + finite-range decomposition + strong-coupling cluster expansion
  + RG interlacing inequalities + Wilson-loop step-scaling + OS
  reconstruction; claims $\Delta\ge\min(\Delta_\star,m_\star)>0$, continuum
  area law $\mathcal W(C)\le e^{-\sigma A(C)}$, linear confining potential,
  universality. **Preprint, not peer-reviewed**; companion papers in
  *Int. J. Geom. Meth. Mod. Phys.* (2026). To-verify on the admissible-
  class framework and the RG-interlacing defect summability.
- **Agawa 2025**, Cambridge Open Engage, *A Rigorous Proof of the Mass
  Gap in SU($N$) Yang-Mills Theory* (v2) + addendum (2025-06-18):
  non-local holonomy formulation + Balaban-type multi-scale cluster
  expansion + holonomy gauge-fixing (claims no Gribov copies) + OS via
  checkerboard. **Preprint, not peer-reviewed; author unaffiliated,
  acknowledges significant AI assistance; addendum needed for continuum
  limit + finite Gribov.** Flagged unverified.
- **Eriksson 2026** (viXra): already flagged in attempt-02 (viXra-only,
  conditional on Assumption A, OS/thermodynamic-limit/mass-gap open even
  conditionally, abstract-vs-body $O(4)$/hypercubic discrepancy). The
  search confirms Eriksson's *own honest assessment*: does not prove the
  RG-Cauchy estimate, postulates the transfer-matrix spectral gap, does
  not construct renormalized local fields as operator-valued
  distributions. **Still not load-bearing.**

**Bottom line (the sharpened frontier):** Chatterjee 2021 (published, CMP)
is the rigorous state of the art — it proves *confinement follows from the
mass gap* but not the mass gap itself. The 2025-26 wave (Shabir-Faizal,
Agawa, Eriksson) all claim the full construction but are **all unpeer-
reviewed**, each with conditional assumptions or identified gaps; **none
accepted**. The rigorous construction of 4D YM with a proven continuum
mass gap remains **open** — the frontier is unchanged, but the obstruction
is now triangulated from three angles (Balaban UV-half / SUSY
dual-Meissner / Chatterjee mass-gap-⟹-confinement), all converging on the
same UV→IR control step.

## Honesty / scope

- Chatterjee 2021 CONFIRMED against the primary source (CMP, DOI
  10.1007/s00220-021-04086-y); the mass-gap-as-hypothesis sharpening +
  the weak-coupling-exponential-decay open piece recorded.
- The 2025-26 preprints (Shabir-Faizal, Agawa, Eriksson) flagged
  `ym-recent-claims-unverified`; none peer-accepted; same discipline as
  the Hodge (Shimizu/Bouari/Abdelgalil) and Collatz (Fathi/Nwankpa/Chang)
  flagging.
- No rigorous 4D quantum YM, no proven continuum mass gap. The
  verification is the cycle's point: direction (C) is now primary-source-
  backed and shown to relocate (not remove) the control step; the
  preprint wave is fenced off.
- Outcome: **confirmed** (Chatterjee verified + mass-gap-as-hypothesis
  sharpening + three-angle obstruction triangulation + preprint wave
  flagged), **partial** overall (frontier unchanged).

## Next (attempt-05)

The YM to-verify list is now exhausted (all items resolved or claim-
verified). Natural next moves: (a) monitor Shabir-Faizal / Agawa for peer
review / community reception (a status-check Continue), or (b) deepen
direction (A) — the uniform-in-$a$ IR bound bridging the strong↔weak
crossover (the literal UV→IR bridge, now the single load-bearing control
step named from three angles). The rotation continues: next cross-problem
cycle → hodge-conjecture (attempt-04) per the rotation, OR beals
(occasional cycle-in).