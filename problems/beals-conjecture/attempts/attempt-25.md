---
type: attempt
problem: beals-conjecture
attempt: 25
date: 2026-08-31
approach: near-miss stratification theorem (T1-T4) + odd-odd Pillai-2 conjecture + corrected 56-signature min-gap table + Corner Principle; adversarially verified breakthrough-hunt candidate
outcome: partial
tags: [near-miss, gap-1, pillai, universal-families, corner-principle, correction, computational]
---

# Attempt 25 — The near-miss stratification: theorem, conjecture, corrected table

**This attempt converts five attempts of empirical near-miss observation
(12/13/20/23/24) into a theorem-plus-conjecture package, and corrects two
recorded values (a real bug) plus one recorded law (refuted by corrected
data). The full write-up is the draft preprint
[../../papers/beal-near-miss-stratification.md](../../papers/beal-near-miss-stratification.md).**

## Theorem (stratification of unit-base gap-1 near-misses)

For a signature $(p,q,r)$ of distinct primes, a *unit-base* triple has some
base $=1$, and the *universal families* are
$\mathcal{F}_1=\{(t^r,1,t^p)\}$, $\mathcal{F}_2=\{(1,t^r,t^q)\}$ (gap $+1$
identically).

- **T1 (unconditional, global).** Every unit-base gap-(+1) near-miss lies
  exactly on $\mathcal{F}_1\cup\mathcal{F}_2$ (and every family member is
  one). One-paragraph proof: $B=1\Rightarrow A^p=C^r\Rightarrow A=t^r, C=t^p$
  by $\gcd(p,r)=1$ + UFD; symmetric for $A=1$; $C=1\Rightarrow A=B=1$.
  *This turns attempts 12/13/20/23/24's empirical "all gap-1 hits lie on the
  universal families" into a theorem.*
- **T2 (exact reduction).** The unit-base gap-(−1) channel is exactly
  $X^r-Y^p=2$ and $X^r-Y^q=2$ — i.e. Pillai's $k=2$ equation restricted to
  the signature's odd primes.
- **T3 (raw-metric bound).** Quasi-degenerate triples ($A^p=C^r$ or
  $B^q=C^r$) force raw min gap $\le 2^{\min(p,q)}$ (at $(2,3^r,3^q)$ /
  $(3^r,2,3^p)$, $t=3$) — any metric not excluding this layer measures the
  layer. Also $\gcd(t^r,B,t^p)=\gcd(t,B)$.
- **T4 (even boundary, conditional on Cohn 1993 / BMS 2006 [attribution
  to-verify vs LeVeque 1952 / Siksek 2003]).** With an exponent $2$: the
  $B=1$ sub-channel is $x^2+2=y^n$, completely solved — unique solution
  $5^2+2=3^3$ — so it exists only at signatures $(2,q,3)$ via the single
  identity $(5,1,3)$; the $A=1$ sub-channel is odd-odd Pillai-2 again. So
  Beal's all-odd restriction removes precisely the surviving identity.

## New conjecture (odd-odd Pillai-2)

$X^u-Y^v=2$ has no solutions with $u,v$ both odd primes (a named restriction
of the famous open $k=2$ Pillai case — Waldschmidt's survey; NOT a new
equation). Evidence (this session, `scripts/near_miss_package.py`):
no solutions with $Y^v\le10^{18}$ over all ordered odd-prime pairs $\le23$
(1,004,437 powers checked); **everywhere locally soluble** (no obstructing
modulus $m\le1000$, no prime power $\le10^6$) → Catalan-like, not refutable
by congruences. Under it, Prop: universal families are the ONLY unit-base
gap-1 near-misses of every open signature, globally. Filed as
[[odd-odd-pillai-2]].

## CORRECTIONS (append-only; supersede recorded values)

1. **search_3711.py / search_5711.py have an overshoot-exclusion bug** (break
   at $B^Q> C^R$; skip $\mathrm{rem}<2^p$). Corrected values:
   - $(3,7,11)$: min genuine coprime gap is **147** at $(2,3,2)$
     ($2^3+3^7-2^{11}=147$), NOT 277 (attempt-20's $(13,2,2)$ is rank 4).
   - $(5,7,11)$: **171** at $(2,3,2)$ ($2^5+3^7-2^{11}=171$), NOT 288.
   Both confirmed by an independent audit scanner
   (`scripts/audit_corrected_scan.py`, skeptic agent) and by the corrected
   56-signature run. Old scripts deprecated (headers added).
2. **The "monotone in $-\chi$" law (attempts 19/23/24 claim) is REFUTED** by
   the corrected table: $(3,5,13)$ gives 51 < 77 at $(3,5,11)$ with more
   negative $\chi$; $(3,5,17/19/23)$ gives 1281/831/860 (non-monotone). The
   corrected sequence $29<77<147<171<1771$ is monotone but NOT in $-\chi$ —
   the min is small-base corner arithmetic, not a smooth law. Attempt-23/24's
   "re-confirmed" claims relied on the buggy values.
3. (Prior values 29, 77, 1771 re-verified unchanged.)

## The corrected 56-signature table + Corner Principle

All 56 distinct-odd-prime signatures from primes $\le23$ scanned (corrected
scan; full box $C\le60$, $B\le10^4$, exact nearest $A$; corner box $C\le3$):

- **Corner Principle verified 56/56**: min genuine gap always attained at
  $C\le3$ — at $C=2$ for 55 signatures, $C=3$ only at $(5,11,13)$ (2681 at
  $(17,3,3)$). **Robustness confirmed: at $C\le100$, $B\le10^5$ — 0
  violations in 56, all minima identical**
  (`scripts/near_miss_robustness.py`, 942s run 2026-08-31; also discharges
  attempt-24's wider-box flag on 1771).
- **0 genuine gap-1 hits** in the entire scanned open class (56×0).
- **Boundary law**: the principle FAILS at near-Euclidean signatures —
  $(3,3,3)$: $G=2$ at $(5,6,7)$, corner value 11 (hand-verified), and FOUR
  genuine gap-1 near-misses (e.g. $6^3+8^3=9^3-1$); $(3,3,5)$: $G=2$ at
  $(239,271,32)$ ($271^3+239^3=2^{25}-2$). It HOLDS at $(3,3,7)$ and
  $(3,5,5)$ (granularity exponent $\gamma=7/3$ each; $G=5$ both). So the
  failure boundary sits at $\gamma\le5/3$, and the open class
  ($\gamma\ge3.267$ at $(3,5,7)$) lies strictly above it. Filed as
  [[corner-principle]].

## Mechanism

Granularity: attainable sums $A^p+B^q$ near height $C^r$ have mean spacing
$C^{\gamma}$, $\gamma=1-r\chi=r(1-\frac1p-\frac1q)$; open-class $\gamma\ge3.267$
pins the min to the corner where it is small-number arithmetic (erratic — no
smooth law in $\chi$); near-Euclidean $\gamma\le5/3$ lets deep coincidences
($2^{25}-2$) win. Supersedes the counting heuristic of attempt-19
(`theory/methods/counting-heuristic.md` — its monotone prediction is wrong;
its finiteness prediction stands).

## Provenance of this attempt (ultracode session)

Breakthrough-hunt workflow candidate (beals scan) → adversarial verification
(3 lenses): novelty SURVIVES (4/4 literature checks negative: no prior
unit-base near-miss classification, no odd-odd k=2 formulation, no corner
principle, no per-signature gap tables; near-miss folklore = MSE thread
3256867 + OEIS A050787-793 + Norvig's relative-error page), soundness
SURVIVES (bug confirmed by independent re-run; T1-T4 re-derived; corner
numbers reproduce), referee SURVIVES (JIS/Integers-grade computational note).
Robustness run CONFIRMED (0/56 violations at C≤100, B≤1e5). Remaining
to-verify: Ratcliffe–Grechuk 2412.11933 full read; T4 citation
chain (Cohn 1993 vs LeVeque 1952).

## Next

1. ~~Complete robustness run~~ — done (0/56 violations); preprint §5.3 patched.
2. Read Ratcliffe–Grechuk in full (the one must-check primary source).
3. Verify T4's citation against Cohn 1993 / BMS 2006 paper bodies.
4. Consider: T2+3.2 gives a clean target — prove odd-odd Pillai-2 for the
   smallest pair $(3,3)$: $X^3-Y^3=2$ is trivially impossible
   (factorization) — check which pairs are trivial; the first non-trivial is
   likely $(3,5)$: $X^5-Y^3=2$.
5. Open problem 3 of the preprint: prove no non-unit-base gap-1 near-miss
   in the open class (0 found across 56 signatures).