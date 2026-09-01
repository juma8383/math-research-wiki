---
type: source
id: collatz-survey
title: "Collatz Conjecture status — compiled from web-search summaries"
author: "(compiled, not a primary source)"
date: 2026-08-24
provenance: "web searches; URLs below; NOT verbatim primary sources — flagged [summary]"
tags: [collatz-statement, collatz-verified, collatz-density-terras, collatz-density-allouche-korec, collatz-kl-count, collatz-tao-almost-bounded, collatz-cycle-steiner, collatz-cycle-simons-deweger, collatz-conway-undecidable, collatz-matthews-watts, collatz-average-contraction, collatz-recent-claims-unverified]
used-in: [[collatz_conjecture]]
---

# Collatz Conjecture status survey (compiled from web searches)

> Compiled 2026-08-24 from three web searches; **not a verbatim primary
> source**. Each `[summary]` claim should be re-verified against primary
> sources before load-bearing use. URLs:
> https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/
> (Tao blog);
> https://doi.org/10.1017/fmp.2022.8 (Tao, Forum Math. Pi 2022);
> https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/
> (Tao full text);
> https://deweger.net/papers/[35a]SidW-3n+1-v1.44[2010].pdf (Simons–de Weger);
> https://doi.org/10.46298/dmtcs.3512 (Belaga–Mignotte, Conway/Matthews-Watts).

## [collatz-statement] Statement (3n+1 / Syracuse / Ulam-Kakutani)
[summary] T(n)=n/2 (even), 3n+1 (odd); conjecture every N reaches 1
(cycle 1-4-2-1). Two failure modes: a nontrivial cycle ≠{1,4,2}, or a
divergent trajectory (T^k(n)→∞). Both open. Col_min(N):=min_k T^k(N);
conjecture = Col_min(N)=1 for all N. [used-in: [[collatz_conjecture]] [[def-collatz-map]]]

## [collatz-verified] Computational verification
[summary] Verified for all N ≤ 2^68 ≈ 2.95×10^20 (Barina 2020); Oliveira e
Silva x_min > 5.76×10^18. No counterexample found. [used-in: [[collatz_conjecture]] [[thm-collatz-cycle-bounds]]]

## [collatz-density-terras] Terras (1976) / Everett (1977)
[summary] Col_min(N) < N for almost all N (natural density). Almost every
start eventually drops below itself. [used-in: [[thm-collatz-density-results]]]

## [collatz-density-allouche-korec] Allouche (1979), Korec (1994)
[summary] Col_min(N) < N^θ for almost all N: Allouche any
θ > 3/2 - log3/log2 ≈ 0.869; Korec any θ > log3/log4 ≈ 0.792. Pushing the
almost-all bound toward smaller powers. [used-in: [[thm-collatz-density-results]]]

## [collatz-kl-count] Krasikov–Lagarias (2003, Acta Arith. 109)
[summary] #{N ≤ x : Col_min(N) = 1} ≫ x^0.84 for sufficiently large x. A
rigorous lower bound on the COUNT of integers reaching 1 (power 0.84 < 1,
still far from "almost all reach 1"). [used-in: [[thm-collatz-density-results]]]

## [collatz-tao-almost-bounded] Tao (2019/2022, Forum Math. Pi)
[summary] For any f: N^+ → R with f(N) → +∞, Col_min(N) < f(N) for almost all
N (LOGARITHMIC density). E.g. Col_min < log log log log N a.a. "Almost all
orbits attain almost bounded values." Techniques: accelerated Syracuse map,
3-adic analysis, approximately invariant probability measures
(Bourgain-inspired, NLS analogy), first-passage stabilization,
superpolynomial Fourier decay, 2D renewal process. Tao: replacing f→∞ by a
constant is "likely almost as hard as the full Collatz conjecture."
[used-in: [[thm-collatz-tao-almost-bounded]] [[method-average-vs-pointwise-control]]]

## [collatz-cycle-steiner] Steiner (1977) — no 1-cycles
[summary] No nontrivial 1-cycles exist. Via linear form in logs
Λ = (K+L)log2 - K log3 forced exponentially small by a cycle, contradicting
transcendence lower bounds for small m. [used-in: [[thm-collatz-cycle-bounds]]]

## [collatz-cycle-simons-deweger] Simons (2004), Simons–de Weger (2010)
[summary] Simons 2004: no nontrivial 2-cycles. Simons–de Weger 2010: no
nontrivial m-cycles for 1 ≤ m ≤ 75; explicit upper/lower bounds on K, L,
x_min for m ≥ 76. Uses linear forms in logs (Laurent–Mignotte–Nesterenko,
Rhin), continued fractions of log3/log2, diophantine-approximation lattice
methods. Bounds degrade for large m; no exclusion of all cycles.
[used-in: [[thm-collatz-cycle-bounds]] [[method-cycle-exclusion-linear-forms]]]

## [collatz-conway-undecidable] Conway (1972) — generalized maps undecidable
[summary] Generalized Collatz-type (Conway) maps T(n)=(m_i n - r_i)/p can
simulate a universal Turing machine; the "ultimately cyclic?" question is
UNDECIDABLE for general such maps. NOTE: this is for GENERAL maps, NOT the
specific 3n+1 — does not prove 3n+1 undecidable (common overclaim to avoid).
[used-in: [[thm-collatz-conway-undecidability]]]

## [collatz-matthews-watts] Matthews–Watts (contracting vs expanding)
[summary] Classifies generalized maps by growth parameter μ. Contracting
(μ < p^p): all trajectories conjectured ultimately cyclic. Expanding
(μ > p^p): almost all trajectories conjectured divergent (experimentally
~1.3% of starts diverge for μ=28 > 27 = 3^3). For 3n+1: μ = 3 < 4 = 2^2,
contracting — no divergent trajectory expected. [used-in: [[thm-collatz-conway-undecidability]]]

## [collatz-average-contraction] Average contraction heuristic
[summary] Accelerated Syracuse map: one odd step multiplies by 3 and divides
by 2^{k(n)}, k(n)=ν_2(3n+1). Heuristically E[k(n)] = 2 > log_2 3 ≈ 1.585, so
each odd step multiplies by ≈ 3/4 < 1 on average — entropy decreases on
average, predicting convergence. DISTRIBUTIONAL over parity sequences, NOT
pointwise — this gap IS the obstruction. [used-in: [[method-average-vs-pointwise-control]] [[def-collatz-map]]]

## [collatz-recent-claims-unverified] Recent claimed solutions (NOT peer-accepted)
[summary] 2024–25 preprint flurry: Fathi 2025 (Zenodo, "entropy descent" =
the standard average-contraction heuristic dressed as "Recursive Type
Arithmetic", claims non-probabilistic but uses E[k]=2 which IS
distributional); Nwankpa 2025 (Preprints.org, mod-4/12 residue analysis,
gaps in handling the full accelerated map / shared odd primes); Chang 2026
(arXiv, burst-gap decomposition, HONESTLY conditional on an open "Orbit
Equidistribution Conjecture"). NONE peer-reviewed or community-accepted;
all fail at exactly the average-vs-pointwise control step that IS the
obstruction. viXra preprints (2408.0100, 2505.0010) likewise unvetted.
[used-in: [[collatz_conjecture]]]