---
type: method
name: multi-agent-harness
created: 2026-09-09
tags: [methodology, governance]
used-in: [[beals_conjecture]], [[birch_swinnerton_dyer]], [[navier_stokes]], [[yang_mills]], [[hodge_conjecture]], [[collatz_conjecture]], [[riemann_hypothesis]], [[PvsNP]]
provenance: [[gemini-contribution-plan-2026-09-09]]
---

# Multi-agent harness (contract-scoped ensemble)

**What:** every Attack/Continue on an active problem runs as four
contract-scoped roles, never one monolithic context: **Orchestrator**
(the main session; frontier + dispatch; writes structural files only),
**Worker/Prover** (one node, isolated context; files work; may not
change any node status), **Target Reviewer** (adversarial parity check
of Worker output vs. the informal source; separate context — nobody
reviews their own work), **Refiner** (failing-node fixes under a hard
budget; on exhaustion signals the Orchestrator to trigger the Dynamic
Splitting Protocol). Status changes require: Worker filed → Reviewer
verdict → Orchestrator updates `dag.md`/`index.md`/`progress.md` with
anchors. All dispatches under `.claude/usage-policy.md` zones.

**When to reach for it:** any node dispatch on an actively-attacked
problem (see each problem's `dag.md`); any long-horizon session where
one context window would hold the whole repo. Not for one-off Queries
or Lint passes.

**Provenance:** Gemini's plan [gemini-plan-multi-agent]
(sources/gemini-contribution-plan-2026-09-09.md), translated to the
Markdown medium 2026-09-09; Lean-literal parts rejected (no Lean
infrastructure exists here — see the source's ingest note).