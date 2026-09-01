---
type: attempt
problem: beals_conjecture
attempt: 17
date: 2026-08-24
approach: Verify the Poonen-Schaefer-Stoll mechanism against the actual paper; caught and corrected a factual error in the wiki
outcome: confirmed
tags: [verification, correction, triangle-groups, pss2007, honesty]
loop_cycle: 15 of 20
---

# Attempt 17 — Verify PSS against the paper (and a caught error)

This cycle verifies the one substantive flagged to-verify item: the
Poonen–Schaefer–Stoll mechanism, ingested in attempt-14 from a search-result
summary. Fetched the paper's abstract/Theorem 1.1 (arXiv math/0508174; Duke
Math. J. 137(1), 103–158, 2007).

## Verified claims (confirmed against the paper)

- **16 primitive integer solutions** to $x^2+y^3=z^7$ (Theorem 1.1) — full list
  recorded in `sources/poonen-schaefer-stoll-2007.md`. ✓
- **Nonabelian descent via $\mathrm{PSL}_2(\mathbb F_7)$** (order 168), the
  smallest Hurwitz group. ✓
- Reduction to **10 twists $C_1$–$C_{10}$ of the Klein quartic** $X$
  ($x^3y+y^3z+z^3x=0$, genus 3, 168 automorphisms), after a local-solubility
  filter. ✓
- $X\cong X(7)$ as a modular curve; irreducible 7-torsion cases reduced via
  **Ribet level lowering + modularity** to 13 elliptic curves of low
  conductor. ✓
- **Chabauty–Coleman** for $\operatorname{rank}J<3$ (all curves except $C_5$);
  **$(1-\zeta)$-descent** for $C_1,C_2,C_3$ (CM by $\mathbb Z[\zeta_7]$);
  **2-descent** for $C_4$–$C_{10}$; **Mordell–Weil sieve** for $C_5$
  ($\operatorname{rank}=\operatorname{genus}=3$), proving
  $C_5(\mathbb Q)_{\text{subset}}=\varnothing$. ✓
- $(2,3,7)$ has $\chi=1/2{+}1/3{+}1/7-1=-1/42$, the negative value **closest to
  $0$** — "the hardest generalized Fermat equation," and the **first complete
  treatment of a pairwise-coprime $(p,q,r)$ with $\chi<0$**. ✓

## The error this verification caught

attempt-14 / `method-triangle-group-descent.md` labeled $(2,3,7)$ as
**"spherical"** with "$41/42>1$". This is **false**: $41/42 = 0.976 < 1$, so
$(2,3,7)$ is **hyperbolic** (infinite triangle group), not spherical. PSS works
via a **finite quotient** $\mathrm{PSL}_2(\mathbb F_7)$ of the *infinite*
$\Delta(2,3,7)$ (the Klein quartic automorphisms), not because the triangle
group itself is finite.

The real enablers of PSS are two things $(3,5,7)$ lacks:
1. **Near-spherical position** — $(2,3,7)$ has $\chi=-1/42$ (closest to $0$),
   giving the distinguished finite quotient $\mathrm{PSL}_2(\mathbb F_7)$;
   $(3,5,7)$ has $\chi=-34/105$, far deeper hyperbolic, no analogous natural
   finite quotient for descent.
2. **An exponent $2$** — the $X(7)$ modular-curve interpretation (twists =
   exotic level-7 structures on elliptic curves) requires the $x^2$ term;
   $(3,5,7)$ has no exponent $2$.

## Corrections applied (append-only discipline)

- `method-triangle-group-descent.md`: rewrote the table and "why it stops
  there" section with the corrected framing (both $(2,3,7)$ and $(3,5,7)$
  hyperbolic; distinction is near-spherical + exponent $2$ vs deep-hyperbolic +
  no $2$). Method pages are wiki-layer (mutable) so corrected directly; the
  correction is logged here and in the page's own correction blockquote.
- `sources/poonen-schaefer-stoll-2007.md`: updated all tag sections with
  verified facts; flagged the specific Mordell–Weil sieve primes
  ($2,3,13,23,97$) as "[summary]" (present in the original search summary, not
  re-confirmed against the full text); added the "first pairwise-coprime
  $\chi<0$" significance and the $X(7)$ modular interpretation.
- `attempt-14.md`: append-only **correction blockquote** at the top noting the
  $(2,3,7)$ mislabel and pointing to the corrected references; original text
  unchanged.
- `synthesis.md`: corrected the unifying-lens paragraph and direction (B) —
  the divide is "near-spherical + exponent $2$" vs "deep hyperbolic + no $2$",
  not "spherical vs hyperbolic."

## Outcome

**confirmed (with correction).** The PSS mechanism as recorded is
substantively accurate; the verification confirmed every load-bearing claim
(16 solutions, PSL₂(F₇), 10 Klein-quartic twists, Chabauty/MW-sieve/descents,
C₅, X(7), level lowering). It caught one factual error — the spherical
mislabel of $(2,3,7)$ — now corrected across the wiki via the append-only +
direct-fix discipline. The structural conclusion is unchanged but sharper:
the obstruction at distinct-odd-prime signatures is **deep hyperbolicity + no
exponent $2$**, which simultaneously gates the modular route (thread 1), the
spherical-reduction route (thread 5), and the geometric PSS route (B).

## Honesty note

This cycle is a good example of why flagged to-verify items matter: a
plausible-sounding first-principles framing ("spherical vs hyperbolic")
contained a silent arithmetic error ($41/42>1$). Verifying against the
primary source surfaced it. The wiki's discipline (flag unverified claims,
verify, correct with a dated trail) worked as intended.

## Next cycles (5 remain)

- Final Lint pass (the corrections touched 4 files — check consistency).
- Loop close-out summary for the log.
- Guard against padding: if no further genuine angle appears, declare the arc
  complete.