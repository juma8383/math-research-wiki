---
type: attempt
problem: collatz_conjecture
attempt: 3
date: 2026-08-24
approach: Verify the foundational density base (Terras 1976 / Everett 1977) and the Krasikov-Lagarias 2003 count bound against primary sources, pinning exact citations + the control-step echo
outcome: confirmed
tags: [verification, primary-source, density, stopping-time, krasikov-lagarias, cross-problem]
---

# Attempt 03 — Verify Terras/Everett (density) + Krasikov-Lagarias 2003 (count)

Cycle-11 Continue on Collatz (cross-problem loop, second pass; yellow zone
78.7% session / 50.6% weekly, 0 subagents). Attempt-02 verified the two
*strongest* results (Tao 2022 almost-bounded, Simons-de Weger 2010 cycle
exclusion); the to-verify list still carried the **foundational density base**
(Terras 1976 / Everett 1977) and the **Krasikov-Lagarias 2003 count bound**,
which everything above them rests on. This cycle verifies both against the
primary source. Same discipline that caught the NS Buckmaster-Vicol date
(2019 not 2022) and the Hodge journal (Compositio not Jussiu).

## Verification 1: Terras 1976 / Everett 1977 — CONFIRMED

- **Riho Terras**, *A stopping time problem on the positive integers*,
  **Acta Arithmetica 30**, 241–252 (1976) [IMAN, CC-BY].
- **C. J. Everett**, *Iteration of the number-theoretic function
  f(2n)=n, f(2n+1)=3n+2*, **Advances in Mathematics 25**, 42–45 (1977).

**The density result (Terras's Theorem A, found independently by Everett):**
the set of integers with **finite stopping time** σ(n):=min{k: T^k(n)<n} has a
limiting asymptotic density, and that density **equals 1** — equivalently,
almost all integers eventually reach a value below their starting value.
Sharper than `progress.md`'s bare "a.a. Col_min<N": the convergence of the
density to 1 is at an **exponential rate** (Terras Theorem D, a binomial
argument: the fraction of "divergent" parity vectors decays to 0 because
ln 2/ln 3 > 1/2). The mechanism: each parity vector of length k ↔ a unique
residue class mod 2^k, so the stopping-time event is a finite union of
congruence classes with computable density.

**Robustness sharpening:** the result was found *independently* by at least
three more groups around the same time — **H. Möller 1977** (*J. reine angew.
Math.* 289), **E. Heppner 1978** (*Arch. Math. (Basel)* 31), and
**J.-P. Allouche 1979** (Sém. Théorie des Nombres de Bordeaux). Five
independent proofs of the same density-1 fact is strong evidence the result is
correct and load-bearing-safe (the `progress.md` line
`[collatz-density-terras]` is now primary-source-backed).

## Verification 2: Krasikov-Lagarias 2003 — CONFIRMED

- **I. Krasikov & J. C. Lagarias**, *Bounds for the 3x+1 problem using
  difference inequalities*, **Acta Arithmetica 109**(3), 237–258 (2003),
  DOI [10.4064/aa109-3-4](https://doi.org/10.4064/aa109-3-4).

**Theorem 6.1:** π₁(x) ≥ x^0.84 for all sufficiently large x, where π₁(x) =
#{n ≤ x : the 3n+1 trajectory of n reaches 1} = #{n ≤ x : Col_min(n)=1}.
This matches `progress.md`'s
`#{N≤x: Col_min(N)=1} ≫ x^0.84` `[collatz-kl-count]` exactly.

**Method (the genuine sharpening):** difference inequalities (Krasikov 1989) —
a system Iₖ for functions φₖᵐ(y) on residue classes mod 3ᵏ encoding
trajectory counts. Applegate-Lagarias 1995 had to *truncate* the system
(getting x^0.81 at k=9) to eliminate "advanced" variables. The 2003 paper's
**Theorem 2.2 + Theorem 3.1** show the linear program L_{NT}ᵏ(λ) applies
*directly to the untruncated system*: "advanced" variables are eliminated by a
**back-substitution** that loses no strength. Computation (D. Applegate) at
**k=11, λ=1.7922310** gives γ = log₂(λ) ≈ 0.84175 → **x^0.84**. Exponent
sequence: k=2→0.4365, k=5→0.7335, k=9→0.8168, k=11→0.8417.

**The authors' own conjecture (load-bearing for the obstruction map):**
showing **λₖ → 2 as k → ∞** would yield **π₁(x) ≥ x^{1−ε} for any ε>0** —
the theoretical limit of the difference-inequality method. This is the key
control-step fact: **even the method's theoretical ceiling is "almost all"
(x^{1−ε}), never "all N".** The count bound can get arbitrarily close to
density 1 but, by construction, cannot turn a count `≫ x^{1−ε}` into "every
N reaches 1" — a measure-zero / pointwise exceptional set is invisible to
counting bounds. This is the *same* density→pointwise wall as Terras (and
Tao), now seen from the counting side: **the one-dimensional engine stops at
"almost all" for the count method too**, exactly parallel to Terras's
density-1-but-not-pointwise on the density side.

## Cross-problem echo (the control step)

Both verified results sit on the **resolution side** (they control a
density-1 / large-count set). The **control step** — pointwise / universal —
is the gap, and the Krasikov-Lagarias authors' own x^{1−ε} ceiling makes the
wall *quantitative*: the best-known count method, taken to its theoretical
limit, still leaves a density-0 exceptional set. So:

- The "one-dimensional engine stops" sub-pattern (6-for-6) gets a **second
  Collatz instance**: the Terras density engine stops at "almost all"
  (density 1), and the KL count engine stops at x^{1−ε} — two independent
  engines, same wall, neither reaches pointwise.
- The wall is the deterministic, uncontrolled parity sequence of a given N
  (no pointwise Lyapunov), exactly as `progress.md`'s direction (A-ii) and
  (C) already state. KL's back-substitution is a *resolution* refinement
  (tighter count), not a *control* extension — it does not address the
  pointwise gap.

## Honesty / scope

- Terras 1976 / Everett 1977 CONFIRMED (full citations pinned; exponential-rate
  + independent-discoverer robustness recorded).
- Krasikov-Lagarias 2003 CONFIRMED (Acta Arith. 109(3) 237-258, DOI
  10.4064/aa109-3-4; Theorem 6.1; method + x^{1−ε} theoretical ceiling).
- No proof of Collatz; the density→pointwise leap remains open. The
  verification is the cycle's point: two `progress.md` to-verify items
  (Terras/Everett, KL 2003) are now resolved and primary-source-backed.
- Other to-verify items remain (Conway 1972 FRACTRAN/undecidability primary
  source; Barina 2020 verification bound; the 2024-25 preprints' actual
  claims) — natural attempt-04 targets.
- Outcome: **confirmed** (verification goal met, citations pinned, exponential-
  rate + x^{1−ε}-ceiling sharpenings, second-engine control-step echo),
  **partial** overall (frontier unchanged).

## Next (attempt-04)

Continue resolving the remaining to-verify items: **Conway 1972** (FRACTRAN /
generalized-Collatz undecidability, to confirm the "3n+1 is a weak/contracting
case" framing is faithful to the primary source) and **Barina 2020** (the
2^68 verification bound) are the next most load-bearing. Or status-check the
most-cited 2024-25 preprint (Fathi 2025 / Chang 2026). The rotation continues:
next cross-problem cycle → beals-conjecture (occasional cycle-in) OR back to
birch-swinnerton-dyer (attempt-04) per the bias rule.