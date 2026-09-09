---
type: dag
problem: collatz-conjecture
last-updated: 2026-09-09
---

# Proof DAG — collatz-conjecture

Live frontier: pointwise convergence (no divergent trajectory + no
nontrivial cycle for every $N$); the obstruction is the
average/density-to-pointwise control step — the density engine
controls almost-all but not the measure-zero exceptional set.

- id: collatz-itself
  kind: conjecture
  status: open
  uses: [collatz-map, collatz-density-results, collatz-tao-almost-bounded, collatz-cycle-bounds, collatz-conway-undecidability, average-vs-pointwise-control, cycle-exclusion-linear-forms]
  source: [[collatz_conjecture]]
  next: the open content is "almost all (density) to every $N$
    (pointwise)" — open leaves: (A-i) log-density to natural density
    (blocker: the $\exp(O(n^{1/2}))$ Syracuse-heuristic error), (A-ii)
    natural to pointwise (no pointwise Lyapunov), (B-uniform) all-$m$
    cycle exclusion (transcendence-bottlenecked), (C) a per-trajectory
    Lyapunov (NS-flavored)
- id: collatz-map
  kind: definition
  status: open
  uses: []
  source: [[collatz-map]]
  next: the two failure modes (nontrivial cycle, divergent
    trajectory) are the exact open content
- id: collatz-density-results
  kind: theorem
  status: proven
  uses: []
  source: [[collatz-density-results]]
  next: a.a. $\mathrm{Col}_{\min}<N$ at natural density (Terras,
    five independent proofs) — density-1 slice only, never "all"
- id: collatz-tao-almost-bounded
  kind: theorem
  status: proven
  uses: []
  source: [[collatz-tao-almost-bounded]]
  next: a.a. (log-density) $\mathrm{Col}_{\min}<f(N)$ for any
    $f\to\infty$ — the apex of the density line; $f$ to a constant is
    "likely almost as hard as the full conjecture"
- id: collatz-cycle-bounds
  kind: theorem
  status: proven
  uses: []
  source: [[collatz-cycle-bounds]]
  next: no nontrivial $m$-cycles for $m\le91$ (Simons-de Weger 2010;
    Hercher 2023, attempt-07) — per-$m$ finite verification with no
    uniform all-$m$ bound
- id: collatz-conway-undecidability
  kind: theorem
  status: proven
  uses: []
  source: [[collatz-conway-undecidability]]
  next: generalized Collatz maps are undecidable ($\Pi^0_2$-complete,
    Kurtz-Simon 2007) — NO uniform all-$T$ argument exists, so a
    3n+1 proof must exploit the concrete contracting structure
    (per-instance control); 3n+1 itself NOT proven undecidable
- id: average-vs-pointwise-control
  kind: method
  status: open
  uses: [collatz-density-results, collatz-tao-almost-bounded, collatz-map]
  source: [[average-vs-pointwise-control]]
  next: the unifying lens — average contraction ($3/4<1$,
    $\mathbb E[k]=2>\log_2 3$) is distributional over parity
    sequences; a density-1 result cannot exclude a measure-zero
    exceptional set
- id: cycle-exclusion-linear-forms
  kind: method
  status: open
  uses: [collatz-cycle-bounds]
  source: [[cycle-exclusion-linear-forms]]
  next: a cycle forces $\Lambda=(K+L)\log2-K\log3$ exponentially
    small; transcendence lower bounds rule out $m\le91$ and degrade
    for large $m$ — the literal Beal-flavored transcendence wall