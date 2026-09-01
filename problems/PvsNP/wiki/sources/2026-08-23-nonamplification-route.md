# Cycle 3 — The non-amplification average-case route: CLOSED (the class drift is in the reconstruction machinery, not the XOR lemma) (Williams side)

**Date:** 2026-08-23
**Sub-target:** Cycle 3 of the 5-cycle loop. The second-pass [mining-worst-vs-average] obstruction named the "genuine open shape" as a *non-amplification* route to an explicit average-case-hard function for MAJ∘MAJ (avoiding the IW XOR-lemma amplification that drifts the predictor to XOR∘MAJ∘MAJ). This cycle tests that suggested opening: can a worst-case→average-case conversion that BYPASSES the XOR lemma (Sudan-Trevisan-Vadhan list-decoding; CRTY well-structured wc→ac) deliver average-case hardness for MAJ∘MAJ *without* class drift?
**Provenance (honest):** main-loop (no subagents — HTTP 429 persists); grounded by web search against STV (Sudan-Trevisan-Vadhan, STOC 1999 / JCSS 2001, [PDF](https://lucatrevisan.github.io/pubs/stv99stoc.pdf), [JCSS](https://dl.acm.org/doi/10.1006/jcss.2000.1730)); CRTY (Chen-Rothblum-Tell-Yogev, JACM 70(4) 2023, [DOI](https://doi.org/10.1145/3593581)); Goldreich-Rothblum 2019 (wc→ac for subclasses of P, [Weizmann](https://www.wisdom.weizmann.ac.il/~oded/COL2/wc2ac.pdf)). The reconstruction-class claim is a structural inference verified against STV's stated reconstruction machinery (multivariate polynomial encoding + Sudan univariate list-decoding + polynomial self-correction; and pairwise-independent XOR + Trevisan extractor); it is NOT a published theorem "STV fails for MAJ∘MAJ" — it is the verified observation that the machinery STV/CRTY use is arithmetic and thus exceeds MAJ∘MAJ.

---

## The verified negative result — the non-amplification route is blocked by the SAME class drift, via the reconstruction machinery

### What the non-amplification routes actually use (arithmetic, exceeding MAJ∘MAJ)

**STV "PRGs without the XOR Lemma" (two approaches, both arithmetic):**
- *Approach 1 (pseudoentropy + extractor):* a modified NW generator on a *mildly* hard predicate produces pseudoentropy; an extractor (Trevisan '98) converts it to pseudorandomness. The construction uses **pairwise-independent string generation via XOR with an expander-walk generator** — i.e., **XOR/parity machinery**.
- *Approach 2 (algebraic hardness amplification via list decoding):* encodes the hard function as a **multivariate low-degree polynomial**; the reconstruction uses **univariate list decoding (Sudan's algorithm) on random lines through F^m combined with self-correction of polynomials**. STV explicitly states the reconstruction's running time "determines the circuit class against which the hardness amplification works."

Both approaches' reconstruction circuits live in **(arithmetic / field-operation / parity) ∘ (predictor's class)**: polynomial encoding needs low-degree polynomial EVALUATION over a field (MOD_q / arithmetic gates); Sudan list-decoding needs polynomial root-finding; polynomial self-correction needs low-degree testing; pairwise-independent XOR needs XOR/parity. **None of these is in MAJ∘MAJ** — and this is not accidental: MAJ∘MAJ *lacks* parity (IP₂/parity ∉ MAJ∘MAJ is the HMPT lower bound [hmpt-1993], the very fact the mining program rests on). So applying STV to a MAJ∘MAJ predictor lifts the reconstruction class to **(parity/arithmetic) ∘ MAJ∘MAJ ⊋ MAJ∘MAJ** — a class drift, via the arithmetic decoder rather than a top XOR.

**CRTY (well-structured wc→ac):** the function `ws` is PSPACE-complete, downward-self-reducible, sample-aided wc→ac reducible (ρ = 2^{−n/polylog n}), TQBF→ws quasilinear blowup. The wc→ac reduction is **arithmetization-based** (Boolean→Arithmetic→Boolean, self-correction of low-degree polynomials) — the same arithmetic machinery. The average-case hardness CRTY obtains is for the **class in the assumption** (general circuits / the class ws is worst-case-hard for), NOT specifically MAJ∘MAJ; instantiating it for MAJ∘MAJ requires a MAJ∘MAJ worst-case anchor *and* the arithmetization lifts the predictor to (arithmetic) ∘ MAJ∘MAJ.

**Goldreich-Rothblum 2019 (corroborating):** wc→ac reductions are achieved for **uniform AC⁰[2]** (AC⁰ *with parity gates*) and for counting problems in P — i.e., for classes that **already contain parity/arithmetic**. They are *not* achieved for MAJ∘MAJ. This is exactly the pattern: the wc→ac machinery *needs* parity/arithmetic, so it works for classes that have it and drifts classes that lack it.

### The Cycle-3 finding — [non-amplification-also-class-drifts]

**[non-amplification-also-class-drifts] — bypassing the XOR lemma does NOT bypass the class drift.** The drift is **not specific to the IW XOR lemma**; it is a robust feature of every known worst-case→average-case conversion. The XOR lemma drifts the predictor to XOR∘MAJ∘MAJ (a top XOR); the XOR-lemma-free routes drift it to (arithmetic/parity)∘MAJ∘MAJ (a decoder/encoding layer). Either way the reconstruction circuit exceeds MAJ∘MAJ, defeating the NW class-relativity (the NW reconstruction must produce a circuit in the *same* class one is trying to fool). So the second-pass's "genuine open shape — a non-amplification route" is **closed**: avoiding amplification does not help, because the drift lives in the reconstruction step (encoding + decoding + self-correction), which is arithmetic and present in *both* the amplified and the amplification-free pipelines.

**The drift is robust because the decoder needs parity/polynomial operations, and MAJ∘MAJ provably lacks parity (HMPT).** This is the deeper content of the second-pass [mining-worst-vs-average]: the obstruction is not "amplification is lossy" (a fixable engineering issue) but "the reconstruction's decoder requires operations outside MAJ∘MAJ" (a structural feature tied to MAJ∘MAJ's inability to compute parity).

### What this reduces to (the genuine open shape, sharpened)

The non-amplification route reduces to the **same** open problem as Cycle 2: a **direct (non-reconstructive) exponential average-case-correlation LB for full-poly-size MAJ∘MAJ**. The only ways to avoid the class-drifting reconstruction are:
- (a) a function that is **directly** average-case hard for MAJ∘MAJ at exponential correlation (no conversion needed) — the Cycle-2 target; or
- (b) a **locally-list-decodable error-correcting code whose decoder lies in MAJ∘MAJ** (so the reconstruction stays within MAJ∘MAJ). Known locally-list-decodable codes decode via parity (Hadamard→Goldreich-Levin, needs inner-product/parity) or low-degree polynomial evaluation (multilinear→Sudan) — **both exceed MAJ∘MAJ**. A MAJ∘MAJ-decodable code is not known; it would itself be the breakthrough (and is essentially equivalent to a direct average-case LB, since decoding ≈ reconstructing the hard function).

So the non-amplification route offers no new lever beyond the Cycle-2 direct-LB target; it confirms the obstruction is at the **reconstruction/decoder level**, tied to MAJ∘MAJ's lack of parity.

---

## Honest status of the test (`[honest-ceiling]`)

I tested the second-pass's own suggested opening (the non-amplification route) against the primary sources (STV's two approaches; CRTY's arithmetization; Goldreich-Rothblum's parity-containing-class pattern) and **confirmed it is blocked** — not by the XOR lemma specifically, but by the arithmetic decoder/encoding that every known worst-case→average-case conversion uses, which exceeds MAJ∘MAJ. The seam **holds and is now strictly stronger**: the class drift is a robust, decoder-level feature (tied to MAJ∘MAJ's lack of parity), not an amplification-specific artifact that avoiding amplification would fix. No opening found; the genuine-open shape for a breakthrough remains the **direct** (non-reconstructive) exponential average-case-correlation LB for full-poly-size MAJ∘MAJ (Cycle 2), OR a MAJ∘MAJ-decodable locally-list-decodable code (equivalent). This is a verified *closure* of a suggested route, consistent with [witness-needs-explicit-lb]: the only escape is a directly-constructed average-case-hard MAJ∘MAJ function, which is the circuit-LB problem itself.

## Tags

`[non-amplification-also-class-drifts]` `[mining-worst-vs-average]` `[mining-nw-seam]` `[mining-gap-two-dimensional]` `[witness-needs-explicit-lb]` `[hmpt-1993]` `[stv-2001]` `[crty-2023]` `[goldreich-rothblum-2019]` `[css-2018]` `[chen-ren-2020]` `[honest-ceiling]`

## Sources
- STV — Sudan-Trevisan-Vadhan, "Pseudorandom Generators without the XOR Lemma," STOC 1999 / JCSS 62(2), 2001 ([PDF](https://lucatrevisan.github.io/pubs/stv99stoc.pdf), [JCSS](https://dl.acm.org/doi/10.1006/jcss.2000.1730)) `[stv-2001]` — two XOR-lemma-free approaches (pseudoentropy+extractor; algebraic list-decoding), both arithmetic.
- CRTY — Chen-Rothblum-Tell-Yogev, "On Exponential-Time Hypotheses, Derandomization, and Circuit Lower Bounds," JACM 70(4), 2023 ([DOI](https://doi.org/10.1145/3593581)) `[crty-2023]` — well-structured `ws`, arithmetization-based wc→ac, quasilinear blowup.
- Goldreich-Rothblum, "Worst-case to Average-case Reductions for Subclasses of P," 2019 ([Weizmann](https://www.wisdom.weizmann.ac.il/~oded/COL2/wc2ac.pdf)) `[goldreich-rothblum-2019]` — wc→ac for uniform AC⁰[2] (parity present) and counting-in-P; the parity-containing-class pattern.
- CSS16 — Chen-Santhanam-Srinivasan, ToC 2018 `[css-2018]` (prior pass) — the few-wire average-case frontier.
- HMPT — Hajnal-Maass-Pudlák-Szegedy-Turán, JCSS 1993 `[hmpt-1993]` — parity ∉ MAJ∘MAJ (the structural reason the decoder's parity machinery exceeds MAJ∘MAJ).