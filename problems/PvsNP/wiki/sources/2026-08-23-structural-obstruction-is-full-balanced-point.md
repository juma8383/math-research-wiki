---
cycle: 22
loop: 6
date: 2026-08-23
slug: structural-obstruction-is-full-balanced-point
tags:
  - sixth-loop-cycle-2
  - s1a-class-is-dnf-easy-sat
  - williams-template-convergence-asymmetric
  - structural-obstruction-is-full-balanced-point
  - cycle21-elpnp-lb-under-specified
  - fpnp-escape-not-breakthrough
  - wall-purely-structural-for-fpnp
  - meta-obstruction-fp-specific
  - fpnp-converges-to-williams-template
  - a-is-a-balanced-point
  - a-is-two-balanced-points
  - balanced-point-non-compositional
  - lifting-needs-expensive-and-small-gap
  - expensive-tensions-small-gap
  - tension-is-lupanov-observed-not-proven-inherent
  - apepp-derand-needs-lb
  - a-is-apepp-style-construction
  - nexp-lb-route-naturalproofs-closed
  - mining-redirects-to-s1a
  - s1a-is-the-live-thread
  - two-faces-two-np-variants
  - two-faces-constructivity-axis
  - barrier-ceases-above-conp
  - recognizer-strength-escape-is-open
  - witness-needs-explicit-lb
  - honest-ceiling
  - main-loop
  - no-subagents
provenance: "main loop, no subagents; sixth-loop Cycle 2 — a self-correcting REFINEMENT of Cycle 21 (parallel to the second-loop 13→14→15 and fourth-loop 22→23 self-correction pattern). NO new web search; grounded in the wiki's OWN primary-source-verified S1.a class definition (Ilango FOCS 2020 §1.3, content-lines 340-388 read verbatim in Cycle 9 / Diagnosis 19) and the standing [apepp-derand-needs-lb] (Cycle 18, Korten FOCS 2021). The refinement was forced by re-reading the wiki's §19 to identify WHICH class the Cycle-21 'E^NP LB' is against."
source_grounding: "wiki-internal (no fresh external claims). Load-bearing facts already in the wiki: (1) the S1.a balanced-point class is DNF / depth-d AND_{d−1}/OR_d FORMULAS (Diagnosis 19, Ilango §1.3 verbatim, [lifting-needs-expensive-and-small-gap]); (2) DNF/depth-d-formula SAT is EASY (poly-time) — textbook, no verification needed; (3) parity is expensive-for-DNF (2^{n-1} DNF size) but has a LARGE gap (Diagnosis 19 verbatim, lines 385-387) — so parity is NOT the balanced point; (4) [apepp-derand-needs-lb] (Cycle 18): deterministic FP^NP for EMPTY ⟺ E^NP 2^{Ω(n)} LB (Korten Thm 11). The Cycle-22 conclusion (the structural obstruction is the FULL balanced point, of which the E^NP LB is only the expensive side) follows from (1)+(3)+(4): the E^NP LB / EMPTY derandomization yields a HARD function (expensive), but (A) needs expensive ∧ small-gap, and parity shows expensive-without-small-gap exists — so the LB gives only one side. Flagged: the exact circuit class C of the Korten E^NP LB (general circuits vs DNF/depth-d) is kept at the wiki's prior framing level; the conclusion is robust to that ambiguity because EITHER way the LB yields the expensive/existence side, and the small-gap is the separate Lupanov-structure side."
---

# Cycle 22 — REFINING Cycle 21: the structural obstruction is the FULL balanced point (expensive ∧ small-gap), NOT just "an E^NP LB"; the Williams-template convergence is ASYMMETRIC (DNF SAT is easy); a self-correction that tempers Cycle-21's optimism

## What this cycle does

Cycle 21 ([wall-purely-structural-for-fpnp]) correctly removed the META/FLY obstruction for the FP^NP route, but framed the remaining structural obstruction as "an E^NP LB" ([apepp-derand-needs-lb]) — which could be read as "just need an E^NP circuit lower bound, which Williams-style methods sometimes deliver." This cycle re-reads the wiki's own §19 (the primary-source-verified S1.a class definition) to identify WHICH class that E^NP LB is against, and finds the framing UNDER-specified the structural obstruction in two ways. It is a self-correcting refinement (the wiki's recurring honest pattern — second-loop 13→14→15, fourth-loop 22→23), NOT a breakthrough. It tempers Cycle-21's optimism.

## Finding 1 — the S1.a balanced-point class is DNF / depth-d FORMULAS, and DNF-SAT is EASY `[s1a-class-is-dnf-easy-sat]`

Re-reading Diagnosis 19 (Ilango FOCS 2020 §1.3, content-lines 340-388 read verbatim in Cycle 9): the S1.a balanced-point class is **DNF / depth-d AND_{d−1}/OR_d FORMULAS** — the lifting theorem's witness g must be expensive relative to f AND have a small L^{AND_{d−1}}(g) − L^{OR}_d(g) gap, in the DNF/depth-d-formula model. This is a FORMULA class, NOT the threshold (MAJ∘MAJ/THR∘THR) class of the mining face — confirming the two faces are different classes (not just different axes).

`[s1a-class-is-dnf-easy-sat]`: **DNF and depth-d formula SAT are EASY** — DNF satisfiability is decidable in polynomial time (a DNF is satisfiable iff any term is satisfiable; each term is a conjunction, checkable directly), and depth-d-formula SAT is likewise polynomial. This is textbook and needs no verification. The consequence: **the Williams faster-SAT template — the nontrivial lever for the mining class (ACC/TC⁰, where SAT is hard and a faster-than-2^n algorithm is the breakthrough ingredient) — gives only TRIVIAL/known LBs for the S1.a class** (e.g. parity ⊄ poly-size-DNF, exponential, long-known). Faster-SAT for DNF is not a lever; it is already free.

## Finding 2 — the Williams-template convergence is ASYMMETRIC (partial walk-back of Cycle-21 Finding 6) `[williams-template-convergence-asymmetric]`

Cycle 21's `[fpnp-converges-to-williams-template]` claimed the two faces re-merge at the FP^NP/Williams-template level (FP^NP construction of (A) ⟺ E^NP LB ⟺ faster-SAT/CAPP-for-the-class). Finding 1 refines this: **the template is CLASS-DEPENDENT, and it is productive ONLY where SAT is hard.** For the mining class (ACC/TC⁰/THR, hard SAT), the faster-SAT/CAPP algorithm IS the nontrivial lever (Williams 2011 ACC-SAT; Chen-Tal-Wang XOR-of-two CAPP). For the S1.a class (DNF/depth-d, easy SAT), the template yields only trivial LBs (parity) — it does NOT produce the balanced-point construction. `[williams-template-convergence-asymmetric]`: the two faces do NOT cleanly converge at the *productive* Williams-template level; they converge only at the ABSTRACT "both need an E^NP LB" level. The mining face has a Williams-template lever; the S1.a face does not (its SAT is easy). Cycle-21 Finding 6 over-stated the convergence — walked back.

## Finding 3 — the structural obstruction is the FULL balanced point, of which the E^NP LB is only the expensive side `[structural-obstruction-is-full-balanced-point]` `[cycle21-elpnp-lb-under-specified]`

The core refinement. Cycle 21 framed the FP^NP route's structural obstruction as "an E^NP LB" (via [apepp-derand-needs-lb]: deterministic FP^NP for EMPTY ⟺ E^NP 2^{Ω(n)} LB). But (A) is the **balanced point {expensive ∧ small-gap}** (Diagnosis 19, verbatim), and these two conditions are in TENSION (lines 385-387: as g gets more expensive, the gap gets larger). Parity is the witness to the gap: parity IS expensive for DNF (2^{n-1} DNF size) — so an E^NP LB / EMPTY-derandomization can output a function as hard as parity — BUT parity has a LARGE gap (§19), so parity is NOT the balanced point.

`[structural-obstruction-is-full-balanced-point]`: the E^NP LB equivalence ([apepp-derand-needs-lb]) yields the **expensive / existence** side — a hard function exists and (under derandomization) can be found in FP^NP. But (A) needs expensive **∧** small-gap, and the small-gap is the **Lupanov-structure** side (the near-optimal-CNF structure that simultaneously yields a small gap AND random-like hardness, the Lupanov sweet spot). The E^NP LB does NOT provide the small-gap; it provides only the expensive side. So the structural obstruction for the FP^NP route is the **FULL balanced point (A)** — the non-compositional tension of §19 ([balanced-point-non-compositional]: you cannot solve expensive then small-gap and combine; they must emerge from one structural feature) — of which the E^NP LB is only one side.

`[cycle21-elpnp-lb-under-specified]`: Cycle 21's "wall = an E^NP LB" framing UNDER-specified this. Escaping FLY via FP^NP (Cycle 21, correct) does NOT reduce the wall to "a single E^NP LB that Williams-style methods sometimes deliver" — it reduces it to the **balanced point (A)**, which is the original open construction, with the small-gap (Lupanov structure) as a separate, non-compositional structural requirement that the E^NP LB does not provide. The wall, for the FP^NP route, is: {meta/FLY obstruction REMOVED (Cycle 21)} + {structural obstruction = the full balanced point (A), not reducible to an E^NP LB}. This tempers Cycle-21's optimism — escaping FLY is necessary but does not make (A) a single-LB problem.

This is consistent with the wiki's own [a-is-two-balanced-points] (Cycle 18) and [balanced-point-non-compositional] (Cycle 20): the structural wall was ALWAYS the balanced point (expensive ∧ small-gap, non-compositional). Cycle 21 correctly removed the META level (FLY, FP-specific) but did not — and could not — remove the structural balanced-point tension, because that IS (A). Cycle 22 makes this explicit: the FP^NP route's structural obstruction = (A) = the balanced point, unchanged; only the meta obstruction was removed.

## Honest scope `[honest-ceiling]`

- **NO BREAKTHROUGH.** This is a self-correcting refinement that PREVENTS over-optimism from Cycle 21, not a breakthrough. The wall (for the FP^NP route) = the balanced point (A) with the meta/FLY obstruction removed; the E^NP LB is only the expensive side; the small-gap (Lupanov structure) is the non-compositional hard part, separate. (A) remains an OPEN construction `[a-remains-open-construction]`.
- This is the wiki's recurring honest self-correction pattern (second-loop 13→14→15, fourth-loop 22→23): a prior cycle's clean framing (here Cycle 21's "wall = an E^NP LB") under-specified the obstruction; the honest move is to refine it and walk back the over-strong optimism — exactly `[honest-ceiling]`-driven. Cycle 21 was CORRECT that the FP^NP route escapes FLY (the meta obstruction is removed); it was INCOMPLETE in framing the structural obstruction as "an E^NP LB" rather than the full balanced point. Not "wrong" — incomplete, refined.
- The two faces' relationship is now THREE-part: (a) same unifying obstruction [witness-needs-explicit-lb]; (b) different natural-proofs variants on two axes [two-faces-two-np-variants] (largeness + constructivity-level, the latter added Cycle 21); (c) ASYMMETRIC Williams-template applicability (mining = hard-SAT lever exists; S1.a = easy-SAT, no lever) `[williams-template-convergence-asymmetric]`. The mining face has a productive template route; the S1.a face does not — yet the S1.a face is the one the mining face redirects to ([mining-redirects-to-s1a]), and it is the one whose meta obstruction was just removed (Cycle 21). The honest synthesis: removing the meta obstruction (Cycle 21) does not give the S1.a face a Williams-template lever (Cycle 22); the S1.a face's structural obstruction (the balanced point) has no known productive route, only the open Lupanov-construction.
- All grounding is wiki-internal (no fresh web search, no new external claims). The load-bearing facts (S1.a = DNF/depth-d formulas; DNF-SAT easy; parity expensive-but-large-gap; E^NP-LB-⟺-FP^NP-for-EMPTY) are already in the wiki from prior cycles (Diagnosis 19 verbatim; [apepp-derand-needs-lb]). The refinement is a structural reading of those facts, robust to the summary-level caveat (it does not hinge on a fine-grained external detail).
- (A) remains the single live thread `[s1a-is-the-live-thread]`, an OPEN construction. The wall is genuinely alive at one point — the balanced-point DNF/depth-d construction — now with the meta/FLY obstruction removed (Cycle 21) but the structural balanced-point tension (§19, verbatim, Lupanov-observed-not-proven-inherent) unchanged. Precise ≠ solved.

## Net

SIXTH 5-CYCLE LOOP, Cycle 2 (absolute Cycle 22) complete. A self-correcting REFINEMENT of Cycle 21: the S1.a balanced-point class is DNF/depth-d FORMULAS (§19), whose SAT is EASY — so the Williams faster-SAT template (productive for the mining class, hard SAT) gives only trivial LBs for S1.a (parity) `[s1a-class-is-dnf-easy-sat]`; the Cycle-21 Williams-template convergence is ASYMMETRIC, walked back `[williams-template-convergence-asymmetric]`; and the structural obstruction is the FULL balanced point {expensive ∧ small-gap} (§19, verbatim tension), of which the E^NP LB ([apepp-derand-needs-lb]) is only the EXPENSIVE side — parity is expensive-for-DNF but has a large gap, so the LB does not give the small-gap (Lupanov-structure) side `[structural-obstruction-is-full-balanced-point]` `[cycle21-elpnp-lb-under-specified]`. Cycle 21 correctly removed the META/FLY obstruction for FP^NP but UNDER-specified the structural obstruction as "an E^NP LB" — refined: the FP^NP route's wall is the balanced point (A) with meta removed, NOT reducible to a single (Williams-attainable) E^NP LB. This tempers Cycle-21's optimism (escaping FLY is necessary, not sufficient). NO BREAKTHROUGH; `[honest-ceiling]` upheld — the wiki's recurring self-correction pattern, honestly not a breakthrough. (A) remains an OPEN construction, the single live thread. Wiki state after Cycle 22: 16 pages, 38 sources, all wikilinks resolve.