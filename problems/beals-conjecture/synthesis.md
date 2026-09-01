---
type: synthesis
problem: beals_conjecture
title: State of the attack — the five-thread obstruction map
date: 2026-08-24
status: current
tags: [synthesis, obstruction-map, frontier, state-of-attack]
---

# State of the attack on Beal's conjecture

> **CORRECTION 2026-08-31 (attempt-25; supersedes specific numbers below,
> text retained for the record).** The gap values 277 and 288 recorded below
> (and in attempts 20/23) were computed by scripts with an
> overshoot-exclusion bug (`search_3711.py`/`search_5711.py`, now
> deprecated): the true min genuine coprime gaps are **147** at $(3,7,11)$
> ($(2,3,2)$: $2^3{+}3^7{-}2^{11}$) and **171** at $(5,7,11)$ ($(2,3,2)$:
> $2^5{+}3^7{-}2^{11}$). The "monotone in $-\chi$" trend
> ($29<77<277<288<1771$) is **refuted** by the corrected 56-signature table
> (e.g. 51 at $(3,5,13)$ < 77 at $(3,5,11)$ despite more-negative $\chi$).
> The empirical "all gap-1 hits lie on the universal families" observation is
> now a **theorem** ([[thm-near-miss-stratification]] T1; the −1 side is
> exactly [[odd-odd-pillai-2]]), and the min-gap behavior is governed by the
> [[corner-principle]] (verified 56/56). See
> `attempts/attempt-25.md` and the preprint draft
> `papers/beal-near-miss-stratification.md`.

A consolidated reference. Read `progress.md` for the running frontier; this page
is the *structural* picture distilled from attempts 01–08, frozen for
cross-session continuity.

## The problem, reduced

Beal's conjecture: if $A^x+B^y=C^z$ with $x,y,z\geq3$, then $\gcd(A,B,C)>1$.
Equivalent (via [[method-pairwise-coprime-reduction]]) to: **no pairwise-coprime
solution with exponents $\geq3$.** And (via [[method-exponent-reduction]]) it
suffices to rule out exponents in $\{$odd primes$\}\cup\{4\}$.

## The exact frontier: signature $(3,5,7)$

$(3,5,7)$ — $1/3+1/5+1/7<1$, three pairwise-distinct odd primes — is the smallest
open Beal signature [[rg2024-357-smallest]]. Every smaller signature is solved:
repeated-exponent neighbors $(3,3,7)$, $(5,5,7)$, $(3,5,5)$ are all zero
[[thm-solved-generalized-fermat-signatures]]; signatures involving a $2$ are
outside Beal's regime. So $(3,5,7)$ sits exactly on the solved/open boundary,
with the open region being precisely the **all-distinct-odd-prime** signatures
$\{(3,5,7),(3,5,11),(3,7,11),(5,7,11),\dots\}$.

## The entire open content = "finitely many → zero"

Darmon–Granville [[thm-darmon-granville]] gives, unconditionally, *finitely many*
primitive solutions per signature with $1/p+1/q+1/r<1$ (via Faltings). The
abc conjecture gives no more than this [[method-abc-finiteness]]. **Beal's open
content is exactly the upgrade "finitely many → zero" per signature.** No
existing theorem makes that upgrade for any distinct-prime signature.

## The obstruction map: five rigorous threads + one soft angle

Every classical tool breaks at $(3,5,7)$, each for an *independent* reason.
A sixth, *soft* (heuristic) angle converges on the same wall from the
probabilistic side:

| # | thread | page | structure it needs | why $(3,5,7)$ breaks it |
|---|---|---|---|---|
| 1 | Frey curve / modularity / Ribet | [[method-frey-modularity]], [[method-frey-level-lowering-obstruction]] | one level-lowering prime $\ell$ strips all bad primes | $\ell\mid2\gcd(p,q,r)=2$, so only $\ell=2$; useless (parity; Mazur needs $\ell$ large) |
| 2 | Darmon program (Frey abelian varieties, GL₂-type) | [[method-darmon-program]] | a *repeated-exponent* signature | distinct-prime signatures only *classified* (Remark 2.4), no working method; AND gated on the wide-open generalized-Mazur irreducibility conjecture |
| 3 | Mordell-curve lens | [[method-mordell-curve-lens]] | genus 1 (cubic-cubic) | $(3,5,7)$ → genus 4 (Faltings only) |
| 4 | Infinite descent (FLT $n=3,4$) | [[method-infinite-descent]] | cyclotomic factorization of $x^p+y^q$ | no factorization when $p\neq q$; descent cannot begin |
| 5 | Spherical reduction (Siksek–Stoll $(3,4,5)$ route) | [[method-spherical-reduction]] | an even exponent → a spherical $(2,\cdot,\cdot)$ signature | no even exponent; the reduction cannot be written (and even $(3,4,7)\to(2,3,7)$ is hyperbolic, not parametrized) |
| 6* | Counting heuristic *(soft, not rigorous)* | [[method-counting-heuristic]] | a controlled constant to round the expected count below $1$ | gives only "small expected count" ($H^{r\chi}\to0$); finiteness, **not zero** — and not even rigorous finiteness |

Thread 6* is marked with an asterisk because it is a different *kind* of
angle: it produces an expectation (density $\sim H^{r\chi}$), not a reduction
to finitely many curves. It therefore cannot fill the reduction-step gap the
other five hit — but it independently confirms the convergent conclusion
("finiteness, not zero") and *predicts* the monotone sparsity the computations
observe ($(3,5,7)$ gap $29\to(3,5,11)$ gap $77$). It also explains
heuristically why $(3,3,3)$ ($\chi=0$, the borderline Euclidean case where
$H^{r\chi}=H^0$ is a constant) is exactly where the soft estimate is
inconclusive and the hard modular engine is forced.

## Why $(3,5,7)$ is the hard kernel, not "the next case"

The cubic-cubic-cubic signature $(3,3,3)$ is the **unique** signature where all
classical structures coincide: genus 1 (Mordell), cyclotomic UFD factorization
(Euler descent), self-power match (FLT's $z^p$), and the modular method's
single-prime level lowering. Every departure breaks at least one structure:
- $(p,p,r)$, $r\neq p$: descent breaks at "factor-power = RHS-power" (this is
  *why* $(p,p,r)$ needed the modular method, not descent).
- $(p,q,r)$ distinct: breaks *all five*.

So the boundary between solved and open is not arbitrary — it is exactly the
**factorization / no-factorization** divide, confirmed from five threads.
Attempt-14/17 add a *unifying* lens: every effective method at a hyperbolic
signature needs either a near-spherical position ($\chi=1/p{+}1/q{+}1/r-1$
close to $0$, giving a distinguished finite triangle-group quotient) **or** an
exponent $2$ (giving an $X(r)$ modular-curve interpretation). $(3,5,7)$ is
**deeply hyperbolic** ($\chi=-34/105$) **with no exponent $2$**, so it has
neither. (Correction, attempt-17: $(2,3,7)$ — the one hyperbolic signature PSS
solved — is itself hyperbolic, $\chi=-1/42$, not spherical; it worked via the
finite quotient $\mathrm{PSL}_2(\mathbb F_7)$ of the *infinite* $\Delta(2,3,7)$,
enabled by its near-spherical position and its exponent $2$.) The five threads
are thus five symptoms of one underlying structural absence at
distinct-odd-prime signatures: no $2$ and no near-spherical finite structure.

## What a proof of $(3,5,7)$ would require (honest assessment)

**The obstruction is at the reduction step, not the resolution step.** Across
all five threads the failure is *not* in proving a result on a given curve
(Chabauty, effective Faltings, Mordell–Weil sieve all work — and that is how
the solved cases were finished) but in *getting from the equation to finitely
many curves to resolve*. Every existing reduction-to-finite mechanism relies on
a shared exponent, an even exponent, or a spherical parametrization;
$(3,5,7)$ has none. So the one-sentence need:

> A proof requires a **reduction-to-finite-curves mechanism that uses none of
> {shared exponent, even exponent, spherical parametrization}**.

Two candidate directions (attempt-11, refined by attempt-14):
- **(A) Modular:** extend Darmon's Frey-variety modular method to three-distinct
  primes **and** prove Darmon Conjecture 1.2 (generalized-Mazur irreducibility,
  wide open [[dv2022-irreduc-conjecture]]). "Two programs away," most principled.
- **(B) Geometric:** a reduction of $(3,5,7)$ to finitely many genus-$\geq2$
  curves, then effective Chabauty. *Refinement (attempt-14, corrected 17):* the
  reduction **already exists** — Darmon–Granville's covering descent
  (Chevalley–Weil + Faltings) — but is **ineffective**. The one effective
  instance (Poonen–Schaefer–Stoll, $x^2+y^3=z^7$) used nonabelian descent via the
  **finite quotient** $\mathrm{PSL}_2(\mathbb F_7)$ of the *infinite* triangle
  group $\Delta(2,3,7)$ (the Klein quartic / $X(7)$), enabled by $(2,3,7)$'s
  **near-spherical** position ($\chi=-1/42$) **and its exponent $2$** (the
  modular-curve interpretation). $(3,5,7)$ is **deeply hyperbolic**
  ($\chi=-34/105$) **with no exponent $2$** → no known finite-quotient descent
  and no modular-curve interpretation → the PSS technique is unavailable
  [[method-triangle-group-descent]]. So direction (B) is gated on the same
  "needs a $2$" structure as threads 1 and 5; it is not the independent escape
  route attempt-11 hoped.

Ruled out as recapitulating a known wall: abc (finiteness only), cleverer
descent (no factorization exists), density/metric ("tight-by-1" refutes), and
"just compute the Faltings set" (ineffective; that *is* the missing reduction).

## Computational state

- General Beal search (bases $\le120$, exponents $\{3,4,5,7\}$): 0 coprime
  exact solutions; "tight-by-1" (coprime triples can land exactly 1 below a
  $\geq3$-power — Ramanujan $9^3+10^3=12^3+1=1729$), so metric/density arguments
  cannot prove Beal.
- $(3,5,7)$ signature search ($A\le6000,B\le600,C\le200$): 0 exact solutions;
  gap-1 near-misses all *degenerate* (one base $=1$) from universal families
  $t^{21}+1$, $t^{35}+1$; smallest non-degenerate coprime near-miss is gap 29
  (attempt-04; *exhaustively* classified in attempt-12: 4 gap-1 hits, all
  degenerate + on a universal family, 0 genuine).
- $(3,5,11)$ signature probe (attempt-13): same pattern — 0 exact, 0 genuine
  gap-1, all gap-1 degenerate on the generalized universal families
  $t^{33}+1$, $t^{55}+1$; min non-degenerate coprime gap 77 at $(12,3,2)$. The
  rigidity is **uniform across the open class and monotone in the exponents**
  ($29\to77$). (General fact: the degenerate families are
  $t^{\operatorname{lcm}(p,r)}{+}1$ and $t^{\operatorname{lcm}(q,r)}{+}1$ for any
  $(p,q,r)$.)
- $(3,7,11)$ signature probe (attempt-20): the counting-heuristic prediction
  *tested*. $\chi=-100/231\approx-0.433$ (most negative of the three) → min
  non-degenerate coprime gap **277** at $(13,2,2)$, exceeding $77$ as predicted;
  monotone trend $29<77<277$ tracks $-\chi$ ($-0.324>-0.376>-0.433$). 0 coprime
  exact (the one hit $(128,8,4)$ has $\gcd=4$, Beal-consistent), 0 genuine gap-1,
  gap-1's degenerate on $t^{33}+1$. **The heuristic survived its falsification
  test**; the empirical line now spans three signatures.
- Survey verification to $z^r\le2^{100}$ [[rg2024-comp-bound]].
- Mordell birational equivalence $x^3+y^3=N\leftrightarrow Y^2=X^3-432N^2$
  verified exactly (`scripts/mordell_check.py`).
- Honest scope: all searches are box-limited; genuine gap-1 with large bases is
  not ruled out, but small-base concentration makes the box likely to contain
  the genuine minima.

## Open to-verify items (minor)

- Exact UFD boundary of $\mathbb Z[\zeta_p]$ (thread 4; first irregular prime
  $37$) — does not affect the $(3,5,7)$ conclusion.
- Siksek–Stoll $(3,4,5)$ computational step — verify the reconstructed mechanism
  (reduce → parametrize → impose-square → Chabauty) against the paper; the
  structural gate (needs even exponent + spherical landing) is robust
  regardless.
- Poonen–Schaefer–Stoll mechanism — the `pss2007` source page was ingested from
  a search-result summary; verify the PSL₂(F₇)/Klein-quartic descent details
  against the paper. The spherical-triangle-group finiteness criterion is
  standard and robust regardless.
- Composite-exponent signatures $(3,4,n)$, $n\ge7$: subsumed by the survey's
  "smallest open = $(3,5,7)$" claim; structurally the spherical-reduction route
  does not reach them (hyperbolic reduction).

## Index of attempts

| attempt | cycle | thread | outcome |
|---|---|---|---|
| 01 | — | reductions + computational obstruction + frontier map | partial |
| 02 | — | ingest literature; exact frontier $(3,5,7)$; classical method provably blocked | breakthrough-diagnostic |
| 03 | 1/20 | ingest Darmon's program; repeated-exponent only | partial |
| 04 | 2/20 | computational $(3,5,7)$ probe | partial |
| 05 | 3/20 | Mordell-curve lens, verified; cubic-only | partial |
| 06 | 4/20 | descent; 3 requirements; convergent 4-thread diagnosis | partial |
| 07 | 5/20 | neighbors check; $(3,5,7)$ = solved/open boundary | confirmed |
| 08 | 6/20 | Siksek–Stoll route; doubly gated; 5th thread | partial |
| 09 | 7/20 | synthesis page (this map) | partial |
| 10 | 8/20 | Lint pass 1: orphan fixed, tools list rebuilt | confirmed |
| 11 | 9/20 | forward-looking: obstruction at reduction not resolution; 2 directions | partial |
| 12 | 10/20 | exhaustive $(3,5,7)$ gap-1 classification; min genuine gap 29 | confirmed |
| 13 | 11/20 | $(3,5,11)$ probe; rigidity uniform & monotone across open class | confirmed |
| 14 | 12/20 | direction (B) literature check; correction (DG descent exists, ineffective); triangle-group lens | partial |
| 15 | 13/20 | Lint pass 2: superseded-claim marked append-only; clean | confirmed |
| 16 | 14/20 | close-out consolidation of synthesis (unifying lens, computational state, bottom line) | partial |
| 17 | 15/20 | verify PSS vs paper; all claims confirmed; caught & corrected (2,3,7) spherical mislabel | confirmed |
| 18 | 16/20 | final Lint: correction consistency; 1 stale index line fixed; clean | confirmed |
| 19 | 17/20 | counting heuristic (sixth angle, soft); predicts monotone sparsity; finiteness not zero | partial |
| 20 | 18/20 | (3,7,11) probe; tested the heuristic prediction (min gap 277 > 77 > 29); confirmed | confirmed |
| 21 | 19/20 | consolidate progress.md to full 20-attempt state (read-first file current) | confirmed |
| 22 | 20/20 | loop close-out; arc declared complete; resume point recorded | partial |

## Bottom line

No proof of Beal, and no proof of even $(3,5,7)$. The breakthrough is
*diagnostic and structural*: a 30-year open problem converted into a precisely
mapped frontier. After 22 attempts (20 substantive + 2 consolidation/close-out) the picture is:

- **The frontier** is the all-distinct-odd-prime class, with $(3,5,7)$ least.
- **The open content** is exactly "finitely many → zero" per signature.
- **The obstruction** is at the *reduction* step, not the resolution step: every
  reduction-to-finite mechanism exploits a structure (shared exponent, even
  exponent, or spherical/finite triangle group) that distinct-odd-prime
  signatures lack. Five rigorous threads fail for five distinct reasons, all
  unified by the hyperbolic (no-finite-group) nature of $(3,5,7)$; a sixth
  *soft* angle (the counting heuristic, $\sim H^{r\chi}$) converges on the same
  wall from the probabilistic side — it gives finiteness, not zero, and
  *predicts* the monotone sparsity the computations observe.
- **Empirically**, the rigidity is uniform across the open class and monotone in
  the exponents ($(3,5,7)$ min gap 29, $(3,5,11)$ min gap 77, $(3,7,11)$ min gap
  277; 0 coprime exact, 0 genuine gap-1 in all three) — and this monotonicity was
  *predicted* by the counting heuristic ($\chi$ more negative → $H^{r\chi}$
  shrinks faster) and *confirmed* at $(3,7,11)$ after the prediction was made.
- **What a proof would need**: either (A) extend Darmon's Frey-variety modular
  method + prove generalized-Mazur irreducibility, or (B) an *effective*
  finiteness mechanism not relying on a finite triangle group — neither is a
  transplant of an existing theorem; both are major open projects.

The compounding artifact is this map itself. A future session resumes not by
re-deriving but by extending it — e.g. by picking up direction (A) or (B), or by
ingesting a new source against the stable claim tags.