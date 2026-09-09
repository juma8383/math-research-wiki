# Harness Trial Report — end-to-end run (overhaul Task 8)

**Date:** 2026-09-09 · **Problem:** beals-conjecture · **Verdict: PASS**

First live end-to-end run of the multi-agent math harness built by this
overhaul (dag manifest → Orchestrator node selection → Scout gate →
Worker → Target Reviewer → Orchestrator status update → linter). All
four roles exercised on one real open leaf.

## The run

| Step | Role | Result |
|---|---|---|
| 1. Node selection | Orchestrator | open leaf `beal-nearmiss-5713-widbox-verify` from `problems/beals-conjecture/dag.md` — the computational census (plan's preferred candidate (a)); dispatched solo under the usage zone cap |
| 2. Scout gate | Scout (WebSearch) | `scout: not-found` — no existing (5,7,13) gap census in the literature (BealsTriples uses different methodology; Project Goliath signature sweeps skip (5,7,13); recorded in attempt-26 frontmatter) |
| 3. Prove | Worker (`worker-prover` contract) | filed `attempts/attempt-26.md` + new `scripts/search_5713_widbox.py` in one attempt file, no status changes, no subagents |
| 4. Verify | Target Reviewer (read-only) | **`review: target-reviewer 2026-09-09 APPROVED`** — semantic parity, numeric parity (hand-verified arithmetic), novelty, honesty: all items |
| 5. Status update | Orchestrator | dag node → `proven`; `progress.md` `to-verify` discharged; `index.md` + `log.md` bookkeeping; linter re-run |

## Claim verified

Attempt-24's flagged `to-verify` datum — min genuine coprime near-miss
gap **1771 at $(A,B,C)=(6,3,2)$** for signature $(5,7,13)$ —
**CONFIRMED, not corrected**, over the strictly wider box $C\le120$,
$B\le2\cdot10^4$ (all $A$; 617,334 candidate triples, 3.5 s, pure
integer arithmetic, overshoot-inclusive scan + T3 quasi-degenerate
filter). 0 exact solutions; 2 gap-1 hits, both unit-base on the
universal $t^{65}+1$ family (now non-vacuously witnessed in-box at
$t=2$); Corner Principle holds (min at $C=2$); quasi-degenerate layer
min 2187 strictly above. The Orchestrator independently reproduced the
headline numbers before review (exact match to the Worker's).

## Status delta

- `problems/beals-conjecture/dag.md`: node `beal-nearmiss-5713-widbox-verify` `open` → **`proven`** (source `[[near-miss-stratification]]`, a proven theorem page — linter parity holds); anchors = attempt-26 + the `review:` line.
- `problems/beals-conjecture/progress.md`: dated resolution note discharges attempt-24's `to-verify`; the counting-heuristic rate claims resting on the 1771 datum stand on verified ground.
- `SCHEMA.md`: attempt `outcome:` vocabulary amended **additively** to include `confirmed` (with a one-line meaning: a completed verification/census whose central claim is confirmed — distinct from `solved` = a proof). Rationale: 12 attempts use it as folder precedent; the linter checks presence, not enum; rewriting attempt-26 to `solved` would have been dishonest.
- `log.md`: `[HARNESS 2026-09-09]` entry (append-only).

## Friction notes (harness improvements for the next dispatch)

1. **Custom agent types not registered in the running session** —
   `worker-prover`/`target-reviewer` fell back to `general-purpose`
   with the agent-file contract inlined verbatim (spec-honest per
   SCHEMA's per-tool-not-per-path note). Future sessions started after
   the agents' landing will register them natively.
2. **EOL discipline is load-bearing.** `log.md` is CRLF+BOM with 25
   ratified LF-stray lines; a whole-file read-modify-write churned 25
   lines twice before the fix (append-as-raw-bytes + targeted line
   splice). Rule now enforced in every dispatch: binary EOL-preserving
   edits only; never normalize.
3. **Log-prefix vocabulary is `[A-Z]+`** — hyphenated entry types
   (`[HARNESS-TRIAL]`) are unparseable by `lint_dag.py`; use a
   single-word prefix (`[HARNESS]`). Worth a SCHEMA one-liner if more
   prefixes appear.
4. **`outcome: confirmed` needed a schema amendment** — the folder's
   de-facto vocabulary ran ahead of SCHEMA's enum; the additive fix is
   landed in the same commit (flagged by the Target Reviewer as a
   harness note — exactly the honesty gate working).
5. **Push of `main` remains parked on credential scope** — the gh
   keyring token lacks `workflow` scope, so the 20-commit stack (incl.
   `.github/workflows/lint.yml`) is local-only until the user runs
   `! gh auth refresh -h github.com -s workflow` (or pushes via their
   own tooling); first live Actions-run verification deferred until
   then (Task 6 Step 4 deferred ruling).

## Artifacts

- `problems/beals-conjecture/attempts/attempt-26.md` (Worker; carries `scout:`, `node:`, appended `review:` line)
- `problems/beals-conjecture/scripts/search_5713_widbox.py` (Worker; pure computation, no model backends — Ollama-only environment respected)
- `problems/beals-conjecture/dag.md`, `problems/beals-conjecture/progress.md`, `index.md`, `log.md`, `SCHEMA.md` (Orchestrator bookkeeping)
- Review package: `.superpowers/sdd/2026-09-09-math-wiki-overhaul/` (attempt + reproduction run outputs)

**Post-trial lint: 0 blockers, 128 warnings, CI gate green (exit 0).**