# Progress — P vs NP

> Running state of the attack. **Read this first when resuming.** The
> detailed work lives in the self-contained nested wiki at [wiki/](wiki/);
> this file is the bridge/summary the main-wiki convention expects at
> `problems/<slug>/progress.md`. The nested wiki's catalog is
> [wiki/index.md](wiki/index.md) and its audit trail [wiki/log.md](wiki/log.md)
> — read those before any Continue rather than re-deriving. Consolidated
> through absolute **Cycle 28** (seventh loop, C3).

> **Provenance note.** This problem folder was created in a separate session
> as a self-contained LLM-wiki (`wiki/`) and ingested into the main wiki on
> 2026-08-25. The folder name `PvsNP` is PascalCase (not the kebab-case
> convention used by the other six problems, e.g. `birch-swinnerton-dyer`);
> the user explicitly chose this name, so it is kept. Cross-problem wikilink:
> `[[PvsNP]]`. The nested `wiki/` structure (own SCHEMA/index/log/pages/sources)
> differs from the main wiki's standard `problems/<slug>/{progress,notes,
> attempts}/` + shared `theory/` layout; it is **preserved as-is** (it is
> coherent and self-cataloging; destructively flattening ~70 files would be
> hard to reverse and gain nothing). These top-level files
> (`problem.md`/`progress.md`/`notes.md`) are the bridge, not a replacement.

## The exact frontier

No super-poly circuit lower bound for any natural class above $\mathrm{ACC}^0$.
Field frontier: $\mathrm{NEXP}\not\subseteq\mathrm{ACC}^0$ (Williams 2011);
$\mathrm{NTIME}[n^{\mathrm{polylog}\,n}]\not\subseteq\mathrm{P/poly}$
(Murray–Williams 2017); Chen–Tal–Wang 2026 $n^{2.5-\varepsilon}$
$\mathrm{THR}\circ\mathrm{THR}$. The $\mathrm P\neq\mathrm{NP}$ gap =
$\mathrm{NP}\not\subseteq\mathrm{P/poly}$.

## The central obstruction (the unifying meta-finding)

**`[witness-needs-explicit-lb]`** — the wall is an **open construction**, not
a proven impossibility. Across **seven loops / 28 cycles**, every live
P≠NP-adjacent route bottlenecks on the same task:

> *Construct an **explicit** lower-bound-carrying / average-case-hard
> witness for a restricted class. Cheap inputs — worst-case lower bounds,
> non-uniformity, randomness — supply one only insufficiently; the explicit
> construction **is** the circuit-lower-bound problem (the natural-proofs
> frontier).*

The wall's lock is **non-compositional** `[balanced-point-non-compositional]`
and **axis-independent**: it blocks the size axis (S1.a lifting — a function
at the balanced point of {expensive ∧ small-gap}) AND the depth axis (KRW
direct-sum `[meir-2023]`) alike. The three local barriers (relativization /
natural proofs / algebrization) are **local symptoms**; the construction lock
is **universal** `[barriers-and-construction-are-complementary]` — escaping
all three (GCT, Cycle 26) does **not** remove the lock, it isolates it.

**The single live thread `[s1a-is-the-live-thread]`:** the breakthrough shape
**(A)** = an explicit function at the balanced point of {expensive ∧
small-gap} for the $\mathrm{AC}^0$ (S1.a) face, satisfying
{deterministically-constructible ∧ non-recognizable}. Gate 1 (recognizability)
discharged soft from three directions (Williams (⇒) non-targetability;
Ilango automaticity; recognizable-variation one-sidedness); Gate 2 (tight
window) is the binding residual. (A) is an **open construction** — blocked by
open-ness, not a theorem; genuinely alive at the hardest known point.

## The arc (7 loops / 28 cycles, 2026-08-21 → 2026-08-24)

1. **Loop 1 (Cycles 1–5):** the 10-agent fan-out survey + MCSP deep-dive;
   Route A/B bridges; the `[witness-needs-explicit-lb]` unification from
   seven angles (S1.a DNF / S2 general-circuit / S3 formula + depth-2
   threshold average-case). Proven `[n2-wall]` (SAT route) vs open
   construction (mining/CAPP route).
2. **Loop 2 (Cycles 6–10):** the AC⁰ (S1.a) face — thinnest face, LB-existence
   *passed* (Sipser/RST) but natural (P/poly)-recognizable ⇒ would collapse,
   not separate. Triple-conjunction wall → (Q-targetability).
3. **Loop 3 (Cycles 11–15):** wall compressed 2-D (two gates) → 1-D (one
   balanced point of two tensioned lifting-intrinsic conditions). Gate 1
   soft from three directions.
4. **Loop 4 (Cycles 16–20):** mining face — Tell's quantified-derand wire
   lever is REAL and quantitative, but guarded by the NEW Fan-Li-Yang
   black-box natural-proof barrier; the NEXP-LB route closes
   (natural-proofs-blocked for all NEXP-LB techniques); both routes converge
   on (A).
5. **Loop 5 (Cycles 21–25):** "connections humans have missed" survey — found
   NO missed connection, only under-synthesized known ones (Williams 2016,
   Dhayal-Impagliazzo 2020, Korten 2021, Ilango 2025). Honest meta-finding:
   the wall's lock is a **construction, not a connection**. (A) sharpened to
   its sharpest mechanistic form (determinism = recognizability; derandomization
   destroys non-recognizability).
6. **Loop 6 (Cycles 26–30 wait — actual 26–28):** FPⁿP route escapes FLY
   (Cycle 21 corrected a Cycle-19 over-extension); measure / disjoint-NP-pairs
   / descriptive-complexity pivots all re-collapse to the same lock;
   descriptive is the FIRST surface to escape relativization (one of three
   barriers) but not reach P≠NP.
7. **Loop 7 (Cycles 26–28):** GCT is the barrier-cleanest surface (escapes all
   three) — confirms the wall is the construction, not the barriers. Direct
   attack on (A) (CAPP template) localizes the construction lock to the
   bridge between two corners. Depth/KW surface barrier-profiled — the
   non-compositionality lock is axis-independent.

## Honest ceiling `[honest-ceiling]`

No breakthrough. No super-poly circuit LB for any natural class above
$\mathrm{ACC}^0$; no derandomization built; no NP-hardness of MCSP under
uniform-$\mathrm{AC}^0$ many-one reductions; no $\mathrm P\neq\mathrm{NP}$
proof. The product is a precise, falsifiable, mechanistically-sharpest map:
one obstruction (`[witness-needs-explicit-lb]`), one live thread ((A)),
seven sub-surfaces all re-converging on the same non-compositional
construction lock. The wall neither fell nor was proven impossible; it is
genuinely alive at one point. All web-grounded findings are
search/arXiv-summary-level, **NOT PDF-line-verified** unless noted
(`[s1a-chebyshev-phantom]`, `[gate-1-automatic]`, `[b-reduces-to-a]`,
`[a-is-intrinsic-not-lupanov-artifact]` are primary-source-grounded in
Ilango FOCS 2020 §1.3/§1.4 read verbatim).

## To-verify (the load-bearing flags)

- The web-grounded primary-literature findings (Williams 2016, Fan-Li-Yang
  2022, Chen-Williams-Yang 2023, Korten 2021, Chen-Tal-Wang 2026, Ilango 2025,
  etc.) are search/arXiv-summary-level, **not PDF-line-verified** — the
  natural next-session targets for a verification pass.
- The nested wiki's `[honest-ceiling]` tags mark each cycle's honest scope;
  see [wiki/pages/open-problems.md](wiki/pages/open-problems.md) for the
  ⭐-flagged highest-leverage targets (Route A / S1.a (A) / Res(⊕) size-rank
  / GCT flip / Gurevich logic-for-P).

## Next

The nested wiki's fifth-loop synthesis directs: **do not start an eighth
loop without the user's direction** — the wall's lock is a construction, not
a connection, and five loops of barrier-profiling have exhausted the
surveyable surface. The productive next move (if budget allows) is a
PDF-line verification pass of the load-bearing web-grounded findings, or a
direct construction attempt on (A) under the user's direction.