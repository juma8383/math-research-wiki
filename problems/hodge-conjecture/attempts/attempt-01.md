# Attempt 01 — Hodge Conjecture: frontier, obstruction, toolbox

> First attack. Establishes the clean form, exact frontier, open content,
> obstruction map, and forward directions. Verified from web searches
> 2026-08-24 before committing. Source: [hodge-survey](../../sources/hodge-survey.md)
> (web-search-compiled, NOT primary; flagged `[summary]`/to-verify).

## Clean form

On a smooth projective $X/\mathbb C$, the cycle class map
$\mathrm{cl}:\mathrm{CH}^p(X)\otimes\mathbb Q\to\mathrm{Hdg}^p(X)$ is
surjective for all $p$ [[def-hodge-class-cycle-map]]. Hodge classes
$\mathrm{Hdg}^p(X)=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)$ are analytic; algebraic
cycles are algebraic; the conjecture is the analytic→algebraic bridge.

## Frontier table

| Codim $p$ | Degree | Status | Reference |
|---|---|---|---|
| $0$ | $0$ | trivial | $[\mathrm{pt}]$ |
| $1$ | $2$ | **PROVEN** | Lefschetz $(1,1)$ [[thm-lefschetz-1-1]] [hodge-lefschetz-1-1] |
| $\in\{n-1,n\}$ | $2n-2,2n$ | proven (hard Lefschetz / trivial) | [[thm-hard-lefschetz-reduction]] [hodge-hard-lefschetz-reduction] |
| $2\le p\le n-2$ ($n\ge4$) | middle | **OPEN** | first case $p=2,n=4$ [hodge-codim-2-open] |

Only middle codimensions are new (hard Lefschetz). Smallest open case:
**codimension-2 Hodge classes on a 4-fold**. Deligne: open in dimension $\ge4$.

## Open content (named)

"**Hodge class (analytic) → algebraic cycle** in codimension $\ge2$" =
surjectivity of $\mathrm{cl}\otimes\mathbb Q$ in the middle codimensions.
Analog of:
- Beal: "finitely many → zero";
- BSD: "analytic rank $\le1$ → arbitrary rank";
- NS: "small/local → arbitrary large-data global regularity";
- YM: "lattice-discretized → continuum-rigorous 4D QFT with gap."

## Obstruction: control step, not resolution step

Resolution layer (works):
- Chow groups $\mathrm{CH}^p(X)$ and cycle class map $\mathrm{cl}$ defined for
  all $p$ [[def-hodge-class-cycle-map]].
- For $p=1$: exponential sequence $0\to\mathbb Z\to\mathcal O\to\mathcal O^*\to0$
  gives $\mathrm{Hdg}^1=\ker(H^2(\mathbb Z)\to H^2(\mathcal O))\subset\mathrm{Pic}$;
  for projective $X$, $\mathrm{NS}(X)=\mathrm{Pic}/\mathrm{Pic}^0$ is algebraic
  divisors (GAGA) — **the bridge works for divisors** [[thm-lefschetz-1-1]].
- Hard Lefschetz propagates $p=1$ to $p=n-1$ [[thm-hard-lefschetz-reduction]].

Control step (the gap):
- For codim $\ge2$, given an arbitrary Hodge class, no mechanism produces a
  $\mathbb Q$-combination of algebraic cycles mapping to it.
- The Griffiths **intermediate Jacobian** $J^p(X)$ / Abel–Jacobi map is
  *transcendental* for $p\ge2$ (not an abelian variety), and unlike the Picard
  variety for $p=1$ it does **not** control algebraicity.
- Unifying lens: the **analytic→algebraic bridge** works for $p=1$
  (exponential sequence, one-dimensional Picard object) and is conjectured for
  all $p$; the control over this bridge in codim $\ge2$ is the obstruction
  [[method-analytic-algebraic-bridge]].

Structural "one-dimensional engine stops" (5-for-5 pattern): the working tool
is intrinsically one-codimension / one-dimensional (Picard variety via
exponential sequence); the open content is the leap to higher codimension —
parallel to Beal's cubic coincidence, BSD's one-point Euler system, NS's 2D
Serrin equality, YM's single RG scale.

## Wrinkle: integral version is FALSE

Atiyah–Hirzebruch and Kollár: integral Hodge classes need not be algebraic
[[thm-integral-hodge-fails]] [hodge-integral-fails]. Only $\mathbb Q$-version
conjectured. Unlike the other four problems, Hodge has a built-in "naive
strong statement is false" (torsion/divisibility obstruction). The
$\mathbb Z$-version killed by differentials in the Atiyah–Hirzebruch spectral
sequence; the conjectural salvage is the $\mathbb Q$-statement. Park as a
*separate* obstruction or a symptom — see notes.md.

## Evidence layer (not resolution, but control-adjacent)

- **Absolute Hodge** (Deligne): every Hodge class on an abelian variety is
  absolute Hodge — behaves well under all $\mathrm{Aut}(\mathbb C)$
  [[thm-absolute-hodge-motivated]] [hodge-absolute-hodge]. André's motivated
  cycles extend. Strongest evidence; a "controlled" substitute where full
  algebraicity is out of reach.
- **Hodge locus algebraic** (Cattani–Deligne–Kaplan): Hodge locus is a
  countable union of algebraic subsets — Hodge classes behave "as if"
  algebraic [[thm-cattani-deligne-kaplan]] [hodge-cattani-deligne-kaplan].
- **Standard conjectures / motives**: if inverse Lefschetz (B) and Künneth
  components (C) are algebraic — known for surfaces, abelian, hyper-Kähler
  $K3^{[n]}$ (Charles–Markman 2013) — motives are Tannakian and HC reduces to
  a fully-faithful functor [[thm-standard-conjectures-motives]]
  [hodge-standard-conjectures]. The motive reduction.
- **Generalized HC** (Grothendieck coniveau) [[conj-generalized-hodge]]
  [hodge-generalized-conjecture]: finer; Hodge's original stronger form false.

## Cross-problem compounding (5-for-5)

"Obstruction at the control/reduction step, NOT the resolution step":
- Beal: reduction-to-finite (needs shared/even/spherical exponent);
- BSD: Selmer-group control (Euler system one-point-shaped, rank ≤1);
- NS: critical-norm control ($L^2$ subcritical $\not\to$ $L^3$ critical);
- YM: continuum-limit convergence + uniform-in-$a$ IR gap transport;
- **Hodge: analytic→algebraic conversion in codim $\ge2$**.

Related links added both ways to all four prior problems
[[beals_conjecture]] [[birch_swinnerton_dyer]] [[navier_stokes]] [[yang_mills]].
Recorded as candidate reusable methodology in notes.md.

## Forward directions

- **(A) Motive / standard-conjecture reduction** [[thm-standard-conjectures-motives]]:
  prove algebraicity of the inverse Lefschetz (B) and Künneth components (C) —
  the "reduction to specific Hodge classes" that makes HC a clean motive
  statement. Known for surfaces, abelian, hyper-Kähler $K3^{[n]}$; open
  generally. Closest analog of Beal's reduction-to-finite-curves.
- **(B) Codim-2 directly** [[method-analytic-algebraic-bridge]]: attack the
  first open case (codim-2 on a 4-fold) via Griffiths intermediate Jacobians /
  normal functions / Abel–Jacobi — the direct bridge at the frontier.
- **(C) Structured sub-cases** [[thm-absolute-hodge-motivated]]: deepen the
  abelian program (Weil type, type III); absolute Hodge / motivated cycles as
  the controlled evidence layer.

## Toolbox filed

- Definitions: def-hodge-class-cycle-map.
- Theorems: thm-lefschetz-1-1, thm-hard-lefschetz-reduction,
  thm-integral-hodge-fails, thm-absolute-hodge-motivated,
  thm-cattani-deligne-kaplan, thm-standard-conjectures-motives.
- Methods: method-analytic-algebraic-bridge.
- Conjectures: conj-generalized-hodge.
- Source: sources/hodge-survey.md (claim tags hodge-*).

## Honesty / to-verify

- No proof claimed; outcome = partial.
- Recent claimed solutions flagged `hodge-recent-claims-unverified` (Shimizu
  2025 / Preprints.org / zero citations; Bouali 2024; Abdelgalil 2025
  conditional on unproven "algebraicity of limits"; Mounda 2025 a conjecture
  not a proof; Hajebi & Hajebi 2025 asserts an unproved "spanning property") —
  NONE peer-reviewed or community-accepted [hodge-recent-claims-unverified].
  Same discipline as YM's preprint flagging and Beal's (2,3,7) correction.
- $\ell$-adic Tate analogue open even for $H^2$ [hodge-tate-analogue].
- To-verify (primary sources): Deligne Clay write-up (hodge.pdf); Lefschetz
  $(1,1)$ via exponential sequence; hard Lefschetz reduction; Atiyah–Hirzebruch
  & Kollár counterexamples; Cattani–Deligne–Kaplan; Charles–Markman; the
  2024–25 preprints' actual claims.