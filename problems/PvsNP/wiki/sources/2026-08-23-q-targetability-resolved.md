---
title: (Q-targetability) resolved — Williams' (=>) accepts a structurally-determined function, not an arbitrary g; the wall stays loosened
cycle: 6
loop: 3
date: 2026-08-23
tags: [q-targetability-resolved, williams-iff-non-targetable, vicinity-does-not-retighten, wall-stays-loosened, retargeting-circular-confirmed, single-lb-implies-class-lb, williams-iff-vicinity, targetability-circularity, wall-pinned-to-targetability, wall-loosened-not-fallen, tension-not-definitional, honest-ceiling, third-loop-cycle-1, main-loop, no-subagents]
provenance: "Third 5-cycle loop, Cycle 1. Main loop, no subagents (HTTP 429 persists). Source-grounded: Williams 2016 Thm 3.2/3.3 construction obtained via search of the paper's proof structure (arXiv:1212.1891 / SIAM J. Comput. 2016), NOT PDF-line-verified. Honors [honest-ceiling]: no fabricated proof; faithful reporting; resolves a previously-flagged open question, does not claim a breakthrough."
---

# Cycle 6 — (Q-targetability) RESOLVED: Williams' (=>) accepts a structurally-determined function, not an arbitrary g; the wall stays loosened

## What Cycle 6 attacks

The second loop's synthesis (`sources/2026-08-23-second-loop-synthesis.md`) named a single actionable next verification as its product: **(Q-targetability)** — is Williams' Theorem 1.1 (⇒) (class LB ⟹ recognizable useful property) **retargetable onto a specific chosen hard function** *f* (taking *f*'s hardness as input), or does it produce a recognizable property only for an **unspecified/generic** NEXP hard function *h*? Cycle 4 (`sources/2026-08-23-boundary-case-targetability.md`) had flagged this as the precise locus on which the wall's status turns — *soft* (Cycle 3's loosening survives) iff Williams' property is generic; *hard* (re-tightening, the Ilango collapse) iff it can be retargeted onto the specific S1.a witness g. Cycle 4's own reasoning (a circularity: retargeting onto g requires g's LB, but a recognizable g-LB already collapses and a non-recognizable one can't be the retargeting certificate) favored "generic," but was reasoning from the search-level theorem *statement*, not the construction. Cycle 6 obtains the actual construction and resolves it.

## The actual (⇒) construction (Williams 2016, Theorem 3.2 / 3.3)

Obtained via search of the paper's proof structure (arXiv:1212.1891, "Natural Proofs versus Derandomization," SIAM J. Comput. 2016). The forward direction NEXP ⊄ C ⟹ recognizable useful property proceeds:

- **Theorem 3.1 (on IKW 2002):** NEXP ⊄ C ⟺ NEXP lacks C-witnesses of every polynomial size (a "C-witness" is an NEXP-verifier witness whose truth table is computable by a small C-circuit; "oblivious" = one circuit family per input length).
- **Theorem 3.2, direction (1)⇒(2) — the core construction.** Given the witness lower bound (NTIME[2^{O(n)}] lacks s(cn)-size C-witnesses), there is a **good predicate V** (an NEXP verifier, running in TIME[2^{dn}]) with no small-circuit witnesses. The construction then identifies (existentially) an **infinite subsequence of "bad" inputs {x'ᵢ}**: each x'ᵢ ∈ L(V) is a YES-instance, and **every** accepting witness y for V(x'ᵢ, y) requires C-circuit complexity > s(c·|x'ᵢ|). The recognizable property is then:
  > **P(f) = 1  iff  V(x'ᵢ, f) accepts**  (viewing f's truth table as a witness y), with x'ᵢ supplied as **O(log n) advice** (specified by its index).
  - *Accepts ≥1 function:* x'ᵢ ∈ L(V), so some witness f exists ⇒ P(f)=1.
  - *Rejects all easy:* x'ᵢ is bad, so every accepted witness has C-complexity > s ⇒ P rejects all ≤s-size C-functions.
  - *P/poly-computable:* V runs in 2^{O(n)} = poly(truth-table length) time; advice is O(log n).
- **Theorem 3.3 — the universal HISTORY property.** To get one property useful against all polynomial sizes, Williams uses SUCCINCT HALTING (NEXP-complete) and defines HISTORY(y): accept iff some prefix y' of y (|y'| a power of two) encodes an **accepting computation history** of an NTM M(x) within n steps. The accepted function is an **accepting computation history of a nondeterministic Turing machine**.

**The function Williams' (⇒) accepts is therefore structurally determined:** an **accepting witness of an NEXP verifier V on an existentially-found "bad" input x'ᵢ** (Thm 3.2), or an **accepting computation history of an NTM** (Thm 3.3, the universal version). It is NOT an arbitrary chosen hard function — it is whatever accepting witness/computation-history the construction's bad-input subsequence yields.

## Resolution of (Q-targetability): NOT targetable onto an arbitrary g `[williams-iff-non-targetable]`

The construction makes the resolution decisive:

1. **The accepted function is fixed by the construction, not chosen.** The property P accepts the accepting witness(es) of V on a bad input x'ᵢ; x'ᵢ is found *existentially* ("there is an infinite subsequence of inputs {x'ᵢ} such that..."), specified to the algorithm only by an O(log n) index. You do not get to declare "let the accepted function be g." The accepted function is an accepting-witness-of-V / an accepting-computation-history — a specific structural kind, not a parameter of your choice.

2. **Retargeting onto a specific g requires engineering V so that g's truth table is the accepting witness of a bad input** — and that requires *proving* the input is "bad" (every accepting witness has high C-complexity), which in the case where g is the intended witness requires **proving g has high C-complexity** = g's lower bound. `[retargeting-circular-confirmed]` A recognizable g-LB makes the engineered property recognizable ⟹ collapse (Ilango); a non-recognizable g-LB cannot serve as the certificate that the engineered input is bad. So the re-tightening scenario is **circular**, exactly as Cycle 4 reasoned — now grounded in the actual construction: the construction's "bad input" certificate IS a high-complexity lower bound, and targeting g requires that lower bound to be the construction's input, which is the very recognizability in question.

3. **The accepted function is a different object from the reduction's witness g.** Williams' (⇒) function is an NEXP computation history / V-witness — *one-sided-hard* (C-complexity > s; no upper bound, no two-sided tight window) and *not AC⁰-constructible* (it is an NEXP computation, not a uniform-AC⁰-computable function). The S1.a reduction's witness g is required to be **AC⁰-constructible AND tight-window** (hard at (1−4δ)T, easy at (1+4δ)T). The two are different objects with different requirements. `[vicinity-does-not-retighten]`

## The Ilango collapse is specific to the reduction's witness, not any recognizable property

The decisive logical point (re-examined against the construction): the Ilango collapse (`[ppoly-recognizable]`, Cycle 1, line-verified against Ilango §1.4) is triggered when the **LB collection used in the reduction's correctness proof** is (P/poly)-recognizable — i.e. when the **reduction's specific witness's** LB (g's, at the tight window) is recognizable. Williams' (⇒) guarantees a recognizable property Π* for a **different** function h (an NEXP computation history / V-witness), found by its own machinery. Π* being recognizable does **not** make g's LB collection recognizable — they accept different functions, and the collapse algorithmizes the *reduction's* correctness (about g), not Π* (about h). A recognizable property for h cannot substitute for a recognizable LB for g in the reduction's correctness proof, because the reduction's correctness is a statement about g's tight-window complexity, and Π* certifies nothing about g's window. So the existence of Π* (guaranteed by Williams ⇒, because g ∈ NEXP makes the class LB true, Cycle 4) does **not** collapse SAT.

## Net: the wall stays loosened; Cycle 3's "possible-in-principle" is UN-conditioned `[wall-stays-loosened]` `[q-targetability-resolved]`

Cycle 4 had found that g ∈ NEXP makes the S1.a LB entail the class LB, and Williams' IFF then guarantees a recognizable property EXISTS in the vicinity — a partial walk-back of Cycle 3's "no theorem forces recognizability here." Cycle 6 resolves the open question that walk-back raised:

- **Williams' guaranteed recognizable property is for a structurally-determined, existentially-found function (an NEXP computation history / V-witness), NOT for the reduction's specific witness g.** It cannot be retargeted onto g without g's own LB (circular). It certifies a different function with different (one-sided, non-AC⁰-constructible) properties.
- **Therefore the vicinity-recognizability does NOT re-tighten the wall.** The recognizable property Williams guarantees and the reduction's specific witness are **different objects** (existence-of-a-useful-property ⟂ construct-a-specific-witness — exactly the `[witness-needs-explicit-lb]` gap). The Ilango collapse needs the *reduction's witness's* LB to be recognizable; Williams gives a recognizable property for *another* function.
- **Cycle 3's "possible-in-principle" is therefore UN-CONDITIONED.** The breakthrough shape — a non-recognizable explicit-f tight-window AC⁰ LB — remains certified possible-in-principle, **no longer conditional on Williams' (⇒) being non-retargetable** (Cycle 6 confirms it is non-retargetable). The wall is blocked *only* by (i) the empirical absence of a non-recognizable explicit-f LB method (the natural-proofs frontier) and (ii) Gate 2, the tight-window explicit construction (`[ac0-tight-window]`) — NOT by the constructivity-forcing theorem, whose guaranteed recognizable property provably lives at the wrong function.

This is a genuine advance over the second loop's end-state: it **closes the one flagged open question** (the second loop's honest-scope left (Q-targetability) as the unresolved pivot) and **strengthens the conclusion** from "possible-in-principle, *conditioned* on (Q-targetability) = generic" (Cycle 4) to "possible-in-principle, *un-conditioned*" (Cycle 6), with the resolution source-grounded in the actual (⇒) construction. The wall's recognizability gate (Gate 1) is now **fully resolved as soft**; the live blockers are Gate 2 (tight-window) and the empirical method-gap, both located exactly.

## What this means for the remaining cycles

With Gate 1 resolved soft, the third loop's leverage shifts to:
- **Gate 2 (tight-window)** — the now-primary gate: is an explicit function with multiplicatively-tight AC⁰ complexity at fixed depth constructible, or is tight-window itself theorem-blocked? (Cycle 1 noted Sipser/RST are one-sided-hard, failing the upper-bound side; no known tight-size-at-fixed-depth AC⁰ function.)
- **The empirical method-gap** — a non-recognizable explicit-f LB *method* (Cycle 3's "genuinely new LB method certifying a specific explicit function hard WITHOUT a P/poly-checkable separator from the easy functions"). Gate 1 being soft confirms this gap is empirical (not theorem-forced), but does not fill it.

Cycle 6 thus **refocuses** the third loop: the recognizability question is closed (soft, un-conditioned); the tight-window and method-gap questions are now the live targets.

## Honest scope `[honest-ceiling]`

- **No breakthrough.** No P≠NP proof, no new circuit LB, no derandomization, no explicit witness. The product is the resolution of a previously-flagged open question, refining the map.
- **Source-grounded but NOT PDF-line-verified.** The (⇒) construction (Thm 3.2/3.3: the bad-input x'ᵢ, the V-witness property P, the universal HISTORY/accepting-computation-history) was obtained via a search that returned the paper's proof structure (from arXiv:1212.1891 / the paper's exposition). The *targetability* conclusion (accepted function is structurally fixed, not arbitrarily chosen) follows directly from that construction and from the existential wording ("there is an infinite subsequence of inputs {x'ᵢ}"). It is robust to the construction's details. A line-check of Williams 2016 §3 would confirm; the resolution does not hinge on any detail I have not seen.
- **The circularity argument is now source-grounded.** Cycle 4 reasoned the retargeting was circular from the theorem *statement*; Cycle 6 grounds it in the *construction* (the "bad input" certificate IS a high-complexity lower bound; targeting g requires that bound as input). The circularity is not an assumption — it is the construction's structure.
- **One residual subtlety, FLAGGED.** Could one *engineer* the NEXP verifier V and a bad input so that g's truth table is its accepting witness, making Π* accept g? In principle this requires (a) an NEXP verifier accepting g's truth table, and (b) a *proof* that the input is bad (all its accepting witnesses, including g, have high C-complexity) = g's LB. (b) is the circular point: the badness proof IS g's LB. If g's LB is recognizable, the engineered Π* is recognizable (collapse); if non-recognizable, you cannot prove the input bad. So even the engineering route is circular — consistent with the resolution. Flagged, not exhaustively excluded (a clever encoding might evade the literal "bad input" framing), but the conclusion (non-targetable onto a non-recognizable g) is robust.
- **The one-sidedness of Williams' (⇒) function is a RED HERRING for the collapse question, correctly noted.** Williams' accepted function is one-sided-hard (no tight window). This does NOT block re-tightening by itself (if one could retarget onto g, the property would accept g — which independently has a tight window — and reject easy functions, yielding collapse regardless of one-sidedness). So the re-tightening is blocked **solely by non-targetability**, not by one-sidedness. The one-sidedness is a reason Williams' function is not *reduction-usable as a witness*, but not the reason the wall doesn't re-tighten. Recorded to avoid conflating the two.

## Net

The second loop's pivotal open question — (Q-targetability) — is **resolved**: Williams' (⇒) accepts a structurally-determined function (an NEXP computation history / V-witness on an existentially-found bad input), NOT an arbitrary chosen g; retargeting onto g is circular (requires g's LB as the construction's "bad input" certificate). The vicinity-recognizability (Cycle 4) therefore does **not** re-tighten the wall — the recognizable property Williams guarantees and the reduction's specific witness are different objects, and the Ilango collapse is specific to the reduction's witness's LB. **Cycle 3's "possible-in-principle" is UN-conditioned**: the breakthrough shape (a non-recognizable explicit-f tight-window AC⁰ LB) is certified possible-in-principle, blocked only by Gate 2 (tight-window) and the empirical non-recognizable-method gap — NOT by the constructivity-forcing theorem. Gate 1 (recognizability) is now **fully resolved as soft**. No breakthrough; the map is sharper and one open flag closed. `[honest-ceiling]`.

## Sources

- Williams, R. — "Natural Proofs versus Derandomization," arXiv:1212.1891 / SIAM J. Comput. 2016, Theorems 3.1, 3.2 (direction (1)⇒(2): the "bad input" x'ᵢ, the V-witness property P with O(log n) advice), 3.3 (the universal HISTORY property / accepting computation history), 1.1/1.2 (the IFF + advice removal). [construction obtained via search of the paper's proof structure; NOT PDF-line-verified]
- Cycle 4: `sources/2026-08-23-boundary-case-targetability.md` (posed (Q-targetability); the vicinity-recognizability; the circularity reasoning from the theorem statement).
- Cycle 3: `sources/2026-08-23-tension-not-definitional.md` (the "possible-in-principle" reclassification that Cycle 6 un-conditions).
- Cycle 1: `sources/2026-08-23-ac0-escape-hatch.md` (the Ilango §1.4 collapse, line-verified; the tight-window Gate 2).
- Second loop synthesis: `sources/2026-08-23-second-loop-synthesis.md` (named (Q-targetability) as the actionable next verification).
- Search results (this turn) returning Williams 2016 §3's proof structure (Thm 3.1/3.2/3.3, the bad-input construction, the HISTORY universal property).