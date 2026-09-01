# Collatz — notes (scratch / dead ends / half-formed ideas)

> Appended 2026-08-31 (breakthrough-hunt session). Two entries: one candidate
> KILLED by prior art, one literature update.

## [2026-08-31] m-cycle exclusion frontier has MOVED: Wang 2026 (Zenodo) claims m ≤ 93 — kills the "m=92 deadlock" candidate

The breakthrough-hunt produced a candidate ("the m=92 deadlock theorem": the
CF partial quotient $a_{44}=37$ of $\log_2 3$ leaves no K-rung covering the
$m{=}92$ activation threshold $\mathrm{lhs}(92)\approx3.09\times10^{20}$, so
Hercher's program stalls at $m\le91$ regardless of verification progress).
Adversarial verification: arithmetic SURVIVED (independent recomputation;
constants need exact-rational correction: lhs(92)=3.093e20, threshold
$X_0>2^{73.25}$), but the **decisive novelty check REFUTED the premise**:

- **Wang 2026** (Xinjun Wang, Zenodo preprints, June 2026, UNREVIEWED —
  `10.5281/zenodo.20557259`, `.../20588490`, `.../20589910`) claims a
  reproducible computer-assisted exclusion of Collatz m-cycles for **m ≤ 93**
  — crossing m=92 — using a "suffix-balanced block method" that *avoids*
  Hercher's block estimate, exact rational interval arithmetic,
  **continued-fraction denominator certificates**, and Simons–de Weger-type
  upper bounds. (Surfaced by the novelty-lens verifier; secondhand Zenodo
  summaries; full read `to-verify`.)

So the "deadlock" is not a true barrier — it is a barrier only for
Hercher's specific ladder program, already bypassed by a different
certificate construction. **Candidate killed (append-only, per protocol);
no note written.** Residual value of the CF-rung analysis: it explains the
2010–2025 stall and quantifies the ladder mechanism; if Wang's preprints
fail verification, the analysis becomes relevant again.

**Literature updates the folder was missing (from the same hunt/verify):**
- Cycle exclusion now stands at **m ≤ 91 peer-reviewed** (Hercher, J. Integer
  Sequences 26 (2023), Article 23.3.5, arXiv:2201.00406 — the wiki recorded
  only Simons–de Weger m ≤ 75; `theory/theorems/collatz-cycle-bounds.md` is
  STALE and needs a Hercher line + a Wang-flagged m ≤ 93 line).
- Barina's verification limit moved to $2^{71}$ (Jan 2025; project-reported,
  published figure $2^{68}$, J. Supercomput. 81:810 (2025)) — attempt-05's
  `2^71` flag can be upgraded to "published 2025" [to-verify volume/page].
- Hercher also shows: verifying convergence to $1536\cdot2^{60}=3\cdot2^{69}$
  would suffice for $K>1.375\times10^{11}$ odd members — the
  verification→cycle-exclusion coupling.

## Next
- Lint task: update `theory/theorems/collatz-cycle-bounds.md` (Hercher 2023,
  Wang 2026 flagged unverified) — natural next Lint cycle item.