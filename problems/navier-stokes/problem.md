---
type: problem
slug: navier-stokes
title: Navier-Stokes existence and smoothness
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [pde, fluid-mechanics, analysis, nonlinear]
tools: [[def-navier-stokes-equation], [thm-local-wellposedness], [thm-leray-weak-solutions], [thm-serrin-regularity], [thm-beale-kato-majda], [thm-caffarelli-kohn-nirenberg], [thm-tao-averaged-blowup], [method-energy-supercriticality]]
related: [[beals_conjecture], [birch_swinnerton_dyer], [yang_mills], [hodge_conjecture], [collatz_conjecture]]
target-frontier: global regularity for large 3D data
---

# Navier-Stokes existence and smoothness

## Statement (Fefferman / Clay, 2000)

The 3D incompressible Navier-Stokes equations [[def-navier-stokes-equation]]
$$\partial_t u + (u\cdot\nabla)u - \nu\Delta u = -\nabla p,\qquad \nabla\cdot u = 0$$
on domains WITHOUT boundary. The Millennium problem asks for a proof OR
counterexample of one of four statements [ns-millennium-fefferman]:
- **(A)** Global smooth solution on $\mathbb R^3$ for any smooth, divergence-free,
  decaying initial data (no force).
- **(B)** Same on the 3-torus $\mathbb R^3/\mathbb Z^3$.
- **(C)** Breakdown on $\mathbb R^3$: smooth data/force with no global smooth solution.
- **(D)** Breakdown on $\mathbb R^3/\mathbb Z^3$.

Solutions must be smooth ($C^\infty$) and have bounded energy
($\int|u|^2<C$). The complementary A/C (or B/D) pair means either global
regularity OR a finite-time singularity closes the problem.

## Known partial results (frontier)

- **2D — fully solved**: global smooth unique solutions (Ladyzhenskaya, 1960s)
  [ns-2d-solved].
- **3D local well-posedness** [[thm-local-wellposedness]]: smooth unique
  solutions on $[0,T)$ with $T$ depending on the data; **small data $\Rightarrow$
  global** [ns-local-wp].
- **3D global weak (Leray-Hopf) solutions** [[thm-leray-weak-solutions]]:
  exist for all time, satisfy the energy inequality; **uniqueness open**
  [ns-leray-weak].
- **Conditional regularity** [[thm-serrin-regularity]] [[thm-beale-kato-majda]]:
  IF a critical norm (e.g. $L^\infty_t L^3_x$ [ns-ess-endpoint], or
  $\int\|\omega\|_\infty$ [ns-bkm]) stays bounded THEN smooth — but no
  unconditional global critical bound is known.
- **Partial regularity** [[thm-caffarelli-kohn-nirenberg]] (CKN 1982): the
  space-time singular set has parabolic Hausdorff dimension $\le1$ [ns-ckn].
- **Averaged-NS blowup** [[thm-tao-averaged-blowup]] (Tao 2016): a *modified*
  NS blows up in finite time — a model, not the true equations
  [ns-tao-averaged-blowup].

## The obstruction

3D NS is **supercritical** [[method-energy-supercriticality]] [ns-supercritical]:
the only known unconditional global a priori bound is the energy
($\|u\|_{L^2}$, subcritical), while regularity requires a **critical** norm
($L^3$, scaling-invariant) to be controlled. The nonlinear advection
$(u\cdot\nabla)u$ in 3D has Serrin number $S=d+1=4>3.5=d/2+2$ (the linear
terms); they are EQUAL in 2D, which is exactly why 2D is solved. The gap is a
global bound on a critical norm — a *control* step; the *resolution* tools
(local existence, conditional regularity, partial regularity) all work but are
conditional on that bound.

## Status

in-progress. Frontier = global regularity for large 3D data (A/B) OR a
finite-time blowup counterexample (C/D). Toolbox and obstruction map under
construction; see `progress.md` and `attempts/`.