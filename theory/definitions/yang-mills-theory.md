---
type: definition
name: Classical Yang-Mills theory and dimensional transmutation
created: 2026-08-24
tags: [mathematical-physics, qft, gauge-theory]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Classical Yang-Mills theory and dimensional transmutation

## The classical action

For a compact simple gauge group $G$ (e.g. $SU(N)$) with connection
$A_\mu=A_\mu^a T^a$ ($[T^a,T^b]=f^{abc}T^c$), curvature
$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$, the pure YM
action on $\mathbb R^4$:
$$S_{\text{YM}}[A]=\frac{1}{4g_0^2}\int_{\mathbb R^4}\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})\,d^4x.$$
Gauge invariance $A\mapsto UAU^{-1}-\mathrm{d}U\,U^{-1}$. The pure (no-matter)
theory is the Clay target [[yang_mills]].

## Scale invariance in 4D

In 4D the coupling $g_0$ is **dimensionless** (the action is dimensionless
since $[F]=\text{mass}^2$ and $d^4x$ has mass$^{-4}$). So **classical 4D YM is
scale-invariant**: there is no intrinsic scale. A mass gap would therefore be
a purely quantum effect.

## Dimensional transmutation [ym-dimensional-transmutation]

Quantum mechanically the bare coupling runs with the scale. The 1-loop
β-function (asymptotic freedom [[thm-asymptotic-freedom]]):
$$\beta(g)=-\beta_0 g^3+\cdots,\qquad \beta_0=\frac{11N}{48\pi^2}>0\quad(SU(N)).$$
Solving $\mu\,\mathrm dg/\mathrm d\mu=\beta(g)$ generates a scale
$$\Lambda_{\text{YM}}=\mu\,e^{-1/(2\beta_0 g(\mu)^2)}$$
— a **quantum-generated mass scale** from a classically scale-invariant
theory. The mass gap is expected to be $\Delta\sim\Lambda_{\text{YM}}>0$
[[def-mass-gap-confinement]]. This transmutation is the heart of the problem:
the continuum limit (fix $\Lambda_{\text{YM}}$ as the UV cutoff $\to\infty$,
$g_0\to0$) and the mass gap are the same RG question.