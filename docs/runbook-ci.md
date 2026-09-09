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

## Warnings (Task 5, 2026-09-09)

Lint `warning:` lines NEVER fail CI and are not selectable as a
required check until the workflow has run at least once; branch
protection is tightened only after the green baseline (and admins
bypass by default unless "do not allow bypassing" is set). Current
honest leaves that stay: unknown page type '' / 'progress' / 'notes'
(the nested PvsNP wiki's own convention and the working-notebook
pages — SCHEMA.md defines no type for them), and `claim tag defined
but never cited` on sources pages (defined for future use). Do not
"fix" these by inventing types or deleting definitions.
