---
type: attempt
problem: yang_mills
attempt: 2
date: 2026-08-24
approach: Primary-source verification of the two load-bearing facts ([ym-clay-jaffe-witten], [ym-balaban-rg]) against the Clay official page and Balaban's CMP papers / Dimock's exposition; then deepen direction (A) — the concrete blocker for transporting a lattice spectral gap to the continuum uniformly in a, and where O(4) covariance fails
outcome: confirmed
tags: [verification, primary-source, balaban-rg, continuum-limit, mass-gap-transport, o4-covariance, cross-problem]
---

# Attempt 02 — Verify Jaffe-Witten + Balaban, deepen direction (A)

Cycle 3 of the math-work loop. YM had only attempt-01; its "Next" note was:
*verify the load-bearing facts against primary sources (Jaffe-Witten Clay
write-up; Balaban's RG papers; the 2025-26 preprints' actual claims), then
deepen direction (A): what concretely blocks transporting a lattice spectral
gap to the continuum uniformly in $a$, and where does $O(4)$ covariance fail?*
This cycle does the verification half and the deepening half.

## [ym-clay-jaffe-witten] CONFIRMED (primary source: Clay official page)

Verified against the Clay Mathematics Institute official problem page
(https://www.claymath.org/millennium/yang-mills-the-maths-gap/) and the
official problem-description PDF by Jaffe & Witten. The exact wording:

> **Yang–Mills Existence and Mass Gap.** Prove that for any compact simple
> gauge group $G$, a non-trivial quantum Yang–Mills theory exists on
> $\mathbb R^4$ and has a mass gap $\Delta>0$. Existence includes establishing
> axiomatic properties **at least as strong as** those cited in Streater &
> Wightman (1964), Osterwalder & Schrader (1973), and Osterwalder & Schrader
> (1975).

Two things this nails down, both flagged `to-verify` in attempt-01:

1. **The "at least as strong" clause is real and exact.** Existence is not
   merely "some QFT" — it must meet Wightman / Osterwalder-Schrader (1973, OS
   positivity; 1975, the reconstruction sharpening) **at least as strongly**.
   So OS reflection positivity is a *hard requirement* of the problem, not an
   optional refinement. This matters directly for Eriksson's conditional
   result (below), which leaves OS reflection positivity OPEN.

2. **The framework-existence wrinkle is in the official text.** Jaffe-Witten:
   *"one does not yet have a mathematically complete example of a quantum
   gauge theory in four-dimensional space-time, nor even a precise definition
   of quantum gauge theory in four dimensions."* This validates the
   "uniquely-hard wrinkle" recorded in attempt-01 / progress.md — unlike
   NS/BSD/Beal, the *definition* of the object is itself part of the open
   content. `[ym-existence-open]` re-confirmed.

Douglas's Clay status report (2004) is the corroborating secondary source;
it frames lattice approaches, SUSY YM, and Seiberg-Witten as the landscape.
`[ym-clay-jaffe-witten]` moves from `to-verify` to **CONFIRMED**.

## [ym-balaban-rg] CONFIRMED + sharpened (primary sources: Balaban CMP; Dimock)

Verified against Balaban's original *Comm. Math. Phys.* papers and Dimock's
three-part exposition. Balaban's program is **11 papers (CMP 95–122,
1984–89)** on YM in $d=3,4$, all on the **UV problem**:

| paper | CMP | content |
|---|---|---|
| propagators / RG transforms | 95,96,99,102 (84-85) | setup |
| averaging ops | 98 (85) | blocking |
| regular gauge fields / gauge fixing | 99 (85) | gauge handling |
| RG I: small-field + coupling renorm | 109 (87) | weak-coupling control |
| RG II: cluster expansions | 116 (88) | polymer decay |
| **convergent renorm expansions** | **119 (88)** | **UV stability bounds, β-function, polymer rep** |
| **large-field ℝ-op I, II** | **122 (89)** | **completes UV stability** |

The load-bearing clarification (attempt-01 only said "incomplete"):

- **What Balaban PROVES:** *UV stability* — the effective densities $\rho_k$
  produced by the inductive RG transformation satisfy bounds **uniform in the
  lattice spacing $\varepsilon$** (CMP 102, Theorem 1, for 3D pure gauge; the
  4D case via the full series + the ℝ-operation in CMP 122). Plus polymer
  representation with exponential decay, β-function extraction, and
  irrelevance of the dimension-6 remainder (after subtracting vacuum energy +
  marginal operators). This is **asymptotic freedom made constructive on the
  lattice**: control of the short-distance / weak-coupling regime.

- **What Balaban LEAVES OPEN:** the **continuum limit** (convergence as
  $a\to0$ to a non-trivial 4D QFT), the **mass gap**, the **IR**, full
  **constructive reconstruction**. UV stability is a necessary input to a
  continuum-limit proof, not the proof itself.

So the precise status: **Balaban = the UV half of the UV→IR bridge.** He
controls the RG flow *where the coupling is weak* (small scales, $g\to0$ by
asymptotic freedom). The mass gap lives at the *other* end — long distances,
strong coupling — where Balaban's convergent weak-coupling expansions give no
expansion parameter. This is the structural content of the obstruction,
sharper than attempt-01's "incomplete."

Dimock's exposition is the clean secondary confirmation:
- Part I (small fields), *Rev. Math. Phys.* **25**, 1330010 (2013);
- Part II (large fields), *J. Math. Phys.* **54**, 092301 (2013);
- Part III (convergence), *Ann. Henri Poincaré* **15**, 2133–2175 (2014).
`[ym-balaban-rg]` moves from `to-verify` to **CONFIRMED**.

## Eriksson 2026 — two new honesty flags (NOT a resolution)

The verification surfaced two facts about the "recent claim"
`[ym-recent-claims-unverified]` that attempt-01 had not nailed down:

1. **It is on viXra, not arXiv** (viXra 2602.0077v1). viXra is essentially
   unmoderated — a much lower bar than arXiv, with no peer-review filter at
   all. This *raises* the skepticism bar for the claim, it does not lower it.
   A viXra-only "continuum limit of 4D YM" should be treated as a proposal to
   study, emphatically not a solution. (Same discipline that kept the Beal
   (2,3,7) spherical→hyperbolic correction honest and PSS flagged until
   verified.)

2. **Its result is CONDITIONAL on "Assumption A"** (a quantitative
   regularity hypothesis: squared-oscillation summability of the blocking
   map). Under Assumption A it gets: continuum limit on the algebra of
   **blocked** observables at **finite volume**, gauge-invariant + positive,
   and the abstract claims **Euclidean-covariant**. Remaining OPEN even
   conditionally: **OS reflection positivity, thermodynamic limit, mass gap,
   nontriviality** (extension to sharp Wilson-loop observables).

   **Discrepancy to verify:** the viXra *abstract* says "Euclidean-covariant,"
   but attempt-01 / progress.md flagged that Eriksson "explicitly only gets
   hypercubic $W^4$ covariance." These two statements conflict. The likely
   reconciliation (to confirm by reading the paper body, not the abstract):
   the *blocked-observable algebra* inherits only the hypercubic subgroup
   $W^4$ (signed permutations, order 384) from the lattice, and full $O(4)$ is
   claimed only as a *formal* covariance of the limit state, not a proven
   symmetry of the reconstructed QFT. I am **not** silently overriding the
   earlier flag — I record the conflict and leave it `to-verify` against the
   paper body. Either way, OS reflection positivity (a *hard requirement* per
   the confirmed Jaffe-Witten wording above) remains open, so the claim does
   not meet the problem's bar even if Assumption A held.

`[ym-recent-claims-unverified]` stays `to-verify`; sharpened with the
viXra/conditional/OS-open facts.

## Direction (A) deepened: the concrete blocker + where O(4) fails

With Balaban's scope pinned to the UV half, the direction-(A) question —
*what concretely blocks transporting a lattice spectral gap to the continuum
uniformly in $a$?* — has a clean answer, sharper than attempt-01.

**The two-regime split on the lattice.** Lattice pure-gauge YM has two
controlled regimes, and the continuum-limit point sits in neither's mass-gap
reach:

- **Strong bare coupling** (large $g_0$, the lattice's natural starting
  point): the strong-coupling cluster expansion (Osterwalder-Seiler; Münster)
  gives the **area law** → Wilson loop decay → confinement, i.e. a **mass gap
  at finite spacing**. But this is at *finite* $a$ with *large* $g_0$ — NOT
  the continuum-limit point.

- **Weak bare coupling** ($g_0\to0$, the continuum-limit point): asymptotic
  freedom fixes $\Lambda_{\text{YM}}$ as $a\to0$ by taking $g(a)\to0$. This is
  exactly where **Balaban's UV stability** applies. But the strong-coupling
  cluster expansion does **not** reach here — there is no expansion parameter
  at weak bare coupling for the *long-distance* (IR) spectrum.

**The blocker, stated precisely.** The mass gap is a **long-distance / IR**
statement. The lattice proves it (area law) only at **strong** bare coupling;
the continuum limit lives at **weak** bare coupling, where Balaban gives UV
control but no IR spectral bound. Transporting the gap to the continuum
requires a bound **uniform in $a$** that bridges the strong→weak bare-coupling
crossover — i.e. control of the RG flow *all the way* from the perturbative UV
(Balaban's domain) into the non-perturbative IR (the gap's home). No such
uniform-in-$a$ IR bound exists. This is the literal UV→IR bridge, and it is
exactly the "control runs out" boundary — the same structural shape as NS's
supercriticality (subcritical energy ↔ critical $L^3$), BSD's rank-$\ge2$
Euler-system shape, and Beal's distinct-odd-prime class.

**Where $O(4)$ covariance fails / is not yet restored.** The lattice has only
**hypercubic** $W^4$ symmetry (signed permutations of the 4 axes, order 384),
not full $O(4)$. Full $O(4)$ is supposed to be *restored* in the continuum
limit as the irrelevant $O(4)$-breaking operators (dimension-4 and higher,
suppressed by powers of $a$) vanish. Balaban's irrelevance bounds (the
dimension-6 remainder control) handle these in the **UV**. But restoration of
*full* $O(4)$ in the IR/continuum requires (i) the limit to be non-trivial
and (ii) the broken-symmetry irrelevant operators to vanish *uniformly* down
to long distances — which loops back to continuum-limit existence itself,
still open. So $O(4)$ restoration and continuum-limit existence are not two
problems but two faces of the same control problem. This is why Eriksson's
"Euclidean-covariant" abstract claim (even if taken at face value) is not
enough: covariance of a *blocked-observable, finite-volume* limit state is a
UV statement; full $O(4)$ of the reconstructed continuum QFT is the IR/limit
statement that remains open. (The discrepancy above — abstract "Euclidean"
vs body-level $W^4$ — is exactly this UV/IR distinction in disguise.)

**Cross-problem compounding.** The "two controlled regimes, the target sits
in the gap between them, and the blocker is controlling the crossover
uniformly" is the YM instance of the now-6-for-6 "obstruction at the
control/reduction step" spine:
- **Beal** — distinct-odd-prime class is the crossover no reduction mechanism
  survives;
- **BSD** — rank-$\ge2$ is the crossover no known Euler-system shape covers;
- **NS** — supercritical gap (subcritical energy ↔ critical $L^3$) is the
  crossover no global a priori bound crosses;
- **YM** — strong↔weak bare-coupling crossover is the gap no uniform-in-$a$
  IR bound crosses, with $O(4)$-restoration as its second face.
The "one-dimensional engine stops" sub-pattern also fits: Balaban's RG is a
single-scale (UV) engine; the gap needs the multi-scale (UV→IR) version that
stops being controlled at the crossover.

## Theory toolbox touched this cycle

No new theory pages needed (the verification *confirms* existing pages rather
than introducing new entities). `thm-balaban-rg` should be updated with the
UV-half / leaves-IR-open precision; `def-wightman-os-axioms` with the "at
least as strong" + OS-positivity-as-hard-requirement point. (Edits deferred
to keep this cycle one-move; flagged for a later Continue.)

## Honesty / to-verify (remaining)

- `[ym-clay-jaffe-witten]`: **CONFIRMED (attempt-02)** — exact wording + "at
  least as strong" clause + framework-existence quote, all against the Clay
  official page.
- `[ym-balaban-rg]`: **CONFIRMED (attempt-02)** — UV stability (uniform-in-$\varepsilon$
  density bounds) proven; continuum limit / mass gap / IR left open. Dimock
  exposition corroborates.
- `[ym-recent-claims-unverified]`: **sharpened, still to-verify.** Eriksson
  2026 is viXra-only (unmoderated), conditional on Assumption A, and leaves OS
  reflection positivity / thermodynamic limit / mass gap / nontriviality
  OPEN even conditionally. **Open discrepancy:** abstract "Euclidean-covariant"
  vs earlier flag "hypercubic $W^4$ only" — to resolve by reading the paper
  body, not the abstract.
- `[ym-supersymmetric]`: **still to-verify** (attempt-03 target) — confirm
  Seiberg-Witten/Nekrasov scope is $\mathcal N=2$ SUSY, not pure YM.

## Next

Two natural branches for attempt-03:
1. **Verify `[ym-supersymmetric]`** (Seiberg-Witten 1994 exact solution +
   Nekrasov localization) against primary sources — the solved RELATED model
   that illuminates the gap mechanism; confirm it is $\mathcal N=2$ SUSY YM,
   not pure YM, and extract what it does/does not say about pure-YM confinement.
2. **Resolve the Eriksson $O(4)$ discrepancy** by reading the viXra paper body
   (blocked-observable $W^4$ vs limit-state $O(4)$) — a small, honest
   cleanup of the recent-claim flag.
Both are single-move Continues. The rotation advances to hodge-conjecture
next regardless.