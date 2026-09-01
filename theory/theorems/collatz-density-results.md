---
type: theorem
name: Collatz density / almost-all results (Terras, Allouche, Korec, Krasikov–Lagarias)
created: 2026-08-24
tags: [number-theory, dynamical-systems, density]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# Collatz density / almost-all results

The **resolution layer that works for average-case / density control**.

## Terras (1976) / Everett (1977)

$\mathrm{Col}_{\min}(N)<N$ for **almost all** $N$ (natural density)
[collatz-density-terras]. I.e. almost every starting value eventually drops
below itself — a finite stopping time for a density-1 set.

## Allouche (1979), Korec (1994)

$\mathrm{Col}_{\min}(N)<N^\theta$ for almost all $N$, for:
- Allouche: any $\theta>3/2-\log3/\log2\approx0.869$;
- Korec: any $\theta>\log3/\log4\approx0.792$.
[collatz-density-allouche-korec] — pushing the almost-all bound toward smaller
powers.

## Krasikov–Lagarias (2003, Acta Arith. 109)

$$\#\{N\le x:\mathrm{Col}_{\min}(N)=1\}\gg x^{0.84}$$
[collatz-kl-count] — a rigorous **lower bound on the count** of integers that
reach 1. (A counting, not a density-1, statement; a power $0.84<1$, so still
far from "almost all reach 1.")

## Role in the obstruction

These establish a **density-1 / almost-all** control: the *average* behavior
shrinks. They are the resolution tools for their slice. The gap is
**pointwise** control — density-1 cannot exclude a measure-zero exceptional
set, which is exactly where a divergent trajectory or nontrivial cycle would
live [[method-average-vs-pointwise-control]]. Tao [[thm-collatz-tao-almost-bounded]]
is the apex of this line, taking "almost all" from $<N$ down to $<f\to\infty$.