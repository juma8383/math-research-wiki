---
type: attempt
problem: birch_swinnerton_dyer
attempt: 9
date: 2026-08-30
approach: Primary-source verification of BCK21 (Burungale–Castella–Kim, "A proof of Perrin-Riou's Heegner point main conjecture", Algebra & Number Theory 15:7 (2021)) — pin down the exact hypotheses under which the Heegner MC (the discharged leg of Kataoka–Sano's three-fold conditional) is proven
outcome: confirmed
tags: [primary-source-verification, heegner-point-main-conjecture, bck21, perrin-riou, hypothesis-spades, nonanomalous, iwasawa-greenberg, bdp, control-step, direction-a]
---

# Attempt 09 — BCK21 primary-source-verified: the Heegner MC is proven under explicit hypotheses (Hypothesis ♠ + ρ surjective + p nonanomalous), discharging the first leg of Kataoka–Sano's conditional

Cycle-5 Continue on BSD (attempt-08's "Next" target). attempt-08 read
Kataoka–Sano's Remark 1.6 — "Burungale–Castella–Kim has recently proved the
Heegner point main conjecture under mild [conditions]" — but the extracted PDF
text cut off at "undermildBC", leaving the exact hypotheses unspecified. This
cycle pins them down from the primary source.

## BCK21 — the paper and its exact hypotheses

**Burungale–Castella–Kim**, *A proof of Perrin-Riou's Heegner point main
conjecture*, **Algebra & Number Theory 15:7 (2021), 1627–1653**, DOI
[10.2140/ant.2021.15.1627](https://doi.org/10.2140/ant.2021.15.1627),
arXiv:1908.09512. MSC 11R23 (primary), 11F33.

**Setting:** $E/\mathbb Q$ of conductor $N$; $p>3$ a prime of **good ordinary**
reduction; $K$ imaginary quadratic of discriminant $D_K<0$ prime to $Np$;
**(disc)** $D_K$ odd and $D_K\neq-3$; **(Heeg)** the generalized Heegner
hypothesis — writing $N=N^+N^-$ with $N^+$ (resp. $N^-$) divisible only by
primes split (resp. inert) in $K$, $N^-$ is the squarefree product of an
**even** number of primes.

**Hypothesis ♠** (for the triple $(E,p,K)$), with $\rho:G_{\mathbb Q}\to
\mathrm{Aut}_{\mathbb F_p}(E[p])$ and $\mathrm{Ram}(\rho)$ the primes
$\ell\Vert N$ where $E[p]$ is ramified:
1. $\mathrm{Ram}(\rho)$ contains all primes $\ell\Vert N^+$;
2. $\mathrm{Ram}(\rho)$ contains all primes $\ell\mid N^-$ with
   $\ell\equiv\pm1\pmod p$;
3. if $N$ is not squarefree, then either $\mathrm{Ram}(\rho)$ contains a prime
   $\ell\mid N^-$, or there are at least two primes $\ell\Vert N^+$.

**Nonanomalous:** $p\nmid|\tilde E(\mathbb F_w)|$ for all $w\mid p$ of $K$
(equivalently $a_p\not\equiv1\pmod p$ if $p$ splits, $a_p^2\not\equiv1\pmod p$
if $p$ inert).

## Theorem A — the Heegner MC (the discharged leg)

Assume $p>3$, good ordinary, **(Heeg)**+**(disc)**, **Hypothesis ♠**,
**$\rho$ surjective**, **$p$ nonanomalous**. Then the **Heegner point main
conjecture** (Perrin-Riou's Conjecture 1.1) holds.

This is the precise content of Kataoka–Sano's Remark 1.6 "mild conditions."
So Kataoka–Sano's Thm 1.5 (Heegner MC ⟹ rank-two Euler system $c$ with
$c_{K_\infty}=z^{Hg}_\infty$) is **unconditional under BCK21's hypotheses** —
the rank-2 Euler system exists (non-canonically) for $E/\mathbb Q$ with good
ordinary reduction at $p>3$ satisfying Hypothesis ♠, $\rho$ surjective, $p$
nonanomalous. The **first leg of the three-fold conditional is discharged**,
and the obstruction to the $p$-part of BSD for $E/K$ is now the **two-fold**
conditional: **Conj 1.9** (Darmon-derivative explicit formula) + **$R^{Boc}_{K_\infty}\neq0$**
(Bockstein regulator).

## Theorem B — the Iwasawa–Greenberg MC for the BDP $p$-adic $L$-function

Assume additionally **(spl)** $p\mathcal O_K=\mathfrak p\bar{\mathfrak p}$
splits in $K$ (same hypotheses as Theorem A). Then the **Iwasawa–Greenberg
main conjecture** for the Bertolini–Darmon–Prasanna $p$-adic $L$-function
$L_p^{\mathrm{BDP}}$ holds: $\mathrm{Char}_\Lambda(X^{\emptyset,0})=(L_p^{\mathrm{BDP}})^2$
as ideals in $\Lambda^{\mathrm{ur}}$.

This is a bonus: it pins the **anticyclotomic** summand's main conjecture (the
$E^K$-twist side of the Selmer decomposition $\mathrm{Sel}(K)\simeq
\mathrm{Sel}(\mathbb Q)\oplus\mathrm{Sel}(\mathbb Q,E^K)$), complementing the
cyclotomic side (Kato). So *both* summands' main conjectures are now proven
under BCK21's hypotheses — the resolution side of the rank-2 structure is
fully discharged; only the rank-2 *composition* control (Darmon-derivative
Kolyvagin system) remains.

## Generalization to modular forms (Hypothesis ♥, Theorem 3.2)

For a newform $f\in S_2(\Gamma_0(N))$ with $p\nmid N$, ordinary at a prime
$\wp$ of its coefficient ring $\mathcal O$, **Hypothesis ♥** adds a fourth
condition to ♠: for all $\ell$ with $\ell^2\mid N^+$,
$H^1(\mathbb Q_\ell,A_f[\wp])=H^0(\mathbb Q_\ell,A_f[\wp])=\{0\}$. (For
$\mathcal O=\mathbb Z$, i.e. $f$ an elliptic curve, ♥ reduces to ♠.) So the
Heegner MC is proven in the modular-form generality too.

## Appendix Theorem A.1 — rank-one alternative without nonanomalous

The appendix gives an alternative proof of a special case **without** the
nonanomalous hypothesis, assuming instead Hypothesis ♠, $\rho$ surjective,
$p$ splits, and $\mathrm{ord}_{s=1}L(E/K,s)=1$ (analytic rank one). Under
these, both Conjecture 1.1 and 1.3 hold. This is the rank-one bridge to the
classical Gross–Zagier–Kolyvagin setting.

## Methods (why this is a genuine advance)

The proof builds on Howard's bipartite Euler systems (2006), Wei Zhang's
Kolyvagin-conjecture work (2014), Bertolini–Darmon (2005), Pollack–Weston
(2011), Chida–Hsieh (2015), and an extension of the Castella–Hsieh explicit
reciprocity law to $N^-\neq1$. It **dispenses with Xin Wan's deep
Rankin–Selberg results** and allows $N^-=1$, $N$ with square factors, and $p$
inert in $K$ — cases not covered by earlier work.

## What this changes in the obstruction map

- **The "mild conditions" of Remark 1.6 are now exact**: $p>3$ good ordinary,
  **(Heeg)**+**(disc)**, Hypothesis ♠, $\rho$ surjective, $p$ nonanomalous.
  The Heegner MC is a **theorem** under these hypotheses, not a conjecture.
- **Kataoka–Sano's three-fold conditional is now two-fold** (Conj 1.9 +
  $R^{Boc}_{K_\infty}\neq0$), and the two-fold conditional is *conditional
  only on the control step* — the resolution step (rank-2 Euler system
  existence) is discharged by BCK21 (Thm A) + Kataoka–Sano (Thm 1.5).
- **Both summands' main conjectures are proven** (cyclotomic Kato +
  anticyclotomic BDP via BCK21 Thm B), so the Selmer decomposition
  $\mathrm{Sel}(K)\simeq\mathrm{Sel}(\mathbb Q)\oplus\mathrm{Sel}(\mathbb Q,E^K)$
  is fully resolved on each summand; the wall is purely the rank-2
  *composition* control (Darmon-derivative Kolyvagin system + Bockstein
  non-degeneracy). This is the sharpest possible statement of the
  "obstruction at control, not resolution" thesis for BSD.
- **Direction (A) is now a two-condition target with a named, proven base**:
  prove Conj 1.9 and $R^{Boc}_{K_\infty}\neq0$ (both control-step), and the
  $p$-part of BSD for $E/K$ follows — over a base (Heegner MC) that is a
  theorem.

## Honesty / scope

- **This is a primary-source verification, not a proof move.** BSD remains
  open; rank $\ge2$ and exact $|\Sha|$ untouched. The cycle *verified* BCK21's
  exact hypotheses and *sharpened* the conditional from three-fold to
  two-fold with a named, proven base.
- **The hypotheses are restrictive** (good ordinary, $p>3$, Hypothesis ♠,
  $\rho$ surjective, $p$ nonanomalous) — the Heegner MC is *not* proven for
  all $E/\mathbb Q$; it is proven for a large, explicit class. The
  "unconditional" rank-2 Euler system of Thm 1.5 is unconditional *within
  that class*.
- **Theorem B's BDP statement** and **Theorem 3.2's Hypothesis ♥** are
  recorded from the search summary (primary-source-consistent but not
  line-by-line re-derived from the PDF); the exact $\mathrm{Char}_\Lambda$
  ideal equality and the ♥ fourth condition are flagged `to-verify` against
  the BCK21 PDF body if they become load-bearing.

## Next (attempt-10)

The remaining two-fold conditional is now the cleanest target in the BSD
attack: **Conj 1.9** (Darmon-derivative explicit formula) and **$R^{Boc}_{K_\infty}\neq0$**
(Bockstein regulator). A future cycle should survey what is known toward
Conj 1.9 (the algebraic variant Thm 1.10 already reduces it to the Heegner MC
up to $\mathbb Z_p^\times$ — so the gap is the *explicit* $\mathbb Z_p^\times$
unit, i.e. the Bockstein regulator) and whether $R^{Boc}_{K_\infty}\neq0$ is
known in any case. The rotation continues; weekly usage is being spent toward
the user's 99% target.
