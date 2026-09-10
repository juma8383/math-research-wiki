---
type: source
id: fiori-kadiri-swidinsky-2023
title: "Sharper bounds for the Chebyshev function ψ(x)"
author: "Andrew Fiori, Habiba Kadiri, Joshua Swidinsky"
date: 2023
provenance: "J. Math. Anal. Appl. 527(2), Paper No. 127426 (2023); arXiv:2204.02588v3 (17 May 2023); abstract-verified 2026-09-10 from the arXiv landing page, full-text verbatim re-check pending"
tags: [fks2023-allx-bounds, fks2023-large-threshold, explicit-pnt-bounds]
---

# Fiori–Kadiri–Swidinsky 2023 — sharper explicit bounds for ψ(x)

SUMMARY-VERIFIED 2026-09-10 from the arXiv:2204.02588v3 abstract page
(search-derived; full-text verbatim extraction pending, per
[CLAUDE.md](../CLAUDE.md) verify-first rule). Used by
[[magic_square_of_squares]]-adjacent toolbox page
[[explicit-chebyshev-bounds]]. Note: revised version of "Density results
for the zeros of zeta applied to the error term in the prime number
theorem"; results on π(x) deferred to follow-up work.

## The bounds (abstract-anchored)

- **[fks2023-allx-bounds]** — for ALL x > 2:
  $$|\psi(x) - x| < 9.22106\, x\,(\log x)^{3/2}\exp(-0.8476836\sqrt{\log x}).$$
  Constant note: the v3 abstract states **9.22106**; the published-text
  Corollary 1.4 as rendered by the TME-EMT explicit-bounds wiki states
  **9.22022**. Reconcile against the journal PDF before load-bearing
  use — the exponential constant **0.8476836** agrees everywhere.
  The exponential constant is tied to the de la Vallée Poussin zero-free
  region with **R = 5.5666305** via **C = 2/√R** (Theorem 1.2, full-text;
  NOT C = √(2/R) as the ingested plan asserted — arithmetic check:
  2/√5.5666305 = 0.8476836 ✓, √(2/5.5666305) = 0.5996 ✗) `[to-verify]`
  on the exact Theorem 1.2 statement.
- **[fks2023-large-threshold]** — for log x ≥ 3000:
  $$|\psi(x) - x| < 4.47 \times 10^{-15}\, x,$$
  vs. Platt–Trudgian 2021's 4.51 × 10⁻¹³ x (abstract-anchored; a search
  summary also reports 4.9678 × 10⁻¹⁵ from the full text —
  `[to-verify]` reconcile).

## Method notes

"a significant refinement of ideas of Pintz", splitting the zeros into
additional regions + careful term estimation + computation. Method: modern
explicit formula (truncated Perron), the Riemann-zeta zero-free region,
partial RH verification (Platt–Trudgian height H₀ = 3·10¹², per
[[riemann_hypothesis]]), and explicit zero-density estimates. The paper
notes that if Hiary–Patel–Yang's subconvexity constant is confirmed, the
all-x constant improves to 8.99284 `[to-verify]`. Downstream use: Mertens
sums (Broadbent–Fiori–Kadiri–Ng–Wilk) and Axler's Ramanujan-inequality
threshold (see [[explicit-pnt-bounds-plan-2026-09-10]] assessment).