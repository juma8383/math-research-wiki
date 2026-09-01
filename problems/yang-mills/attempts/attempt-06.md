---
type: attempt
problem: yang_mills
attempt: 6
date: 2026-08-25
approach: Re-check the two deferred preprint-wave items (Agawa 2025, Eriksson 2026) for peer-review / reception status — the option-(a) to-verify deferred from attempt-05 for budget
outcome: confirmed
tags: [verification, status-check, agawa, eriksson, preprint-wave, control-step, uv-ir-bridge, cross-problem, retraction, ai-assisted]
---

# Attempt 06 — Agawa 2025 RETRACTED; Eriksson 2026 self-concedes the control step (independent confirmation of the UV→IR bridge obstruction)

Resume-cycle Continue on YM (cross-problem loop, new run; user directive:
keep running until weekly > 75% then pause. Yellow zone session 1.3% /
weekly 69.8%, max 2 subagents — **0 used**, one targeted WebSearch; fresh
session after the midnight reset). Attempt-05's `Next` option (a): re-check
**Agawa 2025** and **Eriksson 2026** — the two preprint-wave items deferred
for budget — for peer-review / community reception. This cycle closes
both. Headline: one is **retracted**, the other **self-concedes the exact
control step** the wiki has named from three angles.

## Agawa 2025 — the addendum is RETRACTED (flag resolved, negatively)

**Yuta Agawa** (unaffiliated, ORCID 0009-0005-6336-0403), *A Rigorous Proof
of the Mass Gap in SU(N) Yang-Mills Theory*, Cambridge Open Engage, DOI
[10.33774/coe-2025-sgpbm](https://doi.org/10.33774/coe-2025-sgpbm)
(received 2025-03-07, v2). Companion addendum *On the Completion of
Agawa's Proof ... The Essential Addendum on the Continuum Limit and
Finite Gribov Uniqueness*, DOI
[10.33774/coe-2025-3jmcf](https://doi.org/10.33774/coe-2025-3jmcf)
(2025-06-18 v1, 2025-07-20 v2); both mirrored on Zenodo.

- **Cambridge Open Engage is explicitly "not peer-reviewed by Cambridge
  University Press"** — it is a preprint platform (DOI assignment +
  dissemination, no editorial review).
- **The addendum is RETRACTED** — both v1 and v2 are marked "Retracted" in
  the version history. (The main v2 carries no retraction marker in the
  search results but has 0 citations, author h-index 0.)
- Author acknowledges **extensive ChatGPT / Google Gemini** use; unaffiliated,
  no formal math/physics credentials.

Attempt-04/05 flagged Agawa as "preprint, unaffiliated, AI-assisted,
**addendum needed**." This cycle **resolves that flag in the negative**:
the addendum *was* posted (addressing the continuum limit via RG stability
+ finite Gribov via Morse theory) and **then retracted**. So the
"addendum needed" status is closed — the gap was addressed and the
address withdrawn. Agawa is effectively a **non-result** (retracted,
not peer-reviewed, AI-assisted, unaffiliated, uncited). **No formal
validation from the mathematical-physics community.**

## Eriksson 2026 — extensive (68 papers), still viXra, but self-concedes the control step

**Lluis Eriksson** (independent), **"The Eriksson Programme"** — 68
timestamped papers on **ai.viXra.org** (2025-12-16 → 2026-02-27), aiming
at constructive YM existence + mass gap (Clay #4). GitHub audit repo
`github.com/lluiseriksson/ym-audit`. **ai.viXra.org = "AI assisted
e-prints," not peer-reviewed** (platform: "Articles ... should be
treated as preliminary").

### Assumption A — the load-bearing undischarged control step (three forms)

Across the programme, "Assumption A" appears in related but distinct
formulations, all **undischarged**:

1. **Blocking-map paper** (viXra:2602.0077): *squared-oscillation
   summability of the blocking* — $\sum_e\mathrm{osc}_e(F\circ Q)^2\le
   C_Q\,\mathrm{Lip}(F)^2$ uniform in $k$. Conditional; "expected to follow
   from quantitative locality and smoothing" of Bałaban's averaging maps,
   **not proven** ("provide an explicit citation/lemma here once
   extracted").
2. **Gradient-flow paper** (viXra:2602.0085): **replaces the blocking
   map with Lüscher's Yang-Mills gradient flow (Wilson flow)** — the
   oscillation summability becomes **Theorem 3.11, proved unconditionally
   from heat-kernel smoothing** (a resolution-side improvement). BUT a
   **new Assumption A** appears: an $L^1$ scale-consistency condition on
   the observable family across RG scales — **unconditional for standard
   observables** (Wilson/Polyakov loops, action density), **conditional
   for the full algebra**.
3. **Two-layer paper** (viXra:2602.0063): *Assumption 3.5 (RG–Cauchy
   along the trajectory)* — a summable bound $\sum\varepsilon(a_0/2^k)<\infty$.
   **Conditional, undischarged.** "Naive asymptotic-freedom estimates give
   a **non-summable $O(g_k^2)\sim O(1/k)$ rate**" → **logarithmic
   divergence**, insufficient for a Cauchy argument. **"We do not prove
   the RG–Cauchy estimate (Assumption 3.5) from first principles."**

### The control-step echo (the load-bearing cross-problem finding)

Eriksson's own **Section 8.2 honest self-assessment** (viXra:2602.0063):

1. Assumption 3.5 (RG–Cauchy) **not proven** from first principles; naive
   estimates give **non-summable $O(1/k)$** rates (logarithmic divergence).
2. The transfer-matrix spectral gap (Assumption A.2) is **postulated, not
   derived**; the LSI results control the Glauber dynamics, not the
   transfer matrix.
3. Uniform IR positivity for Creutz ratios (Assumption 4.9, confinement)
   is **postulated**; area-law is **not derived** from the mass gap.
4. Restricted to **bounded local observables**; continuum field-strength
   correlators (requiring renormalization) **deferred**.

This is an **independent confirmation, from inside an attempted proof, of
the exact control step the wiki has named from three angles** (attempt-05):
*"the uniform-in-$a$ IR bound bridging the strong↔weak crossover (the
literal UV→IR bridge, the single load-bearing control step)."* Eriksson's
**non-summable $O(1/k)$ RG-Cauchy rate** is precisely the "one-dimensional
engine stops" sub-pattern: the **RG engine** (resolution — controls UV
behavior scale-by-scale via asymptotic freedom) **stops at the summable-
Cauchy / continuum-limit control step**. The author explicitly concedes
the bridge cannot be proven from the resolution-side tool (asymptotic
freedom) — the naive estimate diverges logarithmically. The
gradient-flow variant (Wilson flow) is a resolution-side **improvement**
(Thm 3.11, unconditional oscillation-summability for standard observables)
that **shifts but does not remove** the open control step (now the $L^1$
scale-consistency + reflection positivity, both open).

Status table (from the search): UV closure conditional (blocking) /
unconditional-for-standard-observables (gradient flow); **reflection
positivity OPEN; OS reconstruction OPEN; thermodynamic limit OPEN; mass
gap OPEN;** confinement conditional on Assumption 4.9 (undischarged);
nontriviality conditional on confinement.

## What this changes (and does not change) in the obstruction map

- **Agawa 2025: flag RESOLVED (negatively).** The "addendum needed"
  to-verify is closed — the addendum was posted and **retracted**.
  Agawa = retracted, not peer-reviewed, AI-assisted, unaffiliated, uncited
  → a non-result. Removed from the active to-verify list.
- **Eriksson 2026: flag UPDATED, not resolved.** Still viXra (AI-assisted
  e-prints), not peer-reviewed, not Clay-accepted. BUT its **self-
  assessment corroborates the 6-for-6 control-step obstruction**: the
  RG-Cauchy / UV→IR bridge fails at the control step (non-summable
  $O(1/k)$, logarithmic divergence), exactly the wall the wiki named
  independently. A **weak but real convergent signal** — an attempted
  proof's honest concession aligning with the wiki's obstruction map.
- **Substantive-acceptance flag (attempt-05) REINFORCED.** Even the most
  extensive preprint-wave attempt (Eriksson, 68 papers, with a gradient-
  flow resolution-side improvement) explicitly concedes the control step
  is undischarged. Combined with Agawa's retraction, this strengthens:
  **no preprint-wave item has cleared the control step or received
  independent validation.** The Faizal-Shabir IJGMMP publication
  (attempt-05) remains the only peer-reviewed item, and its
  substantive-acceptance flag (mid-tier venue, Clay non-acceptance,
  attempt-04 admissible-class/RG-interlacing caveats unaddressed) stands.
- **No change to the YM frontier or the control-step obstruction.** This
  cycle verified + corroborated the *frontier map*; the mass-gap /
  existence problem remains fully open.

## Honesty / scope

- **Agawa RETRACTED** — confirmed from the Cambridge Open Engage version
  history (addendum v1/v2 both "Retracted"); main v2 not marked retracted
  in the search but uncited/unaffiliated/AI-assisted. Both on a
  non-peer-reviewed preprint platform. Honest: Agawa is a non-result.
- **Eriksson** findings are from **ai.viXra.org ("AI assisted e-prints")**
  — not peer-reviewed, AI-assisted. Their value here is **corroborative,
  not probative**: an attempted proof's self-concession that aligns with
  the wiki's independently-derived obstruction. **Not evidence the
  obstruction is correct** (a flawed attempt failing does not prove the
  problem is hard); only a weak convergent signal. Flagged honestly.
- **No proof of YM existence + mass gap.** The Clay problem is
  untouched. The realistic goal (as for the other five) is a precise,
  sourced, compounding frontier — advanced this cycle by closing Agawa
  and corroborating the control step via Eriksson's self-assessment.
- Outcome: **confirmed** (Agawa retraction confirmed; Eriksson
  control-step self-concession corroborates the 6-for-6 obstruction;
  substantive-acceptance flag reinforced), **partial** overall (no
  proof move; both items AI-assisted preprints, corroborative only).

## Next (attempt-07)

The user directive is to keep the loop running until weekly > 75% then
pause (weekly was 69.8% at this cycle's start). Natural YM next moves:
(a) **deepen direction (A)** — the uniform-in-$a$ IR bound / strong↔weak
crossover / UV→IR bridge (the single load-bearing control step, now
corroborated by Eriksson's $O(1/k)$ non-summability) — survey recent
rigorous progress, OR (b) status-check the **Chatterjee 2025 follow-up**
(arXiv:2505.16585, flagged lightly to-verify), OR (c) read the
Faizal-Shabir Part 3/4 bodies once the 2027-02 embargo lifts. The
rotation continues per the rotation order.