---
type: source
id: mss-k4-c4quotients
title: "MSS k=4 multiplier line: Copilot contribution integrated + quotient rank audit (2026-09-11)"
author: "Copilot chat session (user-mediated), integrated and independently verified by Claude session 2026-09-11"
date: 2026-09-11
provenance: "private notes — chat-transcript work package; primary artifacts are the materialized attempt files and scripts under problems/magic-square-of-squares/magic-square-chat-Copilot-Contribution/ (215-page chat PDF is the only record of the lineage's earlier rounds) and the promoted/verification scripts under problems/magic-square-of-squares/scripts/k4_*"
tags: [mss-k4-c4quotients]
---

# MSS k=4 multiplier line: Copilot contribution + rank audit (2026-09-11)

**[mss-k4-c4quotients]** — the work-package tag for the k=4 multiplier
round of the [[magic_square_of_squares]] offsets program: the external
Copilot chat contribution (C₄ genus-3 lift of the k=4 first-cover quartic,
Klein-four quotient structure, mod-7 support theorem, 7-adic disk
fullness, corrected Jacobian families, naive squareclass sieve) integrated
into notes.md §2bd after independent verification, plus the same session's
PARI/GP + mwrank rank audit that closes the contribution's two named
open frontiers (rank J_u; sign-quotient model + full decomposition).
This page exists to define the tag per the claim-tag join convention
(SCHEMA.md `sources/<id>.md`); it is session bookkeeping, not an
external-source claim — every mathematical claim made under it is anchored
in the round text and its script artifacts, with the verification path
recorded there.

## Coverage

- **Received contribution** (materialized files, 2026-09-11): C₄ lift
  Z² = x⁸ − 252x⁶ + 518x⁴ − 252x² + 1 of the k=4 quartic
  W² = u⁴ − 248u² + 16 (t = x + 1/x, u = x − 1/x, Z = Wx²); norm
  factorization over ℚ(√15); mod-7 support theorem 7 ∣ pq(p−q)(p+q);
  7-adic disk fullness (Hensel lifts through 7⁶); Jacobian models J_u
  and J_t; Lutz–Nagell infinite-order point P = (4, 504) on J_t;
  corrected general families J_{u,k}, J_{t,k}; naive squareclass sieve
  (no obstruction at 12 moduli).
- **This session's audit** (promoted scripts): exact-arithmetic
  verification `k4_quotient_verify.py`; PARI/GP rank audit
  `k4_pari_rank_audit{,2}.gp` (ellfromeqn model for the sign quotient;
  ellrank + elltors + point checks); Frobenius charpoly product identity
  `k4_charpoly_check.gp`; mwrank certification of all five quotient
  curves. Headline: **rank J_u = 0 unconditional** (J_u(ℚ) = (ℤ/2)²,
  degenerate locus only); **E_s rank 1** (generator (−258, 1024));
  **rank J(C₄)(ℚ) ≤ 2 < 3 = genus** — the Chabauty regime entered for
  the k=4 line for the first time.