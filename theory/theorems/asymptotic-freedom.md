---
type: theorem
name: Asymptotic freedom (Gross-Wilczek-Politzer)
created: 2026-08-24
tags: [mathematical-physics, qft, renormalization-group]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Asymptotic freedom

For non-abelian gauge theory with a compact simple group $G$, the running
coupling obeys (1-loop) [ym-asymptotic-freedom]:
$$\mu\frac{\mathrm dg}{\mathrm d\mu}=\beta(g)=-\beta_0 g^3+\mathcal O(g^5),
\qquad \beta_0=\frac{11N}{48\pi^2}>0\quad(SU(N)).$$
- Gross-Wilczek, Politzer (1973; Nobel 2004).
- $\beta_0>0\Rightarrow g(\mu)\to0$ as $\mu\to\infty$: the theory is
  **asymptotically free** — weakly coupled at high energy (UV).
- Conversely $g(\mu)$ **grows** at low energy (IR), where perturbation fails
  and confinement is expected [[def-mass-gap-confinement]].

## Role in the obstruction

Asymptotic freedom is the **perturbative UV control** that makes non-abelian
YM the simplest nontrivial constructive QFT in 4D (most other 4D interacting
QFTs have a Landau pole and would be trivial at all scales). But it gives **no
control in the IR**: the mass gap [[def-mass-gap-confinement]] lives where
$g$ is large. The dimensional-transmutation scale
$\Lambda_{\text{YM}}=\mu\,e^{-1/(2\beta_0 g^2)}$ [[def-yang-mills-theory]] is
the boundary between the perturbative UV (controlled) and the non-perturbative
IR (the gap). The obstruction is the UV→IR bridge across this boundary.