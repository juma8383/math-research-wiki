---
title: Second 5-cycle loop synthesis — the AC⁰ face mapped; the wall pinned, not moved
cycle: 5
loop: 2
date: 2026-08-23
tags: [second-loop-synthesis, wall-pinned-not-moved, single-lb-implies-class-lb, williams-iff-vicinity, targetability-circularity, wall-pinned-to-targetability, tension-not-definitional, recognizable-stronger-than-natural, ac0-lb-existence-passed, ac0-natural-proofs-wall, ac0-tight-window, triple-conjunction-wall, wall-loosened-not-fallen, honest-ceiling, second-loop-cycle-5, main-loop, no-subagents]
provenance: "Second 5-cycle loop, Cycle 5 (synthesis). Main loop, no subagents (dispatching API HTTP 429 usage limit persists). Synthesizes Cycles 1-4 of the second loop (all web-confirmed, NOT PDF-line-verified except Cycle 1's Ilango quotation). Honors [honest-ceiling]: no fabricated P vs NP proof; faithful reporting; the deliverable is a sharper map + one concrete next verification, not a theorem."
---

# Cycle 5 — synthesis of the second 5-cycle loop: the AC⁰ face is mapped; the wall is pinned, not moved

## What the second loop set out to do, and did

The user's second mandate was "make a true breakthrough or solve the problem." The first loop (`sources/2026-08-23-five-cycle-synthesis.md`) had confirmed the `[witness-needs-explicit-lb]` obstruction from seven angles across both live routes (meta-complexity Route A + Williams mining) and three circuit models, concluding the wall is an OPEN construction (conditional on OWFs), not a proven impossibility — with the worst-case SAT route blocked by a PROVEN theorem (`[n2-wall]`) and the average-case/mining route blocked by an open construction (hence more promising). The second loop did not re-survey; it **attacked the wall's thinnest face directly** — the AC⁰ (S1.a) face, identified in Cycle 1 as the one face where LB-existence PASSES — and traced the recognizability gate that blocks it across four cycles.

## The four-cycle trajectory of the recognizability gate

The second loop's substantive content is a four-cycle oscillation in the *status* of the S1.a wall's Gate 1 (the `(P/poly)`-recognizability gate), each cycle testing the previous one's claim under `[honest-ceiling]`:

| Cycle | Claim about Gate 1 (recognizability) | Wall status | Pessimism |
|---|---|---|---|
| **1** (`[ac0-lb-existence-passed]`, `[ppoly-recognizable]`, `[ac0-tight-window]`) | The AC⁰ face passes LB-existence (Sipser/RST explicit exponential AC⁰ LBs exist) but the known LBs are `(P/poly)`-recognizable (Ilango §1.4, line-verified) ⇒ would collapse SAT. Wall = two gates: recognizability + tight-window. | Located exactly in AC⁰ | medium |
| **2** (`[recognizable-stronger-than-natural]`, `[triple-conjunction-wall]`) | Ilango's gate is the **constructivity** axis, not largeness — **strictly stronger than Razborov-Rudich**; the canonical non-natural escape (Williams NEXP⊄ACC⁰, drops largeness) is the WRONG escape. Wall = triple conjunction {non-recognizable ∧ AC⁰-constructible explicit g ∧ tight-window}; non-recognizable↔constructible in **near-definitional** tension. | One level deeper; near-paradox | **highest** |
| **3** (`[tension-not-definitional]`, `[wall-loosened-not-fallen]`, `[recognizer-needs-mcsp]`) | Corrects Cycle 2 DOWNWARD: the constructivity-forcing (Williams Thm 1.1 via the Easy Witness Lemma) is **NEXP-specific**, absent for explicit f. The S1.a witness is explicit, not a nondeterministic class, so the forcing does NOT reach it. "Explicit g ⇒ recognizable" is false (recognizer must reject ALL easy = MCSP-complement). Wall reclassified from near-paradox to **requires a genuinely new LB method** — possible-in-principle, not theorem-blocked. | Reclassified, loosened | **lowest** |
| **4** (`[single-lb-implies-class-lb]`, `[williams-iff-vicinity]`, `[wall-pinned-to-targetability]`, `[targetability-circularity]`) | Closes Cycle 3's flagged caveat: g IS in NEXP (AC⁰-constructible ⊆ P ⊆ NEXP), so the single-function LB **entails** the class LB NEXP ⊄ size-T·AC⁰, and Williams' IFF (⇒) then **guarantees a recognizable property EXISTS in the vicinity**. Partially walks back Cycle 3 (forcing's *consequence* present where *mechanism* absent). Wall now pins to **(Q-targetability)**: does Williams' (⇒) accept the *specific* g or only a generic h? My flagged reasoning: retargeting onto g is circular (needs g's LB; a recognizable one collapses, a non-recognizable one can't retarget). | Pinned to one question | medium-low |

The trajectory is not monotone: Cycle 2 was the most pessimistic (near-definitional tension — possibly impossible), Cycle 3 the most optimistic (empirical, possible-in-principle, not theorem-blocked), Cycle 4 recovered *some* pessimism (vicinity-recognizability is guaranteed by Williams' IFF because g ∈ NEXP) but not all of it (the recognizable property is for a generic h, not necessarily g). **The net is a pinning, not a fall and not a proof of impossibility.**

## Did the wall move? — honest assessment `[wall-pinned-not-moved]`

**No breakthrough was made.** Under `[honest-ceiling]`: no P≠NP proof, no new circuit lower bound, no derandomization, no explicit witness constructed. The wall stands.

**But the wall's *locus* moved dramatically — from vague to precisely pinned:**
- Before the second loop: "the natural-proofs frontier, somewhere, governing the S1.a witness."
- After Cycle 1: located **exactly** in AC⁰; the two gates named (recognizability + tight-window).
- After Cycle 2: the recognizability gate shown **harder than natural proofs** (constructivity axis, strictly stronger than RR); triple conjunction.
- After Cycle 3: the hardness shown **empirical, not definitional**; the constructivity-forcing theorem does not reach explicit f; breakthrough shape certified possible-in-principle.
- After Cycle 4: the possibility-in-principle shown **conditional** on Williams' (⇒) not being retargetable onto the specific g; the wall pinned to that single question.

**The net movement is in PRECISION and CONDITIONALITY, not in the wall itself:**
1. The AC⁰ face is confirmed the **thinnest** face (LB-existence passed; the only face where an explicit exponential LB already exists).
2. The wall's two gates are **exactly characterized**: Gate 1 (recognizability) is pinned to (Q-targetability); Gate 2 (tight-window) remains an open explicit-construction problem (`[ac0-tight-window]`, unchanged across the loop).
3. The breakthrough shape — **a non-recognizable explicit-f tight-window AC⁰ LB** — is certified **possible-in-principle** (Cycle 3) **but now conditioned** (Cycle 4) on Williams' (⇒) not being retargetable onto g. So the second loop both *loosened* the wall (Cycle 3: not theorem-blocked) and then *re-conditioned* that loosening (Cycle 4: vicinity-recognizability is guaranteed; the loosening survives only if the guaranteed property is generic, not g-specific).

**This is the honest shape of the outcome:** the wall did not fall; it was not proven impossible; it was driven from a vague backdrop to a single, named, line-verifiable sub-question on which its status — and hence whether the AC⁰ face can yield the breakthrough — now turns.

## The single concrete next verification (the loop's actionable product)

Across four cycles the entire second loop's outcome converges to **one checkable question**:

> **(Q-targetability)** Is Williams' Theorem 1.1 (⇒) construction (class LB ⟹ recognizable useful property) **retargetable onto a specific chosen hard function f ∈ NEXP \ C** (taking f's hardness as a given input), or does it produce a recognizable property only for an **unspecified/generic** NEXP hard function h?

- **How to resolve:** read Williams 2016 ("Natural Proofs vs. Derandomization") §3 — the constructive proof of the (⇒) direction — and determine whether the recognizable property it builds can be parameterized by a chosen hard function, or only by the *assumption* (which supplies existence of *some* hard function).
- **If retargetable (onto g):** the wall RE-TIGHTENS — a recognizable property accepting the specific AC⁰-constructible tight-window g exists whenever the S1.a witness exists ⟹ Ilango collapse ⟹ the S1.a witness cannot be non-recognizable ⟹ Cycle 3's loosening is overturned; the AC⁰ face is blocked at Gate 1 by a (now-understood) theorem.
- **If generic only (h ≠ g):** the wall STAYS LOOSENED — the guaranteed recognizable property accepts a different function, unusable in the reduction; g's non-recognizable LB survives; the AC⁰ face's breakthrough shape (non-recognizable explicit-f tight-window AC⁰ LB) remains possible-in-principle, blocked only by the empirical absence of a method + Gate 2.

My flagged reasoning (the **circularity**: retargeting onto g requires g's LB, but a recognizable g-LB already collapses and a non-recognizable one cannot be the retargeting certificate) favors "generic only," i.e. the wall stays loosened — but this is reasoning from the search-level theorem statement, **not line-verified**, and resolving it is a single, bounded literature check.

This is the loop's genuine product: it converted a vague question ("is the non-natural explicit AC⁰ LB witness possible?") into a single, falsifiable, line-verifiable question (Williams' (⇒) targetability). Either answer advances the map — a re-tightening is itself a sharpening (the wall's mechanism understood), and a confirmed loosening keeps the AC⁰ face alive as the most-precisely-characterized live thread.

## The breakthrough shape, precisely conditioned

The second loop leaves the genuine breakthrough shape as:

> An **explicit, AC⁰-constructible function g**, in a **tight window** [(1−4δ)T, (1+4δ)T], with a **non-`(P/poly)`-recognizable** AC⁰ LB —
> certified **possible-in-principle** (Cycle 3: the constructivity-forcing theorem does not reach explicit f) **CONDITIONED** (Cycle 4) on Williams' (⇒) recognizable property being **generic (h ≠ g), not retargetable onto g** —
> blocked in practice by (i) the empirical absence of a non-recognizable explicit-f LB method (the natural-proofs frontier) and (ii) Gate 2 (the tight-window explicit construction, `[ac0-tight-window]`).

Compared to the first loop's framing ("an explicit lower-bound-carrying witness = the circuit-LB problem = natural-proofs frontier, open"), the second loop's contribution is that the *recognizability* sub-condition of this witness is now **exactly characterized** rather than assumed — its status is the (Q-targetability) question, not a vague "is it natural."

## Honest assessment of the two-loop arc

- **First loop:** confirmed `[witness-needs-explicit-lb]` from seven angles across both routes + three models; the wall is an open construction (conditional on OWFs), not a proven impossibility; the worst-case SAT route is blocked by a proven theorem (`[n2-wall]`), the average-case/mining route by an open construction (more promising); near-term de-conditioning ⟹ EXP≠ZPP-class, not P≠NP.
- **Second loop:** attacked the thinnest face (AC⁰/S1.a) directly; across four cycles drove the recognizability gate's status from vague → exactly-located → harder-than-natural-proofs → empirical-not-definitional → pinned-to-one-question. Surfaced one genuinely novel diagnostic (Cycle 2: Ilango's barrier is **strictly stronger than natural proofs** — the standard escape misses it because the gate is the constructivity axis, not largeness) and one precise re-conditioning (Cycle 4: g ∈ NEXP ⟹ the single-function LB entails the class LB ⟹ vicinity-recognizability is guaranteed). The AC⁰ face's two gates are now exactly characterized; the entire face's outcome hinges on (Q-targetability).

**The wall neither fell nor was proven impossible. It was driven from vague to precisely pinned. The deliverable is a sharper map + one concrete next verification, not a theorem.** `[honest-ceiling]`.

## What would actually constitute the breakthrough (unchanged, sharpened)

A single explicit construction producing a **non-recognizable explicit-f tight-window AC⁰ LB** (conditional on (Q-targetability) = generic-only) would fall the AC⁰ face and advance Route A. The two near-term *relaxations* remain the tractable seams: (meta-complexity) a structurally-different uniform-AC⁰ MCSP reduction (the compression crux, `[route-a-compression-crux]`); (Williams) Tell's promise/wire-count derandomization = the CSS16 wire frontier (`[tell-2018-quantified]`). Near-term de-conditioning still ⟹ EXP≠ZPP-class, NOT P≠NP. P≠NP still requires crossing the wall — now understood, for the AC⁰ face, to turn on (Q-targetability) + the tight-window explicit construction + the empirical non-recognizable-method gap.

## Honest scope `[honest-ceiling]`

- **No breakthrough.** No P≠NP proof, no new circuit LB, no derandomization, no explicit witness. The wall stands; the map is sharper.
- **Provenance.** All four cycles web-confirmed (search/arXiv-summary level). Only Cycle 1's Ilango §1.4 quotation is line-verified (against `_tr20-183.txt`). Williams Thm 1.1, CWY ITCS 2023, Dhayal-Impagliazzo 2020 are NOT PDF-line-verified.
- **The loop's pivotal claim — (Q-targetability) and the circularity reasoning — is FLAGGED, not verified.** It is the single most important thing to check next (Williams 2016 §3). If Williams' (⇒) is retargetable onto a chosen hard f, the circularity dissolves, Cycle 4 re-tightens, and the AC⁰ face is blocked at Gate 1 by a (now-understood) theorem rather than by an empirical gap.
- **The d-dependent threshold subtlety is FLAGGED.** Whether "NEXP ⊄ size-T·AC⁰_{d−1}" at the Lupanov window T is itself known vs open (parity may already witness it for small d) is not pinned; it affects whether the vicinity-recognizability (Cycle 4) is concrete (known) or conditional (open).
- **The oscillation itself is a methodological finding.** The recognizability gate's status is sensitive to a subtle logical point (g ∈ NEXP ⟹ single-function LB entails class LB) that is easy to miss; the loop's successive downward/upward corrections (Cycle 2→3→4) are a model of `[honest-ceiling]`-driven self-correction — each cycle tested the previous's central claim against the literature and corrected it. The map's reliability is itself the product: a claim that survived three rounds of adversarial self-test (Cycle 3's "empirical not definitional" survived Cycle 4's vicinity-recognizability test *as a conditional*, not as a blanket).

## Sources

- Cycle 1: `sources/2026-08-23-ac0-escape-hatch.md` (AC⁰ LB-existence passed; the recognizability + tight-window gates; Ilango §1.4 line-verified).
- Cycle 2: `sources/2026-08-23-recognizable-stronger-than-natural.md` (Ilango's barrier strictly stronger than RR; triple conjunction; near-definitional tension).
- Cycle 3: `sources/2026-08-23-tension-not-definitional.md` (tension empirical not definitional; constructivity-forcing NEXP-specific; reclassified, loosened).
- Cycle 4: `sources/2026-08-23-boundary-case-targetability.md` (g ∈ NEXP ⟹ class LB; vicinity-recognizability; pinned to Williams' (⇒) targetability).
- First loop synthesis: `sources/2026-08-23-five-cycle-synthesis.md` (seven angles on `[witness-needs-explicit-lb]`; the asymmetry: proven-theorem SAT route vs open-construction mining route).
- Williams, R. — "Natural Proofs versus Derandomization," SIAM J. Comput. 2016, Thm 1.1 (the IFF; the (⇒) direction whose constructive content is the loop's pivotal open question). [web-confirmed, NOT PDF-line-verified].