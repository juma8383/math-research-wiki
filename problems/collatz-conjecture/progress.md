# Collatz Conjecture — progress (read-first file)

> Start here. Navigational entry point; structural depth in
> [notes.md](notes.md) and [attempts/attempt-02.md](attempts/attempt-02.md).
> Verified 2026-08-24 from web searches BEFORE committing (same discipline as
> the other five; Beal's attempt-17 caught a silent arithmetic error this way).
> Consolidated through attempt-06.
> Source: [collatz-survey](../../sources/collatz-survey.md) — web-search-compiled,
> NOT primary; flagged `[summary]`/to-verify.

## Exact frontier

Collatz map $T(n)=n/2$ (even), $3n+1$ (odd); conjecture: every $N$ reaches $1$
[[def-collatz-map]]. $\mathrm{Col}_{\min}(N):=\min_k T^k(N)$; conjecture =
$\mathrm{Col}_{\min}(N)=1$ for all $N$.

| Result | Scope | Status |
|---|---|---|
| Verified computationally | $N\le 2^{68}\approx2.95\times10^{20}$ (Barina 2020/2021, peer-reviewed, J. Supercomput. 77); **project-reported frontier $2^{71}\approx2.36\times10^{21}$ (Jan 2025, `to-verify`)** | done [collatz-verified] |
| Terras/Everett: $\mathrm{Col}_{\min}<N$ | almost all, natural density | proven [collatz-density-terras] |
| Allouche/Korec: $\mathrm{Col}_{\min}<N^\theta$ | almost all, $\theta\downarrow0.79$ | proven [collatz-density-allouche-korec] |
| Krasikov–Lagarias: count reaches 1 | $\#\{\}\gg x^{0.84}$ | proven [collatz-kl-count] |
| Tao: $\mathrm{Col}_{\min}<f(N)$, any $f\to\infty$ | almost all, log-density | proven [collatz-tao-almost-bounded] |
| No nontrivial $m$-cycle | $m\le75$ | proven [collatz-cycle-simons-deweger] |
| **Every $N$ reaches 1** | **all $N$** | **OPEN** |

The gap is the leap from **density** (almost all) to **pointwise** (every $N$).

## Verified base

- Terras 1976 / Everett 1977: a.a. $\mathrm{Col}_{\min}(N)<N$ (natural density)
  [[thm-collatz-density-results]] [collatz-density-terras].
  **attempt-03 (primary-source):** Terras, *Acta Arith.* **30**, 241–252 (1976);
  Everett, *Adv. Math.* **25**, 42–45 (1977). The set with finite **stopping
  time** $\sigma(n):=\min\{k:T^k(n)<n\}$ has density **1 at an exponential
  rate** (Terras Thm D; $\ln2/\ln3>1/2$ binomial decay of "divergent" parity
  vectors; parity vector $\leftrightarrow$ residue class mod $2^k$). Found
  independently also by Möller 1977, Heppner 1978, Allouche 1979 — five
  independent proofs, robust.
- Allouche 1979 ($\theta>3/2-\log3/\log2\approx0.869$), Korec 1994
  ($\theta>\log3/\log4\approx0.792$): a.a. $\mathrm{Col}_{\min}<N^\theta$
  [collatz-density-allouche-korec].
- Krasikov–Lagarias 2003: $\#\{N\le x:\mathrm{Col}_{\min}(N)=1\}\gg x^{0.84}$
  [collatz-kl-count].
  **attempt-03 (primary-source):** *Acta Arith.* **109**(3), 237–258, DOI
  10.4064/aa109-3-4. Thm 6.1: $\pi_1(x)\ge x^{0.84}$, $0.84=\log_2(1.7922)$
  from LP $L_{NT}^{11}$ (k=11). Method = Krasikov difference inequalities +
  **back-substitution** (Thm 2.2/3.1) eliminating "advanced" variables without
  the truncation Applegate-Lagarias 1995 needed ($x^{0.81}$). **Authors'
  conjecture $\lambda_k\to2$ would give $\pi_1(x)\ge x^{1-\varepsilon}$ — the
  method's theoretical ceiling is "almost all", never "all"**: a *second*
  Collatz "one-dimensional engine stops" instance (count engine, parallel to
  the Terras density engine). Both stop at density-1 / $x^{1-\varepsilon}$;
  neither reaches pointwise.
- Tao 2019/2022: a.a. (log-density) $\mathrm{Col}_{\min}(N)<f(N)$ for any
  $f\to\infty$ — "almost all orbits attain almost bounded values"
  [[thm-collatz-tao-almost-bounded]] [collatz-tao-almost-bounded].
  **attempt-02 (primary-source, Forum Math. Pi 10, 2022, e12, DOI
  10.1017/fmp.2022.8):** Theorem 1.3 confirmed. The **trade-off is the key
  fact:** Korec had $\mathrm{Col}_{\min}\le N^\theta$ ($\theta>\log3/\log4\approx
  0.792$) in **natural density**; Tao replaces $N^\theta$ by **any $f\to\infty$**
  but drops to **logarithmic density** — the two improvements (stronger
  function $\leftrightarrow$ stronger density) are in tension. The blocker is
  the $\exp(O(n^{1/2}))$ multiplicative error in the Syracuse heuristic
  $\mathrm{Syr}^n(N)\approx\exp(O(n^{1/2}))(3/4)^n N$, controllable only at
  log-density (Benford). Proof borrows **Bourgain's almost-sure NLS
  wellposedness** stabilization — a mechanism-level NS echo.
- Steiner 1977 (no 1-cycles), Simons 2004 (no 2-cycles), Simons–de Weger 2010
  (no $m$-cycles $m\le75$), via linear form $\Lambda=(K+L)\log2-K\log3$ +
  transcendence (Laurent–Mignotte–Nesterenko, Rhin)
  [[thm-collatz-cycle-bounds]] [[method-cycle-exclusion-linear-forms]]
  [collatz-cycle-steiner] [collatz-cycle-simons-deweger].
  **attempt-02 (primary-source, Acta Arith. 117, 2005 + 2010 update v1.44):**
  the **$m\le75$ is the 2010 update** (Oliveira e Silva $x_{\min}>5\cdot2^{60}$);
  the 2005 published bound is **$m\le68$**. Method = $\Lambda=(K+L)\log2-K\log3$,
  upper bound exponential in $K$ (chaining), lower bound from **Rhin 1987
  irrationality measure** ($\Lambda>e^{-13.3(0.46057+\log K)}$), continued
  fractions of $\delta=\log3/\log2$ + LLL. **Rhin's bound + the exponential
  upper bound are near-optimal** (the authors' own assessment) — the method is
  **per-$m$ finite-verification, no uniform all-$m$ bound**; "all $m" needs a
  uniform transcendence improvement or a non-linear-form approach.
- Conway 1972: generalized Collatz maps universal → halting undecidable in
  general; 3n+1 is a weak/contracting case ($\mu=3<4=2^2$)
  [[thm-collatz-conway-undecidability]] [collatz-conway-undecidable]
  [collatz-matthews-watts].
  **attempt-04 (primary-source):** Conway, *Unpredictable Iterations* (1972)
  — generalized $g(n)=a_i n+b_i$ ($n\equiv i\pmod p$); Main Thm + Corollary:
  **no algorithm** decides whether $g^k(n)=1$ (generalized problem
  **undecidable**; via Minsky machines → vector/rational games → FRACTRAN
  1987). **Kurtz–Simon 2007** (TAMC, LNCS 4484, 542–553) sharpened to
  **$\Pi^0_2$-complete** — the uniform "every orbit hits $1$" problem is
  undecidable, and its $\forall n\,\exists k\,T^k(n){=}1$ shape matches the
  specific $3n{+}1$ conjecture. **Contracting framing confirmed (Matthews–
  Watts/Lagarias):** shortcut map $T(x){=}x/2$ (even), $(3x{+}1)/2$ (odd),
  $d{=}2$, $(a_0,a_1){=}(1,3)$, $\prod a_i{=}3<4{=}d^d$, geometric mean
  $(3/4)^{1/2}\approx0.866<1$ → contracting regime (convergence expected).
  **Honesty flag:** the Matthews–Watts criterion is a **conjectural
  heuristic, not a theorem** — "$\prod a_i<d^d\Rightarrow$ cycle" is itself
  the Collatz conjecture for $3n{+}1$; Conway's amusical permutation $\mu$
  (Monthly 120(3), 2013) is contracting by the same criterion ($3^4{<}4^4$)
  yet conjectured to have infinite orbits. **The $\Pi^0_2$-completeness is
  the new load-bearing fact:** any *uniform* (all generalized $T$) argument
  is impossible; a $3n{+}1$ proof must exploit the concrete contracting
  structure — a per-instance **control** argument, exactly the open piece
  (the *resolution* = a general decision procedure is ruled out by
  undecidability).
  **attempt-05 (verification + evidence update):** Barina 2020/2021
  CONFIRMED — D. Barina, *Convergence verification of the Collatz
  problem*, **J. Supercomput. 77** (2021), 2681–2688, DOI
  10.1007/s11227-020-03368-x; verified all $N\le2^{68}$ by 2020-05-07 via
  a novel $O(N)$-table (not $O(2^N)$) 128-bit GPU algorithm ($\sim2.2
  \times10^{11}$/sec on RTX 2080); path record
  $n=274{,}133{,}054{,}632{,}352{,}106{,}267$ below $2^{68}$, confirming
  the Lagarias-Weiss $n^2$ peak-height prediction. **Evidence line
  UPDATED (append-only):** the record has since **advanced** — Barina's
  project website reports $2^{69}$ (Dec 2021), $2^{70}$ (Jul 2023),
  $1.5\cdot2^{70}$ (Nov 2023), **$2^{71}\approx2.36\times10^{21}$ (Jan
  2025)**, the current frontier — **but the $2^{71}$ is self-reported,
  NOT peer-reviewed** (the published figure stays $2^{68}$); flagged
  `to-verify` against a publication (same publication-status split as YM
  Faizal-Shabir / NS Hou-Seregin). **Oliveira e Silva precision:**
  $20\cdot2^{58}\approx2^{62.3}$ (AMS 2010, *Ultimate Challenge* pp
  189–207), not bare $2^{58}$. **No counterexample** at any bound.
  **Control-step echo (the cleanest "one-dimensional engine stops"):
  the verification engine controls the "checked instances" slice
  (resolution) and stops at the "all $n$" slice (control) — $2^{71}$
  instances is measure-zero vs $\mathbb N$, and $\Pi^0_2$-completeness
  (attempt-04) means no uniform algorithm exists for the generalized
  problem, so the stop is *logical*, not merely technical. Reinforces,
  does not move, the attempt-04 wall.
- Average contraction: accelerated map shrinks on average, $\mathbb E[k]=2>
  \log_2 3\approx1.585$, geometric mean $3/4<1$ per two steps
  [collatz-average-contraction].

## Open content

"**Almost all (density) → every $N$ (pointwise/universal).**" Equivalently:
exclude the two failure modes for *every* starting value — (a) a nontrivial
cycle, (b) a divergent trajectory. The Hodge/YM/etc. analog:
- Beal: "finitely many → zero";
- BSD: "analytic rank $\le1$ → arbitrary rank";
- NS: "small/local → arbitrary large-data global regularity";
- YM: "lattice-discretized → continuum-rigorous 4D QFT with gap";
- Hodge: "Hodge class (analytic) → algebraic cycle in codim $\ge2$";
- **Collatz: "almost all (density) → every $N$ (pointwise)."**

## Obstruction (control step, not resolution step)

Resolution layer (works): the average/density machinery controls a
density-1 / almost-all set — Terras, Allouche/Korec, Krasikov–Lagarias, Tao.
The cycle-exclusion machinery (transcendence) rules out small cycles
($m\le75$). Both are *resolution* tools for their slice.

Control step (the gap): **pointwise / universal** control. The average
contraction $3/4<1$ is a *distributional* statement over parity sequences; the
parity sequence of a given $N$ is deterministic and uncontrolled, so a
density-1 result cannot exclude a measure-zero exceptional set (which could
contain a divergent trajectory or a nontrivial cycle)
[[method-average-vs-pointwise-control]]. Tao: replacing $f\to\infty$ by a
constant is "likely almost as hard as the full conjecture."

The obstruction **splits** into two prior-problem flavors:
- **(a) No nontrivial cycle** — Diophantine / transcendence (linear forms in
  logs $\Lambda=(K+L)\log2-K\log3$; excluded $m\le75$, open beyond)
  [[method-cycle-exclusion-linear-forms]] — echoes Beal's generalized-Fermat
  flavor [[beals_conjecture]].
- **(b) No divergent trajectory** — analytic / ergodic control (need a
  per-trajectory contraction / Lyapunov; average $<1$ but no pointwise
  monotone quantity) — echoes NS's critical-norm control [[navier_stokes]].

## "One-dimensional engine stops" (6-for-6 pattern)

The working tool is a *single-scale / average / one-cycle-type* engine that
controls its slice, and the open content is the leap beyond:
- Beal: cubic-cubic-cubic coincidence (one exponent shape);
- BSD: one-point Euler system (rank $\le1$);
- NS: 2D Serrin-index equality $3=3$;
- YM: single RG scale / asymptotic freedom;
- Hodge: Picard-variety one-codimension (exponential sequence);
- **Collatz: average over one parity sequence ($3/4<1$), density-1 only.**

## Forward directions

- **(A) Upgrade density → pointwise** [[method-average-vs-pointwise-control]]:
  strengthen Tao's log-density result to natural density, then to a pointwise
  bound; the direct "almost all → all" attack. Closest to the heart.
  **attempt-02 sharpening (two stages, each with a named blocker):**
  **(A-i) log-density → natural density** keeping "any $f\to\infty$" — blocker
  is the $\exp(O(n^{1/2}))$ multiplicative error in the Syracuse heuristic
  (controlled by Fourier-decay/mixing only at log-density; needs sharper 3-adic
  mixing for natural density). **(A-ii) natural density → pointwise** — blocker
  is the deterministic uncontrolled parity sequence (no pointwise
  Lyapunov/monotone quantity; the $(3/4)^n$ is distributional) — the NS-flavored
  part. Tao: replacing $f\to\infty$ by a constant is "likely almost as hard as
  the full conjecture" (i.e. (A-ii) pointwise-with-constant ≈ the conjecture).
  Realistic compounding frontier = (A-i), a *control* improvement (of the
  $\exp(O(n^{1/2}))$ error), not resolution.
- **(B) Cycle exclusion to all $m$** [[method-cycle-exclusion-linear-forms]]:
  push Steiner/Simons–de Weger beyond $m\le75$ via sharper linear-form-in-logs
  / transcendence bounds (the Diophantine sub-problem, Beal-flavored).
  **attempt-02 sharpening (primary-source):** splits into **(B-finite)**
  per-$m$ verification further (more $x_{\min}$ computation + continued
  fractions) — incremental, bounded — vs **(B-uniform)** a uniform/all-$m$
  argument — open, transcendence-bottlenecked. Simons–de Weger's own
  assessment: Rhin's irrationality measure + the exponential $\Lambda$ bound
  are **near-optimal**, so (B-uniform) needs a better irrationality measure for
  $\log3/\log2$ or a non-linear-form approach — the **literal Beal-flavored
  transcendence wall** (linear forms in logs degrade for large parameters).
- **(C) Divergent-trajectory Lyapunov** [[navier_stokes]] echo: find a
  rigorous per-trajectory decreasing quantity (a true Lyapunov, not just an
  average) — the NS-flavored analytic control sub-problem.

## To-verify (primary sources, before load-bearing use)

Tao 2022 (Forum Math. Pi, DOI 10.1017/fmp.2022.8) — **CONFIRMED (attempt-02)**;
Terras 1976 / Everett 1977 — **CONFIRMED (attempt-03, primary source)**;
Krasikov–Lagarias 2003 (Acta Arith. 109(3), 237–258, DOI 10.4064/aa109-3-4) —
**CONFIRMED (attempt-03, primary source)**;
Steiner 1977 / Simons 2004 / Simons–de Weger 2010 — **CONFIRMED (attempt-02)**;
Conway 1972 (FRACTRAN/undecidability) + Kurtz–Simon 2007 ($\Pi^0_2$-complete) +
contracting framing — **CONFIRMED (attempt-04, primary source)**;
**Still to-verify (attempt-07 targets):** the **$2^{71}$ project-reported
bound** (Barina website, Jan 2025, self-reported — `to-verify` against a
publication if Barina publishes the extension); the Santana refutation
(arXiv:2601.03297, $f_0(n)=n$ counterexample — search-surfaced via Pith,
minor to-verify directly). **(2024-26 claimed proofs: STATUS-CHECKED
attempt-06 — see below; Barina 2020 $2^{68}$: CONFIRMED attempt-05.)**

## Honesty check

- No proof claimed; outcome attempt-01 = partial.
- 2024–25 preprints flagged `collatz-recent-claims-unverified`:
  **STATUS-CHECKED attempt-06 — none peer-accepted; all fail at the
  average-vs-pointwise control step; 6-for-6 wall reinforced from the
  negative side.**
  - **Fathi 2025** = THREE Zenodo preprints (entropy-descent / potential-
    descent+mod-32 / Kolmogorov-compression; Zenodo DOIs 10.5281/zenodo.
    {15191755,15313916,15549017}), all 0-citation unreviewed, not on arXiv;
    the load-bearing "entropy descent" one uses $\mathbb E[k]=2>\log_2 3$ =
    the standard average-contraction heuristic (distributional, not
    pointwise). Flag RESOLVED.
  - **Nwankpa 2025** (Preprints.org, DOI 10.20944/preprints202503.0929.v9,
    v9) = a **mod-9 17-state FSM** reduction — **CORRECTION (append-only):
    mod-9 FSM, not "mod-4/12"**; the flaw is the modular-residue≠magnitude
    reduction (a finite-slice engine can't control unbounded magnitude).
    Unreviewed, 0-citation. Flag RESOLVED.
  - **Chang 2026** (arXiv:2603.11066) = **honestly conditional**, explicitly
    NOT a proof; reduces Collatz to an open **Orbit Equidistribution
    Conjecture**; machine-reviewed by **Pith** (a machine-review platform,
    NOT human peer review) → **CONDITIONAL**; self-corrected a false "Gap
    Lemma." Sharpened.
  - **Sibling claims surfaced:** **Santana 2026** (arXiv:2601.03297) —
    **REJECTED** by Pith, main theorem **REFUTED** by the counterexample
    $f_0(n)=n$ (fixed points in the paper's own family); Kawasaki 2025
    (arXiv:2502.20642, fixed-point approach, considered flawed); Trifaro
    2025 (viXra). All unreviewed.
  They all fail at exactly the average-vs-pointwise control step
  [collatz-recent-claims-unverified] — a **negative-side confirmation** of
  the 6-for-6 wall (corroborative, not probative). Same discipline as
  YM/Hodge.
- Conway's undecidability is for *generalized* maps, NOT the specific 3n+1 —
  flagged to avoid overclaiming the problem's difficulty (it may be genuinely
  undecidable, but that's unproved).