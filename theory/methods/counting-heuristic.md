---
type: method
name: Counting heuristic for generalized Fermat equations
created: 2026-08-24
tags: [number-theory, heuristic, counting, reciprocal-invariant, fermat-catalan]
used-in: [[beals_conjecture]]
provenance: [heuristic — standard Fermat-Catalan/Tijdeman-type volume estimate; NOT a theorem]
---

# Counting heuristic for generalized Fermat equations

> **Heuristic, not a theorem.** This page records a standard volume/counting
> estimate for $X^p+Y^q=Z^r$. It is the soft-probabilistic analogue of
> [[thm-darmon-granville]]'s rigorous finiteness. It is cited for *predictive*
> insight (why zero is the expected answer; why sparsity is monotone in the
> exponents), never as a proof.

## The estimate

Fix a signature $(p,q,r)$ and count primitive solutions to
$X^p+Y^q=Z^r$ with $Z\leq H$ (height bound). Then $X\leq H^{r/p}$,
$Y\leq H^{r/q}$, so there are $\sim H^{r(1/p+1/q)}$ candidate $(X,Y)$ pairs. Each
yields a value $X^p+Y^q$ in a range of size $\sim H^r$; the density of perfect
$r$-th powers there is $\sim H/H^r=H^{1-r}$ (there are $\sim H$ $r$-th powers up
to $H^r$). The expected number of hits scales as

$$N_{p,q,r}(H)\;\sim\; H^{\,r\chi}, \qquad
\chi=\tfrac1p+\tfrac1q+\tfrac1r-1 .$$

This is the reciprocal invariant of [[def-beal-equation]] made *predictive*.

## The trichotomy, now as a growth rate

| regime | $\chi$ | expected count $H^{r\chi}$ | prediction |
|---|---|---|---|
| spherical | $>0$ | $\to\infty$ | infinitely many (parametrized families) |
| Euclidean | $=0$ | constant | **borderline / inconclusive** |
| hyperbolic | $<0$ | $\to 0$ | finitely many, sparse |

The classification in [[def-beal-equation]] ($>1/=1/<1$ for $1/p{+}1/q{+}1/r$)
becomes a statement about *solution density*, not just geometry.

## What it predicts, and what it does not

**Predicts (heuristically):**
- **Finiteness for $\chi<0$.** $H^{r\chi}\to0$ means the density of solutions
  thins to nothing; the total count is expected small and finite. This
  *parallels* — does not derive — the rigorous
  [[thm-darmon-granville]] finiteness (Faltings) and the
  [[method-abc-finiteness]] strength.
- **Monotone sparsity.** As $\chi$ grows more negative, $H^{r\chi}$ shrinks
  faster, so solutions get sparser and near-miss gaps grow. This is *exactly*
  the empirical monotonicity observed computationally
  [[rg2024-comp-bound]]: $(3,5,7)$ min non-degenerate coprime gap $29$ →
  $(3,5,11)$ gap $77$, with $0$ exact and $0$ genuine gap-$1$ in both. The
  heuristic *predicts* the rigidity the searches found.
- **Why the modular engine is forced at $(3,3,3)$.** $(3,3,3)$ has $\chi=0$,
  the Euclidean/borderline case where $H^{r\chi}=H^0$ is a *constant* — the
  heuristic is inconclusive (could be $0$, finite, or need finer structure).
  This is precisely where the soft estimate fails to decide and the hard
  machinery (FLT's Frey/modularity/level-lowering, [[method-frey-modularity]])
  is required. The "hard kernel" diagnosis of synthesis.md is now mirrored
  heuristically: the unique signature where all classical structures coincide
  is also the unique signature where the counting heuristic is borderline.

**Does NOT prove:**
- **Zero.** For $\chi<0$ the heuristic says the expected count is *small*
  (density tending to $0$), but a heuristic constant rounding below $1$ is
  not a theorem. The "finitely many → zero" upgrade — the entire open content
  of Beal — is *also* beyond the counting heuristic. Every route (modular,
  geometric, descent, spherical, PSS, **and counting**) delivers at most
  finiteness; zero is the common open content.

## Place in the obstruction map

This is a **sixth** angle on $(3,5,7)$, distinct from the five rigorous
threads but converging on the same wall:

| # | angle | delivers | stops at |
|---|---|---|---|
| 1–5 | Frey/Darmon/Mordell/descent/spherical (rigorous) | varies | reduction step; no mechanism without shared/even/spherical structure |
| 6 | counting heuristic (soft) | finiteness (qualitative) | "small expected count" ≠ "zero" |

The unifying lens of synthesis.md — distinct-odd-prime signatures lack the
near-spherical position or exponent $2$ that every *effective* method needs —
is silent on the counting heuristic, because the heuristic is *not* an
effective method: it never produces a finite list to check, only a density.
So it cannot fill the reduction-step gap either; it explains *why* zero is
expected without providing a mechanism to verify it. This is consistent, not
a contradiction: the heuristic is a different *kind* of obstruction
(expectation, not reduction).

## Honest scope

- The $H^{r\chi}$ scaling is the standard volume heuristic; the implicit
  constant is not controlled, so even the finiteness prediction is
  non-rigorous (rigorous finiteness is Faltings/Darmon–Granville alone).
- It gives the right qualitative picture (spherical $\to$ infinite; Euclidean
  $\to$ borderline; hyperbolic $\to$ sparse-finite) and the right
  *comparative* prediction (monotone sparsity), which the computations
  confirm.
- It does not touch the "zero" content. A proof of Beal cannot rest on it.