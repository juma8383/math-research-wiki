# Attempt 01 — Riemann Hypothesis (first attack)

> First attack. Per the research protocol: ≥3 distinct approaches, evidence +
> counterevidence, simpler-equivalent AND more-general statements, computational
> check, formalized assumptions, failed-attempt tracking, re-evaluated
> confidence, cross-problem lens. Verified via 4 WebSearches (2 succeeded
> richly, 2 rate-failed); classical facts search-confirmed, 2024 / preprint
> items flagged `[to-verify]`.
>
> Date: 2026-08-25. Folder: `problems/riemann-hypothesis/` (the 9th wiki
> problem; the missing Clay Millennium problem — 8 prior = 7 open + the solved
> [[poincare_conjecture]] contrast case). Budget: orange zone (weekly ~83.4%),
> 0 subagents, 4 WebSearches.

## 1. Statement and exact frontier

**Statement.** All non-trivial zeros of $\zeta(s)$ have $\Re(s)=\tfrac12$. The
trivial zeros $s=-2,-4,\dots$ (from the $\Gamma$ poles) are excluded; the
question is the non-trivial zeros in the critical strip $0<\Re(s)<1$. Clay
Millennium Prize; the most famous open problem in mathematics; controls the
PNT error term and prime distribution.

**Exact frontier (verified facts):**

| Regime | What is known | Gap |
|---|---|---|
| Computational | All zeros on the line up to $T\le3\cdot10^{12}$ (Platt–Trudgian 2021) | a slice (up to $T$) — not "every" |
| Zero-free region | no zeros in $\Re\ge1-c(\log\lvert t\rvert)^{-2/3}(\log\log\lvert t\rvert)^{-1/3}$ (Korobov–Vinogradov) | near $\Re=1$ only |
| Zero-density $N(\sigma,T)$ | Ingham 1940 (stood 80 yrs) → **Guth–Maynard 2024** breaks it at $\sigma=\tfrac34$; Chourasiya 2024 explicit Carlson | average/density — not "every" |
| Proportion on line | Levinson $\tfrac13$ (1974) → Conrey $\tfrac25$ (1989) → $\tfrac{5}{12}$ (2020); **2/3 claimed 2024, un-peer-reviewed** | a fraction — not "all" |
| Symmetry | functional equation pairs $\Re\leftrightarrow1-\Re$ | pairs, does not pin |
| **Open content** | **every non-trivial zero has $\Re=\tfrac12$** | **the control step** |

## 2. The obstruction (control, not resolution)

The wiki's standing lens: the obstruction is at the **control/reduction step**,
not the **resolution step**; "one-dimensional engine stops." RH fits in the
same shape as [[collatz_conjecture]] (density→pointwise) and [[navier_stokes]]
(slice→full):

- **Resolution works on a slice / on average**: computation (up to $T$),
  Selberg almost-all, zero-density, zero-free regions, proportion. All work.
- **Control to full strength is the wall**: every zero, every height. The
  functional equation is a *resolution-layer symmetry* (pairs zeros) that does
  **not** discharge the control step (does not pin the line — a zero at
  $\tfrac12+\beta+it$ is allowed, paired with $\tfrac12-\beta+it$). Forcing
  $\beta=0$ is the open content.

Three **exact control-reductions** (each turns RH into a single property one
cannot then discharge):

1. **Hilbert–Pólya** — RH ⟺ zeros = spectrum of a self-adjoint operator.
   Control = self-adjointness; **no operator known**. Connes (1997 numdam
   10.5802/jedp.516; 2019 essay) builds the adele-class-space spectral
   interpretation, reduces RH to a trace-formula validity (Weil positivity),
   names a minus-sign / Riemannian obstruction. Berry–Keating $H=xp$ is a
   toy. `[to-verify: Connes reductions at line level]`
2. **Weil / Li / Bombieri–Lagarias** — RH ⟺ positivity of the explicit-
   formula distribution (Weil); ⟺ $\lambda_n\ge0\ \forall n$ (Li 1997, J.
   Number Theory 65); generalized (Bombieri–Lagarias 1999, JNT 77); screw-
   function equivalents (Suzuki 2023, JLMS, DOI 10.1112/jlms.12785); $\xi$-
   positivity (Lagarias 1999, Acta Arith. 89). Control = proving the
   positivity / $\lambda_n\ge0$ — **not done**. `[to-verify: precise reduction statements]`
3. **Function-field** — RH for varieties over $\mathbb F_q$ is a THEOREM
   (Weil 1940s curves; Deligne 1973/74 all varieties, the Weil conjectures),
   via étale cohomology + Lefschetz trace + **positivity of the Rosati
   involution** (Frobenius eigenvalues are Weil numbers, $|\alpha|=q^{-n/2}$).
   Milne (ALM 35, 2015) / Kowalski surveys. The engine **stops at the number
   field**: no Frobenius / no Rosati positivity in char 0. Canonical
   "one-dimensional engine stops."

## 3. The two-avatars structure (deepest finding)

RH has the same **function-field-proven / number-field-open** two-avatars
structure as [[birch_swinnerton_dyer]] (attempt-07) and [[PvsNP]] (notes):

- Function-field RH (varieties / $\mathbb F_q$) — **PROVEN** (Weil; Deligne).
- Number-field RH ($\zeta(s)$ / $\mathbb Q$) — **OPEN** (Millennium).

Same shape as BSD's function-field BSD (proven, Kato–Trihan) vs number-field
BSD (open). In both, the function-field control tool (Frobenius/Rosati for
RH; étale Euler-system for BSD) has no char-0 / number-field translation —
the engine stops. Two-avatars now in **three** problems (RH, BSD, PvsNP),
suggesting it is a general Millennium-grade feature. Sharpens 6-for-6/7-for-7
from "parallel walls" to "two avatars of one control step, one proven one
open." (Structural analogy, not mathematical equivalence.)

**Hodge link** ([[hodge_conjecture]]): the standard conjectures (Lefschetz B
= algebraicity of the inverse Lefschetz operator → Rosati-type positivity)
are the *same* control step for Hodge (HC ⇔ standard conjectures ⇒ motives
Tannakian ⇒ HC reduces to specific classes, Hodge attempt-02) and for a
*motivic* RH (the number-field Rosati positivity). Both open; both hinge on
positivity/algebraicity of correspondences. Genuine link at the control-tool
level.

## 4. ≥3 approaches (research-protocol step)

Named in [notes.md](../notes.md): **(A)** Hilbert–Pólya spectral (self-
adjointness = control); **(B)** Weil/Li/Bombieri–Lagarias positivity
(positivity = control); **(C)** zero-density/computational/proportion
(resolution on slices); **(D)** function-field analogy (engine that works,
stops at number field); **(E)** de Branges (tracked failed approach —
coefficient-inequality in Hilbert spaces of entire functions; load-bearing
inequality fails; not accepted `[to-verify]`). Approaches (A) and (B) are
linked: Connes's trace formula *is* Weil positivity.

## 5. Simpler-equivalent AND more-general statements

- **Simpler equivalent (the exact reductions):** RH ⟺ Li coefficients
  $\lambda_n\ge0\ \forall n$ (Li 1997) ⟺ Weil explicit-formula distribution
  $\ge0$ ⟺ a broad class of analogous positivity statements
  (Bombieri–Lagarias) ⟺ Suzuki screw-function positivity (2023). Each is an
  *equivalent* of RH reduced to a single sign control.
- **More general:** the **generalized Riemann hypothesis (GRH)** for all
  $L$-functions (Dirichlet, Dedekind, Hecke, automorphic); the **Selberg
  class** axiomatizes the functions expected to satisfy RH; the **Weil
  conjectures / function-field RH** for varieties over finite fields
  (proven) is the geometric generalization. The number-field RH is the one
  avatar of this broad family that remains open in its classical form.

## 6. Computational check

Zeros verified on the line up to $T=3\cdot10^{12}$ (Platt–Trudgian 2021),
$\sim10^{13}$ zeros, no counterexample. The empirical evidence is
overwhelming and the zeros exhibit GUE random-matrix statistics (Montgomery
pair correlation; Odlyzko numerics) — *consistent* with a self-adjoint
spectrum (Hilbert–Pólya). But statistics ≠ proof: GUE statistics support
approach (A) heuristically without supplying the operator (the control tool).

## 7. Counterevidence / honest caveats

- **Symmetry does not pin.** The functional equation is the most-often-cited
  "why RH should be true" intuition, but it only pairs zeros — it is logically
  insufficient (off-line zeros are symmetry-allowed). Citing it as evidence is
  weak.
- **de Branges failure.** A serious, repeated attempt at (a variant of) the
  positivity approach failed (the coefficient inequality does not hold) —
  recorded (E), a caution against naïve positivity arguments.
- **Proportion/density cannot reach "all."** Even a verified 2/3-on-the-line
  result leaves 1/3 unaccounted; zero-density bounds $N(\sigma,T)$ leave a
  vanishing-but-nonzero exceptional set. The average side is *structurally*
  incapable of the all-zeros conclusion (the Collatz echo — Π²₀-completeness
  there; the symmetry-doesn't-pin gap here).
- **`[rh-2024-claims-unverified]`**: the 2/3-of-zeros-on-the-line claim (2024,
  linear-algebraic + Lean-4 core) is **not peer-reviewed**; treated as
  unverified (same discipline as YM/NS/Collatz preprints). Even if true it is
  a proportion, not the control step.

## 8. Re-evaluated confidence

- **RH is almost certainly true** (overwhelming computation + GUE statistics
  + the function-field precedent + the structural analogy to proven
  function-field RH). Confidence that the conjecture holds: very high.
- **Confidence that any current approach will prove it soon: low.** Each of
  the three control-reductions lands on an undischarged property (self-
  adjointness / positivity / number-field Rosati) with no known tool. The
  2024 advances (Guth–Maynard, Chourasiya) are resolution-on-average, not
  control. Honest ceiling for this attempt: **frontier mapped, obstruction
  framed as a control step, two-avatars twin to BSD identified** — no proof
  move, no claim to progress on RH itself.

## 9. Cross-problem lens (8th open problem, + the contrast case)

- [[birch_swinnerton_dyer]]: the two-avatars **twin** (function-field proven /
  number-field open) — the deepest link; both stop at the char-0 translation of
  a function-field control tool.
- [[hodge_conjecture]]: the standard conjectures are a **shared control tool**
  (motivic Rosati positivity for both a motivic RH and HC).
- [[collatz_conjecture]] / [[navier_stokes]]: the slice→full / average→pointwise
  control wall, the same shape.
- [[PvsNP]]: the two-faces structure (one closes, one open) — the third
  two-avatars instance.
- [[poincare_conjecture]]: the contrast — the one problem where the control
  step *was* discharged (Perelman's $W$-entropy); RH is the canonical instance
  of one still standing.

## 10. Outcome

**Partial.** Frontier verified (computational Platt–Trudgian; zero-free
Korobov–Vinogradov; zero-density Ingham→Guth–Maynard 2024; proportion
Levinson/Conrey→5/12 + the un-peer-reviewed 2/3 claim). Obstruction framed =
the control step (slice/average → every zero), three exact reductions
(Hilbert–Pólya self-adjointness; Weil/Li/Bombieri–Lagarias positivity;
function-field Frobenius/Rosati proven, stops at the number field). Deepest
finding: the two-avatars structure = the [[birch_swinnerton_dyer]] twin
(sharpens the wiki to "two avatars of one control step, one proven one open,"
now in RH/BSD/PvsNP). ≥3 approaches + simpler-equivalents (Li, Weil,
Bombieri–Lagarias) + more-general (GRH / Selberg class / function-field RH) +
computational evidence + counterevidence (symmetry-doesn't-pin, de Branges
failure, average-can't-reach-all) + cross-problem lens. No proof move; honest
ceiling = map + framing + twin.

## To-verify (next moves)

- Primary-source verify the 2024 advances: Guth–Maynard (statement, venue/DOI,
  "breaks Ingham 1940"); `[rh-2024-claims-unverified]` (authorship, venue,
  peer-review, exact 2/3 vs 5/12); Chourasiya 2024 (arXiv:2412.02068, the
  $5-2\sigma$ Carlson exponent).
- Suzuki 2023 (JLMS DOI 10.1112/jlms.12785) screw-function equivalents; Connes
  1997/2019 trace-formula reduction at line level; Li 1997 / Bombieri–Lagarias
  1999 / Lagarias 1999 precise statements; Platt–Trudgian 2021 height record;
  Weil positivity criterion; Deligne 1974.
- de Branges: the precise obstruction in his manuscripts.
- Optional future `theory/methods/`: a shared **function-field-proven /
  number-field-open two-avatars** page (RH ‖ BSD) and a **standard-conjectures
  control-tool** page (RH ‖ Hodge).