---
type: method
name: The analytic→algebraic bridge (Hodge obstruction lens)
created: 2026-08-24
tags: [algebraic-geometry, hodge-theory, obstruction, algebraic-cycles]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# The analytic→algebraic bridge — the Hodge unifying lens

> **When to reach for it.** You want to convert an *analytic* object (a Hodge
> class, defined by Hodge theory) into an *algebraic* object (an algebraic
> cycle), or to locate where this conversion breaks. This is the engine /
> lens for the [[hodge_conjecture]] attack — the Hodge-specific instance of
> the cross-problem "obstruction at the control step, not the resolution step."

## The bridge that works (codimension 1)

For divisors ($p=1$) the bridge is fully constructive [[thm-lefschetz-1-1]]:
$$\text{Hodge class}\ \in H^2(X,\mathbb Z)\cap H^{1,1}
\ \xleftarrow{c_1}\ \mathrm{Pic}(X)\ \twoheadleftarrow\ \text{algebraic line bundles}
\ \xleftarrow[\text{GAGA}]{}\ \text{algebraic divisors}.$$
The exponential sequence identifies Hodge classes with $c_1$ of line bundles;
GAGA makes analytic line bundles algebraic. The **Picard variety**
$\mathrm{Pic}^0(X)$ is the one-dimensional analytic→algebraic object that
makes this work, and it is an *abelian variety* (algebraic).

## The bridge that breaks (codimension $\ge2$)

For $p\ge2$ the Griffiths **intermediate Jacobian** $J^p(X)$ and the
Abel–Jacobi map replace the Picard variety, but $J^p(X)$ is in general
*transcendental* (not an abelian variety for $p\ge2$), and its image under
Abel–Jacobi does **not** characterize algebraicity the way $c_1(\mathrm{Pic})$
does for divisors. There is no known mechanism that, given a Hodge class of
codim $\ge2$, produces a $\mathbb Q$-combination of algebraic cycles mapping
to it [[def-hodge-class-cycle-map]].

## The open control steps (the obstruction)

- **Cycle-producing mechanism in codim $\ge2$:** the Picard-variety /
  exponential-sequence engine has no effective higher-codimension analogue.
- **Torsion wrinkle** [[thm-integral-hodge-fails]]: even the integral version
  fails (Atiyah–Hirzebruch, Kollár); the $\mathbb Q$-version removes this but
  the analytic→algebraic gap remains.
- **Reduction itself is open:** the motive reduction (standard conjectures
  B, C) [[thm-standard-conjectures-motives]] would reduce HC to specific
  classes, but B, C are open in general (known only for surfaces, abelian,
  hyper-Kähler $K3^{[n]}$).

## Place in the cross-problem obstruction map

The "one-dimensional engine stops" pattern: the working tool is intrinsically
*one-codimension* (the Picard variety / exponential sequence), and the open
content is the leap to higher codimension — parallel to:
- Beal's cubic-cubic-cubic coincidence (one exponent shape)
  [[beals_conjecture]];
- BSD's one-point Euler system (rank $\le1$) [[birch_swinnerton_dyer]];
- NS's 2D Serrin-index equality $3=3$ [[navier_stokes]];
- YM's single RG scale / asymptotic freedom [[yang_mills]].

The Hodge-specific lens is **analytic vs algebraic**; the control over the
analytic→algebraic conversion in codim $\ge2$ is the obstruction. See
[[hodge_conjecture]].