---
type: method
name: Energy estimates, scaling, and the supercriticality obstruction
created: 2026-08-24
tags: [pde, fluid-mechanics, scaling, obstruction]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Energy estimates and the supercriticality obstruction

> **When to reach for it.** You want to explain WHY 3D Navier-Stokes is open
> and 2D is solved, and locate the exact gap. This is the unifying lens of the
> NS attack, analogous to Beal's hyperbolicity + no-exponent-2 and BSD's
> Euler-system shape.

## The energy estimate (the only global a priori bound)

Testing 3D NS [[def-navier-stokes-equation]] against $u$ kills the advection
$(u\cdot\nabla)u$ in the $L^2$ inner product (divergence-free), leaving the
**energy inequality** — the unique unconditional global bound:
$$\|u(t)\|_{L^2}^2+2\nu\int_0^t\|\nabla u\|_{L^2}^2\le\|u_0\|_{L^2}^2.$$

## Scaling: subcritical vs critical

Under NS scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$:
- $\|u_\lambda\|_{L^2}=\lambda^{-1/2}\|u\|_{L^2}$ — **subcritical** (weakens
  at small scales $\lambda\to\infty$).
- $\|u_\lambda\|_{L^3}=\|u\|_{L^3}$ — **critical** (scale-invariant).
- $\|u_\lambda\|_{\dot H^{1/2}}=\|u\|_{\dot H^{1/2}}$ — critical.

The energy controls only the subcritical $L^2$. Regularity (via Serrin
[[thm-serrin-regularity]], ESS endpoint) needs the critical $L^3$ bounded. A
subcritical bound cannot control a critical norm — the **supercriticality
gap** [ns-supercritical].

## Why the nonlinearity dominates in 3D [ns-supercritical]

The scaling-regularity ("Serrin") index of $\nabla^k u$ is $d/2+k$:
- linear dissipation $\Delta u$ ($k=2$): $S_{\text{lin}}=d/2+2$.
- nonlinear advection $(u\cdot\nabla)u$ (product of $u$, index $d/2$, and
  $\nabla u$, index $d/2+1$): $S_{\text{nonlin}}=d+1$.

| dim | $S_{\text{lin}}$ | $S_{\text{nonlin}}$ | status |
|---|---|---|---|
| 2 | 3 | 3 | balanced — **solved** [ns-2d-solved] |
| 3 | 3.5 | 4 | nonlinearity dominates — **supercritical, open** |

In 3D the nonlinearity moves energy to small scales faster than dissipation
removes it; the energy estimate (subcritical) cannot keep up. In 2D the two
balance, and the energy + 2D Sobolev inequalities close the estimates.

## Place in the obstruction map

This is the analog of Beal's "reduction step" and BSD's "Selmer-control step":
the *resolution* tools (local existence [[thm-local-wellposedness]],
conditional regularity [[thm-serrin-regularity]] [[thm-beale-kato-majda]],
partial regularity [[thm-caffarelli-kohn-nirenberg]]) all work but are
conditional. The gap is the **control step**: an unconditional global bound on
a critical norm. Tao's triple-log blowup rate [ns-tao-quant-l3] quantifies how
close to bounded that critical norm can stay without regularity. See
[[navier_stokes]] and the cross-problem analogy [[beals_conjecture]]
[[birch_swinnerton_dyer]].