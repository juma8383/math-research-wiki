---
type: attempt
problem: beals_conjecture
attempt: 10
date: 2026-08-24
approach: Lint pass over the ~23-page wiki (orphans, broken cross-refs, contradictions, stale tools lists)
outcome: confirmed
tags: [lint, cross-references, orphans, maintenance]
loop_cycle: 8 of 20
---

# Attempt 10 — Lint pass

First Lint of the wiki (it had grown to ~23 content pages after attempts
01–09). Per the LLM-wiki Lint operation: find orphans, broken cross-references,
contradictions, stale claims, missing links; fix inline; log the pass.

## Method

Enumerated all 34 `.md` files (Glob), extracted every `[[…]]` cross-reference
(Grep), and checked each against (a) page slugs derived from filenames with
type prefixes `method-`/`thm-`/`conj-`/`def-`/source-id, and (b) claim tags
defined in `sources/`. SCHEMA placeholder links in `SCHEMA.md`
(`[[<other-slug>]]`, `[[method-pmi]]`, etc.) excluded as examples.

## Findings

### Broken links / claim tags — NONE
All page-slug cross-references resolve to an existing page. All claim-tag
references (`[[rg2024-357-smallest]]`, `[[rg2024-comp-bound]]`,
`[[rg2024-faltings-algorithm]]`, `[[dv2022-…]]`) are defined in their source
files. No dangling references.

### Orphan pages — 1 (FIXED)
`theory/definitions/beal-equation.md` had **no inbound** `[[…]]` reference —
it defined the central equation but nothing pointed to it. Fixed by adding
`[[def-beal-equation]]` to `problem.md` (tools list + Provenance section). The
`def-` prefix is consistent with the existing `method-`/`thm-`/`conj-` slug
convention.

### Missing top-level pointer — 1 (FIXED)
`synthesis.md` (the consolidated five-thread map, attempt-09) was reachable only
via the index markdown link. Added a pointer line at the top of `progress.md`
directing readers to `synthesis.md` for the structural picture. Also added a
`synthesis: [synthesis]` field to `problem.md` frontmatter.

### Stale tools list — 1 (FIXED)
`problem.md` frontmatter `tools:` listed only the first 10 pages; it was missing
the four method pages added in attempts 03–08 (`method-darmon-program`,
`method-mordell-curve-lens`, `method-infinite-descent`,
`method-spherical-reduction`) and the definition. Rebuilt the full list (15
entries).

### Contradictions — NONE
The only candidate — attempt-06 says "4-thread diagnosis" while attempt-08/
synthesis say "five-thread" — is **not** a contradiction: it is historical
(fourth thread added in attempt-06, fifth in attempt-08). The progression is
correct and the synthesis page records the final five. No other conflicting
claims found.

### Stale claims — NONE
Both ingested sources (`rg2024`, `dv2022`) remain current; no source has been
superseded. The to-verify items flagged in synthesis.md (cyclotomic UFD
boundary; Siksek–Stoll computational step) are explicitly marked unverified,
not stated as fact — acceptable.

## Orphan-status check (informational)

Pages with no inbound `[[…]]` that are **expected** to be unlinked and so
left alone: `notes.md` (scratch), `log.md`/`index.md` (navigation, linked
structurally not via wikilinks), `README.md`/`SCHEMA.md` (meta), and the
`attempts/` files (linked from synthesis's attempt-index table and the index,
not via wikilinks — by design, since attempts are append-only records).

## Outcome

**confirmed — wiki is healthy.** One orphan fixed, one missing pointer added,
one stale list rebuilt; no broken links, no contradictions, no stale claims.
The cross-reference graph is now complete: every theory page is reachable from
`problem.md` via the `tools:` list, and the synthesis page is reachable from
`progress.md`. Net effect: a fresh session can land on `problem.md` →
`progress.md` → `synthesis.md` and reach every concept page.

## Next cycles

With the diagnostic picture consolidated (synthesis) and the wiki Lint-clean,
the remaining cycles shift from "map the obstruction" to the forward-looking
question:

- **What genuinely-new machinery** would a $(3,5,7)$ proof require? A
  speculative cycle honestly framed (likely: nothing actionable, but completes
  the picture and guards against false hope).
- **Strengthen the degenerate-near-miss claim** computationally — confirm the
  universal families $t^{21}+1$, $t^{35}+1$ account for *all* small gap-1's, not
  just those found.
- A second Lint after the final attempts, before the loop closes.