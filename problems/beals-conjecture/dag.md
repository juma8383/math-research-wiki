---
type: dag
problem: beals-conjecture
last-updated: 2026-09-09
---

# Proof DAG — beals-conjecture

Live frontier: signature (3,5,7); the obstruction is the
control/reduction step (attempt-11 directions A/B; attempt-24/25
heuristic-verified near-miss stratification).

- id: beal-equation
  kind: definition
  status: open
  uses: []
  source: [[beal-equation]]
  next: —
- id: pairwise-coprime-reduction
  kind: method
  status: open
  uses: [beal-equation]
  source: [[pairwise-coprime-reduction]]
  next: —
- id: exponent-reduction
  kind: method
  status: open
  uses: [beal-equation]
  source: [[exponent-reduction]]
  next: —
- id: fermat-last
  kind: theorem
  status: proven
  uses: []
  source: [[fermat-last]]
  next: —
- id: darmon-granville
  kind: theorem
  status: proven
  uses: []
  source: [[darmon-granville]]
  next: finiteness per signature only — zero for no signature
- id: frey-level-lowering-obstruction
  kind: method
  status: open
  uses: [fermat-last]
  source: [[frey-level-lowering-obstruction]]
  next: —
- id: near-miss-stratification
  kind: theorem
  status: proven
  uses: [catalan-mihailescu]
  source: [[near-miss-stratification]]
  next: —
- id: catalan-mihailescu
  kind: theorem
  status: proven
  uses: []
  source: [[catalan-mihailescu]]
  next: —
- id: beal-itself
  kind: conjecture
  status: open
  uses: [pairwise-coprime-reduction, exponent-reduction,
         darmon-granville, near-miss-stratification,
         frey-level-lowering-obstruction]
  source: [[beals_conjecture]]
  next: open leaves for the (3,5,7) attack are the modular (A) and
    geometric (B) directions (attempt-11/17) — dispatch targets when
    the harness goes live
- id: beal-nearmiss-5713-widbox-verify
  kind: method
  status: proven
  uses: [near-miss-stratification]
  source: [[near-miss-stratification]]
  next: RESOLVED — widened-box census (attempt-26,
    `scripts/search_5713_widbox.py`): min genuine coprime gap 1771
    CONFIRMED at $(6,3,2)$ over $C\le120$, $B\le2\cdot10^4$ (0 exact;
    2 gap-1, both T1 universal-family; Corner Principle holds;
    quasi-degenerate min 2187 strictly above); attempt-24's
    `to-verify` discharged. Anchors: attempts/attempt-26.md + the
    `review:` line appended there (target-reviewer 2026-09-09
    APPROVED)
