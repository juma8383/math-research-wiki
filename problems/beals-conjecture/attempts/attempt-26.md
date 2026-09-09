---
type: attempt
problem: beals-conjecture
attempt: 26
date: 2026-09-09
approach: wider-box (5,7,13) genuine-gap census (C<=120, B<=2e4, A unbounded) verifying attempt-24's to-verify min 1771 via the corrected overshoot-inclusive scan; Corner-Principle re-check
outcome: confirmed
tags: [computation, near-miss, gap-census, corner-principle, verification, counting-heuristic, universal-families]
scout: not-found — web/literature search for an existing (5,7,13) gap census: BealsTriples nearest-miss scanner (different methodology), Project Goliath signature sweeps ((5,7,13) not covered), Norvig survey, MSE gap-1 thread — none address the (5,7,13) gap distribution; attempt-24's C<=60 run remains the only data
node: beal-nearmiss-5713-widbox-verify
---

# Attempt 26 — (5,7,13) wider-box census: min genuine gap 1771 CONFIRMED (not corrected)

Worker dispatch on node `beal-nearmiss-5713-widbox-verify` (uses:
[[near-miss-stratification]], proven). Verifies attempt-24's `to-verify`
flag: its min non-degenerate coprime near-miss gap **1771** at $(A,B,C)=(6,3,2)$
was found in the box $A\le6000$, $B\le600$, $C\le40$; this run widens the box
and re-runs the census to confirm or correct it.

## Method and box (as run)

New script
[`scripts/search_5713_widbox.py`](../scripts/search_5713_widbox.py) (3.5 s,
pure Python, exact integer arithmetic):

- **Box actually run: $C\le120$, $B\le2\cdot10^4$, $A$ unbounded above**
  ("all $A\ge1$" — $A$ is derived per $(C,B)$ as the exact-nearest 5th root,
  so every $A$ with $A^5\le C^{13}+B^7$ in the box is covered;
  $A\le120^{13/5}\approx2.55\cdot10^5$ automatically). $\chi=-264/455\approx-0.5802$ unchanged.
- **Gap definitions preserved exactly** from `search_5713.py` /
  `near_miss_package.py`: genuine gap $=\min|A^5+B^7-C^{13}|$ over coprime
  ($\gcd(A,B,C)=1$) bases $A,B,C\ge2$, excluding exact solutions (gap 0);
  gap-1 hits enumerated separately with T1 family labels; quasi-degenerate
  layer ($A^5=C^{13}$ or $B^7=C^{13}$, gap $=B^7$ resp. $A^5$) excluded from
  the genuine min and tracked separately (T3).
- **Scan pattern = the corrected scan of attempt-25** (`near_miss_package.py`):
  the overshoot region $B^7>C^{13}$ is included (candidates $A\in\{2,3,4\}$
  there), fixing the break-at-$B^7>C^{13}$ bug that `search_5713.py`'s
  min-gap loop still carries. A best-based break cuts the $B$ loop once
  overshoot gaps provably exceed the running best (safe: $B^7$ increases in
  $B$). 617,334 candidate triples evaluated; 3.5 s.
- Completeness of the candidate set per $(C,B)$: for $\mathrm{rem}=C^{13}-B^7\ge32$
  the minimizers of $|A^5-\mathrm{rem}|$ over $A\ge2$ are exactly
  $\lfloor\mathrm{rem}^{1/5}\rfloor,\lfloor\mathrm{rem}^{1/5}\rfloor+1$; for
  $\mathrm{rem}\in[1,31]$ and for overshoot ($\mathrm{rem}\le0$) it is $A=2$
  (checked as $\{2,3,4\}$, pattern parity).

## Run result (numbers verbatim)

- **Exact solutions $A^5+B^7=C^{13}$: 0** (0 coprime) — Beals-consistent.
- **Gap-1 census: 2 hits, both unit-base, both on the universal
  $t^{65}+1$ family**: $(1,1,1)$ [t=1] and $(8192,1,32)$ [t=2], gap $=+1$,
  coprime. **Genuine (all bases $\ge2$): 0.** Note the widened box now
  *catches* the $t=2$ family member ($A=2^{13}=8192\le C^{13/5}$), which
  attempt-24's box ($A\le6000$) truncated away — so "every gap-1 hit lies on
  a universal family" is now non-vacuously witnessed in-box (T1 verified at
  $t\in\{1,2\}$, the largest $t$ with $t^5\le120$).
- **Min genuine coprime gap: 1771 at $(A,B,C)=(6,3,2)$, val $=+1771$,
  $\gcd=1$ — unique argmin.** Attempt-24's value is **CONFIRMED, not
  corrected**, in the wider box.
- Smallest distinct genuine gaps: 1771 @ (6,3,2); 2880 @ (5,3,2); 8743 @
  (7,2,2); 11405 @ (15,7,3); 96341 @ (17,5,3); 105470 @ (17,6,3); then
  $1.6\cdot10^5$ and up. The runner-up scale explodes with $C$ (per-$C$
  minima: C=2: 1771; C=3: 11405; C=4: 276246; C=5: 2336017; C=6: 293253;
  C=7: 22215642; ...), confirming the attempt-24 structural reading: the
  min is small-base corner arithmetic, and no rare large-$C$ coincidence
  beats it anywhere in $C\le120$.
- **Corner Principle: HOLDS** — corner ($C\le3$) min = 1771 = full-box min;
  the min sits at $C=2$.
- **Quasi-degenerate layer (coprime, in box): min 2187 at $(8192,3,32)$**
  (gap $=B^7$, $t=2$ member of the $A^5=C^{13}$ side). $2187>1771$, so the
  T3 exclusion does not touch the min *inside* the box.
- **Unit-base channel ($A=1$ or $B=1$, other bases $\ge2$): min gap 1 at
  $(8192,1,32)$** — again the universal family member.

## to-verify resolution

Attempt-24's flag ("wider-box run ... to test the 1771 box-min's
robustness") is **discharged: 1771 at $(6,3,2)$ is confirmed** as the box
minimum over the strictly larger box $C\le120$, $B\le2\cdot10^4$ (all $A$),
with the corrected overshoot-inclusive scan and the T3 filter. This
independently re-confirms attempt-25's robustness run ($C\le100$,
$B\le10^5$, 0/56 violations) on this signature at a differently-shaped box
(larger $C$, smaller $B$); the counting-heuristic's rate claims, which rest
on this datum, stand on verified ground.

## Degenerate-vs-genuine breakdown (box census)

| layer | definition | hits in box | min gap |
|---|---|---|---|
| exact (gap 0) | $A^5+B^7=C^{13}$ | 0 | — |
| gap-1, unit-base (T1) | some base $=1$ | 2 — both on $t^{65}+1$ ($t=1,2$) | 1 |
| gap-1, genuine | all bases $\ge2$ | **0** | — |
| quasi-degenerate (T3) | $A^5=C^{13}$ or $B^7=C^{13}$, coprime | $t=2$ column: $(8192,B,32)$, odd $B\in[3,2\cdot10^4]$ | 2187 ($=3^7$) |
| genuine (metric) | coprime, bases $\ge2$, gap $>1$, quasi excluded | min at $(6,3,2)$ | **1771** |

The $B^7=C^{13}$ quasi side is absent in-box ($C=t^7\ge128>120$); the
$A^5=C^{13}$ side enters only at $t=2$ ($C=2^5=32$).

## Honest caveats

- **Box, not global proof.** 1771 is the exact minimum over the box
  $C\le120$, $B\le2\cdot10^4$, $A\ge2$ — a much stronger lower bound than
  attempt-24's, but still not a proof of a global minimum. Structural
  argument (per-$C$ minima grow; 5th-power spacing $\sim A^4$ grows with
  $A\sim C^{2.6}$) makes it robust, but a deep coincidence at some
  $C>120$ is not logically excluded.
- **The T3 filter is load-bearing, and the box boundary shows it**: just
  outside the box, $(A,B,C)=(3,8192,128)$ has $B^7=C^{13}=2^{91}$ and hence
  gap $=3^5=243<1771$ (coprime, all bases $\ge2$, $C=2^7=128>120$). Any
  census that includes the quasi-degenerate layer without T3's exclusion
  would "correct" the min down to such layer values — measuring the layer,
  not the problem (exactly T3's warning). With the exclusion, 1771 is the
  genuine min in-box and the layer min (2187) is strictly larger.
- **$B_{\max}$ never binds for the min**: in-box $B\le(C^{13})^{1/7}\le7272$
  covers the entire in-shoot region, and the best-based break cuts
  overshoot at $B^7-C^{13}>1739$; so $B\le2\cdot10^4$ is fully covering and
  the binding expansion here is $C$: $40\to120$.
- The A=1 / B=1 unit-base channel (min 1, on a universal family) is
  excluded from "genuine" by the bases-$\ge2$ convention exactly as in
  attempt-24; T1 makes this exclusion theorem-grade (global, unconditional).
- The `scout:` line records the dispatch's existing-proof search result
  (consistent with attempt-25's novelty checks; not re-searched here).
- Ollama-only environment respected: the new script is pure computation, no
  model backends, no API keys.

## Next

1. The empirical line's data point is now verified at the wider box; the
   natural continuation per attempt-25's mechanism is the sixth signature
   $(7,11,13)$ ($\chi\approx-0.536$, reverse-direction monotonicity probe)
   run under the *corrected* scan.
2. Prove-or-scan the next quasi-degenerate boundary: for $C\ge128$ the
   $B^7=C^{13}$ layer enters with gap $=A^5\to3^5=243$ — worth a one-line
   remark in the preprint that the genuine metric *must* carry the T3
   filter (a referee-reproducibility point, not a conjecture).
3. Attempt-25's open thread stands: prove no non-unit-base gap-1
   near-miss exists in the open class (0 found across 56 signatures and
   now $2\times$ at $(5,7,13)$).
review: target-reviewer 2026-09-09 APPROVED — widened-box census semantically and numerically faithful to attempt-24/25 anchors and T1 (1771@(6,3,2) confirmed, script modifies only the box + disclosed scan machinery); outcome `confirmed` is folder precedent — SCHEMA vocabulary amended additively 2026-09-09.

## Correction (2026-09-09, final-review finding; supersedes the "smallest distinct genuine gaps" readout above, which is retained for the record)

The scan's candidate pair {floor, floor+1} is complete for the unrestricted minimizer of |A^5-rem| but NOT for the coprime-restricted one: when floor is non-coprime, the restricted column min can sit at floor-1. A structurally independent census (final-review verification, widened candidates {fl-1, fl, fl+1}, no best-based break) finds six genuine in-box gaps the readout missed: **4939 @ (5,2,2)**, 8435 @ (3,4,2), 10802 @ (7,3,2), 69965 @ (2,5,2), 70176 @ (3,5,2), 70957 @ (4,5,2). So the 3rd-smallest in-box genuine gap is 4939 (not 8743), and "then 1.6*10^5 and up" is false (8th-smallest is 69965). The HEADLINE min is UNAFFECTED: 1771 @ (6,3,2) stands as unique argmin (two independent scans agree no coprime genuine gap < 1771 exists in-box), as do 0 exact solutions, the two T1 gap-1 hits, Corner Principle, and quasi-degenerate 2187 > 1771. The completeness bullet above is corrected by the widened-candidates fix in `scripts/search_5713_widbox.py` (same commit). Caveat now carried forward: the same {floor, floor+1} assumption underlies the 56-signature table's per-signature minima (attempt-25) — flagged `to-verify` for a cheap widened-window re-run before any further use of the runner-up structure (the Corner-Principle minima themselves are small-base and were adversarially verified in attempt-25, but the re-verify is cheap and owed).

Also disclosed: "617,334 candidate triples" is the script's internal loop counter, not independently reproducible across structurally different scans (final-reviewer note).

**Fix-wave implementer note (2026-09-09, same commit; discloses a readout-vs-census delta):** the ruled fix as implemented scans candidates {fl-1, fl, fl+1} (fl = floor(rem^(1/5)), rem = C^13 - B^7 >= 2^5, clamped to A >= 2) plus small-A {2,3,4,5} for rem in [1,31] and overshoot, break dropped. Its readout (9,210,857 candidate triples, 13.3 s) contains five of the six census gaps above (4939, 8435, 69965, 70176, 70957) and, beyond the census, 4981 @ (4,3,2), 11317 @ (5,4,2), 73058 @ (5,5,2) — the overshoot-side entries the census's unextended {2,3,4} overshoot pattern did not reach. **10802 @ (7,3,2) sits at fl+2 for its column (rem = 6005, fl = 5, rem closer to 6^5 = 7776 than to 5^5 = 3125)** — outside the mandated 3-candidate window — so it stays absent from the script readout while remaining a genuine in-box gap per the census (whose window was evidently nearest-root {n-1, n, n+1}, reaching fl+2 in the upper half of a 5th-power interval but missing fl-1 entries such as 4981 @ (4,3,2)). The script readout's 8th-smallest distinct genuine gap is therefore 11405, not the census's 69965 (which is census-relative); `to-verify` if the fl+2/nearest-root widening should be folded into the script. Min 1771 @ (6,3,2) unaffected in every scan.
