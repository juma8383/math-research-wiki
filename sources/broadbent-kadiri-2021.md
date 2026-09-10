---
type: source
id: broadbent-kadiri-2021
title: "Sharper bounds for the Chebyshev function θ(x)"
author: "Samuel Broadbent, Habiba Kadiri, Allysa Lumley, Nathan Ng, Kirsten Wilk"
date: 2021
provenance: "Math. Comp., doi:10.1090/mcom/3643 (published March 2021); arXiv:2002.11068v2 (27 Jan 2021); abstract-verified 2026-09-10 from the arXiv landing page, full-text verbatim re-check pending"
tags: [bklw2021-log-bounds, bklw2021-eps-bounds, explicit-pnt-bounds]
---

# Broadbent–Kadiri–Lumley–Ng–Wilk 2021 — explicit bounds for θ(x)

SUMMARY-VERIFIED 2026-09-10 from the arXiv:2002.11068 abstract page
(search-derived; full-text verbatim extraction pending). Toolbox
reference for [[explicit-chebyshev-bounds]].

## The bounds (abstract-anchored)

- **[bklw2021-log-bounds]** — explicit bounds for θ(x) in all ranges of
  x, of the shape
  $$x\Big(1 - \frac{m_k}{(\log x)^k}\Big) \le \theta(x) \le x\Big(1 + \frac{M_k}{(\log x)^k}\Big),$$
  for k = 1, …, 5 (search summaries report a k = 0 case too:
  θ(x) ≤ (1 + 1.93378·10⁻⁸)x for all x ≥ 0 `[to-verify]`), with
  extensive tables of m_k/M_k (ancillary file with Tables 8–15,
  41 pages).
- **[bklw2021-eps-bounds]** — the companion εx-shape bounds
  |θ(x) − x| ≤ ε x over explicit x-ranges (abstract: "of the shape
  εx and c_k x/(log x)^k, for k = 1, …, 5").

## Method notes

Combines ψ(x) − x bounds (Büthe's Logan-function smoothing for
x < e^2300; Platt–Trudgian's truncated Perron + explicit zero-density
above), explicit ψ − θ difference bounds of shape a₁√x + a₂x^{1/3}
(refining Rosser–Schoenfeld / Costa Pereira), the zeta zero-free region
with R = 5.573412 `[to-verify]` (search renders this as the value used
here; FKS 2023 use R = 5.5666305 — the two papers cite different
Mossinghoff–Trudgian-region constants; reconcile), and partial RH
verification to H ≈ 3·10¹² (Platt–Trudgian; standing record in
[[riemann_hypothesis]]). Search-level constants (5.9771·10⁻⁵ at
k = 2, X = e³⁵; k = 3 upper 0.024334 recovering/improving Axler's 0.15)
all `[to-verify]` pending full-text check.