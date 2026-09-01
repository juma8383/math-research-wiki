# Cycle 2 — The CSS16/Tell wire-frontier push: two-dimensional characterization of the mining gap (Williams side)

**Date:** 2026-08-23
**Sub-target:** Williams-side continuation of the [witness-needs-explicit-lb] / mining-program seam; the user's autonomous "continue the next best options on loop for 5 cycles" request — Cycle 2. Pushes the second-pass [mining-worst-vs-average] refinement to primary-source precision by mapping the full depth-2-threshold correlation-vs-wire landscape.
**Provenance (honest):** main-loop (no subagents — HTTP 429 persists); grounded by web search + the Amano 2020 PDF (LATA, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206633/), [author PDF](https://ama.inf.gunma-u.ac.jp/~amano/paper/IP2_v1.pdf)); CSS16 ([ToC 2018](https://theoryofcomputing.org/articles/v014a009/v014a009.pdf)); Kane-Williams ([STOC 2016](https://dl.acm.org/doi/10.1145/2897518.2897636)); Chen-Tal-Wang ([STOC 2025](https://dl.acm.org/doi/10.1145/3798129.3800802)); HMPT/Forster via prior passes. The Chen-Tal-Wang STOC 2025 page returned HTTP 403 to WebFetch; its parameters (worst-case, f ∈ E^NP, algorithmic method, XOR-of-two estimator) are taken from the search summary.

---

## The verified landscape — IP₂ and depth-2 threshold, worst-case vs average-case

### Worst-case (exact computation) — exponential ONLY when one layer's weights are restricted

The central open question is stated explicitly in **Amano 2020** and as **Kane-Williams 2016 Open Question #2**: *does IP₂ have polynomial-size depth-2 threshold circuits with unbounded weights in both layers (THR∘THR)?* The gap is enormous:

| Class (weights) | IP₂ worst-case LB | Method |
|---|---|---|
| **THR∘THR** (unbounded, both) | **Ω(n)** (trivial) | — (open; upper bound O(1.682ⁿ), Amano) |
| MAJ∘THR (poly top) | Ω(2^{(1/3−ε)n}) | HMPT 1993, discriminator/discrepancy |
| THR∘MAJ (poly bottom) | Ω(2^{n/2}/poly) | Forster 2002, sign-rank |
| THR∘SYM (symmetric bottom) | Ω((1.5−ε)ⁿ) | Amano 2020, LP-dual |
| THR∘AND, THR∘XOR | 2ⁿ | folklore |

**Key fact:** all known exponential/subexponential worst-case LBs for IP₂ require restricting weights in at least one layer (poly-bounded, or symmetric). For the *fully unrestricted* THR∘THR, only a trivial **Ω(n)** LB is known — the worst-case exponential LB for IP₂ against unrestricted depth-2 threshold is itself **open** (Amano; Kane-Williams Open Q #2).

### Average-case (correlation) — only few-wire, and Parity is wire-TIGHT at n^{1.5}

CSS16 ([css-2018], the explicit "frontier" paper) proves average-case *correlation* LBs for bounded-depth threshold at **few wires**:
- **Parity** vs depth-2 threshold ≤ **n^{1.5−ε} wires**: correlation ≤ n^{−Ω(γ)} (γ=1/2−ε) — and this is **TIGHT**: depth-2 with O(√n) gates / O(n^{1.5}) wires already approximates Parity well, so **Parity cannot give an average-case LB past n^{1.5} wires** (it is wire-tight for Parity).
- **Generalized Andreev** vs depth-d threshold ≤ **n^{1+ε_d} wires**: correlation ≤ **exp(−n^{ε_d})**.

### The recent worst-case progress (Chen-Tal-Wang STOC 2025) — wrong direction for mining

Chen-Tal-Wang STOC 2025: f ∈ E^NP requires **n^{2.5−ε}-size THR∘THR** (worst-case), breaking the n^{2−ε} barrier (Tamaki 2016 / Alman-Chan-Williams 2016) via a 2^n − n^{Ω(ε)}-time algorithm for estimating the acceptance probability of an **XOR of two** n^{2.5−ε}-size THR∘THR circuits + the Williams algorithmic method. **Crucially: this is (a) worst-case, not average-case; (b) f ∈ E^NP, not an explicit polytime function usable as an NW hard function; (c) a specialized XOR-of-two-circuits estimator, not a general MAJ∘MAJ/THR∘THR CAPP; (d) the Williams direction fast-sub-problem-algo → LB (CAPP→LB), the OPPOSITE of what the mining program needs (LB → CAPP).** So it confirms the algorithmic method is actively progressing on depth-2 THR∘THR worst-case, but it does not feed the mining program (and goes the wrong way).

---

## The Cycle-2 finding — the mining gap is TWO-DIMENSIONAL (correlation-strength × regime)

The second-pass [mining-worst-vs-average] "quantitative+regime gap" sharpens to a **two-dimensional gap**. The NW/Chen-Ren target — a **2^n/n^{ω(1)} 1/poly-error CAPP for full-poly-size MAJ∘MAJ** — needs, after the NW predictor loss, an explicit function with **average-case correlation ≤ 2^{−Ω(ℓ)} (exponential in ℓ) against full-poly-size MAJ∘MAJ**. The two known average-case data points both fall short on BOTH dimensions:

| Data point | Correlation strength | Regime (wires) | vs target |
|---|---|---|---|
| **NW target** | 2^{−Ω(ℓ)} (exponential) | full poly-size | — |
| CSS16 Parity (depth-2) | n^{−Ω(γ)} (polynomial) | ≤ n^{1.5−ε} | short on both; **wire-tight** |
| CSS16 Gen-Andreev (depth-d) | exp(−n^{ε_d}) (**sub**exponential) | ≤ n^{1+ε_d} | short on both |

So the gap is not a single one-dimensional jump. It is:
- **Dimension 1 — correlation strength:** known average-case correlations are polynomial (Parity) or subexponential exp(−n^{ε_d}) (Gen-Andreev); the target is **exponential 2^{−Ω(ℓ)}**. Even CSS16's best (Gen-Andreev) is subexponential, not exponential.
- **Dimension 2 — regime (wires):** known average-case bounds hold at few wires (≤ n^{1+ε_d}; Parity wire-tight at n^{1.5}); the target is **full poly-size**. Parity is the *wrong* function to push past n^{1.5} wires (it is wire-tight there); one must use Generalized Andreev or a new function.

**[mining-gap-two-dimensional] — the mining obstruction is a two-dimensional (correlation-strength × wire-regime) gap; no known average-case data point is exponential-correlation OR full-poly-size, let alone both.**

### MAJ∘MAJ vs THR∘THR anchoring (sharpened via the CAPP-equivalence)

Chen-Williams (CCC 2019): MAJ∘MAJ CAPP ⟺ THR∘THR CAPP (CAPP-equivalent, [majmaj-symmetry-deflated]). So the mining program can aim at either, but they are **not equally anchored**:
- **MAJ∘MAJ** (bounded weights, both layers): HMPT gives a **worst-case exponential** LB for IP₂ (Ω(2^{(1/3−ε)n})). So the worst-case exponential anchor EXISTS for MAJ∘MAJ; the gap is purely the worst-case→average-case + two-dimensional jump.
- **THR∘THR** (unbounded weights, both layers): even the **worst-case exponential** LB for IP₂ is OPEN (Ω(n) trivial, Amano; Kane-Williams Open Q #2). 

So **MAJ∘MAJ is the better-anchored mining target** (worst-case exponential already present), and the CAPP-equivalence means a CAPP at the MAJ∘MAJ level automatically serves THR∘THR. Targeting THR∘THR directly would require first closing the worst-case-exponential open question — strictly harder. This confirms the mining program's "use HMPT (worst-case, MAJ∘MAJ)" instinct is correctly anchored, *and* re-confirms that the obstruction is precisely the worst-case(MAJ∘MAJ)→average-case(full-poly-size, exponential-correlation) jump — the second-pass finding, now with the unrestricted-THR∘THR-worst-case-is-open adjacency making clear why MAJ∘MAJ is the only viable anchor.

---

## Honest status of the test (`[honest-ceiling]`)

I pushed the wire frontier from both ends — the average-case side (CSS16; confirmed Parity is wire-tight at n^{1.5}, Gen-Andreev only subexponential at n^{1+ε_d}) and the worst-case side (Amano THR∘SYM Ω((1.5−ε)ⁿ); the open unrestricted THR∘THR worst-case; Chen-Tal-Wang 2025 n^{2.5−ε} worst-case via the algorithmic method, wrong direction for mining). **The seam holds, now two-dimensionally characterized.** No opening found:
- The average-case frontier (CSS16) is wire-tight for Parity and only subexponential-correlation for Gen-Andreev; the NW target (exponential correlation, full poly-size) is short on both dimensions.
- The unrestricted THR∘THR worst-case exponential for IP₂ is itself open (Amano; Kane-Williams Open Q #2) — so the "CAPP-equivalent" THR∘THR target lacks even a worst-case anchor; MAJ∘MAJ (HMPT worst-case) is the only anchored target.
- The most recent progress (Chen-Tal-Wang 2025) is worst-case + the CAPP→LB direction (opposite of mining) + a specialized XOR-of-two estimator, not a general CAPP.

**The near-term lever remains the CSS16/Tell wire frontier** — but sharpened: the open improvement is not merely "more wires" (Tell's n^{1+exp(−d)} → n^{1+O(1/d)}), it must ALSO cross the correlation-strength dimension (subexponential exp(−n^{ε_d}) → exponential 2^{−Ω(ℓ)}), and Parity cannot help (wire-tight). The genuine-open shape for a breakthrough is now precise: **an average-case correlation LB that is exponential (2^{−Ω(ℓ)}) against full-poly-size MAJ∘MAJ, for a Parity-different function** (Gen-Andreev or new) — open on both dimensions, or a single advance crossing both at once.

## Tags

`[mining-gap-two-dimensional]` `[mining-worst-vs-average]` `[mining-nw-seam]` `[witness-needs-explicit-lb]` `[css-2018]` `[kane-williams-2016]` `[hmpt-1993]` `[tell-2018-quantified]` `[chen-tal-wang-2025]` `[amano-2020]` `[majmaj-symmetry-deflated]` `[chen-williams-2019]` `[honest-ceiling]`

## Sources
- CSS16 — Chen-Santhanam-Srinivasan, "Average-Case Lower Bounds and Satisfiability Algorithms for Small Threshold Circuits," ToC 14(9), 2018 ([article](https://theoryofcomputing.org/articles/v014a009/v014a009.pdf)) `[css-2018]` — Parity wire-tight at n^{1.5}; Gen-Andreev exp(−n^{ε_d}) at n^{1+ε_d} wires.
- Amano, "On the Size of Depth-Two Threshold Circuits for the Inner Product Mod 2 Function," LATA 2020 ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206633/), [author PDF](https://ama.inf.gunma-u.ac.jp/~amano/paper/IP2_v1.pdf)) `[amano-2020]` — states the open question (poly-size THR∘THR for IP₂); THR∘SYM Ω((1.5−ε)ⁿ) via LP-dual; THR∘THR upper O(1.682ⁿ).
- Kane-Williams, STOC 2016 ([DOI](https://dl.acm.org/doi/10.1145/2897518.2897636)) `[kane-williams-2016]` — Open Question #2 (poly-size LTF∘LTF for IP₂); superquadratic-wire average-case for Andreev.
- Chen-Tal-Wang, "Superquadratic Lower Bounds for Depth-2 Linear Threshold Circuits," STOC 2025 ([ACM DL](https://dl.acm.org/doi/10.1145/3798129.3800802)) `[chen-tal-wang-2025]` — f ∈ E^NP needs n^{2.5−ε}-size THR∘THR (worst-case, algorithmic method, wrong direction for mining).
- HMPT — Hajnal-Maass-Pudlák-Szegedy-Turán, JCSS 1993 `[hmpt-1993]` — IP₂ worst-case exponential for restricted-weight MAJ∘THR.
- Forster et al. 2002 — sign-rank; IP₂ worst-case Ω(2^{n/2}/poly) for THR∘MAJ.