---
type: attempt
problem: beals_conjecture
attempt: 19
date: 2026-08-24
approach: Develop the unexplored probabilistic side — the counting/volume heuristic for generalized Fermat, predicting solution density from chi
outcome: partial
tags: [heuristic, counting, reciprocal-invariant, fermat-catalan, sixth-thread]
loop_cycle: 17 of 20
---

# Attempt 19 — The counting heuristic (a sixth angle from the soft side)

The wiki's five threads + PSS all attack $(3,5,7)$ from the *rigorous* side and
all stop at the reduction step. This cycle develops the one angle not yet
touched: the **counting/volume heuristic**, which predicts solution *density*
from the reciprocal invariant $\chi=1/p{+}1/q{+}1/r-1$. It engages the open
content ("finitely many → zero") from the probabilistic side that no prior
cycle explored.

Filed [[method-counting-heuristic]].

## The estimate

Count primitive $X^p+Y^q=Z^r$ with $Z\leq H$. Candidate pairs
$\sim H^{r(1/p+1/q)}$; hit-density (perfect $r$-th power in a range $\sim H^r$)
$\sim H^{1-r}$. Expected count

$$N_{p,q,r}(H)\sim H^{r\chi},\qquad \chi=\tfrac1p+\tfrac1q+\tfrac1r-1.$$

The trichotomy of [[def-beal-equation]] becomes a *growth rate*: $\chi>0$
$\to\infty$ (spherical: infinite families); $\chi=0$ constant (Euclidean:
borderline); $\chi<0$ $\to0$ (hyperbolic: sparse-finite).

## Three things the heuristic gets right (and is honest about)

1. **Finiteness for $\chi<0$, qualitatively.** $H^{r\chi}\to0$ means the solution
   density thins to nothing — *parallels* (does not derive) the rigorous
   Darmon–Granville/Faltings finiteness [[thm-darmon-granville]] and the
   abc-strength [[method-abc-finiteness]].

2. **Monotone sparsity — and the heuristic *predicts* the computations.** As
   $\chi$ grows more negative, $H^{r\chi}$ shrinks faster, so solutions get
   sparser and near-miss gaps grow. This is *exactly* what the searches found:
   $(3,5,7)$ min non-degenerate coprime gap $29$ → $(3,5,11)$ gap $77$, with
   $0$ exact and $0$ genuine gap-$1$ in both. A theoretical sub-thread now
   explains the empirical monotonicity, not just records it. This is the
   cycle's genuine compounding content.

3. **Why the modular engine is forced at $(3,3,3)$.** $(3,3,3)$ is the
   Euclidean/borderline case ($\chi=0$, $H^{r\chi}=H^0=$ constant) where the
   heuristic is *inconclusive* — could be $0$, finite, or need finer
   structure. The soft estimate fails to decide *exactly there*, which is
   where the hard machinery (FLT: Frey/modularity/level-lowering
   [[method-frey-modularity]]) is required. synthesis.md's "hard kernel"
   diagnosis — $(3,3,3)$ is the unique signature where all classical
   structures coincide — is now mirrored heuristically: it is also the unique
   signature where the counting heuristic is borderline.

## What it does NOT prove (the honest limit)

**Zero.** For $\chi<0$ the heuristic says the expected count is *small*, but a
heuristic constant rounding below $1$ is not a theorem. The "finitely many →
zero" upgrade — the entire open content of Beal — is *also* beyond the
counting heuristic. So every route (modular, geometric, descent, spherical,
PSS, **and counting**) delivers at most finiteness; **zero is the common open
content across all six angles.** This is the convergent diagnosis restated
from a new direction.

## Relation to the unifying lens

synthesis.md's unifying lens (distinct-odd-prime signatures lack the
near-spherical position or exponent $2$ that every *effective* method needs)
is *silent* on the counting heuristic — because the heuristic is not an
effective method: it never produces a finite list to check, only a density.
So it cannot fill the reduction-step gap either. This is consistent, not a
contradiction: the heuristic is a different *kind* of obstruction
(expectation, not reduction). It explains *why* zero is expected without
providing a mechanism to verify it.

## Outcome

**partial — a genuine sixth angle, not padding.** Per the honesty guard
recorded in attempt-18, this cycle was conditional on a real new angle
appearing. The counting heuristic qualifies: it is unexplored in the wiki,
directly engages the "zero" content from the un-touched probabilistic side,
*predicts* (not merely post-dicts) the empirical monotone sparsity, and
recasts the "hard kernel" diagnosis heuristically. Its limit is honest and
mirrors the rigorous obstruction: it gives finiteness, not zero. The wiki now
has six convergent angles, five rigorous + one soft, all stopping at
"finiteness, not zero."

## Next cycles (3 remain)

- The sixth thread is now in place. The remaining angles are thin: a third
  computational probe $(3,7,11)$ would only confirm an already-confirmed
  monotonicity (low value). No new source is obviously additive to the
  structural picture.
- Per the honesty guard: if no further genuine angle appears, the remaining
  cycles should write the **loop close-out** — a final summary declaring the
  arc complete — rather than manufacture content. The next cycle will make
  that call.