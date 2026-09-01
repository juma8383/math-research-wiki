---
type: conjecture
name: Generalized Hodge Conjecture (Grothendieck, coniveau)
created: 2026-08-24
tags: [algebraic-geometry, hodge-theory, coniveau, algebraic-cycles]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# Generalized Hodge Conjecture (Grothendieck)

## Hodge's original stronger conjecture (FALSE)

Hodge originally conjectured that any Hodge class with support in an analytic
subspace of codimension $\ge k$ comes from an algebraic cycle of codimension
$\ge k$. Grothendieck observed this is "trivially false" and gave a corrected
version [hodge-generalized-conjecture].

## Grothendieck's Generalized Hodge Conjecture (GHC)

For $X$ smooth projective and $r\ge0$, the **GHC at coniveau $r$** asserts that
the Hodge substructures of $H^k(X,\mathbb Q)$ of coniveau $\ge r$ (i.e. those
vanishing on the complement of a codimension-$\ge r$ algebraic subset) come
from cohomology with support on codimension-$\ge r$ algebraic subsets. The
usual Hodge conjecture is the special case $k=2r$ [[def-hodge-class-cycle-map]].

## Known / open

- Coniveau $1$ (the case $r=1$): essentially reduces, via weak Lefschetz /
  blow-up, to the Lefschetz $(1,1)$ theorem [[thm-lefschetz-1-1]] — known.
- Coniveau $\ge2$: largely **open**. The clean coniveau-1 case works; the rest
  is open — the same "codim-1 engine stops" pattern as the ordinary Hodge
  conjecture.

## Role in the obstruction map

The GHC is the "right" generalization (Hodge's original was false). It
sharpens the frontier: the obstruction is not merely "produce cycles for a
$(p,p)$ class" but "realize a *coniveau-$r$ Hodge substructure* from support
on an algebraic subset of codimension $\ge r$." It is a finer analytic→algebraic
question on the same bridge [[method-analytic-algebraic-bridge]]. Not the
primary target of the [[hodge_conjecture]] attack but the natural
generalization to track.