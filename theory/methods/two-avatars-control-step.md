---
type: method
name: Two-avatars control step (function-field proven / number-field open)
created: 2026-08-31
tags: [number-theory, arithmetic-geometry, obstruction, methodology]
used-in: [[riemann_hypothesis], [birch_swinnerton_dyer], [hodge_conjecture], [PvsNP]]
provenance: [[riemann-hypothesis-attempt-01], [bsd-survey]]
---

# Two-avatars control step — the function-field / number-field twin

> **When to reach for it.** A problem has a **geometric avatar over a finite
> field** (curves/varieties over $\mathbb F_q$, function fields) where the
> central statement is a **proven theorem**, and an **arithmetic avatar over a
> number field** ($\mathbb Q$, $\mathbb Z$) where the same-shaped statement is
> open. Diagnose: which control tool carries the geometric proof, and does it
> have *any* characteristic-0 translation? If not, the open avatar's
> obstruction is precisely the missing translation — not a failure of the
> resolution machinery, which usually works in both avatars.

## Statement of the pattern

For each pair below, the *same control step* is discharged in one avatar and
undischarged in the other, because the tool that discharges it exists only in
the geometric avatar:

| Problem | Geometric avatar (proven) | Number-field avatar (open) | The untranslated control tool |
|---|---|---|---|
| RH | Weil (curves, 1940s) / Deligne (all varieties, 1974): Frobenius eigenvalues are Weil numbers $\lvert\alpha\rvert=q^{-n/2}$ | RH for $\zeta(s)$, all $L$-functions [[riemann_hypothesis]] | **Frobenius + Rosati positivity** — no Frobenius in char 0 |
| BSD | Function-field BSD (Birch–Swinnerton-Dyer over $\mathbb F_q(t)$) — proven | BSD for elliptic curves over $\mathbb Q$ [[birch_swinnerton_dyer]] | **Euler systems + étale cohomology** (Kato–Trihan route) — no known char-0 translation of the geometric mechanism |
| Hodge (analogue) | Motivic / standard-conjectures world: Rosati positivity is *conjectural itself* (the standard conjectures) [[hodge_conjecture]] | — | The standard conjectures are the shared Rosati-type positivity both a motivic RH and the Hodge conjecture would rest on [[method-analytic-algebraic-bridge]] |

## Why it is stronger than "parallel walls"

The wiki's base methodology ("obstruction at the control/reduction step, not
the resolution step") is a *parallelism* across problems. The two-avatars
structure is a sharper claim: in RH and BSD the geometric and arithmetic
avatars are **the same mathematical statement specialized to different base
fields**, so the control step is literally one step seen twice — once
discharged, once not. This converts an analogy into an exact
question: *what property of $\mathbb F_q$ (finiteness, positive
characteristic, existence of Frobenius, étale cohomology with its
positivity) makes the control tool available, and is any of it simulable over
$\mathbb Q$?*

Known structural facts about the gap (all `[summary]`, classical):

- **Finiteness of the base field** gives Frobenius an *actual operator* whose
  fixed points are the points being counted (Lefschetz trace formula). Over
  $\mathbb Q$ there is no such operator on any known cohomology of
  $\operatorname{Spec}\mathbb Z$.
- **Weil II / Deligne** needs the *positivity of the Rosati involution* on
  endomorphisms of the Jacobian/motive — this is an input, not an output.
- Connes's adele-class space program [[riemann_hypothesis]] is the most
  serious attempt to *build* the number-field avatar of this operator; it
  reduces RH to a trace formula whose positivity is unavailable — i.e. it
  relocates the two-avatars gap rather than closing it.

## Relationship to the other cross-problem lenses

- **Average-vs-pointwise** [[method-average-vs-pointwise-control]]: usually
  the *stated* control step inside one avatar ("almost all → every"). The
  two-avatars lens is orthogonal and deeper: it explains why the tool that
  gets you pointwise control **in one world** does not export.
- **One-dimensional engine stops**: both avatars share the engine; the stop
  is at the avatar *interface*.
- Extension (with the same standing disclaimer as the [[PvsNP]] extension —
  structural analogy, not mathematical equivalence): the
  `[witness-needs-explicit-lb]` pattern in P vs NP has a two-avatar shape —
  *random/counterexample-based* resolution methods (natural proofs) that
  fail exactly at the explicit-construction step mirror "the technique
  works for the generic object, not for the object that exists".

## How to use it in an attack

1. Write the statement over $\mathbb F_q$; confirm the analogue is a theorem
   and identify the *exact* positivity/operator input in the proof.
2. Attempt the translation honestly: for each input, either name a
   char-0 substitute or record that none is known (this is where the wall is,
   precisely).
3. Check whether any proposed construction (Connes, motives, standard
   conjectures) is *building* the missing input — if so, the problem
   inherits that construction's own open status (e.g. the standard
   conjectures).

## See also

- [[riemann_hypothesis]] — the cleanest instance; three control-reductions
  in progress.md, avatar-(C) is this page.
- [[birch_swinnerton_dyer]] — attempt-07 two-avatars twin.
- [[method-average-vs-pointwise-control]] — the in-avatar control lens.
- [[hodge_conjecture]] — the standard conjectures as the shared positivity.