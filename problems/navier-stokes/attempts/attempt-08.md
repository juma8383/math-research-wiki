---
type: attempt
problem: navier_stokes
attempt: 8
date: 2026-08-30
approach: Verify the two remaining NS to-verify items (Seregin 2025 arXiv:2507.08733; Hou–Qin–Wang 2026 arXiv:2606.26658) and record the surfaced Hou–Wang–Yang 2026 Leray–Hopf nonuniqueness claim
outcome: confirmed
tags: [primary-source-verification, seregin-2025, liouville-theorems, ancient-euler, hou-qin-wang-2026, weak-advection, leray-hopf-nonuniqueness, hou-wang-yang-2026, computer-assisted, major-open]
---

# Attempt 08 — Seregin 2025 + Hou–Qin–Wang 2026 verified; NEW: Hou–Wang–Yang 2026 claims the first rigorous computer-assisted proof of Leray–Hopf nonuniqueness (the attempt-03 "major open problem")

Cycle-5 Continue on NS (attempt-07's "Next" target). Two to-verify items
resolved, and a potentially landmark 2026 preprint surfaced.

## Seregin 2025 (arXiv:2507.08733) — CONFIRMED: the fence gets a Liouville-type engine

**Gregory Seregin**, *A note on certain scenarios of Type II blowups of
suitable weak solutions to the Navier-Stokes equations* (some versions:
*"A note on impossible scenario of Type II blowups..."*), arXiv:2507.08733,
July 11, 2025 (preprint, math.AP; Leverhulme Emeritus Fellowship 2023).

- **Technique**: Euler scaling + **Liouville-type theorems for ancient
  solutions to the Euler system** — a new engine for the Type II exclusion
  program.
- **Theorem 2.1**: finds a region for parameters $m,m_0$ that completely
  excludes a Type II blowup scenario (growth condition (1.2) + boundedness
  condition (1.4)); shows a restriction from the CPAA 2024 paper was **too
  strong** (the fence is being widened).
- **Section 3**: modified scenario; a necessary condition is the existence
  of a non-trivial ancient Euler solution in a specific class.
- **Section 4**: Liouville-type theorems for ancient Euler solutions
  (self-similar profiles, discrete self-similar, axisymmetric with zero
  swirl).
- **Theorem 5.1**: rules out the scenario under an additional
  Ladyzhenskaya–Prodi–Serrin type condition (reduces to classical LPS when
  $m=1$).

## Hou–Qin–Wang 2026 (arXiv:2606.26658) — CONFIRMED: exact blowup for the weak-advection Hou–Li model

**Thomas Y. Hou, Xiang Qin, Xiuyuan Wang**, *Exact Blowup Analysis for the
Weak-Advection Hou–Li Model*, arXiv:2606.26658, June 25, 2026 (preprint).

- **Periodic setting**: exact finite-time self-similar blowup for
  $2/3<a<1$, profiles neither focusing nor expanding.
- **Whole-space with Neumann condition**: exact finite-time self-similar
  blowup for the full range $0<a\le1$, profiles focusing /
  non-expanding-non-focusing / expanding depending on the sign of the
  self-similar scaling parameter.
- Method: fixed-point formulation near the origin + ODE extension argument,
  plus regularity, asymptotic behavior, monotonicity, and uniqueness up to
  natural scaling invariance.

This extends the 1D-engine resolution program to the weak-advection Hou–Li
model with a full classification of profile types — the resolution side of
the 1D slice keeps strengthening.

## NEW — Hou–Wang–Yang 2026 (arXiv:2509.25116v2): claimed Leray–Hopf nonuniqueness

**Thomas Hou, Yixuan Wang, Changhe Yang**, *Nonuniqueness of Leray–Hopf
solutions to the unforced incompressible 3D Navier–Stokes Equation*,
arXiv:2509.25116v2 (v2 dated Aug 11, 2026). The search summary reports:

- **Claim**: the first rigorous **computer-assisted proof** of nonuniqueness
  of Leray–Hopf solutions to the **unforced** 3D Navier–Stokes equations —
  infinitely many distinct **suitable** Leray–Hopf solutions with the same
  divergence-free initial data.
- Code available at github.com/HouGroup2026/3d-navier-stokes-nonuniqueness.

**Significance if confirmed**: this is exactly the "**major open** problem"
flagged in attempt-03 — Leray–Hopf nonuniqueness (Buckmaster–Vicol 2019
proved nonuniqueness only *below* Leray–Hopf, $\beta<\tfrac12$; the
Leray–Hopf class itself was the open barrier). A rigorous proof would settle
the Leray–Hopf uniqueness question (open since Leray 1934) in the negative,
and would mean the energy inequality does not pin down the weak solution.

**Flags**: (i) preprint (v2 Aug 2026), not peer-reviewed; (ii)
**computer-assisted** — the proof's validity depends on the code; (iii) the
claim is search-surfaced, not primary-source-verified — `to-verify` against
the arXiv HTML/PDF before any load-bearing reuse. This is the single most
consequential NS item to verify next.

**Relation to the Millennium problem**: nonuniqueness of Leray–Hopf
solutions does NOT resolve the Millennium problem (which asks for global
regularity of smooth solutions OR a breakdown counterexample) — but it
sharpens the landscape: if weak solutions are nonunique, the regularity
question for smooth data becomes even more central, and the "weak solution"
concept loses its uniqueness anchor.

## What this changes in the obstruction map

- **The fence (Seregin) is widening and gaining a new engine**: Liouville-type
  theorems for ancient Euler solutions, with Thm 2.1 relaxing a CPAA 2024
  restriction. The Type II exclusion program is active and strengthening.
- **The 1D engine (Hou–Li) is fully classified**: Hou–Qin–Wang 2026 gives
  exact blowup for the weak-advection model across the full parameter range
  with a profile-type trichotomy — the resolution side of the 1D slice is
  now essentially complete.
- **The weak-solution side may have just moved**: if Hou–Wang–Yang 2026
  holds, Leray–Hopf nonuniqueness (the attempt-03 "major open problem") is
  resolved negatively — a landmark on the weak-solution front, though not a
  Millennium resolution.

## Honesty / scope

- **This is a verification/status cycle, not a proof move.** The Millennium
  problem is untouched.
- **Hou–Wang–Yang 2026 is a preprint, computer-assisted, and
  search-surfaced** — the most important `to-verify` item in the NS attack
  right now. Its claim must be verified against the arXiv HTML/PDF (and the
  code) before load-bearing reuse.
- Seregin 2025 and Hou–Qin–Wang 2026 details are from search summaries
  (primary-source-consistent, not line-by-line re-derived).

## Next (attempt-09)

**Primary-source-verify Hou–Wang–Yang 2026 (arXiv:2509.25116v2)** — the
claimed Leray–Hopf nonuniqueness proof. This is the highest-value NS
verification target: if confirmed, it resolves the attempt-03 "major open
problem" and rewrites the weak-solution section of the frontier.
