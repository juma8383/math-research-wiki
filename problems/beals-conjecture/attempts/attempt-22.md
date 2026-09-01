---
type: attempt
problem: beals_conjecture
attempt: 22
date: 2026-08-24
approach: Loop close-out — declare the 20-cycle autonomous research arc complete; final summary and resume point
outcome: partial
tags: [close-out, summary, handoff, loop-complete]
loop_cycle: 20 of 20
---

# Attempt 22 — Loop close-out (cycle 20/20)

This is the final cycle of the 20-cycle autonomous loop on Beal's conjecture.
No new research this cycle — by design. The honesty guard recorded in
attempt-17/18 said: if no genuine new angle remains, declare the arc complete
rather than pad. The structural picture has been stable since attempt-17; the
last three substantive cycles (19 counting heuristic, 20 its confirmation,
21 progress consolidation) were each justified and non-padded, but the
genuine angles are now exhausted within this arc's scope. This cycle closes
out.

## What the 20-cycle arc produced

No proof of Beal, and no proof of even $(3,5,7)$. The deliverable — as scoped
from the start — is a **compounding, sourced, precisely-mapped research
frontier**, not a proof. Concretely:

- **Two clean reductions** (pairwise-coprime [[method-pairwise-coprime-reduction]];
  exponents to {odd primes}∪{4} [[method-exponent-reduction]]).
- **The exact frontier located**: $(3,5,7)$ is the smallest open Beal signature
  [[rg2024-357-smallest]]; the open region is the all-distinct-odd-prime class.
- **The entire open content named**: the upgrade "finitely many → zero" per
  signature — Darmon–Granville [[thm-darmon-granville]] gives finiteness, abc
  gives no more [[method-abc-finiteness]], nothing makes the zero upgrade.
- **Six convergent angles** (five rigorous + one soft), each breaking at
  $(3,5,7)$ for an independent reason, unified by one structural absence:
  **deep hyperbolicity + no exponent 2** (no near-spherical finite quotient,
  no $X(r)$ modular-curve interpretation).
  - 1 Frey/modularity [[method-frey-modularity]] [[method-frey-level-lowering-obstruction]]
  - 2 Darmon program [[method-darmon-program]]
  - 3 Mordell lens [[method-mordell-curve-lens]]
  - 4 infinite descent [[method-infinite-descent]]
  - 5 spherical reduction [[method-spherical-reduction]]
  - 6* counting heuristic (soft) [[method-counting-heuristic]]
- **The obstruction located at the reduction step, not the resolution step**:
  Chabauty / effective Faltings / Mordell–Weil sieve all work and finished the
  solved cases; the missing piece is *getting to finitely many curves to
  resolve* without a shared/even/spherical structure. The one effective
  precedent at a hyperbolic signature — PSS $x^2+y^3=z^7$ [[pss2007]]
  [[method-triangle-group-descent]] — was verified against the paper and shown
  to rely on exactly the structure $(3,5,7)$ lacks.
- **Two concrete forward directions** (attempt-11, refined 14/17): (A) extend
  Darmon's Frey-variety method + prove generalized-Mazur irreducibility; (B) an
  effective finiteness mechanism not relying on a finite triangle group. Both
  are major open projects, not transplants of existing theorems.
- **A falsifiable prediction, made and confirmed**: the counting heuristic
  predicted min non-degenerate coprime gaps grow with $-\chi$ (attempt-19);
  $(3,7,11)$ was computed afterward (attempt-20) and gave $277 > 77 > 29$,
  exactly the predicted monotone trend.
- **Empirical rigidity across three signatures**: 0 coprime exact, 0 genuine
  gap-1, all gap-1 degenerate on universal families
  $t^{\operatorname{lcm}(p,r)}{+}1$, $t^{\operatorname{lcm}(q,r)}{+}1$.

## Discipline that held throughout

- **Append-only attempts + correction blockquotes**: errors caught by
  verification (the $(2,3,7)$ spherical mislabel, attempt-17; the
  attempt-11 overstatement, attempt-14) were corrected with a dated trail,
  never silently overwritten. Method pages (wiki-layer, mutable) were fixed
  directly with the correction logged.
- **Flagged to-verify items**: unverified claims (PSS from a search summary)
  were flagged, then verified against the primary source — which is how the
  factual error was caught. The discipline worked as intended.
- **Honest framing**: outcomes labeled partial/confirmed/breakthrough-diagnostic;
  no overclaiming; the box-limited scope of every computation stated; heuristics
  flagged as non-theorems.
- **Three Lint passes** (attempts 10, 15, 18) kept the ~35-page wiki consistent
  as it grew; no broken links, orphans, or live contradictions survived.

## The compounding artifact

The wiki itself is the deliverable. 35+ pages across `problems/`, `theory/`,
`sources/`, governed by `SCHEMA.md`, indexed in `index.md`, audited in `log.md`.
Stable claim tags (`[rg2024-*]`, `[dv2022-*]`, `[pss2007-*]`) are the join keys
that make claims editable in one place and trusted everywhere. A future
session does not re-derive this; it extends it.

## Resume point for a future session

Read `progress.md` first (the current frontier, consolidated through
attempt-20), then `synthesis.md` (the structural picture). To extend:
- Pick up **direction (A)** — what would extending Darmon's Frey-variety
  method to three distinct primes concretely require?
- Pick up **direction (B)** — is there *any* effective-finiteness mechanism
  that bypasses the finite-triangle-group requirement?
- **Ingest a new source** against the stable claim tags (e.g. the Siksek–Stoll
  $(3,4,5)$ paper itself, still flagged to-verify in synthesis).
- **Extend the empirical line** to a fourth signature if a new prediction is
  worth testing.

## Outcome

**partial — arc complete.** This was never going to prove Beal in 20 cycles
(or likely at all, with current machinery); the realistic goal was a precise,
sourced, compounding frontier, and that is what was built. The loop stops
here. The user can resume anytime — with `/loop` for another autonomous arc, or
by pointing at a specific direction above.

*End of 20-cycle loop.*