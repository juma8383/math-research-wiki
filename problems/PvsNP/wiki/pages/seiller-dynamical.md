---
title: Seiller linear realizability / dynamical systems
category: angle
tags: [seiller-2023, carderi-2021, semantic-invariant-gap]
status: blocked-for-pnp-alive-for-lvsp
last_touched: 2026-08-21
---

# Seiller Linear Realizability / Dynamical Systems

## Core
`[seiller-2023]`: computation modeled as a **graphing** (generalized dynamical system / measured relation from ergodic theory) acting on a measured space; complexity classes characterized by which graphings are "realizable" in types defined by orthogonality w.r.t. monoid actions. Separation conjectured via **non-orbit-equivalence** of monoid actions, using measured-group-theory invariants (cost, ℓ²-Betti, topological entropy).

## Breaks for P vs NP — the semantic gap `[semantic-invariant-gap]`
P vs NP is a **semantic** distinction (an existential quantifier over witnesses), but existing orbit-equivalence invariants are **dynamical**. Four break points:
1. **Cost measures the generator, not the space.** Groupoid cost `[carderi-2021]` is the inf of generating-graphing costs — the *program's* edge structure. Both P and NP use polynomial-time generators, so costs coincide; the exponential witness fiber does not increase cost (the verifier processes one witness at a time).
2. **Kolmogorov-Sinai entropy fails** — it measures information production *per step of the action*; both run poly-time with the same per-step production. The state-space size difference is static, not dynamical.
3. **The semantic gap** — the ∃-quantifier is in the *metalogic*, not the *dynamics*. The graphing does not "traverse" the witness space; orbit-equivalence invariants are blind to it.
4. **OE→inequality is unproved** in the forward direction (non-OE ⟹ class inequality).

## Alive for L vs P
L vs P is a genuinely **dynamical** distinction (head-count / access pattern), so cost/entropy invariants may detect it. Concrete target: apply groupoid cost `[carderi-2021]` to the groupoids of germs of the m₁ (logspace) and n₁ (polytime) monoid actions. Handle the non-measure-preserving issue (computation graphings are not pmp; investigate Tao's quasi-cost / type III extensions). If costs differ, invoke Gaboriau for non-OE. This would validate the whole dynamical approach.

## Barrier position
Evades natural proofs `[rr-1997]` (operates on dynamics, not truth tables) and algebrization `[aw-2008]` (measure-theoretic, no oracle algebra). Relativization status **unproven** (oracle graphings undefined) — the weak point.

## The deepest convergence
This angle and [[gct]] **independently** break at the same missing object: an invariant sensitive to the **acceptance condition / quantifier order** rather than transition structure. See [[semantic-invariant-gap]].

## See also
[[gct]] · [[semantic-invariant-gap]] · [[open-problems]] · [[status-map]]