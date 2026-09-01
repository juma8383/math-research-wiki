---
type: method
name: Mordell-curve lens (cubic-cubic sum of two cubes)
created: 2026-08-24
tags: [number-theory, elliptic-curves, mordell-curves, integral-points]
used-in: [[beals_conjecture]]
provenance: []
---

# Mordell-curve lens — sum of two cubes

A non-modular angle on the cubic-cubic Beal sub-case, **verified
computationally** in attempt-05 (script `scripts/mordell_check.py`).

## The birational equivalence (verified)

The curve $C_N:\ x^3 + y^3 = N$ is birationally equivalent to the **Mordell
elliptic curve**

$$E_N:\ Y^2 = X^3 - 432\,N^2$$

via

$$X = \frac{12N}{x+y},\qquad Y = \frac{36N(x-y)}{x+y}.$$

Verified on the Ramanujan point: $9^3+10^3=1729=12^3+1$, $N=1729$, maps to
$(X,Y)=(1092,-3276)$ on $Y^2=X^3-432\cdot1729^2$; the trivial representation
$1^3+12^3$ maps to $(1596,-52668)$; and $6^3+8^3=728=9^3-1$ maps to
$(624,-3744)$ on $Y^2=X^3-432\cdot728^2$.

## What the gap-1 / gap-0 distinction becomes

- **Gap 0 (Beal/FLT $n=3$):** $x^3+y^3=z^3 \Leftrightarrow N=z^3$, Mordell curve
  $E_{z^3}: Y^2=X^3-432z^6$. FLT $n=3$ (Euler) ⟺ this family has **no
  non-trivial** integral points (beyond the degenerate $1^3+(-1)^3$-type).
- **Gap 1:** $x^3+y^3=z^3\pm1 \Leftrightarrow N=z^3\pm1$, Mordell curve
  $E_{z^3\pm1}$. This family **does** have non-trivial integral points for some
  $z$ (e.g. $z=12$ → $1729$, $z=9$ → $728$) — the Ramanujan/taxicab near-misses.

So the "why is the gap exactly 1 and never 0" question is reframed as a question
about **integral points on a family of Mordell curves**: $E_{z^3}$ has none,
$E_{z^3\pm1}$ sometimes does. **Siegel's theorem** gives finiteness of integral
points on each $E_N$ individually, but not a uniform Beal-style "zero" result.

## The decisive scope limit — this lens is cubic-only

The curve $x^a + y^b = N$ (smooth projective model) has genus

$$g = \frac{(a-1)(b-1)-(\gcd(a,b)-1)}{2}.$$

- $(a,b)=(3,3)$: $g=1$ — **elliptic** (Mordell), the lens above applies.
- $(a,b)=(3,5)$: $g=4$ — **higher genus** (Faltings territory).
- $(a,b)=(4,4)$: $g=9$; $(5,5)$: $g=21$ — higher genus.

**Consequence:** the Mordell-curve / elliptic lens exists *only* for the
cubic-cubic signature. For every other Beal signature — including the frontier
$(3,5,7)$ (where the relevant $x^3+y^5=N$ has genus $4$) — the "sum of two
powers" curve is genus $\geq 2$, where we have only Faltings (finiteness,
ineffective [[rg2024-faltings-algorithm]] gives effective computation only at
rank-0 Jacobian), and no explicit integral-point theory. This is consistent
with attempt-04's empirical finding that $(3,5,7)$ near-misses are degenerate:
there is no elliptic structure to generate genuine non-degenerate near-misses.

## Honest assessment

For the cubic case this lens is essentially a reformulation of Euler's FLT $n=3$
in Mordell-curve language — illuminating, not a new proof. It does **not**
generalize to the Beal frontier. Its value is conceptual: it pinpoints that the
gap-1-vs-gap-0 distinction is an *integral-points-on-a-genus-1-family*
phenomenon, and that this phenomenon is **specific to cubics** — which is
exactly why the cubic case is the only one with rich near-miss structure and the
only one classical descent (Euler) could close.

## When to reach for it

Only for the cubic-cubic sub-case, to understand the near-miss arithmetic. Do
not expect it to help with $\min\geq 4$ or mixed signatures — there the curve
leaves genus 1 and the lens dies.