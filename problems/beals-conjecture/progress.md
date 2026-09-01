# Progress — Beal's Conjecture

> Running state of the attack. Read this first when resuming. For the
> consolidated *structural* picture (the obstruction map, what a proof
> requires, computational state, attempt index) see [synthesis.md](synthesis.md)
> — this file is the current frontier in brief; synthesis is the durable
> handoff. Consolidated current through attempt-24 (cross-problem loop cycle 22).

## Where Beal actually stands (sourced [[rg2024]])

1. **Beal ≠ Fermat–Catalan** [rg2024-fc-vs-beal]. Fermat–Catalan = finiteness
   across signatures (may include a 2); Beal = *zero* when $\min\geq3$.
   Distinct conjectures. The 10 known primitive Fermat–Catalan solutions all
   have a $2$ [rg2024-10-solns] — none is a Beal counterexample.
2. **Computationally verified to $z^r\leq2^{100}$** [rg2024-comp-bound].
3. **Solved signatures all have a repeated odd exponent**
   [[thm-solved-generalized-fermat-signatures]]: $(p,p,p)$, $(n,n,3)$,
   $(3,3,n)$ ($n\leq10^9$), $(5,5,7),(5,5,19),(7,7,5)$, $(3,4,5)$,
   $(2j,2k,n)$-family. **No solved Beal signature has three pairwise-distinct
   odd-prime exponents.**

## The exact frontier: $(3,5,7)$

[rg2024-357-smallest] The smallest open Beal signature is **$(3,5,7)$**
($1/3+1/5+1/7<1$, three pairwise-distinct odd primes). The open region is
precisely the **all-distinct-odd-prime** signatures
$\{(3,5,7),(3,5,11),(3,7,11),\dots\}$.

## The entire open content = "finitely many → zero"

Darmon–Granville [[thm-darmon-granville]] gives, unconditionally, *finitely many*
primitive solutions per signature with $1/p+1/q+1/r<1$ (via Faltings). The abc
conjecture gives no more than this [[method-abc-finiteness]]. **Beal's open
content is exactly the upgrade "finitely many → zero" per signature.** No
existing theorem or heuristic makes that upgrade for any distinct-prime
signature.

## The obstruction: five rigorous threads + one soft angle (6 total)

Every classical tool breaks at $(3,5,7)$, each for an independent reason; a
sixth *soft* angle converges on the same wall from the probabilistic side. Full
table in synthesis.md; in brief:

| # | angle | needs | why (3,5,7) breaks it |
|---|---|---|---|
| 1 | Frey/modularity/Ribet [[method-frey-modularity]] | one $\ell$ strips all bad primes | $\ell\mid2\gcd(p,q,r)=2$, only $\ell=2$; useless |
| 2 | Darmon program [[method-darmon-program]] | repeated-exponent signature | distinct-prime only *classified*; + wide-open generalized-Mazur |
| 3 | Mordell lens [[method-mordell-curve-lens]] | genus 1 | $(3,5,7)\to$ genus 4 (Faltings only) |
| 4 | Infinite descent [[method-infinite-descent]] | cyclotomic factorization of $x^p+y^q$ | no factorization for $p\neq q$ |
| 5 | Spherical reduction [[method-spherical-reduction]] | even exponent → spherical $(2,\cdot,\cdot)$ | no even exponent; reduction unwritable |
| 6* | Counting heuristic [[method-counting-heuristic]] *(soft)* | controlled constant <1 | gives "small expected count" ($H^{r\chi}\to0$); finiteness, **not zero** |

## The unifying lens (attempt-14/17, corrected)

Every *effective* method at a hyperbolic signature needs either a **near-spherical
position** ($\chi=1/p{+}1/q{+}1/r-1$ close to $0$, giving a distinguished finite
triangle-group quotient) **or an exponent $2$** (giving an $X(r)$ modular-curve
interpretation). $(3,5,7)$ is **deeply hyperbolic** ($\chi=-34/105$) **with no
exponent $2$** → it has neither. The one effective precedent at a hyperbolic
signature — PSS $x^2+y^3=z^7$ [[pss2007]] [[method-triangle-group-descent]] —
works via the finite quotient $\mathrm{PSL}_2(\mathbb F_7)$ of the *infinite*
$\Delta(2,3,7)$, enabled by $(2,3,7)$'s near-spherical position ($\chi=-1/42$)
*and* its exponent $2$. *(Correction, attempt-17: $(2,3,7)$ is hyperbolic, not
spherical — $41/42<1$; the earlier "spherical" label was a factual error, now
fixed across the wiki.)* The obstruction is at the **reduction** step, not the
resolution step: Chabauty / effective Faltings / Mordell–Weil sieve all work
and finished the solved cases; the missing piece is *getting from the equation
to finitely many curves to resolve* without using a shared/even/spherical
structure.

## What a proof of $(3,5,7)$ would require

> A reduction-to-finite-curves mechanism that uses **none** of {shared
> exponent, even exponent, spherical parametrization}.

Two candidate directions (attempt-11, refined 14/17):
- **(A) Modular:** extend Darmon's Frey-variety method to three distinct primes
  *and* prove Darmon Conjecture 1.2 (generalized-Mazur irreducibility, wide open
  [[dv2022-irreduc-conjecture]]). "Two programs away."
- **(B) Geometric:** an *effective* finiteness mechanism not relying on a finite
  triangle group. The Darmon–Granville reduction *exists* but is ineffective;
  PSS made it effective only via the near-spherical + exponent-$2$ structure
  $(3,5,7)$ lacks. Not a transplant of an existing theorem; a major open project.

Ruled out as recapitulating a known wall: abc (finiteness only), cleverer
descent (no factorization exists), density/metric ("tight-by-1" refutes —
Ramanujan $9^3+10^3=12^3+1$), "just compute the Faltings set" (ineffective; that
*is* the missing reduction).

## Empirical state — five signatures, prediction confirmed (monotone; rate erratic, NOT smooth in −χ)

| signature | $\chi$ | exact (coprime) | genuine gap-1 | min coprime gap |
|---|---|---|---|---|
| $(3,5,7)$  | $-0.324$ | 0 | 0 (all degenerate on $t^{21}{+}1,t^{35}{+}1$) | 29 |
| $(3,5,11)$ | $-0.376$ | 0 | 0 (all degenerate on $t^{33}{+}1,t^{55}{+}1$) | 77 |
| $(3,7,11)$ | $-0.433$ | 0 | 0 (all degenerate on $t^{33}{+}1$) | 277 |
| $(5,7,11)$ | $-0.566$ | 0 | 0 (all degenerate on $t^{55}{+}1$) | **288** |
| $(5,7,13)$ | $-0.580$ | 0 | 0 (only $t{=}1$ degenerate in box) | **1771** |

The min gap grows monotonically with $-\chi$ ($29<77<277<288<1771$) — and this
was **predicted** by the counting heuristic (attempt-19) *before* $(3,7,11)$ was
computed (attempt-20), then **confirmed** there, **re-confirmed** at
$(5,7,11)$ (attempt-23), and **re-confirmed again** at $(5,7,13)$ (attempt-24,
cross-problem loop cycle 22). The non-coprime exact hit at $(3,7,11)$,
$(128,8,4)$ ($\gcd=4$), is Beal-consistent (a non-counter-example).
**attempt-23 nuance (four points):** the growth **decelerated sharply** — the
largest $-\chi$ step ($+0.133$, $(3,7,11)\to(5,7,11)$) gave the smallest gap
step ($+11$, $277\to288$); trend monotone but **sub-linear in $-\chi$**. The
$(5,7,11)$ min sits at the small base $(A,B,C)=(11,4,3)$: $11^5{+}4^7{-}3^{11}=288$.
**attempt-24 correction (five points) — the deceleration REVERSES:** at
$(5,7,13)$ the **smallest** $-\chi$ step ($+0.014$; $p,q$ fixed, only
$r{:}11\to13$) gives by far the **largest** gap step ($+1483$, a $6.1\times$
jump, $288\to1771$) at $(A,B,C)=(6,3,2)$: $6^5{+}3^7{-}2^{13}=1771$. So the
trend stays **monotone** but the rate is **erratic, not a smooth function of
$-\chi$** — the attempt-23 "sub-linear" framing (based on four points) is
**refuted** by the fifth: the min gap is governed by **exponent-specific
small-base arithmetic** (the $C^r$ granularity near small $A^p{+}B^q$; the min
sits at the smallest $C,A$ corner where 5th-power spacing $\sim A^4$ is
smallest), **not** by the scalar $\chi$. The qualitative Beals prediction
("coprime near-misses get rarer as the signature grows more hyperbolic")
survives; any smooth quantitative $\chi\mapsto\mathrm{gap}$ law does not.
Scripts: `search.py`, `search_357.py`, `search_357_nearmiss.py`,
`search_3511.py`, `search_3711.py`, `search_5711.py`, `search_5713.py`,
`mordell_check.py`. All searches are box-limited; minima sit at small bases
($C=2$ or $3$), so boxes likely contain the genuine minima (attempt-24's 1771
flagged `to-verify` by a wider-box run).

**attempt-25 CORRECTION (2026-08-31; supersedes parts of the table and the
monotone claims above, which are retained for the record):**
`search_3711.py`/`search_5711.py` have an overshoot-exclusion bug (break at
$B^Q>C^R$; skip $\mathrm{rem}<2^p$) — the true minima are **147** at $(3,7,11)$
($(2,3,2)$: $2^3{+}3^7{-}2^{11}=147$) and **171** at $(5,7,11)$ ($(2,3,2)$:
$2^5{+}3^7{-}2^{11}=171$); 277/288 were rank-4/rank-2 values. The
"monotone in $-\chi$" law is **REFUTED** by the corrected 56-signature table:
$51<77$ at $((3,5,13)$ vs $(3,5,11))$ despite more-negative $\chi$, and
$1281/831/860$ non-monotone in $r$ at fixed $(3,5)$. Corrected table:
all 56 distinct-odd-prime signatures from primes $\le23$, box
$C\le60$, $B\le10^4$ (`scripts/near_miss_package.py`, 66s, data in
`near_miss_package_data.json`) — **Corner Principle verified 56/56** (min
genuine gap always at $C\le3$; $C=2$ for 55, $C=3$ only at $(5,11,13)$);
**0 genuine gap-1 hits** in the whole scanned open class; boundary: the
principle fails at $(3,3,3)$ ($G=2$ at $(5,6,7)$, 4 genuine gap-1s) and
$(3,3,5)$ ($G=2$ at $(239,271,32)$: $271^3{+}239^3=2^{25}{-}2$), holds at
$(3,3,7)$/$[3,5,5)$ ($\gamma=7/3$) — failure boundary at granularity exponent
$\gamma=1-r\chi\le5/3$, open class $\gamma\ge3.267$ strictly above it.
**Theorem (attempt-25/T1):** all unit-base gap-(+1) near-misses lie exactly on
the two universal families (global, elementary); **the −1 channel is exactly
odd-odd Pillai-2** (new conjecture [[odd-odd-pillai-2]], verified to
$10^{18}$ + everywhere locally soluble). Full preprint draft:
[papers/beal-near-miss-stratification.md](../../papers/beal-near-miss-stratification.md).

## Attempt log (01–20)

- **01** reductions + tight-by-1 + frontier map; **02** ingest literature,
  exact frontier $(3,5,7)$, classical method provably blocked; **03** Darmon
  program = repeated-exponent only, + wide-open irreducibility; **04** $(3,5,7)$
  probe (0 exact, degenerate near-misses); **05** Mordell lens verified,
  cubic-only (genus barrier); **06** descent 3-requirement analysis; **07**
  neighbors check — $(3,5,7)$ is the solved/open boundary; **08** Siksek–Stoll
  $(3,4,5)$ route, doubly gated, 5th thread; **09** synthesis page; **10** Lint 1
  (orphan fixed, tools rebuilt); **11** forward-looking: obstruction at
  reduction not resolution, 2 directions; **12** exhaustive $(3,5,7)$ gap-1
  (all degenerate, 0 genuine, min gap 29); **13** $(3,5,11)$ (same pattern, min
  gap 77, monotone); **14** direction (B) literature check + triangle-group
  lens (correction to attempt-11); **15** Lint 2; **16** synthesis close-out
  consolidation; **17** PSS verified vs paper, caught + corrected the
  $(2,3,7)$ spherical mislabel (4 files); **18** final Lint (correction
  consistency, 1 stale index line fixed); **19** counting heuristic (6th angle,
  soft, predicts monotone sparsity); **20** $(3,7,11)$ — prediction confirmed
  (min gap 277). See synthesis.md for the attempt-index table with outcomes.
  **21** progress consolidation; **22** loop close-out (20-cycle arc complete).
  **23** (cross-problem loop cycle 6) fourth signature $(5,7,11)$ — prediction
  re-confirmed (min gap 288), but growth **decelerated sharply** ($+11$ vs prior
  $+200$ despite a larger $-\chi$ step); trend monotone but sub-linear in $-\chi$.
  Script `search_5711.py`.
  **24** (cross-problem loop cycle 22) fifth signature $(5,7,13)$ — prediction
  re-confirmed (min gap 1771 ≫ 288 at $(6,3,2)$, $6^5{+}3^7{-}2^{13}=1771$), but
  the attempt-23 **deceleration REVERSES**: smallest $-\chi$ step ($+0.014$)
  gives largest gap step ($+1483$, $6.1\times$). Trend **monotone** but rate
  **erratic, not smooth in $-\chi$** — min governed by exponent-specific
  small-base arithmetic, not the scalar $\chi$. Append-only correction of the
  four-point "sub-linear" framing. Script `search_5713.py`.
  **25** (2026-08-31, ultracode session) near-miss stratification theorem
  (T1-T4: universal families classify unit-base gap-+1 near-misses globally;
  −1 channel = odd-odd Pillai-2) + corrected 56-signature table (bug fix:
  277→147, 288→171; scripts `search_3711.py`/`search_5711.py` deprecated) +
  Corner Principle (56/56, failure boundary at $\gamma\le5/3$) + monotone-law
  refutation; adversarially verified (novelty/soundness/referee survive);
  preprint draft `papers/beal-near-miss-stratification.md`. Scripts
  `near_miss_package.py`, `near_miss_robustness.py`, `audit_corrected_scan.py`.

## Honesty check

No proof of Beal. No proof of even $(3,5,7)$. The "breakthrough" is
*diagnostic and structural*: a 30-year open problem converted into a precisely
mapped frontier — the exact obstruction (reduction step, not resolution), the
unifying lens (deep hyperbolicity + no exponent 2), six convergent angles (five
rigorous + one soft), a falsifiable heuristic prediction that was confirmed,
and two concrete (major) forward directions. That compounds: a future session
resumes by extending this map — picking up direction (A) or (B), or ingesting a
new source against the stable claim tags — not by re-deriving it.