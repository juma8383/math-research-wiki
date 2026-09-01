---
type: attempt
problem: navier_stokes
attempt: 2
date: 2026-08-24
approach: Verify load-bearing blowup/regularity facts against primary sources (Tao 2019, ESS 2003), then deepen direction (B) — what blocks removing the averaging in Tao's blowup model
outcome: confirmed
tags: [verification, primary-source, blowup-rate, averaged-ns, axisymmetric, cross-problem, correction]
---

# Attempt 02 — Verify the blowup/regularity base; deepen the blowup program

Cycle-2 Continue on NS, following attempt-01's `Next`: verify the
load-bearing facts (Fefferman; ESS 2003; Tao 2016/2019; Barker 2022), then
deepen direction (B). Verification is not a formality — it caught a mislabel
this cycle (see below), as it caught Beal's (2,3,7) spherical error.

## Verification: [ns-tao-quant-l3] — CONFIRMED (triple log, exact)

**Confirmed against the primary source.** Tao, *Quantitative bounds for
critically bounded solutions to the Navier-Stokes equations*, Proc. Symp.
Pure Math. (2021), arXiv:1908.04958 (2019), DOI
[10.1090/pspum/104/01874](https://doi.org/10.1090/pspum/104/01874). The exact
blowup criterion: if $[0,T^*)$ is maximal smooth and $T^*<\infty$,
$$\limsup_{t\uparrow T^*}\frac{\|u(t)\|_{L^3_x(\mathbb R^3)}}
{\bigl(\log\log\log\frac1{T^*-t}\bigr)^c}=\infty,\qquad c>0.$$
So the **critical $L^3$ norm must blow up faster than a triple logarithm** —
exactly as recorded. First "(very slightly) supercritical" blowup criterion.
The three logs come from: Bourgain pigeonholing (one exp) + Carleman/unique-
continuation (one exp) + stacking of scales (one exp).

Refinements verified:
- **Barker–Prange (2021)**, *Quantitative Regularity for NS via Spatial
  Concentration*, Comm. Math. Phys. **385** (2021), 717–792 (DOI
  10.1007/s00220-021-04122-x) — Type I blowup rate, local-in-space smoothing
  (Jia–Šverák) + Carleman.
- **Barker (2022)**, *Localized quantitative estimates and potential blow-up
  rates for the NS equations*, arXiv:2209.15627 — **localized** the $L^3$
  blowup rate to any neighborhood of a singular point (improving Tao's global
  result to local). Matches `progress.md` "Barker (2022) localized this."

## Verification: [ns-ess-endpoint] — CONFIRMED (endpoint Serrin)

**Confirmed.** Escauriaza–Seregin–Šverák, *$L_{3,\infty}$-solutions of the
Navier–Stokes equations and backward uniqueness*, Russian Math. Surveys
**58**:2 (2003), 211–250 (DOI 10.1070/RM2003v058n02ABEH000609). They proved
$L^\infty_t L^3_x$ (i.e. $L^{3,\infty}$) solutions are **smooth** — the endpoint
Serrin case $s=3,\ell=\infty$ of the Serrin–Prodi–Ladyzhenskaya condition
$3/s+2/\ell=1$. Method: reduction to **backward uniqueness** for the heat
operator (vorticity equation) via two new **Carleman inequalities**. Corollary:
at a finite singularity, $\limsup_{t\uparrow T^*}\int|v|^3=+\infty$ — the
**qualitative** precursor that Tao (2019) made **quantitative** (triple log).

> Convention check: our notes write the Serrin condition as $2/r+3/s=1$ with
> $(r,s)=$ (time, space); ESS write $3/s+2/\ell=1$ with $(s,\ell)=$ (space,
> time). Same condition, letters swapped — **not** an error, just record the
> variable convention to avoid confusion.

## ⚠️ MISLABEL CAUGHT — [ns-tao-quant-l3] Palasek attribution (corrected)

`progress.md` and `attempt-01` both say *"Palasek sharpened it for
**axisymmetric** data."* The primary source shows otherwise:

- **Palasek (2022)**, *A Minimum Critical Blowup Rate for the High-Dimensional
  Navier–Stokes Equations*, J. Math. Fluid Mech., arXiv:2111.08991 — extended
  Tao's rate to **dimensions $d\ge4$**, where it becomes a **quadruple**
  logarithm (one more than 3D, from the lack of "bounded total speed" +
  quantitative epochs of regularity in higher dimensions). **Not axisymmetric.**

This is corrected append-only: `progress.md` "running state" updated to the
correct attribution; `attempt-01` left intact with a dated correction blockquote
pointer to this attempt. The "axisymmetric" thread is real but lives in the
Hou/Seregin blowup program below (different authors), not in Palasek. Same
discipline as Beal's (2,3,7) spherical→hyperbolic correction.

## Deepening direction (B): the blowup program, concretely

### Tao's averaged-NS blowup and the obstruction to removing the averaging

Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes
equation*, J. Amer. Math. Soc. (2016), DOI
[10.1090/jams/838](https://doi.org/10.1090/jams/838) [[thm-tao-averaged-blowup]].

The **averaged** bilinear operator
$$\tilde B(u,v)=\int T_1\,B(T_2u,\,T_3v)\,d\mu(\omega),$$
($T_i$ = rotations / dilations / order-0 Fourier multipliers) preserves the
energy identity $\langle\tilde B(u,u),u\rangle=0$ and all harmonic-analysis
estimates the true Euler operator $B$ satisfies — **yet admits finite-time
blowup**. Mechanism: a "quadratic circuit" of ODEs built from "quadratic logic
gates" (pump, amplifier, rotor) → a delayed, abrupt, **self-replicating**
energy cascade ("von Neumann machine" in fluid).

**The concrete block on removing the averaging (= direction (B) core):**
$\tilde B$ has **tunable degrees of freedom** (the rotations/dilations/
multipliers $T_i$) that the **rigid** true nonlinearity $(u\cdot\nabla)u$ lacks.
Removing the averaging means the logic gates must be built from $(u\cdot\nabla)u$
with no tuning. Tao: *"there is no mathematical barrier to such a machine
existing… there is however an immense engineering barrier to actually
constructing such a machine, even on paper."* Equivalently: any regularity
proof using **only** the energy identity + abstract nonlinearity estimates
**cannot** succeed — one must exploit finer structure (vorticity, unique
continuation). This is the control-step obstruction in its sharpest form:
the averaged operator *has* the control freedom; the true operator does not.

### The axisymmetric ansatz — the leading geometric candidate (and its obstructions)

Two 2024 works sharpen the axisymmetric sub-thread (both arXiv preprints →
flagged `to-verify` on publication status, results treated as evidence not
proof):

- **Hou (2024)**, *Nearly self-similar blowup of generalized axisymmetric
  Navier–Stokes equations*, arXiv:2405.10916. Derives axisymmetric NS with
  swirl in real-valued dimensions; a novel **two-scale dynamic rescaling** uses
  the dimension $n(t)=1+2R(t)/Z(t)$ as a free parameter to kill **scaling
  instability** (the key obstruction). Strong **numerical** evidence for
  nearly-self-similar blowup with *solution-dependent* viscosity
  $\nu(t)=\nu_0\|u_1\|_\infty Z(t)^2$, effective dimension $n(t)\to3.188$ ($\to3$
  as background viscosity $\to0$); vorticity growth $\sim10^{30}$; all
  blowup criteria (BKM, LPS, $L^\infty$, pressure) violated. **Suggestive, not a
  proof for true constant-viscosity 3D NS** — the blowup is for the generalized
  (solution-dependent-viscosity) model, though the profile satisfies
  axisymmetric NS with constant $\nu_0$.

- **Seregin (2024)**, *A note on potential Type II blowups of axisymmetric
  solutions to the NS equations*, arXiv:2402.13229. Under axial symmetry the
  limiting Euler equations have **no swirl**; $|\omega_\vartheta|^{l_1/2}/|x'|
  ^{l_1/2}$ is conserved; **exact self-similar** profiles are trivially zero
  (Prop 3.1) and **discrete self-similarity** is also ruled out (Prop 4.1)
  under conditions. So Seregin **rigorously obstructs** exact/discrete-self-
  similar axisymmetric Type II blowup — constraining where a blowup can live.

**Tension = the refined open content for (B):** Hou suggests a
*nearly*-self-similar axisymmetric blowup may be achievable as $n\to3$;
Seregin rules out *exact/discrete* self-similarity under conditions. So a true
blowup, if it exists, must be **non-self-similar** (or violate Seregin's
integrability conditions) and must bridge from the generalized (tunable-
viscosity) model to the rigid constant-viscosity equation. The gap
"averaged-NS blowup → true-NS blowup" now has a concrete **geometric axis**
(axisymmetric, nearly-self-similar) and a concrete **obstruction** (the tuning
freedom of $\tilde B$; Seregin's no-exact-self-similarity constraints).

## Outcome

`confirmed` for the verification goal (two load-bearing facts primary-source
verified, one mislabel caught + corrected append-only); `partial` for the
conjecture overall (no global-regularity proof, no true-NS blowup). Direction
(B) block concretized: removing the averaging = building "fluid logic gates"
from the rigid $(u\cdot\nabla)u$ (no $T_i$ tuning freedom); axisymmetric
nearly-self-similar is the leading candidate, obstructed by Seregin's
no-exact-self-similarity and the generalized→true-viscosity gap.

## Files touched

- NEW: this `attempt-02.md`.
- Updated: `attempt-01.md` (dated correction blockquote on the Palasek
  attribution), `progress.md` (to-verify items resolved; direction (B)
  deepened; Palasek correction), `index.md`, `log.md`.
- `thm-tao-averaged-blowup` to be updated with the $\tilde B$ mechanism + the
  removal obstruction (next cycle or now).

## Next (attempt-03)

Either (i) verify the remaining to-verify items `[ns-millennium-fefferman]`
(four statements + no-boundary domain) and `[ns-buckmaster-vicol]`
(non-uniqueness scope: very-weak, non-Leray-Hopf only), or (ii) push the
axisymmetric blowup program quantitatively: can Seregin's no-self-similarity
conditions be evaded by a *nearly*-self-similar (Hou-type) profile, and does
the generalized→true-viscosity limit survive?