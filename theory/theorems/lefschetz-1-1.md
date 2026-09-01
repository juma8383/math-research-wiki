---
type: theorem
name: Lefschetz theorem on (1,1)-classes (the divisor case)
created: 2026-08-24
tags: [algebraic-geometry, hodge-theory, divisors]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# Lefschetz theorem on (1,1)-classes

**Theorem (Lefschetz 1924).** On a smooth projective $X/\mathbb C$, every
integral Hodge class in $H^2(X,\mathbb Z)\cap H^{1,1}(X)$ is a $\mathbb
Z$-linear combination of classes of divisors (hypersurfaces)
[hodge-lefschetz-1-1]. I.e. the Hodge conjecture holds for $p=1$, integrally.

## The mechanism (exponential sequence)

The exact sequence of sheaves
$$0\to\mathbb Z\to\mathcal O_X\xrightarrow{\exp(2\pi i\,\cdot)}\mathcal O_X^*\to0$$
yields the long exact sequence
$$H^1(\mathcal O_X)\to H^1(\mathcal O_X^*)=\mathrm{Pic}(X)\xrightarrow{c_1}
H^2(X,\mathbb Z)\to H^2(\mathcal O_X).$$
Hence
$$\mathrm{Hdg}^1(X)=\ker\bigl(H^2(X,\mathbb Z)\to H^2(\mathcal O_X)\bigr)
=c_1(\mathrm{Pic}(X)),$$
and for projective $X$ the Néron–Severi group
$\mathrm{NS}(X)=\mathrm{Pic}(X)/\mathrm{Pic}^0(X)$ consists of algebraic
divisors (GAGA: analytic line bundles = algebraic). So the Hodge class is a
$c_1$ of an algebraic line bundle — **the analytic→algebraic bridge works
for divisors**.

## Role in the obstruction

This is the **resolution layer that works** — the one codimension where the
full mechanism (exponential sequence → Picard variety → GAGA) converts a
Hodge class into an algebraic cycle, integrally. The obstruction is that this
one-dimensional mechanism has no effective analogue in codimension $\ge2$
[[method-analytic-algebraic-bridge]]. By hard Lefschetz [[thm-hard-lefschetz-reduction]]
it also covers $p=n-1$. The structural reason it stops: the Picard variety is
a *one-dimensional* analytic→algebraic object (abelian variety); the
Griffiths intermediate Jacobian for $p\ge2$ is transcendental and does not
control algebraicity.