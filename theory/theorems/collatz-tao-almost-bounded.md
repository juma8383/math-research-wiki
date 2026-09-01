---
type: theorem
name: Tao (2019/2022) — almost all Collatz orbits attain almost bounded values
created: 2026-08-24
tags: [number-theory, dynamical-systems, ergodic-theory]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# Tao — almost all orbits attain almost bounded values

**Theorem (Tao 2019, published 2022, Forum Math. Pi).** For any
$f:\mathbb N^+\to\mathbb R$ with $f(N)\to+\infty$, one has
$\mathrm{Col}_{\min}(N)<f(N)$ for **almost all** $N$ (in **logarithmic
density**) [collatz-tao-almost-bounded]. E.g. $\mathrm{Col}_{\min}(N)<\log\log
\log\log N$ for a.a. $N$. "Almost all orbits attain almost bounded values."

This is the apex of the density line [[thm-collatz-density-results]]: from
Terras ($<N$) through Allouche/Korec ($<N^\theta$) to Tao ($<f\to\infty$).

## Techniques

- **Syracuse map** [[def-collatz-map]] (one $\times3$ per iteration).
- **3-adic** analysis (not 2-adic) of Syracuse iterates; Syracuse random
  variables $\mathbf{Syrac}(\mathbb Z/3^n\mathbb Z)$.
- **Approximately invariant probability measures** transported to each other
  by Syracuse iterations (Bourgain-inspired — nonlinear Schrödinger analogy),
  bootstrapping local → almost-global control.
- **First-passage** function $\mathrm{Pass}_x$ with a stabilization property.
- **Fine-scale mixing**: Syracuse variables ~uniform at fine 3-adic scales,
  reduced to superpolynomial Fourier decay.
- **2D renewal process** over a "triangles" geometric structure (the deepest
  part, Section 7).

## Role in the obstruction

Tao reaches the **quantitative frontier of the average-case engine**: a.a.
$<f\to\infty$ (log-density). The two explicit gaps to the full conjecture
[[method-average-vs-pointwise-control]]:
- **Log-density → natural density**: plausible upgrade, requires more work.
- **$f\to\infty$ → absolute constant**: Tao — "likely almost as hard as the
  full Collatz conjecture." This *is* the density→pointwise obstruction made
  quantitative.
- **a.a. → all $N$**: the exceptional measure-zero set (where a divergent
  trajectory or nontrivial cycle would live) is uncontrolled.