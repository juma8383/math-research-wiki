---
title: Algorithmic GCT (novel combined angle)
category: synthesis
tags: [williams-2011, coarsening-gap, fixed-degree-escape, fi-2020-asymmetry, bip-2019]
status: conjectural
last_touched: 2026-08-21
---

# Algorithmic GCT

A genuinely novel combined angle synthesizing [[williams-algorithmic]] + [[gct]] + the barrier constraints. **No single angle proposed this; the synthesizer built it.** Research program, not a theorem.

## The idea
Reframe GCT's determinant-boundary bottleneck as an **algorithmic** problem and import Williams' *fast-test + easy-witness* paradigm `[williams-2011]` into the algebraic setting. The analogy:

| Williams (Boolean) | Algorithmic GCT (algebraic) |
|---|---|
| faster-than-brute-force **ACC0-SAT** test | sub-trivial **determinant-hole/multiplicity test** |
| easy-witness lemma | algebraic easy-witness (a hole certificate) |
| ⇒ NEXP ⊄ ACC0 | ⇒ a multiplicity obstruction for perm vs det |

## Concrete program
1. Fix d=2,3 and n=Θ(m²) — the regime where `[bip-2019]`'s m^25 threshold does NOT apply and `[mr-2004]` already works at d=2.
2. The permanent-side plethysm coefficient a_λ(d,n) is **P-time for fixed d** `[fi-2020-asymmetry]` — the tractable side, analogous to the "easy" part of ACC0-SAT evaluation.
3. The determinant-side multiplicity in C[Ω_n]_d is the bottleneck; brute force is infeasible. **Reframe**: seek not a full algorithm, but a **sub-trivial** test — faster than brute-force enumeration of the orbit closure's degree-d piece — exploiting saturation structure (obstructions must be "holes" of S(Det_n)).
4. Build the algebraic easy-witness analog: if the determinant orbit closure at degree d does NOT contain a V_λ the permanent side DOES, a small witness (hole certificate) must exist; if no small witness exists the boundary is large, and a fast hole-test would contradict this — yielding the obstruction.
5. Barrier-compliant by construction: GCT's non-constructivity evades algebraic natural proofs (Forbes-Shpilka-Volk).

## Why it is new
[[gct]] treats the determinant boundary as pure algebraic geometry ("needs new AG results"). [[williams-algorithmic]] treats the fast-test method as Boolean. The synthesis reframes a geometric bottleneck as an algorithmic one and asks whether fast-test + algebraic-easy-witness yields the obstruction — exactly as ACC0-SAT + easy-witness yields NEXP⊄ACC0. The fixed-degree escape makes this the one setting where one side is tractable and the other is the algorithmic frontier, mirroring the Williams setup.

## Risk (honest)
The central conjecture — a sub-trivial determinant-hole test exists at fixed d — is **unverified and may be false**. But falsifying it is itself a theorem (the boundary's largeness), sharpening the GCT negative result. Also: Williams' theorem needs closure-under-composition, which has no known algebraic analog.

## See also
[[williams-algorithmic]] · [[gct]] · [[novel-diagnoses]] · [[open-problems]]