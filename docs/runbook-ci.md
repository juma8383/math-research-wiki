# CI runbook — wiki structure gate

## What runs
`scripts/lint_dag.py --ci` + the linter's unit tests on every push and
PR to main. Blockers fail the check; warnings never do.

## Enforce as merge authority (one-time, GitHub web UI)
Settings -> Branches -> Add branch protection rule -> Branch name
pattern `main` -> check "Require status checks to pass" -> select
`lint` -> require branches up to date. (Needs admin on
github.com/juma8383/math-research-wiki.)

## Weekly Lint cadence
Run `python scripts/lint_dag.py` locally (or read the latest Actions
run); fix findings as a logged `[LINT <date>]` pass per SCHEMA.md.

## If the check goes red
The linter is report-only. Fix the named files (bookkeeping may be
edited in place; content pages under the append-only discipline), then
push. Never bypass a red check to merge.