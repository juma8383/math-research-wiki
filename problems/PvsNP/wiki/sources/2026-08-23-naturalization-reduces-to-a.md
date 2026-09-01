---
title: "Cycle 8 / 3rd-loop Cycle 3 — the naturalization question (B) reduces to (A): recognizable variations are one-sided, fail the tight-window upper bound; the wall's binding barrier simplifies to (A)"
cycle: 8
loop: 3
date: 2026-08-23
tags: [honest-ceiling, ilango-2020, ac0-tight-window, ppoly-recognizable, s1a-antiprox-obstruction, s1a-lupanov-only-rng, witness-needs-explicit-lb, naturalization-open-question, gate-1-residual-is-naturalization, gate-1-automatic, lupanov-plausibly-nonnatural, lupanov-largeness-violated, two-gates-overcounted, wall-collapses-to-derandomization, ilango-recognizable-modification-loses-hardness, recognizable-variations-one-sided, tight-window-upper-bound-linchpin, b-reduces-to-a, b-existence-yes-b-usability-likely-no, wall-collapses-to-a, cwy-2023-blackbox, q-targetability-resolved, wall-stays-loosened, third-loop-cycle-3, main-loop, no-subagents]
status: raw
---

# Cycle 8 — the naturalization question (B) reduces to (A)

## The question Cycle 8 set out to answer

Cycle 7 (`sources/2026-08-23-two-gates-overcounted.md`) collapsed the two-gate wall to two tasks: **(A)** derandomize the Lupanov sampler (= the `[s1a-antiprox-obstruction]` = a fine-grained DNF LB for an explicit function in the tight window = the circuit-LB frontier = S1.b′) + **(B)** prove the Lupanov/direct-sum LB is genuinely non-naturalizing (Ilango's own open question, ECCC TR20-183 line 615). Cycle 7 named the residual Gate-1 risk as exactly (B): does the Lupanov/direct-sum tight-window LB admit a (P/poly)-recognizable variation S′ (Ilango's Smolensky-style caveat, lines 620–625), and if so does it re-tighten Gate 1?

Cycle 8 attacks (B) directly: **does the Lupanov/direct-sum tight-window LB admit a (P/poly)-recognizable variation, and if one exists, can it re-tighten Gate 1?**

## Finding 1 — Ilango's OWN caveat answers the re-tightening sub-question: a recognizable modification S′ (likely) loses the ability to prove (C)-MCSP hardness `[ilango-recognizable-modification-loses-hardness]`

Re-reading Ilango §1.4 (`_tr20-183.txt`, content-lines 620–629) VERBATIM (file-line offset located via `grep -n "recognizable"`; the recognizability definition sits at file-line 1012 = content-line 566, `sed -n '1000,1130p'`):

> "Caveats. Even though a collection of lower bound statements S might not be (P/poly)-recognizable, it is possible that there is a variation S′ of S that is (P/poly)-recognizable and still captures all the 'interesting' lower bounds given by S. A situation like this occurs in Razborov and Rudich's paper where they show how to modify Smolensky's [32] lower bound against AC⁰[p] circuits to fit into the natural proofs framework, even though it is unclear whether Smolensky's original method is constructive. **That being said, if a collection of lower bound statements S is used to prove hardness for (C)-MCSP, then any (P/poly)-recognizable modification S′ (likely) loses the ability to prove hardness of (C)-MCSP, so it seems like some 'interesting' lower bounds must be lost in this case.**" (lines 620–629)

This splits (B) into two sub-questions — and answers one of them:
- **(B-existence):** does a (P/poly)-recognizable variation S′ of the Lupanov LB exist? — *Open* (Ilango's analogy to Smolensky suggests plausibly yes).
- **(B-usability):** even if S′ exists, is it *usable to prove (C)-MCSP hardness* (i.e., retain the "interesting" LBs the reduction needs, hence re-tighten Gate 1)? — **Ilango: (likely) NO.** A recognizable modification S′ (likely) loses the ability to prove (C)-MCSP hardness.

The residual Gate-1 risk Cycle 7 flagged ("a recognizable S′ usable in the reduction ⇒ Ilango collapse ⇒ re-tightening") requires BOTH (B-existence)=yes AND (B-usability)=yes. Ilango's caveat directly addresses (B-usability) and says (likely) no. So the re-tightening scenario is, per the author of the barrier, **(likely) blocked**. The hedge ("(likely)", "it seems like") is carried as the honest residual.

## Finding 2 — the mechanism, grounded in the landscape: recognizable natural properties that EXIST against AC⁰/formulas are ONE-SIDED (lower-bound only), and fail the tight-window UPPER bound `[recognizable-variations-one-sided]` `[tight-window-upper-bound-linchpin]` `[cwy-2023-blackbox]`

Why would a recognizable S′ lose the ability to prove (C)-MCSP hardness? The mechanism is visible in the actual landscape of recognizable lower-bound properties:

- **Chen-Williams-Yang ITCS 2023** (`[cwy-2023-blackbox]`, already cited in Cycle 3 for black-box constructivity; web-confirmed, search/arXiv-summary-level, NOT PDF-line-verified): **Theorem 1.8** — DTIME[polylog(N)]-natural (= (P/poly)-recognizable, since polylog(N)=poly(n) with O(log N) advice) properties useful against **fixed-polynomial-size AC⁰** EXIST (via pseudorandom restrictions with logarithmic seed length); **Theorem 1.7** — exist against n^{2−ε}-size formulas; **Theorem 1.11** — bootstraps n^{2+ε} → n^k. So **recognizable natural properties against AC⁰/formulas DO exist** (at fixed-polynomial sizes). This makes **(B-existence) lean YES** — a Smolensky-style recognizable variation plausibly exists.

- **But these recognizable natural properties are ONE-SIDED.** A natural property "useful against size-s C" certifies complexity > s — a **lower-bound** property. It says nothing about the function being EASY at some slightly larger size. The Lupanov tight-window LB requires BOTH a lower bound (hard below (1−4δ)T) AND an **upper** bound (easy at (1+4δ)T) — the constructive/free side from Lupanov (Claims 30–31, `[s1a-lupanov-only-rng]`). A one-sided recognizable natural property gives the lower-bound side but **fails the upper-bound side** — exactly the "all-hard" failure mode of Sipser/RST that motivated the tight-window gate (Gate 2, Cycle 1, `sources/2026-08-23-ac0-escape-hatch.md`).

- **So a recognizable S′ (one-sided, lower-bound) is a BROADER, coarser property** that accepts all hard-below-T functions, including all-hard functions (Sipser/RST) that do NOT satisfy the tight window. It does NOT pin the narrow band [(1−4δ)T,(1+4δ)T]. The reduction's correctness needs the tight-window witness specifically (the upper bound pins g to be easy at (1+4δ)T, which is what makes the Lupanov construction work as the reduction's witness). Hence a one-sided recognizable S′ **cannot substitute in the reduction** — confirming Ilango's "(likely) loses the ability to prove (C)-MCSP hardness" with a CONCRETE MECHANISM (one-sidedness → fails the tight-window upper bound → can't pin the reduction's witness).

## Finding 3 — (B)'s re-tightening branch requires recognizing the tight window, which is ≥ (A) `[b-reduces-to-a]` `[wall-collapses-to-a]`

The ONLY way a recognizable variation could re-tighten Gate 1 is if it pins the tight window — i.e., recognizes BOTH the lower bound (hard below (1−4δ)T) AND the upper bound (easy at (1+4δ)T) from the truth table:
- Recognizing the **lower-bound side** ("hard below (1−4δ)T") from the truth table = certifying NO small circuit exists = a fine-grained LB decision = the `[s1a-antiprox-obstruction]` = **(A)** = the circuit-LB frontier.
- Recognizing the **upper-bound side** ("easy at (1+4δ)T") from the truth table = certifying a circuit of size (1+4δ)T EXISTS = a (C)-MCSP-type YES decision (the very problem the reduction reduces TO; believed hard).
- Recognizing the tight window (the narrow band) requires BOTH — at least as hard as recognizing the lower bound, which is (A). Moreover, a recognizability decision over ALL truth tables is a STRONGER requirement than an existential construction of ONE good g (which is what (A) is): recognizing ≥ constructing for the lower-bound side. So **(B-re-tightening) ⟹ (A)**, indeed ⟹ something at least as hard as (A).

**Net structural conclusion:** the residual Gate-1 risk (B) is NOT an independent obstacle below the (A) frontier:
- Where (B) is (likely) blocked (Ilango's caveat): recognizable S′ is one-sided, fails the tight window, can't prove the hardness — no re-tightening. `[b-existence-yes-b-usability-likely-no]`
- Where (B) is not blocked: a recognizable S′ that pins the tight window requires recognizing the fine-grained LB = ≥ (A) = the circuit-LB frontier. `[b-reduces-to-a]`
- Either way, the wall's binding barrier is **(A)**, not (A)+(B). Cycle 7's "(A)+(B)" simplifies to **essentially (A)**, with (B) (likely) not independently binding and otherwise absorbed into (A). `[wall-collapses-to-a]`

## The unification: the tight-window UPPER bound is the linchpin coupling Gate 1 and Gate 2 `[tight-window-upper-bound-linchpin]`

A single feature — the **upper-bound side of the tight window** (g easy at (1+4δ)T, the Lupanov constructive side, Claims 30–31) — is what couples the two gates:
- It is what **Sipser/RST fail** (they are all-hard; no upper bound at the tight size) → blocks the existing explicit LBs from being tight-window witnesses (Gate 2, Cycle 1).
- It is what **recognizable natural properties fail** (they are one-sided, lower-bound only; CWY23) → blocks recognizable variations from substituting in the reduction (Gate 1 residual, this cycle).
- Recognizing/pinning it (to make a recognizable tight-window property) is the antiprox obstruction + an MCSP-type upper check = ≥ (A).

So Lupanov's specific contribution (the constructive upper bound at (1+4δ)T) is the single feature that makes the tight window, and recognizing/pinning that upper bound is the hard part = (A). The two gates, which Cycle 1 framed as "partly independent" and Cycle 7 refined to "coupled via the Lupanov method," are now seen to be coupled via this ONE feature — the tight-window upper bound.

## Consistency with prior cycles

- **Cycle 6** (`[vicinity-does-not-retighten]`): Williams' (⇒) guaranteed recognizable property is for a generic h, one-sided (no tight window), not AC⁰-constructible — the SAME mechanism (a one-sided recognizable property that fails the tight window does not re-tighten). Cycle 8 generalizes this from "Williams' (⇒) vicinity-recognizability" to "ANY recognizable variation (CWY23-style or Smolensky-style)" — all are one-sided and fail the tight window.
- **Cycle 1** (`[ac0-tight-window]`, Gate 2): Sipser/RST fail the tight-window upper bound. Cycle 8: recognizable variations fail the SAME upper bound. The tight-window upper bound is the common blocker of both the existing LBs (Gate 2) and the recognizable variations (Gate 1 residual).
- **Cycle 7** (`[wall-collapses-to-derandomization]`): wall = (A)+(B). Cycle 8: (B) reduces to (A) / (likely) blocked → wall = essentially (A). A consistent DEEPENING (sharpening), not a contradiction — Cycle 7 already said (B) is open and flagged it as the residual; Cycle 8 resolves the residual as (likely) non-independent.

## What this changes in the map

1. **The wall's binding barrier simplifies from (A)+(B) (Cycle 7) to essentially (A).** (B) is (likely) not independently binding (Ilango's caveat + one-sidedness), and where it would bind it is ≥ (A). The wall is one task: derandomize the Lupanov sampler / produce an explicit tight-window DNF LB = the circuit-LB frontier.
2. **Gate 1's residual risk (the naturalization question) is discharged (likely) from a THIRD direction.** Cycle 6 (Williams' (⇒) non-targetability — the specific g), Cycle 7 (Ilango's automaticity — the general filter), Cycle 8 (recognizable variations are one-sided and fail the tight window — the variation landscape). Three independent soft-discharges.
3. **Gate 1 and Gate 2 are coupled via a single feature** — the tight-window upper bound — not two independent gates (Cycle 1) nor two coupled tasks (Cycle 7), but one linchpin feature. The map is now at maximum structural compression: one wall, one linchpin feature, one frontier task (A).
4. **The near-term tractable seam is unchanged** (a structurally-different uniform-AC⁰ reduction / Tell's promise derandomization). The long-term breakthrough shape is unchanged: an explicit tight-window DNF LB (= (A)).

## Honest scope `[honest-ceiling]`

- **Primary-source-grounded:** Ilango §1.4 lines 620–629 read VERBATIM (the recognizable-modification-loses-hardness caveat). The one-sidedness of recognizable natural properties is the standard definition of "useful against size-s" (a lower-bound property). CWY23 Thm 1.7/1.8/1.11 are web-confirmed (search/arXiv-summary-level, NOT PDF-line-verified).
- **Structural interpretation, not a new theorem:** the (B)→(A) reduction is a STRUCTURAL argument — "recognizing a fine-grained tight-window LB from the truth table is ≥ constructing one (A); the existing recognizable properties are one-sided and fail the tight window" — sound but not a formal theorem about THIS specific Lupanov S. The "recognizing ≥ constructing" step for the lower-bound side is a general principle (a recognizer accepting the witnessing set is a certificate; producing a witness is existential), reasonable but not formally proved for this S.
- **Ilango's "(likely)" hedge is the residual:** the conclusion that (B) is not independently binding rests on Ilango's "(likely) loses the ability" (lines 626–629) + the one-sidedness mechanism. A clever recognizable relaxation that pins the tight window via some proxy NOT requiring (A) is NOT ruled out — that is exactly what Ilango's "(likely)" hedges. If such a relaxation exists AND is usable in the reduction AND is achievable below the (A) frontier, (B) would re-tighten as an independent obstacle. This is not ruled out; it is judged (likely) not the case, per the author and the landscape.
- **(A) is still the circuit-LB frontier, unsolved.** No breakthrough. The wall stands. The deliverable is a sharper map: the wall's binding barrier is (A); Gate 1's residual (B) is (likely) non-independent (discharged soft from three directions); Gate 1 and Gate 2 are coupled via one feature (the tight-window upper bound).

## Net

No breakthrough (no P≠NP proof, no new circuit LB, no derandomization, no explicit witness). The wall is unchanged at (A) = the circuit-LB frontier. But the map sharpens: (B) — the residual Gate-1 risk Cycle 7 named — is (likely) non-independent (Ilango's own caveat + the one-sidedness of existing recognizable properties), and where it would bind it is ≥ (A). The wall's binding barrier simplifies from (A)+(B) to essentially (A). Gate 1 is now discharged soft from THREE directions (Cycle 6 + Cycle 7 + Cycle 8). The two gates are coupled via a single linchpin feature (the tight-window upper bound). More optimistic in STRUCTURE (one binding task, not two; one linchpin feature, not two gates), equally honest in DIFFICULTY ((A) is the circuit-LB frontier; Ilango's "(likely)" hedge is the residual; (B-existence) remains open but (likely) irrelevant to re-tightening).

## What this means for the remaining cycles

The wall is now maximally compressed to (A) = the circuit-LB frontier = derandomize the Lupanov sampler = an explicit tight-window DNF LB. The remaining third-loop cycles (9, 10) should either:
- **Attack (A) from a new angle** — e.g., is there a structurally-different route to an explicit tight-window DNF LB that does NOT go through derandomizing Lupanov (e.g., a direct combinatorial construction of a tight-size-at-fixed-depth AC⁰ function, the open problem Cycle 1 named)? Or
- **Stress-test the "(likely)" hedge** — is there a recognizable relaxation that pins the tight window via a proxy, re-tightening (B) as an independent obstacle? (Either outcome informative.)
- **Synthesize** (Cycle 10) the third loop: the wall driven from "two independent gates" (Cycle 1) → "two coupled tasks (A)+(B)" (Cycle 7) → "one task (A), one linchpin feature, Gate 1 soft from three directions" (Cycle 8).

## Sources
- Ilango, "Constant Depth Formula and Partial Function Versions of MCSP are Hard," FOCS 2020 / SIAM J. Comput. 2022 (ECCC TR20-183), §1.4 (lines 620–629 verbatim). https://www.rahulilango.com/papers/FOCS2020.pdf
- Chen, Williams, Yang, "Black-Box Constructive Proofs Are Unavoidable," ITCS 2023 (Thm 1.7/1.8/1.11). https://doi.org/10.4230/lipics.itcs.2023.35
- Prior wiki sources: `2026-08-23-two-gates-overcounted.md` (Cycle 7), `2026-08-23-ac0-escape-hatch.md` (Cycle 1, Gate 2 / tight window), `2026-08-23-q-targetability-resolved.md` (Cycle 6, vicinity-recognizability does not re-tighten), `2026-08-21-s1a-primary-source.md` (Lupanov Claims 30–31 / antiprox).