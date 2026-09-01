---
type: method
name: Cycle exclusion via linear forms in logarithms (Collatz, Beal-flavored)
created: 2026-08-24
tags: [number-theory, transcendence, diophantine, collatz, obstruction]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# Cycle exclusion via linear forms in logarithms

> **When to reach for it.** You want to rule out a *cycle* of a discrete
> dynamical system by showing its defining equation forces a linear form in
> logarithms to be exponentially small, contradicting transcendence lower
> bounds. The cycle-exclusion sub-problem of the [[collatz_conjecture]] attack
> — the Diophantine / transcendence flavor that echoes Beal.

## The cycle equation

A nontrivial Collatz cycle of $m$ odd values $o_0,\dots,o_{m-1}$ with total
$L$ halvings [[def-collatz-map]] satisfies
$$2^L=\prod_{i=0}^{m-1}\frac{3o_i+1}{o_i}.$$
Taking logs gives a linear form
$$\Lambda=(K+L)\log 2-K\log 3$$
($K=\sum$ odd-step contributions) which, if the cycle exists, must be
**exponentially small** in the cycle's size.

## The transcendence bound (the resolution tool)

Lower bounds on linear forms in logarithms (Laurent–Mignotte–Nesterenko;
Rhin) force $\Lambda$ to be only **subexponentially** small — contradicting
the exponential smallness a cycle requires, *for small $m$*. Combined with
continued-fraction approximations to $\log3/\log2$ and diophantine-approximation
lattice methods, this yields [[thm-collatz-cycle-bounds]]:
- Steiner: no 1-cycles; Simons: no 2-cycles; Simons–de Weger: no $m$-cycles
  $m\le75$ [collatz-cycle-steiner] [collatz-cycle-simons-deweger].

## The obstruction (control step, not resolution step)

The transcendence bounds **degrade with $m$**: they suffice for $m\le75$ but
do not rule out cycles of arbitrarily large period. The control gap is
pushing to **all $m$** — direction (B) of the [[collatz_conjecture]] attack.
This is a Diophantine / transcendence problem in exactly the **Beal flavor**
[[beals_conjecture]]: a cycle is a specific exponential-diophantine relation,
and ruling it out is a Diophantine-approximation question, just as Beal reduces
to ruling out solutions of generalized-Fermat equations.

## Place in the cross-problem map

This sub-problem makes Collatz a **compound** of two earlier problems:
- **cycle exclusion** = Diophantine / transcendence = Beal flavor (here);
- **divergent-trajectory exclusion** = analytic / ergodic control = NS flavor
  [[navier_stokes]] [[method-average-vs-pointwise-control]].

A genuine cross-problem compounding artifact: the Beal-flavored machinery
(linear forms in logs, Diophantine approximation) is exactly what
Steiner/Simons/de Weger deploy. Candidate for a shared method page if a second
problem's cycle exclusion uses the same linear-forms-in-logs technique.