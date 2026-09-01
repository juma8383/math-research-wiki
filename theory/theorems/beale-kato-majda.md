---
type: theorem
name: Beale-Kato-Majda vorticity blowup criterion
created: 2026-08-24
tags: [pde, fluid-mechanics, blowup-criteria]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Beale-Kato-Majda (BKM) criterion

For the 3D Euler and Navier-Stokes equations [[def-navier-stokes-equation]], a
smooth solution is regular on $[0,T]$ if and only if [ns-bkm]:
$$\int_0^T \|\omega(\cdot,t)\|_{L^\infty}\,dt < \infty,\qquad \omega=\nabla\times u.$$
Equivalently: blowup at $T^*$ requires $\int_0^{T^*}\|\omega\|_\infty\,dt=\infty$.

## Frequency-localized refinements

- **Planchon (2003)**: $\lim_{\varepsilon\to0}\sup\int_{T-\varepsilon}^T
  \|\Delta_q(\nabla\times u)\|_\infty\,dt<c$ (Littlewood-Paley).
- **Cheskidov-Shvydkoy (2014)**, **Cheskidov-Dai (2015)**: control only modes
  below a time-dependent wavenumber.
- **Luo (2019)**: **optimal frequency and temporal localization** — only
  Fourier modes below $\lambda_q(t)=c(T-t)^{-1/2}$, consistent with parabolic
  scaling; the sharpest BKM-type criterion.

## Role in the obstruction

BKM is another **conditional** resolution tool: regularity is equivalent to a
bound on $\int\|\omega\|_\infty$ (a slightly supercritical quantity). Like the
Serrin criteria [[thm-serrin-regularity]], it converts "norm bounded
$\Rightarrow$ smooth" but provides no unconditional global bound. The
refinements progressively weaken the required bound — narrowing what a proof
must achieve — but all remain conditional. This is direction (C) of the
attack.