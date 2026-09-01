---
title: "Cycle 2 (2nd loop) — Ilango's (P/poly)-recognizable barrier is strictly stronger than Razborov-Rudich: Williams' non-natural method is still caught"
date: 2026-08-23
cycle: 2
loop: 2
tags: [honest-ceiling, witness-needs-explicit-lb, ac0-natural-proofs-wall, ppoly-recognizable, ac0-tight-window, ac0-lb-existence-passed, recognizable-stronger-than-natural, williams-constructive-theorem, largeness-vs-constructivity, triple-conjunction-wall, williams-algorithmic, second-loop-cycle-1]
---

# Cycle 2 (2nd loop) — Ilango's barrier is stronger than natural proofs; Williams is still caught

Cycle 1 (`sources/2026-08-23-ac0-escape-hatch.md`) located the AC⁰ face's blocking gate as the **natural-proofs/(P/poly)-recognizability gate**: the `(AC⁰_d)`-MCSP reduction needs a **non-(P/poly)-recognizable** explicit exponential AC⁰ LB. The natural next question for a breakthrough attempt: **is there any known *non-natural* LB method that crosses this gate?** The obvious exemplar is **Williams' algorithmic method** (NEXP ⊄ ACC⁰, JACM 2011/2013) — the canonical LB widely held to *evade* the natural-proofs barrier. This cycle asks whether Williams' method can supply the S1.a witness. **Answer (verified against the literature): no — and the reason reveals that Ilango's (P/poly)-recognizable barrier is *strictly stronger* than the Razborov-Rudich natural-proofs barrier.** `[honest-ceiling]` upheld: no breakthrough; the wall is characterized more sharply, and the one known "escape" from natural proofs is shown to be the wrong escape for the MCSP-reduction witness.

## The key distinction: largeness vs constructivity `[largeness-vs-constructivity]`

The Razborov-Rudich (RR) natural-proofs barrier has **three** conditions on a "natural" property: **constructivity** (computable in P/poly), **largeness** (holds for a large fraction of functions), and **usefulness** (distinguishes hard from easy functions for the target class). To *evade* RR it suffices to drop ANY ONE — and the crypto-breaking consequence (no OWFs) needs all three.

**Ilango's (P/poly)-recognizable condition (TR20-183 §1.4, lines 565-568) requires only constructivity + usefulness, NOT largeness:** a collection S of LB statements is (P/poly)-recognizable if a poly-size circuit family *accepts all elements of S and rejects all YES-instances of (C)-MCSP* (the easy functions). There is **no largeness requirement** — S need not contain a large fraction of functions.

`[recognizable-stronger-than-natural]`: **Ilango's barrier is strictly stronger than RR for the MCSP-reduction-witness setting.** RR is evaded by dropping largeness; Ilango's barrier does not *have* a largeness condition to drop. So the standard "escape from natural proofs" (drop largeness) is the **wrong escape** — it leaves constructivity intact, and constructivity is exactly what Ilango's barrier forbids.

## Williams' method is non-natural by dropping LARGENESS, but is still (P/poly)-recognizable `[williams-constructive-theorem]`

**Verified (Williams, "Natural Proofs vs. Derandomization," SIAM J. Comput. 2016 — web-confirmed):**
- **Theorem 1.1 (Williams 2016):** For all "typical" circuit classes C (including ACC⁰), **NEXP ⊄ C if and only if there is a polynomial-time computable property useful against C (with O(log n) advice).** "Constructivity is unavoidable even for NEXP lower bounds — every NEXP lower bound must exhibit some constructive useful property."
- The NEXP ⊄ ACC⁰ proof is **not P-natural** because it **lacks largeness**: the extracted property "does not accept a large fraction of strings." The constructivity is present; largeness is absent. It evades RR by dropping largeness.

**The "O(log n) advice" makes it (P/poly)-recognizable.** A P-time property with O(log n) advice *is* a P/poly-computable property (the advice is the non-uniformity). So Williams' Theorem 1.1 says: **every NEXP LB (including Williams' own NEXP ⊄ ACC⁰) yields a (P/poly)-recognizable useful property.** Williams' method is constructive ⇒ (P/poly)-recognizable.

`[williams-constructive-theorem]` `[ppoly-recognizable]`: **Williams' canonical "non-natural" LB is still (P/poly)-recognizable** (it evades RR by dropping largeness, NOT constructivity). Therefore, *if Williams' method were used to certify the witness g's LB in the `(AC⁰_d)`-MCSP reduction*, the LB collection would be (P/poly)-recognizable, and Ilango's §1.4 consequence would fire: algorithmizing it yields **SAT ∈ subexp-circuits — a collapse, the opposite of Route A's separation target**. So Williams' method is **ruled out as the reduction's witness**, exactly as the switching-lemma LBs (Sipser/RST) were in Cycle 1. The one celebrated "natural-proofs-evading" LB does not cross Ilango's gate, because it evades the wrong condition.

This is the cycle's central finding: **the escape from Razborov-Rudich (drop largeness, as Williams does) is *not* an escape from Ilango's (P/poly)-recognizable barrier (which needs only constructivity). To cross the AC⁰ face's gate one must drop *constructivity* — i.e. produce a genuinely non-constructive LB.**

## The wall is a triple conjunction; non-recognizable ↔ non-constructive is in tension `[triple-conjunction-wall]`

Combining Cycle 1 + Cycle 2, the S1.a witness must satisfy **three** conditions simultaneously:

1. **Non-(P/poly)-recognizable** (Gate 1, `[ac0-natural-proofs-wall]`): the LB method's certified collection must not be recognizable by small circuits (else SAT ∈ subexp).
2. **AC⁰-constructible explicit g** (constructibility): the hard function must be specifiable/constructible *within the reduction* (an AC⁰ many-one reduction cannot compute an NEXP function).
3. **Tight-window / fine-grained** (Gate 2, `[ac0-tight-window]`): the LB must pin g's AC⁰_{d-1} complexity in [(1−4δ)T,(1+4δ)T] for each T — a complexity cliff, not just "high."

The known LB methods split, and **no method achieves even the first two simultaneously**:

| Method | Gate 1 (non-recognizable) | constructible g | Gate 2 (tight-window) |
|---|---|---|---|
| **Switching lemma** (Sipser/RST, parity) | ✗ (constructive ⇒ recognizable) | ✓ (explicit) | ✓ (tight-ish: parity 2^{Θ(n^{1/(d-1)})}) |
| **Williams' algorithmic method** (NEXP⊄ACC⁰) | ✗ (Theorem 1.1 ⇒ recognizable) | ✗ (hard f ∈ NEXP, not AC⁰-constructible) | ✗ (coarse: superpoly / 2^{n^δ}, not tight) |
| **Counting argument** (most functions hard) | ✓ (non-constructive ⇒ not recognizable) | ✗ (no explicit f) | ✗ (coarse) |

`[triple-conjunction-wall]`: the three requirements are in a **three-way tension**, and crucially **Gate 1 (non-recognizable) and constructibility are in direct, near-definitional tension**: a non-(P/poly)-recognizable LB method is necessarily *non-constructive* (a constructive method, by Williams' Theorem 1.1's spirit, yields a recognizable property) — but a non-constructive method (counting) gives **no explicit witness**. The S1.a witness demands a method that is simultaneously **non-constructive (to pass Gate 1) AND constructive-of-an-explicit-g (to be reduction-usable)** — a method that produces an explicit witness whose LB is certified non-constructively.

## Honest scope `[honest-ceiling]`

- **No breakthrough.** No P≠NP, no new LB, no MCSP NP-hardness. The wall stands, now characterized as a triple conjunction with an identified tension.
- **The "non-recognizable ↔ non-constructive" tension is a HEURISTIC, not a theorem.** Williams' Theorem 1.1 establishes the constructivity↔recognizability equivalence *for NEXP-class hard functions* (and E^NP). The S1.a witness g is a **polytime-explicit** function (weaker than NEXP), so Theorem 1.1 does **not** directly prove that an explicit-g LB is necessarily recognizable. The tension is: (a) the only known *non*-recognizable methods (counting) are non-constructive; (b) the known constructive methods (switching lemma, Williams) are recognizable. Whether an explicit, AC⁰-constructible g with a *non*-recognizable LB can exist is itself **open** — it is the precise genuine-open shape. The equivalence may simply not cover the explicit-f regime, leaving room. Stating the tension as "near-definitional" is the honest upper bound; it is not proven that non-recognizable + explicit are incompatible.
- **Williams' method ruled out for the reduction — verified at the theorem level, flagged at the application level.** Theorem 1.1 (recognizability of NEXP LBs) is web-confirmed from Williams 2016 (search-summary-level, not PDF-line-verified); the inference "Williams' method used for g would be recognizable ⇒ ruled out" applies Theorem 1.1's *spirit* (constructive methods yield recognizable LBs) to an explicit-f setting Theorem 1.1 does not literally cover. Flagged: the *direct* statement (NEXP LBs are recognizable) is solid; the *application* (Williams'-style method for explicit g is recognizable) is a strong inference.
- **The "stronger than RR" claim** (`[recognizable-stronger-than-natural]`) is a clean logical observation: RR = {constructivity ∧ largeness ∧ usefulness}; Ilango = {constructivity ∧ usefulness}; Ilango ⊆ RR's conditions, so evading RR (dropping largeness) does not evade Ilango. This is a logical relationship, not a new theorem, and is sound.
- **Gate 2 (tight-window) interacts with the tension.** Even setting Gate 1 aside, tight-window LBs (Gate 2) come only from the switching lemma (recognizable) — Williams gives coarse LBs. So a non-recognizable method would *additionally* need to be fine-grained, which the non-constructive methods (counting) are not. The triple is genuinely hard on every face.

## Net

Cycle 2 sharpens the AC⁰ face of `[witness-needs-explicit-lb]` into a **triple conjunction** {non-(P/poly)-recognizable, AC⁰-constructible, tight-window}, and identifies the central tension: **the non-recognizable gate (dropping constructivity) and the constructibility requirement are in near-definitional conflict** — non-constructive methods give no explicit witness; constructive methods (including Williams' celebrated natural-proofs-evading method, per Theorem 1.1) are recognizable and hence ruled out. The escape from Razborov-Rudich (drop largeness) is the **wrong escape** for Ilango's barrier (which needs only constructivity). The genuine-open shape is now maximally precise: **an explicit, AC⁰-constructible function g with a non-(P/poly)-recognizable tight-window AC⁰ LB** — where whether "non-recognizable" and "explicit-constructible" are even simultaneously achievable is itself open (Theorem 1.1 makes them equivalent for NEXP, hinting at tension, but the explicit-f regime is uncovered). No breakthrough; the wall is one level deeper and its inner tension is named. Cycles 3–5 should either (a) test whether the non-recognizable↔constructible tension is a real incompatibility or merely an artifact of known methods (the genuine breakthrough would be a non-recognizable explicit-f LB), or (b) revisit the Williams/mining face for whether the same triple-conjunction (or its analog) governs there.

## Sources
- sources/2026-08-23-ac0-escape-hatch.md (Cycle 1 — located the (P/poly)-recognizability gate)
- sources/_tr20-183.txt (Ilango FOCS 2020 §1.4 — the (P/poly)-recognizable definition, lines 565-568; the barrier needs constructivity+usefulness, no largeness)
- Williams, "Non-Uniform ACC Circuit Lower Bounds," JACM 61(1) 2014 (NEXP ⊄ ACC⁰; the algorithmic method; E^NP exponential 2^{n^δ})
- Williams, "Natural Proofs vs. Derandomization," SIAM J. Comput. 45(2) 2016 — **Theorem 1.1** (NEXP ⊄ C ⟺ P-time useful property with O(log n) advice; constructivity unavoidable; NEXP ⊄ ACC⁰ is non-natural by lacking *largeness*) — web-confirmed (search-summary-level)
- sources/2026-08-23-five-cycle-synthesis.md (the wall this cycle deepens)