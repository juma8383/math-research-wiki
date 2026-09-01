---
title: "Cycle 1 (2nd loop) — The AC⁰-model escape hatch: LB-existence gate passed, natural-proofs gate is the real wall"
date: 2026-08-23
cycle: 1
loop: 2
tags: [honest-ceiling, ilango-2020, witness-needs-explicit-lb, s1a-antiprox-obstruction, s1a-lupanov-only-rng, ac0-lb-existence-passed, ac0-natural-proofs-wall, ppoly-recognizable, ac0-tight-window, five-cycle-synthesis, sipser-rst-2015, parameterization-correction]
---

# Cycle 1 (2nd loop) — The AC⁰-model escape hatch

This is Cycle 1 of the user's second 5-cycle mandate ("continue the next best options on loop for 5 cycles to make a true breakthrough or solve the problem"). The first loop's synthesis (`sources/2026-08-23-five-cycle-synthesis.md`) concluded the frontier is one `[witness-needs-explicit-lb]` wall on two routes, and that the wall is "open construction, not proven impossibility." The highest-leverage way to *attack the wall itself* (rather than re-tread a lever) is to ask which **face** of the wall is thinnest and push there. This cycle does that — and **corrects an over-broad claim of the first loop's synthesis** in the process. `[honest-ceiling]` upheld: no breakthrough; the product is a primary-source-verified refinement that locates the natural-proofs frontier *exactly* in the AC⁰ model.

## The hypothesis that motivated the cycle

The first-loop synthesis states (and the orientation memory repeats): "best explicit is **polynomial** — linear-general, cubic-formula; the exponential target 2^{Θ(L)} is exponentially far." This was stated as a **uniform** property of all three circuit models (DNF / general-circuit / formula). The hypothesis of this cycle: that blanket statement is **inaccurate for the AC⁰ model**. Sipser's function and the Håstad–Rossman–Servedio–Tan (RST) average-case depth hierarchy give **explicit exponential AC⁰ lower bounds** — so the AC⁰ face of the wall may be thinner than "LB-existence blocked," and the real obstruction there may be a *different, finer* gate. If so, the AC⁰ face (Ilango's `(AC⁰_d)-MCSP` reduction, sub-target S1.a) is the thinnest part of the wall and the right place to push.

## Finding 1 — explicit exponential + average-case AC⁰ LBs EXIST (LB-existence gate passed) `[ac0-lb-existence-passed]` `[sipser-rst-2015]`

**Verified (primary sources, web-confirmed):**
- **Håstad 1986 (worst case):** Sipser's function $f_{d,n}$ is a depth-$d$ read-once monotone formula with alternating AND/OR layers; any depth-$(d-1)$ formula computing it requires size $2^{\Omega(n^{1/(d-1)}/\mathrm{polylog})}$ — exponential, with an explicit construction and a *linear-size* depth-$d$ circuit computing it (so the upper bound at depth $d$ is small).
- **Rossman–Servedio–Tan, FOCS 2015 / JACM 2017 (average case):** the **average-case depth hierarchy theorem** — for every $d\ge 2$, Sipser$_d$ is computed by a linear-size depth-$d$ formula, and any depth-$(d-1)$ circuit *agreeing* with it on a $(1/2+o(1))$ fraction requires size $\exp(n^{\Omega(1/d)})$. I.e. an **explicit average-case-hard** function for $AC^0_{d-1}$ with a **known small (linear) upper bound** at depth $d$. Valid for $2\le d\le c\sqrt{\log n/\log\log n}$. Technique: random projections (a generalization of random restrictions).

**Why this matters for S1.a's parameterization (the correction).** The witness barrier's "exponential in $L$" target has **different parameterizations per sub-target**, which the first-loop synthesis conflated:
- **S2 (general circuit):** the witness is a function on $L=O(\log n)$ bits; target general-circuit complexity $2^{\Theta(L)}$; best explicit $\Theta(L)$ (Blum 1984). **LB-existence blocked** (polynomial).
- **S3 (formula):** the witness is a function on $m=O(\log N)$ bits; target formula complexity $2^{\Theta(m)}$; best explicit $\tilde\Omega(m^3)$ (Håstad 1998 / Filmus-Meir-Tal 2023). **LB-existence blocked** (polynomial).
- **S1.a (AC⁰, DNF):** the witness $g$ lives on $N=\Theta(n^2)$ bits (Lemma 26: $m=n^2/\delta$); the target complexity is the tight window $[(1-4\delta)t\!\cdot\! n^2,\,(1+4\delta)t\!\cdot\! n^2]$ with $t\in[n^{8/\delta},2^n]$, i.e. up to $\approx 2^n\!\cdot\! n^2 = 2^{\Theta(\sqrt N)}\!\cdot\! N$. Sipser/RST gives an explicit $AC^0_{d-1}$ LB of $2^{N^{\Omega(1/(d-1))}}$ — for $d=3$ this is $2^{\Theta(\sqrt N)}$, **in the right ballpark as the target's upper end**. So **LB-existence is NOT blocked for S1.a**: an explicit exponential-(in-$\sqrt N$) AC⁰ LB exists, within the same order of magnitude the reduction's window reaches.

`[ac0-lb-existence-passed]`: **the AC⁰ face of the wall passes the LB-existence gate.** The first-loop synthesis's blanket "all three stuck at polynomial best-explicit" is **correct for S2/S3 and WRONG for S1.a**. Recorded as a correction (not retroactive — the synthesis and the S3 source are immutable; this source records the correction against them). `[parameterization-correction]`

So the AC⁰ face is genuinely the **thinnest** part of the wall: at S2/S3 we cannot even exhibit an exponential witness; at S1.a we *can* exhibit one of the right magnitude. The question becomes: why does the existing explicit AC⁰ LB not fall the wall?

## Finding 2 — the existing AC⁰ LBs are (P/poly)-recognizable ⇒ natural-proofs-blocked `[ppoly-recognizable]` `[ac0-natural-proofs-wall]`

**Verified against the primary source** (`sources/_tr20-183.txt`, Ilango FOCS 2020 / SIAM J. Comput. 2022, §1.4 "When can lower bounds be used to prove hardness?", lines 40-46, 565-591, 620-629 — quoted verbatim below):

> (Abstract, lines 40-46) "we formulate a notion of lower bound statements being **(P/poly)-recognizable** that is closely related to Razborov and Rudich's definition of being (P/poly)-constructive. We show that **unless there are subexponential-sized circuits computing SAT, the collection of lower bound statements used to prove the correctness of our reductions cannot be (P/poly)-recognizable**."

> (Lines 565-572) "a collection of lower bound statements $S$ against a circuit class $\mathcal C$ is **(P/poly)-recognizable** if there exists a family of polynomial-sized circuits that accepts all elements of $S$ and rejects all the YES instances of $(\mathcal C)$-MCSP. … under widely believed complexity assumptions, one should not be able to prove hardness for $(\mathcal C)$-MCSP using (P/poly)-recognizable collections of lower bound statements … many lower bound methods we know, like **Håstad's switching lemma, yield collections of lower bound statements that are (P/poly)-recognizable**."

> (Lines 589-591) "any proof requires considering lower bounds of **a slightly different flavor than many existing lower bound techniques**."

> (Lines 620-629, caveat) a non-recognizable $S$ *might* have a recognizable variation $S'$ that still captures the "interesting" bounds — but "if a collection $S$ is used to prove hardness for $(\mathcal C)$-MCSP, then any (P/poly)-recognizable modification $S'$ (likely) loses the ability to prove hardness."

**The mechanism, made explicit.** The `(AC⁰_d)`-MCSP reduction $R:\mathrm{SAT}\to (\mathcal C)\text{-MCSP}$ is correct *because* a lower bound holds (the lifting theorem: $g$ is hard for $AC^0_{d-1}$). If the collection of LB statements certifying that hardness is **(P/poly)-recognizable** — i.e. a polynomial-size circuit family can recognize "this $(f,s)$ pair is a valid LB" — then that circuit family can be **algorithmized** and plugged *back into* $R$ to yield **a subexponential-size circuit computing SAT**. That is an *upper bound on SAT* (SAT $\in$ subexp-circuits) — the **opposite direction** from the P$\ne$NP separation Route A wants. So:

`[ppoly-recognizable]` `[ac0-natural-proofs-wall]`: **the known explicit AC⁰ LBs — Sipser/RST, proven via Håstad's switching lemma / random projections — are (P/poly)-recognizable, hence natural (constructive). Using them as the witness for the `(AC⁰_d)`-MCSP reduction would (under the reduction) yield SAT$\in$subexp-circuits, i.e. a *collapse*, not the *separation* Route A targets. They are therefore useless for the P$\ne$NP goal despite existing at the right magnitude.** Route A requires a **non-(P/poly)-recognizable** — i.e. **non-natural** — explicit exponential AC⁰ LB. This is the natural-proofs frontier (Razborov-Rudich's constructivity condition, here in the (P/poly)-recognizable form), now located **exactly** in the AC⁰ model — the thinnest face of the wall.

This is the precise content of why "having an explicit exponential AC⁰ LB" does **not** fall the wall: the LBs we *have* are natural; a natural LB, plugged into the reduction, proves the negation of the target.

## Finding 3 — the S1.a obstruction is a TWO-GATE wall, not one `[ac0-tight-window]`

Combining Findings 1–2 with the first-loop S1.a analysis (`[s1a-antiprox-obstruction]`), the AC⁰ face of the wall is now resolved into **two distinct gates**, both open:

1. **The natural-proofs / (P/poly)-recognizability gate** `[ac0-natural-proofs-wall]` (Finding 2): the LB must be **non-natural** — its certified $(f,s)$ collection must not be (P/poly)-recognizable. The existing explicit exponential AC⁰ LBs (switching lemma) are natural and fail this gate.
2. **The tight-window / two-sided-precision gate** `[ac0-tight-window]` `[s1a-antiprox-obstruction]` (first loop, upheld): the LB must **pin** $g$'s $AC^0_{d-1}$ complexity in $[(1-4\delta)T,(1+4\delta)T]$ for *each* $T=t\!\cdot\! n^2$ — a **fine-grained complexity cliff at a tunable size**, not merely "high." Sipser/RST give *all-hard* functions (exponential at $AC^0_{d-1}$, no small $AC^0_{d-1}$ upper bound) — they satisfy the lower-bound side but **fail the upper-bound side** (the window needs $g$ *easy* at size $T$ *and* hard below it). No known explicit function has a known *tight size complexity at fixed AC⁰ depth* (switching lemma gives asymptotic, not tight-window, bounds).

`[ac0-tight-window]`: the two gates are **partly independent** — non-naturality is about the LB *method's recognizability*; the tight window is about the LB's *precision/tunability*. Both must be crossed. Crossing only one (e.g. a non-natural but coarse LB, or a tight-window but natural LB) does not suffice: the natural one collapses SAT; the coarse one breaks the reduction's threshold. This is sharper than the first-loop framing, which treated S1.a as a single "fine-grained DNF LB" obstruction.

## What this changes in the map

1. **A correction to the first-loop synthesis.** The blanket "all three circuit models stuck at polynomial best-explicit" is **wrong for the AC⁰ (S1.a) model**: explicit exponential (in-$\sqrt N$) AC⁰ LBs *exist* (Sipser/RST), in the right magnitude ballpark. The honest statement is: **S2 (general circuit) and S3 (formula) are blocked at LB-existence (polynomial best); S1.a (AC⁰) passes LB-existence and is blocked at two finer gates — the natural-proofs/(P/poly)-recognizability gate and the tight-window gate.** The AC⁰ face is the thinnest.
2. **The natural-proofs frontier is located *exactly* in the AC⁰ model.** The first loop knew the natural-proofs barrier "lurks behind" the wall (conditional on OWFs). This cycle makes it concrete: the very tool that gives the explicit exponential AC⁰ LB (Håstad's switching lemma) is, per Ilango §1.4, (P/poly)-recognizable and therefore *ruled out* as the reduction's witness. The frontier is not a vague backdrop; it is the specific statement "a **non-natural** explicit exponential AC⁰ LB in a tight window."
3. **Unification preserved, sharpened.** `[witness-needs-explicit-lb]` still governs all three faces, but the gate that blocks each face now differs: LB-existence (S2, S3) vs. {non-naturality, tight-window} (S1.a). The AC⁰ face is one gate-closer (LB-existence already crossed) but blocked at the natural-proofs gate — which is precisely where one would expect the wall to be hardest, since natural proofs are the canonical barrier and AC⁰ is the one class where they *work* (so the non-natural LB Route A needs is genuinely outside the standard toolbox).

## Honest scope `[honest-ceiling]`

- **No breakthrough.** No P$\ne$NP proof, no new circuit lower bound, no derandomization, no new MCSP NP-hardness was produced. The wall stands. The deliverable is a primary-source-verified *refinement*: the AC⁰ face is thinner than the first loop stated, and the blocking gate there is identified as the natural-proofs/(P/poly)-recognizability barrier (plus the tight-window gate), not LB-existence.
- **The "thinnest face" is a *directional* claim, not a distance.** Saying the AC⁰ face is "one gate closer" does **not** mean it is close to falling. The natural-proofs gate is the canonical barrier of the field; being blocked at it (rather than earlier, at LB-existence) is progress in *locating* the wall, not in *crossing* it. A non-natural explicit exponential AC⁰ LB in a tight window is not known and is not obviously approachable; this cycle did not produce one.
- **Primary-source-verified components:** the (P/poly)-recognizable definition, the SAT$\in$subexp consequence, and the "switching lemma is recognizable" attribution are verified verbatim against `_tr20-183.txt` (Ilango FOCS 2020 §1.4). The Sipser/RST LBs and the S1.a parameterization ($g$ on $N=\Theta(n^2)$ bits, window up to $2^{\Theta(\sqrt N)}$) are from the first-loop S1.a source (`_tr20-183.txt` Lemma 26) + web-confirmed Håstad/RST statements (RST details from the JACM 2017 / FOCS 2015 summaries, not the PDF line-by-line; the *existence* of the explicit exponential + average-case AC⁰ LB is textbook-settled and not in doubt, but the precise RST constants are search-summary-level).
- **Unverified/flagged.** The two-gate independence claim (non-naturality ⊥ tight-window) is a structural observation, not a theorem — a single construction might conceivably address both; stating them as independent gates is an organizing hypothesis, not proven. The "would yield SAT$\in$subexp-circuits (collapse, not separation)" framing follows Ilango's stated consequence (recognizable ⟹ SAT∈subexp) read against Route A's target (separation); it is a faithful reading, not a new derivation.
- **Relationship to the first-loop untried-lever #4** ("a structurally-different uniform-AC⁰ MCSP reduction = the compression crux = the breakthrough"). This cycle did *not* find such a reduction. It refined *why* the *existing* reduction (Ilango `(AC⁰_d)`) is blocked (natural-proofs gate on its witness), which is adjacent to but distinct from the compression crux (which is about constructing a *different* reduction). The two are related: a structurally-different reduction might use a non-natural witness by construction; but no candidate exists.

## Net

The AC⁰ face is the thinnest part of the `[witness-needs-explicit-lb]` wall: it is blocked at the **natural-proofs/(P/poly)-recognizability gate** (the known explicit exponential AC⁰ LBs are natural and would collapse SAT, not separate it) **and the tight-window gate**, *after* passing the LB-existence gate that blocks S2/S3. This corrects the first-loop synthesis's over-broad "polynomial best-explicit" claim and locates the natural-proofs frontier exactly in the AC⁰ model. The wall stands; the map is sharper. Cycles 2–5 should now push either (a) the non-natural AC⁰ LB directly (the genuine-open shape, now precisely stated), or (b) a structurally-different reduction that builds in a non-natural witness (the compression crux), or (c) — if both are blocked — revisit the Williams face with the same "which gate is thinnest" question.

## Sources
- sources/_tr20-183.txt (Ilango, FOCS 2020 / SIAM J. Comput. 2022 — §1.4 (P/poly)-recognizable, lines 40-46/565-591/620-629; Lemma 26 Lupanov parameterization from the first-loop S1.a read)
- sources/2026-08-21-s1a-primary-source.md (S1.a — established `[s1a-antiprox-obstruction]`, the tight-window gate)
- sources/2026-08-21-s2-primary-source.md (S2 — LB-existence blocked, general-circuit)
- sources/2026-08-23-s3-choprs-thm49.md (S3 — LB-existence blocked, formula; the "all three polynomial" claim this source corrects)
- sources/2026-08-23-five-cycle-synthesis.md (the synthesis this source refines)
- Håstad 1986 (switching lemma / Sipser worst-case AC⁰ LB); Rossman-Servedio-Tan FOCS 2015 / JACM 2017 (average-case depth hierarchy, Sipser$_d$) — web-confirmed