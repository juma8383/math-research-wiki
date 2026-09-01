---
type: attempt
problem: collatz_conjecture
attempt: 4
date: 2026-08-24
approach: Verify Conway 1972 (FRACTRAN / generalized-Collatz undecidability) + Kurtz-Simon 2007 (Pi^0_2-completeness) against primary sources, and pin the "3n+1 is a weak/contracting case (mu=3<4=2^2)" framing via the Matthews-Watts/Lagarias criterion
outcome: confirmed
tags: [verification, primary-source, undecidability, conway, kurtz-simon, fractran, contracting-criterion, cross-problem]
---

# Attempt 04 — Verify Conway 1972 undecidability + the contracting-case framing

Cycle-16 Continue on Collatz (cross-problem loop, second pass; green zone
23.5% session / 56.5% weekly, 0 subagents). Attempt-03's `Next` named
**Conway 1972** (FRACTRAN / generalized-Collatz undecidability) — to
confirm the `progress.md` framing "3n+1 is a weak/contracting case
($\mu=3<4=2^2$)" is faithful to the primary source — and Barina 2020
($2^{68}$) as the next most load-bearing to-verify items. This cycle
verifies the **undecidability** thread (Conway 1972 + Kurtz-Simon 2007 +
Conway 2013) and the **contracting-criterion** classification (Matthews-
Watts / Lagarias). Same discipline that caught the BSD Kim-2022 "bounds
rank $\le1$ only" update and the Hodge integral-Hodge two-sources-of-failure
sharpening.

## Verification 1: Conway 1972 — generalized Collatz is UNDECIDABLE (CONFIRMED)

**J. H. Conway**, *Unpredictable Iterations* (1972), Proc. 1972 Number
Theory Conf., Univ. of Colorado; archived at
[gwern.net/doc/cs/computable/1972-conway.pdf](https://gwern.net/doc/cs/computable/1972-conway.pdf).

- **Generalized Collatz functions** $g(n)=a_i n+b_i$ for $n\equiv i\pmod p$,
  with rational $a_i,b_i$ chosen so $g(n)$ is always integral.
- **Main Theorem:** for any computable function $f$ there is such a $g$
  with $g(n)/n$ periodic (rational values) and $g^k(2^n)=2^{f(n)}$ for the
  minimal $k$ with $g^k(2^n)$ a power of $2$.
- **Corollary:** there is **no algorithm** that, given such a $g$ and $n$,
  decides whether $g^k(n)=1$ for some $k$ — the generalized "does the orbit
  hit $1$" problem is **undecidable**.
- Mechanism: **Minsky machines** (counter machines) → **vector games** →
  **rational games** (later repackaged as **FRACTRAN** in 1987, a universal
  fraction-list programming language; Conway, *FRACTRAN: A Simple Universal
  Programming Language for Arithmetic*, in Open Problems in Communication &
  Computation, Springer 1987).

## Verification 2: Kurtz-Simon 2007 — GCP is $\Pi^0_2$-complete (CONFIRMED)

**S. A. Kurtz & J. Simon**, *The Undecidability of the Generalized Collatz
Problem*, TAMC 2007, **LNCS 4484**, 542–553.

- Strengthens Conway: the **GCP** — deciding whether *every* forward orbit
  of a generalized Collatz function contains $1$ — is **$\Pi^0_2$-complete**.
- The $\Pi^0_2$ level reflects the logical shape: $\forall n\,\exists k\;
  T^k(n)=1$ — a $\forall\exists$ statement, the same shape as the specific
  $3n+1$ conjecture. So the *specific* conjecture is a $\Pi^0_2$ statement
  about one fixed $T$; the *general* problem (uniform over all $T$) is
  $\Pi^0_2$-**complete**, hence undecidable.

## Verification 3: the contracting-case framing — CONFIRMED (Matthews-Watts / Lagarias)

`progress.md`'s "3n+1 is a weak/contracting case ($\mu=3<4=2^2$)" is
faithful to the standard classification, now pinned:

- **Framework (Lagarias 1985 survey / Matthews-Watts):** a generalized
  Collatz map of **relatively prime type**
  $f(x)=\frac{a_i x+b_i}{d}$ for $x\equiv i\pmod d$, with
  $\gcd(a_0\cdots a_{d-1},d)=1$, is classified by $|\prod a_i|$ vs $d^d$:
  - $|\prod a_i|<d^d$ → **contracting** (trajectories *expected* to cycle);
  - $|\prod a_i|>d^d$ → **expanding** (almost all *expected* to diverge);
  - equality cannot occur for relatively-prime-type maps.
- **Shortcut (accelerated/Terras) $3n+1$ map:**
  $T(x)=x/2$ if even, $(3x+1)/2$ if odd. Here $d=2$, $(a_0,a_1)=(1,3)$:
  $\prod a_i=3<4=2^2=d^d$, geometric mean $(\prod a_i/d^d)^{1/d}=(3/4)^{1/2}\approx0.866<1$.
  So $3n+1$ is squarely in the **contracting regime** — the regime where
  convergence is *expected*. This is the precise content of "weak/contracting
  case."
- **Honesty sharpening (load-bearing):** the Matthews-Watts classification
  is a **conjectural heuristic, not a theorem** — "$\prod a_i<d^d$
  $\Rightarrow$ all trajectories cycle" is itself unproved and, for the
  specific $3n+1$ instance, IS the Collatz conjecture. Conway's own
  **amusical permutation** $\mu$ ($2k\mapsto3k$, $4k{+}1\mapsto3k{+}1$,
  $4k{-}1\mapsto3k{-}1$; *Amer. Math. Monthly* **120**(3), 2013, "On
  Unsettleable Arithmetical Problems") sits in the contracting regime by
  the same criterion ($3^4{=}81<256{=}4^4$) yet is conjectured to have
  **infinite** orbits ("probviously" unsettleable). So the criterion does
  NOT settle convergence even within the contracting regime — it only says
  where the heuristic points. $3n+1$ is the prototypical open instance of
  "contracting regime, convergence conjectured but unproved."

## What this sharpens for the obstruction map

- `progress.md`'s "Conway 1972: generalized Collatz maps universal →
  halting undecidable in general; 3n+1 is a weak/contracting case
  ($\mu=3<4=2^2$)" is **CONFIRMED and primary-source-backed** (Conway 1972
  for undecidability; Matthews-Watts/Lagarias for the contracting
  criterion), with the crucial honesty nuance that the criterion is
  **heuristic**, not theorem.
- **The Kurtz-Simon $\Pi^0_2$-completeness is the new load-bearing fact:**
  any argument that works **uniformly** over the whole generalized-Collatz
  family cannot prove $3n+1$ (the general problem is undecidable). A proof
  for $3n+1$ specifically **must exploit the concrete contracting
  structure** (the exact multipliers $1,3$, the $3<4$ margin, the
  $3/4<1$ geometric mean) — a *per-instance*, not *uniform*, argument. This
  is the **control-step** spine made sharp: the *resolution* (a general
  decision procedure) is impossible (undecidable); the *control* (per-
  instance, using the contracting structure to get pointwise convergence)
  is the only route and is exactly the open piece.
- **Cross-problem echo (6-for-6, undecidability as the meta-control-wall):**
  the generalized problem being $\Pi^0_2$-complete is the hardest possible
  "no uniform method exists" wall — the Collatz analog of Beal's
  reduction-to-finite-curves (a uniform Diophantine method is unavailable)
  and of NS/BSD/YM/Hodge where each known engine controls only its slice.
  Here the wall is *logical* (undecidability) rather than *analytic*, but
  it plays the same role: it forces any attack onto the specific structure.
  The "one-dimensional engine stops" sub-pattern gets a **logical** edge:
  the uniform engine (works for all generalized $T$) is provably stopped by
  undecidability; the instance-specific engine (for $3n+1$) is the open
  contracting-structure control.

## Honesty / scope

- Conway 1972 (undecidability of generalized Collatz), Kurtz-Simon 2007
  ($\Pi^0_2$-complete GCP, LNCS 4484), and Conway 2013 (amusical
  permutation) CONFIRMED against primary sources; the contracting-criterion
  framing ($\prod a_i=3<4=d^d$, geometric mean $(3/4)^{1/2}<1$) confirmed
  via Matthews-Watts/Lagarias.
- **Key honesty flag:** the Matthews-Watts contracting criterion is a
  **conjectural heuristic**, not a theorem — recorded to avoid
  overclaiming that "contracting ⇒ convergent" is known. The amusical
  permutation is the cautionary counter-expectation within the contracting
  regime.
- Conway's undecidability is for **generalized** maps, NOT the specific
  $3n+1$ — `progress.md`'s existing honesty check stands and is sharpened:
  the $\Pi^0_2$-completeness means the *uniform* problem is undecidable,
  but the *specific* $3n+1$ (a single fixed $\Pi^0_2$ statement) may well
  be provable; its decidability/convergence is open, not known-undecidable.
- No proof of Collatz; the density→pointwise leap and the cycle-exclusion
  wall remain open. The verification is the cycle's point: two
  `progress.md` to-verify items (Conway 1972, the contracting framing) are
  now resolved and primary-source-backed, with the $\Pi^0_2$-completeness
  sharpening added.
- Remaining to-verify (attempt-05 targets): **Barina 2020** ($2^{68}$
  verification bound, the computational-evidence base); the **2024-25
  preprints' actual claims** (Fathi 2025 / Nwankpa 2025 / Chang 2026).
- Outcome: **confirmed** (Conway/Kurtz-Simon/contracting-framing verified +
  $\Pi^0_2$-completeness sharpening + heuristic-not-theorem honesty flag +
  control-step/undecidability echo), **partial** overall (frontier
  unchanged).

## Next (attempt-05)

Continue resolving the remaining to-verify items: **Barina 2020** (the
$2^{68}$ computational verification bound, the evidence base line in the
exact-frontier table) and the **2024-25 preprints** (status-check Fathi
2025 / Chang 2026 against their actual claims) are the next most
load-bearing. Or, per the bias rule (five problems that had only
attempt-01 now all advanced to $\ge2$), the rotation could cycle in
**beals-conjecture** occasionally next. The rotation continues: next
cross-problem cycle → beals-conjecture (occasional cycle-in) OR
birch-swinnerton-dyer (attempt-05) per the rotation order.