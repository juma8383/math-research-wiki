---
type: source
id: explicit-pnt-bounds-plan-2026-09-10
title: "Contribution plan: explicit bounds for Chebyshev functions (external LLM plan, 2026-09-10)"
author: "External LLM-generated contribution plan (user-submitted 2026-09-10; authoring tool unidentified)"
date: 2026-09-10
provenance: "private notes — user-submitted plan text; NOT a mathematical source; every factual claim in it was assessed against primary literature before wiki use"
tags: [pnt-bounds-plan, dvp-effective-unverified]
---

# Explicit-PNT-bounds contribution plan (2026-09-10) — ingestion assessment

**[pnt-bounds-plan]** — an external LLM-drafted plan proposing to
"modernize" the wiki's (nonexistent) analytic-number-theory module with
the 2018–2023 explicit Chebyshev-bounds literature and a Lean 4
formalization architecture. Ingested per the gemini-plan precedent
([[gemini-contribution-plan-2026-09-09]]): adapted in-place, fact-checked
claim by claim. The plan's **repository description is hallucinated**;
its **literature pointers are mostly real**; the salvageable core is
filed as [[explicit-chebyshev-bounds]] + the two paper sources
([[fiori-kadiri-swidinsky-2023]], [[broadbent-kadiri-2021]]).

## Verdict table (plan claim → status)

| Plan claim | Verdict |
|---|---|
| Repo has issue tracker / PR workflow / fork+branch phases | **FALSE** — 0 issues, 0 PRs, single-maintainer direct-to-main, deterministic lint gate |
| `docs/analytic-number-theory/`, `src/lean/`, Mathlib integration | **FALSE** — no Lean anywhere; 2026-09-09 overhaul verified no Lean and REJECTED Lean phases (standing decision) |
| FKS 2023: 9.22 (log x)^{3/2} exp(−0.8476836 √log x) for x > 2 | **REAL** — arXiv:2204.02588; constants verified (abstract v3 renders 9.22106, corollary text 9.22022) |
| Plan's derivation "C = √(2/R₀)" | **WRONG** — correct relation C = 2/√R (0.8476836 = 2/√5.5666305; √(2/R) = 0.5996) |
| Broadbent et al. 2021 log-bounds k ∈ {1..5} | **REAL** (k ≤ 5; abstract also carries the εx shape) |
| Patel sub-Weyl 307.098·t^{27/164}, t ≥ 3 | **REAL** (Patel 2021 thesis; exponent-pair ABA³B(0,1) = (11/82, 57/82)) — but Patel–Yang 2023 (arXiv:2302.13444) already improved the constant to 66.7; plan missed this |
| H₀ = 3·10¹² (Platt–Trudgian) | **REAL** — already filed in [[riemann_hypothesis]] |
| "Effective dVP" bounds \|θ−x\| < x·exp(−1/(4√ln x)) x ≥ 2, C = 1/3 x ≥ 3 | **UNVERIFIED, suspect** — as written the exponent → 0, degenerating to the trivial \|θ−x\| < x; likely garbled from the PNT+ Lean blueprint (Kontorovich et al.), which has formalized FKS Cor. 1.4. **[dvp-effective-unverified]** — do not load without full-text check |
| Ramanujan inequality holds for x ≥ exp(3361), down from exp(3915) | **REAL but superseded** — exp(3915) = Platt–Trudgian, exp(3361) = Johnston–Yang 2022; current record Axler 2022 (Math. Ineq. Appl. 25) exp(3158.442) `[to-verify]` |
| Kadiri–Lumley–Ng 2018 zero-density N(σ,T) bound | plausible, NOT verified here `[to-verify]` |
| van der Corput 0.618·t^{1/6} explicit Weyl bound | NOT verified here `[to-verify]` |

## Disposition

Lean stub phase (ChebyshevBounds.lean with `sorry`) rejected: repo has no
Lean toolchain and the standing 2026-09-09 ruling adapts external plans
in-place instead. Fork/branch/PR phase rejected: single-maintainer repo.
Mathematical core accepted with corrected constants. Useful external
pointer discovered during verification: the TME-EMT explicit-bounds wiki
(CNRS archimede) maintains this exact literature; and the PNT+ Lean
blueprint already formalizes FKS Corollary 1.4 — the plan's Phase-3 goal
exists as community work to cite, not to rebuild.