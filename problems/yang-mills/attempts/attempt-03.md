---
type: attempt
problem: yang_mills
attempt: 3
date: 2026-08-24
approach: Verify the last load-bearing to-verify item [ym-supersymmetric] (Seiberg-Witten/Nekrasov scope = N=2 SUSY, not pure YM) against primary sources, and pin exactly why the SUSY mechanism does not transfer to the Clay problem
outcome: confirmed
tags: [verification, primary-source, seiberg-witten, nekrasov, supersymmetry, dual-superconductor, cross-problem]
---

# Attempt 03 — Verify [ym-supersymmetric]: SUSY illuminates the mechanism, does not solve Clay

Cycle-9 Continue on YM (cross-problem loop, second pass; yellow zone 66.7%
session / 48.5% weekly, 0 subagents). Attempt-02's `Next` offered two moves;
this cycle takes **(i)** — verify the last to-verify item `[ym-supersymmetric]`
against primary sources. Same discipline that caught the Eriksson
viXra/conditional sharpening (attempt-02) and Beal's (2,3,7) spherical
mislabel. The to-verify text in `progress.md` read: *"confirm
Seiberg-Witten/Nekrasov scope (N=2 SUSY, not pure YM)."*

## Verification: Seiberg-Witten — CONFIRMED (N=2 SUSY SU(2), dual-superconductor)

**Seiberg–Witten**, *Electric-magnetic duality, monopole condensation, and
confinement in N=2 supersymmetric Yang-Mills theory*, Nucl. Phys. B **426**
(1994), 19–52, arXiv:[hep-th/9407087](https://arxiv.org/abs/hep-th/9407087),
DOI [10.1016/0550-3213(94)90124-4](https://doi.org/10.1016/0550-3213(94)90124-4).
~3832 citations (INSPIRE). For $N{=}2$ SUSY YM with gauge group $SU(2)$:

- **Exact low-energy effective action** — the Kähler metric on the quantum
  moduli space of vacua (the $u$-plane, $u=\langle\mathrm{Tr}\,\phi^2\rangle$)
  and exact particle mass formulas, fixed by $N{=}2$ holomorphy.
- **Electric-magnetic duality** $SL(2,\mathbb Z)$ on $\tau=\theta/2\pi+
  4\pi i/g^2$; the strongly-coupled vacuum is a *weakly* coupled theory of
  monopoles. Solution via periods of the elliptic curve
  $y^2=(x-1)(x+1)(x-u)$ (monodromies $\Gamma(2)\subset SL(2,\mathbb Z)$).
- **Monopole condensation $\Rightarrow$ confinement** by **softly breaking**
  $N{=}2\to N{=}1$ (adding a superpotential $W=m\,\mathrm{Tr}\,\Phi^2$):
  monopoles condense, electric charge is confined via a **dual Meissner
  effect** — *the first relativistic field theory in which confinement is
  explained by monopole condensation.* A mass gap is generated (gauge field
  massive by the magnetic Higgs mechanism).

## Verification: Nekrasov — CONFIRMED (instanton localization, N=2 prepotential)

**Nekrasov**, *Seiberg-Witten prepotential from instanton counting*,
arXiv:[hep-th/0306211](https://arxiv.org/abs/hep-th/0306211) (ICM 2002).
Localization on framed-instanton moduli spaces on $\mathbb R^4$:
$$Z(a,\varepsilon_1,\varepsilon_2;q)=\sum_{k\ge0}q^k\int_{\mathcal M_k}1
=\exp\!\bigl(\mathcal F^{\rm inst}(a,\varepsilon_1,\varepsilon_2;q)/
\varepsilon_1\varepsilon_2\bigr),$$
with $\mathcal F^{\rm inst}(a,0,0;q)$ = the **Seiberg-Witten prepotential**;
equivariant localization (Duistermaat–Heckman / Atiyah–Bott) reduces the
integrals to sums over fixed points labeled by $N$-tuples of Young diagrams.

**Mathematical rigor: Nakajima–Yoshioka**, *Instanton counting on blowup. I.
4-dimensional pure gauge theory*, Inventiones Math. (2005),
arXiv:[math/0306198](https://arxiv.org/abs/math/0306198) — rigorous proof via
the **blowup equation** recursively determining the instanton corrections.
Extension to all classical gauge groups $SU/ SO/ Sp$ by
**Nekrasov–Shadchin** (arXiv:[hep-th/0404225](https://arxiv.org/abs/hep-th/0404225)).

## The scope point — CONFIRMED + made precise (the whole to-verify)

This is the load-bearing fact, now pinned to primary sources:

1. **All of the above is $N{=}2$ supersymmetric YM, not pure
   (non-supersymmetric) YM.** The Clay problem [ym-clay-jaffe-witten] is pure
   YM for a compact simple $G$ — *no supersymmetry*. `progress.md` already had
   this ("a solved RELATED problem, not the original"); the verification makes
   it primary-source-backed.

2. **Why it does not transfer — SUSY is essential, not decorative.** The
   exact solvability rests on $N{=}2$ supersymmetry supplying: (a) a BRST-like
   supercharge $Q$ enabling **equivariant localization** on instanton moduli
   spaces (Nekrasov); (b) the **holomorphic prepotential** $\mathcal F(a)$
   protected non-renormalization; (c) the finite-dimensional Coulomb-branch
   moduli space with controllable monodromy. **Pure YM has none of these** —
   no prepotential, no preserved fermionic symmetry to localize against, no
   controlled instanton gas. **There is no known bridge from the Nekrasov
   partition function (or the Seiberg-Witten solution) to the pure-YM mass
   gap.** So the SUSY machinery is an *illumination of the mechanism*, not a
   proof technique for Clay.

3. **Genuine nuance (sharpening):** the mass gap Seiberg-Witten exhibits is
   **not in pure $N{=}2$**. The $N{=}2$ theory has a **Coulomb-branch moduli
   space of vacua** — the photon and (at singularities) a *massless*
   monopole/hypermultiplet; generically **no mass gap**. The gap and
   confinement arise only after the **soft breaking $N{=}2\to N{=}1$**
   ($W=m\,\mathrm{Tr}\,\Phi^2$), which lifts the moduli space and condenses the
   monopoles. So the illuminated mechanism — **dual-superconductor
   confinement** ('t Hooft–Mandelstam) — is a property of the *softly broken
   $N{=}1$* theory, doubly removed from pure YM (SUSY, *and* broken).

## What this confirms for the obstruction map

- `progress.md` direction (B) entry ("Seiberg-Witten/Nekrasov for
  supersymmetric YM … Gives mass-gap-like results in RELATED theories, not the
  original") is **correct and now primary-source-verified**, with the
  mechanism named: **dual-Meissner-effect monopole condensation** = the
  hoped-for 't Hooft–Mandelstam dual-superconductivity picture for pure YM,
  here made *exact* by SUSY. So (B)'s content is: the *mechanism* one would
  want for pure YM (monopole condensation $\to$ confinement + gap) is
  demonstrated exactly in $N{=}2/ N{=}1$ SUSY, but the *control* that makes it
  exact (SUSY localization + holomorphy) is precisely what pure YM lacks. The
  obstruction is at the control step **again**: SUSY supplies the control
  (localization, holomorphy); pure YM does not. This is the YM instance of the
  6-for-6 control-step spine — the *resolution* (compute the spectrum /
  exhibit the condensate) works in SUSY because the *control* (SUSY-protected
  holomorphy + localization) is there; removing SUSY removes the control.
- Consistent with the Balaban UV-half picture (attempt-02): in SUSY the
  UV→IR bridge is *crossed exactly* (duality maps the strong-coupling singularity
  to a weakly-coupled monopole theory); in pure YM the same crossover is
  *uncontrolled* (the uniform-in-$a$ IR bound / strong↔weak bare-coupling
  bridge is the open blocker). The two attempts now triangulate the same
  obstruction from the lattice side (Balaban) and the continuum-SUSY side.

## Honesty / scope

- `[ym-supersymmetric]` **CONFIRMED + sharpened.** Seiberg-Witten (1994) and
  Nekrasov (2003, rigorous Nakajima–Yoshioka 2005) are for $N{=}2$ SUSY YM;
  the mass gap arises in the softly-broken $N{=}1$ theory via dual-Meissner
  monopole condensation; SUSY is essential (localization + holomorphy), with
  no known bridge to pure YM. Direction (B) mechanism named.
- No rigorous 4D quantum YM, no proven pure-YM mass gap. The verification is
  the cycle's point — the last `progress.md` to-verify item is now resolved.
- Outcome: **confirmed** (verification goal met, mechanism pinned + scope made
  precise + a Coulomb-vs-broken nuance), **partial** overall (frontier
  unchanged).

## Next (attempt-04)

With all `progress.md` to-verify items now resolved (Jaffe-Witten, Balaban,
supersymmetric; Eriksson remains a "sharpened preprint-status" item, not a
load-bearing fact to verify), the natural next move is to **push direction
(A) concretely**: survey the constructive-continuum-limit literature beyond
Balaban (Magnen–Rivasseau–Sénéor, AFS/Brydges–Kennedy finite-range
decompositions, cluster/polymer expansions) for the closest existing result
to a uniform-in-$a$ IR / mass-gap bound, and diagnose exactly where the
strong↔weak bare-coupling crossover loses control — the concrete control-step
question, the YM instance of the cross-problem obstruction. (Optionally also
body-verify the Eriksson abstract-vs-body $O(4)$ discrepancy, but that is a
preprint-quality issue, not a load-bearing fact.)