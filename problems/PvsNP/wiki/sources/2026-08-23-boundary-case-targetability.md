---
title: The boundary case — a single-function LB in NEXP implies the class LB; the wall pins to Williams' (=>) targetability
cycle: 4
loop: 2
date: 2026-08-23
tags: [boundary-case-resolved, single-lb-implies-class-lb, williams-iff-vicinity, targetability-circularity, wall-pinned-to-targetability, honest-ceiling, second-loop-cycle-4, main-loop, no-subagents]
provenance: "Second 5-cycle loop, Cycle 4. Main loop, no subagents (dispatching API HTTP 429 usage limit persists). Web-confirmed (search/arXiv-summary level), NOT PDF-line-verified. Honors [honest-ceiling]: no fabricated P vs NP proof; faithful reporting; the deliverable is a sharper map, not a theorem."
---

# Cycle 4 — the boundary case: g ∈ NEXP, so the S1.a LB implies the class LB; the wall pins to Williams' (=>) targetability

## What Cycle 4 attacks

Cycle 3 (`sources/2026-08-23-tension-not-definitional.md`) reclassified the S1.a wall from Cycle 2's "near-definitional tension" to "requires a genuinely new LB method," concluding the constructivity-forcing (Williams Thm 1.1) is **NEXP-specific** (Easy Witness Lemma mechanism) and **absent for explicit functions**. But Cycle 3's own honest-scope left one case explicitly open: *"the boundary case (an explicit g that is ALSO in a nondeterministic class, e.g. NP∩coNP) is unaddressed."* This is the natural next lever, because the S1.a witness g IS such a function: g is AC⁰-constructible ⊆ P ⊆ NP ⊆ NEXP. So g is not merely an explicit function floating free of the nondeterministic regime — it lives INSIDE NEXP. Cycle 4 tests whether this boundary case re-tightens the wall (i.e. whether the constructivity-forcing, which Cycle 3 said is "absent for explicit f," is in fact present once the explicit f is observed to be in NEXP).

## The verified logical chain `[single-lb-implies-class-lb]`

The S1.a witness g is AC⁰-constructible: the `(AC⁰_d)`-MCSP reduction outputs g_n (a function on N = Θ(n²) bits) via a **logtime-uniform AC⁰** circuit family. As a language g = {(n, x) : g_n(x) = 1}, this is computable in polytime (logtime-uniform AC⁰ ⊆ P), so **g ∈ P ⊆ NP ⊆ NEXP**. This is the entry point Cycle 3 did not examine.

The S1.a lower bound is the **single-function-family** statement

> (LB) for each n, g_n ∉ size-(1−4δ)T_n · AC⁰_{d−1}

i.e. g has no depth-(d−1) AC⁰ circuit of size below the window. Because g ∈ NEXP and g_n is hard, g is **an NEXP witness of non-containment**:

> (A) **(LB) ⟹ NEXP ⊄ size-T·AC⁰_{d−1}.**

This is purely logical: "NEXP ⊄ C" means "∃ f ∈ NEXP : f ∉ C," and g is exactly such an f. The S1.a single-function LB is **stronger than necessary** to witness the class-containment LB — it does not merely imply it, it *is* a witness of it. So the S1.a LB is NOT disjoint from the class-LB regime Williams' theorem governs; it sits squarely inside it. This is the point that was invisible to Cycle 3's "explicit f ≠ nondeterministic class" framing — the S1.a witness is simultaneously an explicit function AND an NEXP function, so the class-LB-forcing applies to the *consequence* of its LB even though it does not (per Cycle 3) apply to the *mechanism* of its proof.

## The wall re-tightens — partially — via Williams' (=>) `[williams-iff-vicinity]`

Williams Theorem 1.1 (`[williams-constructive-theorem]`, "Natural Proofs vs. Derandomization," SIAM J. Comput. 2016; web-confirmed) is an **IFF**:

> **NEXP ⊄ C  ⟺  there exists a (P/poly)-recognizable useful property against C** (P-time, O(log n) advice).

The (⇒) direction is the one that bites here: if the class LB is TRUE, then a recognizable useful property **exists**. Combining with (A):

> (B) **whenever the S1.a witness g exists (with its LB), a (P/poly)-recognizable useful property against size-T·AC⁰_{d−1} EXISTS.**

This is a genuine re-tightening relative to Cycle 3. Cycle 3's framing — "the constructivity-forcing is absent for explicit f, so a non-recognizable LB is not blocked" — is incomplete: it considered whether the forcing *blocks the proof of g's LB*, and found it does not (the Easy Witness mechanism doesn't reach explicit functions). But it did not consider that g's LB **entails** a class LB, which Williams' IFF then equips with a recognizable property — so a recognizable property is **guaranteed to exist in the vicinity** of any successful S1.a witness. The forcing's *consequence* (a recognizable property exists) is present even where its *mechanism* (easy-witness diagonalization) is absent. Cycle 4 therefore **partially walks back** Cycle 3's optimism: the wall is not as cleanly "soft" as "no theorem forces recognizability here," because a theorem (Williams ⇒) forces the *existence* of a recognizable property whenever the witness exists.

## The crux: does the guaranteed recognizable property reach g? `[targetability-circularity]`

The re-tightening is only partial because (B) guarantees a recognizable property for **some** NEXP hard function h ∈ NEXP \ size-T·AC⁰_{d−1}, and the S1.a reduction does not need "some" h — it needs the **specific** g (AC⁰-constructible, tight-window). So the wall's status turns on a precise question about the **constructive content of Williams' (⇒)**:

> **(Q-targetability)** Does Williams' (⇒) construction produce a recognizable property that can be made to **accept the specific g** (the reduction's witness), or only a generic/unspecified NEXP hard function h ≠ g?

- **If (Q-targetability) = "can target g":** the wall **re-tightens** to roughly Cycle 2's severity. A recognizable property accepting g exists whenever the S1.a witness exists ⟹ algorithmizing the reduction with that property yields SAT ∈ subexp-circuits (the Ilango collapse, `[ppoly-recognizable]`) ⟹ the S1.a witness cannot be non-recognizable ⟹ Cycle 3's loosening is **overturned** for this boundary case.
- **If (Q-targetability) = "generic h only":** the wall **stays loosened** (Cycle 3). The recognizable property P* Williams guarantees accepts a *different* function h (not AC⁰-constructible, not tight-window), which cannot substitute for g in the reduction (g must be the specific AC⁰-constructible tight-window witness). P*'s existence does not collapse SAT, because the collapse requires the *reduction's specific witness's* LB to be recognizable, not just any recognizable property in the vicinity. g's non-recognizable LB survives.

### Why (Q-targetability) leans toward "generic h only" — the circularity `[targetability-circularity]`

A first-principles read of Williams' (⇒) supports the "generic h only" reading, and hence the wall **staying loosened**, but on reasoning I flag rather than line-verify. Williams' (⇒) builds a recognizable property **from the assumption** "NEXP ⊄ C" (the easy-witness/diagonalization machinery certifies the existence of a hard NEXP function and turns that existence into a recognizable property). The assumption supplies only the **existence** of *some* hard NEXP function; it does not single out g. To make the resulting property **accept the specific g**, one would need to feed the machinery the additional fact "g is the hard one" — i.e. **g's own lower bound**. But g's LB is exactly the object whose (non-)recognizability is in question: if g's LB is recognizable it already collapses (Ilango), and if it is non-recognizable it cannot be the certificate that retargets Williams' property onto g. So the re-tightening scenario appears **circular** — it needs a recognizable LB for g to make Williams' property target g, and that recognizable LB is precisely what the barrier forbids. This is the "generic h only" reading: the guaranteed recognizable property lives at the level of a generic NEXP hard function, and cannot be pulled down onto the specific AC⁰-constructible tight-window g without independently solving the very recognizability problem the wall poses.

**`[honest-ceiling]` flag:** the circularity/targetability argument is *my reasoning* about the constructive content of Williams' (⇒), derived from the search-level description of the theorem (the property "distinguishes *some* single function from all C-functions"), **not line-verified against the proof**. If Williams' (⇒) construction in fact permits arbitrary retargeting onto any chosen hard function f ∈ NEXP \ C (taking f's hardness as a given), the circularity dissolves and the wall re-tightens. I do not resolve this; I record it as the precise open sub-question on which the boundary case now turns.

## `[wall-pinned-to-targetability]` — the wall's status, refined

Cycle 4 does NOT restore Cycle 2's "near-definitional tension" (that was correctly deflated by Cycle 3's mechanism argument: the Easy Witness forcing does not reach explicit functions). And it does NOT leave Cycle 3's "loosened" status untouched (it surfaces that g's LB *entails* a class LB, which Williams equips with a recognizable property in the vicinity). The wall's status now lands **between** Cycle 2 and Cycle 3, and is **pinned to a single precise open question** — (Q-targetability), the constructive content of Williams' (⇒):

> The S1.a wall is **soft** (a non-recognizable explicit-f tight-window AC⁰ LB is possible in principle) **IFF** Williams' guaranteed recognizable property cannot be retargeted onto the specific g; it is **hard** (re-tightened, the witness cannot be non-recognizable) **IFF** that property can be retargeted onto g. The boundary case is reduced to the targetability question, not resolved.

This is a sharpening, not a loosening or a tightening: the wall's previously-vague "is the constructivity-forcing present?" is now the precise "does Williams' (⇒) target a specific hard function or only a generic one?" The empirical absence of a non-recognizable explicit-f method (Cycle 3) and the tight-window gate (Gate 2, `[ac0-tight-window]`) remain; Cycle 4 adds that the vicinity-recognizability (Williams ⇒) is *also* present and its reach into g's regime is the now-precise locus of the wall.

## Honest scope `[honest-ceiling]`

- **No breakthrough.** No P≠NP proof, no new circuit lower bound, no derandomization. The product is a precise refinement of the wall's status: the boundary case Cycle 3 left open is now **reduced to a precise open question** (Williams' (⇒) targetability), not resolved either way.
- **The chain (A)+(B) is solid.** g ∈ NEXP (logtime-uniform AC⁰ ⊆ P ⊆ NEXP) and g's LB ⟹ NEXP ⊄ size-T·AC⁰_{d−1} (logical) and Williams (⇒) ⟹ a recognizable property exists (the IFF, web-confirmed). These do not depend on the unverified targetability claim.
- **The targetability/circularity claim is FLAGGED, not line-verified.** It is reasoning about Williams' (⇒) constructive content from the search-level theorem statement. If the proof permits retargeting onto any given hard f (taking f's hardness as input), the wall re-tightens; the circularity-against-retargeting argument would then be wrong. Resolving this requires reading Williams 2016 §3 (the (⇒) construction), not done here.
- **Threshold/d-parameter subtlety, FLAGGED.** Whether "NEXP ⊄ size-T·AC⁰_{d−1}" at the Lupanov window T (up to 2^{Θ(√N)} as a function of g's input length N) is itself KNOWN vs OPEN is d-dependent and NOT verified here. For small d (e.g. d=3, AC⁰_2 = DNF), parity requires 2^{Ω(N)} DNF size, which **exceeds** 2^{Θ(√N)}, so the class LB (and hence a recognizable property, e.g. the parity-based natural property) is **already known** — making the vicinity-recognizability *concrete* there (and the targetability question live on a known object). For larger d, parity's depth-(d−1) bound 2^{Ω(N^{1/(d−2)})} may fall **below** the window threshold T = 2^{Θ(√N)}, so the class LB at the window is OPEN and Williams' guarantee is conditional on the S1.a witness existing (vacuous until then). The d-dependence is not pinned; it is recorded as a parameter subtlety for Cycle 5, not resolved.
- **A secondary, sharper reading of the vicinity point.** Even granting (B) concretely (recognizable property exists), it is a property against AC⁰_{d−1} at size T — the *same* threshold the reduction uses. So the "vicinity" is not loose: the recognizable property and the reduction's witness live at the same size/depth. This makes the targetability question (Q) the more central, not a side issue: the recognizable property is at the *right place*; the only question is whether it can be made to accept the *right function* (g). Recorded for Cycle 5.

## Net

The boundary case Cycle 3 flagged is now precisely characterized but **not closed**: because g ∈ NEXP, the S1.a single-function LB **entails** the class-containment LB (NEXP ⊄ size-T·AC⁰_{d−1}), and Williams' IFF then **guarantees a recognizable useful property exists in the vicinity** of any successful S1.a witness. The wall is therefore **not as soft as Cycle 3 implied** (a recognizable property is forced to exist, not merely possibly absent). But the wall is **not re-tightened to Cycle 2** either, because (my flagged reasoning) the guaranteed recognizable property accepts a *generic* NEXP hard function and cannot be retargeted onto the specific AC⁰-constructible tight-window g without an independently-recognizable LB for g — which is circular. The wall's status is **pinned to (Q-targetability)**, the constructive content of Williams' (⇒): the single open sub-question on which the boundary case, and hence whether Cycle 3's loosening survives the g ∈ NEXP observation, now turns. No breakthrough; the map is sharper and the wall's locus is now a named, falsifiable question. `[honest-ceiling]`.

## Sources

- Williams, R. — "Natural Proofs versus Derandomization," STOC 2013 / SIAM J. Comput. 2016, Theorem 1.1 (NEXP ⊄ C ⟺ recognizable useful property against C, P-time + O(log n) advice). [web-confirmed, search/arXiv-summary level; NOT PDF-line-verified]
- Cycle 3 source: `sources/2026-08-23-tension-not-definitional.md` (the boundary case flagged in its honest-scope; the NEXP-specific Easy Witness mechanism argument).
- Cycle 2 source: `sources/2026-08-23-recognizable-stronger-than-natural.md` (the triple-conjunction wall; Williams' LB is (P/poly)-recognizable).
- Cycle 1 source: `sources/2026-08-23-ac0-escape-hatch.md` (g ∈ AC⁰-constructible; the (P/poly)-recognizability gate `[ppoly-recognizable]`; the tight-window gate `[ac0-tight-window]`).
- Ilango FOCS 2020 / ECCC TR20-183 §1.4 (the collapse: recognizable LB ⟹ SAT ∈ subexp-circuits) — referenced via Cycle 1's line-verified quotation.
- Search results (this turn) on Williams Thm 1.1, CWY ITCS 2023 (black-box constructivity for NEXP), Oliveira 2013 survey (Prop 4.2, the IFF) — confirming the IFF is a class-containment-LB statement and the property "distinguishes some single function from all C-functions."