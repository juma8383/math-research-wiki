---
type: attempt
problem: navier_stokes
attempt: 1
date: 2026-08-24
approach: First attack — state NS, locate the exact frontier (local/weak/conditional known vs global regularity open), name the open content, map the obstruction to the critical-norm control step via supercriticality
outcome: partial
tags: [frontier, obstruction-map, supercriticality, conditional-regularity, cross-problem]
---

# Attempt 01 — Establish the frontier and obstruction for Navier-Stokes

First cycle on NS. Mirrors Beal/BSD attempts 01: get the clean form, locate the
exact frontier, name the open content, map where the obstruction sits.

## Statement established [[def-navier-stokes-equation]]

Fefferman's four Millennium statements [ns-millennium-fefferman]: (A) global
smooth on $\mathbb R^3$; (B) global smooth on $\mathbb T^3$; (C) breakdown on
$\mathbb R^3$; (D) breakdown on $\mathbb T^3$. Domains without boundary;
solutions smooth + bounded energy. A/C (or B/D) are complementary — global
regularity OR finite-time blowup closes the problem.

## The exact frontier

| piece | 2D | 3D |
|---|---|---|
| local smooth existence | known | known [[thm-local-wellposedness]] |
| small-data global | known | known |
| global weak (Leray-Hopf) | known (unique) | known, **non-unique?** [[thm-leray-weak-solutions]] |
| global smooth for large data | known [ns-2d-solved] | **OPEN** |
| finite-time blowup counterexample | n/a | **OPEN** |

Plus conditional regularity (Serrin/BKM [[thm-serrin-regularity]]
[[thm-beale-kato-majda]]) and partial regularity (CKN
[[thm-caffarelli-kohn-nirenberg]]) hold in 3D but are conditional.

## Open content (analog of Beal's "finitely many → zero", BSD's "rank ≤1 → arbitrary rank")

- Regularity side: **"small/local data → arbitrary large-data global regularity."**
- Counterexample side: **"averaged-NS blowup → true-NS blowup."**

## The obstruction: control step, not resolution step

The *resolution* layer works and finished the verified cases: local existence,
small-data global, conditional regularity (BKM $\int\|\omega\|_\infty
\Leftrightarrow$ regular; Serrin $L^r_tL^s_x$, $2/r+3/s\le1 \Rightarrow$
smooth; endpoint $L^\infty L^3$ by ESS), partial regularity (CKN singular set
dim $\le1$). All say "IF a critical norm is bounded THEN smooth."

The gap is the **global a priori bound on a critical norm** — a *control*
step, exactly parallel to BSD's Selmer-group control and Beal's reduction step.
The only unconditional global bound is the **energy** ($\|u\|_{L^2}$), which is
**subcritical** in 3D [[method-energy-supercriticality]] [ns-supercritical].
Under NS scaling $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$:
$\|u_\lambda\|_{L^2}=\lambda^{-1/2}\|u\|_{L^2}$ (weakens at small scales), but
$\|u_\lambda\|_{L^3}=\|u\|_{L^3}$ (critical, scale-invariant). So the energy
cannot control the critical norm.

The structural reason: the nonlinear advection $(u\cdot\nabla)u$ has Serrin
number $S=d+1$; the linear terms have $S=d/2+2$. In 3D: $4>3.5$ (nonlinearity
dominates, supercritical). In 2D: $3=3$ (balanced — solved). This is the
cleanest single fact explaining the 2D/3D divide, parallel to Beal's
"cubic-cubic-cubic is the unique coincidence" and BSD's "one-point-shaped
Euler system."

## Tao's quantitative frontier [ns-tao-quant-l3]

If smoothness is first lost at $T^*$:
$\limsup_{t\uparrow T^*}\|u\|_{L^3}\cdot(\log\log\log(1/(T^*-t)))^c=\infty$.
The critical norm must blow up faster than a triple log — this QUANTIFIES the
missing control step's difficulty. Barker (2022) localized it; Palasek
sharpened it for axisymmetric data. The residual difficulty is the
supercritical gap (subcritical energy ↔ critical $L^3$).

> **[CORRECTION 2026-08-24, attempt-02]** The phrase *"Palasek sharpened it
> for axisymmetric data"* is a **mislabel**, verified against the primary
> source. Palasek (2022, J. Math. Fluid Mech., arXiv:2111.08991) extended
> Tao's rate to **dimensions $d\ge4$** (a **quadruple** logarithm, one more
> than 3D) — **not** axisymmetric. The axisymmetric blowup program is real but
> lives in Hou (2024, arXiv:2405.10916) and Seregin (2024, arXiv:2402.13229),
> different authors. Original text left intact (append-only); see
> `attempt-02.md` for the primary-source verification. (Same discipline as
> Beal's (2,3,7) spherical→hyperbolic correction.)

## Cross-problem compounding [[beals_conjecture]] [[birch_swinnerton_dyer]]

The "obstruction at the control/reduction step, not the resolution step" lens
is now 3-for-3:
- **Beal** — reduction-to-finite-curves step (resolution tools work; no
  reduction mechanism without even/spherical structure).
- **BSD** — Selmer-group-control step (resolution tools work; no Euler system
  of rank-$\ge2$ shape).
- **NS** — critical-norm-control step (resolution/conditional tools work; no
  unconditional global critical bound; supercriticality).

This is a genuine reusable research strategy. Recorded in `notes.md` as a
candidate methodology page. `related` links added across all three problems.

## Forward directions

- **(A) A critical a priori bound**: a new global monotone/conserved quantity
  at critical regularity, or a new mechanism controlling $L^3$/$\dot H^{1/2}$
  globally — directly the missing control step.
- **(B) Blowup (Fefferman C/D)**: a finite-time singularity for true 3D NS;
  Tao's averaged-NS blowup [ns-tao-averaged-blowup] is the model, the gap is
  removing the averaging while keeping blowup.
- **(C) Quantitative critical program**: sharpen conditional criteria (Luo
  optimal frequency localization [[thm-beale-kato-majda]], Barker localized
  rates) and quantify the supercritical gap, narrowing what (A)/(B) must do.

## Theory toolbox filed this cycle

`def-navier-stokes-equation`, `thm-local-wellposedness`, `thm-leray-weak-solutions`,
`thm-serrin-regularity`, `thm-beale-kato-majda`, `thm-caffarelli-kohn-nirenberg`,
`thm-tao-averaged-blowup`, `method-energy-supercriticality`; source `ns-survey`
(search-compiled, flagged [summary] / to-verify).

## Honesty / to-verify

Status facts ingested from web-search summaries, **not primary sources**;
flagged in `ns-survey` and `progress.md`: Fefferman's four-statement
formulation, the Serrin/ESS endpoint, Tao's triple-log rate and Barker
localization, the Buckmaster-Vicol non-uniqueness scope. Beal's attempt-17
caught a silent error this way, so verification is not a formality.

## Next

Verify the load-bearing facts against primary sources (Fefferman's Clay
write-up; ESS 2003; Tao 2016; Barker 2022), then deepen direction (B): what
concretely blocks removing the averaging in Tao's blowup model, and is there a
geometric (axisymmetric) ansatz where the gap narrows?