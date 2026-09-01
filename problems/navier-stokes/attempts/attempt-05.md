---
type: attempt
problem: navier_stokes
attempt: 5
date: 2026-08-24
approach: Status-check Continue — resolve the lingering publication-status to-verify flag on the two 2024 axisymmetric preprints (Hou 2405.10916, Seregin 2402.13229), and survey 2025-26 community reception
outcome: confirmed
tags: [status-check, publication-status, axisymmetric, blowup, hou, seregin, cross-problem]
---

# Attempt 05 — Status-check: Hou 2024 published (FoCM 2026); Seregin 2024 still preprint

Cycle-18 Continue on NS (cross-problem loop, second pass; green zone
37.5% session / 59.0% weekly, 0 subagents — weekly about to tip yellow).
The NS to-verify list is exhausted on *claims* (attempt-04 verified
both preprints' content); the one lingering flag was
**publication status** (both arXiv preprints as of attempt-04, "treated
as evidence, not proof, until peer-reviewed"). This cycle is a
status-check Continue: re-survey the two preprints + their 2025-26
reception. Same discipline that produced the BSD citation-upgrade
(Kim arXiv→Trans. AMS 2024, attempt-05) and the NS Buckmaster-Vicol
date correction (2019 not 2022, attempt-03).

## Headline: Hou 2024 is now PUBLISHED (Foundations of Computational Mathematics, 2026)

**Thomas Y. Hou**, *Nearly Self-similar Blowup of Generalized
Axisymmetric Navier–Stokes Equations*, **Foundations of Computational
Mathematics** (Springer, 2026), DOI
[10.1007/s10208-026-09748-8](https://doi.org/10.1007/s10208-026-09748-8)
(= arXiv:2405.10916; arXiv v2 also covered "and Boussinesq equations,"
v3 drops it). **FoCM is a strong, peer-reviewed journal** — so the Hou
blowup claim (for *generalized* axisymmetric NS) is now **published**, not
just a preprint. This resolves the `[ns-hou-2024]` publication-status flag:
**upgrade from "preprint, evidence" to "peer-reviewed publication."**

The published content matches attempt-04's verification (the two-section
construction: Sec 4 solution-dependent viscosity, self-similar
n≈3.188→3, BKM-violating O(1/(T−t)); Sec 5 two-constant-viscosity
Boussinesq, nearly-self-similar with log correction
λ=(1+ε|log(T−t)|)^{−1/2}, n≈4.73). The load-bearing caveat —
**generalized axisymmetric NS, NOT true constant-viscosity 3D NS** —
is unchanged by publication; FoCM accepted it *as a generalized-model
blowup*, not as a true-NS blowup.

## Community reception (active engagement, no refutation)

- **NYU Courant Analysis Seminar** (Hou, "Nearly self-similar blowup of
  generalized axisymmetric Navier-Stokes equations") and **UCB/LBL
  Applied Math Seminar, Spring 2025** (Hou, "Recent progress on
  potential singularity of the 3D Navier-Stokes equation and related
  models") — active seminar circulation, not refutation.
- A **related quasi-exact-1D-model paper** (*Blowup analysis for a
  quasi-exact 1D model of 3D Euler and Navier–Stokes*, Nonlinearity,
  DOI [10.1088/1361-6544/ad1c2f](https://doi.org/10.1088/1361-6544/ad1c2f))
  extends the Hou-group program to a rigorously analyzable 1D model — a
  *supporting* line, not a challenge. (Not deepened this cycle; flagged
  for a future attempt if direction (B) is revisited.)

## Seregin 2024 (arXiv:2402.13229) — still a preprint (the published piece is distinct)

The search surfaced **no journal DOI** for Seregin's 2024 arXiv:2402.13229
(*A note on potential Type II blowups of axisymmetric solutions to the
Navier-Stokes equations*) — only the arXiv DOI 10.48550/arxiv.2402.13229.
The **published** Seregin piece is the **distinct, earlier** *Remarks
on Type II blowups of solutions to the Navier-Stokes equations*, **Comm.
Pure Appl. Anal. (2023)**, DOI
[10.3934/cpaa.2023108](https://www.aimsciences.org/article/doi/10.3934/cpaa.2023108)
— already noted in attempt-04 as "a related earlier note, distinct from
this 2024 piece." So:

- **Hou**: preprint → **published (FoCM 2026)** ✓ (flag resolved,
  upgraded).
- **Seregin 2024 (2402.13229)**: **still a preprint** as of this check;
  its *claims* (verified attempt-04) stand, but the publication-status
  flag persists. The 2023 cpaa note is a published companion (narrower,
  Type II remarks), not a substitute.

## What this changes in the obstruction map

- `[ns-hou-2024]` publication-status flag **RESOLVED** — upgraded to
  peer-reviewed (FoCM 2026, DOI 10.1007/s10208-026-09748-8). The
  complementary-not-contradictory Hou/Seregin picture (attempt-04) is
  now **asymmetric in peer-review status**: Hou published, Seregin
  2024 still preprint. This sharpens the honesty framing: the
  *fence* (Seregin's exclusion of exact/discrete self-similar Type II)
  is the un-peer-reviewed side; the *candidate outside the fence* (Hou's
  nearly-self-similar generalized blowup) is now the peer-reviewed side
  — an unusual but accurate status asymmetry.
- **No change to the frontier or the control-step obstruction.** Hou's
  publication is a generalized-model blowup, not a true-NS blowup; the
  refined open content from attempt-04 stands: a true blowup must be
  (i) non-(discrete-)self-similar (dodge Seregin) AND (ii) bridge the
  generalized→true-viscosity limit (Hou's gap, now peer-reviewed as a
  gap, not closed).
- **Control-step echo unchanged:** Seregin's engine fences off the
  self-similar slice; Hou's nearly-self-similar/generalized candidate
  lives where it stops — published status does not move the slice
  boundary.

## Honesty / scope

- Hou 2024 publication CONFIRMED: *Found. Comput. Math.* (2026), DOI
  10.1007/s10208-026-09748-8 (= arXiv:2405.10916); peer-reviewed. The
  generalized-not-true-NS caveat survives publication.
- Seregin 2024 (arXiv:2402.13229) **still a preprint** at this check —
  the publication-status flag persists for it (claims verified attempt-04;
  the published Seregin piece is the distinct 2023 cpaa note). To re-check
  in a later cycle.
- Community engagement (Courant, UCB/LBL seminars; the 1D-model
  Nonlinearity paper) is supportive/active, no refutation found — but
  "no refutation found in a search" is weak evidence of acceptance, not
  proof of correctness. Flagged honestly.
- No blowup for true 3D NS; no proof of global regularity. The frontier
  is unchanged; the cycle's point is the publication-status resolution
  (Hou) + the asymmetric-status sharpening of the Hou/Seregin pair.
- Outcome: **confirmed** (Hou publication-status flag resolved +
  upgraded to FoCM 2026; Seregin-2024 status re-confirmed still
  preprint; asymmetric peer-review status recorded; community
  reception surveyed), **partial** overall (frontier unchanged).

## Next (attempt-06)

Natural next moves: (a) re-check Seregin 2024 (2402.13229) for journal
publication in a later cycle (the one persistent NS status flag), or
(b) deepen direction (A) — the critical a priori bound (the missing
control step directly) — surveying recent attempts, or (c) dig into the
quasi-exact-1D-model Nonlinearity paper (a rigorously analyzable Hou-
group model, a potential new direction-(B) ingredient). The rotation
continues: next cross-problem cycle → yang-mills (attempt-05) per the
rotation order, OR beals (occasional cycle-in).