---
title: Proof complexity (Res(⊕) & NP vs coNP)
category: angle
tags: [egi-2024, resopl-obstruction, tell-2018]
status: dead-for-feedback-near-reachable-on-frontier
last_touched: 2026-08-21
---

# Proof Complexity

## Feedback to P vs NP is closed
A single-system proof-complexity lower bound yields NP≠coNP (⟹ P≠NP) **only if** the system is p-optimal (p-simulates all propositional proof systems). **No natural system** (Frege, Extended Frege, IPS) is known to be even conditionally p-optimal. The only existing optimal pps (Cook-Krajíček, with O(1) advice) is diagonalization-constructed and intractable as an LB target; it yields only PH-non-collapse, not P≠NP. The one genuine proof-complexity→complexity reduction (Grochow-Pitassi: IPS LB ⟹ VNP≠VP) lands on an **algebraic** separation that does not imply P≠NP. All three barriers hit on different sub-routes. **Dead for feedback to P vs NP under current knowledge.**

## The near-reachable frontier: unrestricted Res(⊕) SIZE lower bound
`[egi-2024]` already proved an Ω(n) rank/width LB for unrestricted dag-like Res(⊕) on BPHP. The missing piece is purely a Ben-Sasson-Wigderson-style **size-rank conversion**.

## The diagnosed obstruction `[resopl-obstruction]`
Parity inferences defeat restriction-based width reduction. Under a random restriction, a resolution clause's width shrinks, but a Res(⊕) line (a disjunction of affine F₂-equations) can **re-expand rank** in one step: a low-rank clause derives a high-rank clause because F₂-linear combinations generate affine equations of arbitrary rank over surviving variables. So **rank is not monotonically controlled by size** in Res(⊕); the BS-W key lemma "small size ⟹ low-width refutation" fails. No width invariant is known that is both restriction-monotone AND BPHP-lower-bounded.

## Value
A Res(⊕) size LB would be the first super-poly LB for any proof-system fragment beyond constant-depth Frege, the direct stepping stone to the 30-year-open AC⁰[2]-Frege problem, and would likely introduce a new width invariant reusable across AC⁰[2]-Frege. **A proof-system separation, not a circuit lower bound** — important but not P vs NP.

## See also
[[meta-duality]] · [[open-problems]] · [[status-map]]