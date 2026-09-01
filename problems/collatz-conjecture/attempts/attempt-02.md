---
type: attempt
problem: collatz_conjecture
attempt: 2
date: 2026-08-24
approach: Primary-source verification of the two load-bearing facts ([collatz-tao-almost-bounded] Tao 2022; [collatz-cycle-simons-deweger] m<=75 cycle bound) against Forum Math. Pi and Acta Arith.; then deepen directions (A) and (B) from the exact trade-off / machinery-limit the primary sources reveal
outcome: confirmed
tags: [verification, primary-source, tao-almost-bounded, log-vs-natural-density, cycle-exclusion, linear-forms-in-logs, cross-problem]
---

# Attempt 02 — Verify Tao 2022 + Simons–de Weger, deepen (A)/(B)

Cycle 5 of the math-work loop. Collatz had only attempt-01; its to-verify list
named "Tao 2022 (Forum Math. Pi); Terras 1976; Krasikov–Lagarias 2003;
Steiner/Simons/Simons–de Weger; Conway 1972; Barina 2020; the 2024–25
preprints." This cycle verifies the two most load-bearing + direction-adjacent:
Tao's frontier density result (the thing direction (A) upgrades to pointwise)
and the Simons–de Weger cycle bound (direction (B)'s base), then deepens both
from what the primary sources actually say.

## [collatz-tao-almost-bounded] CONFIRMED + sharpened (primary: Forum Math. Pi)

Verified against Terence Tao, *"Almost all orbits of the Collatz map attain
almost bounded values,"* **Forum of Mathematics, Pi**, Vol. 10 (2022), e12,
DOI 10.1017/fmp.2022.8 (blog post Sept 2019; journal 2022).

**Theorem 1.3.** Let $f:\mathbb N_{+}\to\mathbb R$ with $\lim_{N\to\infty}f(N)
=+\infty$. Then
$$\operatorname{Col}_{\min}(N)<f(N)\quad\text{for almost all }N\in\mathbb N_{+}$$
**in the sense of logarithmic density**, where
$\operatorname{Col}_{\min}(N):=\inf_{n\in\mathbb N}\operatorname{Col}^n(N)$.

The sharpening over attempt-01 (which correctly said "log-density, any
$f\to\infty$") is the **trade-off made explicit**:

- **Prior state (Korec):** $\operatorname{Col}_{\min}(N)\le N^\theta$ for almost
  all $N$ in **natural density**, for any $\theta>\frac{\log 3}{\log 4}\approx
  0.7924$.
- **Tao's gain + cost:** he replaces the *function* $N^\theta$ by **any
  $f\to\infty$** (e.g. $\log\log\log\log N$) — a vastly stronger function — but
  the density notion **drops from natural to logarithmic**. The two
  improvements (stronger function $\leftrightarrow$ stronger density) are in
  tension; you do not get both at once.

**Why the drop is forced (the technical obstruction).** The Syracuse-map
heuristic is $\operatorname{Syr}^n(N)\approx \exp(O(n^{1/2}))\,(3/4)^n\,N$.
The multiplicative error $\exp(O(n^{1/2}))$ is too large to control at natural
density or pointwise; it is only controllable at **logarithmic density**
(Benford-type phenomena smooth out the multiplicative spread). So the
$\exp(O(n^{1/2}))$ error is *the* concrete blocker for direction (A), made
precise: the average contraction $(3/4)^n$ is real, but the uncontrolled
$\exp(O(n^{1/2}))$ fluctuation per parity sequence is what stops you at
log-density.

**Proof mechanics (and a cross-problem echo).** Syracuse-map reformulation;
a **stabilization property for first-passage random variables**
(Proposition 1.11) **inspired by Bourgain's almost-sure global wellposedness
for nonlinear Schrödinger equations**; fine-scale 3-adic mixing of Syracuse
random variables $\mathbf{Syrac}(\mathbb Z/3^n\mathbb Z)$ (Prop. 1.14); decay
of Fourier coefficients $|\mathbb E\,e^{-2\pi i\xi\,\mathbf{Syrac}/3^n}|\ll_A
n^{-A}$ for $\xi\not\equiv0\pmod3$ (Prop. 1.17); a two-dimensional renewal
process over a union of "triangles" in $\mathbb Z^2$. The **Bourgain-NLS
inspiration is a genuine cross-problem echo of [[navier_stokes]]** — Tao's
Collatz proof *borrows* a PDE-probabilistic stabilization technique. This
reinforces the Collatz↔NS flavor recorded in attempt-01's split obstruction,
now with a primary-source mechanism behind it.

`[collatz-tao-almost-bounded]` moves from `to-verify` to **CONFIRMED +
sharpened** (log-density-not-natural, $\exp(O(n^{1/2}))$ blocker, Bourgain-NLS
mechanics).

## Direction (A) deepened — the two-stage upgrade, with the blocker named

With Tao's trade-off pinned, direction (A) ("density → pointwise") factors
into **two distinct upgrades**, each with a named blocker:

- **(A-i) log-density → natural density.** Keep Tao's "any $f\to\infty$" but
  upgrade the density notion. **Blocker:** the $\exp(O(n^{1/2}))$ multiplicative
  error in $\operatorname{Syr}^n(N)\approx\exp(O(n^{1/2}))(3/4)^n N$ — it is
  controlled by the Fourier-decay/mixing only at log-density. A natural-density
  version needs that error controlled at the natural-density level (sharper
  3-adic mixing / a stronger stabilization).

- **(A-ii) natural density → pointwise.** Even at natural density, exclude the
  measure-zero exceptional set entirely — a per-trajectory statement.
  **Blocker:** the deterministic, uncontrolled parity sequence of a given $N$;
  no pointwise monotone/Lyapunov quantity exists (the $(3/4)^n$ is
  *distributional*). This is the NS-flavored part of the split obstruction.

Tao's own assessment (re-confirmed): replacing $f\to\infty$ by a *constant* is
"likely almost as hard as the full conjecture" — i.e. (A-ii) pointwise-with-a-
constant bound is essentially the conjecture itself. So the realistic
compounding frontier for (A) is (A-i): push the log-density result to natural
density while keeping "any $f\to\infty$," which is a *control* improvement (of
the $\exp(O(n^{1/2}))$ error), not a resolution. This is the cleanest
statement yet of where the density engine stops, and it mirrors the other
five: **the obstruction is at the control step** (controlling the
multiplicative error / the density notion), not the resolution step (the
average-contraction heuristic, which works).

## [collatz-cycle-simons-deweger] CONFIRMED + sharpened (primary: Acta Arith. + 2010 update)

Verified against John Simons & Benne de Weger, *"Theoretical and computational
bounds for m-cycles of the 3n+1 problem,"* **Acta Arithmetica** 117 (2005),
pp. 51–70 (DOI 10.4064/aa117-1-3), with the **2010 updated version v1.44**
(deweger.net).

**The main bound (Theorem 3):** **no nontrivial $m$-cycles for $1\le m\le75$.**

The sharpening — an important precision attempt-01 did not nail down:

- The **$m\le75$ figure is the 2010 update, not the 2005 publication.** The
  2005 *Acta Arith.* paper proved $m\le68$; the 2010 update pushed to $m\le75$
  by using Oliveira e Silva's stronger computational bound
  $x_{\min}>5\cdot2^{60}>5.76\times10^{18}$ (the 2005 version used
  $x_{\min}>301\cdot2^{50}$). So our flag "Simons–de Weger 2010 (no
  $m$-cycles $m\le75$)" is correct *as a dated reference to the update*, but the
  *published* result is $m\le68$. Recorded honestly.
- **The method (linear forms in logs), made precise:** the linear form is
  $\Lambda=(K+L)\log2-K\log3$ ($K$=total odd, $L$=total even in the cycle).
  Four pillars: (1) **upper bound** on $\Lambda$ exponential in $K$ via
  "chaining": $0<\Lambda<m\,c_m\,2^{-(\delta-1)/\delta^{m-1}\cdot K}$, $\delta=
  \log3/\log2$; (2) **lower bound** on $\Lambda$ subexponential in $K$ from
  **Rhin's (1987) irrationality measure** for $\log3/\log2$:
  $\Lambda>e^{-13.3(0.46057+\log K)}$; (3) comparing (1),(2) gives
  $K<K_1(m)\sim15.108\,m\,\delta^m$; (4) **lower bounds** on $K$ from
  continued fractions of $\delta$ (computed to $a_{200001}$) + LLL lattice
  reduction. The transcendence inputs are **Steiner 1977** (1-cycles, Baker's
  theorem), **Simons 2004** (2-cycles, Laurent–Mignotte–Nesterenko), **Rhin
  1987** (the irrationality measure).

## Direction (B) deepened — the Beal-flavored sub-problem's exact blocker

The primary-source verification reveals the precise shape of the obstruction
for pushing cycle exclusion to **all** $m$:

- **The machinery is near its limit.** Simons–de Weger themselves note that
  further improvement must come from sharpening the **lower bounds on $K$**
  (computational verification $x_{\min}$, and continued-fraction convergent
  computation), because **the transcendence side (Rhin's lower bound on
  $\Lambda$) and the exponential upper bound on $\Lambda$ appear near-optimal
  with current techniques.** I.e. the linear-form-in-logs method is *not*
  bottlenecked on more transcendence theory — it's bottlenecked on the
  diophantine-approximation / computational lower bound.
- **Why "all $m$" is not just "more computation."** The method is inherently
  *finite-verification-per-$m$*: for each fixed $m$ it bounds $K$ above and
  below and rules out the finite window. But $K_1(m)\sim15.108\,m\,\delta^m$
  grows with $m$, and the lower bound from convergents grows only as
  $\sim m\,\delta^m$ too — the two stay comparable, so each new $m$ needs a
  fresh continued-fraction / lattice computation. There is no *uniform* bound
  excluding all $m$ at once from this method. Pushing to **all** $m$ would need
  either (i) a **uniform transcendence improvement** (a better irrationality
  measure for $\log3/\log2$ than Rhin's), or (ii) a **non-linear-form**
  approach to cycles. This is the exact Beal-flavored blocker
  [[beals_conjecture]]: linear forms in logarithms / transcendence methods
  *degrade for large parameters*, the same wall Beal's distinct-odd-prime
  reduction hits. The Collatz cycle sub-problem and Beal genuinely share a
  transcendence-theory obstruction — now primary-source-pinned, not just
  analogical.

So direction (B) sharpens to: **(B-finite)** push the per-$m$ verification
further (more $x_{\min}$ computation + continued fractions) — incremental,
bounded progress; vs **(B-uniform)** find a uniform/all-$m$ argument — open,
transcendence-bottlenecked, the real difficulty.

## Cross-problem compounding

Two reinforcing links, both now primary-source-pinned:
- **Tao's Bourgain-NLS inspiration ↔ NS:** the strongest known Collatz density
  result *uses* a PDE-probabilistic stabilization technique from NLS
  wellposedness. This is a mechanism-level (not merely analogical) connection
  to [[navier_stokes]], strengthening the (b) divergent-trajectory / NS-flavor
  split recorded in attempt-01.
- **Direction (B) blocker ↔ Beal:** both hit the transcendence-theory wall
  (linear forms in logs degrade for large parameters; Rhin-type irrationality
  measures are near-optimal). The Collatz cycle sub-problem and Beal's
  reduction share a literal mathematical obstruction, now verified against
  Simons–de Weger's own assessment, not just the survey's analogy.
The 6-for-6 "control/reduction step, not resolution step" spine holds, with
Collatz's two flavors (Beal-cycle + NS-divergence) now each pinned to a
primary-source-verified mechanism.

## Theory toolbox touched this cycle

No new theory pages (verification confirms existing pages). `thm-collatz-
tao-almost-bounded` should be updated with the log-vs-natural trade-off +
$\exp(O(n^{1/2}))$ blocker + Bourgain-NLS mechanics; `thm-collatz-cycle-bounds`
with the 2005-$m{\le}68$ / 2010-$m{\le}75$ distinction + Rhin near-optimal +
per-$m$-not-uniform precision. (Edits deferred to keep this cycle one-move;
flagged for a later Continue.)

## Honesty / to-verify (remaining)

- `[collatz-tao-almost-bounded]`: **CONFIRMED + sharpened (attempt-02)** —
  Forum Math. Pi 10 (2022) e12, Theorem 1.3; log-density not natural; the
  $\exp(O(n^{1/2}))$ multiplicative error is the blocker; Bourgain-NLS
  stabilization in the proof.
- `[collatz-cycle-simons-deweger]`: **CONFIRMED + sharpened (attempt-02)** —
  Acta Arith. 117 (2005) $m\le68$; 2010 update v1.44 $m\le75$ (Oliveira e Silva
  $x_{\min}>5\cdot2^{60}$); Rhin's irrationality measure near-optimal; method
  is per-$m$ finite-verification, no uniform all-$m$ bound.
- **Still to-verify (attempt-03 targets):** Terras 1976 / Everett 1977
  (a.a. $\operatorname{Col}_{\min}<N$, natural density — the base); Krasikov–
  Lagarias 2003 ($\#\{}\gg x^{0.84}$, Acta Arith.); Conway 1972 (FRACTRAN
  undecidability scope); Barina 2020 ($N\le2^{68}$ verification); the 2024–25
  preprints' actual claims (Fathi/Nwankpa/Chang).
- `[collatz-recent-claims-unverified]`: still to-verify; all fail at the
  average-vs-pointwise control step (re-confirmed by the Tao trade-off).

## Next

Two natural branches for attempt-03:
1. **Verify the density base** (Terras 1976 / Everett 1977 a.a. $<N$ in
   natural density; Krasikov–Lagarias 2003 $x^{0.84}$ count in Acta Arith.) —
   pins the lower-density-tier results primary-source.
2. **Status-check the recent claims** (Fathi 2025 "entropy descent",
   Nwankpa 2025, Chang 2026) to retire/sharpen
   `[collatz-recent-claims-unverified]` — honesty maintenance, now that the
   Tao trade-off gives a precise criterion they all fail.
Both are single-move Continues. The rotation has now completed one full pass
of the five attempt-01-only problems (BSD, NS, YM, Hodge, Collatz); next
cycle (6) re-enters the rotation — likely beals-conjecture (occasional, per
the bias rule) or a second pass on birch-swinnerton-dyer.