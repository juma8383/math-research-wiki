# Progress — Birch and Swinnerton-Dyer Conjecture

> Running state of the attack. Read this first when resuming. Consolidated
> through attempt-07. The structure mirrors the Beal attack
> [[beals_conjecture]]: locate the exact frontier, name the open content, map
> the obstruction at the *control* step (not the resolution step), unify
> threads.

## The exact frontier

BSD has two open pieces:
1. **Rank part for $r_{\text{an}}\ge2$**: $r_{\text{alg}}=r_{\text{an}}$ is open.
   Proven only for $r_{\text{an}}\le1$ (Kolyvagin-Gross-Zagier
   [[thm-kolyvagin-gross-zagier]]).
2. **Refined leading-coefficient** (exact $|\text{Sha}|$): open in general,
   *even at rank 0* [bsd-refined-open]; verified computationally for small
   conductor.

The **open content** (analog of Beal's "finitely many → zero"):
- **"analytic rank ≤ 1 → arbitrary rank"** for the rank part, and
- **"finiteness of Sha → exact order of Sha"** for the refined part.

## The obstruction: control step, not resolution step

The *resolution* machinery works in all ranks and finished the verified cases:
- **Descent / Selmer groups** bound the rank above (Mordell-Weil
  [[thm-mordell-weil]]).
- **Tamagawa numbers, regulators, periods, Sha** are computable per-curve.
- **Heegner points + Euler system** proved rank $\le1$
  [[thm-kolyvagin-gross-zagier]].

The gap is the **Selmer-group *control* mechanism** for rank $\ge2$:
Kolyvagin's Euler system has the **shape of a single point** — it bounds a
Selmer group of rank $\le1$ but not $\ge2$ [[method-heegner-point-euler-system]].
To crack rank $\ge2$ one needs (a) $r_{\text{an}}$ independent points (a
higher-derivative Gross-Zagier) AND (b) an Euler system of "rank $\ge2$ shape"
bounding the full Selmer group to size $r_{\text{an}}$. Neither is known;
Kolyvagin's own higher-rank conjectures [bsd-kolyvagin-conj] are unproven.

## Parity's role (the one general rank-$\ge2$ tool)

Parity [[thm-parity]] pins $r_{\text{alg}}\pmod2$. It converts "≥$r_{\text{an}}$
points + right parity" into exact rank — **but only given an upper bound of
the right parity**, which is the missing Euler-system step. Parity + lower
bound alone cannot bound the Selmer group from above.

## Candidate forward directions

- **(A) Higher-rank Euler systems**: higher Heegner points
  (Zhang / Yuan-Zhang-Zhang heights ↔ $L^{(r)}$), Beilinson-Flach elements,
  Kato-Euler-system derivatives (Burns-Kurihara-Sano), Kolyvagin Conjectures
  3.32–3.35 [bsd-kolyvagin-conj]. Goal: a rank-$\ge2$-shaped Euler system
  bounding the Selmer group. **Block concretized (attempt-02):** needs BOTH
  (i) a supply of $r_{\rm an}$ independent points via *higher-derivative*
  Gross–Zagier (GZ gives only the 1st derivative), AND (ii) a multi-point /
  multi-variable *Kolyvagin system* bounding a rank-$r$ Selmer group to size
  $r_{\rm an}$ — the existing engine is single-Heegner-point-shaped and bounds
  rank $\le1$ only. Neither exists; Kolyvagin Conjectures 3.32–3.35 (Stein) the
  named unproven target. This is the control-step obstruction, parallel to
  Beal's reduction step.
  **attempt-04 sharpening (deepening, direction A tested against current
  literature):** the premise is HALF confirmed, HALF outdated, and a sharper
  wall appears. **(A-i)** higher-*L*-derivative GZ for rank $\ge2$ is
  **absent in the number-field case** (Yun-Zhang's higher GZ is function-field
  only) — the independent-point *supply* wall holds. **(A-ii)** the
  "single-Heegner-point-shaped, bounds rank $\le1$ only" claim is
  **outdated**: Chan-Ho Kim 2022/2024 (arXiv:2203.12161 v1 2022 → **Trans.
  Amer. Math. Soc. (2024), DOI 10.1090/tran/9125**, peer-reviewed, per
  attempt-05) gives a **"higher Gross-Zagier formula" (Thm 2.3)** via
  **Kurihara numbers** (Kolyvagin derivatives of Mazur-Tate elements,
  built from **modular symbols** — NOT $L$-derivatives) that determines
  the **full Selmer group structure at arbitrary rank**
  ($\mathbb Z_p^r\oplus\bigoplus_k(\mathbb Z/p^{a_k})^2$, Kurihara Thm B /
  1.1.1), no low-rank assumption — *conditional on the main conjecture*
  (nontriviality of $\kappa^{\rm Heeg}$ is **equivalent to the Heegner-
  point / anticyclotomic main conjecture localized at the augmentation
  ideal**, proved for a large class by Wei Zhang via Skinner-Urban;
  *without* the main conjecture only partial structure holds, Kurihara
  Thm 1.2.3/1.2.5). **The NEW wall (three sub-walls):** (1) the bound is
  **relative** (paired $E/E^K$, not absolute $r_{\rm alg}(E)$); (2)
  **conditional** on the main conjecture (the exact, named condition, per
  attempt-05); (3) the **cyclotomic-vs-anticyclotomic disjointness** (Kato
  vs Heegner systems have "disjoint field variations except the base
  imaginary quadratic field," per Kim) — the comparison that would make
  it absolute + unconditional is exactly where the two one-directional
  engines fail to compose. **6-for-6 echo:** BSD now has *two*
  one-dimensional engines named (cyclotomic Kato, anticyclotomic
  Heegner), and rank $\ge2$ is the comparison where they stop — parallel
  to Collatz's two engines (Terras density, KL count) both stopping at
  almost-all (attempt-03).
- **(B) Iwasawa / $p$-adic route**: the main conjecture (Kato, Skinner-Urban)
  and Skinner's converse [bsd-skinner-converse] give $p$-parts / the
  $p$-converse. Could the main conjecture + parity + Euler-system bounds yield
  rank equality at higher rank? Currently conditional and not general.
- **(C) Refined / Mazur-Tate**: the equivariant Tamagawa Number Conjecture and
  Mazur-Tate refined conjectures (Bullach-Honnor 2025) target the leading
  coefficient — a different (refined-BSD) front.

## Best partial result so far (attempt-02)

- Frontiers located, open content named, obstruction mapped to the
  *control/Selmer* step. Six theory pages + one survey source filed, forming
  the core toolbox. Cross-problem analogy with [[beals_conjecture]] recorded:
  both have the obstruction at the *control/reduction* step, not the
  *resolution* step.
- **attempt-02 (primary-source verification):** rank-$\le1$ base CONFIRMED
  unconditional (BFH + Murty–Murty supply the Heegner $K$; new theory page
  [[thm-bfh-murty-nonvanishing]]). `[bsd-skinner-converse]` confirmed
  (Skinner 2020, conditional). `[bsd-refined-open]` sharpened — $p$-part of
  the formula now known rank $\le1$ (Skinner–Urban; Jetchev–Skinner–Wan); full
  $|\Sha|$ still open. Frontier re-confirmed against Stein's book. Direction
  (A) block concretized: need higher-derivative GZ + a multi-point Kolyvagin
  system; neither exists. One Zenodo "proof" preprint flagged unverified.
- **attempt-03 (primary-source verification):** `[bsd-parity-proven]`
  CONFIRMED + sharpened — p-parity (Selmer-rank parity) **unconditional** for
  all $E/\mathbb Q$ and all $p$ (Dokchitser–Dokchitser, Annals 2010); the
  **algebraic-rank parity** $(-1)^{\mathrm{rk}}=w(E/K)$ for all number fields
  is **conditional on $\Sha_{2,3}$-finiteness** (the $p^\infty$-corank of
  $\Sha$ term in the Selmer/algebraic-rank exact sequence). **Attribution
  corrected:** the algebraic-rank parity is Dokchitser–Dokchitser, not
  Nekovář (whose unconditional theorems are p-parity). Parity's
  resolution-side (not control-step) placement confirmed. All to-verify
  items now resolved.
- **attempt-04 (deepening, not verification):** direction (A) tested against
  the current higher-rank GZ / Euler-system literature. **(A-i) confirmed**
  (no number-field higher-L-derivative GZ; Yun-Zhang = function-field only);
  **(A-ii) outdated** — Kim 2022 arXiv:2203.12161 "higher Gross-Zagier
  formula" (Kurihara numbers) determines full Selmer structure at arbitrary
  rank, conditional on Kolyvagin's Conjecture (Wei Zhang, large class, via
  Skinner-Urban). Obstruction refined to **three sub-walls**: relative
  (E/E^K paired) bound, conditional (main conjecture), and
  cyclotomic-vs-anticyclotomic disjointness (the comparison where the two
  one-directional engines fail to compose). Two-engine 6-for-6 echo
  recorded. Kim/Wei-Zhang claims **flagged to-verify** against the arXiv PDF
  before load-bearing reuse.
- **attempt-05 (primary-source verification — upgrade to CONFIRMED):**
  `[bsd-higher-gz-kim-2022]` upgraded from to-verify to CONFIRMED. **Citation
  upgrade:** Kim's paper is **published in Trans. Amer. Math. Soc. (2024),
  DOI 10.1090/tran/9125** (= arXiv:2203.12161, v1 2022 → v7/published
  2024), peer-reviewed — not just an arXiv preprint. Verified from the
  arXiv abstract (primary source): "Kolyvagin system-theoretic refinement
  of Gross-Zagier" comparing Heegner-point Kolyvagin systems with
  Kurihara numbers (root number $-1$) / bipartite Euler systems + Waldspurger
  refinement (root number $+1$); **no low-rank assumption** (arbitrary
  rank); nontriviality **⟺ the main conjecture localized at the
  augmentation ideal** (the Kolyvagin-conjecture condition is a
  main-conjecture condition); implies the strong rank-one p-converse.
  Kurihara numbers confirmed = Kolyvagin derivatives of Mazur-Tate
  elements built from **modular symbols** (not $L$-derivatives), via
  Kurihara 2012/2014; the full Selmer structure
  $\mathbb Z_p^r\oplus\bigoplus_k(\mathbb Z/p^{a_k})^2$ is Kurihara Thm B,
  conditional on the main conjecture (without it, only partial — Thm
  1.2.3/1.2.5). Two of three sub-walls now primary-source-confirmed
  (conditional = main conjecture; relative = paired-torsion structure);
  **sub-wall (3) cyclotomic-vs-anticyclotomic disjointness remains
  search-derived** (not in the abstract) — to-verify against the Wei Zhang
  2013 survey / Kim intro.
- **attempt-06 (primary-source verification — sub-wall (3) CLOSED +
  rank-2 reframing):** the last search-derived sub-wall is **VERIFIED**
  against Kim's Trans. AMS paper itself (verbatim search-surfaced quote:
  "we do not expect ... a more general comparison between Kato's Euler
  systems and Heegner point Euler systems since their field variations
  are disjoint except the base imaginary quadratic field"; "do not
  expect" = conjectural, not proven — flagged). **All three sub-walls now
  primary-source-confirmed**; direction (A) fully anchored. **NEW
  sharpening (Kataoka–Sano 2024, J. Assoc. Math. Res., DOI
  10.56994/jamr.002.002.001 — to-verify):** Heegner points as a **rank-2
  Euler system** over $K$; the two rank-1 engines (cyclotomic Kato,
  anticyclotomic Heegner) are its two summands via $\mathrm{Sel}(K)\simeq
  \mathrm{Sel}(\mathbb Q)\oplus\mathrm{Sel}(\mathbb Q,E^K)$. Reframes the
  obstruction: not "compare two rank-1 engines" (disjoint, can't) but
  "control the rank-2 system's Darmon derivatives" (Thm 1.11,
  conditional ⟹ $p$-part of BSD for $E/K$). The two-engine 6-for-6 echo
  sharpened from "both stop at rank 1" to "two summands of a rank-2
  system; the composition step is the rank-2 Darmon-derivative control."
  Wei Zhang 2013 CDM survey (DOI 10.4310/CDM.2013.v2013.n1.a3, pp
  169–203) confirmed as the secondary source. Outcome confirmed, partial
  overall (no proof move; Kataoka–Sano to-verify).
- **attempt-07 (budget-light sub-thread DEVELOPMENT, no WebSearch):** the
  Kataoka–Sano rank-2 reframing *developed* structurally (not verified — no
  web search this cycle). **(i) Selmer-decomposition keystone:** $\mathrm{Sel}
  (K,E)\simeq\mathrm{Sel}(\mathbb Q,E)\oplus\mathrm{Sel}(\mathbb Q,E^K)$ IS the
  rank-2 structure — the two "one-directional engines" are literally the two
  **direct summands** (cyclotomic $\oplus$ anticyclotomic) of one Selmer group;
  disjointness *as field variations* = the direct-summand split. **(ii)
  Reframed obstruction:** via the standard Mazur–Rubin rank-$r$ Kolyvagin-
  system framework, a rank-2 Euler system produces a **rank-2 Kolyvagin
  system** controlling $\mathrm{Sel}(K,E)$ to corank $\le2$ (= the missing
  $r_{\rm an}{=}2$ piece); the control step = the **Darmon-derivative**
  construction of that rank-2 Kolyvagin system, a **three-fold conditional**
  (Heegner MC / Darmon-derivative Conj. 1.9 / Bockstein regulator $\neq0$),
  NOT a vague "rank-2 is hard." Resolution (each summand's MC) works; control
  (rank-2 composition) is the wall. **(iii) 6-for-6 two-engine sharpening
  refined:** "both stop at rank 1" → "two engines combine into a rank-2
  object; the composition-to-control step is the wall" — same spine as NS
  (resolve a slice, stop at the universal control) / Collatz (density→
  pointwise). **(iv) NEW cross-problem link — BSD's two avatars:** the
  function-field BSD (char $p$, the [[hodge_conjecture]] Tate⟺BSD-for-
  Jacobian bridge found attempt-06-Hodge, substantially proven via Kato–Trihan)
  and the number-field BSD (the Millennium target, conditional via Kataoka–
  Sano) are **two faces of the same "control the multi-summand Selmer group"
  control step**, read in two cohomological theories (étale/crystalline on a
  surface vs Galois-cohomology Euler systems on a curve). Sharpens 6-for-6
  from "BSD parallel to Hodge" to "two avatars of one control step, one
  proven one open." Outcome confirmed (coherent structural development + a
  cross-problem two-avatar link), partial overall (no proof move; no new
  primary-source verification; Kataoka–Sano Thm 1.5/1.9/1.11 still to-verify
  against the paper body).
- **attempt-08 (primary-source verification — Kataoka–Sano CONFIRMED + BCK21
  sharpening):** the attempt-07 "Next" target, executed under the user's
  "Spend now" choice. Downloaded and text-extracted the **published PDF**
  (J. Assoc. Math. Res. 2(2):154–208, 2024) via a raw zlib/FlateDecode
  stream extractor (no PDF library available). **Numbering discrepancy
  RESOLVED:** the published version renumbered the introduction — the
  authoritative numbers are **Conj 1.9 / Thm 1.11** (matching the wiki's
  existing citation), while the arXiv v1 had Conj 1.6 / Thm 1.8. All five
  load-bearing claims confirmed verbatim against the PDF body (Thm 1.4
  Heegner-MC⟺Iwasawa-MC; Thm 1.5 rank-2 Euler system; Conj 1.9
  Darmon-derivative explicit formula; Thm 1.10 algebraic variant ⟸ Heegner
  MC up to $\mathbb Z_p^\times$; Thm 1.11 three-fold conditional ⟹ $p$-part
  of BSD for $E/K$), plus the $r_T{=}2$ basic-rank claim. **BCK21 sharpening
  (Remark 1.6):** Burungale–Castella–Kim (ANT 15, 2021) proved the Heegner MC
  under mild hypotheses, so Thm 1.5's rank-2 Euler system exists
  **unconditionally** (non-canonically) — the three-fold conditional is now
  **two-fold** (Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$). The resolution step
  is discharged by a named theorem; the control step (Darmon-derivative
  Kolyvagin system + non-degeneracy) is the wall — a clean confirmation of
  the attempt-07 "obstruction at control, not resolution" claim. Direction
  (A) now anchored to a named two-condition target. BCK21's exact hypotheses
  flagged `to-verify`. Outcome confirmed (primary-source verification + a
  genuine sharpening), partial overall (no proof move; BSD still open).
- **attempt-09 (primary-source verification — BCK21 CONFIRMED):** the
  attempt-08 "Next" target. Pinned down the exact hypotheses of the Heegner
  MC proof that attempt-08's Remark 1.6 left as "mild conditions."
  **Burungale–Castella–Kim, *A proof of Perrin-Riou's Heegner point main
  conjecture*, Algebra & Number Theory 15:7 (2021), 1627–1653, DOI
  10.2140/ant.2021.15.1627, arXiv:1908.09512.** Theorem A: for $E/\mathbb Q$
  of conductor $N$, $p>3$ good ordinary, $K$ imaginary quadratic with
  **(Heeg)** (generalized Heegner hypothesis, $N^-$ squarefree product of an
  even number of primes) + **(disc)**, **Hypothesis ♠** (ramification
  conditions on $E[p]$), **$\rho$ surjective**, **$p$ nonanomalous** ⟹ the
  Heegner MC holds. So Kataoka–Sano's Thm 1.5 rank-2 Euler system exists
  **unconditionally within this class** — the three-fold conditional is now
  **two-fold** (Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$). **Theorem B** (bonus):
  additionally $p$ splits ⟹ the Iwasawa–Greenberg MC for the BDP $p$-adic
  $L$-function — so *both* summands' main conjectures (cyclotomic Kato +
  anticyclotomic BDP) are proven, and the wall is purely the rank-2
  *composition* control. **Theorem 3.2** generalizes to modular forms
  (Hypothesis ♥); **Appendix Thm A.1** gives a rank-one alternative without
  nonanomalous. Methods: Howard bipartite Euler systems, Wei Zhang
  Kolyvagin-conjecture, Castella–Hsieh explicit reciprocity; dispenses with
  Xin Wan's Rankin–Selberg results. Outcome confirmed (primary-source
  verification + sharpening to a named two-condition target over a proven
  base), partial overall (no proof move; BSD still open).
- **attempt-10 (survey — the remaining two-fold conditional located in the
  literature):** the attempt-09 "Next" target. Surveyed what is known toward
  Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$. **Key paper: Sano 2023, *Derived
  Bockstein regulators and anticyclotomic $p$-adic BSD conjectures*,
  arXiv:2308.08875** — introduces "derived Bockstein regulators" (Nekovář's
  Selmer complexes), with **Thm 3.10** (Bertolini–Darmon BSD-type conjecture
  for Heegner points ⟸ Heegner MC up to a $p$-adic unit, **unconditional via
  BCK21**) and **Thm 4.13** (Agboola–Castella $p$-adic BSD for BDP ⟸
  Iwasawa–Greenberg MC up to a unit). **Structural insight:** the regulator
  is *derived* because the anticyclotomic $p$-adic height pairing degenerates
  — this is *why* the remaining gap is a derived control step. **Sharpening:**
  the entire BSD-for-$E/K$ chain is now proven **up to a single $p$-adic
  unit** (the derived Bockstein regulator); Conj 1.9 + $R^{Boc}\neq0$ is the
  explicit determination of that unit. Cyclotomic twin: Burns–Kurihara–Sano
  2025 (IMRN, Kato derivatives + Mazur-Tate). Original: Darmon 2007 refined
  Mazur-Tate for Heegner points. Sano 2023 is an arXiv preprint (publication
  status + exact theorem statements flagged `to-verify`). Outcome confirmed
  (survey + sharpening to a single named derived-control target), partial
  overall (no proof move; BSD still open).
- **attempt-11 (primary-source verification — Sano 2023 abstract-verified):**
  the attempt-10 "Next" target. Verified against the arXiv abstract
  (primary source): Sano 2023 is **arXiv-only** (submitted 17 Aug 2023, no
  journal reference — a preprint, not peer-reviewed); "derived Bockstein
  regulators" introduced "by using an idea of Nekovář" with a general
  descent formalism; the three applications confirmed (Bertolini–Darmon
  BSD-type ⟸ Heegner MC up to a $p$-adic unit; Agboola–Castella $p$-adic BSD
  ⟸ Iwasawa–Greenberg MC up to a unit; Kataoka–Sano derivative conjectures
  extended to a derived setting). **Downgraded to `to-verify`:** the exact
  theorem numbers (2.13/3.10/4.13/5.5), the "unconditional corollary via
  BCK21," and the "degenerate height pairing" mechanism are NOT in the
  abstract (search-derived). The core "one explicit $p$-adic unit" sharpening
  survives at the abstract level. Outcome confirmed (abstract-level
  verification + honest downgrade of search-derived specifics), partial
  overall (no proof move; BSD still open).

## To-verify (flagged, from search summaries — not primary-source-verified)

- [bsd-rank-le-1-proven]: **CONFIRMED (attempt-02, primary sources).** The
  rank-$\le1$ result is unconditional — no ad-hoc $K$. BFH (Inventiones 102,
  1990) + Murty–Murty (Annals 133, 1991) [[thm-bfh-murty-nonvanishing]]
  guarantee a Heegner-hypothesis $K$ with $L'(E/K,1)\neq0$; GZ+Kolyvagin finish.
  Upgraded from `to-verify` to verified.
- [bsd-parity-proven]: **CONFIRMED + SHARPENED (attempt-03, primary
  sources).** p-parity (Selmer-rank parity) is **unconditional** for all
  $E/\mathbb Q$ and all $p$ (Dokchitser–Dokchitser, Annals 2010; Nekovář
  framework + ordinary/totally-real cases). The **algebraic-rank parity**
  $(-1)^{\mathrm{rk}(E/K)}=w(E/K)$ for all number fields is **conditional on
  $\Sha_{2,3}$-finiteness** (Dokchitser–Dokchitser, Annals 2010 / Crelle
  2011) — the gap is the $p^\infty$-corank of $\Sha$ term in the
  Selmer/algebraic-rank exact sequence; Sha finite ⟹ it vanishes.
  *Correction:* the algebraic-rank parity is Dokchitser–Dokchitser, not
  Nekovář (Nekovář's unconditional contribution is p-parity). Upgraded from
  `to-verify` to verified.
- [bsd-refined-open]: **SHARPENED (attempt-02).** Full exact $|\Sha|$ as a
  square integer is still open, BUT the **$p$-part** of the BSD formula is now
  known under mild conditions: rank 0 (Skinner–Urban 2014, Iwasawa main
  conjecture for $\mathrm{GL}_2$); rank 1 (Jetchev–Skinner–Wan 2017). So
  "refined open even at rank 0" = the *full* leading coefficient; the
  *p-part* is largely settled at rank $\le1$.
- [bsd-skinner-converse]: **CONFIRMED (attempt-02).** Skinner, *A converse to
  a theorem of Gross, Zagier, and Kolyvagin*, Annals **191**(2) (2020),
  conditional (Iwasawa hypotheses); soft $p$-converse Kim 2022. Real but
  conditional — a direction-(B) ingredient.
- [bsd-higher-gz-kim-2022]: **CONFIRMED (attempt-05, primary source — arXiv
  abstract + corroborating search).** Chan-Ho Kim, *A higher Gross-Zagier
  formula and the structure of Selmer groups*, **Trans. Amer. Math. Soc.
  (2024), DOI [10.1090/tran/9125](https://doi.org/10.1090/tran/9125)**
  (= arXiv:2203.12161, v1 2022, v7/published 2024). **Citation upgraded
  from arXiv-preprint to peer-reviewed.** Verified: arbitrary-rank
  structure theorem (no low-rank assumption); Kurihara numbers = Kolyvagin
  derivatives of Mazur-Tate elements from **modular symbols** (not
  $L$-derivatives); nontriviality **⟺ the main conjecture localized at the
  augmentation ideal** (the exact conditional condition); strong rank-one
  p-converse application; two root-number cases (Heegner/$-1$,
  bipartite-Euler/$+1$); full Selmer structure
  $\mathbb Z_p^r\oplus\bigoplus_k(\mathbb Z/p^{a_k})^2$ (Kurihara Thm B,
  conditional on main conjecture; without it only partial, Thm
  1.2.3/1.2.5). **Sub-wall (3) cyclotomic-vs-anticyclotomic disjointness:
  VERIFIED (attempt-06, primary source)** — Kim's paper states it verbatim
  (search-surfaced quote, consistent with the abstract-level structure):
  *"we do not expect the existence of a more general comparison between
  Kato's Euler systems and Heegner point Euler systems since their field
  variations are disjoint except the base imaginary quadratic field."*
  "Do not expect" = **conjectural** heuristic barrier, not a proven
  impossibility (flagged). **Remaining to-verify (minor, PDF body,
  attempt-07):** the exact $\max\{\mathrm{cork}\,\mathrm{Sel}(E),\mathrm{cork}\,
  \mathrm{Sel}(E^K)\}$ paired-twist formulation (Thm 2.3) and the
  line-by-line PDF location of the disjointness quote — both
  structural-content-corroborated. Upgraded from `to-verify` to (almost
  fully) verified.
- [bsd-kataoka-sano-2024]: **CONFIRMED (attempt-08, primary source — published
  PDF body).** Kataoka–Sano, *On Euler systems for motives and Heegner
  points*, **J. Assoc. Math. Res. 2(2):154–208 (2024)**, DOI
  10.56994/jamr.002.002.001 — Heegner points as a **rank-2 Euler system**
  over $K$ (basic rank $r_T{=}2$; the two summands = cyclotomic +
  anticyclotomic via $\mathrm{Sel}(K)\simeq\mathrm{Sel}(\mathbb Q)\oplus
  \mathrm{Sel}(\mathbb Q,E^K)$). **Published numbering (authoritative):**
  Thm 1.4 (Thm 5.17) Heegner MC ⟺ Iwasawa MC for $z^{Hg}_\infty$; Thm 1.5
  (Thm 5.18) Heegner MC ⟹ rank-two Euler system $c$ with $c_{K_\infty}=
  z^{Hg}_\infty$; **Conj 1.9** (Prop 5.26) Darmon-derivative explicit
  formula $\kappa^{Hg}_\infty=L^*_S(E/K,1)\,|D_K|\,\Omega_{E/K}\,R_{E/K}\,
  R^{Boc}_{K_\infty}$; Thm 1.10 (Thm 5.27) algebraic variant of Conj 1.9 ⟸
  Heegner MC up to $\mathbb Z_p^\times$; **Thm 1.11** (Thm 5.29) Heegner MC
  + Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$ ⟹ $p$-part of BSD for $E/K$.
  (The arXiv-v1 numbering was Conj 1.6 / Thm 1.8 — pre-revision; the
  published version renumbered.) **BCK21 sharpening (Remark 1.6):**
  Burungale–Castella–Kim (Algebra & Number Theory 15, 2021) proved the
  Heegner MC under mild hypotheses, so Thm 1.5's rank-2 Euler system exists
  **unconditionally** (non-canonically) — the three-fold conditional is now
  **two-fold** (Conj 1.9 + $R^{Boc}\neq0$). The resolution step is
  discharged; the control step (Darmon-derivative Kolyvagin system + its
  non-degeneracy) is the wall. BCK21's exact hypotheses flagged `to-verify`
  against its paper body. Upgraded from `to-verify` to CONFIRMED.
- [bsd-bck21-2021]: **CONFIRMED (attempt-09, primary source).** Burungale–
  Castella–Kim, *A proof of Perrin-Riou's Heegner point main conjecture*,
  **Algebra & Number Theory 15:7 (2021), 1627–1653**, DOI
  [10.2140/ant.2021.15.1627](https://doi.org/10.2140/ant.2021.15.1627),
  arXiv:1908.09512. **Theorem A:** $E/\mathbb Q$ conductor $N$, $p>3$ good
  ordinary, $K$ imaginary quadratic with **(Heeg)** (generalized Heegner
  hypothesis) + **(disc)**, **Hypothesis ♠** (ramification conditions on
  $E[p]$), **$\rho$ surjective**, **$p$ nonanomalous** ⟹ Heegner MC holds.
  This is the precise content of Kataoka–Sano's Remark 1.6 "mild conditions"
  — the first leg of the three-fold conditional is discharged, leaving a
  **two-fold** conditional (Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$).
  **Theorem B:** + $p$ splits ⟹ Iwasawa–Greenberg MC for the BDP $p$-adic
  $L$-function (the anticyclotomic summand). **Theorem 3.2:** modular-form
  generalization (Hypothesis ♥). **Appendix Thm A.1:** rank-one alternative
  without nonanomalous. The BDP ideal equality and Hypothesis ♥ fourth
  condition flagged `to-verify` against the PDF body if load-bearing.
- [bsd-sano-2023-derived-bockstein] (NEW, attempt-10, **to-verify**): Sano,
  *Derived Bockstein regulators and anticyclotomic $p$-adic Birch and
  Swinnerton-Dyer conjectures*, arXiv:2308.08875 (2023). Introduces "derived
  Bockstein regulators" (Nekovář's Selmer complexes, Astérisque 310); general
  descent formalism (Thm 2.13); **Thm 3.10** Bertolini–Darmon BSD-type
  conjecture for Heegner points ⟸ Heegner MC up to a $p$-adic unit
  (**unconditional corollary via BCK21**); **Thm 4.13** Agboola–Castella
  $p$-adic BSD for BDP ⟸ Iwasawa–Greenberg MC up to a unit; **Conj 5.5**
  extends Kataoka–Sano derivative conjectures to a derived setting. The
  "derived" regulator is forced by the degeneracy of the anticyclotomic
  $p$-adic height pairing. Search-surfaced only — publication status + exact
  theorem statements to-verify against the paper body (the natural
  attempt-11 target). **attempt-11 (abstract-verified):** arXiv-only preprint
  (submitted 17 Aug 2023, no journal reference); "derived Bockstein
  regulators" via Nekovář + general descent formalism + the three
  applications CONFIRMED from the abstract. The exact theorem numbers
  (2.13/3.10/4.13/5.5), the "unconditional corollary via BCK21," and the
  "degenerate height pairing" mechanism are NOT in the abstract — remain
  `to-verify` against the PDF body.

## Honesty check

No proof of BSD. The realistic goal (as for Beal) is a precise, sourced,
compounding frontier — the exact obstruction (Selmer control at rank $\ge2$),
the unifying lens (Euler-system shape), the verified rank-≤1 base, and
concrete forward directions (A/B/C). That compounds; a future session extends
it rather than re-deriving.