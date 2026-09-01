---
title: Disjoint NP pairs (and the proof-complexity bridge)
category: concept
tags: [disjoint-pairs-stronger-not-easier, disjoint-pairs-relativize, disjoint-pairs-re-collapse-to-inseparable-pair, disjoint-pairs-inherit-rsc, disjoint-pairs-bridge-to-proof-complexity, proof-complexity-face-barriered, witness-needs-explicit-lb, measure-relativization-barrier, rsc-martingale-naturalproof-equivalence, measure-pivot-rediscovers-natural-proofs, point-to-set-principle, disjoint-pairs-characterization, no-missed-connection-moved-wall, three-barriers-required, honest-ceiling, sixth-loop-cycle-4]
status: open (re-collapses to natural proofs; bridges to proof complexity)
last_touched: 2026-08-23
---

# Disjoint NP pairs (and the proof-complexity bridge)

Mapped in Cycle 24 (sixth-loop C4) as the **barrier profile** of the one genuinely new target surfaced by the Cycle-23 measure pivot — the 2022 Lutz-Lutz-Mayordomo disjoint-pairs characterization `dim(disjNP | disjEXP) = 1 ⟹ dim(NP | EXP) > 0 ⟹ P ≠ NP`. This page records that profile and, in doing so, identifies disjoint NP pairs as the **bridge node** connecting the resource-bounded-measure surface ([[resource-bounded-measure]]) to the propositional-proof-complexity surface.

## The object

A **disjoint NP pair** is a pair (A, B) of NP languages with A ∩ B = ∅. `disjNP` is the class of all such pairs (coded over {0,1,−1}); `disjEXP` the disjoint EXP pairs. A pair is **P-separable** if some P language C has A ⊆ C and B ∩ C = ∅; otherwise **P-inseparable**. P-inseparable pairs exist if P ≠ UP (or P ≠ NP∩coNP); P-inseparable pairs are necessary for secure public-key cryptography (Glaßer-Selman-Sengupta-Zhang; Fortnow-Rogers). The Fortnow-Lutz-Mayordomo measure theorem: μ(NP|EXP) ≠ 0 ⟹ for every k there exist **TIME(2^{n^k})-inseparable** disjoint NP pairs.

## The barrier profile (Cycle 24)

- **Stronger, not easier** `[disjoint-pairs-stronger-not-easier]`: `dim(disjNP|disjEXP)=1` *implies* `dim(NP|EXP)>0` (Thm 6.1, Lutz-Lutz-Mayordomo 2022), so the disjoint-pairs condition is **stronger** than the direct dimension hypothesis it delivers — a harder-to-prove sufficient condition, not a shortcut. The Cycle-23 "falsifiable target" is refined: the only candidate leverage is the *different combinatorial shape* (pairs + separability), and the items below show it yields none.
- **Relativization: blocked** `[disjoint-pairs-relativize]`: oracles exist on both sides — Fortnow-Rogers 2002 settle all relativized separability relationships with generic oracles; Glaßer et al. oracle O₂ (complete pairs exist, optimal proof systems do not — Razborov's converse fails relativizably); Fortnow-Lutz-Mayordomo 2009 oracle separations. Inherits `[measure-relativization-barrier]` / `[three-barriers-required]` on the relativization axis.
- **Re-collapse to an inseparable-pair witness** `[disjoint-pairs-re-collapse-to-inseparable-pair]`: full dimension of disjNP = disjNP pseudorandom/dense relative to disjEXP = no efficient gale succeeds against it ⟹ (via RSC `[rsc-martingale-naturalproof-equivalence]`) exhibiting a hard object, namely a **P-inseparable disjoint NP pair** — a *differently-shaped* witness (a pair + separator-resistance), not the single balanced-point function (A). Re-collapses to the same lock `[witness-needs-explicit-lb]`; the construction is no less open for the different shape.
- **Natural proofs: inherited** `[disjoint-pairs-inherit-rsc]`: the dimension statement is density/pseudorandomness; by RSC it re-encounters natural proofs exactly as the parent measure hypothesis did `[measure-pivot-rediscovers-natural-proofs]`. Does not escape the natural-proofs axis.

## The proof-complexity bridge `[disjoint-pairs-bridge-to-proof-complexity]`

Razborov 1994: every propositional proof system f has a **canonical disjoint NP pair** `(SAT*, REF_f)`, and if f is **optimal** then `(SAT*, REF_f)` is ≤_m^pp-**complete** for DisjNP. Glaßer-Selman-Zhang (Thm 3.1): **every** disjoint NP pair is many-one equivalent to the canonical pair of *some* proof system → DisjNP and the canonical-pair degrees have **identical degree structure**. So the disjoint-pairs question and the propositional-proof-system question are **equivalent in degree structure**.

This makes disjoint NP pairs the **bridge** between the measure surface and the proof-complexity surface. Consequence for the pivot map: "pivot to proof complexity" (one of the four original pivot options) is **not a fresh surface** — it is the far end of a bridge whose near end this page maps. The genuinely-untouched pivot surfaces after Cycle 24 are **descriptive complexity** and (already partially mapped) **GCT/algebraic**.

## The far end is barriered too `[proof-complexity-face-barriered]`

- Complete disjoint NP pairs ⟺ DisjNP **uniformly enumerable** (Glaßer-Selman-Sengupta Thm 6.5) — judged **highly unlikely** (a total computable listing of *exactly* all disjoint NP pairs).
- Optimal proof systems: oracles both ways (O₁ yes, O₂ no) → relativization-blocked; existence ⟹ ≤_m-complete sets for NP∩SPARSE (Meßner-Torán), which fails relative to O₂.
- Known proof-complexity lower bounds exist only for **weak** systems (resolution, cutting planes, bounded-depth Frege); the relevant strength (Frege / Extended Frege / optimal systems) is **open**.
- **Unmapped gap:** whether the proof-complexity face meets a natural-proofs-style barrier (in the proof-complexity sense) is NOT web-verified here — the one remaining unmapped piece of the bridge.

## Status

Open. The disjoint-pairs target does not escape the wall on any of the three barrier axes; it re-confirms `[no-missed-connection-moved-wall]` from a third sub-surface (structural face → measure face → disjoint-pairs/proof-complexity bridge) and narrows the pivot space. NO BREAKTHROUGH; `[honest-ceiling]` upheld. See [[resource-bounded-measure]] (parent surface), [[barriers]] (the measure facet + relativization), [[status-map]], [[novel-diagnoses]] (Diagnosis 34), [[open-problems]].