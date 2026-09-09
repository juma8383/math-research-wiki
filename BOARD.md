# COLLAB BOARD — read this FIRST, every session

**Purpose:** cross-machine coordination between the Hermes sessions working this
repo. Windows box (`juma8`, git-bash + WSL2 Ubuntu, Sage 10.9 in WSL at
`~/miniforge3/envs/sage/bin/sage`) is the ONLY session that pushes to GitHub.
Other machines (e.g. Linux box) compute locally and post here.

**Protocol — EVERY session, BEFORE any work:**
1. `git pull` (Windows does the pushing; Linux may also pull).
2. Read `BOARD.md` TOP to the `---` line (head -40 is enough).
3. Do NOT touch files listed in "IN FLIGHT" — they belong to the claiming
   session until it posts DONE/BLOCKED.
4. Claim new work by ADDING a row under "In flight" (edit + commit + push, or
   leave uncommitted if you cannot push; Windows will push it).
5. When done: move your row to "Resolved" (or fold into the log) and add a
   RESULT line. Append-only below the `---` line; newest RESOLVED at top.
6. Never rewrite others' entries. Corrections = new dated line.

**Commit hygiene:** keep research commits (notes/log/scripts) SEPARATE from
board commits when convenient; board-only commits are cheap and fine.

## In flight
| session | machine | work | claimed | note |
|---|---|---|---|---|
| hermes-win | Windows | Sieve re-verification `[mss-k34-sieve2-sage]` (scripts/mss_k34_sieve2_sage_check.sage) | 2026-09-08 | background run; posting result |

---
<!-- APPEND BELOW. Newest first inside each list. -->

## Resolved
*(empty)*

## Blockers / questions
*(none)*