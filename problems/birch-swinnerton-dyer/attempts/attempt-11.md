---
type: attempt
problem: birch_swinnerton_dyer
attempt: 11
date: 2026-08-30
approach: Primary-source verification of Sano 2023 (arXiv:2308.08875) against the arXiv abstract — confirm the paper identity, the three applications, and the "derived Bockstein regulator" mechanism; flag what remains PDF-body-only
outcome: confirmed
tags: [primary-source-verification, sano-2023, derived-bockstein-regulator, bertolini-darmon, agboola-castella, abstract-level, to-verify-remaining]
---

# Attempt 11 — Sano 2023 abstract-verified: arXiv-only preprint, three applications confirmed, "derived Bockstein regulator" via Nekovář confirmed; the "degenerate height pairing" mechanism is search-derived (not in the abstract)

Cycle-5 Continue on BSD (attempt-10's "Next" target). attempt-10 located Sano
2023 as the paper targeting the remaining two-fold conditional, but recorded
its theorem statements from a search summary. This cycle verifies against the
arXiv abstract (primary source).

## Confirmed from the arXiv abstract

- **Identity**: Takamichi Sano, *Derived Bockstein regulators and
  anticyclotomic $p$-adic Birch and Swinnerton-Dyer conjectures*,
  arXiv:2308.08875, submitted 17 Aug 2023. **arXiv-only** — no journal
  reference or published version indicated. (So it is a preprint, not
  peer-reviewed; the citation must carry this caveat.)
- **"Derived Bockstein regulator"**: confirmed — the author introduces them
  "by using an idea of Nekovář" and establishes "a general descent formalism
  involving derived Bockstein regulators."
- **Three applications** (paraphrased from the abstract, confirmed):
  1. a Bertolini–Darmon BSD-type conjecture for Heegner points follows from
     Perrin-Riou's Heegner point main conjecture **up to a $p$-adic unit**;
  2. an Agboola–Castella $p$-adic BSD conjecture for the BDP $p$-adic
     $L$-function follows from the Iwasawa–Greenberg main conjecture **up to
     a $p$-adic unit**;
  3. Kataoka–Sano conjectures/results on derivatives of Euler systems are
     extended into a "natural derived setting."

## What is NOT in the abstract (flagged)

- **The exact theorem statements** (Thm 2.13 descent formalism, Thm 3.10
  Bertolini–Darmon, Thm 4.13 Agboola–Castella, Conj 5.5 derived setting) are
  **not in the abstract** — the theorem *numbers* and precise "up to a
  $p$-adic unit" qualifiers remain search-derived, `to-verify` against the
  PDF body.
- **The "degenerate height pairing" mechanism** (attempt-10's structural
  explanation of *why* the regulator is derived) is **not in the abstract** —
  it was the search summary's gloss. It is structurally plausible (the
  anticyclotomic height pairing is known to degenerate) but is flagged as
  search-derived, not primary-source-confirmed.
- **The "unconditional corollary via BCK21"** (attempt-10's claim that
  Thm 3.10 has an unconditional corollary using BCK21) is **not in the
  abstract** — it was in the search summary. Flagged `to-verify` against the
  PDF body.

## What this changes in the obstruction map

- **Sano 2023 is confirmed as a real, arXiv-only preprint** with the three
  applications that sharpen the BSD-for-$E/K$ chain to "up to a $p$-adic
  unit." The "one explicit $p$-adic unit" sharpening (attempt-10) stands at
  the abstract level.
- **Two of attempt-10's load-bearing specifics are downgraded to
  `to-verify`**: the exact theorem numbers (2.13/3.10/4.13/5.5) and the
  "unconditional corollary via BCK21" are search-derived, not in the
  abstract. The "degenerate height pairing" mechanism is likewise
  search-derived.
- **The core structural claim survives**: the derived Bockstein regulator
  (via Nekovář) is the formalism that reduces the BSD-for-$E/K$ chain to a
  single $p$-adic unit, and that unit is exactly Kataoka–Sano's
  $R^{Boc}_{K_\infty}$ (Conj 1.9 + non-vanishing). This is confirmed at the
  abstract level.

## Honesty / scope

- **This is an abstract-level verification, not a full PDF verification.**
  The exact theorem statements and the "unconditional via BCK21" corollary
  remain `to-verify` against the Sano 2023 PDF body. BSD remains open.
- **Sano 2023 is a preprint** (arXiv-only as of this check) — the citation
  must not be treated as peer-reviewed.
- No proof move; rank $\ge2$ and exact $|\Sha|$ untouched.

## Next (attempt-12)

The natural next target is to fetch the Sano 2023 PDF body and confirm the
exact statements of Thm 3.10 (and its unconditional-via-BCK21 corollary) and
Thm 4.13 — the two results that carry the "up to a $p$-adic unit" sharpening.
Alternatively, rotate to the next problem (navier-stokes attempt-07) per the
standing rotation, since the BSD direction-(A) chain is now mapped to a
single named target (the derived Bockstein regulator) and further BSD
verification is PDF-body-level detail.
