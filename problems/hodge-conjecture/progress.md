# Hodge Conjecture — progress (read-first file)

> Start here. This is the navigational entry point; for structural depth see
> [notes.md](notes.md) and [attempts/attempt-02.md](attempts/attempt-02.md).
> Verified 2026-08-24 from web searches BEFORE committing (same discipline as
> BSD/NS/YM; Beal's attempt-17 caught a silent arithmetic error this way).
> Consolidated through attempt-06.
> Source: [hodge-survey](../../sources/hodge-survey.md) — web-search-compiled,
> NOT primary; flagged `[summary]`/to-verify.

## Exact frontier

The Hodge conjecture asks that the cycle class map
$\mathrm{cl}:\mathrm{CH}^p(X)\otimes\mathbb Q\to\mathrm{Hdg}^p(X)$ be
**surjective** for all $p$ on every smooth projective $X/\mathbb C$
[[def-hodge-class-cycle-map]].

| Codim $p$ | Degree $2p$ | Status |
|---|---|---|
| $0$ | $0$ | trivial ($[\mathrm{pt}]$) |
| $1$ | $2$ | **PROVEN** — Lefschetz $(1,1)$ [[thm-lefschetz-1-1]] |
| $n-1$ | $2n-2$ | proven (hard Lefschetz ← $p=1$) [[thm-hard-lefschetz-reduction]] |
| $n$ | $2n$ | trivial ($[X]$) |
| $2\le p\le n-2$ ($n\ge4$) | middle | **OPEN** — first case $p=2,n=4$ |

By hard Lefschetz only the middle codimensions are new. The **smallest open
case is codimension 2 on a 4-fold** (Deligne: "known when $\dim<4$; open in
dimension $\ge4$") [hodge-codim-2-open].

## Verified base

- Lefschetz $(1,1)$ (1924): $p=1$ integral, via exponential sequence; divisors
  [hodge-lefschetz-1-1].
- Hard Lefschetz: reduces $2p\leftrightarrow 2n-2p$; known degrees
  $0,2,2n-2,2n$ only [hodge-hard-lefschetz-reduction] [hodge-known-degrees-0-2-2n].
- Integral HC FAILS: Atiyah–Hirzebruch, Kollár — only $\mathbb Q$ conjectured
  [[thm-integral-hodge-fails]] [hodge-integral-fails].
  **attempt-04 (primary-source, two sources of failure):** (1) **torsion** —
  Atiyah–Hirzebruch 1961 (Topology 1, 25–45): torsion Hodge classes trivially
  $(k,k)$ but non-algebraic for $k\ge2$ (true for $k=1$ by Lefschetz $(1,1)$),
  via the AH spectral sequence $E_2^{s,t}=H^s(X,\mathbb Z)\Rightarrow
  K_{\text{top}}^{s+t}(X)$ (nonzero differential on Godeaux–Serre varieties).
  Totaro 1997 (JAMS 10(2):467–493, DOI 10.1090/S0894-0347-97-00232-4,
  arXiv:alg-geom/9609016): cycle map factors through
  $MU^*(X)\otimes_{MU^*}\mathbb Z$ (complex cobordism); topological Griffiths-
  group-nonzero proof (Thm 7.1/7.2). Soulé–Voisin 2005 (Adv. Math. 198:107–127,
  DOI 10.1016/j.aim.2004.10.022, arXiv:math/0403254, Thm 1): the obstruction
  detects only **$p\le\dim_{\mathbb C}X$**-torsion. (2) **non-torsion** —
  Kollár 1990 (LNM 1515, 134–135): general $X\subset\mathbb P^4$ degree $D$,
  $p^3\mid D$, $p\nmid6$ $\Rightarrow$ free generator $\alpha\in H^4(X,\mathbb
  Z)$ non-algebraic yet $D\alpha$ algebraic — **not topological** (depends on
  complex structure; algebraic on a dense parameter subset). Soulé–Voisin Thm 3:
  $p\ge5$ torsion in $H^6$ of 5-folds escaping **all** topological obstructions.
  **The $\mathbb Q$-retreat removes both:** torsion $\mapsto0$ in
  $H^*(X,\mathbb Q)$; Kollár's $\alpha$ is algebraic over $\mathbb Q$ via
  $D\alpha$. **Control-step echo (6-for-6):** the integral counterexamples
  obstruct the *resolution* (exhibit the cycle) over $\mathbb Z$; the $\mathbb
  Q$-refinement removes both, leaving the codim-$\ge2$ analytic$\to$algebraic
  *control* as the sole open piece — triangulated from the negative side here
  and the positive (Charles–Markman $K3^{[n]}$, attempt-03).
  **attempt-05 (ℓ-adic Tate analogue verified + attempt-04 framing
  CORRECTED):** the char-p parallel of HC is the **Tate conjecture**
  ($\mathrm{NS}(X)\otimes\mathbb Q_\ell\to
  H^2(X_{\bar k},\mathbb Q_\ell(1))^G$ surjective, and higher-codim
  analogues). **Attempt-04's "open even for $H^2$" is OUTDATED for the
  flagship case:** the K3-surface divisor case (the famous "Tate open
  where HC's $H^2$ is solved" example) is now a **theorem in all
  characteristics** — Nygaard–Ogus 1985 (finite height, reduces to
  Lefschetz $(1,1)$ via quasi-canonical lifting), Charles 2013
  (Invent. Math. 194, supersingular $p\ge5$), Maulik 2014 (Duke 163),
  Madapusi Pera 2015 (Invent. Math. 201, odd char), Kim–Madapusi Pera
  2016 (char 2), Charles 2016 (Annals 184, 2nd proof), with the
  Lieblich–Maulik–Snowden 2014 (Ann. Sci. ENS 47) finiteness⟺Tate
  criterion. The **general** Tate-for-divisors is still open but
  **reduced to surfaces** (de Jong–Morrow; proven for abelian/Tate
  1966, K3, rationally connected). **Sharper symmetric echo:** both
  HC (char 0) and Tate (char p) are solved at divisors (standard
  classes) and **open at codim $\ge2$** — the control-step spine is
  confirmed on **both** sides, not asymmetric. **Cross-problem bridge
  (VERIFIED + REFINED attempt-06):** Tate-for-divisors on a **fibered**
  surface $X/\mathbb F_q$ $\iff$ **function-field BSD for the Jacobian
  $J=\mathrm{Jac}(C)/\mathbb F_q(t)$ of the generic fiber** ($\iff$
  Artin-Tate $\iff$ Brauer / Tate–Shafarevich finiteness) — a **logical
  equivalence** to the **char-$p$ (function-field) avatar** of
  [[birch_swinnerton_dyer]], NOT the number-field Millennium BSD; sharpens
  6-for-6 from "linked" to "logically equivalent in one avatar."
  Primary sources: Tate-Milne 1975 + Artin-Grothendieck + Kato-Trihan 2003,
  re-proven directly by Lichtenbaum-Ramachandran-Suzuki 2022 (Épijournal
  G.A., DOI 10.46298/epiga.2022.7482). **Control echo inside Tate:** Milne —
  Tate-for-divisors $\Rightarrow$ 1-semisimplicity $\iff$ full
  Frobenius-semisimplicity (control vs resolution). **Balkan–Schreieder
  2026** (Selecta Math. 32, Art. 37) recasts Tate/Beilinson/
  semisimplicity as a single birational-vanishing criterion (an
  equivalence of conjectures, not a proof). Correction is append-only
  (attempt-04 left intact); Nygaard–Ogus-reduces-to-Lefschetz,
  Milne-semisimplicity, Tate⟺BSD, and Balkan–Schreieder flagged
  to-verify against paper bodies.
- Algebraicity essential: Zucker tori (Kähler ≠ projective)
  [hodge-algebraicity-essential].
- Absolute Hodge (Deligne): all Hodge classes on abelian varieties absolute
  Hodge — strongest evidence [[thm-absolute-hodge-motivated]] [hodge-absolute-hodge].
- Cattani–Deligne–Kaplan: Hodge locus algebraic
  [[thm-cattani-deligne-kaplan]] [hodge-cattani-deligne-kaplan].
  **attempt-02 (primary-source):** JAMS 8(2) 1995, Theorem 1.1 + Corollaries
  1.2–1.4; **UNCONDITIONAL** (answers André Weil's question; previously known
  only HC-conditionally) — "Hodge classes behave as if algebraic" is an
  unconditional evidence layer. Proof: Schmid nilpotent orbit + $SL(2)^r$-orbit
  theorem (Cattani–Kaplan–Schmid 1986) + GAGA. Control-not-resolution shape
  (controls the locus, doesn't produce the cycles).
- Standard conjectures B/C (Grothendieck): inverse Lefschetz + Künneth
  algebraic; known for surfaces, abelian varieties, hyper-Kähler $K3^{[n]}$
  (Charles–Markman 2013); motive reduction of HC
  [[thm-standard-conjectures-motives]] [hodge-standard-conjectures].
  **attempt-03 (primary-source):** Charles–Markman, *Compositio Math.* 149(3)
  (2013), 481–494, DOI 10.1112/S0010437X12000607 — Theorem 1.1 proves the
  **Lefschetz** standard conjecture (Conj. **B**) for all smooth projective
  $K3^{[n]}$-type; Cor. 1.2: in **char 0** the Lefschetz standard conjecture
  is the **strongest**, so it implies **all** standard conjectures (incl.
  Conj. **C**, Künneth components). Mechanism = **Verbitsky hyperholomorphic
  sheaves** + **twistor-line deformation** of algebraic correspondences across
  the $K3^{[n]}$ class + $O^+_{\Lambda(S)}(v)$ **Mukai-lattice monodromy**
  equivariance — a *control* technique (controls the cycles' deformation),
  the control-not-resolution shape; the precedent is $K3^{[n]}$-specific
  (general varieties lack Verbitsky/twistor structure) — direction (A)'s open
  core. Companion: Charles, *Comment. Math. Helv.* 88(2) (2013), 449–468.
- Abelian sub-cases: products of elliptic curves, Fermat type (Shioda), simple
  prime-dim (Tankeev/Ribet), fourfolds I/II (Moonen–Zarhin), some Weil type
  (Schoen) [hodge-abelian-cases].
- Generalized HC (Grothendieck coniveau) [[conj-generalized-hodge]]
  [hodge-generalized-conjecture]; Hodge's stronger original form false.

## Open content

"**Hodge class (analytic, defined by Hodge theory) → algebraic cycle**
in codimension $\ge2$." Equivalently: surjectivity of
$\mathrm{cl}\otimes\mathbb Q$ in the middle codimensions. This is the Hodge
analog of:
- Beal: "finitely many → zero" per signature;
- BSD: "analytic rank $\le1$ → arbitrary rank";
- NS: "small/local data → arbitrary large-data global regularity";
- YM: "lattice-discretized → continuum-rigorous 4D QFT with gap."

## Obstruction (control step, not resolution step)

The resolution layer works: Chow groups + the cycle class map are defined in
all codimensions; Hodge classes are computable; for $p=1$ the **exponential
sequence** makes $\mathrm{Hdg}^1=\ker(H^2(\mathbb Z)\to H^2(\mathcal O))\subset
\mathrm{Pic}$, and for projective $X$ the Néron–Severi group is algebraic
divisors (GAGA) — the **analytic→algebraic bridge works for divisors**
[[thm-lefschetz-1-1]]. The gap is the **control over this bridge in
codimension $\ge2$**: given a Hodge class of codim $\ge2$, no known mechanism
produces algebraic cycles realizing it. The Abel–Jacobi / normal-function
construction has no effective cycle-producing analogue in higher codimension
[[method-analytic-algebraic-bridge]].

**Unifying lens (analytic↔algebraic):** Hodge classes are *analytic* (Hodge
decomposition); algebraic cycles are *algebraic*. The bridge is GAGA +
Lefschetz $(1,1)$ for $p=1$; the conjecture is that this bridge extends to all
codimensions. The obstruction is exactly the "control over the
analytic→algebraic conversion" — the 5th instance of the cross-problem
"control/reduction step, not resolution step" lens
[[beals_conjecture]] [[birch_swinnerton_dyer]] [[navier_stokes]] [[yang_mills]].

## Parity of the known / the structural reason it stops

For divisors, $\mathrm{Hdg}^1\cong\mathrm{NS}(X)\otimes\mathbb Q$ is governed by
the Picard variety (a one-dimensional, effective, analytic→algebraic object via
the exponential sequence). For codim $\ge2$ there is no analogue: the
intermediate Jacobian / Griffiths Abel–Jacobi map $J^p(X)$ is *transcendental*
in general (not an abelian variety for $p\ge2$), and its image does not control
algebraicity the way the Picard variety does for divisors. This is the
"one-dimensional engine stops at codim 1" — parallel to Beal's
cubic-cubic-cubic coincidence, BSD's one-point Euler system, NS's 2D/3D
Serrin-index equality, YM's one-scale asymptotic freedom.

## Forward directions

- **(A) Motive / standard-conjecture reduction** [[thm-standard-conjectures-motives]]:
  prove the inverse Lefschetz (Conj. B) and Künneth components (Conj. C) are
  algebraic — known for surfaces, abelian varieties, hyper-Kähler $K3^{[n]}$;
  this makes the motive category Tannakian and reduces HC to a fully-faithful
  functor. The "reduction to specific Hodge classes" — the closest analog of
  Beal's reduction-to-finite-curves step.
  **attempt-02 sharpening (primary-source, Deligne hodge.pdf §4/§5):** B and C
  are **open special cases of HC itself** (Deligne §4 Example 1 = Künneth
  components of the diagonal = Conj. C; Example 2 = inverse Lefschetz = Conj.
  B), not merely a reduction pathway. §5: given B and C, motives over $\mathbb C$
  are semi-simple abelian and **HC ⇔ a fully-faithful motives→Hodge-structures
  functor**. So direction (A) is a two-stage control problem: (i) prove B,C
  (open special cases of HC; the "one-dimensional engine stops" here — the
  Picard-variety engine has no analogue for the diagonal's Künneth components
  or $\Lambda$); (ii) HC reduces to fully-faithfulness. The reduction target
  is itself unproven — exactly the Beal-reduction-to-specific-curves shape.
- **(B) Codim-2 directly** [[method-analytic-algebraic-bridge]]: attack the
  first open case (codim-2 Hodge classes on a 4-fold) via Griffiths
  intermediate Jacobians / normal functions / Abel–Jacobi — the direct
  analytic→algebraic bridge at the frontier.
- **(C) Structured sub-cases** [[thm-absolute-hodge-motivated]]: deepen the
  abelian-variety program (Weil type, type III in Albert classification);
  absolute Hodge / motivated cycles as the controlled evidence layer.

## To-verify (primary sources, before load-bearing use)

- Deligne Clay write-up (hodge.pdf): **CONFIRMED (attempt-02)** — exact
  statement, rational-not-integral (Atiyah–Hirzebruch Remark iv), known for
  $H^2$ (Kodaira–Spencer), §4 B/C as open special cases of HC, §5
  HC⇔fully-faithful-motives given B,C.
- Lefschetz $(1,1)$ via exponential sequence: **CORROBORATED (attempt-02)**
  via Deligne §1 (Kodaira–Spencer, $H^2$).
- Cattani–Deligne–Kaplan theorem: **CONFIRMED + sharpened (attempt-02)** —
  JAMS 8(2) 1995, unconditional, Weil-question, $SL(2)^r$ proof.
- **Still to-verify (attempt-07 targets):** hard Lefschetz reduction exact
  statement; the 2024–25 preprints' actual claims; status-check Shimizu 2025;
  Nygaard-Ogus reduce-to-Lefschetz-(1,1) mechanism (attempt-05 option (a),
  deferred). **(Attempt-06 closed option (b) — the Tate⟺BSD bridge:
  verified + refined, see the new to-verify entry below.)** **($\ell$-adic
  Tate analogue: VERIFIED + CORRECTED attempt-05 — the "open even for $H^2$"
  flagship is now a theorem.)**
- Charles–Markman 2013 standard conjectures for $K3^{[n]}$: **CONFIRMED
  (attempt-03, primary source)** — Compositio Math. 149(3) 2013, Thm 1.1 +
  Cor 1.2 (B ⇒ all incl. C in char 0; Verbitsky/twistor deformation control).
  Upgraded from `to-verify` to verified.
- Atiyah–Hirzebruch & Kollár integral counterexamples: **CONFIRMED
  (attempt-04, four primary sources)** — two sources of failure (torsion:
  AH 1961 / Totaro 1997 / Soulé–Voisin 2005 with the $p\le\dim$ ceiling +
  escape-all-topological Thm 3; non-torsion: Kollár 1990), and the
  $\mathbb Q$-retreat logic that removes both (torsion $\mapsto0$ over
  $\mathbb Q$; $D\alpha$ algebraic $\Rightarrow$ $\alpha$ algebraic over
  $\mathbb Q$). Upgraded from `to-verify` to verified.
- Tate⟺BSD-for-Jacobian equivalence (the cross-problem bridge to
  [[birch_swinnerton_dyer]]): **VERIFIED + REFINED (attempt-06, primary
  sources).** For a smooth projective surface $X/\mathbb F_q$ **fibered** over
  a curve (generic fiber $C/\mathbb F_q(t)$, $J=\mathrm{Jac}(C)$):
  Tate-for-divisors$(X)\iff$Artin-Tate$(X)\iff\mathrm{Br}(X)$ finite
  $\iff\text{\III}(J/\mathbb F_q(t))$ finite $\iff\mathrm{BSD}(J)$.
  Chain: Tate-Milne 1975 ($\mathrm{AT}\iff\mathrm{Br}(\ell)$-finite, incl.
  $p$-part by Milne via flat/de Rham-Witt/crystalline; jmilne.org article
  page) + Artin-Grothendieck ($\mathrm{Br}\iff\text{\III}$) + Kato-Trihan 2003
  ($\mathrm{BSD}\iff\text{\III}(\ell)$-finite), **re-proven directly by
  Lichtenbaum-Ramachandran-Suzuki 2022** (Épijournal G.A., DOI
  10.46298/epiga.2022.7482 / arXiv:2101.10222, two proofs); Gordon 1979 +
  Geisser 2020 (order relation) corroborate. **Two honest refinements of
  attempt-05's "BSD for the Jacobian":** (1) it is **function-field (char-$p$)
  BSD** — the geometric avatar, sharing the formulation with but NOT the
  number-field Millennium BSD over $\mathbb Q$ (function-field BSD is
  substantially proven via Kato-Trihan); a genuine avatar-level logical
  equivalence, the deepest cross-problem link, but not a direct bridge to
  the Millennium BSD. (2) it requires the **fibered-surface** setting. The
  Artin-Grothendieck / Kato-Trihan 2003 links search-surfaced (minor
  to-verify against the 2003 body). Upgraded from `to-verify` to verified
  (with scope refinement).

## Honesty check

- Recent claimed solutions flagged `hodge-recent-claims-unverified` (Shimizu
  2025 zero citations; Bouali 2024; Abdelgalil 2025 conditional; Mounda 2025 a
  conjecture; Hajebi & Hajebi 2025 asserts unproved spanning) — NONE
  peer-accepted [hodge-recent-claims-unverified]. Same discipline as YM's
  preprint flagging and Beal's (2,3,7) spherical-mislabel correction.
- $\ell$-adic Tate analogue [hodge-tate-analogue] — **CORRECTED (attempt-05):**
  the "open even for $H^2$" K3 flagship is now a theorem (Charles/Maulik/
  Madapusi Pera 2013–16); general Tate-for-divisors still open but reduced to
  surfaces (de Jong–Morrow). The char-0/char-p asymmetry at $H^2$ is largely
  closed; both HC and Tate are open at codim $\ge2$ (symmetric). A
  Tate-for-divisors-on-surface $\iff$ BSD-for-Jacobian bridge to
  [[birch_swinnerton_dyer]] recorded.
- No proof claimed here. Outcome attempt-01 = partial.