---
type: attempt
problem: beals_conjecture
attempt: 18
date: 2026-08-24
approach: Final Lint pass — verify the attempt-17 corrections are consistent across the whole wiki
outcome: confirmed
tags: [lint, consistency, correction-trail, cross-references]
loop_cycle: 16 of 20
---

# Attempt 18 — Final Lint: correction consistency

The attempt-17 corrections touched 4 files (`method-triangle-group-descent.md`,
`sources/poonen-schaefer-stoll-2007.md`, `attempt-14.md`, `synthesis.md`) plus
index descriptions. This cycle is a full Lint to confirm the corrected
$(2,3,7)$-**hyperbolic** framing is consistent everywhere — no dangling
"spherical" mislabels of $(2,3,7)$, no stale `$41/42>1$`, all cross-refs and
claim tags resolve.

## Checks run

1. **Grep `41/42` across all `.md`.** Every occurrence is now in one of three
   legitimate contexts:
   - correction blockquotes that *flag the old error as an error*
     (`attempt-14.md:13`, `attempt-17.md:43,93`, `pss2007:45`,
     `triangle-group-descent.md:48,62`);
   - the append-only `log.md` historical entry (`log.md:302`) that records the
     correction, and the earlier entry (`log.md:246`) it supersedes — both kept
     by append-only discipline, the later one explicitly marking the earlier
     wrong;
   - the corrected table row `$(2,3,7)\;|\;41/42<1\;|\;\text{hyperbolic}$`
     (`triangle-group-descent.md:62`).
   No live page states $41/42>1$ as current fact. ✓

2. **Grep `spherical` (case-insensitive).** Audited every hit. All uses of
   "spherical" as a *current* claim are correctly attached to genuinely
   spherical signatures — $(2,3,5)$ ($31/30>1$), the spherical family
   $(2,2,n),(2,3,3),(2,3,4),(2,3,5)$ — in `spherical-reduction.md`,
   `attempt-08.md`, `beal-equation.md`, `synthesis.md`, `progress.md`. The
   "near-spherical" qualifier (the corrected enabler for PSS) is used
   consistently for $(2,3,7)$ in `triangle-group-descent.md`, `pss2007`,
   `synthesis.md`. ✓

3. **One stale line found and fixed.** `index.md` line 25 (the attempt-14
   catalog one-liner) still read "PSS $(2,3,7)$ effective via finite PSL2(F7)
   **needs spherical signature**" — the old wrong framing, contradicting the
   correction blockquote at the top of `attempt-14.md` and the corrected
   `method-triangle-group-descent.md`. Fixed inline (index is a mutable
   navigation file): now reads "effective via finite quotient PSL₂(F₇) of the
   *infinite* Δ(2,3,7) needs near-spherical position + exponent 2
   [corrected in attempt-17: original text mislabeled (2,3,7) spherical — it
   is hyperbolic, χ=−1/42]". This was the only live inconsistency; it lived in
   the one-line summary, which the prior correction pass had not touched.

4. **Cross-references / claim tags.** Extracted all `[[…]]` targets (20 real
   page slugs + 4 claim tags + 3 source ids). Verified each resolves:
   - page slugs → existing files under `theory/{theorems,methods,definitions,
     conjectures}/`, `problems/beals-conjecture/`, `sources/` — all present;
   - claim tags `rg2024-357-smallest`, `rg2024-comp-bound`,
     `rg2024-faltings-algorithm`, `dv2022-irreduc-conjecture` — all defined
     in their source pages;
   - the `[[…]]`, `[[<other-slug>]]`, `[[method-pmi]]`, `[[dv2022-…]]` tokens
     are illustrative placeholders in `SCHEMA.md` and `attempt-10.md`'s
     convention explanation, not real references.
   No broken links. ✓

5. **Orphans.** Every wiki page has inbound links: theory pages from
   `problem.md`'s tools list and `synthesis.md`'s obstruction table; sources
   from attempts and method pages; attempts from `index.md`. `progress.md`
   and `notes.md` are working files navigated by convention (read-first /
   scratchpad), not wiki pages requiring inbound links. No orphans. ✓

## Outcome

**confirmed.** The wiki is internally consistent after the attempt-17
correction. The append-only discipline held: the old wrong statement survives
only in (a) the superseded historical log entry, (b) the attempt-14 body
beneath its correction blockquote, and (c) correction blockquotes that label
it as an error — never as current fact in a mutable page. One stale index
one-liner was the sole live inconsistency, now fixed. No broken links, no
orphan pages, no unresolved claim tags.

## State of the arc (cycle 16/20)

4 cycles remain. The wiki is clean and the convergent diagnosis is stable:
the obstruction at all-distinct-odd-prime signatures is **deep hyperbolicity
+ no exponent 2**, gating the modular, spherical-reduction, and PSS routes
together. Per the honesty guard recorded in attempt-17: the remaining
cycles should avoid padding. If no genuine new angle appears, the right
move is to declare the arc complete with a close-out summary rather than
manufacture content. The next cycle will assess whether a substantive new
thread exists (e.g. a fresh source to ingest or a new computational probe);
if not, it will write the loop close-out.