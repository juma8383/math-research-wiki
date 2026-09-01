---
cycle: 19
loop: 5
date: 2026-08-23
slug: determinism-is-recognizability
tags:
  - fifth-loop-cycle-4
  - constructible-implies-recognizable
  - derandomization-destroys-nonrecognizability
  - recognizer-strength-no-escape
  - noncompositionality-mechanistic-asymmetric
  - a-is-two-balanced-points
  - balanced-point-non-compositional
  - a-is-apepp-style-construction
  - korten-apepp-hard-truth-table
  - apepp-derand-needs-lb
  - gate-1-automatic
  - naturalization-open-question
  - s1a-is-the-live-thread
  - a-is-a-balanced-point
  - recognizable-stronger-than-natural
  - fly-needs-no-largeness
  - rr-and-fly-partition-by-largeness
  - cwy-2023-blackbox
  - witness-needs-explicit-lb
  - honest-ceiling
  - main-loop
  - no-subagents
provenance: "main loop, no subagents (HTTP 429 usage limit persists); the mechanism (recompute-and-compare recognizability) is textbook Razborov-Rudich constructivity — no web search needed; the recognizer-strength point is a flagged reading (my own inference, NOT web-verified), stated with honest scope"
source_grounding: "the load-bearing mechanism (a deterministic construction A makes its output (P/poly)-recognizable via recompute-and-compare, poly in the truth-table length) is basic RR constructivity (Razborov-Rudich 1997) — KNOWN, not newly discovered; the wiki's contribution is the two-level ASYMMETRY (meta-tight theorem vs structural heuristic) and the identification that derandomization mechanistically DESTROYS non-recognizability. NO fresh primary-source reading, NO new web search (search budget conserved given the 429 limit; the mechanism is textbook and does not require verification). Search/arXiv-summary-level prior findings (Korten FOCS 2021, CWY ITCS 2023, Fan-Li-Yang STOC 2022, Ilango FOCS 2020) re-cited, NOT PDF-line-verified."
---

# Cycle 19 — the within-connection push: DETERMINISM IS RECOGNIZABILITY — the meta-level non-compositionality is a theorem (RR constructivity, via recompute-and-compare); derandomization mechanistically DESTROYS non-recognizability; the two-level balanced point is asymmetric (meta-tight / structural-heuristic); the wall deepens mechanistically, does not move

## What this cycle does

The Cycle-18 LINT's "Next (Cycle 19)" directive: take the two-level balanced-point characterization of (A) `[a-is-two-balanced-points]` to a concrete falsifiable target — is there a KNOWN construction (even non-uniform / oracle / randomized-with-structure) that satisfies ONE of the two meta-level conditions (deterministically-CONSTRUCTIBLE OR non-RECOGNIZABLE) at the balanced point, or does any satisfaction of one break the other (the non-compositionality `[balanced-point-non-compositional]`)?

This cycle answers it, NEGATIVELY, and in doing so makes the meta-level non-compositionality MECHANISTIC. The key observation is elementary but had not been made explicit in the wiki: **a deterministic construction of g IS, mechanically, a (P/poly)-recognizer of g's truth table** — via recompute-and-compare. This is the textbook content of Razborov-Rudich's *constructivity* condition. The wiki had the *consequence* (Gate 1 automatic for deterministic reductions, `[gate-1-automatic]`, Cycle 7) but not the *mechanism* spelled out. Making it explicit resolves the falsifiable target and reveals that the two levels of the balanced point have DIFFERENT epistemic status — one is a theorem, the other a heuristic.

## Finding 1 — the MECHANISM: a deterministic construction IS a (P/poly)-recognizer (recompute-and-compare) — the textbook RR constructivity condition `[constructible-implies-recognizable]`

Let A be a deterministic polynomial-time algorithm computing g on n-bit inputs, and let T be g's truth table (length N = 2^n). There is a circuit of size poly(N) that, given T, recognizes "is T the output of A?": **recompute A on all n-bit inputs (2^n · poly(n) = poly(2^n) = poly(N)) and compare the result to T.** So "is the output of A" is in P/poly — a (P/poly)-recognizable property of the truth table.

This is the literal content of Razborov-Rudich's *constructivity* condition (a natural property must be P/poly-computable given the truth table). The wiki's Cycle-7 finding `[gate-1-automatic]` ("any reduction that SUCCEEDS automatically uses a non-recognizable collection; Gate 1 is a *consequence* of success") is the *consequence*; **recompute-and-compare is the *mechanism*** — the reason a successful *deterministic* reduction yields a recognizable property is precisely that the construction's algorithm IS a poly(N)-recognizer.

Consequences, made explicit:
- **A deterministic construction of a balanced-point g makes g (P/poly)-recognizable** (as "the output of A"). If A succeeds, that property is also *useful* (it picks out a balanced-point = hard-for-C function). And it is *non-large* (one function per length) ⟹ it is a **FLY property** (recognizable + useful + sound-on-random; per the Cycle-14 `[rr-and-fly-partition-by-largeness]` partition: large → RR, non-large → FLY, `[fly-needs-no-largeness]`). So a *successful* deterministic (A)-construction yields a FLY property breaking PRFs at the threshold ⟹ (assuming PRFs) no such construction exists.
- **This is the natural-proofs barrier, mechanized** — NOT a new impossibility. It is conditional on PRFs, and it is about the *deterministic-constructible* route (the construction being P/poly-computable), NOT about the truth of P≠NP or about non-constructive LBs. It is exactly the wiki's existing Gate-1 framing, now with the mechanism identified. `[honest-ceiling]`: stated as "the deterministic-explicit route is natural-proofs-blocked (assuming PRFs), mechanism = recompute-recognizability" — NOT as "(A) is impossible" (it is not; (A) remains an open construction; a non-deterministic construction escapes, see Finding 2).

## Finding 2 — derandomization mechanistically DESTROYS non-recognizability: the randomness of the Lupanov sampler IS its non-recognizability `[derandomization-destroys-nonrecognizability]`

The sharpest consequence of Finding 1 connects two prior wiki findings that had been stated separately:

- The Lupanov sampler is **BPP / randomized**. Its output g is **non-recognizable**: given a random sample's truth table, you CANNOT recompute it (the sample depends on random coins you no longer have). The randomness is precisely what defeats recompute-and-compare. So the Lupanov sampler's construction is **non-recognizable** ⟹ natural-proofs-UNBLOCKED (it does not yield a recognizable useful property). This is the wiki's existing "Gate 1 soft" / `[naturalization-open-question]` state.
- **But derandomizing the sampler (making it deterministic FP^NP, per Cycle-18 `[apepp-derand-needs-lb]`) DESTROYS this non-recognizability**: a deterministic sampler IS recompute-recognizable (Finding 1). So derandomizing the Lupanov sampler lands it squarely in FLY (recognizable + useful + non-large) ⟹ natural-proofs-BLOCKED (assuming PRFs).

So the two meta-level requirements on (A) from Cycle 18 — (a) **deterministically-constructible** (derandomize the sampler) and (b) **non-recognizable** (escape natural proofs) — are not merely "in tension" (the Cycle-18 heuristic framing: "you built it so you can describe it; non-recognizable ⟹ looks random"). They are **mechanistically incompatible**: determinizing the sampler makes it recompute-recognizable = FLY-blocked; keeping it randomized keeps it non-recognizable = unblocked but NOT explicit/usable. The randomness of the sampler is not a bug to be derandomized away — **it is the SOURCE of the non-recognizability that keeps the construction natural-proofs-unblocked.** Remove the randomness (derandomize) and you remove the non-recognizability (recompute-recognizable) simultaneously.

This is the meta-level non-compositionality `[balanced-point-non-compositional]` made fully mechanistic: you cannot separately "construct deterministically" and "hide recognizability," because constructing deterministically IS revealing (recompute-recognizable). The two requirements are satisfied by DIFFERENT kinds of construction (deterministic ⟹ recognizable; randomized ⟹ non-recognizable), and no single construction satisfies both — the derandomization and the non-recognizability are on opposite sides of the recompute-recognizability mechanism.

This CONNECTS `[apepp-derand-needs-lb]` (derandomizing (A) needs an E^NP LB) with `[gate-1-automatic]` (Gate 1 automatic for deterministic reductions) with `[a-is-two-balanced-points]` (the two meta conditions) via ONE mechanism (recompute-recognizability): the E^NP LB that derandomization needs is not merely hard to get — even IF you got it, the resulting deterministic construction would be recompute-recognizable = FLY-blocked. So derandomizing (A) faces the natural-proofs barrier from BOTH sides: the LB is hard to prove (E^NP LB) AND the proof would, if found, make the construction recognizable (FLY). This is the sharpest mechanistic form of `[witness-needs-explicit-lb]` reached across five loops.

## Finding 3 — the recognizer-strength escape does NOT work `[recognizer-strength-no-escape]`

The natural escape attempt against Finding 2: construct (A) in FP^NP (deterministic *with an NP oracle*) rather than P. Then g is P^NP/poly-recognizable (recompute A with the NP oracle), NOT P/poly-recognizable. The Ilango / RR barrier is stated for (P/poly)-recognizability. Does the stronger recognizer (P^NP/poly) escape the P/poly barrier?

**No.** A stronger recognizer is a *stronger* distinguisher — a P^NP/poly-natural property would break PRFs secure against P^NP/poly. The natural-proofs barrier is robust to recognizer strength: making the recognizer more powerful makes the property *more* of a PRG-breaker, not less, so the barrier is *at least as strong* at P^NP/poly as at P/poly. And cryptographic PRFs are generally believed secure against P^NP/poly (an NP oracle does not break standard PRF security heuristics). So a P^NP/poly-recognizable balanced-point property is FLY-blocked at least as hard as a P/poly one. Constructing (A) in FP^NP does not escape — it is recompute-recognizable at P^NP/poly, and the barrier holds there. (This is consistent with Cycle-18 `[apepp-derand-needs-lb]`: derandomizing to FP^NP needs an E^NP LB; AND even after that, FP^NP-constructible is P^NP/poly-recognizable = still blocked.)

`[honest-ceiling]`: the recognizer-strength point is my own *inference* (reasoning about PRG-breaker strength), NOT web-verified — flagged honestly. The load-bearing mechanism (Finding 1, recompute-recognizability) is textbook RR constructivity and does not depend on this. The point is stated as a reading, with the honest caveat that if a P^NP/poly-natural property were NOT believed to break P^NP/poly-secure PRFs (e.g., if such PRFs were not believed to exist), the escape could re-open — but the standard cryptographic belief is the opposite.

## Finding 4 — the two-level balanced point is ASYMMETRIC: meta-tight (theorem) / structural-heuristic `[noncompositionality-mechanistic-asymmetric]`

Finding 1+2 resolve the Cycle-18 framing. Cycle 18 `[a-is-two-balanced-points]` presented the meta-level tension ("constructible ⇒ recognizable") as "core RR intuition," a heuristic *parallel* to the structural tension (expensive ⇒ large-gap, Ilango verbatim "as g gets more expensive the gap also gets larger", `[a-is-a-balanced-point]`). Cycle 19 shows the parallel is **asymmetric**:

- **META level is a THEOREM.** "Constructible ⟹ recognizable" is not intuition — it is recompute-and-compare (Finding 1), i.e. RR's constructivity condition, a precise mechanism. The meta-level non-compositionality (determinism = recognizability, so you cannot construct-and-hide) is mechanistically tight.
- **STRUCTURAL level is a HEURISTIC.** "Expensive ⟹ large-gap" is Lupanov-observed, NOT proven inherent to all balanced-point constructions — the third loop's `[tension-is-lupanov-observed-not-proven-inherent]` stands: the tension is observed for the Lupanov family but a clever explicit construction decoupling expense from gap is not RULED OUT (it would BE (A), circularly).

So the two-level balanced point is **meta-tight and structural-heuristic**: the meta-level wall is a theorem (derandomize ⟹ recognizable ⟹ FLY, no escape at any recognizer strength), while the structural-level wall remains an open heuristic (a decoupled explicit family is the breakthrough, not ruled out). This is a genuine refinement of `[a-is-two-balanced-points]`: the two levels are not symmetric "one tension seen two ways" — they have different epistemic status. The honest implication: the meta-level (derandomization vs non-recognizability) is the HARDER, theorem-blocked side; the structural-level (expense vs small-gap) is the SOFTER, heuristic side where a clever construction could still land. This RE-ORIENTS the live thread slightly toward the structural level — IF a construction threads the structural balanced point, the meta level's theorem (Finding 1) says it must NOT be deterministic (else FLY), i.e. it must be a randomized-with-structure construction whose non-recognizability survives — and whether such a thing can be "explicit" (usable in the reduction) is precisely the open derandomization gap. The two levels couple: a structural success forces a meta-level randomized construction, which forces the derandomization gap.

## Honest scope `[honest-ceiling]`

- NO BREAKTHROUGH. The wall is NOT moved; the meta-level non-compositionality is confirmed (not dissolved) and made MECHANISTIC (a theorem = RR constructivity, via recompute-and-compare), and the two-level balanced point is refined to asymmetric (meta-tight / structural-heuristic).
- The load-bearing mechanism (Finding 1: deterministic construction ⟹ P/poly-recognizable via recompute-and-compare, = RR constructivity) is TEXTBOOK, KNOWN — not a connection humans missed, not newly discovered. The wiki's contribution is (i) making the mechanism explicit behind its own `[gate-1-automatic]`, (ii) the asymmetric two-level refinement, and (iii) the identification that derandomization mechanistically destroys non-recognizability (the randomness IS the non-recognizability). These are wiki-INTERNAL syntheses connecting prior findings (`[apepp-derand-needs-lb]` + `[gate-1-automatic]` + `[a-is-two-balanced-points]`), with KNOWN ingredients.
- The recognizer-strength point (Finding 3) is my own inference, NOT web-verified — flagged. The conclusion (meta-tight theorem) does not depend on it; it only closes one escape route.
- NO impossibility claimed for (A): (A) remains an OPEN construction. The theorem-blocked piece is the *deterministic-constructible* route (derandomize ⟹ recognizable ⟹ FLY, assuming PRFs). A non-deterministic construction (the Lupanov sampler) is non-recognizable and unblocked — but not explicit/usable. The gap is the derandomization gap, now shown to be mechanistically the SAME as the recognizability gap (derandomize ⟺ make-recognizable). This is consistent with — and sharpens — the wiki's standing framing; it does not overturn any prior cycle.
- The "derandomize ⟺ make-recognizable" identification is the sharpest mechanistic form of `[witness-needs-explicit-lb]`: the explicit (deterministic) requirement and the non-recognizable (natural-proofs-escaping) requirement are mechanistically incompatible (determinism IS recognizability via recompute). The only constructions that are non-recognizable are non-deterministic (randomized), which are not "explicit." This is the wall at its sharpest — but it is a sharpening (mechanism), not a fall.
- Consistent with the fifth loop's honest arc (Cycles 16–18): again NO connection humans missed — only a mechanistic deepening of the wiki's own Gate-1-automatic using a KNOWN mechanism (RR constructivity). Under the user's "connections humans have missed" pressure, this cycle honestly reports the mechanism is textbook and the wiki's product is the asymmetric two-level refinement + the derandomization-destroys-non-recognizability identification, not a breakthrough.

## Net

FIFTH 5-CYCLE LOOP, Cycle 4 complete. The within-connection push on the two-level balanced point resolves the Cycle-18 falsifiable target NEGATIVELY and MECHANISTICALLY: satisfying "deterministically-constructible" AUTOMATICALLY breaks "non-recognizable" (because determinism IS recognizability via recompute-and-compare = RR constructivity, a theorem); the recognizer-strength escape (FP^NP / P^NP/poly) is closed (stronger recognizer = stronger PRG-breaker). The meta-level non-compositionality is now a THEOREM (not a heuristic parallel); the two-level balanced point is asymmetric — meta-tight (theorem) / structural-heuristic (Lupanov-observed, `[tension-is-lupanov-observed-not-proven-inherent]`). The sharpest product: **derandomization mechanistically destroys non-recognizability** — the Lupanov sampler's randomness IS its non-recognizability (you cannot recompute a random sample without the seed); derandomizing makes it recompute-recognizable = FLY-blocked. So the two meta requirements on (A) (deterministic-constructible AND non-recognizable) are mechanistically incompatible, connecting `[apepp-derand-needs-lb]` + `[gate-1-automatic]` + `[a-is-two-balanced-points]` via one mechanism. The wall is NOT moved — it is deepened to its sharpest mechanistic form: the explicit (deterministic) requirement and the non-recognizable (natural-proofs-escaping) requirement are incompatible because determinism IS recognizability. (A) remains an OPEN construction; the live thread is unchanged (`[s1a-is-the-live-thread]`); the structural heuristic level (a decoupled explicit family) is the softer side where a clever construction could still land, but any structural success forces a meta-level randomized construction and hence the open derandomization gap. NO BREAKTHROUGH; `[honest-ceiling]` upheld. Wiki state after Cycle 19: 16 pages, 35 sources, all wikilinks resolve.