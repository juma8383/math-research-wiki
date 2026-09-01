---
type: theorem
name: Tao averaged-NS blowup and quantitative L3 rate
created: 2026-08-24
tags: [pde, fluid-mechanics, blowup, critical-norms]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Tao (2016): averaged-NS blowup + quantitative L³ blowup rate

## Averaged-NS blowup [ns-tao-averaged-blowup]

Tao (2016) constructed finite-time blowup for an **averaged** (modified) 3D
Navier-Stokes equation — a system that preserves key NS features (energy
inequality, scaling, coercivity of dissipation) but replaces the nonlinear
advection by an averaged analogue. This is the most credible evidence that
true-NS blowup MIGHT exist, but it does NOT resolve the original problem.

## Quantitative L³ blowup rate [ns-tao-quant-l3]

For the TRUE equations, Tao proved: if a finite-energy solution first loses
smoothness at $T^*$, then
$$\limsup_{t\uparrow T^*}\|u(\cdot,t)\|_{L^3(\mathbb R^3)}\cdot
\bigl(\log\log\log(1/(T^*-t))\bigr)^c=\infty$$
for a universal $c>0$. It follows from the quantitative estimate
$\|u\|_{L^\infty_t L^3_x}\le M\Rightarrow\|u\|_{L^\infty_{x,t}}\le
\exp\exp\exp(M^C)$.

## Refinements

- **Barker-Prange (2021)**: lower bound on the localized $L^3$ integral.
- **Palasek (2021/22)**: $\limsup\|u\|_3(\log\log(1/(T^*-t)))^c=\infty$ for
  axisymmetric solutions; minimum critical blowup rates in higher dimensions.
- **Barker (2022)**: **localized** quantitative rate — if $(x_0,T^*)$ is a
  singular point,
  $\limsup_{t\uparrow T^*}\|u\|_{L^3(B(x_0,\delta))}\ge\exp(\exp(\exp(\mathscr M^C)))$.

## Role in the obstruction

The triple-log rate **quantifies the missing control step**
[[method-energy-supercriticality]]: the critical $L^3$ norm must blow up
faster than a triple log — blowup is barely possible, but not ruled out. This
is the sharpest measure of the supercritical gap. Direction (B) (constructing
true blowup) must produce a mechanism achieving this rate; direction (A) (a
critical bound) must rule out even this slow blowup. [to-verify: exact rate
and Barker localization against the papers.]