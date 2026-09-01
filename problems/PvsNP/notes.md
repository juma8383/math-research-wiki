# Notes — P vs NP

> Methodology + cross-problem links. Running research notes for
> [[PvsNP]]. Detailed cycle-by-cycle work lives in [wiki/](wiki/).

## The control-step pattern — P vs NP as the 7th problem

The unifying cross-problem methodology of this wiki is: **the obstruction is
at the *control / reduction* step, not the *resolution* step** (the 6-for-6
pattern across [[beals_conjecture]], [[birch_swinnerton_dyer]],
[[navier_stokes]], [[yang_mills]], [[hodge_conjecture]], [[collatz_conjecture]]),
with a **"one-dimensional engine stops"** sub-pattern (TWO-engine variant).

P vs NP fits the pattern cleanly — extending it to **7-for-7**, with one
qualification:

- **Resolution machinery works on slices.** Every LB engine (Williams'
  algorithmic method, the mining/CAPP route, GCT's flip, the measure /
  disjoint-pairs / descriptive pivots) succeeds on a *relaxed* regime or a
  *slice*: NEXP vs ACC⁰, a weakened-advection 1D NS model, a hyper-Kähler
  $K3^{[n]}$ slice of Hodge, a paired $E/E^K$ twist of BSD. The resolution
  step is not where the wall sits.
- **The wall is the control step to full strength.** Promoting each slice
  result to the full problem is the open construction `(A)` / the non-
  compositional balanced-point witness — the step where the engine stops.
  Same spine as: NS (resolve a self-similar slice, stop at the universal
  control to full 3D); Collatz (density→pointwise); BSD (each summand's main
  conjecture works, the rank-2 Darmon-derivative composition is the wall);
  Beal (reduction-to-finite for the all-distinct-odd-prime region).
- **The "one-dimensional engine stops" sub-pattern.** Each LB engine is
  one-dimensional (single hard function, single wire axis, single depth
  axis); the construction lock is non-compositional — the composed object
  (expensive ∧ small-gap on the size axis; direct-sum on the depth axis)
  does not decompose into its parts `[direct-sum-is-depth-face-of-
  noncompositionality]`. Two one-directional engines that cannot compose is
  the BSD cyclotomic/anticyclotomic echo; here it is the size/depth axis
  independence.

**Qualification (honest):** the other six problems are number-theory / PDE /
geometry; P vs NP is complexity theory. The 7-for-7 framing is a *structural*
analogy (control vs resolution), not a mathematical equivalence — the
shared object is the *methodological lens*, not the mathematics. P vs NP's
wall is uniquely characterized by being an **open construction blocked by
the natural-proofs barrier (conditional on OWFs)**, not a proven
impossibility — a status the number-theory problems do not share.

## Two avatars / two axes (P vs NP's own internal duality)

The nested wiki found `[two-faces-two-np-variants]`: the wall's natural-proofs
skin has two variants on two axes — black-box/largeness (RR/FLY for NEXP
LBs, the mining face) vs constructivity/recognizability (Ilango for
explicit-function LBs, the S1.a face), routed by CWY's NEXP-specificity.
This is P vs NP's analogue of BSD's "two avatars" (function-field proven /
number-field open) found in [[birch_swinnerton_dyer]] attempt-07: one face
closes (mining/NEXP-LB natural-proofs-blocked), the other stays open (S1.a
(A) — an open construction). Both problems express a duality where one
avatar is settled and the other is the live frontier.

## Why this problem is NOT the Riemann Hypothesis

The folder was originally pasted in as `Riemann-Hypothesis` (PascalCase),
but the content is entirely **P vs NP / computational complexity theory**
(GCT, MCSP, meta-complexity, disjoint NP pairs, proof complexity,
resource-bounded measure, descriptive complexity, KW communication). The
user corrected the folder name to `PvsNP` on 2026-08-25. The Riemann
Hypothesis is a separate problem not (currently) under attack in this wiki.

## Structural reconciliation with the main wiki

- The nested `wiki/` is a complete LLM-wiki (own SCHEMA/index/log/pages/
  sources) and is **preserved** — it is the detailed work.
- `wiki/sources/` plays the role of `attempts/` (28 cycle files, append-only,
  dated `2026-08-2X-<id>.md`); `wiki/pages/` plays the role of synthesis +
  angle/concept pages.
- Reusable *general* theory is NOT promoted to the shared `theory/` toolbox:
  the P-vs-NP barriers (natural proofs, algebrization, etc.) are specific to
  this problem and not reusable across the six number-theory/PDE problems.
  (Optional future: a `theory/methods/natural-proofs.md` page if a second
  problem ever needs it — not now.)
- The main `index.md` catalogs PvsNP with a single attempts-pointer to the
  nested wiki's own catalog (not 28 duplicated lines).