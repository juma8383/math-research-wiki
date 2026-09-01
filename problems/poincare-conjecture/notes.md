# Notes — Poincaré Conjecture

> Methodology + cross-problem links. Running notes for [[poincare_conjecture]].
> The problem is **SOLVED** (Perelman 2002–03); these notes frame the known
> proof through the wiki's control-step lens — the positive-validation case.

## The control-step pattern — Poincaré as the discharged case

The unifying cross-problem methodology of this wiki is: **the obstruction is
at the *control / reduction* step, not the *resolution* step** (the 7-for-7
pattern across [[beals_conjecture]], [[birch_swinnerton_dyer]],
[[navier_stokes]], [[yang_mills]], [[hodge_conjecture]],
[[collatz_conjecture]], [[PvsNP]]), with a **"one-dimensional engine stops"**
sub-pattern.

Poincaré is the **one problem in the wiki where the control step was actually
discharged** — making it the *positive validation* of the lens, not a member of
the open set. The pattern reads cleanly in the positive direction:

- **Resolution machinery works on a slice / smooth regime.** Hamilton (1982)
  introduced Ricci flow $\partial g_{ij}/\partial t = -2R_{ij}$, a heat-type
  equation for the metric. On regions of positive curvature it smooths toward
  constant curvature; for a simply-connected manifold the expected limit is
  the round $S^3$. This is the resolution engine — and it works perfectly as
  long as the flow stays smooth.
- **The wall is the control step.** Ricci flow develops **singularities in
  finite time** (neckpinches where curvature blows up). Hamilton could run the
  flow but could not: (i) **classify** the singularity models, (ii) **cut and
  cap** (surgery) while preserving the topological type, (iii) show the process
  **terminates** (finitely many surgeries / finite extinction time). Running
  the flow on a smooth slice is resolution; controlling the singularities to
  promote the slice result to the full manifold is the control step — and that
  is exactly where Hamilton's program stalled for two decades.
- **Perelman discharged the control step.** Three new control tools, one per
  preprint:
  1. **$W$-entropy monotonicity** (arXiv:0211159). Perelman introduced the
     $F$- and $W$-functionals (a scale-invariant, coercive entropy
     $W(g,f,\tau)=\int_M[\tau(|\nabla f|^2+R)-f-n]\frac{e^{-f}}{(4\pi\tau)^{n/2}}\,dg$)
     and the reduced volume $\tilde V$ — monotone quantities under the coupled
     Ricci-flow + conjugate-heat equation. The $W$-entropy is the first
     **critical, coercive** Lyapunov functional for Ricci flow, the control
     tool that was missing. No-local-collapsing follows: local curvature bounds
     force local volume lower bounds, the lemma that unblocks singularity
     analysis.
  2. **Canonical-neighborhood theorem + surgery** (arXiv:0303109). Every
     high-curvature point has a neighborhood that is an $\varepsilon$-neck, an
     $\varepsilon$-cap, or a compact positively-curved component. This
     classifies the singularity models (control), enabling $\delta$-cutoff
     surgery: cut along necks in $\varepsilon$-horns, cap off, with surgery
     parameters $\delta(t), h(t)$ decreasing over time. Surgery times are
     discrete (finitely many in any finite interval); the flow-with-surgery
     exists for all positive time. Topology is preserved across surgery.
  3. **Finite extinction** (arXiv:0307245, sketched; Colding–Minicozzi JAMS
     2005, rigorous). On a homotopy 3-sphere the flow-with-surgery becomes
     extinct in finite time, so the long-time $t\to\infty$ analysis is
     unnecessary for Poincaré. Colding–Minicozzi proved this via the **width**
     (a min-max area of 2-spheres sweeping out the manifold), which satisfies
     $dW/dt \le -4\pi + \tfrac{3}{4(t+C)}W$ — the $-4\pi$ from Gauss–Bonnet
     forces $W\to0$ in finite time, destroying the nontrivial $\pi_3$ class,
     which is possible only if the manifold decomposes into spherical space
     forms; simply-connected leaves only $S^3$.

- **The "one-dimensional engine stops" sub-pattern, positively.** The Ricci
  flow resolves the smooth/positive-curvature slice (the engine runs); it
  stops at singularities (the one-dimensional engine stops); Perelman's control
  tools let it *pass through* the stop. In the seven open problems the
  analogous stop is where the wall still sits.

## Why this is the contrast case, not an attack

The seven open problems each have a resolution engine that works on a slice and
a control step that is **not yet dischargeable** (no monotone functional of
the right coercivity/criticality; no singularity classification; no
termination argument). Poincaré had the same shape of obstruction — and the
obstruction was real (Hamilton was genuinely stuck for 20 years) — but the
control tool existed and Perelman found it. The lesson the wiki draws: **the
wall is at control, and when the right control tool arrives, the problem
falls.** This is corroborative evidence *for* the methodology, from the one
solved instance. It is not a proof that the seven open walls will fall the same
way — each may need its own control tool, and some (e.g. [[PvsNP]]'s
natural-proofs barrier) may be genuinely harder than singularity control.

## Cross-problem link — the [[navier_stokes]] twin

The closest structural twin in the wiki is **Navier–Stokes**:

- Both are **geometric PDE control problems** with a supercritical quantity
  (Ricci flow: curvature; NS: vorticity / critical $L^3$ norm).
- Both have a **resolution engine that works on a slice / weakened regime**
  (Ricci flow on smooth positive-curvature regions; NS on 2D, on small data,
  on Hou–Li-type 1D/quasi-exact weakened-advection models — see
  [[navier_stokes]] attempt-06).
- Both hit a **singularity / blowup control wall** going to full strength
  (Ricci-flow finite-time singularities; potential NS finite-time blowup).
- **The asymmetry is the point.** Ricci flow *does* blow up (singularities are
  real and unavoidable) — and Perelman's contribution was a monotone
  *Lyapunov functional* ($W$-entropy) that controls the blowup well enough to
  cut and continue. NS asks, in the regularity formulation, whether blowup
  *does not* occur — and **no analogous critical-coercive monotone quantity
  is known** for the 3D NS supercritical norm. The Tao triple-log blowup rate
  (NS attempt-02) and the absence of a controlling entropy are the NS face of
  the same control gap Perelman closed for Ricci flow. The structural
  suggestion (not a proof): *if* 3D NS regularity is to be shown by
  Perelman-style means, the missing ingredient is an entropy-type monotone
  functional for the supercritical norm — and its absence is exactly the NS
  control-step wall. (The reverse direction — constructing NS blowup — would
  need the opposite: a singularity the existing estimates cannot rule out;
  see the Hou 3D nearly-self-similar candidate, NS attempt-05.)

This is a *structural* analogy, not a mathematical equivalence — the same
qualification as the [[PvsNP]] 7-for-7 extension. Ricci flow and NS are
different equations with different geometry; the shared object is the
*methodological lens* (resolution-on-a-slice vs control-to-full-strength),
not the mathematics.

## Reconciliation with the main wiki

- No `theory/` promotion yet. The Geometrization/Poincaré theorem and a
  Ricci-flow-with-surgery method page are natural future `theory/theorems/`
  and `theory/methods/` entries (flagged in [progress.md](progress.md) under
  "Next") but are not created in attempt-01 — the folder's role here is the
  contrast case, and the reusable control-step lens already lives in the
  shared methodology.
- Cross-problem wikilink: `[[poincare_conjecture]]` (underscore, per the
  cross-problem convention).
- The folder is kebab-case (`poincare-conjecture`), matching the other six
  main-wiki problems (unlike the PascalCase `PvsNP`).