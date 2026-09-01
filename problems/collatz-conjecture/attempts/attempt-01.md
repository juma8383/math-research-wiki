# Attempt 01 — Collatz Conjecture: frontier, obstruction, toolbox

> First attack. Establishes the clean form, exact frontier, open content,
> obstruction map, and forward directions. Verified from web searches
> 2026-08-24 before committing. Source:
> [collatz-survey](../../sources/collatz-survey.md) (web-search-compiled, NOT
> primary; flagged `[summary]`/to-verify).

## Clean form

Collatz map $T(n)=n/2$ (even), $3n+1$ (odd) [[def-collatz-map]]. Conjecture:
every $N\in\mathbb N^+$ reaches $1$ (cycle $1\to4\to2\to1$); i.e.
$\mathrm{Col}_{\min}(N):=\min_k T^k(N)=1$ for all $N$. Two failure modes: a
nontrivial cycle, or a divergent trajectory.

## Frontier table

| Result | Scope | Status |
|---|---|---|
| Verified | $N\le2^{68}\approx2.95\times10^{20}$ (Barina 2020) | done [collatz-verified] |
| Terras/Everett: $\mathrm{Col}_{\min}<N$ | a.a., natural density | proven [collatz-density-terras] |
| Allouche/Korec: $\mathrm{Col}_{\min}<N^\theta$ | a.a., $\theta\downarrow0.79$ | proven [collatz-density-allouche-korec] |
| Krasikov–Lagarias | $\#\{N\le x:\mathrm{Col}_{\min}=1\}\gg x^{0.84}$ | proven [collatz-kl-count] |
| Tao: $\mathrm{Col}_{\min}<f(N)$, any $f\to\infty$ | a.a., log-density | proven [collatz-tao-almost-bounded] |
| No nontrivial $m$-cycle | $m\le75$ | proven [collatz-cycle-simons-deweger] |
| **Every $N\to1$** | **all $N$** | **OPEN** |

The gap: density (almost all) → pointwise (every $N$).

## Open content (named)

"**Almost all (density) → every $N$ (pointwise/universal).**" Exclude both
failure modes for every start — a nontrivial cycle (any period) and a
divergent trajectory. Analog of:
- Beal "finitely many → zero"; BSD "rank $\le1$ → arbitrary rank";
  NS "small/local → arbitrary large-data"; YM "lattice → continuum with gap";
  Hodge "Hodge class → algebraic cycle in codim $\ge2$".

## Obstruction: control step, not resolution step

Resolution layer (works):
- Density machinery: Terras (a.a. $<N$), Allouche/Korec (a.a. $<N^\theta$),
  Krasikov–Lagarias (count $\gg x^{0.84}$), Tao (a.a. $<f\to\infty$)
  [[thm-collatz-density-results]] [[thm-collatz-tao-almost-bounded]].
- Cycle exclusion: Steiner (no 1-cycles), Simons (no 2-cycles),
  Simons–de Weger (no $m$-cycles $m\le75$) via the linear form
  $\Lambda=(K+L)\log2-K\log3$ + transcendence
  [[thm-collatz-cycle-bounds]] [[method-cycle-exclusion-linear-forms]].

Control step (the gap): **pointwise / universal** control. The average
contraction $3/4<1$ ($\mathbb E[k]=2>\log_2 3$) is *distributional* over parity
sequences; a given $N$'s parity sequence is deterministic and uncontrolled, so
density-1 results cannot exclude a measure-zero exceptional set (a divergent
trajectory or a nontrivial cycle) [[method-average-vs-pointwise-control]].
Tao: replacing $f\to\infty$ by a constant is "likely almost as hard as the
full conjecture."

The obstruction **splits** into two prior-problem flavors (unique to Collatz):
- **(a) Cycle exclusion** — Diophantine / transcendence (linear forms in
  logs; excluded $m\le75$, open beyond) — the **Beal** flavor
  [[beals_conjecture]].
- **(b) Divergent-trajectory exclusion** — analytic / ergodic control (need
  a per-trajectory Lyapunov; average $<1$, no pointwise monotone quantity) —
  the **NS** flavor [[navier_stokes]].

## Evidence / context layer

- Average contraction heuristic [collatz-average-contraction]: accelerated map
  shrinks on average, $\mathbb E[k]=2>\log_2 3\approx1.585$, geometric mean
  $3/4<1$ per two steps — the resolution tool *and* the thing that fails to be
  pointwise.
- Conway undecidability [[thm-collatz-conway-undecidability]]
  [collatz-conway-undecidable]: generalized Collatz maps universal → halting
  undecidable in general; 3n+1 is a weak/contracting case ($\mu=3<4=2^2$,
  Matthews–Watts [collatz-matthews-watts]). A "framework" wrinkle echoing YM —
  the possibility 3n+1 is *itself* undecidable is real but unproved (Conway's
  result is for *general* maps).

## Cross-problem compounding (6-for-6)

"Obstruction at the control/reduction step, NOT the resolution step":
- Beal: reduction-to-finite (shared/even/spherical exponent);
- BSD: Selmer control (one-point Euler system, rank $\le1$);
- NS: critical-norm control ($L^2$ subcritical $\not\to$ $L^3$ critical);
- YM: continuum-limit + uniform-in-$a$ IR gap transport;
- Hodge: analytic→algebraic conversion in codim $\ge2$;
- **Collatz: average/density → pointwise/universal control.**

Related links added both ways to all five prior problems. Recorded as
candidate reusable methodology in notes.md. Collatz is the cleanest exemplar
(the average-contraction heuristic *is* the obstruction, made visceral) and
uniquely *compounds* two earlier flavors (Beal-cycle + NS-divergence).

## Forward directions

- **(A) Density → pointwise** [[method-average-vs-pointwise-control]]:
  strengthen Tao's log-density to natural density, then to a pointwise bound;
  the direct "almost all → all" attack.
- **(B) Cycle exclusion to all $m$** [[method-cycle-exclusion-linear-forms]]:
  push Steiner/Simons–de Weger beyond $m\le75$ via sharper linear-form-in-logs
  / transcendence (Beal-flavored Diophantine sub-problem).
- **(C) Divergent-trajectory Lyapunov** [[navier_stokes]] echo: find a
  rigorous per-trajectory decreasing quantity (NS-flavored analytic control).

## Toolbox filed

- Definitions: def-collatz-map.
- Theorems: thm-collatz-density-results, thm-collatz-tao-almost-bounded,
  thm-collatz-cycle-bounds, thm-collatz-conway-undecidability.
- Methods: method-average-vs-pointwise-control,
  method-cycle-exclusion-linear-forms.
- Source: sources/collatz-survey.md (claim tags collatz-*).

## Honesty / to-verify

- No proof claimed; outcome = partial.
- 2024–25 preprints flagged `collatz-recent-claims-unverified` (Fathi 2025 =
  average-contraction heuristic, claims non-probabilistic but uses
  $\mathbb E[k]=2$; Nwankpa 2025 mod-4/12 with gaps; Chang 2026 honestly
  conditional on an equidistribution conjecture) — NONE peer-accepted; all
  fail at exactly the average-vs-pointwise control step
  [collatz-recent-claims-unverified]. Same discipline as YM/Hodge.
- Conway's undecidability is for *generalized* maps, NOT 3n+1 specifically —
  flagged to avoid overclaiming; the specific 3n+1 independence/undecidability
  is unproved (candidate attempt-02 investigation).
- To-verify (primary sources): Tao 2022 (Forum Math. Pi); Terras 1976;
  Krasikov–Lagarias 2003; Steiner 1977 / Simons 2004 / Simons–de Weger 2010;
  Conway 1972; Barina 2020; the 2024–25 preprints' actual claims.