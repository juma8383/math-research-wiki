---
type: attempt
problem: navier_stokes
attempt: 6
date: 2026-08-24
approach: Verify + characterize the Hou-group quasi-exact 1D model (Nonlinearity 2024) — a rigorously analyzable direction-(B) ingredient — and test it against the cross-problem "one-dimensional engine stops" sub-pattern
outcome: confirmed
tags: [verification, primary-source, 1d-quasi-exact-model, blowup, hou-li, direction-B, one-dimensional-engine-stops, cross-problem, computer-assisted]
---

# Attempt 06 — Hou-Wang 1D quasi-exact model: blowup PROVABLE in 1D, stops at the 3D control step (sharpens the "one-dimensional engine stops" pattern)

Cycle-24 Continue on NS (cross-problem loop, second pass; **FINAL cycle** —
24-cycle cap reached; **orange zone** session 85.2% / weekly 67.4%, max 1
subagent — **0 used**, one targeted WebSearch to conserve budget; session
resets in ~1h, ~5 points below the 90% loop-stop). Attempt-05's `Next`
offered three moves; this cycle takes option (c) — the quasi-exact 1D model
*Nonlinearity* paper — as the budget-cheapest, most thematically load-bearing
(it directly tests the cross-problem "one-dimensional engine stops"
sub-pattern, the 6-for-6 unifying theme). Option (a) (re-check Seregin) was
unlikely to change in a few hours; option (b) (direction-A survey) needs
multiple queries — too costly at 85.2%.

## Headline: the 1D quasi-exact model achieves RIGOROUS blowup — the "1D engine stops" pattern is sharpened, not contradicted

**Thomas Y. Hou & Yixuan Wang (Caltech)**, *Blowup analysis for a quasi-exact
1D model of 3D Euler and Navier–Stokes*, **Nonlinearity 37 (2024)**,
DOI [10.1088/1361-6544/ad1c2f](https://doi.org/10.1088/1361-6544/ad1c2f)
(published 2024-01-22; arXiv:2306.04146). **Peer-reviewed, confirmed.**

### The model (Hou-Li 2008, CPAM 61:661–697)

The 1D Hou-Li model approximates the **axisymmetric NS along the symmetry
axis** ($r=0$) and is **"quasi-exact"**: solutions of the 1D model construct
**exact solutions of the full 3D Euler/NS** when the angular velocity,
angular vorticity, and angular stream function are **linear in $r$** — a
special ansatz, not general smooth data.
$$u_t+2\psi u_z=2u\psi_z+\nu u_{zz},\quad \omega_t+2\psi\omega_z=u_z^2+\nu
\omega_{zz},\quad -\psi_{zz}=\omega.$$

### Results (three blowup regimes — all WEAKENED)

1. **Inviscid + weakened advection** ($a<1$, smooth data): **self-similar
   finite-time blowup** (scaling index $c_l=0$, neither expanding nor
   focusing).
2. **Original inviscid** ($a=1$) with **Hölder $C^\alpha$ data** ($\alpha$
   near 1): self-similar blowup — shows the Hou-Li $C^1$ well-posedness
   result is **sharp**.
3. **Viscous + weakened advection** ($a<1$, $\nu>0$, smooth data):
   **finite-time blowup** (no exact self-similar profile, due to viscosity).

Method: **dynamic rescaling formulation**, linearize around
$(\sin x,\sin x,\sin x)$; linear stability via singularly weighted $L^2$
estimates (weight $\rho=1/(2\pi(1-\cos x))$); sharp nonlocal estimates
(exact Fourier low-mode + damping extraction high-mode), **verified by
computer-assisted proof** (interval arithmetic, Matlab, 200 modes); viscous
case via a custom energy norm.

## What this does to the "one-dimensional engine stops" 6-for-6 sub-pattern

The cross-problem methodology ([[beals_conjecture]]/[[navier_stokes]]/
[[birch_swinnerton_dyer]]/[[yang_mills]]/[[hodge_conjecture]]/[[collatz_conjecture]])
records a "one-dimensional engine stops" sub-pattern: the single-scale /
1D / one-engine tool controls its slice and stops at the universal control
step. The **naive read** would be "the 1D model is too weak to blow up, so
it stops." This result **corrects/sharpens that naive read**:

- The 1D quasi-exact engine does **NOT** stop at blowup — it **achieves
  rigorous finite-time blowup** in three regimes.
- It stops at the **control step**: every blowup regime requires a
  **weakening** — weakened advection ($a<1$), or rougher Hölder $C^\alpha$
  data, or the viscous case without an exact self-similar profile. The
  **full-strength 3D NS** (smooth data, full advection $a=1$, the actual
  Millennium problem) is exactly where the rigorous blowup proof does **not**
  extend.
- So the pattern holds, **more precisely**: the 1D engine is *strong
  enough to blow up* (resolution, in weakened slices), and the obstruction
  is the **control step from the weakened/1D slice to the full 3D
  smooth-data slice** — the same "control, not resolution" 6-for-6
  obstruction, now with the 1D engine on the *resolution* side (it
  resolves blowup for its slice) rather than the *control* side.

This is the **cleanest mirror of the Beal/Hodge/BSD control-step framing
within NS**: a tool that fully resolves a slice (here: rigorous blowup in
the 1D quasi-exact weakened regimes) but cannot bridge to the universal
case (full 3D smooth data). The "quasi-exact" linear-in-$r$ ansatz is the
slice boundary; general smooth 3D data is the control step.

### Connection to attempt-05's Hou 2024 (FoCM 2026) 3D candidate

Attempt-05 verified Hou's 3D **nearly-self-similar** blowup candidate
(generalized NS, published FoCM 2026, DOI 10.1007/s10208-026-09748-8) — a
*full-3D* (generalized) candidate that is not yet rigorous for true NS. The
1D quasi-exact model (this cycle) is the **rigorously analyzable reduced
version** of the same Hou-group program: the 1D model rigorously proves
blowup where the 3D model gives only a nearly-self-similar candidate. The
two form the resolution/control pair: 1D = rigorous blowup (resolution,
weakened slice); 3D generalized = candidate (control step, open).

## Related results (search-surfaced; flagged to-verify)

- **Huang–Qin–Wang–Wei**, *Exact Self-Similar Finite-Time Blowup of the
  Hou–Luo Model with Smooth Profiles*, **Commun. Math. Phys. 406, 243
  (2025)**, DOI 10.1007/s00220-025-05429-9 — a **different** (Hou-Luo, not
  Hou-Li) but related 1D model; **purely analytic** fixed-point (Schauder,
  no computer-assistance), exact self-similar blowup on $\mathbb R$ with
  smooth profiles. A second rigorous 1D blowup result, different method.
- **Hou–Qin–Wang**, *Exact Blowup Analysis for the Weak-Advection Hou–Li
  Model*, arXiv:2606.26658 (2026 preprint) — exact finite-time self-similar
  blowup, weak-advection Hou-Li, periodic. **Preprint, to-verify.**

So there is an **active 2024–2026 program**: 1D quasi-exact models of 3D
Euler/NS, rigorously proving blowup in weakened regimes, via two methods
(computer-assisted DRF, Nonlinearity 2024; purely analytic Schauder
fixed-point, CMP 2025). Flagged `to-verify` against the CMP/preprint bodies.

## Honesty / scope

- **The blowup is in REDUCED/weakened models**, NOT the full 3D smooth-data
  Millennium problem. Weakened advection ($a<1$), or Hölder $C^\alpha$ data,
  or viscous+weakened; the "quasi-exact" exact-3D-solution construction
  needs angular quantities linear in $r$ (a special ansatz). **The NS
  Millennium problem is untouched** — this is not a 3D smooth-data blowup
  proof, and the existence of 1D blowup does **not** imply 3D blowup (the
  control step is precisely the gap). Recorded honestly.
- **Viscosity alone does not prevent blowup** in the 1D quasi-exact model
  *with weakened advection* (regime 3): this isolates the
  vortex-stretching-vs-advection competition — weakening advection allows
  blowup even with $\nu>0$. The full 3D question is whether **full
  advection + viscosity** prevents blowup; the 1D model does not answer
  that. Important nuance, flagged.
- **Computer-assisted proof** (interval arithmetic) in the Nonlinearity
  paper — rigorous but computer-dependent (the CMP 2025 Hou-Luo result is
  purely analytic, a methodological complement).
- **Nonlinearity 2024 publication CONFIRMED** (DOI 10.1088/1361-6544/ad1c2f,
  published 2024-01-22, peer-reviewed). CMP 2025 + arXiv:2606.26658 are
  search-surfaced, flagged `to-verify` against the paper bodies.
- **No change to the NS frontier or the critical-a-priori-bound control
  obstruction** (direction A). This is a **direction-(B) ingredient** (the
  rigorously analyzable reduced model), sharpening the cross-problem
  pattern, not a proof move.
- Outcome: **confirmed** (the 1D quasi-exact model verified as a real,
  published, rigorously analyzable direction-(B) ingredient; the
  "one-dimensional engine stops" pattern sharpened — 1D engine achieves
  blowup in weakened regimes, stops at the 3D smooth-data control step;
  Hou 2024 3D candidate / 1D rigorous reduction paired), **partial**
  overall (Millennium problem untouched; CMP 2025 + 2026 preprint
  to-verify).

## Next (attempt-07)

This is the **final cycle of the 24-cycle loop** (cap reached; loop stops
after this cycle and a recovery summary is written). For a future session's
NS attempt-07, natural next moves: (a) primary-source-verify the **CMP 2025
Hou-Luo** purely-analytic blowup (the computer-free complement, a
stronger methodological result — to-verify against the paper body), OR
(b) re-check **Seregin 2024** (2402.13229) for journal publication (the one
persistent NS status flag, deferred), OR (c) deepen direction (A) the
critical a priori bound (the missing control step directly). The rotation
would resume at yang-mills (attempt-06) per the rotation order.