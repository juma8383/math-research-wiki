---
type: attempt
problem: beals_conjecture
attempt: 09
date: 2026-08-24
approach: Write a consolidated synthesis page distilling the five-thread obstruction map from attempts 01–08
outcome: partial
tags: [synthesis, obstruction-map, cross-session-reference]
loop_cycle: 7 of 20
---

# Attempt 09 — State-of-the-attack synthesis page

With five classical threads now mapped (attempts 02/03/05/06/08), each breaking
at $(3,5,7)$ for an independent reason, the attack has reached a natural
consolidation point. This cycle writes a standalone **synthesis page** —
`problems/beals-conjecture/synthesis.md` — freezing the structural picture for
cross-session continuity.

## What the page captures

- The two reductions (Beal ⟺ no pairwise-coprime solution; exponents in
  $\{$odd primes$\}\cup\{4\}$).
- The exact frontier: $(3,5,7)$ is the smallest open signature; the open region
  = all-distinct-odd-prime signatures.
- The open content precisely stated: "finitely many → zero" per signature
  (Darmon–Granville gives finiteness; abc gives no more).
- The **five-thread obstruction table** (Frey/modular, Darmon program, Mordell
  lens, descent, spherical reduction) with the exact structure each needs and
  the exact reason $(3,5,7)$ breaks it.
- The unifying observation: cubic-cubic-cubic is the *unique* signature where
  all classical structures coincide; every distinct-prime signature breaks all
  five. The solved/open boundary = the factorization / no-factorization divide.
- An honest "what a proof would require" assessment (two programs away on the
  modular side; no non-modular foothold).
- Computational state (searches, Mordell verification, $z^r\le2^{100}$).
- The minor to-verify items (cyclotomic UFD boundary; Siksek–Stoll computational
  step; composite-exponent signatures).
- An attempt index table.

## Why this is the right move now

The wiki now holds ~22 pages across `theory/`, `problems/`, `sources/`. A new
session resuming Beal would otherwise re-derive the frontier from scattered
attempt files. The synthesis page is the single entry point: it states the
mapped territory and points to the detailed method/theorem pages via
cross-links. This is the LLM-wiki "compounding" property made explicit — the
*map itself* is the durable artifact, not just the per-cycle content.

## Honest outcome

**partial — consolidating, not advancing.** No new attack; the value is
durability. The five-thread diagnosis is now frozen in one place and will not
need re-derivation. The frontier assessment is unchanged: $(3,5,7)$ requires
genuinely new machinery; the question is well-posed.

## Next cycles

- **Lint pass**: ~23 pages now — check for orphans, contradictions, missing
  cross-refs (especially to the new synthesis + spherical-reduction pages).
- **Speculative "what new machinery"** cycle: honestly frame what a proof of the
  distinct-prime case would need to invent — likely no actionable result, but
  completes the diagnostic picture.
- Possibly: deeper integral-point / Mordell–Weil theory on the degenerate
  near-miss families, to confirm they are *all* degenerate (computational
  strengthening of attempt-04).