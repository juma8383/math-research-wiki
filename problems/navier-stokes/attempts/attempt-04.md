---
type: attempt
problem: navier_stokes
attempt: 4
date: 2026-08-24
approach: Verify the two 2024 axisymmetric preprints (Hou arXiv:2405.10916, Seregin arXiv:2402.13229) flagged to-verify in attempt-02, against the arXiv primary source, pinning exact claims + the complementary-not-contradictory relationship
outcome: confirmed
tags: [verification, primary-source, axisymmetric, blowup, type-ii, self-similar, cross-problem]
---

# Attempt 04 — Verify Hou 2024 + Seregin 2024 axisymmetric preprints

Cycle-13 Continue on NS (cross-problem loop, second pass; orange zone
87.9% session / 52.2% weekly, 0 subagents). Attempts 02-03 resolved every
*load-bearing* to-verify item (Tao triple-log, ESS endpoint, Fefferman
formulation, Buckmaster-Vicol). The two remaining flagged items were the
**2024 axisymmetric preprints** — Hou arXiv:2405.10916 and Seregin
arXiv:2402.13229 — left `to-verify` on publication status in attempt-02.
This cycle verifies their *claims* against the arXiv HTML and pins the
complementary relationship. Same discipline that caught the NS
Buckmaster-Vicol date (2019 not 2022) and the Palasek high-dimensional
(not axisymmetric) mislabel.

## Verification 1: Hou 2024 (arXiv:2405.10916) — CONFIRMED

Thomas Y. Hou (Caltech), *Nearly self-similar blowup of generalized
axisymmetric Navier-Stokes equations*, arXiv:2405.10916 (2024). Two-part
construction:

- **Rigorous derivation of axisymmetric NS with swirl in any integer
  dimension n>3**, then generalized to arbitrary positive real dimensions,
  preserving circulation conservation, incompressibility, energy
  conservation, and known non-blowup criteria.
- **Two-scale dynamic rescaling** with the space dimension n as an
  *additional dynamic degree of freedom*: n(t)=1+2R(t)/Z(t) (independent
  r- and z-rescaling). This eliminates scaling instability and prevents
  two-scale blowup structures, enabling a one-scale self-similar solution.
- **Section 4 (solution-dependent viscosity):** ν(t)=ν₀‖u₁‖∞Z(t)²,
  ν₀=0.006. A **stable self-similar blowup**: effective dimension n≈3.188
  →3 as ν₀→0; scaling exponent c_l≈0.523; max vorticity O(1/(T−t)),
  **violating the Beale-Kato-Majda criterion**; max vorticity up 9×10²¹
  by τ=185. Surprising sub-fact: the self-similar profile satisfies NS
  with **constant** viscosity ν₀ (the solution-dependent viscosity
  vanishes yet retains an O(1) effect).
- **Section 5 (two constant viscosities, Boussinesq-type):** ν₁=6×10⁻⁴
  (Γ), ν₂=6×10⁻³ (ω₁). A **nearly self-similar** blowup with a
  **logarithmic correction** λ(t)=(1+ε|log(T−t)|)^(−1/2); max vorticity
  up 1.4×10³⁰ by τ=155; dimension settles at n≈4.73, consistent with
  Cheskidov's diadic-model blowup threshold n>4.

**Scope (the load-bearing caveat, CONFIRMED):** this is **generalized
axisymmetric NS** — Section 4 uses *solution-dependent* viscosity, Section
5 uses a *modified Boussinesq-type system with two constant viscosities* —
**NOT true constant-viscosity 3D NS**. progress.md's caveat ("for
generalized (solution-dependent-viscosity) NS, not true constant-viscosity
NS") is correct and now sharpened with the two-section split.

## Verification 2: Seregin 2024 (arXiv:2402.13229) — CONFIRMED

Gregory Seregin (Oxford/Steklov), *A note on potential Type II blowups of
axisymmetric solutions to the Navier-Stokes equations*, arXiv:2402.13229
(2024). Type II blowups (g=∞) of axisymmetric suitable weak solutions via
**Euler scaling** v(x,t)→λ^α v(λx,λ^{α+1}t), q→λ^{2α}q, α=2−m=(4−m₀)/(2+m₀),
½≤m<1 (2/5≤m₀<1).

- **Proposition 1.1:** under boundedness assumptions (eq 1.3, 1.5) a
  nontrivial **Euler** blowup solution u is extracted in
  Q₋=ℝ³×(−∞,0), satisfying the local energy inequality. The Euler limit
  has **no swirl** (u_ϑ=0): rv_ϑ scales as λ^{α−1}·rv_ϑ and α−1<0 forces
  the swirl to vanish in the limit.
- **Proposition 2.1 / Lemma 2.1:** under condition m<(9−4s₁)/(7−2s₁),
  the **weighted vorticity** g(t)=∫Φ(|f|)dx, f=ω_ϑ(u)/r, is conserved
  (estimate ∫|gₐ'(t)|dt ≤ c·a^{m₁/2+γ*s₁/2−1}→0).
- **Proposition 2.2:** if additionally ess sup ∫|v|^q dx <∞ with
  q=3/(2−m)∈[2,3), then z=0 is a **regular point** (u(·,0)=0 ⇒ ω(·,0)=0
  ⇒ u irrotational, contradicting nontriviality). Cor 2.3: same for
  ‖∇×v‖_{L^{q₁}}, q₁=3/(3−m)∈[6/5,3/2).
- **Proposition 3.1:** under the self-similarity ansatz (3.3) + condition
  (3.7), the profile U must be **identically zero** — **no self-similar
  Type II blowup**.
- **Proposition 4.1:** for periodic-in-time (discrete self-similar)
  profiles, under (2.4)+(2.5), U≡0 — **no discrete self-similar Type II
  blowup**.

progress.md's summary ("rigorously rules out exact/discrete-self-similar
axisymmetric Type II blowup under conditions (no-swirl limiting Euler;
conserved |ω_ϑ|^{l₁/2}/|x'|^{l₁/2})") is CONFIRMED; the conserved quantity
is the weighted vorticity g(t)=∫Φ(|f|)dx, f=ω_ϑ/r, and the mechanism is the
irrotationality contradiction (Prop 2.2).

## The relationship: complementary, NOT contradictory (the sharpening)

The two results operate in **different scopes** and are complementary:

| | Hou 2405.10916 | Seregin 2402.13229 |
|---|---|---|
| Approach | Numerical (dynamic rescaling) | Theoretical (Euler scaling limits) |
| Equation | Generalized axisymmetric NS, fractional dim n | 3D axisymmetric NS, standard scaling |
| Self-similar profile | Exists (Sec 4) / nearly (Sec 5, log correction) | **Ruled out** (exact + discrete, Prop 3.1/4.1) |
| Viscosity | Solution-dependent (Sec 4) / two constant (Sec 5, Boussinesq) | Standard NS |
| Dimension | n≈3.188→3, or n≈4.73 | Fixed 3D |

Seregin constrains the **classical exact/discrete self-similar Type II**
scenario (3D, standard NS scaling, under his boundedness + L^q + no-swirl-
Euler conditions). Hou's candidate lives **outside** that scope: fractional
dimension + modified (solution-dependent or Boussinesq-type) viscosity +
the **logarithmic correction** λ(t)=(1+ε|log(T−t)|)^(−1/2) makes it
*nearly* self-similar, not exactly self-similar. So the two do not
contradict; rather Seregin fences off the exact-self-similar class and
Hou's blowup sits in the residual nearly-self-similar/generalized class
Seregin does not cover.

## Refined open content + control-step echo

This sharpens progress.md's direction (B) refined open content:
- A **true** 3D NS blowup must be **(i) non-(discrete-)self-similar** to
  dodge Seregin's Prop 3.1/4.1, AND **(ii) bridge the
  generalized→true-viscosity limit** (Hou's blowup is generalized, not
  true constant-viscosity 3D NS). Hou's log-corrected nearly-self-similar
  ansatz is precisely the form that dodges (i); the open part is (ii).
- **Control-step echo (the 6-for-6 sub-pattern in microcosm):** Seregin's
  no-swirl-limiting-Euler + weighted-vorticity-conservation engine
  **controls the self-similar slice** (rules it out). The residual
  freedom — the non-self-similar / generalized-viscosity slice — is exactly
  where the engine **stops** and where Hou's candidate lives. This is the
  same "one-dimensional engine stops" shape: a control tool fences off
  one class, and the open content is the class just beyond its reach.
  Parallel to BSD's cyclotomic-vs-anticyclotomic disjointness (attempt-04,
  the comparison where the two engines stop) and Collatz's two engines
  both stopping at almost-all (attempt-03).

## Honesty / scope

- Hou 2024 + Seregin 2024 CONFIRMED against the arXiv HTML; exact claims
  (two-section split, n≈3.188/4.73, log correction, no-swirl Euler,
  weighted-vorticity conservation, Prop 2.2/3.1/4.1) pinned.
- **Publication status persists:** both remain arXiv preprints (no journal
  publication found in the search; Seregin has a *related* earlier note
  "Remarks on Type II blowups," Comm. Pure Appl. Anal. 2023, cpaa.2023108,
  distinct from this 2024 arXiv piece). Results treated as evidence, not
  proof, until peer-reviewed — the `to-verify` on *publication status*
  remains; the `to-verify` on *claims* is now resolved.
- No blowup for true 3D NS; no proof of global regularity. The frontier
  (global regularity for large 3D data / true-NS blowup) is unchanged.
- Outcome: **confirmed** (both preprint claims verified + complementary
  relationship pinned + control-step echo), **partial** overall.

## Next (attempt-05)

The NS to-verify list is now exhausted (all items resolved or
claim-verified). Natural next moves: (a) monitor Hou/Seregin for journal
publication / community reception (a status-check Continue), or (b) deepen
direction (A) — survey recent critical-a-priori-bound attempts (the
missing control step directly). The rotation continues: next cross-problem
cycle → yang-mills (attempt-04) per the rotation, OR beals (occasional
cycle-in).