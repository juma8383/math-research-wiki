---
cycle: 21
loop: 6
date: 2026-08-23
slug: fpnp-escapes-fly
tags:
  - sixth-loop-cycle-1
  - fly-constructivity-is-corp-bptime
  - barrier-ceases-above-conp
  - recognizer-strength-escape-is-open
  - cycle19-no-escape-was-overextension
  - fpnp-escape-not-breakthrough
  - wall-purely-structural-for-fpnp
  - meta-obstruction-fp-specific
  - two-faces-constructivity-axis
  - fpnp-converges-to-williams-template
  - constructible-implies-recognizable
  - derandomization-destroys-nonrecognizability
  - noncompositionality-mechanistic-asymmetric
  - a-is-two-balanced-points
  - apepp-derand-needs-lb
  - a-is-apepp-style-construction
  - nexp-lb-route-naturalproofs-closed
  - mining-redirects-to-s1a
  - s1a-is-the-live-thread
  - cwy-2023-blackbox
  - rr-and-fly-partition-by-largeness
  - fly-needs-no-largeness
  - gate-1-automatic
  - balanced-point-non-compositional
  - two-dim-to-one-dim-wall
  - a-is-a-balanced-point
  - tension-is-lupanov-observed-not-proven-inherent
  - witness-needs-explicit-lb
  - honest-ceiling
  - main-loop
  - no-subagents
provenance: "main loop, no subagents (HTTP 429 usage limit persists); sixth-loop Cycle 1 — the user directed 'continue making a real breakthrough or solve the problem,' authorizing a sixth loop. Per the fifth-loop synthesis ([no-missed-connection-moved-wall]: the wall's lock is a CONSTRUCTION not a CONNECTION, build (A) directly), this cycle attacks the ONE load-bearing link self-flagged as unverified in Cycle 19 — [recognizer-strength-no-escape] (my own inference, explicitly flagged 'NOT web-verified'). Two targeted web searches (Fan-Li-Yang black-box natural proof constructivity; Williams NP-natural/coNP-natural hierarchy) were run to settle it. The result is a real CORRECTION of Cycle 19, not a re-assertion."
source_grounding: "web-verified at SEARCH/arXiv-SUMMARY level, NOT PDF-line-verified (the standing [honest-ceiling] caveat). Concretely: (1) FLY black-box-natural constructivity = BPTIME[polylog(N)] (randomized oracle poly-time), and the CWY unavoidable form = coRTIME[polylog(N)]/log N (one-sided error) — from the Fan-Li-Yang STOC 2022 / ECCC TR21-125 summary and the Chen-Williams-Yang ITCS 2023 summary; (2) the constructivity hierarchy P-natural (RR) → BPP/coRP-natural (FLY) → NP-natural ('seem unlikely to exist', Rudich 1997) → coNP-natural ('trivially exist, uninformative — anything coNP-constructive or worse is basically uninformative', Williams) — from the natural-proofs survey + Williams 'Natural Proofs versus Derandomization' summary; (3) the recompute-recognizability mechanism (determinism = recognizability) is textbook RR constructivity (Cycle 19, no web search needed). The load-bearing conclusion (FP^NP / P^NP-poly is above the FLY ceiling and the barrier ceases at coNP+) follows from definitions (1)+(2); it is robust to the summary-level caveat because it is a CONSEQUENCE of the stated constructivity classes, not a fine-grained theorem-internal claim. Flagged honestly: the Williams-template convergence and the relativization point at the structural level are reading-level syntheses, less certain than the constructivity-axis map."
---

# Cycle 21 — ATTACKING THE ONE SELF-FLAGGED WEAK LINK: the FP^NP recognizer-strength escape from FLY is OPEN (Cycle 19's [recognizer-strength-no-escape] was an over-extension); the wall, for the FP^NP route, is PURELY STRUCTURAL (the E^NP LB); a real correction, NOT a breakthrough

## What this cycle does

The fifth-loop synthesis ([no-missed-connection-moved-wall], Cycle 20) concluded the wall's lock is a CONSTRUCTION, not a CONNECTION, and the next direction is to attack the (A) open construction directly. The single weakest, self-flagged-as-unverified link in the entire 25-cycle edifice was Cycle 19's `[recognizer-strength-no-escape]` — my own inference (explicitly marked "NOT web-verified") that constructing (A) in FP^NP (giving a P^NP/poly recognizer) does NOT escape the Fan-Li-Yang black-box natural-proofs barrier, because "a stronger recognizer is a stronger PRG-breaker, so the barrier is at least as strong at P^NP/poly." That is exactly where a real gap would hide if one exists — and exactly where an error in my own reasoning would hide. This cycle verifies it against the actual definitions, instead of re-asserting it.

Two targeted web searches settled it (Fan-Li-Yang black-box-natural constructivity; Williams NP-natural/coNP-natural hierarchy). The result is a real CORRECTION of Cycle 19: the FP^NP route is NOT FLY-blocked; the escape is OPEN. But — honestly — the escape does not yield a lower bound by itself; it removes a SPUROUS meta obstruction (Cycle 19's over-extension) and reveals that the wall, for the FP^NP route, is PURELY STRUCTURAL (the E^NP LB). The real obstruction was always there. No breakthrough.

## Finding 1 — the actual constructivity classes of RR and FLY (web-verified): RR = P/poly, FLY = BPTIME/coRTIME[polylog(N)] (randomized oracle); both BELOW the PRF-security (BPP-adversary) threshold `[fly-constructivity-is-corp-bptime]`

The web search confirms the exact constructivity requirements, which Cycle 19 had not pinned down:

- **Razborov-Rudich (standard natural proofs):** constructivity = the property is decidable in **P/poly** (polynomial-size circuits / deterministic poly(N) time on the N-bit truth table, N = 2^n). The barrier: if PRFs exist in C of size s, no P/poly-constructive + large + useful property exists against s-size C.
- **Fan-Li-Yang (black-box natural proofs, STOC 2022 / ECCC TR21-125):** constructivity is STRENGTHENED to a **randomized oracle algorithm running in polylog(N) = poly(n) time** — i.e., **BPTIME[polylog(N)]-constructive** (BPP with oracle access to the candidate function f). The barrier: if PRFs secure against **BPP adversaries** can be built in C of size s, no BPTIME[polylog(N)]-constructive useful property exists against s-size C. The black-box distinguisher would be a BPP oracle algorithm that breaks the PRF.
- **Chen-Williams-Yang (ITCS 2023):** black-box constructivity is UNAVOIDABLE for NEXP lower bounds — NEXP ⊄ C ⟺ a **coRTIME[polylog(N)]/log N**-constructive (one-sided-error = coRP) property useful against C. And they prove unconditionally that no **DTIME[polylog(N)]-constructive** (deterministic) property is useful against any class expressive enough to simulate CNFs — "randomness is essential," the BPTIME/coRTIME aspect cannot be removed.

`[fly-constructivity-is-corp-bptime]`: the two barrier constructivity classes are **P/poly** (RR) and **BPTIME/coRTIME[polylog(N)]** (FLY/CWY) — deterministic-poly and randomized-oracle-polylog respectively. **Both are below the PRF-security (BPP-adversary) threshold.** This is not incidental: the natural-proofs barrier's mechanism is "a PRF (indistinguishable from random to LOW-complexity tests) fools the property," so the barrier can only exist where the property's decider is BELOW the PRF's security level. RR and FLY are exactly the low-complexity regimes where PRFs are secure.

## Finding 2 — the constructivity hierarchy: the barrier CEASES at coNP+; P^NP/poly is above the ceiling `[barrier-ceases-above-conp]`

The second web search surfaced the constructivity hierarchy that the wiki had not made explicit:

- **P-natural** (RR): the standard barrier zone. Cryptographically blocked (assuming PRFs).
- **NP-natural:** Rudich (1997) — NP-natural useful properties "seem unlikely to exist." Impagliazzo-Kabanets-Wigderson: NP-natural (without largeness) useful against P/poly ⟹ NEXP ⊄ P/poly. An informal barrier, NOT the cryptographic RR barrier.
- **coNP-natural and above:** **useful properties TRIVIALLY exist** (exhaustively try all small circuits in parallel — "is T computable by some s-size C-circuit?" is in coNP) and are **UNINFORMATIVE** — Williams: "anything coNP-constructive or worse is basically uninformative." The barrier **CEASES** to be meaningful at coNP constructivity: properties are trivially available there, but they are the *negation* of the lower bound (exhaustive search), not a constructive insight, so they yield no real LB.

`[barrier-ceases-above-conp]`: the natural-proofs/FLY barrier is fundamentally a **LOW-constructivity** barrier (P, BPP, coRP — below the PRF-security/BPP-adversary threshold). At **coNP constructivity and above** the barrier ceases: useful properties trivially exist (via exhaustive circuit search) and are uninformative. **P^NP ⊇ coNP** (a P^NP machine simulates coNP via the NP oracle), so **P^NP/poly-constructive properties sit at/above the coNP threshold — in the "barrier ceases, uninformative" regime.** This is robust and definitionally forced: the barrier cannot be extended to P^NP/poly without assuming PRFs secure against NP-oracle adversaries — which is false (an NP oracle inverts/searches and breaks PRFs) and far stronger than one-way functions.

This is a NEW AXIS for the wiki. The wiki had partitioned the barrier space by **LARGENESS** ([rr-and-fly-partition-by-largeness]: large → RR-blocked, non-large → FLY-blocked, Cycle 14). Cycle 21 adds the **CONSTRUCTIVITY-LEVEL** axis: the barrier operates at P / BPP / coRP (below PRF security) and **ceases at coNP+**. The two axes are independent: largeness partitions the *low-constructivity* barrier zone; constructivity-level determines whether you are *in* the barrier zone at all.

## Finding 3 — the REAL CORRECTION of Cycle 19: the FP^NP recognizer-strength escape from FLY is OPEN, not closed `[recognizer-strength-escape-is-open]` `[cycle19-no-escape-was-overextension]`

Now the load-bearing settlement. Cycle 19's `[recognizer-strength-no-escape]` claimed: construct (A) in FP^NP (deterministic poly-time + NP oracle) → recognizer "is-the-output-of-A" is in P^NP/poly → "a stronger recognizer is a stronger PRG-breaker, so the barrier is at least as strong at P^NP/poly" → escape closed. That was my own inference, explicitly flagged "NOT web-verified."

Against the actual definitions (Findings 1-2): **the claim is WRONG.**

- The "determinism = recognizability" mechanism (Cycle 19, `[constructible-implies-recognizable]`) is real: an FP^NP construction A of g does yield a recognizer of g's truth table via recompute-and-compare (run A, with its NP-oracle calls, on all n-bit inputs = poly(N) with an NP oracle = P^NP(N) = P^NP/poly nonuniformly). That part is correct.
- **But the barrier consequence does not follow for FP^NP.** The recognizer is **P^NP/poly**, which is (a) NOT RR-natural (RR needs P/poly — and P^NP/poly-complete properties are not in P/poly, assuming P^NP ⊄ P/poly; this is exactly why Williams's ACC proof "does not appear to yield any P-natural or NP-natural property"), and (b) NOT FLY-natural (FLY needs BPTIME/coRTIME[polylog(N)] — a randomized *f*-oracle machine; P^NP has an NP oracle, a fundamentally different and stronger oracle than f-access, and is deterministic-with-NP-oracle not randomized-with-f-oracle). P^NP/poly is **above the FLY ceiling** and **above the coNP threshold where the barrier ceases** (Finding 2).
- "A stronger recognizer is a stronger PRG-breaker" is the error: a P^NP/poly recognizer is NOT a PRG-breaker *in the sense FLY means*, because FLY's barrier is keyed to **BPP-adversary** PRF security, and a P^NP adversary breaks PRFs trivially (NP search) — so PRFs are not assumed secure against it, and FLY's theorem does not speak to it. The barrier does not get "stronger" above its ceiling; it gets **vacuous** (the cryptographic assumption fails).

`[recognizer-strength-escape-is-open]`: the FP^NP route is **NOT FLY-blocked**. The escape is **OPEN**. `[cycle19-no-escape-was-overextension]`: Cycle 19's `[recognizer-strength-no-escape]` was an **OVER-EXTENSION** of the "determinism = recognizability ⟹ FLY" mechanism — which is valid for the **FP** route (P/poly recognizer = exactly FLY's constructivity class) — to the **FP^NP** route (P^NP/poly recognizer = above FLY's constructivity class). The mechanism (recompute-recognizability) is universal; the *barrier consequence* is FP-specific. This is a real correction of my own prior analysis, caught by actually verifying the link I had flagged.

## Finding 4 — honest scope: the FP^NP escape is NOT a breakthrough — it removes a SPUROUS obstruction and reveals the wall is purely structural `[fpnp-escape-not-breakthrough]` `[wall-purely-structural-for-fpnp]` `[meta-obstruction-fp-specific]`

`[honest-ceiling]` applied to my own correction: does escaping FLY via FP^NP get us closer to a lower bound? **No — not by itself.** The P^NP/poly property "is-the-output-of-A" is only *informative* if A actually constructs a hard function g ∉ C — and constructing such an A **IS** the lower bound. Per Cycle 18's `[apepp-derand-needs-lb]` (Korten FOCS 2021, Thm 11): a **deterministic FP^NP** construction of (A) (i.e. derandomizing the Lupanov sampler / EMPTY ∈ FZPP^NP to deterministic FP^NP) **is equivalent to an E^NP 2^{Ω(n)} circuit lower bound.** So:

- The FLY barrier does NOT block the FP^NP route (Finding 3) — but the FP^NP route's *sole* obstacle is the **structural E^NP LB** (Cycle 18), the open circuit-LB-frontier problem.
- Escaping FLY via FP^NP removes a **SPURIOUS** meta obstruction (Cycle 19's over-extension added a meta/FLY obstruction to the FP^NP route that was never really there — the barrier doesn't reach P^NP/poly). The **real** obstruction (structural E^NP LB) was always there and is unchanged.

`[wall-purely-structural-for-fpnp]`: for the FP^NP route, the wall is **PURELY STRUCTURAL** (the E^NP LB / balanced-point construction); the meta/recognizability obstruction is **absent** (P^NP/poly is above the FLY ceiling). `[meta-obstruction-fp-specific]`: the Cycle-19 "mechanistic incompatibility" (determinism = recognizability ⟹ the explicit and non-recognizable requirements are incompatible) is **FP-specific, NOT universal** — it holds for the FP route (P/poly recognizer ∈ FLY's class) and does NOT hold for the FP^NP route (P^NP/poly recognizer ∉ FLY's class, above the ceiling). The two meta requirements (deterministically-constructible ∧ non-recognizable-in-the-barrier-sense) are **RECONCILABLE** for FP^NP: constructible-in-FP^NP ⟹ P^NP/poly-recognizable, which is > coRP = non-FLY-recognizable. Cycle 19's "sharpest mechanistic form of the wall" was the sharpest form of the **FP-route** wall, not the universal wall. This is a genuine walk-back of the universality claim in Cycle 19 / the Cycle-20 synthesis — caught by attacking the link the fifth loop itself flagged as weakest.

The two-level balanced point ([a-is-two-balanced-points], Cycle 18) **DECOUPLES** for FP^NP:
- **META level** (constructible ⟹ recognizable): a THEOREM (RR constructivity), but its *barrier consequence* is **FP-specific** (only at FP/P/poly). At FP^NP, no meta FLY obstruction.
- **STRUCTURAL level** (expensive ⟹ large-gap): a HEURISTIC ([tension-is-lupanov-observed-not-proven-inherent]), and the **SOLE** real obstruction for FP^NP (via [apepp-derand-needs-lb]).

So for the FP^NP route the wall is one-level (structural), not two-level. The "coupling" between the levels (Cycle 19: a structural success forces a meta randomized construction) is **FP-specific**: at FP^NP a structural success (an E^NP LB) *is* the FP^NP construction and incurs no meta FLY penalty. The levels couple only on the FP route.

## Finding 5 — the two faces' opposite fates, sharpened to the CONSTRUCTIVITY-LEVEL axis `[two-faces-constructivity-axis]`

The wiki's [two-faces-two-np-variants] explained the two faces' opposite fates via CWY's NEXP-specificity (the mining/class-LB face is CWY-forced to coRP and FLY-blocked; the explicit-function face is outside CWY's scope). Cycle 21 sharpens the mechanism: it is the **CONSTRUCTIVITY LEVEL**, not just NEXP-specificity.

- **Mining / class-LB face** (NEXP ⊄ C): CWY forces a **coRTIME[polylog(N)]/log N** (coRP) constructive property — which is **in FLY's barrier zone** (coRP = FLY's constructivity class) → **FLY-blocked** ([nexp-lb-route-naturalproofs-closed]). The class-LB face is forced DOWN to the barrier zone.
- **Explicit-function / (A) face** (g ∉ C, a single function): CWY's unavoidability is NEXP-specific and does NOT apply; the construction can be stated at **FP^NP / P^NP-poly** — **above** the FLY ceiling and the coNP threshold → **NOT FLY-blocked** ([recognizer-strength-escape-is-open]). The explicit-function face is NOT forced down; it can sit above the barrier.

`[two-faces-constructivity-axis]`: the two faces sit at **different constructivity levels** on the P → BPP/coRP → NP → coNP+ hierarchy, and the barrier applies only **below coNP**. The mining face is forced to coRP (in the zone, blocked); the (A) face can be at P^NP (above the zone, not blocked). The two faces have opposite fates because they live at opposite ends of the constructivity-level axis. This is the mechanism behind [two-faces-two-np-variants], made explicit — and it is a SECOND axis (the wiki had largeness; Cycle 21 adds constructivity-level). The two variants are now on TWO axes: largeness (RR vs FLY) AND constructivity-level (below-coNP blocked vs above-coNP unblocked).

## Finding 6 — the FP^NP route RE-MERGES with the Williams mining face at the Williams-template level `[fpnp-converges-to-williams-template]`

`[fpnp-converges-to-williams-template]`: the FP^NP construction of (A) ⟺ E^NP LB (Cycle 18) ⟺ the **Williams algorithmic method** (a faster-than-exhaustive SAT/CAPP algorithm for the class ⟹ an E^NP/NEXP lower bound against the class) applied to the balanced-point class. So the explicit-function face, taken at the FP^NP constructivity level, RE-MERGES with the mining/Williams face at the Williams-template level: both reduce to "find a faster-SAT/CAPP algorithm for the relevant circuit class." This confirms [two-faces-two-np-variants]'s convergence-on-(A) and sharpens it: the two faces converge at the **FP^NP / Williams-template** constructivity level, not merely at the (A) object.

The honest caveat: the E^NP LB faces the **relativization/algebrization** barrier. Williams overcame relativization for NEXP/ACC via the non-relativizing ACC-SAT algorithm (the Yao-Beigel-Tarui SYM+ representation). A faster-SAT/CAPP algorithm for the **balanced-point class** would need the same non-relativizing structure — which is the open structural problem. So the FP^NP route is not barrier-free at the structural level; it trades the (spurious, FP-specific) meta FLY obstruction for the (real) structural relativization obstruction. This reading-level synthesis is flagged as less certain than the constructivity-axis map (Finding 1-3 are definitionally forced; Finding 6 is a synthesis).

## Honest scope `[honest-ceiling]`

- **NO BREAKTHROUGH.** This is stated plainly. The structural E^NP LB — the circuit-LB frontier — remains open and is the SOLE real obstruction for the FP^NP route. Correcting Cycle 19's over-extension does not construct (A); it clarifies that the obstruction is purely structural, not meta+structural.
- This cycle DID move something real, honestly: it **corrected an error** in the wiki's own prior analysis (Cycle 19's `[recognizer-strength-no-escape]` was an unverified over-extension; the actual FLY/CWY definitions refute it). Corrections are progress, and this is the first cycle in several that changed a substantive claim rather than re-describing the same wall. But a correction that removes a *spurious* obstruction is not a breakthrough — the real obstruction (structural E^NP LB) was always there and is unmoved.
- The genuine (modest) products of this cycle: (i) the web-verified **constructivity-level axis** ([barrier-ceases-above-conp], [two-faces-constructivity-axis]) — a NEW axis complementing the largeness axis; (ii) the **correction** of Cycle 19 ([recognizer-strength-escape-is-open], [cycle19-no-escape-was-overextension]); (iii) the **reframe** that the wall is purely structural for FP^NP ([wall-purely-structural-for-fpnp], [meta-obstruction-fp-specific]) — the two-level balanced point decouples to one-level (structural) on the FP^NP route; (iv) the **convergence** of the two faces at the FP^NP/Williams-template level ([fpnp-converges-to-williams-template]).
- The fifth-loop synthesis claimed the wall's "sharpest mechanistic form" was the universal incompatibility (determinism = recognizability). This cycle **walks back the universality**: that incompatibility is FP-specific. The wall, properly understood, is structural (the E^NP LB) — the meta "wall" was an artifact of restricting to the FP route. This is a cleaner, more honest picture, but it does not make (A) easier to construct; it makes the obstruction *precise*: the only thing standing between us and (A) is an E^NP circuit lower bound for the balanced-point class, attainable (by the Williams template) via a faster-SAT/CAPP algorithm for that class. Precise ≠ solved.
- All web-grounded findings are **search/arXiv-summary-level, NOT PDF-line-verified** (the standing caveat). The load-bearing conclusion (FP^NP/P^NP-poly is above the FLY ceiling; the barrier ceases at coNP+) is a consequence of the STATED constructivity classes (P/poly for RR, BPTIME/coRTIME[polylog(N)] for FLY/CWY, coNP+ = barrier-ceases), so it is robust to the summary-level caveat; it does not hinge on a fine-grained theorem-internal detail. The Williams-template convergence (Finding 6) is a reading-level synthesis, flagged as less certain.
- (A) remains an OPEN construction ([a-remains-open-construction]). The natural-proofs barrier is conditional on PRFs/OWFs. The wall is genuinely alive at one point — now identified precisely as the structural E^NP LB, with the meta obstruction removed for the FP^NP route.

## Net

SIXTH 5-CYCLE LOOP, Cycle 1 (absolute Cycle 21) complete. Attacking the one self-flagged-as-unverified link ([recognizer-strength-no-escape], Cycle 19) produced a real CORRECTION, not a re-assertion: the FP^NP route is NOT FLY-blocked (P^NP/poly is above the FLY ceiling = BPTIME/coRTIME[polylog(N)] and above the coNP threshold where the barrier ceases); Cycle 19's no-escape was an over-extension of the FP-route mechanism. The escape is OPEN but NOT a breakthrough — it removes a spurious meta obstruction and reveals the wall is PURELY STRUCTURAL for the FP^NP route (the E^NP LB, via [apepp-derand-needs-lb] / the Williams template). The "mechanistic incompatibility" (Cycle 19's sharpest form) is FP-specific, not universal — walked back. New axis added: constructivity-level (barrier operates at P/BPP/coRP, ceases at coNP+), complementing the largeness axis. The two faces' opposite fates sharpened to the constructivity-level axis (mining forced to coRP = blocked; (A) can sit at P^NP = unblocked). The two faces re-merge at the FP^NP/Williams-template level. NO BREAKTHROUGH; `[honest-ceiling]` upheld — the deliverable is a corrected, cleaner map (wall = structural E^NP LB for FP^NP, meta obstruction removed) + the honest report that correcting an error ≠ solving the problem. (A) remains the single live thread, an OPEN construction. Wiki state after Cycle 21: 16 pages, 37 sources, all wikilinks resolve.