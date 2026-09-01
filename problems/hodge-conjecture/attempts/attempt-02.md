---
type: attempt
problem: hodge_conjecture
attempt: 2
date: 2026-08-24
approach: Primary-source verification of the two most load-bearing facts ([hodge-statement] Deligne Clay write-up; [hodge-cattani-deligne-kaplan] Hodge-locus-algebraic) against the Clay hodge.pdf and JAMS 1995; then deepen direction (A) — the motive/standard-conjecture reduction, sharpened by Deligne's own §4/§5
outcome: confirmed
tags: [verification, primary-source, deligne-clay, cattani-deligne-kaplan, standard-conjectures, motive-reduction, cross-problem]
---

# Attempt 02 — Verify Deligne statement + CDK, deepen direction (A)

Cycle 4 of the math-work loop. Hodge had only attempt-01; its to-verify list
named "Deligne's Clay write-up (hodge.pdf); Lefschetz (1,1) via exponential
sequence; hard Lefschetz reduction; Atiyah–Hirzebruch & Kollár; Cattani–
Deligne–Kaplan; Charles–Markman; the 2024–25 preprints." This cycle verifies
the two most load-bearing + direction-(A)-adjacent: the official Deligne
statement and the Cattani–Deligne–Kaplan theorem, then deepens direction (A)
from what Deligne's own write-up says.

## [hodge-statement] CONFIRMED (primary source: Deligne, hodge.pdf)

Verified against Pierre Deligne's official problem description in *The
Millennium Prize Problems* (Clay Mathematics Institute, 2006, pp. 45–53),
served as `hodge.pdf` (https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf;
mirror https://publications.ias.edu/sites/default/files/hodge.pdf). The exact
statement (§1):

> **On a projective non-singular algebraic variety over $\mathbb C$, any Hodge
> class is a rational linear combination of classes $\mathrm{cl}(Z)$ of algebraic
> cycles.**

with Hodge class $= H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)=H^{2p}(X,\mathbb Q)\cap F^p
\subset H^{2p}(X,\mathbb C)$, and $\mathrm{cl}(Z)\in H^{2p}(X,\mathbb Z)$ the
cohomology class of a closed analytic subspace of codimension $p$ (viewed via
its integration current). Points confirmed against the primary text:

1. **Rational, not integral (Remark vi).** Hodge's original integral form fails;
   the conjecture holds only after tensoring with $\mathbb Q$. Atiyah–Hirzebruch
   (Remark iv) is the counterexample. This **confirms the "integral version
   FALSE" wrinkle** recorded in attempt-01/progress.md — it is in Deligne's own
   write-up, not just the survey.

2. **Known for $H^2$ (Kodaira–Spencer).** Via the exponential exact sequence and
   line bundles. **Confirms Lefschetz $(1,1)$** as the $p=1$ proven case and the
   "bridge works for divisors" framing — primary-source-verified now, not just
   survey-level. `[hodge-lefschetz-1-1]` corroborated.

3. **Algebraicity is essential.** Projective, not merely Kähler — consistent
   with the Zucker-tori evidence `[hodge-algebraicity-essential]`.

`[hodge-statement]` and the Lefschetz-$(1,1)$ / integral-fails sub-facts move
from `to-verify` to **CONFIRMED**.

## Direction (A) deepened — from Deligne's own §4 and §5 (the sharp find)

The verification's biggest payoff is *not* the statement itself but what
Deligne writes immediately after it. This directly reshapes direction (A):

- **§4, Example 1:** HC remains open **even for the Künneth components of the
  diagonal** $\Delta\subset X\times X$. These being algebraic is **standard
  conjecture C** (Grothendieck).
- **§4, Example 2:** HC remains open **even for the inverse Lefschetz
  operator** $\Lambda$. Its algebraicity is **standard conjecture B**
  (Grothendieck).

So the standard conjectures B and C are **open special cases of HC itself**,
not merely a pathway to a reduction. This is sharper than attempt-01, which
framed direction (A) as "the motive/standard-conjecture reduction … the closest
analog of Beal's reduction-to-finite-curves step." The primary-source
correction: **direction (A) is literally "prove special cases of HC" — and even
those special cases (Künneth components, inverse Lefschetz) are open.** The
"reduction" is to *specific Hodge classes* (the diagonal's Künneth components,
$\Lambda$), exactly the structural analog of Beal's reduction-to-specific-curves
— but the reduction target is itself unproven.

- **§5 (motives):** IF the Künneth components and inverse Lefschetz were
  algebraic, Grothendieck's motives over $\mathbb C$ would form a **semi-simple
  abelian category**, and the **full Hodge conjecture would be equivalent to a
  natural functor from motives to Hodge structures being fully faithful.**
  This confirms the motive-reduction framing in attempt-01, now
  primary-source-pinned: HC ⇔ fully-faithful motives→Hodge-structures (given B
  and C). The "control" content: B and C give the Tannakian/semi-simple
  framework in which HC becomes a clean fully-faithfulness statement; without
  them the framework itself is missing — the same "control step, not resolution
  step" shape. The resolution tools (Chow groups, cycle class map, Hodge
  decomposition) all work; the gap is the *control* (=algebraicity) of two
  specific classes (Künneth components, $\Lambda$) that would unlock the
  motive category.

- **§6 (substitutes):** On abelian varieties, Hodge classes are **absolutely
  Hodge** (Deligne) and **motivated** (André) — sufficient for some
  applications but not for reduction modulo $p$. Confirms the
  `[hodge-absolute-hodge]` evidence layer and its limit (direction (C)).

**Net sharpening of direction (A):** it is a two-stage control problem —
(i) prove B and C (algebraicity of inverse Lefschetz + Künneth components),
which are *open special cases of HC*; (ii) then HC reduces to a
fully-faithful motives→Hodge-structures functor. Stage (i) is the
control/reduction step where the engine stops: the Picard-variety
(exponential-sequence) engine proves $p=1$ but has no analogue for the
diagonal's Künneth components or $\Lambda$. This is the Hodge instance of the
6-for-6 "one-dimensional engine stops" sub-pattern, now pinned to two named
classes from Deligne's own text.

## [hodge-cattani-deligne-kaplan] CONFIRMED + sharpened (primary: JAMS 1995)

Verified against Cattani–Deligne–Kaplan, *"On the Locus of Hodge Classes,"*
**J. Amer. Math. Soc.** 8(2), 483–506 (1995), DOI 10.1090/S0894-0347-1995-1273413-2
(preprint arXiv:alg-geom/9402009).

**Theorem 1.1.** For $S$ nonsingular complex algebraic, $\mathcal V$ a polarized
variation of Hodge structures of weight 0 with polarization $Q$, and
$S^{(K)}=\{(s,u):s\in S,\ u\in(\mathcal V_s)_{\mathbb Z}\ \text{of type }(0,0),\
Q(u,u)\le K\}$: **$S^{(K)}$ is an algebraic variety, finite over $S$.**

Corollaries 1.2–1.4: the **Hodge locus** — where a flat (rational) class remains
of type $(p,p)$, or where a flat rational subspace remains a Hodge
substructure — is an **algebraic subvariety** of $S$.

The sharpening over attempt-01 (which said only "Hodge locus algebraic"):

- **The result is UNCONDITIONAL.** It answers a question of **André Weil**:
  whether imposing a Hodge class on the generic member of a family is an
  algebraic condition on the parameters. **Previously this was known only
  conditionally — via the Hodge conjecture.** CDK removes that conditionality.
  So "Hodge classes behave as if algebraic" (the locus where they persist is
  algebraic) is now an **unconditional** evidence layer, not an HC-conditional
  one. This is stronger than attempt-01 conveyed and is the right framing for
  the evidence layer.

- **Proof mechanics (why it's a "control" result):** global Theorem 1.1 reduces
  to a local theorem near a normal-crossings boundary via (a) **Schmid's
  nilpotent orbit theorem**, (b) the **$SL(2)^r$-orbit theorem** of
  Cattani–Kaplan–Schmid (1986, *Ann. Math.* 123), and (c) **GAGA** to pass
  analytic→algebraic on the compactification. The local theorem is by
  contradiction, inducting on the number of vanishing coordinates with Hodge-
  metric norm estimates and the monodromy weight filtration. The point: CDK
  controls the *variation* (where Hodge classes live in families) without
  producing the cycles — exactly a control-not-resolution result, parallel in
  shape to Balaban's UV control (controls the regime, doesn't produce the IR
  object) and NS's conditional regularity (controls IF a norm is bounded,
  doesn't produce the bound).

`[hodge-cattani-deligne-kaplan]` moves from `to-verify` to **CONFIRMED +
sharpened** (unconditional, Weil-question, proof mechanics).

## Cross-problem compounding

Two reinforcing links surface:
- **CDK ↔ Balaban (YM):** both are "control the regime without producing the
  target object" results — CDK controls the Hodge locus (where classes
  persist) without producing cycles; Balaban controls the UV without producing
  the continuum gap. Same control-not-resolution shape, different fields.
- **Direction (A) ↔ Beal reduction:** Deligne §4 makes the analogy literal —
  HC reduces to *specific* Hodge classes (Künneth components, $\Lambda$), as
  Beal reduces to *specific* curves; in both, the reduction target is itself
  unproven. The 6-for-6 "control/reduction step, not resolution step" spine
  holds, with Hodge's "one-dimensional engine stops" now pinned to two named
  classes from the primary source.

## Theory toolbox touched this cycle

No new theory pages (verification confirms existing pages). `thm-cattani-
deligne-kaplan` should be updated with the unconditional/Weil-question +
$SL(2)^r$ proof-mechanics precision; `thm-standard-conjectures-motives` with
the "B and C are open special cases of HC (Deligne §4)" sharpening and the §5
HC⇔fully-faithful-motives equivalence. (Edits deferred to keep this cycle
one-move; flagged for a later Continue.)

## Honesty / to-verify (remaining)

- `[hodge-statement]`: **CONFIRMED (attempt-02)** — exact Deligne wording,
  rational-not-integral (integral fails, Atiyah–Hirzebruch, Remark iv), known
  for $H^2$ (Kodaira–Spencer), all against `hodge.pdf`.
- `[hodge-cattani-deligne-kaplan]`: **CONFIRMED + sharpened (attempt-02)** —
  JAMS 8(2) 1995, Theorem 1.1 + Corollaries 1.2–1.4; unconditional
  (Weil-question answered); proof via Schmid nilpotent orbit + $SL(2)^r$
  (Cattani–Kaplan–Schmid 1986) + GAGA.
- `[hodge-lefschetz-1-1]`: **corroborated (attempt-02)** — known for $H^2$ via
  exponential sequence / line bundles (Kodaira–Spencer), per Deligne §1.
- `[hodge-standard-conjectures]`: **sharpened (attempt-02)** — B (inverse
  Lefschetz) and C (Künneth components) are open special cases of HC (Deligne
  §4 Examples 1–2); §5 HC ⇔ fully-faithful motives→Hodge-structures given B,C.
  Charles–Markman known-cases detail **still to-verify** (attempt-03 target).
- `[hodge-recent-claims-unverified]`: **still to-verify** — Shimizu 2025 /
  Bouali 2024 / Abdelgalil 2025 / Mounda 2025 / Hajebi–Hajebi 2025; none
  peer-accepted (attempt-03 target: confirm status of the most-cited one).
- `[hodge-tate-analogue]`: **still to-verify** — $\ell$-adic Tate analogue
  open even for $H^2$.

## Next

Two natural branches for attempt-03:
1. **Verify the standard-conjecture known cases** (Charles–Markman 2013 for
   hyper-Kähler $K3^{[n]}$; surfaces; abelian varieties) against primary
   sources — directly extends the direction-(A) sharpening filed here.
2. **Status-check the most-cited recent claim** (e.g. Shimizu 2025) to either
   retire or sharpen `[hodge-recent-claims-unverified]` — honesty maintenance.
Both are single-move Continues. The rotation advances to collatz-conjecture
next regardless (cycle 5).