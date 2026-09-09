---
type: dag
problem: PvsNP
last-updated: 2026-09-09
---

# Proof DAG — PvsNP

Live frontier: $\mathrm{NP}\not\subseteq\mathrm{P/poly}$; the
obstruction `[witness-needs-explicit-lb]` = an open non-compositional
construction (A) — an explicit balanced-point witness for the S1.a
(AC^0) face — with the three local barriers (relativization / natural
proofs / algebrization) as local symptoms and the construction lock as
the universal wall.

- id: pvsnp-itself
  kind: conjecture
  status: open
  uses: [construction-a, barrier-relativization, barrier-natural-proofs, barrier-algebrization]
  source: [[PvsNP]]
  next: the single live thread is construction (A) at the balanced
    point of {expensive and small-gap} (S1.a face) — the three local
    barriers are symptoms; the construction lock is universal
- id: construction-a
  kind: conjecture
  status: open
  uses: [barrier-relativization, barrier-natural-proofs, barrier-algebrization]
  source: problems/PvsNP/progress.md
  next: an explicit function at the balanced point of {expensive and
    small-gap} for the AC^0 (S1.a) face satisfying
    {deterministically-constructible and non-recognizable} — Gate 1
    (recognizability) discharged soft from three directions; Gate 2
    (tight window) is the binding residual; an open construction,
    blocked by open-ness not a theorem
- id: barrier-relativization
  kind: theorem
  status: conditional
  uses: []
  source: problems/PvsNP/progress.md
  next: Baker-Gill-Solovay oracles — proven in the literature but
    anchored here to the live-thread section (PDF-line verification
    pending per the honesty ceiling); escaping it (descriptive
    complexity, cycle 28) isolates but does not remove the lock
- id: barrier-natural-proofs
  kind: theorem
  status: conditional
  uses: []
  source: problems/PvsNP/progress.md
  next: Razborov-Rudich natural proofs + the Fan-Li-Yang black-box
    barrier guarding the mining face (cycle 19/20) — proven in the
    literature, PDF-line verification pending; NEXP-lower-bound
    techniques are all natural-proofs-blocked
- id: barrier-algebrization
  kind: theorem
  status: conditional
  uses: []
  source: problems/PvsNP/progress.md
  next: Aaronson-Wigderson algebrization — proven in the literature,
    PDF-line verification pending; escaping all three (GCT, cycle 26)
    does not remove the lock, it isolates it