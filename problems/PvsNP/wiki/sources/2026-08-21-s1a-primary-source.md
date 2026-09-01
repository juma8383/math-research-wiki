# Source — S1.a: verification against the primary source ECCC TR20-183 (2026-08-21)

**Tags:** `[honest-ceiling]` `[ilango-2020]` `[s1-derandomization]` `[s1-chebyshev-moce-oracle]` `[s1-meta-vs-lowdegree]` `[s1-necessary-insufficient]` `[s1a-chebyshev-phantom]` `[s1a-lupanov-only-rng]` `[s1a-antiprox-obstruction]` `[hos-2018]`

**Provenance (honest):** Main-loop verification (no subagents — the dispatching API account's session-usage limit, HTTP 429, from the prior `mcsp-deep-dive` fan-out remains in effect). Verified against the **primary source**: the extracted plaintext of ECCC TR20-183 (Ilango, *Constant Depth Formula and Partial Function Versions of MCSP are Hard*, FOCS 2020 / SIAM J. Comput. 2022), saved at `sources/_tr20-183.txt` (3955 lines, via `pdftotext -layout` from the ECCC PDF). All line/paragraph numbers below cite that file. **This source CORRECTS a substantive claim of the s1-push source** (`[s1-chebyshev-moce-oracle]`): the "named plausible mechanism" was aimed at a randomness source that does not exist in the reduction algorithm. No derandomization completed; no NP-hardness claimed; `[honest-ceiling]` upheld.

---

## What S1.a set out to verify

The s1-push source named `[s1-chebyshev-moce-oracle]` as the "genuinely forward step": derandomize **Source 1** (the Chebyshev/second-moment Splitting Claim) via method-of-conditional-expectations *using the reduction's own oracle* as the potential evaluator, exploiting (i) pairwise-independence suffices (short enumerable seed) + (ii) the Turing-oracle + inductive d-1↔d structure make the partition-quality potential evaluable. The linchpin flagged for verification (S1.a, micro-target): *is the Splitting Claim's partition-quality potential actually a query the reduction's algorithm evaluates?* I.e. — does the **reduction algorithm** invoke the Splitting Claim as a randomized procedure, or is the Splitting Claim only used in the **proof** of a lemma the algorithm consumes as a deterministic black-box?

## The decisive finding — the Splitting Claim is PROOF-INTERNAL `[s1a-chebyshev-phantom]`

Reading Theorem 25 (the inductive step d-1→d, lines 2399-2776) settles it.

**The reduction ALGORITHM (lines 2446-2474, "Algorithm for the reduction")** is:
1. **Brute-force** (deterministic): iterate all AND∈AC⁰_{d-2} formulas of size n^{1024/δ}; output the smallest computing f if one exists (lines 2449-2451).
2. For each i∈[2^{2n}] and each t∈[n^{8/δ}, 2^n]: **sample g_{i,t} ~ D_{n,t,δ,ε}** (the Lupanov distribution, Lemma 26) — line 2456. Set b_{i,t}=1 iff O(f(x)∧g_{i,t}(y)) ≤ (1+ε/16)·t·n² (lines 2458-2462).
3. Set t* = max{t : b_{i,t}=1 for ≥ half the i} (line 2466).
4. Pick a **random** i*∈[2^{2n}] and output O(f(x)∧g_{i*,t*}(y)) − t*·n² (lines 2470-2472).

**The Splitting Claim (Claim 21, lines 2169-2326) appears NOWHERE in this algorithm.** It is part of the proof of **Theorem 5** (the "lifting theorem" / lower bound L^{OR}_d(f∧g) ≥ L^{OR}_d(g) + L^{A-ND}_{d-1}(f)). Theorem 5 is invoked **only in the CORRECTNESS proof** of Theorem 25's reduction:
- Claim 28 (line 2574-2578): *"We wish to use the lower bound L^{OR}_d(f∧g_{i,t}) ≥ L^{OR}_d(g_{i,t}) + L^{A-ND}_{d-1}(f) that is given in Theorem 5."*
- The lower-bound half of correctness (line 2742): *"we will again make use of Theorem 5 in order to obtain the lower bound…"*

Theorem 5 is a **deterministic inequality**: once proven (via the probabilistic method — Claim 21 establishes the existence of a good partition L,R *unconditionally*), the inequality **holds for all** f,g satisfying the hypotheses. The reduction uses it as a **black-box true fact**, not as a procedure it runs. The randomized coins of Claim 21 (the partition of {S_i} into L,R) are spent **inside the proof**, not by the algorithm.

`[s1a-chebyshev-phantom]`: **the Splitting Claim is NOT a randomness source in the reduction algorithm.** It is proof-internal to the lifting theorem (Theorem 5), used as a deterministic inequality in the correctness argument. **`[s1-chebyshev-moce-oracle]` is a phantom target** — derandomizing the Chebyshev split via MOCE-with-oracle addresses randomness that the algorithm never spends. The "MOCE using the oracle to evaluate the partition-quality potential" mechanism is moot.

**The simultaneity obstruction dissolves.** In the s1-push analysis (and the pre-compaction reasoning) I flagged "derandomizing the SIMULTANEITY (both L and R good — a nonlinear joint condition)" as the real obstruction to the Chebyshev-MOCE route. **That worry was mis-aimed**: the simultaneity (both L,R forming .73-one-sided approximations, yielding the contradiction 2·L_{ND,.73}(g) ≤ L^{OR}_d(g)+L^{A-ND}_{d-1}(f)) is part of the probabilistic-method *proof* of the inequality, not an algorithmic step. There is no simultaneous-pair condition in the reduction to derandomize. The dissolution is itself a finding: a would-be obstruction that turned out not to live in the algorithm.

---

## The ONLY algorithmic randomness — Lupanov sampling of g `[s1a-lupanov-only-rng]`

With Source 1 reclassified as proof-internal, **the sole substantive randomness in Theorem 25's reduction is the Lupanov sampling of g (Lemma 26)** — what the s1-push source called "Source 2," and what I had ranked as the *harder, less-mechanized* half. The primary source shows it is in fact the **only** half, and recharacterizes its structure in a way that changes the derandomization story.

**Lemma 26's distribution D_{n,t,δ} (lines 2782-2821) is a SMALL-SEED distribution**, not a sample over a doubly-exponential function space:
- m = n²/δ. For each y∈[t], sample Z_y ⊆ [m] by placing each element of [m] into Z_y independently with probability m⁻¹ (lines 2803-2805).
- Output g: {0,1}^{n+m}→{0,1}, g(y,z)=1 iff wt(z)=1 ∧ y∈[t] ∧ (the j-th bit of z is 1 for some j∈Z_y) (lines 2808-2818).
- **The seed is the t·m ≈ 2ⁿ·n²/δ independent Bernoulli(m⁻¹) coins** choosing the Z_y's — **quasipolynomial, enumerable**. This is *why* D is "samplable in time quasipolynomial in 2ⁿ" (line 2787): the seed itself is quasipolynomial, not the truth table.

So the s1-push source's framing of Source 2 as "existential-over-inputs (no single g works for all f)" was **imprecise**: D is a *single fixed distribution*; the reduction samples *many* independent g_{i,t} (i∈[2^{2n}]) from it and takes a median/threshold (lines 2466-2472), purely for amplification. The "for all f" robustness comes from Theorem 5 + goodness of g, not from f-dependent sampling. (The final random i* at line 2470 is trivial amplification — derandomizable by picking any i with b_{i,t*}=1, since ≥ half qualify.)

**Goodness of g (the two properties the reduction needs) holds with probability 1−o(1) over the seed** (Lemma 26, lines 2789-2794), by a two-part argument:
- **Upper bound (constructive, FREE):** L^{AND_2}_{ND}(g) ≤ (1+4δ)·t·n². Claims 30-31 (lines 2855-2893) give an **explicit formula** for g whose size is computed directly from the seed (it equals ≈ 2m² + (t+1)n + Σ|Z_y|). For ANY seed (conditioned on the Chernoff event Σ_{y∈[t]}|Z_y| ≈ t·n²), the upper bound holds. ✓ computable from the seed — no meta-complexity.
- **Lower bound (the OBSTRUCTION):** L_{ND}(g) ≥ (1−4δ)·t·n² — i.e. NO non-deterministic formula of size < (1−4δ)t·n² ε-one-sided-approximates g. Proved (Claim 32, lines 2932-2967) by a **union bound over all candidate formulas h of size s=(1−4δ)t·n²**: for each fixed h, the probability (over the random Z_y's, since g's values are independent Bernoulli(m⁻¹)) that h ε-approximates g is ≤ O(2^{−ε²(1−3δ)t·n²·log n}) (line 2946); the number of candidate h's is ≤ 2^{2·s·log(200n)} (Prop 9, line 2952-2959); the union bound gives o_{ε,δ}(1) (line 2966).

`[s1a-lupanov-only-rng]`: **S1 = derandomize the Lupanov sampling of g.** The seed is small (quasipolynomial, enumerable). Goodness is a high-probability (1−o(1)) event over the seed, with an **asymmetric two-sided structure**: the *upper-bound* half is constructive and seed-computable (free); the *lower-bound* half is a derandomized-union-bound over an exponentially-large family of candidate formulas.

---

## The obstruction, precisely located `[s1a-antiprox-obstruction]`

The real S1 derandomization question is: **find a seed (a choice of the Z_y's) such that g is good — deterministically.** The seed space is quasipolynomial (enumerable in principle), and a good seed exists with probability 1−o(1), so existence is not the issue. The question is *finding one efficiently*.

The upper-bound half derandomizes trivially: it is a constructive formula size computable from any seed (conditioned on the Chernoff event, itself a sum of independent indicators — foolable / MOCE-able by standard means).

**The lower-bound half is the obstruction** `[s1a-antiprox-obstruction]`. To derandomize the union bound (Claim 32) by method of conditional expectations, the potential is the **conditional expected number of "bad" formulas h** (size-s formulas that ε-one-sided-approximate g) given the partial seed:
  potential = Σ_{h of size s} Pr_{remaining seed}[h ε-approximates g].
The per-h probability is a **product of independent per-y terms** (each Z_y is sampled independently) — individually cheap to compute for a FIXED h (line 2946 is exactly this product). **But the sum is over the family of all size-s non-deterministic formulas, of size 2^{O(s·log n)} = 2^{O(t·n²·log n)}** (line 2952) — **doubly-quasipolynomial, infeasible to enumerate.** Computing the exact conditional expectation requires summing over an exponentially-large formula family: that enumeration **is the meta-computational core**.

`[s1a-antiprox-obstruction]`: the Lupanov-derandomization obstruction is precisely **the lower-bound / anti-approximation side** — a derandomized union bound over the family of candidate small CNFs, where the potential is a sum over a 2^{O(t·n²·log n)}-sized formula family. This is the exact content of `[s1-meta-vs-lowdegree]`, now located against the primary source rather than inferred: it is *not* vaguely "ε-biased fails meta-tests"; it is specifically that the MOCE potential for the anti-approximation lower bound is an exponential sum over circuit-complexity witnesses. The upper-bound side is free.

**Why HOS18's trick does not port — now exact.** HOS18's bad events (niceness/scatteredness of the set-cover lift) are `AND◦MOD_m`-type tests — ε-biased distributions fool them *because the per-event probability and the family are both low-degree-structured*, so the small-bias seed fools the whole union bound at once (no enumeration). Ilango's bad events are "small formula h approximates g" — a *circuit-complexity / approximation* event, not a low-degree test. Small-bias does not fool the per-h probability, and the union bound's exponential family is not low-degree-structured, so neither the per-event fooling nor the family-enumeration collapses. The HOS18 mechanism's two ingredients both fail here. `[s1-meta-vs-lowdegree]` confirmed and sharpened.

---

## Salvageable routes (honest, not completed)

The deflation of `[s1-chebyshev-moce-oracle]` does not leave S1 empty — it relocates the question. Two honest directions remain, both open and both harder than the phantom mechanism:

1. **Explicit-construction route (replace the sampler).** Bypass D entirely: construct a **deterministic** function g with DNF complexity in the tight window [(1−4δ)t·n², (1+4δ)t·n²] for each t∈[n^{8/δ}, 2ⁿ], plus the min{L_{ND}+L_{ND,ε}, 2·L_{ND,.73}} condition. The upper bound is free (Lupanov's explicit formula); the crux is a **fine-grained DNF lower bound** (ruling out size-<(1−4δ)t·n² approximations) for an explicit function in a parameterized window. This is a genuine circuit-lower-bound construction — the same flavor of difficulty as the rest of the field, now isolated as S1's true core. Not known; falsifiable (find such a g, or prove no explicit one exists in the window).

2. **Pseudorandom-fooling route.** Find a PRG (not necessarily ε-biased) whose seed is short enough to enumerate, that fools the *specific* bad event "∃ small formula h approximating g." This requires fooling a circuit-approximation test — exactly what `[s1a-antiprox-obstruction]` says is hard, and the same flavor as the `[dilv-2024]`/`[s1-meta-vs-lowdegree]` family. No known PRG fools meta-computational approximation tests; this is the obstruction, not a route — but stating it precisely is itself progress.

**Net:** the "named plausible mechanism" of the s1-push source is **deflated** — it targeted a non-existent randomness source. The genuine S1 question is harder than it appeared: derandomizing the Lupanov sampling reduces, on the lower-bound side, to a fine-grained DNF lower bound for an explicit function in a tight parameterized window. S1's "most tractable Route-A-adjacent step" framing is **tempered**: the derandomization is tractable on the upper-bound side and obstructed (circuit-LB-hard) on the lower-bound side.

---

## Corrections to the s1-push source (recorded, not retroactive)

The s1-push source is **immutable raw record** (per the wiki schema). This source records the corrections against it:
- **CORRECTED:** "Source 1 — the probabilistic Splitting Claim" is **not a randomness source in the reduction algorithm**; it is proof-internal to Theorem 5. `[s1a-chebyshev-phantom]`
- **CORRECTED:** `[s1-chebyshev-moce-oracle]` (MOCE-with-oracle on the Chebyshev split) is a **phantom mechanism** — it derandomizes randomness the algorithm never spends. The "linchpin" flagged for S1.a verification is **resolved: NO** (the potential is not an algorithmic query because the Splitting Claim is not in the algorithm).
- **CORRECTED:** the "simultaneity obstruction" (both L,R good) flagged in pre-compaction analysis **dissolves** — simultaneity is part of the probabilistic-method proof of the inequality, not an algorithmic step.
- **RECHARACTERIZED:** "Source 2 — Lupanov sampling" is the **sole** algorithmic randomness `[s1a-lupanov-only-rng]`, and it is a **small-seed** distribution (t·m enumerable coins), not an existential-over-inputs sample over a doubly-exponential space.
- **SHARPENED:** `[s1-meta-vs-lowdegree]` is now located exactly `[s1a-antiprox-obstruction]` — the MOCE potential for the anti-approximation lower bound is an exponential sum over a formula family; the upper bound is free.

**Unchanged / upheld:** `[s1-hos18-precedent]` (HOS18 did derandomize a restricted-class MCSP reduction — real, confirmed by the contrast); `[s1-necessary-insufficient]` (S1 closes only randomized→deterministic; Route A still needs quasipoly→AC⁰, Turing→many-one, restricted→original — the honest bound is unaffected by where the randomness lives).

---

## Net honest outcome of S1.a

1. **Primary-source verification DONE.** Read ECCC TR20-183 (Theorem 25 algorithm lines 2446-2474; Theorem 5/Claim 28 invocation lines 2574-2605, 2742-2771; Lemma 26 distribution lines 2782-2821; Claim 32 union bound lines 2932-2967).
2. **A substantive self-correction.** The s1-push source's flagship mechanism `[s1-chebyshev-moce-oracle]` was a phantom — the Splitting Claim it targeted is proof-internal to the lifting theorem, not a randomness source in the reduction algorithm. `[s1a-chebyshev-phantom]` Honest correction recorded against the immutable source rather than retroactively edited.
3. **The real S1 question located.** S1 = derandomize the Lupanov sampling of g `[s1a-lupanov-only-rng]`: small enumerable seed, asymmetric two-sided goodness (upper bound free / constructive; lower bound = derandomized union bound over an exponential formula family = the meta-computational obstruction `[s1a-antiprox-obstruction]`).
4. **S1's tractability re-rated (downward on the mechanism, honest).** The deflation removes a too-optimistic "named non-blocked mechanism." The genuine core is a fine-grained DNF lower bound for an explicit function in a tight window — a circuit-LB-hard problem, the same flavor as the field's central difficulty. S1 remains a legitimate, precisely-stated derandomization target and the most tractable Route-A-adjacent step *in the sense of being well-defined and precedent-adjacent*, but its derandomization is **not obviously closer than a fine-grained circuit lower bound**.
5. **Honest bound unchanged** `[s1-necessary-insufficient]`: even a full S1 closes only randomized→deterministic; necessary-but-insufficient for P≠NP.

**No derandomization completed; no NP-hardness claimed; no lower bound claimed; `[honest-ceiling]` upheld.** The product of S1.a is a verified self-correction (phantom mechanism deflated) plus a precisely-located, harder-than-expected true target (Lupanov derandomization ↔ fine-grained DNF lower bound).

### Remaining micro-targets (revised)
- **(S1.a′)** [done] Splitting Claim location: proof-internal. (Was: "verify the potential is an oracle query" — answered NO, the question was mis-aimed.)
- **(S1.b′)** [reframed] Does an **explicit** function with DNF complexity in the tight window [(1−4δ)t·n², (1+4δ)t·n²] exist for each t∈[n^{8/δ}, 2ⁿ]? This is the explicit-construction route; it IS the fine-grained DNF lower bound. The genuine open core of S1.
- **(S1.c)** [unchanged] Quasipolynomial overhead interaction with seed enumeration (now moot for the Chebyshev side; live only for the Lupanov side if route 1 or 2 pans out).