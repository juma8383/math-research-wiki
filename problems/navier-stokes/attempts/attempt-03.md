---
type: attempt
problem: navier_stokes
attempt: 3
date: 2026-08-24
approach: Verify the two remaining load-bearing to-verify items [ns-millennium-fefferman] (four statements + no-boundary domain) and [ns-buckmaster-vicol] (non-uniqueness scope) against primary sources
outcome: confirmed
tags: [verification, primary-source, fefferman-formulation, nonuniqueness, convex-integration, leray-hopf, cross-problem]
---

# Attempt 03 — Verify [ns-millennium-fefferman] + [ns-buckmaster-vicol]

Cycle-8 Continue on NS (cross-problem loop, second pass; yellow zone 60.1%
session / 47.3% weekly, 0 subagents). Attempt-02's `Next` offered two moves;
this cycle takes **(i)** — verify the last two to-verify items
`[ns-millennium-fefferman]` and `[ns-buckmaster-vicol]` against primary
sources. Same discipline that caught the Palasek mislabel (attempt-02) and
Beal's (2,3,7) spherical mislabel.

## Verification: [ns-millennium-fefferman] — CONFIRMED (four statements, no boundary)

**Confirmed against the official Clay formulation**, Charles L. Fefferman
(Princeton), *Existence and Smoothness of the Navier–Stokes Equation*, dated
May 1, 2000 ([claymath.org/millennium/navier-stokes-equation](https://www.claymath.org/millennium/navier-stokes-equation/); reprinted in the
Millennium Prize Problems volume, CMI/AMS 2006).

- **Two settings, both WITHOUT boundary:** (1) whole space $\mathbb R^3$,
  with rapid decay of the data/force at infinity (conditions (4), (5));
  (2) periodic torus $\mathbb R^3/\mathbb Z^3$, spatially periodic (conditions
  (8), (9)). Fefferman explicitly restricts to these to **avoid boundary
  complications** — confirms `progress.md`'s "domains without boundary."
- **Four statements (the "reasonable leeway" framing):** proving **any one**
  resolves the prize.

| | Existence & Smoothness | Breakdown |
|---|---|---|
| $\mathbb R^3$ | **(A)** for any smooth div-free $u_0$ (satisfying (4)), with $f\equiv0$, smooth $p,u$ on $\mathbb R^3\times[0,\infty)$ exist (smoothness (6), bounded energy (7)). | **(C)** there exist smooth div-free $u_0$ and smooth $f$ (satisfying (4),(5)) for which **no** such smooth solution exists. |
| $\mathbb T^3$ | **(B)** for any smooth div-free $u_0$ (satisfying (8)), with $f\equiv0$, smooth periodic $p,u$ exist (periodicity (10), smoothness (11)). | **(D)** there exist smooth div-free $u_0$ and smooth $f$ (satisfying (8),(9)) for which **no** such smooth solution exists. |

So A/B = global regularity for **all** data ($f\equiv0$); C/D = a
**blowup counterexample** (a smooth $f$ is *allowed* for the breakdown
statements). This matches `progress.md`'s A/B-vs-C/D frontier exactly and is
now primary-source-backed, including the no-boundary restriction and the
$f\equiv0$-for-regularity / $f$-allowed-for-breakdown asymmetry.

## Verification: [ns-buckmaster-vicol] — CONFIRMED + sharpened (non-Leray-Hopf only)

**Confirmed against the primary source**, with two genuine sharpenings.

- **Buckmaster–Vicol**, *Nonuniqueness of weak solutions to the Navier–Stokes
  equation*, **Annals of Math. 189**(1) (2019), 101–144, DOI
  [10.4007/annals.2019.189.1.3](https://doi.org/10.4007/annals.2019.189.1.3)
  (received 2017, accepted 2018, published Jan 2019). **Date correction:** the
  survey/`progress.md` did not pin a year; the result is **2019**, not 2022.
  The 2022 JEMS paper (*Wild solutions … singular sets … Hausdorff dim <1*)
  is **Buckmaster–Colombo–Vicol**, a *different* follow-up (JEMS 24(9), 2022,
  3333–3378, DOI 10.4171/jems/1162) — keep them distinct.

**Theorem 1.2 (nonuniqueness).** There exists $\beta>0$ such that for any
nonnegative smooth energy profile $e(t)\colon[0,T]\to\mathbb R_{\ge0}$ there is
a weak solution $v\in C^0_t([0,T];H^\beta_x(\mathbb T^3))$ of 3D NS with
$\int_{\mathbb T^3}|v|^2=e(t)$ (prescribed energy) and vorticity
$\nabla\times v\in C^0_t L^1_x$. Picking two profiles that agree on $[0,T/2]$
and differ at $T$ gives **nonuniqueness of dissipative weak solutions**
(coming to rest in finite time — Serrin's question). Theorem 1.3: Hölder
dissipative Euler weak solutions are vanishing-viscosity limits of these.

**The scope caveat — confirmed and made precise (the whole point of the
to-verify):** these solutions are **NOT Leray-Hopf.** They do **not** obey the
energy inequality
$\|v(t)\|^2_{L^2}+2\nu\int_0^t\|\nabla v\|^2_{L^2}\le\|v_0\|^2_{L^2}$ and lack
$L^2_t\dot H^1_x$ integrability. The regularity exponent $\beta$ **cannot be
too large**: at $\beta=\tfrac12$ one hits **weak-strong uniqueness** (so the
construction necessarily lives strictly below the Leray-Hopf/strong regime).
The authors state explicitly that **nonuniqueness of Leray-Hopf weak
solutions remains the major open problem.** So the to-verify hedge
("non-uniqueness is for non-Leray-Hopf / very-weak only") is **CONFIRMED**,
and the precise class is $C^0_t H^\beta_x$, $\beta<\tfrac12$, prescribed-energy,
no energy inequality.

**Mechanism (recorded for the toolbox):** convex integration building on
De Lellis–Székelyhidi / Isett (Onsager for Euler), with the new ingredient of
**intermittent Beltrami waves** — approximate curl-eigenfunctions with
$\|W\|_{L^1}\ll\|W\|_{L^2}$ (Dirichlet-kernel oscillations, frequency
param $r$), saturating Bernstein inequalities. The dissipative term
$-\nu\Delta v$ being linear forces the Reynolds-stress estimate into $L^1$,
and intermittency supplies the $L^1\ll L^2$ gain.

## Two cross-problem echoes the verification surfaced

1. **The 2D/3D divide recurs.** The Buckmaster–Vicol construction **fails in
   2D** — there are too few spatial directions to support the intermittent
   Beltrami-wave oscillations. This is a *second*, independent 2D-solved /
   3D-open dividing fact, alongside the Serrin-number equality
   ($S_{\rm nonlin}=S_{\rm lin}$ in 2D, $4>3.5$ in 3D) recorded in
   `progress.md`. The obstruction spine now has two parallel 2D/3D witnesses.
2. **Weak-strong uniqueness as the class boundary.** $\beta<\tfrac12$ is exactly
   the weak-strong-uniqueness threshold: above it the weak solution is
   governed by any strong solution, so nonuniqueness is impossible there. The
   nonuniqueness lives strictly below the physically natural class — the same
   "control step, not resolution step" shape: convex integration *resolves*
   (produces wild solutions) but only in a class that does **not** include the
   Leray-Hopf energy-controlled solutions, where the **control** (energy
   inequality) would forbid it.

## Sharpening to progress.md

- `progress.md` line "3D global Leray-Hopf weak solutions (non-unique?)"
  **sharpened:** Leray-Hopf **uniqueness is OPEN**; nonuniqueness is proven
  only **below** Leray-Hopf (Buckmaster–Vicol $C^0_tH^\beta_x$, $\beta<1/2$,
  no energy inequality). The "?" is resolved in the conservative direction
  (uniqueness still not refuted in the physically natural class).
- The BV date is **2019** (Annals 189), not the implied-recent; the 2022
  follow-up is Buckmaster–**Colombo**–Vicol (JEMS), a distinct paper.

## Honesty / scope

- Both to-verify items **CONFIRMED + sharpened.** Fefferman four-statement /
  no-boundary formulation primary-source-verified; Buckmaster–Vicol scope
  (non-Leray-Hopf, $\beta<1/2$, prescribed-energy, Leray-Hopf still open)
  primary-source-verified; BV date corrected to 2019; 2D-fails echo and
  weak-strong-uniqueness boundary recorded.
- No proof of global regularity or blowup. No progress on the frontier
  (global critical bound / true-NS blowup). The verification is the cycle's
  point — the last two `progress.md` to-verify items are now resolved.
- Outcome: **confirmed** (verification goal met, two sharpenings + one date
  correction), **partial** overall (frontier unchanged).

## Next (attempt-04)

With all `progress.md` to-verify items now resolved, the natural next move is
attempt-02's option **(ii)**: push the axisymmetric blowup program
quantitatively — can Seregin's no-exact/discrete-self-similarity conditions
(arXiv:2402.13229, still `to-verify` on publication) be evaded by a
**nearly**-self-similar Hou-type profile, and does the generalized
(solution-dependent-viscosity) → true constant-viscosity limit survive? The
refined open content for (B) (non-self-similar + viscosity bridge) is the
concrete control-step question, the NS instance of the cross-problem
obstruction.