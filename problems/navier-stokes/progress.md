# Progress — Navier-Stokes existence and smoothness

> Running state of the attack. Read this first when resuming. Consolidated
> through attempt-06. Same methodology as [[beals_conjecture]] and
> [[birch_swinnerton_dyer]]: locate the exact frontier, name the open content,
> map the obstruction at the *control* step (not the resolution step), unify
> threads.

## The exact frontier

The Millennium problem (Fefferman) [ns-millennium-fefferman] asks for global
regularity (A/B) OR a breakdown counterexample (C/D) for 3D incompressible NS
on domains without boundary.

Known:
- 2D solved [ns-2d-solved] [[def-navier-stokes-equation]].
- 3D local well-posedness + small-data global [[thm-local-wellposedness]].
- 3D global Leray-Hopf weak solutions; **uniqueness OPEN** [[thm-leray-weak-solutions]]
  (nonuniqueness proven only *below* Leray-Hopf — Buckmaster–Vicol, see attempt-03).
- Conditional regularity (Serrin/BKM) [[thm-serrin-regularity]]
  [[thm-beale-kato-majda]]; partial regularity (CKN)
  [[thm-caffarelli-kohn-nirenberg]].
- Averaged-NS blowup model [[thm-tao-averaged-blowup]].

Open: **global regularity for large 3D data** (no unconditional global critical
bound; no blowup example for true NS).

The **open content** (analog of Beal's "finitely many → zero" and BSD's
"rank ≤1 → arbitrary rank"):
- regularity side: **"small/local data → arbitrary large-data global
  regularity"**; and
- counterexample side: **"averaged-NS blowup → true-NS blowup"**.

## The obstruction: control step, not resolution step

The *resolution* machinery works and finished the verified cases:
- **Local existence** + **small-data global** [[thm-local-wellposedness]].
- **Conditional regularity**: BKM ($\int\|\omega\|_\infty<\infty \Leftrightarrow$
  regular) [[thm-beale-kato-majda]], Serrin ($u\in L^r_tL^s_x$,
  $2/r+3/s\le1\Rightarrow$ smooth; endpoint $L^\infty L^3$ by ESS)
  [[thm-serrin-regularity]].
- **Partial regularity** (CKN: singular set parabolic dim $\le1$)
  [[thm-caffarelli-kohn-nirenberg]].

These say "IF a critical norm is bounded THEN smooth." The gap is the missing
**global a priori bound on a critical norm** — a *control* step, exactly
parallel to BSD's Selmer-group control and Beal's reduction step. The only
unconditional global bound is the **energy** ($\|u\|_{L^2}$), which is
**subcritical** in 3D [[method-energy-supercriticality]] [ns-supercritical]:
under NS scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$,
$\|u_\lambda\|_{L^2}=\lambda^{-1/2}\|u\|_{L^2}$ (weakens at small scales),
while the critical norm $L^3$ is scale-invariant. So the energy cannot control
the critical norm, and the nonlinear advection — Serrin number $S=d+1=4$ in
3D vs $d/2+2=3.5$ for the linear terms — transfers energy to small scales
faster than dissipation removes it. In 2D the two Serrin numbers are EQUAL
($3=3$), which is precisely why 2D is solved.

## Tao's quantitative frontier

Tao's quantitative $L^3$ blowup rate [ns-tao-quant-l3]: if smoothness is first
lost at $T^*$,
$\limsup_{t\uparrow T^*}\|u\|_{L^3}\cdot(\log\log\log(1/(T^*-t)))^c=\infty$.
This QUANTIFIES how hard the missing critical control is — the critical norm
must blow up faster than a triple log. Barker (2022) localized this; Palasek
(2022) extended the rate to **dimensions $d\ge4$** (a **quadruple** log, one
more than 3D) — **corrected** from the earlier "axisymmetric" mislabel (see
attempt-02 + the dated correction in attempt-01; Palasek is high-dimensional,
not axisymmetric; the axisymmetric program is Hou/Seregin, below). The
residual difficulty lives in the supercritical gap between the subcritical
energy bound and the critical norm.

## Candidate forward directions

- **(A) A critical a priori bound**: find a new global monotone/conserved
  quantity at critical (or super-to-critical) regularity, or a new mechanism
  controlling $L^3$/$\dot H^{1/2}$ globally — directly the missing control step.
  (Hard: energy is the only known monotone quantity, and it is subcritical.)
- **(B) Blowup construction (Fefferman C/D)**: a finite-time singularity for
  TRUE 3D NS. Tao's averaged-NS blowup [ns-tao-averaged-blowup] is the model;
  the gap is removing the averaging/modification while preserving blowup
  (axisymmetric/geometric ansätze). **Deepened (attempt-02):** the averaged
  operator $\tilde B=\int T_1B(T_2u,T_3v)\,d\mu$ has **tunable** rotations/
  dilations/multipliers the rigid true nonlinearity $(u\cdot\nabla)u$ lacks —
  removing the averaging = building "fluid logic gates" from the rigid
  operator (Tao: "no mathematical barrier… immense engineering barrier");
  equivalently, energy-identity + abstract-estimate proofs *cannot* work.
  **Axisymmetric ansatz** is the leading geometric candidate: Hou (2024,
  arXiv:2405.10916, preprint `to-verify`) gives strong *numerical* evidence
  for nearly-self-similar blowup as effective dimension $n(t)\to3$ (via a
  dimension-as-free-parameter rescaling that kills scaling instability), but
  for generalized (solution-dependent-viscosity) NS, not true constant-viscosity
  NS. Seregin (2024, arXiv:2402.13229, preprint `to-verify`) **rigorously
  rules out** exact/discrete-self-similar axisymmetric Type II blowup under
  conditions (no-swirl limiting Euler; conserved $|\omega_\vartheta|^{l_1/2}/
  |x'|^{l_1/2}$). **Refined open content:** a true blowup must be
  *non-self-similar* (or violate Seregin's conditions) and bridge the
  generalized→true-viscosity limit.
  **attempt-04 (primary-source, arXiv HTML):** both preprints CONFIRMED.
  **Hou 2405.10916** — two-section: Sec 4 solution-dependent viscosity
  $\nu(t){=}\nu_0\|u_1\|_\infty Z(t)^2$ ($\nu_0{=}0.006$) → stable
  *self-similar* blowup, effective $n{\approx}3.188{\to}3$ as $\nu_0{\to}0$,
  max vorticity $O(1/(T{-}t))$ violating BKM, profile satisfies NS with
  *constant* $\nu_0$; Sec 5 two *constant* viscosities (Boussinesq-type) →
  *nearly* self-similar with **log correction**
  $\lambda(t){=}(1{+}\varepsilon|\log(T{-}t)|)^{-1/2}$, $n{\approx}4.73$
  (Cheskidov diadic threshold $n{>}4$). **Generalized axisymmetric NS, NOT
  true constant-viscosity 3D NS** (caveat confirmed). **Seregin
  2402.13229** — Euler scaling $v{\to}\lambda^\alpha v(\lambda x,\lambda^{\alpha+1}t)$,
  $\alpha{=}2{-}m$, $\tfrac12{\le}m{<}1$; Prop 1.1 no-swirl limiting Euler
  ($\alpha{-}1{<}0$ forces $u_\vartheta{\to}0$); Prop 2.1 conserved weighted
  vorticity $g(t){=}\int\Phi(|f|)\,dx$, $f{=}\omega_\vartheta/r$; Prop 2.2
  no Type II blowup under $L^q$, $q{=}3/(2{-}m){\in}[2,3)$ (irrotationality
  contradiction); Prop 3.1/4.1 rule out **exact** and **discrete**
  self-similar Type II blowup ($U{\equiv}0$). **Complementary, NOT
  contradictory:** Seregin fences off the *classical exact/discrete
  self-similar* class (3D, standard scaling); Hou's candidate lives outside
  it (fractional dim + modified viscosity + log correction = *nearly*
  self-similar). Refined open content: a true blowup must be (i)
  non-(discrete-)self-similar (dodge Seregin) AND (ii) bridge
  generalized→true viscosity (Hou's gap). **Control-step echo:** Seregin's
  no-swirl-Euler + weighted-vorticity engine controls the self-similar
  slice; the non-self-similar/generalized slice is where it stops — the
  "one-dimensional engine stops" shape in microcosm (‖ BSD
  cyclotomic/anticyclotonic disjointness attempt-04, Collatz two-engine
  attempt-03).
- **(C) Critical-regularity / quantitative program**: sharpen conditional
  criteria (Luo 2019 optimal frequency localization [[thm-beale-kato-majda]],
  Barker localized rates) and push the supercritical-to-critical gap
  quantitatively, narrowing what an (A) or (B) proof must achieve.

## Best partial result so far (attempt-02)

- Frontier located (A/B vs C/D), open content named, obstruction mapped to the
  *critical-norm control* step with the supercriticality lens. Eight theory
  pages + one survey source filed, forming the core toolbox. Cross-problem
  analogy recorded: all three Millennium-class problems now share the
  "obstruction at the control/reduction step, not the resolution step"
  methodology.
- **attempt-02 (primary-source verification + direction B):** `[ns-tao-quant-l3]`
  confirmed (Tao 2019, triple-log rate, DOI 10.1090/pspum/104/01874; Barker 2022
  localized; Barker-Prange 2021 spatial concentration) and `[ns-ess-endpoint]`
  confirmed (ESS 2003, DOI 10.1070/RM2003v058n02ABEH000609, endpoint Serrin via
  backward uniqueness). **Mislabel caught + corrected append-only:** Palasek
  (2022) is the **high-dimensional** ($d\ge4$, quadruple log) extension, NOT
  axisymmetric (attempt-01 left intact with a dated correction blockquote).
  Direction (B) deepened: removing the averaging = building fluid logic gates
  from the rigid $(u\cdot\nabla)u$ (the averaged $\tilde B$ has tunable
  $T_i$ freedom the true operator lacks; Tao: "no mathematical barrier, immense
  engineering barrier"). Axisymmetric ansatz is the leading geometric candidate
  — Hou 2024 (preprint) nearly-self-similar numerical blowup as $n\to3$;
  Seregin 2024 (preprint) rigorously rules out exact/discrete self-similar
  Type II blowup. Refined open content: a true blowup must be non-self-similar
  and bridge generalized→true viscosity.
- **attempt-03 (primary-source verification):** `[ns-millennium-fefferman]`
  CONFIRMED — Fefferman's official Clay formulation (May 1, 2000): two
  no-boundary settings ($\mathbb R^3$ with decay, torus $\mathbb T^3$
  periodic); four statements A/B (existence-smoothness, $f\equiv0$) and C/D
  (breakdown, smooth $f$ allowed), proving any one resolves the prize.
  `[ns-buckmaster-vicol]` CONFIRMED + sharpened — Buckmaster–Vicol, *Annals*
  **189**(1) **2019**, 101–144 (DOI 10.4007/annals.2019.189.1.3; **not** 2022 —
  the 2022 JEMS follow-up is Buckmaster–**Colombo**–Vicol): nonuniqueness of
  $C^0_tH^\beta_x$ ($\beta<\tfrac12$) weak solutions with **prescribed energy**
  $e(t)$, vorticity $\in C^0_tL^1_x$, via convex integration + intermittent
  Beltrami waves ($\|W\|_{L^1}\ll\|W\|_{L^2}$). **NOT Leray-Hopf** (no energy
  inequality, no $L^2_t\dot H^1_x$); $\beta<\tfrac12$ is the weak-strong-
  uniqueness barrier; Leray-Hopf nonuniqueness remains the **major open**
  problem. **Two echoes:** the BV construction **fails in 2D** (too few
  directions to oscillate) — a second 2D/3D dividing fact alongside the Serrin
  equality; and weak-strong uniqueness ($\beta=\tfrac12$) marks the class where
  the energy-control (Leray-Hopf) would forbid nonuniqueness — the control-step
  shape again. `progress.md`'s "(non-unique?)" on Leray-Hopf resolved
  (uniqueness still open; nonuniqueness only below Leray-Hopf). All to-verify
  items now resolved.
- **attempt-04 (primary-source, arXiv HTML):** the two 2024 axisymmetric
  preprints verified. Hou 2405.10916 — two-section generalized-axisymmetric
  blowup (Sec 4 solution-dependent viscosity, self-similar n≈3.188→3, BKM-
  violating O(1/(T−t)); Sec 5 two-constant-viscosity Boussinesq, nearly
  self-similar with log correction λ=(1+ε|log(T−t)|)^(−1/2), n≈4.73);
  generalized NOT true constant-viscosity 3D NS (caveat confirmed).
  Seregin 2402.13229 — Euler-scaling exclusion of exact & discrete
  self-similar Type II axisymmetric blowup (no-swirl limiting Euler +
  weighted-vorticity conservation + irrotationality contradiction; Prop
  3.1/4.1 U≡0). **Complementary not contradictory:** Seregin fences off
  the classical self-similar class; Hou's nearly-self-similar/generalized
  candidate lives outside it. Refined open content: true blowup must be
  non-(discrete-)self-similar AND bridge generalized→true viscosity.
  Control-step echo recorded (Seregin's engine controls the self-similar
  slice; the non-self-similar slice is where it stops). Claims resolved;
  publication status still to-verify (both arXiv preprints).
- **attempt-05 (status-check):** publication-status flag **resolved for
  Hou, persists for Seregin.** **Hou 2024 is now PUBLISHED** —
  *Foundations of Computational Mathematics* (Springer, 2026), DOI
  10.1007/s10208-026-09748-8 (= arXiv:2405.10916); peer-reviewed; the
  generalized-not-true-NS caveat survives publication. **Seregin 2024
  (2402.13229) still a preprint** (no journal DOI found; the published
  Seregin piece is the *distinct* 2023 cpaa note, DOI
  10.3934/cpaa.2023108). So the Hou/Seregin pair is now **asymmetric in
  peer-review status**: the candidate outside the fence (Hou) is
  published, the fence itself (Seregin 2024) is not — sharpening the
  honesty framing without moving the slice boundary. Community
  reception: active/supportive (Courant + UCB/LBL seminars; a related
  quasi-exact-1D-model Nonlinearity paper, DOI 10.1088/1361-6544/ad1c2f),
  no refutation found. Frontier + control-step obstruction unchanged.
- **attempt-06 (direction-(B) ingredient + cross-problem pattern
  sharpening):** verified the Hou-Wang quasi-exact 1D model — *Blowup
  analysis for a quasi-exact 1D model of 3D Euler and Navier–Stokes*,
  **Nonlinearity 37 (2024)**, DOI 10.1088/1361-6544/ad1c2f (arXiv:2306.04146),
  peer-reviewed, CONFIRMED. The Hou-Li (2008, CPAM) 1D model is
  "quasi-exact" (solutions construct exact 3D Euler/NS solutions when
  angular velocity/vorticity/stream are linear in $r$ — a special ansatz).
  It achieves **rigorous finite-time blowup in three WEAKENED regimes**:
  inviscid + weakened advection ($a<1$, smooth, self-similar); original
  inviscid ($a=1$) with Hölder $C^\alpha$ data (Hou-Li $C^1$
  well-posedness sharp); viscous + weakened advection ($a<1,\nu>0$,
  finite-time, no exact self-similar profile). Method = dynamic rescaling
  + singularly weighted $L^2$ + sharp nonlocal estimates, **computer-
  assisted** (interval arithmetic). **Sharpens the "one-dimensional engine
  stops" 6-for-6 sub-pattern:** the 1D engine does NOT stop at blowup —
  it *achieves* rigorous blowup (resolution, in weakened slices); it stops
  at the **control step** from the weakened/1D slice to full-strength 3D
  smooth data (the Millennium problem). The cleanest NS mirror of the
  Beal/Hodge/BSD control-step framing: a tool that fully resolves a slice
  but cannot bridge to the universal case. **Viscosity alone does not
  prevent blowup** in the 1D model *with weakened advection* (regime 3) —
  isolating vortex-stretching vs advection; the full 3D question (full
  advection + viscosity) remains open. Pairs with Hou's 3D
  nearly-self-similar candidate (attempt-05): 1D = rigorous blowup
  (resolution); 3D generalized = candidate (control step, open). Related,
  to-verify: Huang-Qin-Wang-Wei CMP 406:243 (2025), Hou-Luo model, purely
  analytic Schauder blowup; Hou-Qin-Wang arXiv:2606.26658 (2026 preprint).
  Outcome confirmed, partial overall (Millennium problem untouched;
  direction-(B) ingredient, not a proof move).
- **attempt-07 (primary-source verification — Seregin status + HQWW CMP 2025):**
  the two remaining attempt-06 to-verify items resolved. **(i) Seregin 2024
  (2402.13229) publication status RESOLVED: still a preprint** — no journal
  DOI; the revised version (Oct 8, 2024) is retitled *"A note on potential
  Type II blowups of axisymmetric solutions to the Navier-Stokes equations"*
  (dedicated to Nadirashvili); Seregin's own July 2025 preprint cites it as
  a preprint. The **published** Seregin piece is the predecessor: *Remarks
  on Type II blowups*, **CPAA 23(10) (2024), 1389–1406**, DOI
  10.3934/cpaa.2023108. **NEW: Seregin July 2025 preprint
  (arXiv:2507.08733)** — the Type II exclusion program continues. The
  Hou/Seregin peer-review asymmetry persists (Hou published, Seregin 2024
  not) but the fence has a published predecessor + a 2025 extension.
  **(ii) Huang–Qin–Wang–Wei CMP 406:243 (2025) CONFIRMED** — *Exact
  Self-Similar Finite-Time Blowup of the Hou–Luo Model with Smooth Profiles*,
  DOI 10.1007/s00220-025-05429-9, arXiv:2308.01528: **purely analytic**
  (Schauder fixed point, no computer assistance) exact self-similar blowup
  with $C^\infty$ profiles; $2<c_l\le4.5298$ (cruder than Chen–Hou–Huang's
  computer-assisted $2.99870\pm6\times10^{-5}$ but analytic); builds on their
  ARMA 248 (2024) generalized-CLM framework; next target 2D Boussinesq.
  **Sharpening:** the 1D engine now achieves blowup *fully analytically*
  (resolution side); the control step (1D → 3D) remains the wall — the
  cleanest NS mirror of the control-step thesis. Outcome confirmed
  (verification + sharpening), partial overall (Millennium problem
  untouched).
- **attempt-08 (primary-source verification — Seregin 2025 + HQW 2026 + NEW
  Leray–Hopf claim):** the two remaining to-verify items resolved, plus a
  potentially landmark 2026 preprint surfaced. **(i) Seregin 2025
  (arXiv:2507.08733) CONFIRMED** — *A note on certain scenarios of Type II
  blowups of suitable weak solutions to the NS equations* (July 11, 2025,
  preprint): Euler scaling + **Liouville-type theorems for ancient Euler
  solutions** (a new engine for the fence); Thm 2.1 excludes a Type II
  scenario for a parameter region and shows a CPAA 2024 restriction was too
  strong (the fence is widening); Thm 5.1 rules out the scenario under an
  LPS-type condition. **(ii) Hou–Qin–Wang 2026 (arXiv:2606.26658)
  CONFIRMED** — *Exact Blowup Analysis for the Weak-Advection Hou–Li Model*
  (June 25, 2026, preprint): exact self-similar blowup for $2/3<a<1$
  (periodic) and $0<a\le1$ (whole-space, Neumann), with a profile-type
  trichotomy (focusing / non-expanding-non-focusing / expanding) — the 1D
  resolution side is now essentially complete. **(iii) NEW MAJOR:
  Hou–Wang–Yang 2026 (arXiv:2509.25116v2, v2 Aug 11, 2026)** — *Nonuniqueness
  of Leray–Hopf solutions to the unforced incompressible 3D Navier–Stokes
  Equation*: claims the first rigorous **computer-assisted** proof of
  Leray–Hopf nonuniqueness (infinitely many distinct suitable Leray–Hopf
  solutions, same divergence-free data; code at
  github.com/HouGroup2026/3d-navier-stokes-nonuniqueness). This is exactly
  the attempt-03 "**major open** problem" — if confirmed, the Leray–Hopf
  uniqueness question (open since Leray 1934) is settled negatively.
  **Flags: preprint, computer-assisted, search-surfaced — the single most
  consequential NS `to-verify` item.** Does NOT resolve the Millennium
  problem (regularity/breakdown), but sharpens the weak-solution landscape.
  Outcome confirmed (verification + a major new claim flagged), partial
  overall (Millennium problem untouched).

## To-verify (flagged, from search summaries — not primary-source-verified)

- [ns-millennium-fefferman]: **CONFIRMED (attempt-03, primary source).**
  Fefferman's official Clay formulation (May 1, 2000); two no-boundary settings
  ($\mathbb R^3$ decay, $\mathbb T^3$ periodic); four statements A/B
  (existence-smoothness, $f\equiv0$) and C/D (breakdown, smooth $f$ allowed);
  proving any one resolves the prize. Upgraded from `to-verify` to verified.
- [ns-serrin]/[ns-ess-endpoint]: **CONFIRMED (attempt-02).** Escauriaza–Seregin
  –Šverák, Russian Math. Surveys 58:2 (2003), 211–250 (DOI
  10.1070/RM2003v058n02ABEH000609) — $L^\infty_tL^3_x$ solutions smooth (endpoint
  Serrin $3/s+2/\ell=1$); via backward uniqueness + Carleman. Convention note:
  our $2/r+3/s=1$ (time,space) = their $3/s+2/\ell=1$ (space,time), same condition.
- [ns-tao-quant-l3]: **CONFIRMED (attempt-02).** Tao, Proc. Symp. Pure Math
  (2021), arXiv:1908.04958 (DOI 10.1090/pspum/104/01874) —
  $\limsup\|u\|_{L^3}/(\log\log\log(1/(T^*-t)))^c=\infty$ (triple log). Barker
  (2022, arXiv:2209.15627) localized it. **Mislabel corrected:** Palasek (2022,
  arXiv:2111.08991) extended to **$d\ge4$** (quadruple log), NOT axisymmetric.
- [ns-buckmaster-vicol]: **CONFIRMED + SHARPENED (attempt-03, primary
  source).** Buckmaster–Vicol, *Annals* **189**(1) (2019), 101–144 (DOI
  10.4007/annals.2019.189.1.3) — nonuniqueness of $C^0_tH^\beta_x$ ($\beta<
  \tfrac12$) weak solutions with prescribed energy $e(t)$, vorticity $\in
  C^0_tL^1_x$, via convex integration + intermittent Beltrami waves. **NOT
  Leray-Hopf** (no energy inequality); $\beta<\tfrac12$ = weak-strong-
  uniqueness barrier; fails in 2D; Leray-Hopf nonuniqueness still **major
  open**. *Correction:* the result is **2019**, not 2022; the 2022 JEMS
  follow-up is Buckmaster–**Colombo**–Vicol (a distinct paper). Upgraded from
  `to-verify` to verified.
- Hou 2024 (arXiv:2405.10916) and Seregin 2024 (arXiv:2402.13229): **CLAIMS
  CONFIRMED (attempt-04, arXiv HTML primary source)** — two-section Hou
  construction (Sec 4 solution-dependent viscosity self-similar n≈3.188→3;
  Sec 5 two-constant-viscosity Boussinesq nearly-self-similar with log
  correction, n≈4.73) + Seregin Euler-scaling no-swirl/weighted-vorticity
  exclusion of exact & discrete self-similar Type II blowup (Prop 1.1/2.1/
  2.2/3.1/4.1); complementary-not-contradictory relationship pinned;
  generalized-axisymmetric-not-true-NS caveat confirmed. **Publication
  status: Hou RESOLVED (attempt-05) — published *Found. Comput. Math.*
  (2026), DOI 10.1007/s10208-026-09748-8 (peer-reviewed). Seregin 2024
  (2402.13229) STILL `to-verify` (preprint, no journal DOI; the published
  Seregin piece is the distinct 2023 cpaa note, DOI 10.3934/cpaa.2023108).
  Asymmetric peer-review status recorded (Hou published, Seregin 2024
  not); both claims treated as evidence for true-NS — Hou now
  peer-reviewed as a *generalized*-model blowup. **Seregin status RESOLVED
  (attempt-07):** 2402.13229 remains a preprint (revised Oct 2024, retitled
  "A note on potential Type II blowups..."; Seregin's own 2025 preprint
  cites it as a preprint). The published Seregin piece is the predecessor
  CPAA 23(10) (2024), 1389–1406, DOI 10.3934/cpaa.2023108. NEW: Seregin
  July 2025 preprint arXiv:2507.08733 (Type II exclusion scenarios) —
  content `to-verify`.
- Huang–Qin–Wang–Wei CMP 406:243 (2025): **CONFIRMED (attempt-07).** *Exact
  Self-Similar Finite-Time Blowup of the Hou–Luo Model with Smooth Profiles*,
  DOI 10.1007/s00220-025-05429-9, arXiv:2308.01528 — **purely analytic**
  Schauder fixed-point proof (no computer assistance) of exact self-similar
  blowup with $C^\infty$ profiles for the 1D Hou–Luo model; $2<c_l\le
  2(\alpha+1)/(\alpha-1)\approx4.5298$; builds on their ARMA 248 (2024)
  generalized-CLM framework; next target 2D Boussinesq. Upgraded from
  `to-verify` to verified.
- Hou–Qin–Wang arXiv:2606.26658 (2026 preprint): **CONFIRMED (attempt-08).**
  *Exact Blowup Analysis for the Weak-Advection Hou–Li Model* (June 25, 2026):
  exact self-similar blowup for $2/3<a<1$ (periodic) and $0<a\le1$
  (whole-space, Neumann), profile-type trichotomy; fixed-point + ODE
  extension. Upgraded from `to-verify` to verified.
- Seregin 2025 (arXiv:2507.08733): **CONFIRMED (attempt-08).** *A note on
  certain scenarios of Type II blowups of suitable weak solutions to the NS
  equations* (July 11, 2025, preprint): Euler scaling + Liouville-type
  theorems for ancient Euler solutions; Thm 2.1 (parameter region excluding
  Type II, relaxing a CPAA 2024 restriction); Thm 5.1 (LPS-type condition).
- [ns-hou-wang-yang-2026] (NEW, attempt-08, **to-verify — HIGH PRIORITY**):
  Hou–Wang–Yang, *Nonuniqueness of Leray–Hopf solutions to the unforced
  incompressible 3D Navier–Stokes Equation*, arXiv:2509.25116v2 (v2 Aug 11,
  2026). Claims the first rigorous **computer-assisted** proof of Leray–Hopf
  nonuniqueness (infinitely many distinct suitable Leray–Hopf solutions,
  same divergence-free data; code at
  github.com/HouGroup2026/3d-navier-stokes-nonuniqueness). This is the
  attempt-03 "major open problem." Preprint + computer-assisted +
  search-surfaced — verify against the arXiv HTML/PDF (and code) before
  load-bearing reuse. The natural attempt-09 target.

## Honesty check

No proof of global regularity or blowup. The realistic goal (as for Beal/BSD)
is a precise, sourced, compounding frontier — the exact obstruction
(supercriticality → no global critical bound), the unifying lens (critical vs
subcritical norms; Serrin-number equality in 2D), the verified
local/weak/conditional base, and concrete forward directions (A/B/C). That
compounds; a future session extends it rather than re-deriving.