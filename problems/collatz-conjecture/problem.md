---
type: problem
slug: collatz-conjecture
title: Collatz Conjecture
status: in-progress
difficulty: famous-open-problem
created: 2026-08-24
last-updated: 2026-08-24
tags: [number-theory, dynamical-systems, discrete-dynamics, ergodic-theory]
tools: [[def-collatz-map], [thm-collatz-density-results], [thm-collatz-tao-almost-bounded], [thm-collatz-cycle-bounds], [thm-collatz-conway-undecidability], [method-average-vs-pointwise-control], [method-cycle-exclusion-linear-forms]]
related: [[beals_conjecture], [birch_swinnerton_dyer], [navier_stokes], [yang_mills], [hodge_conjecture]]
target-frontier: pointwise convergence (no divergent trajectory + no nontrivial cycle)
---

# Collatz Conjecture

## Statement [collatz-statement]

The **Collatz map** $T:\mathbb N^+\to\mathbb N^+$ [[def-collatz-map]]:
$$T(n)=\begin{cases}n/2 & n\text{ even},\\ 3n+1 & n\text{ odd}.\end{cases}$$
The trajectory of any $n$ is $n, T(n), T^2(n),\dots$ Let $\mathrm{Col}_{\min}(N):=\min_{k\ge0}T^k(N)$.

**Collatz Conjecture (3n+1 / Syracuse / Ulam-Kakutani):** for every
$n\in\mathbb N^+$, the trajectory eventually reaches $1$ (then cycles
$1\to4\to2\to1$); equivalently $\mathrm{Col}_{\min}(N)=1$ for all $N$.

Two failure modes: (a) a **nontrivial cycle** $\neq\{1,4,2\}$; (b) a
**divergent trajectory** ($T^k(n)\to\infty$). Both are open
[[def-collatz-map]].

## Known partial results

- **Computational verification** [collatz-verified]: verified for all
  $N\le 2^{68}\approx2.95\times10^{20}$ (Barina 2020); Oliveira e Silva
  $x_{\min}>5.76\times10^{18}$.
- **Density / almost-all results** [[thm-collatz-density-results]]:
  - Terras 1976 / Everett 1977: $\mathrm{Col}_{\min}(N)<N$ for **almost all**
    $N$ (natural density) [collatz-density-terras].
  - Allouche 1979: $\mathrm{Col}_{\min}(N)<N^\theta$ for any
    $\theta>3/2-\log3/\log2\approx0.869$, a.a. $N$ [collatz-density-allouche-korec].
  - Korec 1994: $\theta>\log3/\log4\approx0.792$.
  - Krasikov–Lagarias 2003: $\#\{N\le x:\mathrm{Col}_{\min}(N)=1\}\gg x^{0.84}$
    [collatz-kl-count].
- **Tao 2019/2022** [[thm-collatz-tao-almost-bounded]]: for any
  $f\to\infty$, $\mathrm{Col}_{\min}(N)<f(N)$ for **almost all** $N$
  (logarithmic density) — "almost all orbits attain almost bounded values"
  [collatz-tao-almost-bounded]. The strongest rigorous progress; Tao notes
  replacing $f\to\infty$ by a constant is "likely almost as hard as the full
  conjecture."
- **Cycle exclusion** [[thm-collatz-cycle-bounds]] [[method-cycle-exclusion-linear-forms]]:
  Steiner 1977 (no nontrivial 1-cycles); Simons 2004 (no 2-cycles);
  Simons–de Weger 2010 (no $m$-cycles for $1\le m\le75$; bounds for $m\ge76$),
  via the linear form $\Lambda=(K+L)\log2-K\log3$ and transcendence theory
  [collatz-cycle-steiner] [collatz-cycle-simons-deweger].
- **Average contraction heuristic** [collatz-average-contraction]: the
  accelerated map shrinks on average — $\mathbb E[k]=2>\log_2 3\approx1.585$
  halvings per odd step, giving geometric mean factor $3/4<1$ per two steps
  (distributional, NOT pointwise) [[method-average-vs-pointwise-control]].
- **Undecidability context** [[thm-collatz-conway-undecidability]]:
  Conway 1972 — generalized Collatz-type maps can simulate a universal TM;
  the halting/"ultimately cyclic" question is undecidable in general
  [collatz-conway-undecidable]. The 3n+1 map is a special "weak"/contracting
  case below the universality threshold ($\mu=3<4=2^2$)
  [collatz-matthews-watts] (Matthews–Watts).

## The obstruction (control step, not resolution step) [collatz-average-contraction]

The resolution layer works for **average/density control**: Terras (a.a.
$<N$), Allouche/Korec (a.a. $<N^\theta$), Krasikov–Lagarias (count $\gg x^{0.84}$),
Tao (a.a. $<f\to\infty$). The **cycle-exclusion** sub-problem is also a working
resolution tool up to $m\le75$ via transcendence. The gap is
**pointwise / universal control** — going from "almost all" (log/natural
density) to "every $N$." The average-contraction heuristic ($3/4<1$) is a
*distributional* statement over parity sequences; the parity sequence of a given
$N$ is deterministic and uncontrolled [[method-average-vs-pointwise-control]].

The obstruction **splits into two flavors**, making Collatz a compound of two
prior problems:
- **(a) No nontrivial cycle** — a **Diophantine / transcendence** problem
  (linear form $\Lambda=(K+L)\log2-K\log3$; Steiner/Simons/de Weger exclude
  $m\le75$) [[method-cycle-exclusion-linear-forms]] — echoes Beal's
  generalized-Fermat flavor [[beals_conjecture]].
- **(b) No divergent trajectory** — an **analytic / ergodic control** problem
  (need a rigorous per-trajectory contraction / Lyapunov; the average is
  $<1$ but no pointwise monotone quantity known) — echoes NS's
  critical-norm control [[navier_stokes]].

**Frontier (exact):** "almost all $\to$ every $N$." The smallest open
sub-problem is a single divergent trajectory OR a single nontrivial cycle of
period $\ge76$ (or any period beyond the verified bound).

## Status

In-progress; open content = "almost all (density) $\to$ every $N$
(pointwise/universal)." Outcome attempt-01 = partial (frontier + obstruction
mapped, no proof). Honesty: a 2024–25 preprint flurry claiming proofs (Fathi
2025 "entropy descent" = the standard average-contraction heuristic; Nwankpa
2025 mod-4/12 with gaps; Chang 2026 honestly conditional on an open
equidistribution conjecture) is flagged `collatz-recent-claims-unverified` —
NONE peer-reviewed or community-accepted, and they all fail at exactly the
average-vs-pointwise control step that *is* the obstruction
[collatz-recent-claims-unverified]. Erdős: "Mathematics may not be ready for
such problems." Same discipline as YM/Hodge's preprint flagging.