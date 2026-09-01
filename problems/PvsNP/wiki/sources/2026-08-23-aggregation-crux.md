---
title: "Cycle 4 — The aggregation crux: why HMPT worst-case cannot become average-case (one level deeper than the decoder drift)"
date: 2026-08-23
cycle: 4
tags: [avg-worst-2x2-cell, threshold-aggregation-obstruction, cllo-2021, kumar-2023, mining-worst-vs-average, mining-nw-seam, witness-needs-explicit-lb, hmpt-1993, honest-ceiling]
---

# Cycle 4 — The aggregation crux

**Adaptive choice (honest).** Cycles 1–3 each confirmed/extended `[witness-needs-explicit-lb]` from a different angle (S3 locality-orthogonality; the two-dimensional wire frontier; the decoder-level class drift). A rough *first-principles* calculation (mine, initially unverified) appeared to contradict the Cycle-2 conclusion: applying "agreement of f with a threshold of s low-discrepancy functions ≤ O(s · disc(f))" with disc(IP₂) = 2^{−n/2} gave, at *polynomial* size s = poly(n), agreement ≤ poly(n)·2^{−n/2} = 2^{−Ω(n)} — i.e. an **exponential** average-case-correlation bound for **full-poly-size** MAJ∘MAJ, *exactly the mining target* (Cycle 2's open shape). If true, this would already yield the MAJ∘MAJ CAPP ⟹ NEXP ⊄ THR∘THR + TC⁰₃ (Chen-Ren). A result of that magnitude contradicts the field's "within reach, not done" status. Under `[honest-ceiling]`, this contradiction demanded resolution against primary sources rather than assertion. **Resolved: the opening is illusory; the calc mis-identifies the lifting step. The verified reason is one level deeper than Cycle 3's "decoder drift" and explains precisely why the calc fails.**

## 1. The HMPT toolchain, decomposed against the primary source

HMPT (Hajnal-Maass-Pudlák-Szegedy-Turán, JCSS 1993 `[hmpt-1993]`) is built from two lemmas, not one:

- **Lindsey's Lemma (HMPT Lemma 3.4):** the correlation of any *single* threshold gate (depth 1) with IP₂ is ≤ O(weight · 2^{−n/2}) (Hadamard structure). This **is** an average-case (correlation) statement — but at **depth 1 only**.
- **The Discriminator Lemma (HMPT Lemma 3.3):** if a depth-2 circuit T_k^a(C₁,…,C_m) **accepts all of A and rejects all of B** (disjoint sets; worst-case correctness), then some single subcircuit C_i is an ε-discriminator with ε ≥ 1/a. This is the **lifting** step — and it is **worst-case** (exact acceptance/rejection of A vs B).

So HMPT = Lindsey (avg-case, depth-1) **lifted by a worst-case lemma** (Discriminator) to a **worst-case** size LB for depth 2. The exponential strength is purchased at the *worst-case* lifting, *not* carried into an average-case depth-2 correlation. **There is no worst-case→average-case lifting step in the toolchain.** This is the precise, primary-source-verified reason HMPT does not yield the mining target — sharper than Cycle 2's "discrepancy is the wrong object."

## 2. The 2×2 grid: the mining target is the uncovered cell `[avg-worst-2x2-cell]`

The two known lemmas populate three cells of a (avg-case / worst-case) × (class C / MAJ∘C) grid:

|                  | against **C** (depth 1) | against **MAJ∘C** (depth 2) |
|------------------|:-----------------------:|:---------------------------:|
| **worst-case**    | —                       | HMPT ✓ (Discriminator lifts avg(C)→worst(MAJ∘C)) |
| **average-case**  | Lindsey ✓               | **??? — the mining target** |

- **Discriminator Lemma (HMPT):** avg-case-hard(C) ⟹ worst-case-hard(MAJ∘C). Goes **left→right, top row only** (it ends in worst-case MAJ∘C, not average-case MAJ∘C).
- **CLLO21 converse** (Chen-Lu-Lyu-Oliveira, "Majority vs. Approximate Linear Sum and Average-Case Complexity Below NC¹," 2021 `[cllo-2021]`, Thm 1): for C ⊆ NC¹ closed under negations with bottom O(1)-juntas, worst-case-hard(MAJ∘C) ⟺ **strong avg-case-hard(C)**. This is a genuine *converse* to the Discriminator Lemma — but it returns to **avg-case against C** (the bottom class), **not** avg-case against MAJ∘C. With C = depth-1 threshold, it recovers Lindsey (circular), not the mining target.

**Neither lemma touches avg-case-against-MAJ∘C.** The mining target — an exponential average-case-correlation LB for full-poly-size **MAJ∘MAJ** = avg-case(MAJ∘C) with C = depth-1 — is exactly the uncovered fourth cell. The opening my rough calc "found" was the false assertion that this cell is reachable by a linear "threshold of low-discrepancy ≤ O(s·disc)" bound; it is not, and the grid shows *why structurally*: the only known lifting tools pass *through* worst-case(MAJ∘C) or *back to* avg-case(C), never landing in avg-case(MAJ∘C).

## 3. Why no linear bound reaches the cell: the top threshold is a nonlinear aggregator `[threshold-aggregation-obstruction]`

The deeper reason the cell is uncovered — and the precise failure of my O(s·disc) calc — is the **aggregation power of the top threshold**:

- **Low per-gate correlation does NOT bound majority correlation.** A threshold (MAJ) of functions each weakly correlated with f can be strongly correlated with f — this is exactly **boosting** (a majority/weighted-threshold of weak learners yields a strong learner). CLLO21 `[cllo-2021]` formalizes the gap between MAJ∘C and C via **SUM] (Approximate-Linear-Sum) gates**: MAJ simulates SUM] but not conversely (MAJ has approximate degree Ω(m); SUM] is weaker), and this gap *is* "low correlation against individual gates (or simple circuits) does not bound majority correlation." Standard black-box hardness amplification (XOR lemma, direct product) **fails for classes not closed under majority** — and C = depth-1 threshold is NOT closed under majority (MAJ∘C is depth-2). So the aggregation obstruction is *robust and structural*, not an artifact of the discrepancy object.
- **Concrete demonstration (Kumar, CCC 2023 `[kumar-2023]`):** generalized AC⁰ with biased threshold gates GC⁰(k) has a **sharp threshold** in k — for k = Ω(n^{1/d}) exponential LBs against parity hold (low per-gate correlation), but for slightly larger k, **sublinear-size** circuits *compute parity exactly*. I.e., small-bias threshold gates that are *individually* uncorrelated with parity can, under majority aggregation, compute it. This is a positive instance of the very obstruction: aggregation crosses from "no correlation" to "exact computation" by enlarging the bias parameter.
- **Reconciling my rough calc.** The calc treated the bottom MAJ gates as 2-party communication *rectangles* (rank-1) and applied discrepancy. But MAJ∘MAJ's bottom gates are **LTFs**, not rectangles (richer), AND — more fundamentally — even a "threshold of low-discrepancy rectangles" bound would require the top threshold to act as a *linear* weighted sum bounded by discrepancy. GHR92's correlation lemma (TH_H(f) ≤ 1/D_H(f)) shows the weight needed to represent f as a threshold of H grows as **1/correlation**: low per-function correlation *limits the weight* but does **not prevent** aggregation at sufficient size. So O(s·disc) is the wrong (linear) bound for a *nonlinear* top gate; the true aggregate correlation can be high once s ≳ 1/disc — which at disc = 2^{−n/2} is s ≳ 2^{n/2}, precisely the regime where HMPT's *worst-case* size bound also kicks in. The exponential average-case bound at *poly* size does not follow.

## 4. The diagnosis, sharpened one level below Cycle 3

Cycle 3 (`[non-amplification-also-class-drifts]`) located the obstruction at the **NW reconstruction's decoder** (arithmetic/parity machinery exceeding MAJ∘MAJ). Cycle 4 locates it one level **earlier and more fundamentally**: at the **amplification / aggregation step itself**, independent of any NW reconstruction. Even before a worst-case LB is fed into an NW-style reconstruction, the step that would turn it into an average-case LB against the *same composed class* is blocked — by the circuit class's *own* aggregation power (boosting / threshold nonlinearity). The Discriminator Lemma (and CLLO21's converse) are the only known lifters, and they route through worst-case(MAJ∘C) / back to avg-case(C), never reaching avg-case(MAJ∘C); the reason they cannot is that reaching avg-case(MAJ∘C) would require *defeating* the very majority-aggregation that makes MAJ∘C powerful — an "anti-boosting" statement for which no technique is known (consistent with Cycle 3: the techniques that would supply it — list-decodable codes, arithmetization — themselves exceed MAJ∘MAJ).

**This is the fifth angle confirming `[witness-needs-explicit-lb]`.** The only escape remains a **directly-constructed** exponential average-case-correlation LB for full-poly-size MAJ∘MAJ — now with the obstruction's *mechanism* identified (defeat majority-aggregation / anti-boosting), not merely its location. A "direct" LB here would have to prove the per-gate Lindsey correlations *cannot aggregate* under a top threshold at polynomial size — equivalently, an anti-boosting / correlation-structure bound for IP₂, which is the natural-proofs-flavored circuit-LB problem in this precise form.

## 5. Honest scope `[honest-ceiling]`

- **No opening found.** The potential breakthrough my rough calc flagged was verified *closed*; the calc's linear-bound assumption fails for the structural reason (top-threshold nonlinearity / aggregation, verified via CLLO21 + Kumar CCC 2023).
- **No lower bound proved; no CAPP constructed.** All results cited are known (HMPT, Lindsey, CLLO21, Kumar CCC 2023, GHR92). The product is a *sharpened, primary-source-verified diagnosis*: the worst-case→average-case obstruction lives at the amplification/aggregation level (below the Cycle-3 decoder level), in the uncovered cell of a 2×2 grid, for the precise reason that the top threshold's aggregation power defeats any linear lifting.
- **Not P≠NP regardless** — this is a Williams-side derandomization-adjacent diagnosis; even a positive (a direct average-case MAJ∘MAJ LB) would yield NEXP ⊄ THR∘THR + TC⁰₃, not P≠NP.
- **Unverified / flagged.** (a) The CLLO21 converse's exact hypotheses (C ⊆ NC¹, closure under negation, bottom O(1)-juntas) — depth-1 threshold C *plausibly* satisfies these (it is in NC¹, closed under negation, bottom gates are O(1)-juntas in the relevant sense), but the precise match is taken from the search summary, not the PDF; flagged for pre-publication check. (b) The Kumar CCC 2023 "sharp threshold" parameters (k = Ω(n^{1/d})) taken from the search summary. (c) "The only known lifters are the Discriminator Lemma and its CLLO21 converse" — a survey-level claim (no *other* avg(C)↔avg(MAJ∘C) tool found), not an exhaustive impossibility. (d) The "anti-boosting / correlation-structure" framing of the genuine-open shape is a *diagnostic characterization*, not a published reduction.

## Sources
- Hajnal, Maass, Pudlák, Szegedy, Turán, "Threshold Circuits of Bounded Depth," JCSS 46:129–154, 1993 (FOCS'87). Lemma 3.2 (IP₂ depth-2 worst-case), Lemma 3.3 (Discriminator Lemma), Lemma 3.4 (Lindsey). `[hmpt-1993]`
- Chen, Lu, Lyu, Oliveira, "Majority vs. Approximate Linear Sum and Average-Case Complexity Below NC¹," 2021 (`CLLO21`). Thm 1 (converse to the Discriminator Lemma; SUM] gates; black-box amplification fails without majority-closure). `[cllo-2021]`
- Kumar, "Tight Correlation Bounds for Circuits Between AC⁰ and TC⁰," CCC 2023. Multi-switching lemma for GC⁰(k); sharp threshold in the bias parameter (small-bias gates aggregate to compute parity). `[kumar-2023]`
- Goldman, Håstad, Razborov, "Majority Gates vs. General Weighted Threshold Gates," 1992 (GHR92). Correlation lemma TH_H(f) ≤ 1/D_H(f) — weight grows as 1/correlation; aggregation not prevented by low per-function correlation.
- Amano, "On the size of depth-two threshold circuits for the inner product mod 2 function," LATA 2020. The depth-2 IP₂ LB/UB table (THR∘AND, THR∘SYM, THR∘MAJ, THR∘THR, MAJ∘THR, MAJ∘ETHR). `[amano-2020]`
- Prior-cycle records: sources/2026-08-21-mining-program-seam.md (Cycle 0/second pass — the O(s·disc) question's ancestry), sources/2026-08-23-wire-frontier-push.md (Cycle 2 — two-dimensional gap), sources/2026-08-23-nonamplification-route.md (Cycle 3 — decoder-level drift).