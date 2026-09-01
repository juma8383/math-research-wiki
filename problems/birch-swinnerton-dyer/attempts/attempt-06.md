---
type: attempt
problem: birch_swinnerton_dyer
attempt: 6
date: 2026-08-24
approach: Verify the last search-derived sub-wall (3) — cyclotomic-vs-anticyclotomic disjointness (Kato vs Heegner field-variation) — against the primary source (Kim's Trans. AMS paper / Wei Zhang 2013 CDM survey); close the to-verify loop on attempt-04/05's direction-(A) deepening
outcome: confirmed
tags: [verification, primary-source, kato-euler-system, heegner-point, anticyclotomic, cyclotomic, disjointness, rank-2-euler-system, cross-problem]
---

# Attempt 06 — Sub-wall (3) cyclotomic-vs-anticyclotomic disjointness VERIFIED (Kim, primary source); Kataoka–Sano rank-2 reframing

Cycle-23 Continue on BSD (cross-problem loop, second pass; **yellow zone**
session 78.3% / weekly 66.2%, max 2 subagents — **0 used**, direct WebSearch to
conserve budget; session resets in ~1h). Attempt-05's `Next` sanctioned this
run verbatim: the remaining sub-wall (3) — **cyclotomic-vs-anticyclotomic
disjointness** (Kato vs Heegner field-variation) — "is the natural next
to-verify (against the Wei Zhang 2013 *Current Developments in
Mathematics* survey or Kim's Trans. AMS intro), to close the last
search-derived piece." This cycle closes it: the claim is **in Kim's own
paper** (the primary source attempt-05 already verified), not only in the
Wei Zhang survey.

## Headline: sub-wall (3) VERIFIED — the disjointness is Kim's own statement

The targeted search surfaced the **verbatim quote directly in Kim's Trans.
AMS paper** (arXiv:2203.12161, = Trans. Amer. Math. Soc. 2024,
DOI 10.1090/tran/9125, the paper attempt-05 confirmed):

> *"we do not expect the existence of a more general comparison between
> Kato's Euler systems and Heegner point Euler systems since their field
> variations are disjoint except the base imaginary quadratic field."*

This is **exactly** sub-wall (3) as framed in attempt-04/05: the two
one-directional Euler systems — Kato's (varying over **cyclotomic** /
abelian extensions of $\mathbb Q$) and Heegner's (varying over
**anticyclotomic** / ring-class extensions of the imaginary quadratic $K$)
— have field variations that are **disjoint except at the base field $K$**,
so no direct Euler-system comparison is expected. The comparison that *does*
exist (Kim's higher Gross–Zagier, attempt-04/05) goes **not** through the
Euler systems directly but through **Kurihara numbers** (Kolyvagin
derivatives of Mazur–Tate / modular-symbol elements = Kato's *Kolyvagin
system*), using the decomposition
$\mathrm{Sel}(K,E[p^\infty])\simeq\mathrm{Sel}(\mathbb Q,E[p^\infty])\oplus
\mathrm{Sel}(\mathbb Q,E^K[p^\infty])$ to extract the
$\max\{\mathrm{cork}\,\mathrm{Sel}(E),\mathrm{cork}\,\mathrm{Sel}(E^K)\}$
structure (Thm 2.3). So the disjointness is **precisely why the bridge is
Kurihara numbers, not a direct Euler-system map**.

### Honesty caveat on the verification standard

The quote is **search-surfaced from the primary source** (the WebSearch
summary quoted it from arXiv:2203.12161), consistent with the paper's
structural content that attempt-05 verified at the abstract level — but I
have **not** read the PDF body line-by-line this cycle to pin the exact
section/sentence. Same standard as attempt-05's abstract-level
verification. Flagged `to-verify (minor, PDF body location)` for a future
line-by-line read; the *claim* is corroborated by the primary source.
Also: Kim's phrasing is **"we do not expect"** — a **conjectural**
expectation, not a proven impossibility. So the disjointness is a
**heuristic barrier**, not a theorem that no comparison can ever exist;
a future method could in principle find one. Recorded honestly.

## Wei Zhang 2013 CDM survey — confirmed (the named secondary source)

**Wei Zhang**, *The Birch–Swinnerton-Dyer conjecture and Heegner points:
A survey*, **Current Developments in Mathematics 2013**, 169–203, DOI
[10.4310/CDM.2013.v2013.n1.a3](https://dx.doi.org/10.4310/CDM.2013.v2013.n1.a3)
(published 2014-10-22, Intl Press). Wei Zhang's two CDM 2013 talks
(Harvard, Nov 2013) were titled *"Heegner Points and the Birch–Swinnerton-Dyer
Conjecture."* The survey is the secondary source attempt-05 named for the
disjointness framing; Kim's paper (primary) carries the statement directly,
so the wiki's load-bearing use is now primary-source-anchored. (The Intl
Press page returned HTTP 403 to WebFetch this cycle, so the survey body was
not read line-by-line; its existence/citation is confirmed via the
conference + DOI pages.)

## New sharpening: the "two engines" are the two summands of a RANK-2 Euler system (Kataoka–Sano 2024)

The search surfaced a **new result that reframes the disjointness** —
potentially the most important structural finding of this cycle:

**Kataoka–Sano**, *On Euler systems for motives and Heegner points*, **J.
Assoc. Math. Res. (2024)**, DOI
[10.56994/jamr.002.002.001](https://doi.org/10.56994/jamr.002.002.001).
Key points (search-surfaced; **flagged to-verify** against the paper body
before load-bearing use):

- The system of Heegner points is naturally a **rank-2 Euler system**: for
  $T=T_p(E)$ over the imaginary quadratic $K$, the basic rank is
  $r_T=\mathrm{rank}_{\mathbb Z_p}\,Y_K(T^*(1))=2$ (because $T^*(1)$ over $K$
  has rank 2 — the two "directions" being the cyclotomic and anticyclotomic
  summands).
- **Thm 1.4:** the Heegner point main conjecture (Perrin-Riou) ⟺ their
  Iwasawa main conjecture formulation for a "Heegner element"
  $z^{Hg}_\infty$ defined via the second exterior power
  $\bigwedge^2_\Lambda H^1$.
- **Thm 1.5:** assuming the Heegner point MC, constructs a **rank-2 Euler
  system** whose $K_\infty$-component is $z^{Hg}_\infty$.
- **Thm 1.11:** assuming the Heegner point MC + Conjecture 1.9 (Darmon-type
  derivatives) + non-vanishing of the anticyclotomic Bockstein regulator ⟹
  the **$p$-part of BSD for $E/K$ holds**.

**Why this sharpens the 6-for-6 two-engine echo (and is NOT a contradiction
of the disjointness):** the disjointness says the two *rank-1* engines
(Kato cyclotomic, Heegner anticyclotomic) cannot be compared *as Euler
systems* beyond $K$. Kataoka–Sano's reframing says: don't compare them as
two rank-1 systems — view the **Heegner system itself as rank-2 over $K$**,
whose two summands (via $\mathrm{Sel}(K)\simeq\mathrm{Sel}(\mathbb Q)\oplus
\mathrm{Sel}(\mathbb Q,E^K)$) **are** the cyclotomic and anticyclotomic
pieces. So the "disjointness" is not a dead-end but a **structural
feature**: the two one-directional engines are the two summands of a single
rank-2 object, and "composing" them = controlling $\mathrm{Sel}(K)$ =
controlling both $\mathrm{Sel}(\mathbb Q)$ and $\mathrm{Sel}(\mathbb Q,E^K)$
simultaneously — which is exactly what Kim's Thm 2.3
($\max\{\mathrm{cork}\}$) achieves *conditionally* via Kurihara numbers.
Kataoka–Sano then ask for the **Darmon-type derivatives** of this rank-2
system (Thm 1.9/1.11) to reach the $p$-part of BSD — a concrete, named
higher-rank Euler-system target, directly on direction (A).

This is a **genuine compounding move**: BSD's two-engine 6-for-6 echo
(attempt-04/05) is sharpened from "two rank-1 engines both stop at rank 1,
disjoint except at $K$" to "**the two engines are the two summands of a
rank-2 Euler system over $K$; the obstruction is controlling the rank-2
system's Darmon derivatives (not comparing two rank-1 systems)**." Parallel
to the cross-problem pattern: the control step is at the **multi-directional
/ higher-rank composition**, not the resolution (each single engine works
for its slice).

## Supporting primary sources (corroborating the two-engine structure)

- **Howard**, *The Heegner point Kolyvagin system*, **Compositio Math. 140**
  (2004) — the Heegner-point Kolyvagin system (Mazur–Rubin derivative
  operators on the Heegner Euler system); proves **one divisibility** of
  Perrin-Riou's anticyclotomic main conjecture; Thm A (Kolyvagin):
  $\kappa_1\neq0\Rightarrow\mathrm{corank}\,\mathrm{Sel}^{p^\infty}(E/K)=1$
  (the rank-$\le1$ bound, the resolution-side tool). Confirms the
  anticyclotomic engine's shape.
- **Bertolini–Darmon**, *Iwasawa's Main Conjecture for elliptic curves
  over anticyclotomic $\mathbb Z_p$-extensions*, **Annals of Math. 162**
  (2005) — anticyclotomic MC, **root-number $+1$** case (where Heegner
  hypothesis breaks down), via Shimura curves + Cerednik–Drinfeld. The
  $+1$ branch Kim's Thm 2.1(AMC) references.

## Two-engine table (verified)

| Aspect | Kato's Euler system | Heegner-point Euler system |
|---|---|---|
| Field variation | cyclotomic (abelian over $\mathbb Q$) | anticyclotomic (ring-class over $K$) |
| Bounded Selmer | $\mathrm{Sel}(\mathbb Q,E[p^\infty])$ | $\mathrm{Sel}(K,E[p^\infty])$ |
| Kolyvagin system | Kurihara numbers $\delta(E)$ | Heegner-point KS $\kappa^{\rm Heeg}$ |
| Main conjecture | cyclotomic IMC (Kato) | Heegner-point / anticyclotomic MC (Perrin-Riou, Howard, Bertolini–Darmon) |
| Rank (Kataoka–Sano) | 1 (over $\mathbb Q$) | **2** (over $K$: the two summands) |

## What this changes in the obstruction map

- **Sub-wall (3) cyclotomic-vs-anticyclotomic disjointness: VERIFIED**
  (Kim, primary source, search-surfaced quote; minor PDF-location
  to-verify). The "do not expect" phrasing recorded as a **conjectural**
  heuristic barrier, not a proven impossibility. This closes the last
  search-derived sub-wall of attempt-04/05 — all three sub-walls
  ((1) relative paired bound, (2) conditional = main conjecture, (3)
  disjointness) are now primary-source-confirmed. The direction-(A)
  obstruction is fully primary-source-anchored.
- **NEW: Kataoka–Sano 2024 rank-2 Euler-system reframing** — sharpens the
  two-engine 6-for-6 echo. The obstruction is reframed: not "compare two
  rank-1 engines" (disjoint, can't) but "control the rank-2 system's Darmon
  derivatives" (Thm 1.9/1.11, conditional). A concrete higher-rank
  Euler-system target on direction (A), where prior attempts said only
  "neither exists." Flagged `to-verify` against the Kataoka–Sano paper
  body before load-bearing reuse.
- **No proof move.** BSD remains open; rank $\ge2$ and exact $|\Sha|$
  untouched. This cycle verified + sharpened the *frontier map*, did not
  advance the proof. Honesty: outcome **confirmed** (sub-wall 3 closed
  against primary source; two-engine echo sharpened), **partial** overall.

## Honesty / scope

- **Sub-wall (3) VERIFIED** against Kim's Trans. AMS paper (primary
  source) via a search-surfaced verbatim quote; consistent with
  attempt-05's abstract-level verification. Minor to-verify: line-by-line
  PDF location. "Do not expect" = conjectural, not proven — flagged.
- **Kataoka–Sano 2024** findings are **search-surfaced only**; flagged
  `to-verify` against the paper body (J. Assoc. Math. Res., DOI
  10.56994/jamr.002.002.001) before any load-bearing reuse. The rank-2
  reframing is a *plausible sharpening*, not yet primary-source-verified
  line-by-line.
- **Wei Zhang 2013 CDM survey** existence/citation confirmed; body not
  read (Intl Press 403 to WebFetch). Cited as the secondary source; Kim's
  paper is the primary anchor.
- Howard 2004 / Bertolini–Darmon 2005 cited from search summaries; not
  re-verified line-by-line this cycle (budget). Both are well-established;
  flagged for a future verification pass if load-bearing.
- **No proof of BSD.** The rank-$\ge2$ Selmer-control obstruction and
  the exact-$|\Sha|$ refined part remain fully open. The realistic goal
  (as for Beal) is a precise, sourced, compounding frontier — advanced
  this cycle by closing sub-wall (3) and adding the rank-2 reframing.
- Outcome: **confirmed** (sub-wall 3 primary-source-verified; two-engine
  echo sharpened to rank-2 summands; Kataoka–Sano named as a concrete
  direction-(A) target), **partial** overall (no proof move; Kataoka–Sano
  to-verify).

## Next (attempt-07)

Natural next moves: (a) **primary-source-verify Kataoka–Sano 2024**
against the paper body — the rank-2 Euler-system reframing + the Thm 1.11
$p$-part-of-BSD conditional result is the most consequential unverified
new item, directly on direction (A); OR (b) pivot to direction (C) /
refined-BSD (Bullach–Honnor 2025, equivariant Tamagawa / Mazur–Tate) as
the second front (attempt-05's alternative Next); OR (c) line-by-line PDF
read of Kim's paper to pin the disjointness quote's exact location
(closes the minor to-verify). The rotation continues: next cross-problem
cycle → navier-stokes (attempt-06) per the rotation order.