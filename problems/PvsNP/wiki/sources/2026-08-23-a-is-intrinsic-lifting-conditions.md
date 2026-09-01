---
title: "Cycle 9 / 3rd-loop Cycle 4 — (A) is intrinsic to the lifting theorem, not a Lupanov-sampler artifact: an alternative explicit function must satisfy the same two (tensioned) conditions"
cycle: 9
loop: 3
date: 2026-08-23
tags: [honest-ceiling, ilango-2020, s1a-antiprox-obstruction, s1a-lupanov-only-rng, ac0-tight-window, witness-needs-explicit-lb, wall-collapses-to-a, b-reduces-to-a, tight-window-upper-bound-linchpin, lifting-needs-expensive-and-small-gap, expensive-tensions-small-gap, a-is-intrinsic-not-lupanov-artifact, a-is-a-balanced-point, alternative-function-no-bypass, wall-stays-loosened, third-loop-cycle-4, main-loop, no-subagents]
status: raw
---

# Cycle 9 — (A) is intrinsic to the lifting theorem; an alternative function does not bypass it

## The question Cycle 9 set out to answer

Cycle 8 compressed the wall to **(A)** = derandomize the Lupanov sampler = explicitly construct a tight-window DNF LB (= the circuit-LB frontier). Cycle 8's "remaining cycles" note proposed attacking (A) from a new angle: is there a *structurally-different route* to an explicit tight-window DNF LB that does NOT go through derandomizing Lupanov — e.g., a *direct combinatorial construction* of an explicit function whose DNF complexity sits exactly in the tight window? The natural sub-question: could an alternative explicit function with a known *tight* DNF lower bound at a tunable size (e.g., parity, tight at 2ⁿ; the addressing function, tight at ~2^k) substitute for the Lupanov-sampled g?

Cycle 9 (sources read: ECCC TR20-183, content-lines 340–388, the informal Theorem 4/5 exposition + the "how do we get our hands on such g" passage, read VERBATIM) tests this and finds: **the alternative-function angle does not bypass (A) — it recovers the SAME two conditions Lupanov satisfies, because those two conditions are what the lifting theorem (Theorem 5) intrinsically requires of g, and they are in tension.**

## Finding 1 — the lifting theorem requires g to satisfy TWO conditions, which are exactly (A)'s two sides `[lifting-needs-expensive-and-small-gap]`

Verbatim (content-lines 375–383):
> "How do we get our hands on such g? We need g to satisfy two properties: **be expensive relative to f** and **have the quantity L^{AND_{d−1}}(g) − L^{OR}_d(g) be small**. Uniformly random functions (with the right parameters) are expensive, but when d = 3, the quantity L^{AND_{d−1}}(g) − L^{OR}_d(g) is not small for such uniformly random g. We get around this by selecting our g to be drawn randomly from a set of functions that roughly corresponds to the subfunctions computed by CNF subformulas in Lupanov's construction of near optimal depth-3 formulas for random functions [26]. In this way, we get functions that are essentially optimally computed by CNFs but also have properties expected of random functions."

The two conditions on g:
1. **Expensive relative to f** (content-lines 359–368): computing even a weak one-sided approximation of g via nondeterministic formulas is more expensive than computing f exactly with AND∘AC⁰_{d−2} formulas. This is the **hardness / lower-bound** condition — g must be hard (random-function-like hardness; this is the antiprox obstruction, the lower-bound side).
2. **L^{AND_{d−1}}(g) − L^{OR}_d(g) small** — g's AND-depth-(d−1) complexity and OR-depth-d complexity are CLOSE. This is the **tight window / small-gap** condition (Gate 2) — the upper-bound/structural-precision side.

These two conditions are **exactly the two sides of (A)**: condition (1) = the antiprox lower bound (= (A)-lower, the hard part), condition (2) = the tight-window upper bound (= (A)-upper, the linchpin feature of Cycle 8). So the lifting theorem's requirements on g ARE (A). The Lupanov sampler is the known (randomized) way to get a g satisfying both; an explicit construction must produce a g satisfying both — which is (A).

## Finding 2 — the two conditions are in TENSION; Lupanov threads the needle `[expensive-tensions-small-gap]`

Verbatim (content-lines 384–387):
> "In our reduction we have to balance how expensive g is with how large L^{AND_{d−1}}(g) − L^{OR}_d(g) is, since **as g gets more expensive L^{AND_{d−1}}(g) − L^{OR}_d(g) also gets larger**."

So the two conditions are in **tension**: making g more expensive (harder, condition 1) makes the gap L^{AND_{d−1}}(g) − L^{OR}_d(g) larger (violating condition 2). Uniformly random functions are expensive (condition 1 ✓) but have a large gap (condition 2 ✗ for d=3). Lupanov's construction threads the needle: functions that are "essentially optimally computed by CNFs" (small gap, condition 2 ✓) "but also have properties expected of random functions" (expensive, condition 1 ✓). This balancing act is the Lupanov sweet spot.

## Finding 3 — (A) is intrinsic to the lifting theorem, not a Lupanov-sampler artifact; an alternative function does not bypass it `[a-is-intrinsic-not-lupanov-artifact]` `[alternative-function-no-bypass]`

Because the two conditions are Theorem 5's intrinsic requirements on g (not properties of the Lupanov sampler per se), an alternative explicit function substituting for g must satisfy BOTH conditions — i.e., must solve (A). The choice of function does not change the wall:
- **Parity** (the canonical "tight DNF LB" — DNF complexity exactly 2ⁿ) is expensive (condition 1 ✓) but has a LARGE gap (condition 2 ✗) — it is *too hard*; the lifting's error term blows up. Parity does not substitute.
- A **trivially-easy function** has a small gap (condition 2 ✓) but is not expensive (condition 1 ✗).
- An explicit function at the **balanced point** (expensive yet small gap) = exactly the Lupanov sweet spot = (A) itself. **No known explicit function threads the needle**; the Lupanov sampler is the only known (randomized) way. Making it explicit is (A) = the breakthrough.

So the "direct combinatorial construction of an explicit tight-window function" is NOT an alternative to (A) — it IS (A), phrased differently. The wall is robust to the function choice. `[a-is-a-balanced-point]`: (A) is not "an explicit hard function" (parity suffices for hard) nor "an explicit small-gap function" (easy functions have small gaps), but a function at a specific balanced point where hardness and small-gap coexist — the Lupanov sweet spot, made explicit.

## What this changes in the map

1. **(A) is re-described more precisely and confirmed intrinsic.** (A) = construct an explicit g satisfying {expensive (antiprox/lower-bound) ∧ small AND_{d−1}/OR_d gap (tight-window/upper-bound)}, with the two in tension. This is NOT just "derandomize Lupanov" (a sampler-specific framing) — it is the lifting theorem's intrinsic requirement. The wall does not depend on the Lupanov sampler being the chosen method; ANY function paying for the lifting pays (A).
2. **The tension sharpens why (A) is hard.** It is not enough to find an explicit hard function (parity) — that violates the small-gap condition. It is not enough to find an explicit small-gap function — that violates expensive. One needs the balanced point, where the two tensioned conditions coexist. Lupanov threads it randomly; the explicit version is the open problem.
3. **The two-gate / linchpin structure (Cycle 8) is confirmed from the lifting-requirements angle.** Cycle 8 found Gate 1 and Gate 2 coupled via the tight-window upper bound (the linchpin). Cycle 9 confirms the SAME structure from inside the lifting theorem: the two conditions (expensive = lower-bound side = antiprox; small-gap = upper-bound side = tight window) are the two gates, and they are the lifting's intrinsic requirements, not an artifact of the analysis. The linchpin (small gap = tight-window upper bound) is condition (2); the antiprox (expensive = lower bound) is condition (1).
4. **No bypass found; no new leverage.** The alternative-function angle, the most natural "different route to (A)," recovers (A). The near-term tractable seam (a structurally-different uniform-AC⁰ reduction / Tell's promise derandomization) and the long-term breakthrough shape (an explicit balanced-point tight-window DNF LB) are unchanged.

## Honest scope `[honest-ceiling]`

- **Primary-source-grounded:** Ilango §1.3 (content-lines 340–388), the informal Theorem 4/5 exposition and the "how do we get our hands on such g" passage, read VERBATIM.
- **Structural interpretation, not a new theorem:** the identification of the two lifting conditions with (A)'s two sides, and the claim that an alternative function must satisfy both (= solve (A)), is a structural reading of the lifting theorem's hypotheses. The mapping is direct (condition 1 = expensive = the antiprox lower bound; condition 2 = small gap = the tight-window upper bound), but the exact DNF-vs-AND_{d−1}/OR_d depth accounting is kept at the structural level (flagged: the precise depth-formula-complexity measures L^{AND_{d−1}}, L^{OR}_d and their relation to the DNF tight-window [(1−4δ)T,(1+4δ)T] of Cycles 1/7 is a depth-detail not pinned line-by-line here; the structural identification is robust to it).
- **The tension is verbatim** (lines 385–387: "as g gets more expensive [the gap] also gets larger") — not a heuristic.
- **No claim of impossibility:** the tension is a difficulty-sharpening (the balanced point is hard to hit explicitly), NOT a proof that no explicit function can thread the needle. (A) remains an open construction. A clever explicit construction at the balanced point = the breakthrough = (A).
- **No known explicit function threads the needle** (parity too hard; easy functions not expensive) — this is the honest state; if one existed, (A) would be solved. This is a survey-level claim (the field has no such function), not an exhaustive impossibility.
- **No breakthrough.** The wall is unchanged at (A) = the circuit-LB frontier. The deliverable is a robustness/consolidation: (A) confirmed intrinsic to the lifting theorem (not a Lupanov-sampler artifact), re-described as the balanced point of two tensioned conditions, with the two-gate/linchpin structure confirmed from inside the lifting.

## Net

No breakthrough (no P≠NP proof, no new circuit LB, no derandomization, no explicit witness). The wall is unchanged at (A). But the map consolidates: (A) is confirmed intrinsic to the lifting theorem's requirements (not a sampler artifact), re-described precisely as "an explicit g at the balanced point of two tensioned conditions {expensive (antiprox/lower-bound) ∧ small AND_{d−1}/OR_d gap (tight-window/upper-bound)}," and the two-gate/linchpin structure (Cycle 8) is confirmed from inside the lifting theorem. The most natural alternative route to (A) (a different explicit function) recovers (A) — the wall is robust to function choice. Equally honest in difficulty ((A) is the circuit-LB frontier; the tension sharpens why; no impossibility claimed). This is a consolidation/robustness cycle, not a new attack; the remaining lever is unchanged (an explicit balanced-point tight-window DNF LB, or the near-term relaxation seam).

## What this means for the remaining cycle

Cycle 10 (the third loop's final cycle) should **synthesize** the third loop: the wall driven from "two independent gates" (Cycle 1, 2nd loop) → "two coupled tasks (A)+(B)" (Cycle 7) → "essentially (A), with (B) reducing to (A)" (Cycle 8) → "(A) intrinsic to the lifting theorem, re-described as the balanced point of two tensioned conditions, two-gate/linchpin confirmed from inside the lifting" (Cycle 9). The honest deliverable across the third loop: the AC⁰ (S1.a) face's wall driven to maximum structural compression and confirmed robust — one intrinsic barrier (A), one linchpin feature (the tight-window upper bound), Gate 1 soft from three directions, no bypass via alternative function or recognizable variation. No breakthrough; the frontier is (A) = the circuit-LB frontier, an open construction (not a proven impossibility).

## Sources
- Ilango, "Constant Depth Formula and Partial Function Versions of MCSP are Hard," FOCS 2020 / SIAM J. Comput. 2022 (ECCC TR20-183), §1.3 (content-lines 340–388, the Theorem 4/5 informal exposition + the "how do we get our hands on such g" passage, read verbatim). https://www.rahulilango.com/papers/FOCS2020.pdf
- Prior wiki sources: `2026-08-23-naturalization-reduces-to-a.md` (Cycle 8, (B)→(A), the linchpin), `2026-08-23-two-gates-overcounted.md` (Cycle 7), `2026-08-23-ac0-escape-hatch.md` (Cycle 1, Gate 2/tight window), `2026-08-21-s1a-primary-source.md` (Lupanov Lemma 26 / Claims 30–32 / antiprox).