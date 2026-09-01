---
type: method
name: Average-vs-pointwise control (the Collatz obstruction lens)
created: 2026-08-24
tags: [number-theory, dynamical-systems, ergodic-theory, obstruction]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# Average-vs-pointwise control — the Collatz unifying lens

> **When to reach for it.** You have an *average-case / density* result
> (something holds for almost all $N$, in natural or logarithmic density) and
> you want to know whether it upgrades to *pointwise / universal* (every
> $N$). This is the engine / lens for the [[collatz_conjecture]] attack — the
> Collatz-specific instance of the cross-problem "obstruction at the control
> step, not the resolution step."

## The average-contraction heuristic (the resolution tool)

For the accelerated Syracuse map [[def-collatz-map]], one odd step multiplies
by 3 and divides by $2^{k(n)}$, $k(n)=\nu_2(3n+1)$. Under the heuristic that
$3n+1$ is "random" modulo powers of 2, $\mathbb E[k(n)]=2$, so each odd step
multiplies the value by $\approx 3/2^{2}=3/4<1$ on average
[collatz-average-contraction]. Since $\mathbb E[k]=2>\log_2 3\approx1.585$,
the entropy / log-size decreases on average. This *predicts* convergence —
and is borne out by density results [[thm-collatz-density-results]]
[[thm-collatz-tao-almost-bounded]].

## The obstruction (control step, not resolution step)

The heuristic is **distributional**: it averages over parity sequences treated
as random. But the parity sequence $(k(T^i(n)))$ of a *specific* $n$ is
**deterministic** and uncontrolled. A density-1 / "almost all" result
*cannot* exclude a measure-zero exceptional set — exactly where a divergent
trajectory or a nontrivial cycle would live. The gap from "almost all" to
"every $N$" is the obstruction.

Tao [[thm-collatz-tao-almost-bounded]] quantifies the frontier: a.a.
$\mathrm{Col}_{\min}<f\to\infty$ (log-density). The two explicit control steps:
- **$f\to\infty$ → constant**: "likely almost as hard as the full conjecture."
- **a.a. → all $N$**: the exceptional set is uncontrolled.

## Why this is the canonical exemplar of the methodology

Collatz makes the "control step" lens **visceral**: the average-contraction
heuristic ($3/4<1$) *is* the resolution tool, and *is* the thing that fails to
be pointwise. Every 2024–25 claimed proof (Fathi, Nwankpa, Chang
[collatz-recent-claims-unverified]) is this heuristic dressed up, failing at
exactly this step. The cleanest introductory example of the cross-problem
"obstruction at the control step" lens.

## Place in the cross-problem obstruction map (6-for-6)

- Beal: reduction-to-finite (needs shared/even/spherical exponent)
  [[beals_conjecture]];
- BSD: Selmer control (one-point Euler system, rank $\le1$)
  [[birch_swinnerton_dyer]];
- NS: critical-norm control ($L^2$ subcritical $\not\to$ $L^3$ critical)
  [[navier_stokes]];
- YM: continuum-limit + uniform-in-$a$ IR gap transport [[yang_mills]];
- Hodge: analytic→algebraic in codim $\ge2$ [[hodge_conjecture]];
- **Collatz: average/density → pointwise/universal.**

The "one-dimensional engine stops" sub-pattern: the average is over a *single*
parity sequence / single scale; the leap to every (deterministic) $N$ is the
open content. See [[collatz_conjecture]].