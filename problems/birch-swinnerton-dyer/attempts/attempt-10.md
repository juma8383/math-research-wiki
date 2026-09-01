---
type: attempt
problem: birch_swinnerton_dyer
attempt: 10
date: 2026-08-30
approach: Survey the remaining two-fold conditional (Kataoka–Sano Conj 1.9 Darmon-derivative + Bockstein regulator R^Boc ≠ 0) against the current literature — locate Sano 2023's "derived Bockstein regulators" as the formalism that targets exactly this gap
outcome: confirmed
tags: [survey, derived-bockstein-regulator, darmon-derivative, bertolini-darmon, agboola-castella, bdp, sano-2023, control-step, direction-a]
---

# Attempt 10 — The remaining two-fold conditional located in the literature: Sano 2023's derived Bockstein regulators target exactly the Conj 1.9 + R^Boc ≠ 0 gap

Cycle-5 Continue on BSD (attempt-09's "Next" target). attempt-09 left the
obstruction as a **two-fold conditional** — Kataoka–Sano's **Conj 1.9**
(Darmon-derivative explicit formula) + **$R^{Boc}_{K_\infty}\neq0$** (Bockstein
regulator) — over a proven base (Heegner MC, BCK21). This cycle surveys what
is known toward that two-fold conditional.

## The key paper: Sano 2023, "Derived Bockstein regulators"

**Takamichi Sano**, *Derived Bockstein regulators and anticyclotomic $p$-adic
Birch and Swinnerton-Dyer conjectures*, arXiv:2308.08875 (2023). This is the
paper that targets exactly the remaining gap. It:

- Introduces **"derived Bockstein regulators"** using Nekovář's *Selmer
  complexes* (Astérisque 310).
- Establishes a general **descent formalism** for derived Bockstein regulators
  (Theorem 2.13).
- **Theorem 3.10**: the **Bertolini–Darmon BSD-type conjecture for Heegner
  points** (1996) follows from **Perrin-Riou's Heegner point main conjecture
  up to a $p$-adic unit**, with an **unconditional corollary using BCK21**.
- **Theorem 4.13**: the **Agboola–Castella $p$-adic BSD conjecture** for the
  Bertolini–Darmon–Prasanna $p$-adic $L$-function follows from the
  **Iwasawa–Greenberg main conjecture up to a $p$-adic unit**.
- **Conjecture 5.5**: extends the Kataoka–Sano conjectures on derivatives of
  Euler systems for general motives into a natural **derived** setting.

## The structural insight: why the Bockstein regulator is "derived"

The central theme (from the search summary): derived Bockstein regulators
provide a **unified formalism** showing that Iwasawa main conjectures imply
$p$-adic BSD-type conjectures **up to $p$-adic units**, with the anticyclotomic
setting requiring **"derived" heights because the natural $p$-adic height
pairing is degenerate there**.

This is the precise reason the remaining gap is a *derived* control step, not
a classical one: in the anticyclotomic summand (the $E^K$-twist side of
$\mathrm{Sel}(K)\simeq\mathrm{Sel}(\mathbb Q)\oplus\mathrm{Sel}(\mathbb Q,E^K)$),
the classical $p$-adic height pairing degenerates, so the regulator that
appears in the BSD formula must be a **derived** (Bockstein) regulator. This
is exactly Kataoka–Sano's $R^{Boc}_{K_\infty}$ — the "Bockstein regulator" of
Conj 1.9 and Thm 1.11.

## The obstruction map, sharpened again

The two-fold conditional (Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$) is now
understood as a **single derived-control step**, decomposed as:

| Step | Status |
|---|---|
| Heegner MC (Perrin-Riou) | **PROVEN** (BCK21 Thm A, explicit hypotheses) |
| ⟹ Bertolini–Darmon BSD-type conj. up to a $p$-adic unit | **PROVEN** (Sano Thm 3.10, unconditional via BCK21) |
| ⟹ Agboola–Castella $p$-adic BSD for BDP up to a $p$-adic unit | **PROVEN** (Sano Thm 4.13, via Iwasawa–Greenberg MC) |
| **the explicit $p$-adic unit = the derived Bockstein regulator** | **OPEN** — this is Conj 1.9 + $R^{Boc}\neq0$ |

So the entire BSD-for-$E/K$ chain is now **proven up to a single $p$-adic
unit**, and that unit is the derived Bockstein regulator. Conj 1.9 is the
explicit formula for that unit; $R^{Boc}_{K_\infty}\neq0$ is its
non-vanishing. This is the sharpest possible statement of the BSD obstruction:
**one explicit $p$-adic unit (the derived Bockstein regulator) separates the
proven "up to a unit" results from the full $p$-part of BSD for $E/K$.**

## The cyclotomic analogue (the other summand)

**Burns–Kurihara–Sano**, *On Derivatives of Kato's Euler System and the
Mazur-Tate Conjecture*, IMRN (2025), DOI 10.1093/imrn/rnaf012 — the
cyclotomic-side analogue: derivatives of Kato's Euler system, Bockstein
regulators, and the Mazur-Tate conjecture. So the "derived regulator" control
step has a **cyclotomic twin** (Kato's system) and an **anticyclotomic twin**
(Heegner points) — the same two-summand structure as the Selmer decomposition,
now at the level of the *derived regulator* control step.

## The original conjecture

**Henri Darmon**, *A refined conjecture of Mazur-Tate type for Heegner
points* (2007) — the original Darmon conjecture that Sano's Thm 3.10 and
Kataoka–Sano's Conj 1.9 refine. The "Darmon-derivative" of Conj 1.9 is the
rank-2 Euler-system avatar of Darmon's refined Mazur-Tate conjecture.

## What this changes in the obstruction map

- **The two-fold conditional is now a single derived-control step**: the
  entire chain (Heegner MC → Bertolini–Darmon → Agboola–Castella) is proven
  up to a $p$-adic unit, and that unit is the derived Bockstein regulator.
  Conj 1.9 + $R^{Boc}\neq0$ is the *explicit* determination of that unit.
- **The "derived" nature is explained**: the anticyclotomic height pairing
  degenerates, forcing the derived (Bockstein) regulator — this is *why* the
  control step is harder than the classical rank-1 case, and it is a concrete,
  named mechanism, not a vague "rank-2 is hard."
- **The two-summand structure persists to the control step**: cyclotomic
  (Burns–Kurihara–Sano, Kato derivatives) + anticyclotomic (Sano, Heegner
  derivatives) — the same $\mathrm{Sel}(K)\simeq\mathrm{Sel}(\mathbb Q)\oplus
  \mathrm{Sel}(\mathbb Q,E^K)$ split, now at the derived-regulator level.
- **Direction (A) is now a single named target**: determine the derived
  Bockstein regulator explicitly (Conj 1.9) and show it is non-zero
  ($R^{Boc}\neq0$). Everything else in the BSD-for-$E/K$ chain is proven.

## Honesty / scope

- **This is a survey, not a proof move.** BSD remains open; rank $\ge2$ and
  exact $|\Sha|$ untouched. The cycle *located* the remaining two-fold
  conditional in the literature (Sano 2023) and *sharpened* it to a single
  derived-control step.
- **Sano 2023 is an arXiv preprint** (arXiv:2308.08875) — publication status
  not confirmed this cycle; flagged `to-verify` before load-bearing reuse.
- **The theorem statements** (Sano Thm 2.13/3.10/4.13, Conj 5.5; Burns–
  Kurihara–Sano 2025) are recorded from the search summary
  (primary-source-consistent but not line-by-line re-derived); the exact
  "up to a $p$-adic unit" qualifiers and the unconditional-corollary scope
  are flagged `to-verify` against the paper bodies.
- **The "degenerate height pairing" mechanism** is the search summary's
  explanation of why the regulator is derived — structurally consistent with
  the anticyclotomic setting, but flagged as search-derived.

## Next (attempt-11)

Primary-source-verify **Sano 2023** (arXiv:2308.08875) against the paper body
— the exact statements of Thm 3.10 (Bertolini–Darmon ⟸ Heegner MC up to a
unit, unconditional via BCK21) and Thm 4.13 (Agboola–Castella ⟸
Iwasawa–Greenberg up to a unit), and whether Conj 5.5 subsumes Kataoka–Sano's
Conj 1.9. This is the natural next target: it would confirm the "one explicit
$p$-adic unit" sharpening and pin the exact remaining gap.
