---
type: theorem
name: Failure of the integral Hodge conjecture (Atiyah–Hirzebruch, Kollár)
created: 2026-08-24
tags: [algebraic-geometry, algebraic-cycles, torsion]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# The integral Hodge conjecture is false

The Hodge conjecture is stated over $\mathbb Q$, not $\mathbb Z$. The integral
version — every *integral* $(p,p)$ class is a $\mathbb Z$-linear combination
of algebraic-cycle classes — is **false** [hodge-integral-fails].

## Counterexamples

- **Atiyah–Hirzebruch** (and later refinements): construct smooth projective
  varieties with integral Hodge classes (in codimension $\ge2$) that are not
  algebraic integrally, via nontrivial torsion in the Atiyah–Hirzebruch
  spectral sequence.
- **Kollár**: very explicit examples (Tate, ...); also showed the integral
  Hodge conjecture for $p=1$ *does* hold (consistent with Lefschetz $(1,1)$,
  which is integral) but fails for $p\ge2$.

## The obstruction is torsion / divisibility

The integral Hodge class lies in $H^{2p}(X,\mathbb Z)\cap H^{p,p}$ but an
algebraic cycle gives an *integral* class $\mathrm{cl}(Z)\in H^{2p}(X,\mathbb
Z)$; the failure is that some integral Hodge classes are divisible only after
passing to $\mathbb Q$ (torsion in the spectral sequence differentials $d_r$).
The conjectural salvage — the $\mathbb Q$-statement — removes exactly this
torsion obstruction [[def-hodge-class-cycle-map]].

## Role in the obstruction map

Unlike the other four problems in this wiki, Hodge has a built-in **"the naive
strong statement is false"**: even granting the analytic→algebraic bridge
[[method-analytic-algebraic-bridge]], the *integral* version fails for a
*separate* reason (torsion). The $\mathbb Q$-Hodge conjecture bundles "remove
the torsion obstruction" (done: use $\mathbb Q$) with "build the
analytic→algebraic bridge in codim $\ge2$" (the open part). Worth tracking
whether these are genuinely two obstructions or one — see notes.md.