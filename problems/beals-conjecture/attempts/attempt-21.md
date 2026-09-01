---
type: attempt
problem: beals_conjecture
attempt: 21
date: 2026-08-24
approach: Consolidate progress.md (the read-first file), stale past attempt-08, to reflect the full 20-attempt state
outcome: confirmed
tags: [consolidation, progress, bookkeeping, handoff]
loop_cycle: 19 of 20
---

# Attempt 21 — Consolidate progress.md (bring the read-first file current)

`progress.md` is the file a future session reads first when resuming, but its
"Best partial result so far" and "Convergent five-thread diagnosis" sections
stopped at attempt-08 — twelve cycles stale. The synthesis page carried the
later state, but the read-first file did not. This cycle consolidates it.

## What was stale

- "Best partial result so far": ended at attempt-08.
- "Convergent five-thread diagnosis": pre-attempt-14/17 unifying lens, pre-19
  counting heuristic, pre-20 empirical confirmation.
- No mention of: the triangle-group/PSS lens, the $(2,3,7)$ correction, the
  two later Lints, the sixth (soft) angle, the 3-signature empirical line, or
  the confirmed prediction.

## What changed

Rewrote `progress.md` to be current through attempt-20, concise, and pointed
to `synthesis.md` for structural depth (avoiding duplication — synthesis
remains the durable handoff; progress is the brief current frontier). New
sections:

- **The entire open content = "finitely many → zero"** (was implicit; now
  stated up front, the load-bearing framing).
- **Obstruction: five rigorous threads + one soft angle (6 total)** — a brief
  6-row table (full table stays in synthesis), with thread 6* marked soft.
- **The unifying lens (attempt-14/17, corrected)** — near-spherical position or
  exponent 2; $(3,5,7)$ has neither; obstruction at the *reduction* step; with
  the correction note that $(2,3,7)$ is hyperbolic not spherical.
- **What a proof requires** — the one-sentence need + directions (A)/(B) +
  the ruled-out recap.
- **Empirical state — three signatures, prediction confirmed** — a 3-row table
  ($\chi$, exact, gap-1, min gap) with $29<77<277$ and the note that the
  monotonicity was predicted (attempt-19) then confirmed (attempt-20).
- **Attempt log (01–20)** — a one-line-per-attempt summary, pointing to
  synthesis for the outcomes table.
- **Honesty check** — unchanged in spirit, updated to reflect 6 angles + the
  confirmed prediction + the two forward directions.

## Consistency checks during the rewrite

- All wikilinks resolve (verified against the index in attempt-18): the 6
  method slugs, 3 theorem slugs, 2 source slugs, the definition and conjecture.
- The $\chi$ values and min gaps match the computations exactly:
  $-34/105\approx-0.324$ (gap 29), $-62/165\approx-0.376$ (gap 77),
  $-100/231\approx-0.433$ (gap 277).
- The $(2,3,7)$ correction is reflected (hyperbolic, not spherical) — no
  stale "spherical" label reintroduced.
- The degenerate-family general fact
  ($t^{\operatorname{lcm}(p,r)}{+}1$, $t^{\operatorname{lcm}(q,r)}{+}1$) is
  preserved.

## Outcome

**confirmed.** The read-first file now matches the full 20-attempt state. No
new content was invented — this is consolidation of existing, verified
results into the navigational entry point, reducing the risk that a future
session resumes from a stale frontier. Synthesis remains the structural
reference; progress is now a faithful brief of it plus the current empirical
line. 1 cycle remains — the loop close-out.