# P vs NP Research Wiki — Schema

This file fixes the wiki's structure and workflows so any agent can maintain it reproducibly. It is the third layer of the [LLM Wiki](llm-wiki) pattern: it governs the other two (raw sources + wiki pages).

## Directory layout

```
wiki/
  SCHEMA.md            # this file — structure + workflows
  index.md             # catalog of every page, grouped by category
  log.md               # append-only audit trail (INGEST / QUERY / LINT)
  sources/              # RAW, IMMUTABLE source artifacts (verbatim + provenance + claim tags)
  pages/               # LLM-generated wiki pages (summaries, angle/entity/concept pages, comparisons)
```

## Page types (in `pages/`)

- **Angle page** — one research angle (williams-algorithmic, gct, …). Frontmatter: `title`, `category: angle`, `tags`, `status: dead|partially-blocked|alive`, `last_touched`.
- **Concept page** — a cross-cutting idea (barriers, meta-duality, semantic-invariant-gap). `category: concept`.
- **Synthesis page** — a combined/novel view (algorithmic-gct, novel-diagnoses, status-map). `category: synthesis`.
- **Open-problems page** — tracked problems with status. `category: open-problems`.

Every page has YAML frontmatter with at least `title`, `category`, `tags`, `status`.

## Stable claim tags — the join key

A claim tag (lowercase-kebab, e.g. `[bip-2019]`, `[coarsening-gap]`) is **defined once** in the `sources/` file it comes from, with a one-line statement. Any wiki page may cite it. A claim is edited/updated in its source; pages trust the tag. Novel diagnoses/observations we produced get their own tags (e.g. `[coarsening-gap]`, `[meta-duality]`, `[algorithmic-gct]`, `[semantic-invariant-gap]`).

## Workflows

### Ingest (new source)
1. Save the raw artifact under `sources/<YYYY-MM-DD-id>.md` with a provenance header and an **Extracted claims** list (one `tag — statement` per line).
2. In **one pass**, write/update every wiki page it touches (~10-15): the relevant angle page(s), every concept page it bears on, any comparison/status page, and `open-problems.md` if it raises or resolves a problem.
3. Add each new/changed page as a line to `index.md` under its category.
4. Append `[INGEST YYYY-MM-DD] <id> — <one-line>` to `log.md`.
5. A source touching <5 pages was under-ingested — chase the cross-links.

### Query (answer from the wiki)
1. Scan `index.md` → open relevant pages → follow cross-refs (`[[page]]`).
2. Synthesize the answer citing source tags, e.g. "GCT evades natural proofs `[rr-1997]` because…".
3. If the answer is reusable, file it as a new page and index it.
4. Append `[QUERY YYYY-MM-DD] <topic> — <one-line>` to `log.md`.

### Lint (health pass)
Find and fix: contradictions between pages, stale claims (source superseded), orphan pages (no inbound `[[refs]]`), missing cross-references, gaps in `index.md` vs actual files. Append `[LINT YYYY-MM-DD] <summary>` to `log.md`.

## Conventions
- Cross-reference pages with `[[page-name]]` (page slug, no `.md`).
- Cite claims with `[tag]`.
- Never edit `sources/` after the initial ingest (immutable). Corrections/refinements live in pages and get a new source if needed.
- `index.md` is the single map of "what exists"; `log.md` is the single map of "what was done."