---
type: theorem
name: 3D Navier-Stokes local well-posedness and small-data global
created: 2026-08-24
tags: [pde, fluid-mechanics, analysis]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Local well-posedness (Leray / Fujita-Kato / Koch-Tataru)

For smooth divergence-free initial data, the 3D NS equations
[[def-navier-stokes-equation]] are **locally well-posed** [ns-local-wp]: there
is a unique smooth solution on $[0,T)$ with the "blow-up time" $T$ depending
on the data, e.g. $T\gtrsim C/\|u_0\|_{L^\infty}^2$ or
$T\gtrsim C/\|\nabla u_0\|_{L^2}^{-4}$.

- **Leray (1934)**: local strong solutions for $u_0\in L^2\cap L^\infty$.
- **Fujita-Kato (1964)**: semigroup/fractional-power approach, $u_0\in H^1$
  (and critical $\dot H^{1/2}$).
- **Koch-Tataru (2001)**: well-posedness in critical Besov spaces (the natural
  critical threshold).

## Small-data global existence

If $\|u_0\|$ in a critical norm (e.g. $\dot H^{1/2}$, or $L^3$) is sufficiently
small, the local solution extends globally — small data does not blow up.

## Blowup-rate lower bounds

If a strong solution blows up at $T^*$, then for $3<p\le\infty$:
$$\|u(t)\|_{L^p}\gtrsim \frac{1}{(T^*-t)^{\frac12(1-3/p)}}.$$
So a blowup is detected by any $L^p$ norm with $p>3$ — a necessary condition,
not a mechanism producing blowup.

## Role in the obstruction

Local well-posedness is the **resolution** layer working perfectly: it gives
existence/uniqueness/smoothness for short times. The Millennium question is
whether $T$ can be taken $=\infty$ for ALL smooth data. The obstruction is not
local existence (known) but a **global critical bound**
[[method-energy-supercriticality]].