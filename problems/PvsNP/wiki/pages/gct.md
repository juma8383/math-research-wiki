---
title: Geometric Complexity Theory (GCT)
category: angle
tags: [mr-2004, bip-2019, elsw-2017, fi-2020-asymmetry, hl-2016, coarsening-gap, fixed-degree-escape, seventh-loop-cycle-1, gct-escapes-three-barriers, gct-flip-is-construction-lock, mulmuley-complexity-barrier-equals-witness-barrier, barriers-and-construction-are-complementary, flip-construction-objects-are-nphard, vnp-separation-not-pneqnp, gct-flip-needs-deep-open-math]
status: partially-blocked
last_touched: 2026-08-23
---

# Geometric Complexity Theory

## Core
Attack the algebraic analog — **permanent vs determinant** (VNP vs VP) — via representation-theoretic obstructions: a partition λ with multiplicity in the padded-permanent orbit closure coordinate ring exceeding that of the determinant orbit closure. Best unconditional bound is still quadratic `[mr-2014]` (dc(perm_m) ≥ m²/2).

## The transfer is conditional, not direct `[vnp-separation-not-pneqnp]` (CORRECTION, Cycle 26)
A prior version of this page claimed GCT "transfers to P≠NP via Valiant's #P-completeness of the permanent." That is **overstated**. VP≠VNP does **not** directly imply P≠NP. What is known (Bürgisser 2000; Valiant 1992; Koiran-Perifel): VP≠VNP ⟹ **P/poly ≠ NP/poly** (over F₂ by direct Boolean simulation; over general fields under GRH) — a *nonuniform* separation. Conversely VP=VNP ⟹ the **polynomial hierarchy collapses** (under GRH). Via depth reduction (Valiant-Skyum-Berkowitz-Rackoff 1983), VP is an algebraic analogue of **NC²**, so VP≠VNP ≈ algebraic nonuniform NC²≠#P — which does **not** rule out P=NP. So GCT's target is a **necessary but not sufficient** step toward boolean P≠NP; a complete GCT success leaves an open algebraic→Boolean, nonuniform→uniform transfer. Same "necessary-not-sufficient / transfer-gap" shape as the descriptive surface (CPT≠P ≠ P≠NP) and the Williams mining face (NEXP LB ≠ P≠NP).

## Why it is stuck — the coarsening barrier `[coarsening-gap]` (NOVEL)
Both known no-go theorems rule out only **coarse** invariants:
- `[bip-2019]` rules out **occurrence** obstructions (positivity of multiplicities, the coarsest 0/1 question) for n ≥ m^25.
- `[elsw-2017]` rules out **shifted partials** — a **sum** of multiplicities — for n > 2m²+2m.

Neither addresses **fine individual multiplicity differences**: a single multiplicity can exceed the determinant's even when the sum does not (the sum being smaller is consistent with one term larger, others smaller). This gap is real and under-appreciated; `[elsw-2017]`-style no-gos do not reach it.

## The fixed-degree escape `[fixed-degree-escape]` (NOVEL strategy)
`[fi-2020-asymmetry]`: plethysm Sym^d(Sym^n V) is **P-time for fixed OUTER degree d**, #P-hard for fixed inner. So the **permanent-side** plethysm coefficient a_λ(d,n) is tractable for fixed d — this removes the findability barrier on one side and concentrates **all** difficulty on the **determinant orbit-closure boundary** at small degree, which is unknown for n≥9 (only n=3 classified `[hl-2016]`).

## Where it breaks
The determinant boundary is the insurmountable bottleneck. Likely `[bip-2019]`'s m^25 threshold is very loose and the boundary swallows permanent representations far earlier (possibly already ~m²). Group-choice dilemma: tractable group GL(E)×GL(F) gives trivial bounds; meaningful group GL_{n²} is hard. No single explicit multiplicity obstruction for perm vs det under GL_{n²} exists. Even computational verification is infeasible at m=3,n=9 (astronomical dimensions).

## Barrier position — escapes all THREE local barriers `[gct-escapes-three-barriers]` (Cycle 26 upgrade)
GCT is the **first surface in the 26-cycle map to (claim to) escape all three local barriers simultaneously** — not just two:
- **Relativization** `[bgs-1975]`: GCT works on the **algebrized form** of computation (IP=PSPACE spirit) → the relativization barrier does not apply. (The wiki previously did not record this.)
- **Natural proofs** `[rr-1997]`: the proof technique exploits **characterization by symmetries** (Property D of det, Property P of perm), making it **extremely rigid** (Mulmuley's Rigidity Hypothesis: |UP_n| ≤ 2^{poly(n)}, far stronger than RR's mild largeness) → **automatically bypasses the RR largeness criterion** (Prop 7.3). Obstructions are not constructible as a truth-table predicate — the *same* property that makes them hard to find.
- **Algebrization/degree** `[aw-2008]`: perm and det have the **same degree**, so degree reasoning cannot distinguish them; GCT reasons on representation-theoretic multiplicity structure.
**Theorem 8.3 (Mulmuley, arXiv:0908.1932):** the #P≠NC result bypasses all three barriers **simultaneously** with **strongly explicit** obstructions (O(nk) bitlength, O(nk) time) — criterion-B evidence. **Honest caveat:** this is Mulmuley's claim at search/arXiv-summary level, NOT PDF-line-verified; the natural-proofs-via-rigidity escape is accepted in the GCT literature but is not a theorem in the RR framework. Its weakness is structural (the unknown determinant boundary, below), not barrier-theoretic.

## The flip IS the construction lock `[gct-flip-is-construction-lock]` (Cycle 26 — the central finding)
GCT's defining strategy, the **flip** (Mulmuley, GCT6 / arXiv:1009.0246), converts the lower-bound *nonexistence* problem (perm ⊄ det) into an *existence/construction* problem: explicitly exhibit **geometric obstructions** (Weyl modules V_λ on the padded-permanent class variety but not the determinant's) that are (1) **short** — poly(n) bitlength, (2) **easy to verify** — poly(n) time, (3) **easy to discover** — poly(n) constructible. This mirrors NP's own definition: short verifiable witnesses for *membership*; the flip seeks short verifiable witnesses for **nonmembership in P** (hardness). The **trivial obstruction** — an exponential counterexample table over all small circuits — has **"no short witnesses"** (Mulmuley). **This is precisely `[witness-needs-explicit-lb]`** relocated to algebraic geometry: the route to a lower bound runs through an explicitly-constructed short verifiable witness whose explicit construction IS the lower-bound problem. The construction lock is not avoided; it is the *entire point* of the flip.

### The construction lock bites TWICE `[flip-construction-objects-are-nphard]`
The flip requires obstructions that are *poly-time constructible*. But the objects it must construct — Kronecker and plethysm coefficients / their positivity — are themselves **NP-hard / #P-hard**: deciding **Kronecker positivity** is **NP-hard** (Ikenmeyer-Mulmuley-Walter 2017); deciding **plethysm positivity** is **NP-hard** and computing plethysm coefficients is **#P-hard / GapP-complete** (Fischer-Ikenmeyer 2020, Thms 3.5/3.6/3.8 — the wiki's `[fi-2020-asymmetry]`). So the "discover in poly time" half of the flip collides with the **very P≠NP-style hardness it is trying to prove** — the construction lock bites once (you must construct the witness) and again (the witness's components are themselves hard to construct). This is the concrete form of Mulmuley's self-referential "complexity barrier."

### Mulmuley's universal complexity barrier = the wiki's witness barrier `[mulmuley-complexity-barrier-equals-witness-barrier]`
Mulmuley calls the three (four) barriers **"local and mathematical"** (they rule out only restricted technique families) and posits a deeper **universal, complexity-theoretic complexity barrier**: P≠NP says "discovery is hard," which seems to imply "discovering its own proof is hard." Its formalization (GCT6) **is** the short-witness / explicit-construction problem — trading "hard complexity theory (the trivial infeasible obstruction)" for "hard mathematics (positivity hypotheses + obstruction hypothesis)" with the gain that P≠NP isn't expected to obstruct the *mathematics*. **The wiki's independent six-loop meta-finding** — "the wall's lock is a CONSTRUCTION not a CONNECTION/BARRIER," reached from four sub-surfaces (structural→measure→disjoint-pairs/proof-complexity→descriptive) — **converges with Mulmuley's formalization.** Not a missed connection (Mulmuley knew it); an **independent convergence** of two separate lines on the same obstruction, strengthening the diagnosis.

### The positivity core is deep OPEN math `[gct-flip-needs-deep-open-math]`
Per Theorem 10.2 (Mulmuley), an explicit obstruction family exists (m=2^{log^a n}, a>1) assuming **PH1** (multiplicity functions have #P-formulae with *positive* form, characterized by explicit parametrized polytopes) and **OH** (a complexity-theoretic obstruction hypothesis for small m). Proving PH1 requires extending **LR PH0** (positivity of canonical-basis structure coefficients for standard quantum groups, proved via the **Riemann Hypothesis over finite fields**, Deligne/Lusztig) to **Kronecker PH0** (analogous positivity for the **nonstandard quantum groups** of GCT4/7/8). The top-right corner of Mulmuley's commutative diagram — a nonstandard extension of RH over finite fields — is **unknown**. The "law of conservation of difficulty": the complexity-theoretic wall is traded for a representation-theoretic wall of comparable depth.

## The local/universal distinction `[barriers-and-construction-are-complementary]` (Cycle 26 — the sharpened meta-finding)
GCT is the **existence proof** for the map's central sharpened claim: escaping the three (local) barriers does **not** remove the construction lock — it **isolates** it. GCT pays to escape all three barriers (rigidity, algebrized form, representation-theoretic structure) and is left *exactly* with the flip = the full explicit-construction lock. Triangulated with the descriptive surface (Cycle 25: escapes *one* barrier, drops the construction lock on the *instance* side because CFI/multipedes are explicit + in P, but retains the weak-model-LB construction), the two surfaces pin the wall on two orthogonal axes:
- the **three barriers** are **local** — they block specific technique families;
- the **construction lock** is **universal** — it remains after every local barrier is escaped;
- **no surface is clean on both** (GCT: 3/3 barriers escaped, full construction lock retained; descriptive: instance-construction free, weak-model-LB locked).
**The real obstruction is the construction lock, and no barrier-escape removes it.** This is the strongest form of `[no-missed-connection-moved-wall]` and the sharpest `[witness-needs-explicit-lb]`: the wall is *not* the three barriers (local symptoms); the wall *is* the universal short-witness construction problem Mulmuley names the complexity barrier.

## Concrete next step
A computational-algebraic experiment: for n=4,5, classify holes of S(Det_n) under GL_{n²} (in saturation per Bürgisser-Ikenmeyer-Hüttenhain but absent from the orbit closure ring) and check whether any hole has positive permanent-side plethysm `[fi-2020-asymmetry]`. **Either outcome is publishable**: a hole with positive plethysm → first explicit multiplicity obstruction for perm vs det under GL_{n²}; none found → the boundary-swallowing kicks in far earlier than m^25 (a negative result narrowing GCT's viable regime). See [[algorithmic-gct]] for the Williams-style reframing of this bottleneck.

## See also
[[barriers]] · [[algorithmic-gct]] · [[semantic-invariant-gap]] · [[descriptive-complexity]] · [[open-problems]]