---
title: Missed angles (critic) & the MCSP gap
category: synthesis
tags: [mcsp-gap, missed-angles, mcsp-def, meta-complexity-thesis, cikk-2016, hirahara-2018, hirahara-ilango-2025, mcsp-deconditioning, gikkt-2019, ad-2014, barrier-evasion-overstated, route-a-route-b, os-2018, locality-barrier]
status: open
last_touched: 2026-08-21
---

# Missed Angles — the Critic's Catch

The completeness critic found 8 angles the 8-agent fan-out did **not** cover. The biggest is the run's most consequential gap — now covered by its own first-class angle page.

## The biggest hole: meta-complexity / MCSP `[mcsp-gap]` — NOW COVERED
The **Minimum Circuit Size Problem** `[mcsp-def]` and the meta-complexity program is the **single most active current direction** bearing on circuit lower bounds, and was entirely absent from the 8-angle fan-out. Thesis `[meta-complexity-thesis]`: *understanding the complexity of computing complexity is the key to lower bounds.* It is the one current program where near-, medium-, and long-term targets are **all circuit lower bounds** (not proof-system or geometric proxies) and where conditional results are being progressively de-conditioned `[mcsp-deconditioning]` — Hirahara FOCS 2018 `[hirahara-2018]`, Hirahara-Ilango FOCS 2025 `[hirahara-ilango-2025]` conditional NP-hardness, Carmosino-Impagliazzo-Kabanets-Kolokolova `[cikk-2016]` learning-from-natural-proofs. **This is the highest-upside long-term target and the clear next wave.**

**Status update (2026-08-21):** no longer "missed." This gap now has its own first-class angle page — see [[mcsp-meta-complexity]]. The entry is retained here as the historical record of the critic's catch; the substantive content lives on the angle page. Its omission from the original fan-out biased the map toward known-territory cartography; that bias is now corrected.

**Deep-dive update (2026-08-21):** the MCSP angle was pushed deeper (sources/2026-08-21-mcsp-deep-dive.md). Net outcome: (1) attributions verified + corrected — the AC⁰[p] bound is `[gikkt-2019]` (not "Akhmedov-Carlson-Cook"), SZK-hardness is `[ad-2014]`; (2) the primer's "MCSP is orthogonal to the barriers" claim was **downgraded** to *candidate route, not barrier-immune* `[barrier-evasion-overstated]`; (3) the only two formal MCSP→P≠NP bridges `[route-a-route-b]` were identified, both currently blocked; (4) the honest gap made explicit — near-term de-conditioning yields EXP≠ZPP-class, **not P≠NP**. Still the highest-upside direction, now with a sharper, weaker, falsifiable framing.

## Other missed angles `[missed-angles]`
- **Derandomization / hardness-vs-randomness as a primary axis** — the NW/IW paradigm (circuit LBs ⟺ derandomization) was treated only as a dual of the independence angle, never as a primary attack. `[tell-2018]` is the closest bridge and was used only as a barrier.
- **Hardness magnification** (Allender-Koucký; `[os-2018]`) — the one framework where a *weak* (logarithmic) LB provably implies a *strong* (super-poly) one, unlike every angle above where progress is incremental. Hits the **locality barrier** `[locality-barrier]` (Chen-Lyu-Potyagailo-Santhanam, attribution unverified) — now a defined tag and **route B** of the MCSP→P≠NP bridge (`[route-a-route-b]`); the technique-vs-inherent status of this barrier is an open falsifiable target (see [[mcsp-meta-complexity]] § Concrete next steps).
- **Fine-grained complexity (ETH/SETH)** — the reduction web (3SUM, OV, APSP, Max-IP) as a structural constraint on P vs NP from below.
- **Learning theory / crypto as a positive direction** — hardness-of-learning ⟹ circuit LBs (Klivans-Sherstov; Daniely-Shalev-Shwartz), not merely a natural-proofs consequence.
- **Lutz resource-bounded measure** — the measure of P/NP/P/poly; generates unconditional partial results and conditional structural theorems.
- **Direct algebraic VP-vs-VNP outside GCT** — Newton iteration LBs, ABPs, shifted-derivative methods beyond ELSW, secant varieties.
- **Geometric group theory / isoperimetric** — Dehn-function / word-problem connections to circuit depth; non-commutative geometric approaches distinct from GCT (algebraic geometry) and Seiller (ergodic theory).

## See also
[[mcsp-meta-complexity]] · [[novel-diagnoses]] · [[semantic-invariant-gap]] · [[status-map]] · [[open-problems]]