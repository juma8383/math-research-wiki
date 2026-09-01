# Project instructions — Math research wiki

> Auto-loaded by Claude Code on startup and inherited by every subagent.
> This file is the loader for the two standing policies below; it is kept
> short on purpose (the full rules live in the referenced files).

## 1. The math wiki

This repo is an LLM-maintained, compounding math-research wiki (one folder per
open problem, a shared `theory/` toolbox that compounds across problems).
Structure and workflows are fixed in **[SCHEMA.md](SCHEMA.md)** — read it
before any Attack / Continue / Query / Lint. The catalog of every page is
**[index.md](index.md)**; the append-only audit trail is **[log.md](log.md)**.
Always start a task by reading `index.md` and the relevant problem's
`progress.md` (the read-first file); never silently re-derive what a prior
session filed.

Six problems are under attack: beals-conjecture, birch-swinnerton-dyer,
navier-stokes, yang-mills, hodge-conjecture, collatz-conjecture. A unifying
methodology — "the obstruction is at the **control/reduction step**, not the
resolution step" (6-for-6), with a "one-dimensional engine stops" sub-pattern —
is recorded in each problem's `notes.md` and `progress.md`.

## 2. Research protocol (apply to EVERY conjecture, every time)

Follow **[research-protocol.md](research-protocol.md)** in full. Summary:
never stop at the first plausible proof. For every conjecture run the 10 steps
— generate evidence AND counterevidence; produce **≥3 distinct proof
approaches**; seek counterexamples; formalize all assumptions; track failed
attempts (append-only); derive simpler equivalent AND more general statements;
check computational examples; re-evaluate confidence. Maintain the research
notebook (the problem folder: progress/notes/attempts/theory). When stalled,
change the frame (representation, notation, analogy, generalize, specialize,
reverse, dual). **Critique every conclusion before accepting it; honesty over
optimism; flag to-verify.**

## 3. Usage / quota management (Ollama Pro)

Follow **[.claude/usage-policy.md](.claude/usage-policy.md)**. Summary:
prioritize *completing* work over *parallelizing* it. Conserve as usage grows:

| Zone | Trigger | Max subagents |
|---|---|---|
| Green | <60% session & weekly | 4 |
| Yellow | ≥60% session or weekly | 2 |
| Orange | ≥80% | 1 (conservation) |
| Red | ≥90% | 0 (critical) |
| Emergency | ≥95% | stop, summarize, save state, notify user |

- Before spawning any subagent: estimate cost vs value; prefer **1 agent →
  many subtasks** over 1 task → many agents.
- The model context has **no live Ollama usage-% tool**; a session loop
  (Playwright MCP refreshing the Ollama usage page every ~20 min) writes real
  Session/Weekly % to **[.claude/usage-status.json](.claude/usage-status.json)**
  — when that file is fresh, use its real numbers to pick the zone; otherwise
  apply zones heuristically by task scale/context, and treat any % the user
  reports as authoritative.
- For tasks >~30 min or >~10k lines: plan Analysis → Implementation →
  Validation phases; check usage before each phase.
- Every ~10 min on long tasks: write a recovery summary (objective, done,
  files changed, outstanding, next) so work can resume after quota exhaustion.

## 4. Environment notes

- Windows 11; PowerShell primary, Bash tool available (POSIX). `python` (not
  `python3`); set `PYTHONIOENCODING=utf-8`; avoid non-ASCII in script output.
- Slug convention: problem folders kebab-case; cross-problem wikilinks use
  **UNDERSCORE** (`[[birch_swinnerton_dyer]]`); theory-page slugs kebab
  (`[[thm-mordell-weil]]`).
- Verify load-bearing facts via web search before committing; flag search-
  derived facts `[summary]`/`to-verify` until primary-source-verified.