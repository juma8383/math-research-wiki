---
type: attempt
problem: birch_swinnerton_dyer
attempt: 2
date: 2026-08-24
approach: Verify the load-bearing rank-≤1 status fact against primary sources, then sharpen direction (A) — what concretely blocks a rank-≥2 Euler system
outcome: confirmed
tags: [verification, primary-source, nonvanishing, euler-system, refined-bsd, cross-problem]
---

# Attempt 02 — Verify the rank-≤1 base; sharpen the higher-rank block

Cycle-1 Continue on BSD, following attempt-01's `Next`: verify the
load-bearing status facts against primary sources, then deepen direction (A).
The verification discipline is the same one that caught Beal's (2,3,7)
spherical mislabel — it is not a formality.

## Verification: [bsd-rank-le-1-proven] — CONFIRMED (unconditional)

**Confirmed against primary sources.** The rank-$\le1$ result is fully
unconditional; no ad-hoc Heegner field is assumed. The load-bearing input is:

- **Bump–Friedberg–Hoffstein**, *Nonvanishing theorems for L-functions of
  modular forms and their derivatives*, Inventiones Math. **102** (1990),
  543–618 (DOI 10.1007/bf01233440) [[thm-bfh-murty-nonvanishing]].
- **Murty–Murty**, *Mean Values of Derivatives of Modular L-Series*, Annals
  Math. **133** (1991), 447–475 (DOI 10.2307/2944316).

These prove: for a cuspidal newform $f$ of even weight, trivial character,
functional-equation sign $\varepsilon=+1$, there exist **infinitely many**
imaginary quadratic $K=\mathbb Q(\sqrt D)$ (prime to $N$, with a prescribed
finite set $S\ni\{p\mid N\}$ splitting in $K$) such that
$L'(k/2,f\otimes\chi_D)\neq0$.

**Combined argument (the actual rank-$\le1$ engine):**
1. **Modularity** (Wiles et al.) attaches a weight-2 newform $f_E$ to $E$.
2. BFH/Murty–Murty supply a $K$ satisfying the **Heegner hypothesis** (every
   $\ell\mid N$ splits in $K$) AND the needed nonvanishing — so the existence
   of $K$ is guaranteed, not assumed.
   - $\varepsilon(E/\mathbb Q)=-1$ (analytic rank odd): Waldspurger/Murty–Murty
     give $K$ with $L(E^D/\mathbb Q,1)\neq0$; then
     $\mathrm{ord}_{s=1}L(E/K,s)=\mathrm{ord}_{s=1}L(E/\mathbb Q,s)=1$.
   - $\varepsilon(E/\mathbb Q)=+1$ (analytic rank even, i.e. 0): $K$ with
     $L(E^D/\mathbb Q,1)=0$, $L'(E^D/\mathbb Q,1)\neq0$.
3. **Gross–Zagier** (1986): $L'(E/K,1)\neq0 \iff$ the Heegner point $P_K$ is
   non-torsion [[thm-kolyvagin-gross-zagier]].
4. **Kolyvagin** (1989): $P_K$ non-torsion $\Rightarrow$ $E(K)$ rank $1$ and
   $\Sha(E/K)$ finite [[method-heegner-point-euler-system]].
5. Finiteness of $\Sha(E/K)$ $\Rightarrow$ finiteness of $\Sha(E/\mathbb Q)$
   (the restriction kernel has finite 2-torsion).

**Conclusion:** the rank-$\le1$ base in `progress.md` is correct and is
unconditional. The to-verify hedge ("vs needing an ad-hoc $K$") is resolved:
BFH/Murty–Murty remove the ad-hoc $K$. **Fact upgraded from `to-verify` to
verified.** New theory page [[thm-bfh-murty-nonvanishing]] filed (it is the
crux that makes the base unconditional and was not previously recorded).

## Sharpening: [bsd-refined-open] — p-part is further than recorded

The notes had "leading coefficient open in general, even at rank 0." Primary
sources refine this: the **$p$-part of the BSD formula** is now known under
mild conditions, though the **full exact $|\Sha|$** remains open.

- **Skinner–Urban** (2014), Iwasawa main conjecture for $\mathrm{GL}_2$
  $\Rightarrow$ $p$-part of BSD for **rank 0** (semistable $E$, $L(E,1)\neq0$,
  suitable $p$).
- **Jetchev–Skinner–Wan** (2017), $p$-part of the BSD formula for
  **analytic rank 1** ($p\ge3$ good ordinary, $\rho_{E,p}$ irreducible):
  $\mathrm{ord}_p\frac{L'(E,1)}{\Omega_E\,\mathrm{Reg}}=
  \mathrm{ord}_p\bigl(\#\Sha\cdot\prod c_\ell\bigr)$.
- **Zhang**; **Berti–Bertolini–Venerucci**: further rank-1 $p$-part cases.

So the refined picture: rank equality + Sha finiteness are proven for $r_{\rm an}\le1$;
the leading coefficient is known **one prime $p$ at a time** under conditions,
but the full $|\Sha|$ as a square integer is still conjectural. This is a
genuine refinement of `[bsd-refined-open]` (now: *full* leading coefficient
open; *p-part* largely known at rank $\le1$).

## Verification: [bsd-skinner-converse] — CONFIRMED (exists, conditional)

**Skinner**, *A converse to a theorem of Gross, Zagier, and Kolyvagin*,
Annals Math. **191**(2) (2020), 329–354 (DOI 10.4007/annals.2020.191.2.1):
under Iwasawa-theoretic hypotheses, $\mathrm{rank}\,E(\mathbb Q)=1
\Rightarrow \mathrm{ord}_{s=1}L(E,s)=1$. Refinements: **Kim** (2022), *soft
$p$-converse*, Math. Annalen (DOI 10.1007/s00208-022-02511-8). So the converse
(direction (B) ingredient) is real but conditional. To-verify item resolved.

## Frontier re-confirmed against Stein's book

Stein's BSD book (wstein.org/books/bsd/bsd.pdf): beyond rank $\le1$, *"not a
single new result directly about the [BSD rank conjecture] has been proved"*
for analytic rank $\ge2$; *"A new idea is needed"* (N. Katz). This matches the
`progress.md` frontier exactly and is now primary-source-backed.

## Deepening direction (A): the concrete block on a rank-≥2 Euler system

The verification sharpened *why* direction (A) is stuck. A rank-$r$ Euler
system needs **two** things, and the literature confirms neither exists:

1. **Higher-derivative Gross–Zagier / a supply of $r$ independent points.**
   One needs $r_{\rm an}$ independent Heegner-type points whose heights relate
   to $L^{(r)}(E,1)$ (Yuan–Zhang–Zhang higher Gross–Zagier). Gross–Zagier gives
   the **first** derivative only; higher-derivative formulae exist but do not
   by themselves bound the Selmer group.
2. **A "rank-$\ge2$-shaped" Kolyvagin system.** Kolyvagin's Euler system is
   built from a **single** Heegner point: the derived cohomology classes
   $c_\lambda\in H^1(K,E[M])$ bound a Selmer group of rank **$\le1$**. There is
   no known multi-point / multi-variable Kolyvagin system bounding a rank-$r$
   Selmer group to size $r_{\rm an}$. This is the *control-step* obstruction,
   precisely parallel to Beal: the resolution tools (descent, heights, GZ,
   Kolyvagin) all work; the **control mechanism** (a Selmer bound of the right
   rank-shape) does not exist for $r\ge2$.

**The named unproven target stays Kolyvagin's own higher-rank Conjectures
(3.32–3.35 in Stein)** [bsd-kolyvagin-conj] — nonvanishing of the higher
cohomology classes that a rank-$r$ system would need. Confirming the
one-point shape limit of the existing engine (the "one-dimensional engine
stops" sub-pattern, now 6-for-6 across the problems).

## Honesty note on a preprint

A Zenodo preprint *"Unconditional Proof of the Rank Equality of BSD — Based on
Kato's Finiteness and Group Isomorphism Reduction"* (DOI 10.5281/zenodo.20716916)
appears in the search results. **NOT peer-reviewed, NOT community-accepted**;
flagged `bsd-recent-claims-unverified` (same discipline as YM/Hodge/Collatz
preprint flurries). Not used as established fact.

## Outcome

`confirmed` for the verification goal (rank-$\le1$ base now primary-source
verified, two to-verify items resolved, refined-$p$-part picture sharpened);
`partial` for the conjecture overall (no progress on rank $\ge2$ — that remains
the frontier). Direction (A) block concretized: need a multi-point
Kolyvagin system + higher-derivative GZ; neither exists; Kolyvagin Conjectures
3.32–3.35 the named target.

## Files touched

- New: `theory/theorems/bfh-murty-nonvanishing.md` (the nonvanishing input
  making rank-1 unconditional — previously unrecorded load-bearing theorem).
- Updated: `progress.md` (to-verify items resolved; refined picture; direction
  (A) block concretized), `index.md`, `log.md`.

## Next (attempt-03)

Either (i) verify `[bsd-parity-proven]` against Nekovář / Dokchitser–Dokchitser
(the remaining to-verify), or (ii) push direction (A) concretely: survey the
**higher Gross–Zagier** (Yuan–Zhang–Zhang) + **Beilinson–Flach** / Kato
derivative literature for the closest existing rank-2-shaped system and
diagnose exactly where its Selmer bound falls short of rank 2.