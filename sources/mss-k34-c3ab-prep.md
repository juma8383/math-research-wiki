---
type: source
id: mss-k34-c3ab-prep
title: "MSS K34 C3_A/B gate-prep round series (Windows box, 2026-09-09)"
author: "Claude session (hermes-win Windows box, SageMath 10.9/WSL2)"
date: 2026-09-09
provenance: "private notes — session work-package tag; primary artifacts are the scripts and logs under problems/magic-square-of-squares/scripts/ cited below"
tags: [mss-k34-c3ab-prep]
---

# MSS K34 C3_A/B gate-prep round series (2026-09-09, Windows box)

**[mss-k34-c3ab-prep]** — the work-package tag covering the Windows-box
round series recorded in [[magic_square_of_squares]] notes.md §2aa–§2bb
plus their addenda (2026-09-09, SageMath 10.9 under WSL2): the preparation
for the two Coleman targets (C3_A main gate; B-side mirror) run in parallel
with the Linux box's E₊(ℚ(√−271)) descent. This page exists to define the
tag per the claim-tag join convention (SCHEMA.md `sources/<id>.md`); it is a
session bookkeeping tag, not an external-source claim — every mathematical
claim made under it is anchored in the round text and its script/log
artifacts, with independent verification paths noted there.

## What the round series covers (§2aa–§2bb + addenda)

- **§2aa–§2ae groundwork**: B-side sieve-hunt continuation to 2·10⁶
  (`[to-verify]` discharged: 40 valid primes, zero kills), Coleman-prep,
  quartic layer, B-side mirror round, residue groundwork.
- **§2ak–§2au residue layer + assembly**: infinity classes verified, Z_D
  and Z_DB residue filters (p = 13, 19, 23; sweeps to p ≤ 500), log-datum
  layer, height-final assembly (C = 46.59 conservative, cross-checked),
  enumeration probes.
- **§2av–§2bb census bands + descent sieve**: C3_A/C3_B probes and bands
  to 10⁸ (zero points; direct-search wall at 10⁸), Z_D bands to 10⁸
  ((0, ±238) degenerate orbit alone), and the two-stage modular-filter
  descent sieve over both 2-cover classes d ∈ {1, 238} to |x| ≤ 10¹⁰
  — d = 1: degenerate orbit only; d = 238: EMPTY throughout
  (`mss_k34_descent_sieve_win{2..6}.sage` + logs; v2 died on CRT
  construction, v3 timeout-cut, v4/v5 chunked, v6 iterated survivor
  classes, 662 s total).

## Artifacts

`problems/magic-square-of-squares/scripts/mss_c3ab_sage_gateprep{,2,3}.sage`
+ `.log`, `mss_k34_zd_height_sharp{2,3,4}.sage` + `.log`,
`mss_k34_descent_sieve_win{2..6}.sage` + `.log`. Two later in-flight
artifacts of the same series (`mss_k34_descent_sieve_win6b.*`,
`mss_k34_descent_sieve_win7.*`) were left uncommitted when the session's
machine crashed mid-sweep (win7 log truncated at "stage-1 survivors:
5103", C3_A octic sieve) and are NOT yet filed as results.