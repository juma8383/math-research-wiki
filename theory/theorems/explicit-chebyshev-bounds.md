---
type: theorem
name: Explicit bounds for the Chebyshev functions (2018-2023 sharpenings)
created: 2026-09-10
tags: [explicit-pnt-bounds, analytic-number-theory, toolbox-reference]
used-in: [[riemann_hypothesis]]
provenance: [[fiori-kadiri-swidinsky-2023]], [[broadbent-kadiri-2021]]
---

# Explicit bounds for the Chebyshev functions θ(x), ψ(x)

State of the art for the explicit-error-term program (2018–2023
sharpenings), filed from the user-submitted plan
[[explicit-pnt-bounds-plan-2026-09-10]] with corrected constants.
Every bracketed tag anchors to an abstract-verified source; anything
resting on search summaries alone carries `[to-verify]`.

## Definitions

$\theta(x) = \sum_{p\le x} \log p$ and
$\psi(x) = \sum_{p^k \le x} \log p$; PNT ⟺ ψ(x) ∼ x ⟺ θ(x) ∼ x.
The three useful bound shapes: **exponential**
|x-error| ≤ A x (log x)^B exp(−C√log x); **logarithmic**
x(1 − m_k/log^k x) ≤ θ(x) ≤ x(1 + M_k/log^k x); **constant**
|x-error| ≤ ε x beyond a threshold.

## The bounds (current best, all verified at abstract level)

- **All-x exponential (ψ).** For all x > 2,
  |ψ(x) − x| < 9.22·x·(log x)^{3/2}·exp(−0.8476836√log x)
  [fks2023-allx-bounds]. Journal vs. preprint constant reconciliation
  pending (9.22106 / 9.22022).
- **Large-x constant (ψ).** For log x ≥ 3000,
  |ψ(x) − x| < 4.47·10⁻¹⁵·x [fks2023-large-threshold]
  (Platt–Trudgian 2021: 4.51·10⁻¹³).
- **Logarithmic (θ).** For k = 1…5, the m_k/M_k tables of
  [bklw2021-log-bounds]; plus the εx shape over explicit ranges
  [bklw2021-eps-bounds]. θ-bounds are obtained from ψ-bounds via
  ψ − θ = O(√x)-type explicit difference bounds (refining
  Rosser–Schoenfeld).

## The dependency chain (why constants move)

1. **RH verification height** H₀ = 3·10¹² (Platt–Trudgian; standing
   record, [[riemann_hypothesis]]) — zeros below H₀ are treated
   exactly (on-line sums), above it theoretically.
2. **Zero-free region** — no zeros for β ≥ 1 − 1/(R log|γ|) with
   R = 5.5666305 (Mossinghoff–Trudgian-region lineage;
   Broadbent-et-al. text uses R = 5.573412 — reconcile).
3. **Exponential constant from R: C = 2/√R**, NOT C = √(2/R) as the
   ingested plan asserted: 2/√5.5666305 = 0.8476836 ✓.
4. **Zero-density estimates** N(σ,T) control the Perron truncation tail
   (Kadiri–Lumley–Ng 2018 form, `[to-verify]`).
5. **Sub-Weyl input**: |ζ(1/2+it)| ≤ 307.098·t^{27/164} for t ≥ 3
   (Patel; exponent pair ABA³B(0,1) = (11/82, 57/82)); Patel–Yang 2023
   improve the constant to 66.7 `[to-verify]`. Sharper ζ-bounds →
   sharper zero-density → sharper Chebyshev bounds.

## Application anchor (Ramanujan's inequality)

π²(x) < (ex/log x)·π(x/e) for x ≥ exp(3915) (Platt–Trudgian) →
exp(3361) (Johnston–Yang 2022) → **exp(3158.442)** (Axler 2022,
using the FKS θ/ψ estimates) `[to-verify]` on each threshold.

## Formalization status (external pointer only)

No Lean content lives in this repo (standing 2026-09-09 decision:
adapt-in-place, no Lean phases). For community formalization status see
the PNT+ Lean blueprint (Kontorovich et al.), which already formalizes
the FKS all-x corollary — cite, do not rebuild.

## Cross-problem links

Feeds the evidence layer of [[riemann_hypothesis]] (zero-free region,
zero density, verified-height slicing all appear in its attempt-01
framing); independent toolbox reference for any future explicit-number
theory work. Not load-bearing in any active attack yet.