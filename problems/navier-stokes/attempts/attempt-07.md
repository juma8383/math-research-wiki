---
type: attempt
problem: navier_stokes
attempt: 7
date: 2026-08-30
approach: Resolve the two remaining to-verify items from attempt-06 — Seregin 2024 (2402.13229) publication status, and the Huang–Qin–Wang–Wei CMP 2025 Hou–Luo blowup paper — plus record the new Seregin 2025 preprint
outcome: confirmed
tags: [primary-source-verification, seregin, type-ii-blowup, hou-luo-model, schauder-fixed-point, purely-analytic, publication-status, one-dimensional-engine, control-step]
---

# Attempt 07 — Seregin 2024 status resolved (still a preprint; CPAA 2024 is the published piece) + Huang–Qin–Wang–Wei CMP 2025 CONFIRMED: purely analytic exact self-similar blowup of the Hou–Luo model

Cycle-5 Continue on NS (rotation turn; the standing "next loop cycle on
resume" target). Two to-verify items from attempt-06 are resolved, and a new
2025 Seregin preprint is recorded.

## Seregin 2024 (arXiv:2402.13229) — publication status RESOLVED: still a preprint

- **No journal publication found.** The paper remains an arXiv preprint; the
  revised version (Oct 8, 2024) carries the retitled *"A note on potential
  Type II blowups of axisymmetric solutions to the Navier-Stokes equations"*
  (dedicated to Nikolai Nadirashvili).
- **Decisive evidence:** Seregin's own July 2025 preprint (arXiv:2507.08733)
  cites 2402.13229 as *"Seregin, G., On Type II blowups of axisymmetric
  solutions to the Navier-Stokes equations, arXiv:2402.13229v1"* — i.e., as a
  preprint, not a journal article.
- **The published Seregin piece is the predecessor:** *Remarks on Type II
  blowups of solutions to the Navier-Stokes equations*, **Comm. Pure Appl.
  Anal. 23(10) (2024), 1389–1406**, DOI 10.3934/cpaa.2023108 (dedicated to
  Vladimír Šverák) — the paper 2402.13229 builds upon (its reference [7]).
- **NEW: Seregin July 2025 preprint (arXiv:2507.08733)**, *A note on certain
  scenarios of Type II blowups of suitable weak solutions to the
  Navier-Stokes equations* — the Type II exclusion program continues.

So the asymmetric peer-review status recorded in attempt-05 **persists and
sharpens**: the candidate outside the fence (Hou 2024, published Found.
Comput. Math. 2026) is peer-reviewed; the fence itself (Seregin 2024) is
still a preprint — but the fence now has a **published predecessor** (CPAA
2024) and a **2025 extension preprint**, so the exclusion program is active
and ongoing, not stalled.

## Huang–Qin–Wang–Wei CMP 2025 — CONFIRMED: purely analytic exact self-similar blowup

**De Huang, Xiang Qin, Xiuyuan Wang, Dongyi Wei**, *Exact Self-Similar
Finite-Time Blowup of the Hou–Luo Model with Smooth Profiles*,
**Comm. Math. Phys. 406, article 243 (2025)**, DOI
[10.1007/s00220-025-05429-9](https://doi.org/10.1007/s00220-025-05429-9),
arXiv:2308.01528. Received 3 Nov 2024, accepted 29 July 2025, published
1 Sept 2025; communicated by A. Ionescu. (This upgrades attempt-06's
"to-verify" flag to CONFIRMED.)

Key facts:
- **Purely analytic** — the self-similar profiles are constructed by a
  **Schauder fixed-point argument** on a compact convex set in a weighted
  $L^\infty$ Banach space; **no computer assistance**.
- The profiles are **$C^\infty$ smooth**, with proven monotonicity/convexity
  and rigorous algebraic far-field decay rates.
- Scaling bound $2<c_l\le 2(\alpha+1)/(\alpha-1)\approx4.5298$ (with
  $\alpha=1+\sqrt{10}/2$) — cruder than the computer-assisted
  $2.99870\pm6\times10^{-5}$ of Chen–Hou–Huang (Ann. PDE 2022), but purely
  analytic.
- Builds on the authors' fixed-point framework for the generalized
  Constantin–Lax–Majda model (Huang–Qin–Wang–Wei, Arch. Ration. Mech. Anal.
  248, 2024).
- The authors identify the **2D Boussinesq equations** as the next target for
  the fixed-point framework.

## What this changes in the obstruction map

- **The "one-dimensional engine" sharpens again**: the 1D Hou–Luo model now
  has a **purely analytic** exact self-similar blowup proof with smooth
  profiles (Huang–Qin–Wang–Wei 2025), upgrading the computer-assisted
  Chen–Hou–Huang result. The 1D engine achieves blowup (resolution) *fully
  analytically*; the control step from the 1D/weakened slice to full 3D
  smooth data remains the wall. This is the cleanest NS mirror of the
  "obstruction at control, not resolution" thesis: the resolution side is
  now analytic, and the control side is untouched.
- **The fence is active but unpublished**: Seregin's Type II exclusion
  program (no exact/discrete self-similar axisymmetric blowup) has a
  published predecessor (CPAA 2024) and a 2025 extension preprint, but the
  main 2024 fence paper remains a preprint. The Hou/Seregin pair stays
  asymmetric in peer-review status.
- **The refined open content is unchanged**: a true 3D blowup must be
  non-(discrete-)self-similar (dodge Seregin) AND bridge generalized→true
  viscosity (Hou's gap). The new analytic 1D blowup proof does not move this
  boundary — it strengthens the *resolution* side of the 1D slice.

## Honesty / scope

- **This is a verification/status cycle, not a proof move.** The Millennium
  problem is untouched; no new 3D result.
- **Seregin 2025 (arXiv:2507.08733)** is recorded from the search summary
  (title + citation behavior confirmed; content not verified) — flagged
  `to-verify` if load-bearing.
- **Hou–Qin–Wang arXiv:2606.26658 (2026 preprint)** from attempt-06 remains
  `to-verify` (not searched this cycle).
- The Huang–Qin–Wang–Wei details (Schauder argument, $c_l$ bound, Boussinesq
  next step) are from the search summary — primary-source-consistent but not
  line-by-line re-derived from the CMP PDF.

## Next (attempt-08)

The natural next NS target: verify **Seregin 2025 (arXiv:2507.08733)** — the
new Type II exclusion scenarios — and **Hou–Qin–Wang 2026 (arXiv:2606.26658)**,
to see whether the fence has moved or the generalized→true-viscosity gap has
narrowed. Alternatively, rotate onward per the standing rotation.
