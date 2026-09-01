---
type: definition
name: The Collatz map, Syracuse map, and the two failure modes
created: 2026-08-24
tags: [number-theory, dynamical-systems, discrete-dynamics]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# The Collatz map and the Syracuse (accelerated) map

## Collatz map

$T:\mathbb N^+\to\mathbb N^+$ [collatz-statement]:
$$T(n)=\begin{cases}n/2 & n\text{ even},\\ 3n+1 & n\text{ odd}.\end{cases}$$
Trajectory $n, T(n), T^2(n),\dots$ The **stopping time / minimum**:
$$\mathrm{Col}_{\min}(N):=\min_{k\ge0}T^k(N).$$
Conjecture: $\mathrm{Col}_{\min}(N)=1$ for all $N$ (then $1\to4\to2\to1$
cycles). $3n+1$ is always even, so every odd step is followed by a division.

## Syracuse (accelerated) map

Apply $T$ until the next odd number. Each Syracuse step performs exactly one
multiplication by 3: for odd $n$, write $3n+1=2^{k(n)}\cdot\mathrm{Syr}(n)$
with $\mathrm{Syr}(n)$ odd. Then
$$\mathrm{Syr}(n)=\frac{3n+1}{2^{k(n)}},\qquad k(n)=\nu_2(3n+1)\ge1.$$
The parity sequence / 2-adic valuation $k(n)$ is the "random" ingredient.

## Two failure modes

The conjecture fails iff one of:
- **(a) a nontrivial cycle** $\neq\{1,4,2\}$: a finite orbit not through $1$.
  A cycle of odd values $o_0,\dots,o_{m-1}$ satisfies
  $2^L=\prod_{i}(3o_i+1)/o_i$ (a Diophantine relation; $L$ total halvings,
  $m$ odd steps) — this is the cycle equation [[thm-collatz-cycle-bounds]]
  [[method-cycle-exclusion-linear-forms]].
- **(b) a divergent trajectory** $T^k(n)\to\infty$.

Both are open. Anchor of the [[collatz_conjecture]] attack.