---
type: dag
problem: birch-swinnerton-dyer
last-updated: 2026-09-09
---

# Proof DAG — birch-swinnerton-dyer

Live frontier: rank part open for $r_{\text{an}}\ge2$ + refined
leading-coefficient open; the obstruction is the Selmer-group control
step at rank $\ge2$ — the rank-2 Kolyvagin-system composition
(attempt-08/09: the two-fold conditional = Darmon-derivative Conj 1.9
+ Bockstein regulator $\neq0$; attempt-12: all residual weight sits
on the supply half).

- id: bsd-itself
  kind: conjecture
  status: open
  uses: [elliptic-curve-l-function, mordell-weil, modularity, bfh-murty-nonvanishing, kolyvagin-gross-zagier, parity, heegner-point-euler-system, kolyvagin-rank2-conjectures, darmon-derivative-conjecture, bockstein-regulator-nonvanishing, point-supply-reduction]
  source: [[birch_swinnerton_dyer]]
  next: rank $\le1$ base proven; the named control target is the
    two-fold conditional (Darmon-derivative Conj 1.9 + $R^{Boc}\neq0$,
    attempt-08/09) — dispatch targets when the harness goes live
- id: elliptic-curve-l-function
  kind: definition
  status: open
  uses: [modularity]
  source: [[elliptic-curve-L-function]]
  next: —
- id: mordell-weil
  kind: theorem
  status: proven
  uses: []
  source: [[mordell-weil]]
  next: descent/Selmer bounds the rank above in all ranks (resolution
    layer) — supplies no effective upper bound
- id: modularity
  kind: theorem
  status: proven
  uses: []
  source: [[modularity]]
  next: —
- id: bfh-murty-nonvanishing
  kind: theorem
  status: proven
  uses: []
  source: [[bfh-murty-nonvanishing]]
  next: —
- id: kolyvagin-gross-zagier
  kind: theorem
  status: proven
  uses: [modularity, bfh-murty-nonvanishing]
  source: [[kolyvagin-gross-zagier]]
  next: —
- id: parity
  kind: theorem
  status: proven
  uses: []
  source: [[parity]]
  next: p-parity unconditional (Dokchitser-Dokchitser); the algebraic
    rank-parity corollary is conditional on Sha_{2,3}-finiteness, and
    converting parity to exact rank still needs an upper bound of the
    right parity — the missing Euler-system step
- id: heegner-point-euler-system
  kind: method
  status: open
  uses: [kolyvagin-gross-zagier]
  source: [[heegner-point-euler-system]]
  next: the one-point shape bounds a rank-$\le1$ Selmer group only —
    the shape limit IS the rank-$\ge2$ obstruction
- id: kolyvagin-rank2-conjectures
  kind: conjecture
  status: open
  uses: [heegner-point-euler-system]
  source: problems/birch-swinnerton-dyer/attempts/attempt-01.md
  next: Kolyvagin Conjectures 3.32-3.35 (a rank-$\ge2$-shaped Euler
    system bounding the full Selmer group) — the named unproven
    control target [bsd-kolyvagin-conj]
- id: darmon-derivative-conjecture
  kind: conjecture
  status: open
  uses: [heegner-point-euler-system]
  source: problems/birch-swinnerton-dyer/attempts/attempt-08.md
  next: Kataoka-Sano Conj 1.9 (Darmon-derivative explicit formula) —
    first of the two remaining conditions; primary-source confirmed
    attempt-08
- id: bockstein-regulator-nonvanishing
  kind: conjecture
  status: open
  uses: [heegner-point-euler-system]
  source: problems/birch-swinnerton-dyer/attempts/attempt-08.md
  next: $R^{Boc}_{K_\infty}\neq0$ — second of the two remaining
    conditions; the derived regulator degeneracy is why the gap is a
    derived control step (Sano 2023, attempt-10/11)
- id: point-supply-reduction
  kind: conjecture
  status: open
  uses: [heegner-point-euler-system]
  source: problems/birch-swinnerton-dyer/attempts/attempt-12.md
  next: corrected Kim-class reduction — (a) and (b) iff [rank part and
    Sha(E/Q)[p^inf] finite]; the control half is computable at every
    rank, all residual weight on the supply half