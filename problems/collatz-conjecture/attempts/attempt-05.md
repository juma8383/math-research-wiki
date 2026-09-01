---
type: attempt
problem: collatz_conjecture
attempt: 5
date: 2026-08-24
approach: Verify the Barina 2020 2^68 computational-verification bound (the evidence-base line in the exact-frontier table) + status-check the record's 2024-26 progress
outcome: confirmed
tags: [verification, primary-source, computational-evidence, barina, oliveira-e-silva, cross-problem, correction]
---

# Attempt 05 — Barina 2020 (2^68) verified; record has ADVANCED to 2^71 (Jan 2025)

Cycle-21 Continue on Collatz (cross-problem loop, second pass; yellow zone
65.5% session / 63.9% weekly, 0 subagents — session crossed 60% too; resets
in ~2h). Attempt-04's `Next` named the **Barina 2020 $2^{68}$
verification bound** (the computational-evidence base, the "evidence"
line in the exact-frontier table) as the next-most-load-bearing to-verify
item. This cycle verifies it against primary sources — and finds the
record has since **advanced**, so the wiki's evidence line is **outdated**
and gets an append-only update. Same discipline as the Hodge attempt-05
"open even for $H^2$" correction and the BSD Kim citation-upgrade.

## Verification: Barina 2020 — CONFIRMED (J. Supercomput. 2021)

**David Barina** (Brno Univ. of Technology), *Convergence verification of
the Collatz problem*, **The Journal of Supercomputing 77** (2021),
2681–2688, DOI
[10.1007/s11227-020-03368-x](https://doi.org/10.1007/s11227-020-03368-x).

- Verified convergence for all starting values up to **$2^{68}$**
  ($\approx 2.95\times10^{20}$) by **2020-05-07**, via a distributed
  computing project (Sep 2019 – May 2020).
- **Novel algorithmic contribution** (the load-bearing technical point):
  replaced the huge precomputed $O(2^N)$ lookup tables of prior work with
  **small $O(N)$ tables** by tracking the trajectory on $n+1$ instead of
  $n$, using only multiplicative operations (count-trailing-zeros, right
  shift, a small powers-of-three table). Natively **128-bit** (competitors
  used 64-bit). Throughput: $\sim4.2\times10^9$ 128-bit numbers/sec on
  Intel Xeon Gold 5218 (CPU), $\sim2.2\times10^{11}$/sec on NVIDIA RTX 2080
  (GPU).
- Found the largest known **path record** below $2^{68}$: starting value
  $n=274{,}133{,}054{,}632{,}352{,}106{,}267$, confirming the
  **Lagarias-Weiss prediction** that path-record peak heights grow like
  $n^2$.

The "evidence: Barina 2020, $2^{68}$" line in `progress.md`'s exact-
frontier table is **CONFIRMED** as a peer-reviewed fact. `[collatz-barina]`
upgraded from `to-verify` to verified.

## Precision correction: Oliveira e Silva — the bound is 20·2^58, not "2^58"

The earlier record (the prior line in the evidence progression) is
**Tomás Oliveira e Silva** (Univ. of Aveiro), 2004–2009 effort, reaching
**$20\cdot2^{58}\approx5.76\times10^{18}\approx2^{62.3}$** — **not** bare
$2^{58}$ (a factor of 20 larger). Published as *Empirical Verification of
the $3x+1$ and Related Conjectures*, in Lagarias (ed.), *The Ultimate
Challenge: The $3x+1$ Problem* (AMS, 2010), pp. 189–207. The "20·"
coefficient matters: $20\cdot2^{58}\approx2^{62.3}$, so Barina's $2^{68}$
is ~$2^{5.7}$ beyond it, not ~$2^{10}$. *(Minor precision correction;
append-only — attempt-04's "$2^{58}$" shorthand is the rounded form.)*

## The update: the record has ADVANCED to 2^71 (Jan 2025)

The search surfaced that **Barina's distributed project has continued
past the 2020 $2^{68}$ paper**, per his project website (updated 2026-08):

| Milestone | Date | Bound |
|---|---|---|
| Published (J. Supercomput. 2021) | 2020-05-07 | $2^{68}$ |
| — | 2021-12 | $2^{69}$ |
| — | 2023-07 | $2^{70}$ |
| — | 2023-11 | $1.5\times2^{70}$ |
| **Current frontier** | **2025-01** | **$2^{71}\approx2.36\times10^{21}$** |

So the wiki's evidence line ("Barina 2020, $2^{68}$") is **outdated by
three doublings** — the current verified bound is **$2^{71}$ (Jan 2025)**,
with work toward $2^{72}$. **No counterexample found** at any bound.

### Honesty caveat on the 2^71 figure

The $2^{71}$ bound is from **Barina's project website** (self-reported,
last updated 2026-08) — **not a peer-reviewed publication**. The published,
peer-reviewed figure remains the $2^{68}$ of the J. Supercomput. 2021
paper. So the update is recorded as: *peer-reviewed* evidence =
$2^{68}$ (2021); *project-reported* frontier = $2^{71}$ (Jan 2025,
self-reported, `to-verify` against a publication). Same distinction as
the YM Faizal-Shabir publication-status vs substantive-acceptance split
(attempt-05) and the NS Hou-published / Seregin-preprint asymmetry
(attempt-05).

## What this changes (and does NOT change) in the obstruction map

- `[collatz-barina]` **CONFIRMED** (J. Supercomput. 77, 2021, DOI
  10.1007/s11227-020-03368-x); the evidence line in `progress.md`'s
  exact-frontier table is **UPDATED** from $2^{68}$ (2020) to the current
  $2^{71}$ (Jan 2025, project-reported) — an honest, append-only refresh
  of the evidence base, not a proof move.
- **Oliveira e Silva precision**: $20\cdot2^{58}\approx2^{62.3}$ (AMS
  2010), not bare $2^{58}$.
- **No change to the frontier or the control-step obstruction.** The
  density→pointwise control step (attempt-04's $\Pi^0_2$-completeness
  logical wall) is **untouched** by any finite verification, however
  large. **Computational verification is RESOLUTION-side evidence**
  (it confirms individual instances), and the control step (a uniform
  argument from "almost all" to "all") is exactly what finite checking
  cannot supply: $2^{71}$ instances is **measure zero** against $\mathbb
  N$, and the $\Pi^0_2$-completeness of the generalized problem means
  **no finite/uniform algorithm resolves it**. So the computational
  record, however it grows, is precisely the "resolution accumulates
  but control doesn't follow" shape — reinforcing, not moving, the
  attempt-04 control wall.
- **Control-step echo (cross-problem):** this is the cleanest instance
  of the "one-dimensional engine stops" sub-pattern: the verification
  engine (finite computation) **controls** the "checked instances"
  slice (resolution) and **stops** at the "all $n$" slice (control) —
  parallel to NS Seregin (self-similar slice / non-self-similar), YM
  Chatterjee (confinement slice / mass-gap slice), BSD
  cyclotomic-vs-anticyclotomic (each single-point engine / rank-$\ge2$
  comparison). The Collatz instance is the starkest because the
  $\Pi^0_2$-completeness makes the stop a **logical** one (no uniform
  algorithm *can* exist for the generalized problem), not merely a
  technical gap.

## Honesty / scope

- **Barina 2020/2021 CONFIRMED** against the primary source
  (J. Supercomput. 77, 2021, DOI 10.1007/s11227-020-03368-x; $2^{68}$
  by 2020-05-07; novel $O(N)$-table 128-bit GPU algorithm; path record
  $n=274{,}133{,}054{,}632{,}352{,}106{,}267$; Lagarias-Weiss $n^2$
  confirmation).
- **The $2^{71}$ (Jan 2025) figure is project-website-reported, NOT
  peer-reviewed** — flagged `to-verify` against a publication. The
  peer-reviewed figure stays at $2^{68}$. Honest publication-status split
  recorded (as in YM/NS).
- **Oliveira e Silva precision correction** ($20\cdot2^{58}$, AMS 2010)
  — append-only.
- No counterexample found at any bound — consistent with, but not a
  proof of, the conjecture. The density→pointwise control step and the
  cycle-exclusion wall remain open; $\Pi^0_2$-completeness of the
  generalized problem (attempt-04) means no uniform argument exists
  there.
- The 2024-25 *claimed-proof* preprints (Fathi 2025 / Chang 2026 /
  Nwankpa 2025) were **not** status-checked this cycle (budget; one
  search spent on the verification record, which was the more
  load-bearing of attempt-04's two remaining targets). Deferred to a
  later cycle.
- Outcome: **confirmed** (Barina 2020 paper verified; record advanced
  $2^{68}\to2^{71}$ recorded with the peer-reviewed/project-reported
  split; Oliveira e Silva precision; control-step/undecidability echo
  reinforced), **partial** overall (frontier unchanged).

## Next (attempt-06)

Natural next moves: (a) **status-check the 2024-25 claimed-proof
preprints** (Fathi 2025 / Chang 2026 / Nwankpa 2025) — the one remaining
attempt-04 target deferred this cycle, OR (b) primary-source-verify
the **$2^{71}$ bound against a publication** (if Barina publishes the
extended result), OR (c) deepen a direction (A/B/C) sub-thread. The
rotation continues: next cross-problem cycle → beals-conjecture
(occasional cycle-in — the rotation has now visited BSD, NS, YM,
Hodge, Collatz in the second pass; beals is the occasional cycle-in
per the bias rule), OR birch-swinnerton-dyer (attempt-06) per the
rotation order.