# Progress — Magic Square of Squares

> Read-first file (SCHEMA Continue protocol). This problem's full state lives
> in [problem.md](problem.md) (statement + published bounds + censuses +
> heuristic quantification) and [notes.md](notes.md) (the working notebook,
> §§1–2i). This file is the resume pointer only — do not duplicate content.

## Current frontier (2026-09-03)

**Conjecture K34** (two-prime/ω₁=2 sum-freeness of $D((pq)^2)$) is the single
standing obstruction — two-prime freeness ⟺ K34 (`[mss-two-prime-uquad]`,
all other kill-equations K1/K2/K5–K16 dead). K34 is reduced to:

1. **Square-X points on the genus-1 quartics $M_A, M_B$** — MW groups fully
   computed (rank 1, torsion Z/2); genus-3 covers have rank J = 2 < 3
   (**Chabauty gate**: the actual Coleman computation at p=11 is the named
   proof path — notes.md §2h "Chabauty gate"; `#C3_A(F_11)=8`, bound ≤12,
   8 known points).
2. **The odd-depth primitive-divisor gate** (§2e–2g): X(nG)=w² forces even
   depth at every kernel prime; one odd-depth primitive divisor kills.
   Class-0 cosets forced past the effective Verzobio constant (n > 10²⁷²¹ ≫
   C ~ 10⁴¹–10⁴⁴ — §2i, correctly cited); nonzero cosets sit in a window
   BELOW the effective constant (existence there ineffective-only). This is
   a Wall–Sun–Sun-type gap — open unconditionally.
3. **The descent tree** (§2i-adjacent, `[mss-k34-descent]`): terminates in
   four locally-soluble genus-1 leaf quartics — extended census 0 hits
   (§2i, ~470k pairs, corrected parity); insolvability needs
   Tzanakis/2-descent machinery (Bennett–Walsh 1999 does NOT reach them,
   one-parameter scope — sources/bennett-walsh-1999.md).

## Honest state

No solution found (Buell's null verified independently to centers ≤ 10¹⁴);
no impossibility proof. Under the window-corrected Euler-product model a
solution is expected NOT to exist (P(0) ≈ 99.996% — model, not proof). K34
open; both named gates open.

## Single next step

The Chabauty–Coleman computation on C3_A at a good prime (rank 2 < 3) —
standard-but-laborious (Sage/Magma not available on this box; would need
Coleman integration or an honest annihilating differential + residue bound).

## Attempt log

MSS work is filed as notes.md sections + log.md entries (no attempt-NN
files): structural lemmas 2026-08-31 → parallelogram reduction + prime-power
freeness + two-prime structure 2026-09-01 → K34 elliptic + sieve2 + refine
2d–2h + descent 2026-09-01/02 → **continuation §2i 2026-09-03**
(attribution corrected to Verzobio 2023; leaf census extended 0 hits;
layer-1 bookkeeping reconciled; Bennett–Walsh scope clarified).