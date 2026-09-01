# Math Wiki — Schema

> This file fixes the structure, page types, and workflows so every session
> reproduces the same organization. **Without it, every agent reinvents the
> structure.** Adapted from the LLM-Wiki pattern (Karpathy) for mathematics
> research: each problem is a living research thread; theorems, methods, and
> lemmas discovered along the way are filed into a shared **theory toolbox**
> that compounds across problems.

---

## Three layers

1. **Raw sources** (`sources/`) — verbatim, immutable reference material
   (papers, book chapters, transcripts, datasets). The LLM reads but never
   modifies these. Synthesis lives in the wiki layer, never here.
2. **The wiki** — LLM-generated pages: problem folders, theory pages,
   conjectures. The LLM owns all of this bookkeeping.
3. **The schema** (this file) — fixes structure + workflows so every
   Attack / Continue / Query / Lint is reproducible across sessions.

## Directory layout

```
Math/
├── SCHEMA.md                # this file
├── README.md                # human-facing overview
├── CLAUDE.md                # auto-loaded project instructions; loads the two policies below
├── research-protocol.md      # standing 10-step research discipline (every Attack/Continue)
├── .claude/usage-policy.md   # Ollama Pro usage/quota zones (inherited by subagents)
├── index.md                 # catalog of EVERY page, one line each
├── log.md                   # append-only audit trail
│
├── problems/<slug>/         # one folder per problem
│   ├── problem.md           #   statement, status, metadata
│   ├── progress.md          #   running state of the attack (the frontier)
│   ├── attempts/
│   │   └── attempt-NN.md    #   one per work session (zero-padded)
│   └── notes.md             #   scratch / dead ends / half-formed ideas
│
├── theory/                  # the shared, compounding toolbox
│   ├── theorems/<name>.md
│   ├── lemmas/<name>.md
│   ├── methods/<name>.md    #   reusable attack techniques / heuristics
│   ├── definitions/<name>.md
│   └── conjectures/<name>.md  # open questions our work raised
│
└── sources/<id>.md          # raw reference material, immutable
```

---

## Page types & frontmatter

Every page begins with YAML frontmatter. `type` is required on all pages.

### `problem.md`
```yaml
---
type: problem
slug: <kebab-case-slug>
title: <human title>
status: open | in-progress | solved | abandoned
difficulty: unknown | easy | medium | hard | famous-open-problem
created: <YYYY-MM-DD>
last-updated: <YYYY-MM-DD>
tags: [number-theory, analysis, ...]      # topic areas
tools: [[method-pmi], [thm-fund-thm-arithmetic]]   # theory pages used
related: [[<other-slug>]]
---
```
Body: full problem statement, provenance (who posed it, where), any known
partial results, and the reward/context. This page is the anchor for the folder.

### `attempts/attempt-NN.md`
```yaml
---
type: attempt
problem: <slug>
attempt: NN
date: <YYYY-MM-DD>
approach: <one-line summary of the angle>
outcome: stuck | partial | breakthrough | solved | dead-end
tags: [tags touched this session]
---
```
Body: the actual working — reasoning, computations, dead ends, what was tried
and why it did/didn't work. **Be honest about failures**; they are the most
reusable part. End with a "Next" section pointing at the most promising thread.

### `progress.md`  (per problem)
Running summary of the **current frontier**: what is known, what has been
tried, the best partial result so far, the live conjectures, and the single
next step. This is what a fresh session reads first to resume. Keep it
short — details live in the attempts.

### `notes.md`  (per problem, optional)
Loose scratch: observations not yet worthy of an attempt, candidate
reformulations, "try this next" sparks. Promote good notes into attempts.

### Theory pages (`theorems/`, `lemmas/`, `methods/`, `definitions/`)
```yaml
---
type: theorem | lemma | method | definition
name: <canonical name>
created: <YYYY-MM-DD>
tags: [topic areas]
used-in: [[<slug>], ...]    # problems this has been applied to
provenance: [[<source-id>]] # where it came from, if external
---
```
Body: statement (precise), the conditions/assumptions, a sketch of why it
holds (for theorems/lemmas), and — for `methods` — *when to reach for it*
(the trigger pattern). A `method` page is the most valuable compounding unit:
"a technique discovered solving problem A, filed for reuse on problem B."

### `conjectures/<name>.md`
```yaml
---
type: conjecture
name: <name>
status: open | proven | disproven | withdrawn
raised-by: [[<slug>]]
created: <YYYY-MM-DD>
evidence: <one line: computational / heuristic / analogy>
---
```
Body: precise statement, motivation, what would prove/disprove it, status.

### `sources/<id>.md`
```yaml
---
type: source
id: <short-stable-id>
title: <title>
author: <...>
date: <YYYY-MM-DD or year>
provenance: <url or "private notes">
tags: [<claim-tag>, ...]
---
```
Body: verbatim text. Inline **claim tags** like `[beal-2026-def]` mark stable
claims; a tag is *defined* once here and *cited* from any wiki page. This is
the join key that makes a claim editable in one place and trusted everywhere.

---

## The four operations

### Attack  (a new math problem is posed)

> **Governs every Attack and Continue:** apply [research-protocol.md](research-protocol.md)
> in full — the 10-step research discipline (evidence AND counterevidence; ≥3
> distinct proof approaches; seek counterexamples; formalize assumptions; track
> failed attempts append-only; derive simpler-equivalent AND more-general
> statements; check computations; re-evaluate confidence), the research
> notebook (the problem folder itself), the stall-tactics frame-changes, and
> the critique-every-conclusion rule. Honesty over optimism; flag `to-verify`.
> Usage/quota discipline in [CLAUDE.md](CLAUDE.md) / [.claude/usage-policy.md](.claude/usage-policy.md).

1. Slug the problem (kebab-case). Create `problems/<slug>/problem.md` with the
   full statement + frontmatter (`status: in-progress`).
2. Create `progress.md` (initial frontier) and `notes.md` (empty).
3. Open `attempts/attempt-01.md` and **start working**: reason, compute,
   test small cases, search for relevant known results. Per the protocol,
   generate evidence AND counterevidence and pursue **at least three distinct
   approaches** — a single-line attack is out of policy.
4. Whenever you apply or discover a theorem / lemma / method / definition,
   **create or update the matching `theory/` page** and add a `used-in` link
   back to this problem. This is where compounding happens — do not skip it.
5. If a new question arises from the work, file a `conjectures/` page.
6. Update `progress.md` to reflect the new frontier.
7. Add the new pages to `index.md` (one line each) and append a dated entry to
   `log.md` with prefix `[ATTACK <date>]`.
8. On breakthrough/solution: set `problem.md` `status: solved`, write the full
   solution in an attempt, and note it in `progress.md`.

### Continue  (resuming a problem in a new session)
1. Read `index.md` → the problem's `problem.md` → `progress.md` → the last
   `attempt-NN.md`.
2. Pick up from the recorded frontier. Open the next `attempt-NN.md`.
3. Work as in Attack; keep theory pages, progress, index, and log current.
4. **Never silently re-derive** what a prior session already filed — read it
   first, build on it, and cite the earlier attempt.

### Query  (answer a question from accumulated knowledge)
Search `index.md` → open relevant problem/progress/theory pages → follow
cross-refs → synthesize an answer **citing source tags and page links**. If the
answer is good and reusable, **file it back as a new theory/method page** so the
exploration compounds. Append `[QUERY <date>]` to `log.md`.

### Lint  (the wiki has grown / feels tangled)
Health pass, run every several attacks or when things drift:
- **Contradictions** — two pages claiming incompatible things.
- **Stale claims** — a source was superseded; a conjecture was resolved but
  still marked open.
- **Orphan theory pages** — a theorem/method with no `used-in` links (is it
  real, or a dead lead?).
- **Missing cross-references** — two problems that obviously share a method
  but don't link.
- **Data gaps** — a problem with no attempts, or an attempt with no recorded
  outcome.
Fix inline, append `[LINT <date>]` to `log.md` with what was found and fixed.

---

## Conventions

- **Slugs**: kebab-case, short and stable — `beals-conjecture`,
  `goldbach-weak`. Never rename a slug (it breaks every inbound link).
- **Attempt numbering**: zero-padded, monotonically increasing —
  `attempt-01.md`, `attempt-02.md`. Never edit a past attempt in place; write
  the next one. (Progress.md may be edited; attempts are append-only in spirit.)
- **Cross-references**: use `[[page-slug]]` / `[[method-pmi]]` style links
  liberally. A page with no inbound links is an orphan waiting to be connected.
- **Claim tags**: short stable ids in sources, e.g. `[beal-2026-coprime]`.
  Cite them from wiki pages instead of restating the claim.
- **Honesty over optimism**: record dead ends and failed approaches with the
   same care as successes. The next session needs to know what *doesn't* work.
- **Dates**: absolute `YYYY-MM-DD`. When a session lacks a date, use the
  current date from context.