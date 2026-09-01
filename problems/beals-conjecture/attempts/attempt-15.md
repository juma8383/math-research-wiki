---
type: attempt
problem: beals_conjecture
attempt: 15
date: 2026-08-24
approach: Second Lint pass over the ~28-page wiki after the attempt-14 ingest
outcome: confirmed
tags: [lint, cross-references, superseded-claim-marker, maintenance]
loop_cycle: 13 of 20
---

# Attempt 15 — Second Lint pass

Second health check after the attempt-14 ingest added `method-triangle-group-
descent`, `source pss2007`, refined `synthesis.md`, and filed `attempt-14`.
Scope: new-page orphans, broken cross-refs, claim-tag resolution,
superseded-claim handling, and consistency of the corrected direction (B).

## Method

Grepped for the new slugs `method-triangle-group-descent` and `pss2007` and the
new claim tags; checked inbound links; checked `problem.md` tools-list
freshness; checked consistency between attempt-11's direction (B) claim and the
attempt-14 correction.

## Findings

### Broken links / claim tags — NONE
`method-triangle-group-descent` resolves and is linked from `synthesis.md` and
the `pss2007` source. The `pss2007-*` claim tags are all defined in
`sources/poonen-schaefer-stoll-2007.md`. No dangling references.

### Orphans — NONE
The new method page has inbound links from `synthesis.md` and `pss2007`; the new
source is reached via `index.md` and cited from `attempt-14`. (The individual
`pss2007-*` tags are defined but not yet cited individually — acceptable, as
tags are a standing resource for future citation; the source is cited as a
whole.)

### Stale tools list — 1 (FIXED)
`problem.md` frontmatter `tools:` was missing `method-triangle-group-descent`
(added in attempt-14 but not registered). Added it (now 16 entries).

### Superseded claim not marked — 1 (FIXED)
`attempt-11`'s direction (B) still read "no such reduction is known," which
attempt-14 corrected (the Darmon–Granville covering descent *is* a reduction,
but ineffective). Per append-only discipline the original text was **not**
rewritten; instead a **correction blockquote** was inserted at the top of the
(B) subsection pointing to `[[method-triangle-group-descent]]`, the corrected
synthesis, and stating the correction is authoritative. This keeps the audit
trail honest while preventing a reader landing on attempt-11 from taking the
stale claim as current.

### Contradictions — NONE
The five-thread obstruction table in `synthesis.md` (five threads) and
attempt-14's "six angles" framing are consistent: the sixth (triangle-group
lens) is explicitly a *refinement* of how threads 5 and (B) relate, not a new
independent obstruction. The synthesis "what a proof requires" section carries
the corrected direction (B). No conflicting current claims.

### Stale claims — NONE
Both prior sources (`rg2024`, `dv2022`) current; `pss2007` newly ingested and
flagged (mechanism extracted from a search summary, to verify against paper)
in its own page.

## Outcome

**confirmed — wiki healthy after the ingest.** One stale tools-list entry
fixed; one superseded claim properly marked (append-only + correction pointer)
rather than rewritten; no broken links, orphans, or contradictions. The
superseded-claim handling is the notable improvement over the first Lint: the
wiki now models its own corrections as first-class, dated annotations — which
is exactly the compounding-discipline the LLM-wiki pattern calls for.

## Next cycles (7 remain)

- Begin **close-out consolidation**: a final synthesis update reflecting the
  full 15-attempt arc, and a clear "where the problem stands" statement for the
  next session.
- Optional: verify the PSS mechanism against the actual paper (flagged).
- Final Lint at the very end if needed; the wiki is currently clean.