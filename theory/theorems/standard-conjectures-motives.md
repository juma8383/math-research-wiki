---
type: theorem
name: Standard conjectures and the motive reduction of the Hodge conjecture
created: 2026-08-24
tags: [algebraic-geometry, motives, standard-conjectures]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# Standard conjectures and the motive reduction

Grothendieck's **standard conjectures** concern algebraic cycles and would
make the category of motives well-behaved. Two are directly load-bearing for
the Hodge conjecture [hodge-standard-conjectures]:

- **Conjecture B (Lefschetz standard conjecture):** the inverse Lefschetz
  operators $\Lambda$ (rendering the hard Lefschetz diagrams commutative) are
  **algebraic** — induced by algebraic cycles on $X\times X$.
- **Conjecture C (Künneth standard conjecture):** the Künneth components
  $\delta_i$ of the diagonal (Hodge classes of $X\times X$) are **algebraic**.

## Known cases

- $\delta_i$ algebraic for $i\in\{0,1,2n-1,2n\}$ always; **all** $i$ for
  surfaces.
- Conjecture B known for **abelian varieties** (Lieberman 1968, Kleiman
  1968), **surfaces**, and **hyper-Kähler varieties of $K3^{[n]}$ type**
  (Charles–Markman 2013).
- B $\Rightarrow$ numerical equivalence = homological equivalence $\Rightarrow$
  the category of motives (mod homological equivalence) is Tannakian /
  semisimple.

## The motive reduction of the Hodge conjecture

If B (and C) hold — i.e. the specific Hodge classes $\delta_i,\Lambda$ are
algebraic — the category of motives becomes Tannakian, and the Hodge
conjecture becomes equivalent to the natural functor
$\{\text{motives}\}\to\{\text{Hodge structures}\}$ being **fully faithful**.
So the *universal* Hodge conjecture reduces to the algebraicity of a *finite
set of specific* Hodge classes (the Künneth components + inverse Lefschetz).

## Role in the obstruction

This is the Hodge analog of Beal's **reduction-to-finite-curves**: a
universal statement reduced to a finite/specific set, where the reduction
itself is the open step (B, C not known in general — only for surfaces,
abelian, hyper-Kähler). Direction (A) of the [[hodge_conjecture]] attack.
Note a precise parallel: the "obstruction at the reduction step" recurs *one
level down* — even the motive reduction is gated on its own control step
(proving B, C).