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
