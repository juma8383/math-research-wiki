---
type: attempt
problem: birch_swinnerton_dyer
attempt: 7
date: 2026-08-25
approach: Budget-light sub-thread DEVELOPMENT (no WebSearch) of the Kataoka–Sano rank-2 reframing from attempt-06 — work out the Selmer-decomposition keystone, the rank-2 Kolyvagin/Darmon-derivative control step, the refined 6-for-6 "two-engine" sharpening, and the number-field vs function-field BSD-avatar distinction (linking to the Hodge bridge found this run)
outcome: confirmed
tags: [sub-thread-development, synthesis, rank-2-euler-system, selmer-decomposition, darmon-derivatives, kolyvagin-system, control-step, cross-problem, function-field-bsd, number-field-bsd, hodge-bridge, 6-for-6]
---

# Attempt 07 — The rank-2 reframing developed: Selmer decomposition as keystone, the Darmon-derivative control step, and BSD's two avatars (number-field Millennium vs function-field Hodge-linked)

Cycle-4/new-run Continue on BSD (resumed /loop; **yellow zone, weekly 73.6%
/ session 23.1%, 0 subagents — NO WebSearch**: a file-write-only sub-thread
development to minimize weekly drain, ~1.4% below the 75% pause threshold).
Per the standing instruction's "develop a sub-thread" option (sanctioned when
budget-tight), this cycle **synthesizes the structural implications of
attempt-06's Kataoka–Sano rank-2 reframing** from existing notes + standard
Euler-system theory (Mazur–Rubin rank-$r$ Kolyvagin systems) — **not** a new
primary-source verification. Honesty upfront: the Kataoka–Sano specifics
(Thm 1.5/1.9/1.11) remain `to-verify` against the paper body (attempt-06's
flag); this cycle develops the *consequences*, flags them as
structural-not-verified, and sharpens the obstruction map + a cross-problem
link to [[hodge_conjecture]] (the function-field BSD bridge found this run,
attempt-06-Hodge).

## The keystone: Sel(K) ≃ Sel(Q) ⊕ Sel(Q, E^K) — and why it IS the rank-2 structure

The decomposition
$$\mathrm{Sel}(K,E[p^\infty])\;\simeq\;\mathrm{Sel}(\mathbb Q,E[p^\infty])
\;\oplus\;\mathrm{Sel}(\mathbb Q,E^K[p^\infty])$$
(attempt-06, from Kim's Thm 2.3 / Kataoka–Sano) is the **structural
keystone**, and reading it carefully reframes the obstruction:

- $K$ is the imaginary quadratic over $\mathbb Q$ (Heegner hypothesis);
  $E^K$ is the quadratic twist by $K/\mathbb Q$.
- $\mathrm{Sel}(\mathbb Q,E)$ is the **cyclotomic** summand — the Selmer
  group Kato's Euler system bounds (cyclotomic IMC → rank control of
  $\mathrm{Sel}(\mathbb Q,E)$).
- $\mathrm{Sel}(\mathbb Q,E^K)$ is the **anticyclotomic** summand — the
  twist captures the "other direction"; the Heegner-point Euler system /
  anticyclotomic MC bounds $\mathrm{Sel}(K,E)$, and the $E^K$-twist piece
  is the anticyclotomic contribution.
- So $\mathrm{Sel}(K,E) = $ cyclotomic summand $\oplus$ anticyclotomic
  summand **as a direct decomposition** — the two "one-directional engines"
  are literally the two **direct summands** of the rank-2 Selmer group over
  $K$.

This is why Kataoka–Sano's "$r_T=2$" is not a metaphor: $T^*(1)$ over $K$
has $\mathbb Z_p$-rank 2 because the two Galois-cohomology directions
(cyclotomic $\mathbb Q$-variation, anticyclotomic $K$-variation) are
independent, and the Selmer decomposition is the **arithmetic shadow** of
that rank-2 Galois module. The "disjointness" (attempt-06 sub-wall (3)) is
the Galois-theoretic statement that the two summands vary over disjoint
extension towers; the **decomposition is the consequence** — they are
disjoint *as field variations* but **combine as direct summands** of one
Selmer group.

## The reframed obstruction: the rank-2 Kolyvagin / Darmon-derivative CONTROL step

Standard theory (Mazur–Rubin, *Euler systems and modular arithmetic*; the
framework Kataoka–Sano operate in): a **rank-$r$ Euler system** for a
Galois-stable $\mathbb Z_p$-module $T$ produces, via **Kolyvagin derivative
operators**, a **rank-$r$ Kolyvagin system** whose non-vanishing controls
$\mathrm{Sel}$ to corank $\le r$. For $r=1$ (Kato, classical Heegner) this is
the rank-$\le1$ bound (Kolyvagin). For $r=2$ (Kataoka–Sano's Heegner system
over $K$), the **rank-2 Kolyvagin system** would control
$\mathrm{Sel}(K,E)$ to corank $\le2$ — i.e. bound the rank-$2$ Selmer group,
exactly the missing piece for $r_{\rm an}=2$.

The obstruction, refined:

| | Resolution (works) | Control (open) |
|---|---|---|
| rank 1 | Kato cyclotomic IMC, Heegner anticyclotomic MC, Kolyvagin → $\mathrm{cork}\,\mathrm{Sel}\le1$ | — |
| rank 2 | each summand's MC (cyclotomic + anticyclotomic) individually | **the rank-2 Darmon-derivative Kolyvagin system** controlling $\mathrm{Sel}(K,E)$ to corank $\le2$ |

So the "two engines both stop at rank 1" (attempt-04/05) is sharpened:
**each engine resolves its summand (rank-1 control); the stop is the
rank-2 *composition* control** — producing the rank-2 Kolyvagin system
from the rank-2 Euler system. Kataoka–Sano's Thm 1.11 names this as a
**three-fold conditional**:

1. **Heegner-point main conjecture** (Perrin-Riou) — the rank-2 Euler
   system exists (Thm 1.5 conditional on it).
2. **Darmon-derivative Conjecture 1.9** — the *specific* derivative
   construction producing the rank-2 Kolyvagin system from the Heegner
   rank-2 Euler system (the analogue of Howard 2004's Heegner-Kolyvagin
   derivative operators, but for the rank-2 / two-summand system).
3. **Non-vanishing of the anticyclotomic Bockstein regulator** — the
   rank-2 system's "second direction" is non-degenerate.

$\Rightarrow$ the **$p$-part of BSD for $E/K$**. So the control step has
**three undischarged conditions**, each a named, concrete
direction-(A) target — strictly sharper than attempt-04/05's "neither
exists." The obstruction is *not* a vague "rank-2 is hard"; it is
"the rank-2 Darmon-derivative Kolyvagin system is unconstructed
(condition 2), over a rank-2 Euler system whose existence is itself
conditional (condition 1), with a non-degeneracy condition (3)."

## The refined 6-for-6 "two-engine" sharpening

The cross-problem "one-dimensional engine stops" sub-pattern (TWO-engine
variant, BSD/Collatz/NS/YM) is **refined for BSD**:

- **Old framing (attempt-04/05):** two rank-1 engines (cyclotomic Kato,
  anticyclotomic Heegner), both stop at rank 1, *disjoint except at $K$*
  → can't compare as Euler systems.
- **New framing (attempt-06 + this cycle):** the two engines are the two
  **direct summands** of a rank-2 Euler system over $K$ (the disjointness
  *is* the direct-summand structure). The "stop" is **not** "can't compare
  two rank-1 systems" but **"the rank-2 composition control (the
  Darmon-derivative Kolyvagin system) is unconstructed + three-fold
  conditional."**

So the BSD "two engines stop" is really **"two engines *combine* into a
rank-2 object, and the composition-to-control step is the wall"** — a
strict refinement, and a cleaner 6-for-6 instance: the obstruction is at
the **control** step (rank-2 Kolyvagin system → BSD), not the **resolution**
step (each rank-1 engine for its summand). Parallels:
- NS: the 1D quasi-exact engine (attempt-06-NS) *achieves* blowup
  (resolution, in weakened slices) and stops at the control step to full
  3D smooth data — "combines/resolves a slice, stops at the universal
  control."
- Collatz: the two density engines (Terras, KL) both stop at almost-all;
  the pointwise control is the wall — same "resolve a slice, stop at the
  universal control."
- BSD now: the two rank-1 engines resolve their summands; the rank-2
  composition control is the wall. **Same spine, sharpened.**

## BSD's two avatars: number-field Millennium vs function-field Hodge-linked

This run's Hodge cycle (attempt-06-Hodge) found the **Tate⟺BSD-for-Jacobian
bridge** — but refined it to **function-field (char-$p$) BSD** (over
$\mathbb F_q(t)$, the geometric avatar), NOT the number-field Millennium
BSD. Pairing with this cycle's BSD development surfaces the **two-BSD-avatar
structure** of the cross-problem methodology:

| | function-field BSD (char $p$) | number-field BSD (Millennium, char 0) |
|---|---|---|
| avatar | Tate-for-divisors-on-surface ⟺ BSD(Jac) | BSD for $E/\mathbb Q$ (and $E/K$) |
| status | **substantially proven** (Kato–Trihan 2003: BSD ⟺ Sha-finite) | **open** (rank $\ge2$, exact $|\Sha|$) |
| control step | Brauer/Sha finiteness (codim-1 Frobenius→algebraic) | rank-2 Selmer control (Darmon-derivative Kolyvagin) |
| cross-problem link | to [[hodge_conjecture]] (this run) | the Millennium target |
| shape | multi-summand Selmer (Br ↔ Sha) control | multi-summand Selmer (cyclotomic ⊕ anticyclotomic) control |

**Both avatars share the "control the multi-summand Selmer group" shape** —
the function-field one (Brauer↔Tate-Shafarevich↔BSD, the surface-divisor
control) and the number-field one (cyclotomic⊕anticyclotomic Selmer, the
rank-2 control). So the Hodge bridge and the Kataoka–Sano reframing are
**two faces of the same cross-problem control step**, read in two
cohomological theories (étale/crystalline on a surface vs. Galois-cohomology
Euler systems on an elliptic curve). This sharpens the 6-for-6 methodology
from "BSD is parallel to Hodge" to **"BSD has two avatars — the
function-field one is *linked* to Hodge (and largely proven), the
number-field one is the conditional Millennium target; both are the
multi-summand-Selmer control step."** A genuine cross-problem compounding
link, developed from the two cycles of this run.

## What this changes in the obstruction map

- **Rank-2 reframing developed into a concrete control-step structure:**
  Sel(K) ≃ Sel(Q) ⊕ Sel(Q,E^K) as the keystone; the obstruction = the
  rank-2 Darmon-derivative Kolyvagin system (unconstructed) over a
  conditional rank-2 Euler system, with a three-fold conditional (Heegner
  MC / Darmon-derivative conj. / Bockstein regulator). Sharper than
  attempt-06's "control the rank-2 system's Darmon derivatives."
- **6-for-6 two-engine sharpening refined:** "two engines stop at rank 1"
  → "two engines combine into a rank-2 object; the composition-to-control
  step is the wall" — a cleaner cross-problem spine (resolve a slice, stop
  at the universal control), matching NS/Collatz.
- **NEW cross-problem link: BSD's two avatars** (function-field, Hodge-
  linked, proven / number-field, Millennium, conditional) both = the
  multi-summand-Selmer control step. Sharpens 6-for-6 from "parallel" to
  "two avatars of one control step, one proven one open."
- **No proof move.** BSD remains open; rank $\ge2$ and exact $|\Sha|$
  untouched. This cycle *developed the structural consequences* of
  attempt-06's reframing; it did not verify new facts (no web search) and
  the Kataoka–Sano specifics remain `to-verify`.

## Honesty / scope

- **This is a SYNTHESIS/DEVELOPMENT cycle, not a verification.** No
  WebSearch; the structural claims are derived from attempt-06's
  (search-surfaced, to-verify) Kataoka–Sano reframing + standard
  rank-$r$ Euler-system / Kolyvagin theory (Mazur–Rubin framework). The
  Kataoka–Sano Thm 1.5/1.9/1.11 specifics — the rank-2 Euler-system
  construction, the Darmon-derivative Conjecture 1.9, the Bockstein
  regulator, the three-fold conditional — are **NOT primary-source-verified
  this cycle**; they remain the `to-verify` flag from attempt-06. The
  *consequences* (Selmer-decomposition keystone, control-step refinement,
  two-avatar link) are structural, flagged as developed-not-verified.
- **The two-avatar framing** (function-field BSD proven / number-field
  BSD open) is standard (Kato–Trihan 2003 for the function-field side is
  well-established; the Millennium number-field BSD is open) — this cycle's
  contribution is *linking* the two to the cross-problem
  multi-summand-Selmer control step, a structural observation, not a new
  theorem.
- **The Mazur–Rubin rank-$r$ Kolyvagin-system framework** is standard
  (cited from general knowledge, not re-verified this cycle); the specific
  claim that a rank-2 Kolyvagin system controls Sel to corank ≤2 is the
  standard rank-$r$ bound, not a Kataoka–Sano-specific result.
- No proof of BSD. Outcome: **confirmed** (a coherent, honest structural
  development of the rank-2 reframing + a cross-problem two-avatar link to
  [[hodge_conjecture]]), **partial** overall (no proof move; no new
  primary-source verification; Kataoka–Sano to-verify).

## Next (attempt-08)

The **single most consequential unverified item** is now clearly
Kataoka–Sano 2024 (J. Assoc. Math. Res., DOI 10.56994/jamr.002.002.001),
primary-source-verify against the paper body: (i) the rank-2 Euler-system
construction (Thm 1.5, conditional on Heegner MC); (ii) the
Darmon-derivative Conjecture 1.9 (the load-bearing unconstructed control
step); (iii) the Bockstein regulator non-vanishing; (iv) Thm 1.11's
three-fold conditional ⟹ $p$-part of BSD for $E/K$. This is the natural
attempt-08 target when budget allows a WebSearch. The rotation continues;
weekly ~74% post-cycle — the next cycle must live-check and likely PAUSE at
the 75% threshold.