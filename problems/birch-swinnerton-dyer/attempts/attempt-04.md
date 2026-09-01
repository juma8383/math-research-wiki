---
type: attempt
problem: birch_swinnerton_dyer
attempt: 4
date: 2026-08-24
approach: Deepen direction (A) — survey the higher-rank Gross-Zagier / Euler-system landscape (Kim 2022, Wei Zhang survey) to test the control-step premise that the rank->=2 Selmer bound is missing
outcome: partial
tags: [deepening, direction-A, higher-gross-zagier, kolyvagin-system, kurihara-numbers, cross-problem]
---

# Attempt 04 — Deepen direction (A): the higher-rank GZ / Kolyvagin-system landscape

Cycle-12 Continue on BSD (cross-problem loop, second pass; orange zone
82.7% session / 51.3% weekly, 0 subagents). Attempts 02-03 resolved every
to-verify item (rank-<=1 base, p-converse, refined p-part, parity). This
cycle is a *deepening* move, not a verification: it tests the load-bearing
premise of direction (A) — the control-step obstruction — against the
current higher-rank Gross-Zagier / Euler-system literature. The premise
(progress.md, attempt-02): "needs BOTH (i) a supply of r_an independent
points via *higher-derivative* Gross-Zagier (GZ gives only the 1st
derivative), AND (ii) a multi-point / multi-variable *Kolyvagin system*
bounding a rank-r Selmer group to size r_an — the existing engine is
single-Heegner-point-shaped and bounds rank <=1 only."

## Finding: the premise is HALF confirmed, HALF outdated — and a sharper wall appears

### (A-i) higher-L-derivative GZ — CONFIRMED absent (number-field case)

The number-field higher-rank Gross-Zagier via higher *L*-derivatives does
**not** exist beyond the 1st derivative. Wei Zhang's survey (*BSD and Heegner
points*, Current Developments in Mathematics 2013) and Kim 2022 both state
that the only known higher-rank GZ is **Yun-Zhang's work, and it is for the
*function-field* case**. In the number-field case "when the rank is larger
than one, the situation becomes extremely puzzled" (Kim, intro). So the
"supply of r_an independent points via higher-derivative GZ" remains
unavailable — **the (A-i) wall holds.** (Yuan-Zhang-Zhang's generalized GZ
formula, Thm 3.2 of the survey, is still the *first*-derivative formula over
totally real fields; Qiu 2019 extends it to function fields but still rank 1.)

### (A-ii) multi-point Kolyvagin system — PARTIALLY SUPERSEDED (the sharpening)

progress.md's "single-Heegner-point-shaped, bounds rank <=1 only" is now
**outdated**. Chan-Ho Kim, *A higher Gross-Zagier formula and the structure
of Selmer groups*, arXiv:2203.12161 (2022), gives a **"higher Gross-Zagier
formula" (Theorem 2.3)** that determines the **full Selmer group structure
at arbitrary rank**, with **no low-rank assumption**:

  ord(kappa^Heeg) + 1 = max{ ord delta(E), ord delta(E^K) }
                     = max{ cork Sel(Q, E[p^inf]), cork Sel(Q, E^K[p^inf]) }

where kappa^Heeg is the Heegner-point **Kolyvagin system** and delta are
**Kurihara numbers** (Kolyvagin derivatives of Mazur-Tate elements). When
the two Selmer coranks differ by 1 this recovers the classical GZ formula;
in general it gives the full module structure
$(Q_p/Z_p)^{\oplus r} \oplus \bigoplus_i (Z/p^{a_i}Z)^{\oplus 2}$.

Crucially, the "higher" derivative here is of **Mazur-Tate elements**, NOT of
the Rankin-Selberg $L$-function — "completely different from the relative
trace formula approach." So the engine that bounds the Selmer group at
arbitrary rank **does exist** — it is the Heegner Kolyvagin system (built
from a single Heegner point's Kolyvagin derivatives), and it captures the
full structure, not just rank <=1.

**The condition:** this is *conditional on Kolyvagin's Conjecture* — the
nontriviality of kappa^Heeg (Kolyvagin Conjecture A). Wei Zhang proved this
for a large class of elliptic curves (using the Skinner-Urban Iwasawa main
conjecture); Kim's Thm 2.1 ties the nontriviality to the anticyclotomic /
Heegner-point main conjecture at the augmentation ideal. So (A-ii) is no
longer "doesn't exist" — it is "exists and bounds arbitrary rank, *given
the main conjecture / Kolyvagin nontriviality*."

### The NEW wall (the genuine deepening of the obstruction)

Two refinements relocate the control-step obstruction more precisely:

1. **It is a *relative*, not *absolute*, bound.** Kim's formula bounds
   max{cork Sel(E), cork Sel(E^K)} — the Selmer corank of E *or its
   quadratic twist* E^K — not r_alg(E) alone. To extract r_alg(E)=r_an(E)
   one needs the *other* Selmer corank controlled independently. This is the
   descendant of the rank-<=1 trick (where the twist has the opposite root
   number, so one of the two has corank 0 by parity), now seen at arbitrary
   rank: the Kolyvagin system pins the *pair* {E, E^K}, and lifting to a
   single curve's rank needs an extra input. So the control step is not
   "no arbitrary-rank bound" but "**no arbitrary-rank *absolute* (non-paired)
   bound**."

2. **Cyclotomic-vs-anticyclotomic disjointness.** Kim's intro (and the
   survey) flag the structural barrier: Kato's Euler system varies
   *cyclotically*, the Heegner-point Euler system varies *anticyclotically*,
   and the two have "**disjoint field variations except the base imaginary
   quadratic field**," so beyond the bottom classes there is no known way to
   compare / combine them into a single rank->=2 argument. This is the
   one-dimensional-engine-stops sub-pattern in BSD made concrete: **two
   one-directional engines (cyclotomic Kato, anticyclotomic Heegner) each
   control their slice, and the comparison needed for rank->=2 is exactly
   where they stop talking to each other.** Bipartite Euler systems
   (Howard; Kim Thm 2.5) extend the Heegner side to the root-number +1
   (Waldspurger) setting, behaving "like Kolyvagin systems rather than
   Euler systems" — but still anticyclotomic-flavored; the bridge to the
   cyclotomic/Kato side is the open comparison.

## What this changes in the obstruction map

- **Direction (A) refined (not refuted):** the obstruction is no longer
  "no rank->=2 Selmer bound exists" (Kim's Kolyvagin system gives one,
  conditionally); it is "(i) no number-field higher-L-derivative GZ (no
  independent-point *supply* at rank r), AND (ii') the existing Selmer
  bound is *relative* (paired E/E^K) and *conditional* (main conjecture),
  AND (iii) the cyclotomic-anticyclotomic comparison that would make it
  *absolute* and *unconditional* is blocked by field-variation
  disjointness." Three named sub-walls, each a control step.
- **Kolyvagin Conjectures 3.32-3.35 (Stein),** the named unproven target
  in progress.md, are now **partially subsumed** by Kim-Wei Zhang
  (nontriviality proved for a large class), but the *full* conjecture
  (all curves, unconditional) remains open — so the target shrinks but
  does not vanish.
- **6-for-6 / one-dimensional-engine-stops:** BSD's instance gets a second
  engine named. Previously: "one Heegner point (rank <=1)." Now: two engines
  — cyclotomic (Kato) and anticyclotomic (Heegner) — each one-directional,
  and the rank->=2 control step is exactly the comparison where the two
  one-dimensional engines fail to compose. This parallels Collatz's
  "two engines (Terras density, KL count) stop at almost-all" (attempt-03)
  and NS's "2D/3D Serrin index" — the *second* engine does not reach the
  universal claim.

## Honesty / scope

- This is a *deepening* move, not a primary-source verification of a single
  theorem; the load-bearing claims (Kim 2022 arXiv:2203.12161 Thm 2.3/2.1;
  Wei Zhang 2013 survey + Kolyvagin-conjecture proof via Skinner-Urban;
  Yun-Zhang = function-field only; Kurihara-number method) are from the
  search summary and **flagged to-verify** against the arXiv PDF / survey
  before load-bearing reuse. The structural conclusion (relative +
  conditional bound; cyclotomic-anticyclotomic disjointness) is consistent
  across both sources.
- No proof of BSD; the rank->=2 wall is sharpened (three sub-walls) not
  broken. Refined-BSD (direction C) untouched this cycle.
- Outcome: **partial** (obstruction map sharpened, direction (A) refined
  with a named newer mechanism, two-engine echo recorded; no frontier
  change; Kim/Wei-Zhang claims to-verify).

## Next (attempt-05)

Verify Kim 2022 arXiv:2203.12161 Thm 2.3 against the arXiv PDF (the exact
max{cork Sel} statement + the Kolyvagin-conjecture condition), and the
Yun-Zhang "function-field only" boundary, to upgrade this deepening to
confirmed. Or pivot to direction (C) / refined-BSD (Bullach-Honnor 2025,
equivariant Tamagawa / Mazur-Tate) as the second front. The rotation
continues: next cross-problem cycle -> navier-stokes (attempt-04) per the
rotation, OR beals (occasional cycle-in).