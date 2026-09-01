# Math Wiki

A persistent, compounding research notebook for open math problems. The LLM
owns all bookkeeping — working attempts, filing theorems and methods into a
shared toolbox, indexing, and logging — so that work **survives across sessions
and compounds** rather than being re-derived from scratch every time.

Based on the [LLM-Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
*"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*

## How it's organized

- **`problems/<slug>/`** — one folder per problem. Holds the statement, a
  running `progress.md` (the current frontier), and an `attempts/` folder with
  one file per work session.
- **`theory/`** — the shared, compounding toolbox: `theorems/`, `lemmas/`,
  `methods/` (reusable attack techniques), `definitions/`, `conjectures/`. A
  method discovered on problem A is filed here for reuse on problem B.
- **`sources/`** — verbatim reference material (papers, transcripts). Immutable.
- **`index.md`** — catalog of every page; the map of what exists.
- **`log.md`** — append-only audit trail of every Attack / Continue / Query /
  Lint.
- **`SCHEMA.md`** — the rules: directory layout, page frontmatter, and the
  four workflows (Attack / Continue / Query / Lint). **Read this first.**

## How to use it

1. Give me a math problem. I'll **Attack** it: create its folder, start the
   first attempt, and begin working toward a breakthrough or solution.
2. In a later session, just say *"continue <slug>"* (or just describe the
   problem) and I'll read the prior progress and pick up from the frontier.
3. Ask questions about accumulated knowledge and I'll answer from the wiki,
   citing pages, and file good answers back as new theory pages.
4. Every so often I run a **Lint** pass to catch contradictions, orphans, and
   missing links.

Everything is plain markdown. Point Obsidian (or any markdown editor) at this
folder for graph view, search, and cross-link navigation.

## Why publish it

Every substantive claim in the wiki is backed by a **script + log pair** under
the owning problem's `scripts/` folder, and the append-only `log.md` records
every work block — including failed attempts, corrections, and even incidents
(with recovery notes). That makes the notebook auditable in a way a finished
PDF is not: you can check where a number came from, and you can watch errors
get caught and fixed rather than silently rewritten.

## Honesty conventions

- **`[to-verify]`** — a claim known only at second-hand (search-derived,
  unrefereed preprint, or citation not yet checked against the primary
  source). Published flagged, never silently.
- **`[summary]`** — content derived from an abstract/summary rather than the
  full primary text.
- **Heuristics are labeled as heuristics.** The probabilistic pages (expected
  solution counts, window models, plane heuristics) are models with explicit
  assumptions — they are evidence about what to expect, not theorems. The
  wiki keeps a hard line between *proved* (theorem, with proof), *computed*
  (census, with script + log), and *modeled* (heuristic, with assumptions).

## Status

This is an LLM-maintained research notebook, not peer-reviewed literature.
Flagged results should be treated with exactly the skepticism their flags
announce. Corrections are applied append-only with the error left visible in
place.

## License

- Wiki content: **CC BY 4.0**
- Code (all `*.py`): **MIT**

See [LICENSE.md](LICENSE.md).