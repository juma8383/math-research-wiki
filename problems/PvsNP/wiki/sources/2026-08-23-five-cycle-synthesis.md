---
title: "Cycle 5 — Five-cycle synthesis: the frontier is one wall, blocked by an open construction (not a proven impossibility)"
date: 2026-08-23
cycle: 5
tags: [witness-needs-explicit-lb, five-cycle-synthesis, honest-ceiling, n2-wall, mining-program, route-a-compression-crux, route-a-variant-gap, s2-irritable-witness-obstruction, s1a-antiprox-obstruction, s3-locality-escapes-witness-barrier-does-not, mining-gap-two-dimensional, non-amplification-also-class-drifts, threshold-aggregation-obstruction, avg-worst-2x2-cell, resopl-obstruction]
---

# Cycle 5 — Five-cycle synthesis

This is the final cycle of the user's "continue the next best options on loop for 5 cycles" mandate. Cycles 1–4 were adaptive research pushes; this cycle is (a) a final adaptive consideration of whether any *untried* lever remains, and (b) a synthesis of all five cycles into an honest assessment of where the genuine P-vs-NP-adjacent frontier now sits. `[honest-ceiling]` is upheld throughout: no breakthrough is claimed; the product is a precise map and a falsifiable statement of the wall.

## The five cycles, compressed

| Cycle | Route | Angle on the wall | Outcome |
|------|-------|-------------------|---------|
| (pre-loop) S1.a | meta-complexity Route A | derandomize Ilango's (AC⁰_d)-MCSP reduction | `[s1a-antiprox-obstruction]`: the sole randomness is the Lupanov sampling of g; derandomizing the lower-bound half is a fine-grained **DNF** lower bound for an explicit function in a tight window = circuit-LB-hard. |
| (pre-loop) S2 | meta-complexity Route A | uniformize MOCSP's non-uniform AC⁰ reduction | `[s2-irritable-witness-obstruction]`: non-uniformity hardwires an (rn)-irritable T; uniformizing needs an explicit **exponential (in L) general-circuit** lower bound (best explicit Θ(L), linear — exponentially short). |
| 1 (S3) | meta-complexity Route A | port CHOPRS Thm 49's non-localizable LB | `[s3-locality-escapes-witness-barrier-does-not]`: escaping the locality barrier ≠ escaping the witness barrier; needs an explicit **exponential (in m) formula** LB (best explicit Ω̃(m³) cubic). Barrier orthogonality `[locality-vs-witness-orthogonal]`. |
| 2 | Williams mining | CSS16/Tell wire frontier | `[mining-gap-two-dimensional]`: the gap is correlation-strength × wire-regime; both known average-case data points fall short on both axes; MAJ∘MAJ (HMPT worst-case anchor) is the only viable target. |
| 3 | Williams mining | non-amplification average-case route | `[non-amplification-also-class-drifts]`: CLOSED — bypassing the IW XOR-lemma does not bypass the class drift; the drift lives in the reconstruction's *decoder*, present in both amplified and amplification-free pipelines. |
| 4 | Williams mining | aggregation crux | `[threshold-aggregation-obstruction]` `[avg-worst-2x2-cell]`: the obstruction is one level *below* the decoder, at the amplification/aggregation step — the top threshold is a nonlinear aggregator (boosting); the mining target is the uncovered fourth cell of the (avg/worst)×(C/MAJ∘C) grid. |

**The unifying diagnosis `[witness-needs-explicit-lb]`** is now confirmed from **seven angles** spanning **both** live P≠NP-adjacent routes (meta-complexity Route A: S1.a/S2/S3; Williams mining: Cycle 2/3/4) and **three circuit models** (DNF, general circuit, formula) plus the depth-2 threshold average-case world. Every angle converges on the same statement:

> *Both live P≠NP-adjacent routes require, at their core, an explicitly constructed **lower-bound-carrying / average-case-hard witness for a restricted circuit class**. A cheap probabilistic/existential input (non-uniform advice, random T, exhaustive-search f_hard, worst-case LB) supplies it only insufficiently, and the explicit construction IS the circuit-lower-bound problem (the natural-proofs frontier).*

## Untried-lever analysis (the final adaptive consideration)

Honest question: *given every tested lever hits the same wall, is there an untried lever that is NOT itself the breakthrough?* Enumerated:

1. **Direct worst-case→CAPP without average-case (a non-NW / SAT-style derandomization).** This is the Williams *worst-case SAT* route. It is blocked by the `[n2-wall]` — Alman-Williams' Θ√t threshold approximate degree, a **proven theorem about the class** (forces ≥2ⁿ monomials at n² wires). Not the witness wall; a *different, proven* wall.
2. **A majority-closed subclass of MAJ∘MAJ** (so black-box amplification works). Nearly contradictory: a majority of any depth-2 class adds a layer (depth-3); depth-1 C is *not* closed under majority — which is exactly Cycle 4's obstruction. Same wall.
3. **A function other than IP₂ with a known exponential average-case-correlation LB against full-poly-size MAJ∘MAJ.** This *is* the open problem (the genuine-open shape). No known candidate exists. Same wall.
4. **A structurally-different uniform-AC⁰ MCSP reduction** (not a port of S1.a/S2/S3). The compression crux `[route-a-compression-crux]`: such a reduction must encode n-bit SAT-satisfiability into the circuit complexity of a function on O(log n) bits, which is ≥ as hard as NP ⊄ P/poly — the reduction itself *is* the breakthrough. No concrete candidate. Same wall (meta-complexity side).
5. **Res(⊕) size-rank conversion** (proof complexity). Genuinely *different* (NP≠coNP-adjacent, not a circuit LB), untested by the loop, and the portfolio's "near-term/safe" bet. But it is a *different problem* with lower P≠NP-specific upside; the obstruction `[resopl-obstruction]` (rank LB exists, only size-rank conversion missing) is a separate wall.

**Conclusion: across the two live P≠NP-adjacent routes, every remaining lever either hits the same `[witness-needs-explicit-lb]` wall or *is itself* the breakthrough (no concrete candidate exists).** The wall is total across the two routes. The one genuinely different untried lever (Res(⊕)) lives on a separate problem with its own separate wall.

## The asymmetry that matters: proven wall vs. open wall

The synthesis surfaces a diagnostically important asymmetry between the two Williams-side sub-routes:

- **Worst-case SAT route:** blocked by the `[n2-wall]` — a **proven theorem** (Alman-Williams Θ√t approximate degree). Cannot fall without a fundamentally different algorithmic representation; the ACC⁰ trick is provably the wrong tool past n² wires.
- **Average-case CAPP route (mining):** blocked by `[witness-needs-explicit-lb]` — an **open construction problem** (an explicit exponential average-case-correlation LB for a restricted class). Not a proven impossibility; it is the natural-proofs frontier, which is *conditional* (on one-way functions) and not an unconditional barrier.

**This makes the average-case/mining route the genuinely more-promising Williams-side sub-route:** it is blocked by an *open problem*, not a *theorem*. A single explicit construction (an average-case-hard function for one restricted class, in a derandomization-usable form) would fall the wall. The worst-case route cannot fall the same way (its wall is proven). This is consistent with — and sharpens — the survey's framing of the mining program as the "constructive path": constructive *because* its obstruction is an open construction rather than a proven impossibility.

## Honest assessment: where the genuine frontier now sits

1. **The frontier is one wall, on two routes.** `[witness-needs-explicit-lb]` governs both the meta-complexity Route A (uniformize an AC⁰ MCSP reduction) and the Williams mining program (convert a worst-case LB into an average-case derandomization). Seven angles, three circuit models, both routes — one obstruction.
2. **The wall is an OPEN problem, not a proven impossibility.** Explicit exponential (in L=O(log n)) lower bounds for functions on O(log n) bits are *open* (best explicit is polynomial — linear-general, cubic-formula; the exponential target 2^{Θ(L)} is exponentially far). The natural-proofs barrier that lurks behind it is *conditional* (on one-way functions). So the frontier is **genuinely alive** — just at the hardest known point — not closed by a theorem.
3. **The actionable conclusion.** Because both routes fail at the *same* wall from opposite sides, **a single idea producing an explicit average-case / lower-bound-carrying witness for ANY ONE restricted class (in a derandomization-usable form) advances BOTH routes.** The two near-term *relaxations* that lower (not meet) the witness requirement remain the tractable seams: (meta-complexity) a structurally-different uniform-AC⁰ reduction; (Williams) Tell's *promise*/wire-count derandomization = the CSS16 wire frontier.
4. **Near-term vs. P≠NP.** Honest scope unchanged from the survey: near-term de-conditioning (Hirahara-Ilango 2025) yields **EXP≠ZPP-class**, not P≠NP. P≠NP via Route A still needs the full uniform-AC⁰ many-one NP-hardness (the compression crux); P≠NP-adjacent via Williams needs the full-poly-size exponential average-case-correlation LB. Both are at the wall. A genuine breakthrough requires crossing the wall — an explicit restricted-class witness of the magnitude no known technique achieves.
5. **The deliverable is a map, not a theorem.** Per `[honest-ceiling]`: no P≠NP proof, no new circuit lower bound, no derandomization was produced. The compounding product is a precise, falsifiable map of the frontier — seven angles on one wall, the wall's mechanism identified (threshold nonlinearity / aggregation; the existential-witness pattern), the wall's *status* honestly classified (open construction, not proven impossibility), and the two routes unified so that a single success propagates.

## Honest scope `[honest-ceiling]`
- **No breakthrough.** The 5-cycle loop did not produce, or come close to, a P≠NP proof or a new super-polynomial circuit lower bound. Each cycle verified its obstruction against primary sources, tested its own suggested openings (Cycle 3 closed the second pass's non-amplification shape; Cycle 4 closed a contradiction-flagged opening), and recorded sharpened negatives. This is the contract: report outcomes faithfully; do not fabricate.
- **The wall's "totality" is a survey-level claim.** "Every remaining lever hits the wall or is the breakthrough" is an enumeration of *known/considered* levers, not an exhaustive impossibility proof. A genuinely novel idea outside the enumerated space could exist — that is what "open" means.
- **Unverified/flagged.** The proven-vs-open asymmetry (n²-wall = theorem; witness wall = open) is a *classification* of two known obstructions, not a new result. The "single success propagates to both routes" claim is the logical content of the unification (both routes need the same witness), not a constructed bridge.

## Sources (the 5-cycle loop + the pre-loop anchors)
- sources/2026-08-21-s1a-primary-source.md (S1.a — DNF model)
- sources/2026-08-21-s2-primary-source.md (S2 — general-circuit model; established `[witness-needs-explicit-lb]`)
- sources/2026-08-21-mining-program-seam.md (Williams mining framework + first/second pass)
- sources/2026-08-23-s3-choprs-thm49.md (Cycle 1 — formula model; barrier orthogonality)
- sources/2026-08-23-wire-frontier-push.md (Cycle 2 — two-dimensional gap)
- sources/2026-08-23-nonamplification-route.md (Cycle 3 — decoder-level drift, closed)
- sources/2026-08-23-aggregation-crux.md (Cycle 4 — amplification/aggregation level, the mechanism)
- pages/status-map.md (the portfolio: near-term Res(⊕), medium-term mining, long-term Route A)
- pages/novel-diagnoses.md (§7–§11, the diagnoses)
- pages/open-problems.md (the tracked targets)
- pages/williams-algorithmic.md · pages/mcsp-meta-complexity.md (the two route pages)