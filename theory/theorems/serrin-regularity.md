---
type: theorem
name: Serrin-Prodi-Ladyzhenskaya conditional regularity
created: 2026-08-24
tags: [pde, fluid-mechanics, conditional-regularity]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Serrin-Prodi-Ladyzhenskaya conditional regularity

If a weak solution $u$ of 3D NS [[def-navier-stokes-equation]] satisfies
$$u\in L^r_t(0,T;L^s_x),\qquad \frac{2}{r}+\frac{3}{s}\le 1,\quad s>3,$$
then $u$ is smooth and unique on $[0,T]$ [ns-serrin] (Ladyzhenskaya-Prodi-Serrin).

## The critical endpoint

The borderline $2/r+3/s=1$ is **critical**. The most important endpoint is
$r=\infty,\ s=3$, i.e. $u\in L^\infty_t L^3_x$:
- **Escauriaza-Seregin-Šverák (2003)** [ns-ess-endpoint]:
  $u\in L^\infty_t L^3_x\Rightarrow$ smooth (via backward uniqueness + unique
  continuation).
- This is the **critical regularity criterion**: $L^3$ is scale-invariant
  [[def-navier-stokes-equation]], so a global $L^\infty_t L^3_x$ bound would
  prove global regularity.

## Extensions

- Gallagher-Koch-Planchon (2016): $L^\infty_t B^{-1+3/s}_{s,q}$, $3<s,q<\infty$.
- Chemin-Gallagher (2006): global well-posedness for large but nearly-2D data.

## Role in the obstruction

Serrin criteria are **conditional** resolution: "IF a critical norm is bounded
THEN smooth." They are exactly sharp (critical). The obstruction is that no
unconditional GLOBAL bound on such a critical norm is known — the energy only
gives the subcritical $L^2$ [[method-energy-supercriticality]]. Tao's
quantitative $L^3$ blowup rate [ns-tao-quant-l3] measures how the critical
endpoint can fail.