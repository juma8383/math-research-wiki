---
type: attempt
problem: beals_conjecture
attempt: 03
date: 2026-08-24
approach: Ingest Darmon's program (arXiv:2205.15861); determine whether it reaches (3,5,7)
outcome: partial
tags: [ingest, darmon-program, abelian-varieties, irreducibility, distinct-prime-signatures]
loop_cycle: 1 of 20
---

# Attempt 03 — Does Darmon's program reach $(3,5,7)$?

attempt-02 concluded the path to $(3,5,7)$ runs through Darmon's program, gated
on a missing irreducibility theorem. This attempt ingests the program's primary
source [[dv2022]] to check whether that path is even *open* for three-distinct-
prime signatures.

## Ingest

[[dv2022]] = Billerey–Chen–Dieulefait–Freitas, "On Darmon's program for the
generalized Fermat equation, I" (arXiv:2205.15861). Filed with claim tags
[dv2022-frey-av, -irreduc-conjecture, -repeated-only, -55p-cartan, -1111n].

## Findings

### 1. The program is real and general in construction [dv2022-frey-av]
Frey elliptic curves are replaced by **Frey abelian varieties of GL₂-type**
over totally real fields: the Jacobian $J_r$ of Kraus' hyperelliptic curve
$C_r(a,b)$ (dimension $(r-1)/2$) becomes GL₂-type over $K=\mathbb Q(\zeta_r)^+$.
Residual 2-dim Galois representations of **bounded conductor** attach to a
putative solution for **all signatures** (Thm 2.8: cyclotomic determinant →
trivial-character modularity). So the *attachment* step generalizes fully.

### 2. The irreducibility conjecture is wide open [dv2022-irreduc-conjecture]
**Darmon Conjecture 1.2** — a constant $C(L,F)$ such that mod-$\mathfrak p$ images
contain $\mathrm{SL}_2(\mathbb F_{\mathfrak p})$ for large norm — is **"still wide
open."** It is the abelian-variety analogue of **Mazur's theorem**, and **no
such general theorem exists** for GL₂-type abelian varieties over totally real
fields. This *confirms* the "crux of the crux" from attempt-02 — the blocking
ingredient is exactly a generalized-Mazur irreducibility theorem, and it is not
available even for the repeated-exponent signatures the program does treat
(hence results there are conditional, e.g. $(5,5,p)$ conditional on the Cartan
case Conjecture 1.3).

### 3. The decisive refinement: the program handles repeated exponents only [dv2022-repeated-only]
The developed modular method treats **$(r,r,p)$ and $(p,p,r)$** — signatures
with a **repeated exponent**. **Remark 2.4:** Darmon *classified* Frey
representations for three-distinct-prime signatures $(p,q,r)$, but "these are
not considered in this work."

> **Therefore Darmon's program does NOT currently reach $(3,5,7)$.** It is,
> like the classical Frey method [[method-frey-modularity]], a repeated-exponent
> tool. $(3,5,7)$ is outside the scope of *both* the classical and the abelian-
> variety modular methods as they stand.

## What this changes vs attempt-02

attempt-02 said: "path forward = Darmon's program, blocked on missing
irreducibility theorem." That was slightly too optimistic. The refinement:

- $(3,5,7)$ is blocked at **two** levels, not one:
  1. **The modular method for three-distinct-prime signatures is undeveloped**
     (only a Frey-variety *classification* exists; Remark 2.4).
  2. **The irreducibility conjecture 1.2 is wide open** — and even the
     repeated-exponent cases that *are* developed are mostly *conditional* on
     it (or its Cartan subcase).

So $(3,5,7)$ is not merely "hard via the known program"; it is **beyond the
known program's current scope**, and the program's own scope is itself gated on
an open conjecture. This is an important calibration: a modular proof of
$(3,5,7)$ would require (i) extending the Frey-variety modular method to
three-distinct primes and (ii) proving a generalized-Mazur irreducibility
theorem — each a major open project.

## Honest outcome

**partial.** No progress toward a *proof*; instead a sharpened (and humbler)
understanding of the frontier: $(3,5,7)$ is outside current modular methods
entirely, not just gated on one theorem. Filed [[method-darmon-program]] and
source [[dv2022]] so the wiki records this correctly.

## Next threads (for subsequent cycles)

- **Side angle, independent of modular methods:** the Mordell-curve / elliptic-
  fiber viewpoint on the gap-1 near-misses (attempt-01). This may bypass the
  modular obstruction entirely. Promote to a full cycle.
- **Computational:** exhaustive $(3,5,7)$ search to a large bound + near-miss
  structure for distinct-prime signatures specifically.
- **Descent:** pin down exactly why classical infinite descent (FLT $n=3,4$)
  fails for mixed exponents — a non-modular angle.
- **Neighbors of $(3,5,7)$:** confirm $(3,5,5)$, $(3,3,7)$, $(5,5,3)$ status —
  is $(3,5,7)$ truly the boundary, or are adjacent repeated-exponent signatures
  also open?