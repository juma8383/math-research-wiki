# Riemann Hypothesis

> Problem statement. For the running state of the attack, read
> [progress.md](progress.md) first. **STATUS: OPEN** — the one Clay Millennium
> problem that was missing from the wiki; a genuine attack (unlike the solved
> [[poincare_conjecture]]).

## Statement

All non-trivial zeros of the Riemann zeta function $\zeta(s)$ have real part
$\tfrac12$:

$$\zeta(s)=0,\ 0<\Re(s)<1 \;\Longrightarrow\; \Re(s)=\tfrac12.$$

The **trivial** zeros at $s=-2,-4,-6,\dots$ (real, from the poles of
$\Gamma$) are excluded; the open question concerns the non-trivial zeros in the
**critical strip** $0<\Re(s)<1$. The line $\Re(s)=\tfrac12$ is the **critical
line**. The functional equation $\zeta(s)=\chi(s)\zeta(1-s)$ (with $|\chi|=1$ on
the critical line) gives a *symmetry* $\Re(s)\leftrightarrow 1-\Re(s)$ about the
line — it pairs zeros symmetrically but does **not** force them onto the line
(a zero at $\tfrac12+\beta+it$, $\beta\ne0$, is allowed by symmetry, paired
with one at $\tfrac12-\beta+it$). Forcing $\beta=0$ is exactly the open
content; see [notes.md](notes.md).

A Clay Millennium Prize problem ($1M). The single most famous open problem in
mathematics; the central organizing conjecture of analytic number theory —
its truth controls the error term in the Prime Number Theorem and the
distribution of primes. Equivalent, for many purposes, to the **generalized
Riemann hypothesis (GRH)** for all $L$-functions (Dirichlet, Dedekind, Hecke,
automorphic).

## The exact frontier (verified facts, this attempt)

- **Computational.** All non-trivial zeros up to height $T\le 3\cdot10^{12}$
  are on the critical line (Platt–Trudgian 2021) — the standing height record.
  The first $\sim10^{13}$ zeros are on the line. No counterexample at any
  checked height.
- **Zero-free region.** No zeros in
  $\Re(s)\ge 1-c\,(\log|t|)^{-2/3}(\log\log|t|)^{-1/3}$ (Korobov–Vinogradov),
  the best known zero-free region near $\Re=1$.
- **Zero-density.** Bounds on $N(\sigma,T)$ = #{zeros with $\Re(s)\ge\sigma$,
  $0<\Im<T$}: Ingham 1940 ($N(\sigma,T)\ll T^{\frac{3(1-\sigma)}{2-\sigma}\,+\varepsilon}$)
  had stood as the base of the ladder since 1940 (Huxley 1972 held the
  intervening best, $12/5$, in this range); **Guth–Maynard 2024** gave the first
  substantive improvement for $\sigma\le\tfrac34$ — $N(\sigma,T)\le
  T^{\frac{15(1-\sigma)}{3+5\sigma}+o(1)}$ (so $T^{\frac{30(1-\sigma)}{13}+o(1)}$
  at $\sigma=\tfrac34$) — **published Annals of Math. (2) 203 (2026), no. 2,
  623–675** [verified against the Annals listing]. Chourasiya 2024
  (arXiv:2412.02068) *advertises* the first explicit Carlson zero-density
  estimate with log exponent $5-2\sigma$, but an automated audit flags that
  the proof as written concludes Carlson's original $(\log T)^4$, and
  Chourasiya–Simonič (arXiv:2507.15184, 2025) explicitly supersedes it —
  downgraded `[rh-chourasiya-flagged]` `[summary]`, superseding estimate =
  $(7-5\sigma)/(2-\sigma)$.
- **Proportion on the line.** Levinson (1974) $\ge\tfrac13$; Conrey (1989)
  $\ge\tfrac25=40\%$; Pratt–Robles–Zaharescu–Zeindler 2020 $\ge\tfrac{5}{12}
  \approx41.7\%$; Wu 2015 $\ge0.6603$ (the intermediate rung); **now
  $\ge0.6725>\tfrac23$ simple *and* on the line, $\ge\tfrac56$ distinct —
  Alpöge–Furman, arXiv:2608.13637 (Aug 2026)**: unconditional
  Montgomery theorem (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2024) +
  von Neumann rank–trace inequality + Sylvester's law of inertia on finite
  compressions of Weil's Hermitian form; Theorems A/B Lean-4-formalized
  (no `sorry`; repo `github.com/anthropics/formal-math`, project `zeta23/`),
  read by Conrey and Goldston, **not journal-peer-reviewed**
  — the 2024 date and bare "not peer-reviewed" status in the earlier wiki
  text were both imprecise; updated to `[rh-2026-claims-non-journal]`.
  Still a proportion result — resolution-on-average, not the control step.
- **Bandwidth-one ceiling (verify-wave confirmed verbatim, §7.2),** corrected
  against the paper by the 2026-08-31 adversarial verify: the exact rational
  ceiling is $p_0\le 0.6818287$ (ceiling "approximately 0.682"; an earlier
  wiki figure 0.68185 was a misrounding) — *any* certificate depending on the
  configuration only via its first two trace moments against test functions
  of Fourier support in $[-1,1]$ (a "bandwidth-one certificate") is ceilinged
  there by the Lean theorem `Zeta23.PairCeiling.ceiling_law256`; $\frac23$ is
  within $0.016$ of its own method's ceiling. Corroborated supported
  trajectory (§7.2): pushing past $\tfrac23$ by this route needs
  pair-correlation information **beyond Fourier support 1**; HL$(4)^*$ would
  give $\tfrac{13}{18}$, HL$(k_0)^*$ for all $k_0$ or the full Montgomery
  form factor would certify 100%, while "RH itself is out of reach of the
  mechanism." A trajectory "0.70/0.80/0.90 need support 1.04/1.26/1.70"
  circulating in the scan is **not in the paper — deleted as scan-fabricated**
  `[rh-bandwidth-ceiling-verified]`. The ceiling is exactly the
  control/reduction shape: it limits what the certificate can *certify* —
  the remaining third is not shown off-line, merely unreached.
- **The gap.** Every result above works on a **slice** (up to height $T$) or
  on **average / in density** (almost-all / proportion / zero-density). The
  open content is **every zero, every height**: forcing $\beta=0$ for *all*
  non-trivial zeros. This slice→full-strength step is the control wall; see
  [progress.md](progress.md) for the three control-reductions.

## See also

- [progress.md](progress.md) — read-first running state, the central
  obstruction (control-step), the function-field / number-field two-avatars
  structure, 2024 advances.
- [notes.md](notes.md) — methodology + ≥3 approaches (Hilbert–Pólya spectral,
  Weil/Li/Bombieri–Lagarias positivity, zero-density/computational,
  function-field analogy) + cross-problem links (esp. [[birch_swinnerton_dyer]]
  two-avatars twin, [[hodge_conjecture]] standard-conjectures link).
- [attempts/attempt-01.md](attempts/attempt-01.md) — first attack.