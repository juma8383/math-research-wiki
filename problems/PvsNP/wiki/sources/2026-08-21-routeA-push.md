# Source — MCSP Route A push (uniform-AC⁰ NP-hardness ⟹ P≠NP) (2026-08-21)

**Tags:** `[honest-ceiling]` `[route-a-route-b]` `[murray-williams-2017]` `[locality-barrier]` `[goldilocks-structure]` `[route-a-compression-crux]` `[route-a-variant-gap]` `[route-a-dual-locality]` `[route-a-owf-escape]` `[thesis-formal-vs-slogan]` `[mcsp-nphard-owf]` `[mazor-pass-2024]` `[ilango-2020]` `[choprs-2020]`

**Provenance (honest):** Main-loop research push (no subagent fan-out — the dispatching API account's session-usage limit, HTTP 429, hit during the prior `mcsp-deep-dive` fan-out, remains in effect; subagents unavailable). Grounded by web search against primary literature:
- Murray & Williams, *On the (Non) NP-Hardness of Computing Circuit Complexity*, ToC 13(4):1–22, 2017 (CCC 2015) ([10.4086/toc.2017.v013a004](https://doi.org/10.4086/toc.2017.v013a004); [ToC](https://www.theoryofcomputing.org/articles/v013a004/)).
- Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam, *Beyond Natural Proofs: Hardness Magnification and Locality*, ITCS 2020 / JACM 2022 ([10.1145/3538391](https://doi.org/10.1145/3538391); [ITCS pdf](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf)).
- Ilango, *Approaching MCSP from Above and Below* (ITCS 2020); *Constant Depth Formula and Partial Function Versions of MCSP are Hard* (FOCS 2020); *The Minimum Formula Size Problem is (ETH) Hard* (CCC 2020). ([ITCS 2020](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.34/LIPIcs.ITCS.2020.34.pdf); [FOCS 2020](https://www.rahulilango.com/papers/FOCS2020.pdf); [MFSP](https://www.rahulilango.com/papers/MFSP-hard.pdf)).
- Mazor & Pass, *Gap MCSP Is Not (Levin) NP-Complete in Obfustopia*, CCC 2024 ([10.4230/LIPIcs.CCC.2024.36](https://doi.org/10.4230/lipics.ccc.2024.36)).
- Hirahara–Oliveira–Santhanam, (DNF∘XOR)-MCSP NP-hardness, CCC 2018.

No proof of P≠NP, no NP-hardness reduction, and no lower bound is claimed. The product is a **sharpened, falsifiable map** of the single most direct P≠NP bridge, with the compression crux and a concrete next sub-target made explicit. `[honest-ceiling]` upheld.

---

## The target — Route A, stated precisely `[route-a-route-b]`

**Route A:** prove that **MCSP is NP-hard under logtime-uniform AC⁰ many-one reductions** — i.e. exhibit a logtime-uniform AC⁰ circuit family `R` mapping a SAT instance `φ` (size `n`) to an MCSP instance `(T, k)` such that `φ ∈ SAT ⟺ MCSP(T, k)`.

**The implication (Murray–Williams 2017, Theorem 1.8) `[murray-williams-2017]`:** if such a reduction exists, then **NP ⊄ P/poly**, **E ⊄ i.o.-SIZE(2^{δn})** for some δ>0, and **P = BPP**. Since NP ⊄ P/poly ⟹ NP ⊄ P (else NP ⊆ P ⊆ P/poly) ⟹ **P ≠ NP**.

**So Route A is the only one of the two formal MCSP→separation bridges whose success yields P≠NP outright** (route B, hardness magnification, yields class containments like NP ⊄ NC¹ under stronger-magnitude LBs, blocked by `[locality-barrier]`). It is, by construction, the highest-upside target in the entire portfolio.

---

## The Goldilocks zone — why this exact reduction class `[goldilocks-structure]`

Murray–Williams locate a precise ladder of reduction strengths, where each rung is "too weak / just right / too strong":

| Reduction class for NP-hardness of MCSP | Consequence | Status |
|---|---|---|
| `TIME(n^{1/2−ε})` local / projection (Thm 1.3); randomized `TIME(n^{1/5−ε})` (Thm 1.5) | — | **Provably impossible** — no such reduction exists |
| **logtime-uniform AC⁰ (Thm 1.8)** | **NP ⊄ P/poly ⟹ P≠NP**; E ⊄ SIZE(2^{δn}); P=BPP | **Open — the Goldilocks target** |
| logspace (Thm 1.7) | PSPACE ≠ ZPP | Open (stronger) |
| polynomial-time (Thm 1.6) | EXP ≠ NP∩P/poly ⟹ EXP ≠ ZPP | Open (strongest); also triggers `[mcsp-nphard-owf]` |

The local rung is *too weak* (proven unable to make MCSP NP-hard). The polytime rung is *too strong* (its existence would already separate EXP from ZPP and, via the OWF obstruction `[mcsp-nphard-owf]`, rule out one-way functions). **Uniform-AC⁰ is the rung that is weak enough to plausibly exist yet strong enough that its existence is a P≠NP theorem.** This is the Goldilocks zone in its sharpest form `[goldilocks-structure]`.

---

## The compression crux `[route-a-compression-crux]`

Why is constructing the reduction hard at all? Pin the exact technical heart:

A uniform-AC⁰ reduction `R` runs in `poly(n)` time and outputs an MCSP instance `(T, k)` of length `poly(n)`. The truth table `T` has length `N = poly(n)`, so it is the truth table of a function `f_φ` on **`m = log N = O(log n)` bits**. Therefore the reduction must encode the `n`-bit satisfiability of `φ` into the **circuit complexity (≤ k vs > k) of a function on only `O(log n)` bits**.

This is a **massive information-theoretic compression**: the yes/no-ness of an arbitrary SAT instance of size `n` must be encoded into a single `O(log n)`-bit function's circuit complexity, by a constant-depth poly-size circuit family that *does not know the answer*.

- **Why local reductions provably fail (Murray–Williams Thm 1.3):** a local/projection reduction outputs a truth table whose entries are locally-computable functions of few input bits; such truth tables are structurally simple, and the Murray–Williams argument bounds `k` and then assembles small AC⁰ circuits for PARITY, contradicting Håstad. The "hard" side (φ ∉ SAT ⟹ f_φ needs > k) cannot be realized because the construction is too local to inject hardness.
- **The crux:** a uniform-AC⁰ reduction must be *global enough* (constant-depth poly-size, can compute non-local functions of all `n` bits — except PARITY) to inject a satisfiability-conditional complexity gap into an `O(log n)`-bit function, yet still be an AC⁰ circuit. This is the precise open construction.

Honest status: **no construction is known, and constructing it is at least as hard as proving NP ⊄ P/poly** (because the reduction's existence *implies* NP ⊄ P/poly, Murray–Williams Thm 1.8). So a full construction of Route A IS the breakthrough, not a step toward it. I do not claim to construct it.

---

## The variant gap `[route-a-variant-gap]`

A concrete, surveyable diagnostic: **how close are the achieved NP-hardness results for MCSP variants to the uniform-AC⁰-many-one-to-original-MCSP target?**

| Problem | Reduction class | vs Route A target |
|---|---|---|
| DNF-MCSP (Masek 1979) | deterministic polytime | restricted circuit class; polytime (too strong) |
| (DNF∘XOR)-MCSP (Hirahara–Oliveira–Santhanam 2018) | deterministic polytime | restricted class; polytime |
| MOCSP / oracle-MCSP (Ilango ITCS 2020) | **randomized** RP/ZPP | different problem (extra oracle input); randomized |
| Multi-output MCSP (Ilango–Loff–Oliveira CCC 2020) | randomized | different problem; randomized |
| **(AC⁰_d)-MCSP (Ilango FOCS 2020)** | **randomized quasipoly-time Turing** | restricted circuit class; **closest** to Route A |
| Partial MCSP / MCSP? (Ilango FOCS 2020) | "not in P under ETH" (Turing) | conditional, partial functions |
| MFSP (Ilango CCC 2020) | "not in P under ETH"; polytime search-to-decision | different problem (formulas) |
| Gap-MCSP / Gap-MKTP poly-gap (Mazor–Pass CCC 2024) | **NOT NP-complete under Levin reductions** (assuming iO) `[mazor-pass-2024]` | negative, conditional |
| **Original MCSP** | **OPEN** | the target |

**The honest finding `[route-a-variant-gap]`: NO variant of MCSP is known NP-hard under uniform-AC⁰ many-one reductions.** Every achieved NP-hardness is for a *restricted-circuit-class / oracle / partial / formula* variant, and uses reductions that are *randomized*, *Turing (not many-one)*, *quasipoly/poly-time (not AC⁰)*. The closest result to Route A — Ilango's `(AC⁰_d)-MCSP` NP-hardness — is still randomized, quasipoly-time, and Turing, for a restricted-circuit-class variant. So the exact Route A reduction class (uniform-AC⁰, many-one, original MCSP) is not merely open for original MCSP; it is open even for the restricted variants. This is a sharper and more actionable statement of the gap than "MCSP NP-completeness is open."

---

## The dual role of the locality barrier `[route-a-dual-locality]`

The `[locality-barrier]` (CHOPRS ITCS 2020 / JACM 2022) is recorded in the wiki as blocking **route B** (hardness magnification / the LB-proving side): magnification theorems unconditionally produce target problems (parameterized MCSP variants) with efficient **small-fan-in oracle circuits**, and all known LB techniques (Razborov–Smolensky, Tal shrinkage, random restrictions) *extend* to such oracle circuits — so those techniques cannot prove the magnified LB (HM Frontiers A–E; e.g. Frontier C: `MCSP[2^{√n}/10n, 2^{√n}]` ∉ Almost-Formula ⟹ NP ⊄ NC¹).

**This push surfaces that the locality barrier is dual — it touches Route A's reduction side too, not only route B's LB side:**
- *LB side (route B):* the techniques that would prove the magnified LB localize → blocked.
- *Reduction side (route A):* the *natural* way to build the satisfiability-conditional complexity gap (the compression crux) is precisely a magnification-style construction, and CHOPRS show such constructions unconditionally produce small-fan-in-oracle circuits for the target. So the "easy-if-satisfiable / hard-if-unsatisfiable" gap that a Route A reduction needs is exactly the kind of construction whose "hard" side cannot be certified by known LB techniques (they extend to the oracle circuits the construction itself produces).

The one crack: **CHOPRS Theorem 49** (Thm 50 in the JACM version) exhibits a **non-localizable** lower bound — a language `L ∈ E` with `L ∉ GapAND_{O(N)}-Formula[N^{3−ε}]` yet `L ∈ O_{N^{o(1)}}-Formula[N²]` (an Andreev-like function): a LB *above* the magnification threshold that does NOT extend to small-fan-in oracles. This proves non-localizable LBs *can* exist in principle. But Thm 49 is for an Andreev-like function, **not for MCSP or any meta-computational problem**. Finding a non-localizable LB for MCSP (route B) — or a non-localizable gap construction feeding a Route A reduction — remains open.

`[route-a-dual-locality]`: the locality barrier is the common obstruction under both formal bridges; Route A is not a "locality-free" escape from route B.

---

## A point in Route A's favor — OWF-escape `[route-a-owf-escape]`

The Goldilocks framing gives Route A one genuine advantage that is worth stating sharply. The obstructions that block the **strong** reduction rungs do not obviously block the **weak** uniform-AC⁰ rung:
- The OWF obstruction `[mcsp-nphard-owf]` (Liu–Pass / Ren–Santhanam / Allender–Das family) targets reductions strong enough to be "natural" — i.e. **polynomial-time** reductions. Uniform-AC⁰ reductions are far weaker and are not known to be "natural" in the Razborov–Rudich sense; the OWF obstruction is not known to extend to them.
- The Mazor–Pass negative `[mazor-pass-2024]` is for **Levin (witness-preserving) reductions** on **gap** variants under iO — a different reduction class and a gap problem, not uniform-AC⁰ many-one on exact MCSP.

So `[route-a-owf-escape]`: **Route A is plausibly *below* both the OWF obstruction and the natural-proofs net**, while still being *strong enough* to imply NP ⊄ P/poly. The thing that blocks Route A is the `[locality-barrier]` / the compression crux, NOT the crypto obstructions that block the strong rungs. This is a sharpened, honest diagnosis of *where* Route A's resistance lives — it is structural (locality/compression), not cryptographic.

---

## Net honest outcome

1. **Route A is the single highest-upside P≠NP bridge in the portfolio**, precisely characterized: NP-hardness of MCSP under logtime-uniform AC⁰ many-one reductions ⟹ NP ⊄ P/poly ⟹ P≠NP (Murray–Williams Thm 1.8 `[murray-williams-2017]`), sitting in the sharpest Goldilocks zone `[goldilocks-structure]` (local reductions proven impossible Thm 1.3/1.5; polytime ⟹ EXP≠ZPP Thm 1.6).
2. **The compression crux `[route-a-compression-crux]`** is the exact heart: encode `n`-bit SAT-satisfiability into the circuit complexity of an `O(log n)`-bit function via a uniform-AC⁰ family. A full construction is *at least as hard as* NP ⊄ P/poly — i.e. it is the breakthrough itself, not a step toward it. **Not constructed; not claimed.**
3. **The variant gap `[route-a-variant-gap]`**: no MCSP variant is known NP-hard under uniform-AC⁰ many-one reductions; the closest result (Ilango's `(AC⁰_d)-MCSP`) is randomized + quasipoly-time + Turing + restricted-class. The exact Route A reduction class is open even for the restricted variants — a sharper statement of the gap than "MCSP NP-completeness is open."
4. **The locality barrier is dual `[route-a-dual-locality]`**: it blocks route B (LB-proving) AND touches Route A (the natural gap-constructions produce the very oracle circuits that defeat the LB techniques). The Thm 49 non-localizable crack proves non-localizable LBs *can* exist, but not yet for MCSP. Route A is not a locality-free escape.
5. **Route A plausibly escapes the crypto obstructions `[route-a-owf-escape]`**: the OWF obstruction `[mcsp-nphard-owf]` and the Mazor–Pass Levin negative `[mazor-pass-2024]` target *strong* (polytime/Levin/gap) reductions; uniform-AC⁰ many-one on exact MCSP is below both. Route A's resistance is structural (locality/compression), not cryptographic — a sharpened diagnosis of where the difficulty lives.

**Concrete falsifiable next sub-targets (tractable to attack, not solved here):**
- **(S1)** Derandomize Ilango's `(AC⁰_d)-MCSP` randomized quasipoly Turing reduction → a *deterministic* reduction (the [mcsp-gap] derandomization axis, restricted-class). Bounded, concrete.
- **(S2)** Convert a known restricted-variant many-one NP-hardness (e.g. DNF-MCSP, Masek 1979) toward uniform-AC⁰ by analyzing its reduction's actual depth/uniformity — does the Masek reduction already sit in a weak class? (Survey-grade, tractable.)
- **(S3)** Port CHOPRS Thm 49's non-localizable construction to a meta-computational problem (MCSP/parameterized MCSP) — would crack route B's locality wall and, by the duality `[route-a-dual-locality]`, inform Route A's gap construction. Hardest; highest leverage.

These are falsifiable open sub-questions, not results.

### Unverified / flagged for pre-publication check
- The exact uniformity condition in Murray–Williams Thm 1.8 ("logtime-uniform AC⁰") and whether later work sharpened the uniformity to DLOGTIME-uniform vs logtime-uniform — quoted from the search summary; verify the precise uniformity class.
- Whether the OWF obstruction `[mcsp-nphard-owf]` has been formally *shown* not to extend to uniform-AC⁰ reductions, or whether this is merely "not known to extend" — `[route-a-owf-escape]` is the honest "not known to extend" claim, flagged; it is not a proven escape.
- The HM Frontier C parameterization (`MCSP[2^{√n}/10n, 2^{√n}]` Almost-Formula ⟹ NP ⊄ NC¹) — quoted from the search summary; verify exact parameters.
- Ilango's `(AC⁰_d)-MCSP` reduction: "randomized quasipolynomial-time Turing" — verify it is Turing (not many-one) and quasipoly (not poly); this determines the exact (S1) gap.

### What changed vs the mcsp-deep-dive / wiki
- The wiki recorded route A/B as "the only two formal P≠NP bridges" `[route-a-route-b]` but did not state the **compression crux**, the **variant gap**, the **dual locality**, or the **OWF-escape**. This push sharpens all four: it pins *why* Route A is hard (compression), *how far* the achieved reductions are (variant gap table), *that* the locality barrier is the common obstruction (duality), and *that* the crypto obstructions plausibly do not block this rung (OWF-escape). It also names three concrete falsifiable sub-targets (S1–S3).
- Net honest result: a higher-resolution map of the highest-upside P≠NP bridge, with the resistance located (structural, not cryptographic) and a tractable next sub-target (S1, the derandomization of Ilango's restricted-class reduction) identified. **No reduction built; no P≠NP claimed; `[honest-ceiling]` upheld.**