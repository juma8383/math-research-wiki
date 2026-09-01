# Progress — Yang-Mills existence and mass gap

> Running state of the attack. Read this first when resuming. Consolidated
> through attempt-06. Same methodology as [[beals_conjecture]],
> [[birch_swinnerton_dyer]], [[navier_stokes]]: locate the exact frontier,
> name the open content, map the obstruction at the *control* step (not the
> resolution step), unify threads.

## The exact frontier

The Millennium problem (Jaffe-Witten) [ym-clay-jaffe-witten] has TWO coupled
open pieces, both required:
1. **Existence**: a rigorous non-perturbative construction of 4D quantum YM
   for a compact simple $G$ satisfying Wightman/OS axioms
   [[def-wightman-os-axioms]] [ym-existence-open].
2. **Mass gap** $\Delta>0$: the lightest excitation is massive
   [[def-mass-gap-confinement]] [ym-mass-gap].

Known (the verified base):
- Classical YM [[def-yang-mills-theory]]; asymptotic freedom (perturbative UV)
  [[thm-asymptotic-freedom]] [ym-asymptotic-freedom].
- Lattice YM rigorously defined at finite spacing; reflection positivity,
  transfer matrix, strong-coupling area law [[thm-lattice-gauge-constructive]]
  [ym-lattice-constructive]; mass gap **numerically** confirmed.
- RG machinery (Balaban, Magnen-Rivasseau-Sénéor, AFS) [[thm-balaban-rg]]
  [ym-balaban-rg] — the continuum-limit control machinery, incomplete.
- Supersymmetric YM (Seiberg-Witten, Nekrasov)
  [[thm-seiberg-witten-supersymmetric]] [ym-supersymmetric] — a solved RELATED
  problem, not the original.

The **open content** (analog of Beal's "finitely many → zero", BSD's "rank ≤1
→ arbitrary rank", NS's "small data → arbitrary large-data global regularity"):
**"lattice-discretized + numerically confirmed → continuum-rigorous 4D QFT with
a proven spectral gap"**, equivalently **"asymptotic freedom (perturbative UV)
→ confinement (non-perturbative IR) rigorously."**

## The obstruction: control step, not resolution step

The *resolution* machinery works and finished the verified base:
- **Lattice YM** is rigorously defined (finite-dim integrals over holonomies)
  [[thm-lattice-gauge-constructive]].
- **Reflection positivity / transfer matrix** (OS, Lüscher) give a sensible
  Euclidean QFT at finite spacing.
- **Strong-coupling cluster expansion** gives confinement/area law at finite
  spacing.
- **Asymptotic freedom** gives perturbative control in the UV
  [[thm-asymptotic-freedom]].

The gap is a **control step**, exactly parallel to the other three problems:
- **(1) Continuum-limit control**: prove convergence as $a\to0$ to a
  non-trivial 4D QFT satisfying the OS/Wightman axioms — including FULL $O(4)$
  Euclidean covariance (Eriksson 2026 explicitly only gets hypercubic $W^4$
  covariance [ym-recent-claims-unverified]). This IS the "existence" piece.
- **(2) IR mass-gap control**: prove $\Delta>0$ with a bound uniform in $a$ in
  the strongly-coupled IR, where asymptotic freedom gives no expansion
  parameter. This is the "mass gap" piece.

Both are *control* (of the limit / of the IR spectrum), not *resolution*. The
lattice object is built; the gap is **controlling the limit and transporting
the spectral gap across RG scales** [[method-constructive-continuum-limit]].

**attempt-02 precision (Balaban scope, primary-source verified):** Balaban's
11 papers (CMP 95–122, 1984–89) prove **UV stability** — effective-density
bounds **uniform in the lattice spacing** $\varepsilon$, i.e. asymptotic freedom
made constructive on the lattice, controlling the *short-distance / weak-coupling*
regime. They **leave open** the continuum limit, mass gap, and IR. So Balaban =
the **UV half** of the UV→IR bridge, not the bridge. The mass gap is an IR
(strong-coupling, long-distance) statement; the strong-coupling cluster
expansion proves a gap only at *finite* spacing / *large* bare $g_0$, while the
continuum-limit point sits at *weak* bare $g_0$ ($g(a)\to0$, asymptotic
freedom) where that expansion has no parameter. **The blocker is a bound
uniform in $a$ bridging the strong↔weak bare-coupling crossover** — the
literal UV→IR "control runs out" boundary. **$O(4)$ restoration** is its
second face: the lattice has only hypercubic $W^4$; full $O(4)$ is restored
only as the $O(4)$-breaking irrelevant operators vanish *uniformly down to
long distances*, which loops back to continuum-limit existence itself.

## The uniquely-hard extra wrinkle

Unlike NS/BSD/Beal — where the object (PDE/curve/conjecture) is defined — here
**a precise non-perturbative definition of 4D quantum gauge theory is itself
open** [ym-existence-open] (Jaffe-Witten). The **Gribov ambiguity**
(gauge-fixing non-uniqueness in the continuum) is a framework-level obstacle
the others lack; its continuum resolution is not universally accepted. So the
attack must partly *construct the framework* as well as prove a theorem within
it.

## The unifying lens: dimensional transmutation

Classical 4D YM is scale-invariant (the coupling $g$ is dimensionless in 4D)
[ym-dimensional-transmutation]. The mass gap is a **quantum-generated scale**
$\Lambda_{\text{YM}}\sim \tfrac1a e^{-\text{const}/g^2}$ (from the 1-loop
β-function, $\beta_0=11N/(48\pi^2)$). Hence the continuum limit (fix
$\Lambda_{\text{YM}}$ as $a\to0$, so $g(a)\to0$ — asymptotic freedom) and the
mass gap ($\Delta\sim\Lambda_{\text{YM}}$) are **the same RG problem**:
controlling the running coupling from the perturbative UV into the
non-perturbative IR. The obstruction is precisely the UV→IR bridge.

## Candidate forward directions

- **(A) Lattice → continuum constructive program**
  [[method-constructive-continuum-limit]]: Balaban RG + cluster expansions +
  OS reconstruction; transport a lattice spectral gap to the continuum with a
  uniform-in-$a$ bound. The Faizal-Shabir / Eriksson / Gutierrez Ule attempts
  are this direction [ym-recent-claims-unverified], but all conditional on
  unverified bounds (Balaban RG multiscale estimates, AFS for $SU(N)$, Gribov
  resolution, $O(4)$ covariance).
- **(B) Non-lattice / geometric**: holographic QCD (AdS-CFT) for
  strongly-coupled analytic handles; Seiberg-Witten/Nekrasov for supersymmetric
  YM (a solved model illuminating the gap mechanism); integrability of N=4 SYM.
  Gives mass-gap-like results in RELATED theories, not the original. **Mechanism
  named (attempt-03):** dual-Meissner monopole condensation ('t Hooft–Mandelstam
  dual superconductivity), exact in $N{=}2/ N{=}1$ SUSY — the *control* (SUSY
  localization + holomorphy) is what pure YM lacks.
- **(C) Probabilistic / stochastic**: Chatterjee's probabilistic confinement
  mechanism (2021); regularity-structure / SPDE approaches (Hairer) to
  construct the YM measure directly, bypassing the lattice.
  **attempt-04 sharpening (primary-source, CMP 2021, DOI
  10.1007/s00220-021-04086-y):** Chatterjee proves **unbroken center
  symmetry $\Rightarrow$ confinement (area law)** (Thm 2.2) and
  **exponential decay of correlations (under arbitrary BCs) $\Rightarrow$
  unbroken center symmetry $\Rightarrow$ confinement** (Thm 2.4) — the
  first rigorous definition of center symmetry for lattice gauge theories
  (previously a 't Hooft heuristic). **Crucial: the chain is
  mass-gap $\Rightarrow$ center-symmetry $\Rightarrow$ confinement — the
  mass gap (exponential decay) is the HYPOTHESIS, not the CONCLUSION.**
  Chatterjee proves confinement *follows from* the mass gap; he does NOT
  prove the mass gap exists. The mass gap is easy at strong coupling
  (cluster expansion), **open/believed at weak coupling** — exactly the
  UV→IR bridge. So direction (C) **relocates**, not removes, the control
  step: the resolution side (center symmetry $\Rightarrow$ confinement)
  is done; the control step (exponential decay at weak coupling = the
  mass gap) is the open piece, now triangulated from a third angle (after
  Balaban's UV half and SUSY dual-Meissner). **Control-step echo:**
  Chatterjee's engine controls the center-symmetry$\Rightarrow$confinement
  slice (resolution); the mass-gap-at-weak-coupling slice is where it
  stops — the "one-dimensional engine stops" shape, parallel to NS
  Seregin (attempt-04) and BSD cyclotomic/anticyclotonic disjointness
  (attempt-04).

## Best partial result so far (attempt-02)

- Frontier located (existence + mass gap, both required), open content named,
  obstruction mapped to two *control* steps (continuum-limit control + IR
  mass-gap control) with the dimensional-transmutation / UV→IR unifying lens.
  Eight theory pages + one survey source filed. Cross-problem methodology now
  4-for-4: all Millennium-class problems have the obstruction at the
  control/reduction step, not the resolution step — with YM adding the
  framework-existence wrinkle.
- **attempt-02 (primary-source verification + direction A):** `[ym-clay-jaffe-witten]`
  **CONFIRMED** (Clay official page — exact wording + "at least as strong" clause
  making OS reflection positivity a *hard requirement* + the framework-existence
  quote). `[ym-balaban-rg]` **CONFIRMED + sharpened** (Balaban CMP 95–122 +
  Dimock exposition): Balaban proves UV stability (uniform-in-$\varepsilon$
  density bounds) and leaves continuum limit / mass gap / IR open — i.e. the
  UV half of the bridge. Direction (A) deepened: the concrete blocker is a
  uniform-in-$a$ IR bound bridging the **strong↔weak bare-coupling crossover**
  (strong-coupling cluster expansion gives a gap only at finite spacing / large
  $g_0$; the continuum point is at weak $g_0$ where it has no parameter);
  $O(4)$ restoration is the same control problem's second face.
  `[ym-recent-claims-unverified]` sharpened: Eriksson 2026 is **viXra-only**
  (unmoderated), **conditional on Assumption A**, and leaves OS reflection
  positivity / thermodynamic limit / mass gap / nontriviality OPEN even
  conditionally; an **open discrepancy** (abstract "Euclidean-covariant" vs
  body-level "hypercubic $W^4$") is flagged for body-level verification.
  Remaining to-verify: `[ym-supersymmetric]` (Seiberg-Witten/Nekrasov scope).
- **attempt-03 (primary-source verification):** `[ym-supersymmetric]`
  CONFIRMED + sharpened — Seiberg-Witten (1994) + Nekrasov (2003, rigorous
  Nakajima–Yoshioka 2005) are for $N{=}2$ SUSY YM, not pure YM; the gap +
  confinement arise via **dual-Meissner monopole condensation** only after
  softly breaking $N{=}2\to N{=}1$ (pure $N{=}2$ has a Coulomb moduli space,
  no generic gap). SUSY is essential (localization $Q$ + holomorphic
  prepotential); **no known bridge to pure YM**. Direction (B) mechanism
  named: the *control* that makes the dual-superconductor picture exact in
  SUSY (localization + holomorphy) is exactly what pure YM lacks — the YM
  instance of the 6-for-6 control-step spine, triangulated with the Balaban
  UV-half picture (attempt-02) from the continuum-SUSY side. All
  load-bearing to-verify items now resolved (Eriksson remains a preprint-
  status item, not load-bearing).
- **attempt-04 (primary-source verification + recent-claims flag):** direction
  (C) Chatterjee 2021 CONFIRMED (CMP, DOI 10.1007/s00220-021-04086-y):
  center-symmetry $\Rightarrow$ confinement (Thm 2.2) and exponential-decay
  $\Rightarrow$ center-symmetry $\Rightarrow$ confinement (Thm 2.4); first
  rigorous definition of lattice center symmetry. **Sharpening: the mass
  gap is the hypothesis, not the conclusion** — Chatterjee proves
  confinement *follows from* the mass gap, not its existence; the mass gap
  at weak coupling (exponential decay) is the open piece = the UV→IR
  bridge. Direction (C) relocates (not removes) the control step, now
  triangulated from three angles (Balaban UV-half / SUSY dual-Meissner /
  Chatterjee mass-gap$\Rightarrow$confinement). **2025-26 preprint wave
  flagged** `ym-recent-claims-unverified` (extension of attempt-02 list):
  Shabir-Faizal 2026 (arXiv:2606.19362, ~200pp, unpeer-reviewed, claims
  spectral gap + continuum area law + universality, companions IJGMMP
  2026), Agawa 2025 (Cambridge Open Engage, AI-assisted, unaffiliated,
  addendum needed), Eriksson 2026 (viXra, already flagged). NONE
  peer-accepted; each with conditional assumptions or identified gaps.
- **attempt-05 (status-check):** Faizal-Shabir 2026 **publication-status
  RESOLVED + upgraded to peer-reviewed** — a **four-part series in IJGMMP**
  (Int. J. Geom. Meth. Mod. Phys., World Scientific, 2026), all "Refereed,"
  indexed WoS/Scopus, DOIs 10.1142/S0219887826501112–6501148 (Part 1
  6501148 / Part 2 6501136 / Part 3 6501124 / Part 4 6501112;
  arXiv:2606.19362 consolidated). **Name order corrected** to Faizal &
  Shabir (attempt-04 wrote "Shabir & Faizal"; to-verify against the arXiv
  author list). **Sharper honesty framing (the load-bearing point):**
  IJGMMP is a **mid-tier** venue (not CMP/Inventiones/JAMS/Annals); the
  **claim is far stronger** (full 4D YM + proven continuum mass gap =
  Millennium) than Kim (Trans. AMS) or Hou (FoCM) yet the **venue is far
  weaker** — evidence/claim ratio inverted. Clay has **not**
  accepted/verified; no independent community verification; the
  attempt-04 technical caveats (admissible-class framework,
  RG-interlacing defect summability) are **unaddressed by publication**.
  So the flag is **renamed, not removed**: publication-status resolved,
  **substantive-acceptance flag raised** (editorial bar ≠
  community-acceptance bar). Chatterjee 2021 line has a **2025 follow-up**
  (arXiv:2505.16585 "Expanded regimes of area law," Bonn workshop 2025-07)
  — active, but still **resolution-side** (confinement/area law), not the
  mass-gap control step. Agawa 2025 / Eriksson 2026 **not** re-checked
  this cycle (budget); remain at attempt-04 status. Frontier +
  control-step obstruction unchanged.
- **attempt-06 (preprint-wave re-check, the option-(a) deferred from
  attempt-05):** closed both deferred items. **Agawa 2025 — the addendum is
  RETRACTED.** The companion addendum (DOI 10.33774/coe-2025-3jmcf, v1
  2025-06-18 / v2 2025-07-20) is marked "Retracted" in the Cambridge Open
  Engage version history; Cambridge Open Engage is explicitly "not
  peer-reviewed by Cambridge University Press"; author unaffiliated, 0
  citations, extensive ChatGPT/Gemini use. So the attempt-04/05 "addendum
  needed" flag is **RESOLVED IN THE NEGATIVE** — the addendum was posted
  (continuum-limit RG stability + finite-Gribov Morse theory) and then
  retracted. Agawa = a non-result; removed from the active to-verify list.
  **Eriksson 2026 — still ai.viXra.org ("AI assisted e-prints," not
  peer-reviewed), but the author's own §8.2 self-concedes the exact control
  step.** "Assumption A" appears in three undischarged forms: blocking-map
  squared-oscillation summability (viXra:2602.0077, conditional); gradient-
  flow $L^1$ scale-consistency (viXra:2602.0085, unconditional for standard
  observables via Wilson-flow Thm 3.11, conditional for the full algebra);
  two-layer RG-Cauchy (viXra:2602.0063) — naive asymptotic-freedom gives a
  **non-summable $O(1/k)$ rate** (logarithmic divergence), "we do not prove
  the RG-Cauchy estimate from first principles." The gradient-flow variant
  is a resolution-side improvement (Thm 3.11 unconditional for standard
  observables) that shifts but does not remove the open control step (now
  $L^1$ scale-consistency + reflection positivity, both open). **This is an
  independent confirmation, from inside an attempted proof, of the UV→IR
  bridge obstruction** the wiki named from three angles (Balaban UV-half /
  SUSY dual-Meissner / Chatterjee mass-gap⇒confinement): Eriksson's
  non-summable $O(1/k)$ RG-Cauchy rate IS the "one-dimensional engine stops"
  shape — the RG engine (resolution, UV scale-by-scale) stops at the
  summable-Cauchy / continuum-limit control step. **Honesty:** both items
  are AI-assisted preprints; their value is corroborative not probative (a
  flawed attempt failing does not prove the problem is hard) — a weak but
  real convergent signal. Substantive-acceptance flag (attempt-05)
  REINFORCED: even the most extensive preprint-wave attempt (Eriksson, 68
  papers) explicitly concedes the control step. Frontier + control-step
  obstruction unchanged. Outcome confirmed, partial overall.

## To-verify (flagged, from search summaries — not primary-source-verified)

- [ym-clay-jaffe-witten]: **CONFIRMED (attempt-02).** Exact Jaffe-Witten wording
  + "at least as strong" Wightman/OS clause + framework-existence quote, against
  the Clay official page. OS reflection positivity is a hard requirement.
- [ym-balaban-rg]: **CONFIRMED (attempt-02).** Balaban (CMP 95–122, 1984–89) +
  Dimock (RMP 25/JMP 54/AHP 15, 2013–14): UV stability (uniform-in-$\varepsilon$
  effective-density bounds) proven; continuum limit / mass gap / IR open.
- [ym-recent-claims-unverified]: **sharpened, status-split (attempt-05).**
  Eriksson 2026 is viXra-only (unmoderated), conditional on Assumption A,
  leaves OS positivity / thermodynamic limit / mass gap / nontriviality
  open even conditionally; open discrepancy: abstract "Euclidean-covariant"
  vs body "hypercubic $W^4$ only" — to resolve against the paper body.
  **attempt-04 extension:** a 2025-26 preprint wave also flagged —
  Faizal-Shabir 2026 (arXiv:2606.19362), Agawa 2025 (Cambridge Open Engage,
  AI-assisted, unaffiliated, addendum needed for continuum limit + finite
  Gribov). **attempt-05:** Faizal-Shabir 2026 **publication-status
  RESOLVED** — published as a four-part peer-reviewed series in IJGMMP
  (World Scientific, 2026), "Refereed," indexed WoS/Scopus, DOIs
  10.1142/S0219887826501112–6501148 (= arXiv:2606.19362 consolidated);
  name order corrected to Faizal & Shabir (to-verify vs arXiv author list).
  **But a NEW substantive-acceptance flag raised:** IJGMMP is mid-tier
  (not CMP/Inventiones/JAMS/Annals); Clay has NOT accepted/verified; no
  independent community verification; the attempt-04 technical caveats
  (admissible class, RG-interlacing defect summability) unaddressed by
  publication — peer review ≠ solution acceptance for a Millennium claim.
  Agawa 2025 / Eriksson 2026 not re-checked this cycle (budget), remain
  at attempt-04 status (preprint / viXra).
  **attempt-06 (re-check):** **Agawa 2025 RESOLVED (negatively)** — the
  addendum (DOI 10.33774/coe-2025-3jmcf) is RETRACTED (both v1/v2 marked
  "Retracted"); Cambridge Open Engage is explicitly not peer-reviewed;
  unaffiliated + AI-assisted + 0 citations → a non-result, removed from
  the active list. **Eriksson 2026 UPDATED (still viXra/"AI assisted
  e-prints," not peer-reviewed)** but its §8.2 self-concession corroborates
  the control step: Assumption A undischarged in three forms (blocking-map
  oscillation summability viXra:2602.0077; gradient-flow $L^1$ scale-
  consistency viXra:2602.0085, unconditional for standard observables via
  Wilson-flow Thm 3.11, conditional for the full algebra; two-layer
  RG-Cauchy viXra:2602.0063 — naive asymptotic freedom gives a
  **non-summable $O(1/k)$ rate**, logarithmic divergence, not proven from
  first principles). Non-summability IS the UV→IR-bridge / "one-dimensional
  engine stops" obstruction, independently conceded from inside an
  attempted proof — corroborative, not probative (AI-assisted preprint).
  Substantive-acceptance flag (Faizal-Shabir) REINFORCED.
- [ym-chatterjee-confinement]: **CONFIRMED (attempt-04, primary source).**
  Chatterjee, *Comm. Math. Phys.* (2021), DOI 10.1007/s00220-021-04086-y.
  Thm 2.2 unbroken center symmetry $\Rightarrow$ confinement (area law);
  Thm 2.4 exponential decay $\Rightarrow$ unbroken center symmetry
  $\Rightarrow$ confinement; first rigorous lattice center-symmetry
  definition. **The mass gap (exponential decay) is the hypothesis, not the
  conclusion** — the open piece is exponential decay at weak coupling = the
  UV→IR bridge. Direction (C) verified + shown to relocate (not remove)
  the control step. Upgraded from named-but-unverified to verified.
- [ym-supersymmetric]: **CONFIRMED + SHARPENED (attempt-03, primary
  sources).** Seiberg-Witten (Nucl. Phys. B 426, 1994, hep-th/9407087) and
  Nekrasov (hep-th/0306211, rigorous Nakajima–Yoshioka Invent. Math. 2005) are
  for **$N{=}2$ SUSY YM**, not pure YM. The mass gap + confinement arise via
  **dual-Meissner monopole condensation** (the 't Hooft–Mandelstam dual-
  superconductor picture, made exact by SUSY) — but **only after softly
  breaking $N{=}2\to N{=}1$** ($W=m\,\mathrm{Tr}\Phi^2$): pure $N{=}2$ has a
  Coulomb-branch moduli space with *no* generic mass gap. SUSY is essential
  (the localization supercharge $Q$ + holomorphic prepotential), with **no
  known bridge to pure YM**. Direction (B) mechanism now named + scoped.
  Upgraded from `to-verify` to verified.

## Honesty check

No rigorous 4D quantum YM, no proven mass gap. The recent preprints are
flagged unverified, not solutions. The realistic goal (as for the other three)
is a precise, sourced, compounding frontier — the exact obstruction
(continuum-limit + IR-gap control; the UV→IR bridge; framework-existence
wrinkle), the unifying lens (dimensional transmutation), the verified
lattice/AF/constructive base, and concrete directions (A/B/C). That compounds.