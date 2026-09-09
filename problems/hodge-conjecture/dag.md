---
type: dag
problem: hodge-conjecture
last-updated: 2026-09-09
---

# Proof DAG — hodge-conjecture

Live frontier: codimension-2 Hodge classes on a 4-fold (the smallest
open case); the obstruction is the control step over the
analytic-to-algebraic bridge in codim $\ge2$ — the Picard-variety
engine stops at codim 1 (exponential sequence + GAGA).

- id: hodge-itself
  kind: conjecture
  status: open
  uses: [hodge-class-cycle-map, lefschetz-1-1, hard-lefschetz-reduction, integral-hodge-fails, absolute-hodge-motivated, cattani-deligne-kaplan, standard-conjectures-motives, analytic-algebraic-bridge]
  source: [[hodge_conjecture]]
  next: open leaves — (A) standard-conjectures B/C then motive
    reduction (the Beal-reduction shape; the target itself is open
    special cases of HC, Deligne hodge.pdf section 4), (B) codim-2
    directly via the intermediate Jacobian (attempt-02), (C) abelian
    structured sub-cases
- id: hodge-class-cycle-map
  kind: definition
  status: open
  uses: []
  source: [[hodge-class-cycle-map]]
  next: surjectivity of cl rationally in codim $\ge2$ IS the open
    content
- id: lefschetz-1-1
  kind: theorem
  status: proven
  uses: []
  source: [[lefschetz-1-1]]
  next: —
- id: hard-lefschetz-reduction
  kind: theorem
  status: proven
  uses: []
  source: [[hard-lefschetz-reduction]]
  next: reduces HC in degree $2p$ to $2(n-p)$; only middle codims
    $2\le p\le n-2$ ($n\ge4$) are the frontier
- id: integral-hodge-fails
  kind: theorem
  status: proven
  uses: []
  source: [[integral-hodge-fails]]
  next: integral HC fails in codim $\ge2$ (Atiyah-Hirzebruch torsion
    via AHSS; Kollar non-torsion hypersurfaces) — the Q-retreat
    removes both obstructions, leaving rational codim-$\ge2$ control
    as the sole open piece
- id: absolute-hodge-motivated
  kind: theorem
  status: proven
  uses: []
  source: [[absolute-hodge-motivated]]
  next: all Hodge classes on abelian varieties are absolute Hodge
    (Deligne) — the strongest evidence layer; Andre's motivated
    cycles are the Tannakian controlled-evidence category
- id: cattani-deligne-kaplan
  kind: theorem
  status: proven
  uses: []
  source: [[cattani-deligne-kaplan]]
  next: Hodge locus algebraic (JAMS 8(2) 1995, unconditional) —
    Hodge classes behave "as if" algebraic at the locus level;
    controls the locus, does not produce the cycles
- id: standard-conjectures-motives
  kind: theorem
  status: conditional
  uses: []
  source: [[standard-conjectures-motives]]
  next: given B (inverse Lefschetz) and C (Kunneth components), HC
    iff a fully-faithful motives-to-Hodge-structures functor (Deligne
    section 5) — CONDITIONAL on B and C, which are open special
    cases of HC itself (Deligne section 4); proven for surfaces,
    abelian varieties, hyper-Kahler $K3^{[n]}$ (Charles-Markman,
    attempt-03)
- id: analytic-algebraic-bridge
  kind: method
  status: open
  uses: [lefschetz-1-1, hodge-class-cycle-map]
  source: [[analytic-algebraic-bridge]]
  next: the unifying lens — the bridge works for divisors
    (exponential sequence + GAGA + Picard variety); for codim $\ge2$
    the Griffiths intermediate Jacobian is transcendental and does
    not control algebraicity — the one-codimension engine stops