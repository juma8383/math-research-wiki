---
type: definition
name: Navier-Stokes equation, scaling, and critical norms
created: 2026-08-24
tags: [pde, fluid-mechanics, analysis]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Navier-Stokes equation, scaling, and critical norms

## The equation

For a viscous incompressible fluid in $\Omega\subset\mathbb R^d$:
$$\partial_t u + (u\cdot\nabla)u - \nu\Delta u = -\nabla p + f,\qquad
\nabla\cdot u = 0,$$
with $u:\Omega\times\mathbb R_+\to\mathbb R^d$ velocity, $p$ pressure, $\nu>0$
viscosity. The Millennium problem [[navier_stokes]] uses $\Omega=\mathbb R^3$
or $\mathbb T^3=\mathbb R^3/\mathbb Z^3$ (no boundary), $f=0$, smooth
divergence-free decaying initial data $u_0$.

## The energy inequality

Testing against $u$ and using $\nabla\cdot u=0$ (the advection term drops out
of the $L^2$ inner product) gives the **energy inequality**:
$$\frac12\|u(t)\|_{L^2}^2 + \nu\int_0^t\|\nabla u(s)\|_{L^2}^2\,ds
\le \frac12\|u_0\|_{L^2}^2.$$
This is the ONLY known unconditional global a priori bound.

## Scaling and criticality

The NS scaling symmetry:
$$u(x,t)\mapsto u_\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t),\quad
p\mapsto \lambda^2 p(\lambda x,\lambda^2 t).$$
Sobolev scaling: $\|u_\lambda\|_{\dot H^s}=\lambda^{s-1/2}\|u\|_{\dot H^s}$, so
$\dot H^{1/2}$ (and $L^3$: $\|u_\lambda\|_{L^3}=\|u\|_{L^3}$) are **critical**
(scale-invariant). The energy $\|u_\lambda\|_{L^2}=\lambda^{-1/2}\|u\|_{L^2}$ is
**subcritical** (weakens at small scales $\lambda\to\infty$).

## The Serrin number (why 2D is easy, 3D is hard) [ns-supercritical]

For a term $\nabla^k u$ in dimension $d$, the scaling-regularity ("Serrin")
index is $d/2+k$. The linear dissipation $\Delta u$ has $k=2$:
$S_{\text{lin}}=d/2+2$. The nonlinear advection $(u\cdot\nabla)u$ is a product
of $u$ (index $d/2$) and $\nabla u$ (index $d/2+1$), so
$S_{\text{nonlin}}=d/2+(d/2+1)=d+1$.

- **2D**: $S_{\text{lin}}=3=S_{\text{nonlin}}$ — balanced; the nonlinearity is
  absorbed by dissipation. **Solved** [ns-2d-solved].
- **3D**: $S_{\text{lin}}=3.5<4=S_{\text{nonlin}}$ — the nonlinearity dominates
  at small scales; **supercritical**.

This is the structural heart of the obstruction [[method-energy-supercriticality]]:
the controlled quantity (energy, subcritical) is at lower regularity than the
critical norm ($L^3$) that regularity needs.