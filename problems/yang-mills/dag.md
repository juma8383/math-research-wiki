---
type: dag
problem: yang-mills
last-updated: 2026-09-09
---

# Proof DAG — yang-mills

Live frontier: continuum-limit + IR mass-gap control (dimensional
transmutation) — the UV-to-IR bridge; plus the framework-existence
wrinkle (a non-perturbative 4D gauge-theory definition is itself open,
Gribov ambiguity).

- id: yang-mills-itself
  kind: conjecture
  status: open
  uses: [yang-mills-theory, wightman-os-axioms, mass-gap-confinement, asymptotic-freedom, lattice-gauge-constructive, balaban-rg, constructive-continuum-limit, seiberg-witten-supersymmetric]
  source: [[yang_mills]]
  next: two coupled control steps — continuum limit (with full O(4)
    covariance) and uniform-in-a IR gap transport; open leaves:
    direction (A) constructive continuum program, (B) SUSY dual-Meissner
    control (attempt-02/03), (C) Chatterjee mass-gap-hypothesis gate
    (attempt-04)
- id: yang-mills-theory
  kind: definition
  status: open
  uses: []
  source: [[yang-mills-theory]]
  next: classical 4D YM is scale-invariant — dimensional transmutation
    makes continuum limit and mass gap the same RG problem
- id: wightman-os-axioms
  kind: definition
  status: open
  uses: []
  source: [[wightman-os-axioms]]
  next: the existence target itself — no 4D interacting QFT satisfies
    them; O(4) covariance open (framework-existence wrinkle)
- id: mass-gap-confinement
  kind: definition
  status: open
  uses: []
  source: [[mass-gap-confinement]]
  next: —
- id: asymptotic-freedom
  kind: theorem
  status: proven
  uses: [yang-mills-theory]
  source: [[asymptotic-freedom]]
  next: perturbative UV control only — no IR control parameter; the
    UV half of the bridge
- id: lattice-gauge-constructive
  kind: theorem
  status: proven
  uses: []
  source: [[lattice-gauge-constructive]]
  next: rigorous at finite spacing (reflection positivity, transfer
    matrix, strong-coupling area law/gap at finite $a$) — resolution
    layer; the limit is the open control
- id: balaban-rg
  kind: theorem
  status: proven
  uses: []
  source: [[balaban-rg]]
  next: UV stability uniform in the lattice spacing (Balaban CMP
    95-122) — leaves continuum limit / mass gap / IR open: the UV
    half of the bridge, not the bridge
- id: seiberg-witten-supersymmetric
  kind: theorem
  status: proven
  uses: []
  source: [[seiberg-witten-supersymmetric]]
  next: exact low-energy theory for N=2 SUSY YM with dual-Meissner gap
    after soft breaking to N=1 — a solved RELATED problem; no known
    bridge to pure YM (the control SUSY supplies is what pure YM lacks)
- id: constructive-continuum-limit
  kind: method
  status: open
  uses: [lattice-gauge-constructive, balaban-rg, wightman-os-axioms]
  source: [[constructive-continuum-limit]]
  next: the reusable engine (RG control, cluster expansion, OS
    reconstruction, gap transport) — the open control steps
    (convergence + O(4) covariance, uniform gap transport, Gribov) ARE
    the obstruction