---
cycle: 24
loop: 6
date: 2026-08-23
slug: disjoint-pairs-profile
tags: [sixth-loop-cycle-4, disjoint-pairs-stronger-not-easier, disjoint-pairs-relativize, disjoint-pairs-re-collapse-to-inseparable-pair, disjoint-pairs-inherit-rsc, disjoint-pairs-bridge-to-proof-complexity, proof-complexity-face-barriered, witness-needs-explicit-lb, measure-relativization-barrier, rsc-martingale-naturalproof-equivalence, measure-pivot-rediscovers-natural-proofs, no-missed-connection-moved-wall, three-barriers-required, honest-ceiling]
---

# Cycle 24 — barrier profile of the disjoint-pairs target

## Provenance

Continuation of the governing sixth-loop request ("continue making a real breakthrough or solve the problem"). Cycle 23 pivoted to resource-bounded measure / dimension (Lutz) and surfaced one genuinely new, unmapped falsifiable target — the 2022 Lutz-Lutz-Mayordomo disjoint-pairs characterization `dim(disjNP | disjEXP) = 1 ⟹ dim(NP | EXP) > 0 ⟹ P ≠ NP`. Cycle 24 maps that target's **barrier profile**: is proving `dim(disjNP | disjEXP) = 1` any easier than the measure hypothesis it implies, or does it re-collapse to the same construction/hardness lock, relativize, or fall to natural proofs?

## Source grounding

Web-search grounded (four searches); findings are search/arXiv-summary-level, NOT PDF-line-verified, per `[honest-ceiling]`. Sources: Lutz-Lutz-Mayordomo, *Dimension and the Structure of Complexity Classes*, TOCS 2022 / arXiv:2109.05956 (Thm 6.1; point-to-set principle Thm 4.2; Thms 6.2/6.3); Fortnow-Lutz-Mayordomo, *Inseparability and Strong Hypotheses for Disjoint NP Pairs*, 2009 / arXiv:0902.2674 (measure analogue 2012; μ(NP|EXP)≠0 ⟹ TIME(2^{n^k})-inseparable pairs; oracle separations); Fortnow-Rogers, *Separability and One-Way Functions*, Comp. Complexity 2002 (generic oracles settle all relativized separability relationships); Glaßer-Selman-Sengupta-Zhang, *Disjoint NP-Pairs* 2003; Glaßer-Selman-Zhang, *Canonical Disjoint NP-Pairs* 2004 / *Survey* 2005 (Razborov 1994 canonical pair (SAT*, REF_f); optimal proof system ⟹ canonical pair ≤_m^pp-complete; every disjoint NP pair ≡ a canonical pair → identical degree structure; uniform-enumerability equivalence Thm 6.5).

## Findings

### F1 — `[disjoint-pairs-stronger-not-easier]`
Thm 6.1 (Lutz-Lutz-Mayordomo 2022): **dim(disjNP | disjEXP) = 1 ⟹ dim(NP | EXP) > 0** (dimension analogue of Fortnow-Lutz-Mayordomo 2012: μ(disjNP|disjEXP)≠0 ⟹ μ(NP|EXP)≠0). The implication runs **from** the disjoint-pairs condition **to** the direct dimension hypothesis — so the disjoint-pairs condition is **STRONGER** than (implies) the thing it is meant to deliver. It is NOT an easier shortcut: a statement that *implies* the goal is, absent special structure, *harder* to prove than the goal. **Refines the Cycle-23 framing:** the "new falsifiable target" is a *stronger* sufficient condition with a different combinatorial shape (disjoint pairs), not a weaker/easier one. The shape difference (pairs + separability, vs. a single class's density) is the only candidate source of leverage, and F2–F5 below show it does not yield any.

### F2 — `[disjoint-pairs-relativize]`
The disjoint-pairs target **inherits the relativization barrier** — it does not escape `[three-barriers-required]` on the relativization axis:
- Fortnow-Rogers 2002 settle **all** relativized relationships among {P=NP, P=UP, P=NP∩coNP, all disjoint NP pairs P-separable, all disjoint coNP pairs P-separable} using generic oracles — oracles exist on **both sides** of the separability question.
- Glaßer et al. oracle O₂: complete disjoint NP pairs exist **but** optimal proof systems do NOT (Razborov's converse fails relativizably); oracle X: no Turing-complete pair, P≠UP, no optimal proof systems.
- Fortnow-Lutz-Mayordomo 2009: oracle separations showing most converses in the measure/inseparability chain fail relativizably.
Any proof of `dim(disjNP|disjEXP)=1` must therefore be **non-relativizing** — same axis-blocked status as the parent measure hypothesis `[measure-relativization-barrier]`.

### F3 — `[disjoint-pairs-re-collapse-to-inseparable-pair]`
Full dimension of disjNP within disjEXP means disjNP is **pseudorandom/dense** relative to disjEXP — no efficient gale succeeds betting that a typical disjoint EXP pair is *not* a disjoint NP pair. By the Cycle-23 crux `[rsc-martingale-naturalproof-equivalence]` (martingales ≡ natural properties), proving this density is a **hardness/pseudorandomness** statement, and its proof re-collapses to **exhibiting a hard object**. Here the hard object is a **P-inseparable (indeed TIME(2^{n^k})-inseparable) disjoint NP pair** (A, B) — two disjoint NP languages with no P-computable separator (Fortnow-Lutz-Mayordomo: μ(NP|EXP)≠0 ⟹ such pairs exist for every k). This is an **explicit construction of a differently-shaped witness**: a *pair* resisting P-separation, **not** the single balanced-point function (A) of the structural face. So the disjoint-pairs target re-collapses to the same unifying lock `[witness-needs-explicit-lb]`, but the witness has a different shape — and the construction is no less open for the different shape. The connection to one-way functions (P≠UP ⟹ P-inseparable pairs; P-inseparable pairs necessary for public-key crypto) confirms the **cryptographic-hardness / natural-proofs shape**: the inseparable pair is a hard object whose existence is the positive obverse of the natural-proofs barrier.

### F4 — `[disjoint-pairs-inherit-rsc]`
Natural-proofs barrier: **inherited**. The dimension statement is a density/pseudorandomness statement about disjNP; by RSC (Cycle 23) density ≡ martingale-resistance ≡ natural-property, so proving it re-encounters natural proofs exactly as the parent measure hypothesis did `[measure-pivot-rediscovers-natural-proofs]`. The disjoint-pairs target does not escape the natural-proofs axis.

### F5 — `[disjoint-pairs-bridge-to-proof-complexity]` (the genuinely new structural fact)
Razborov 1994: for every propositional proof system f, the **canonical pair** `(SAT*, REF_f)` is a disjoint NP pair, and **if f is optimal, (SAT*, REF_f) is ≤_m^pp-complete for DisjNP**. Glaßer-Selman-Zhang (2004, Thm 3.1): **every** disjoint NP pair is many-one equivalent to the canonical pair of *some* proof system → DisjNP and the canonical-pair degrees have **identical degree structure**. The disjoint-pairs question is therefore **equivalent (in degree structure) to the propositional-proof-system question**. Consequence for the map: the disjoint-pairs target is the **BRIDGE** connecting the measure surface (Cycle 23) to the proof-complexity surface — the latter was one of the four offered pivot surfaces, but it is **not a fresh surface**; it is the far end of a bridge whose near end (disjoint pairs) Cycle 24 has now mapped. "Pivot to proof complexity" would land on already-adjacent territory, not on genuinely-new ground.

### F6 — `[proof-complexity-face-barriered]`
The far (proof-complexity) end of the bridge is itself barriered and does not obviously escape the wall:
- Complete disjoint NP pairs ⟺ DisjNP **uniformly enumerable** (Glaßer-Selman-Sengupta Thm 6.5) — a condition judged **highly unlikely** (it would require a total computable listing of *exactly* all disjoint NP pairs).
- Optimal proof systems: oracles both ways (O₁ has them, O₂ does not) → **relativization-blocked**; existence implies ≤_m-complete sets for NP∩SPARSE (Meßner-Torán), which fails relative to O₂.
- Known proof-complexity lower bounds exist only for **weak** systems (resolution, cutting planes, bounded-depth Frege); the relevant strength (Frege / Extended Frege / optimal systems) is **open**.
- **Honest gap:** whether the proof-complexity face meets a *natural-proofs-style* barrier (in the proof-complexity sense) is NOT web-verified here — flagged as the one remaining unmapped piece of the disjoint-pairs bridge. (Razborov-style "pseudorandom" barriers for proof complexity are suspected but not confirmed by this cycle's searches.)

## Honest scope

NO BREAKTHROUGH. The disjoint-pairs target `dim(disjNP|disjEXP)=1` does **not** escape the wall on **any** of the three barrier axes: relativization blocked (F2), natural proofs inherited (F4), explicit construction re-collapsed — to a differently-shaped inseparable-pair witness — but re-collapsed nonetheless (F3). It is stronger, not easier, than the direct dimension route (F1). The cycle's one genuinely new product is **structural, not a crack**: the disjoint-pairs formulation is the bridge connecting the measure surface to the proof-complexity surface (F5), and the proof-complexity far end is itself barriered (F6). This **re-confirms `[no-missed-connection-moved-wall]`** from a third sub-surface (structural face → measure face → disjoint-pairs/proof-complexity bridge), and it **narrows the pivot options**: of the four original pivot surfaces, proof complexity is now shown to be adjacent (not fresh); the genuinely-untouched surfaces are descriptive complexity and (the already-partially-mapped) GCT/algebraic. `[honest-ceiling]` upheld.

## Net

Cycle 24 maps the disjoint-pairs target's barrier profile: stronger-not-easier (F1), relativization-blocked (F2), re-collapse to an inseparable-pair witness via RSC (F3/F4), and the proof-complexity bridge (F5/F6). The wall is confirmed from a third sub-surface and the pivot space narrows. New concept page `disjoint-np-pairs.md` created (the bridge node). (A) remains the single live thread (OPEN construction) from the structural side. Wiki state after Cycle 24: 18 pages, 40 sources, all wikilinks resolve.