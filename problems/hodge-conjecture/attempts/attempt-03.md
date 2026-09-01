---
type: attempt
problem: hodge_conjecture
attempt: 3
date: 2026-08-24
approach: Verify the standard-conjecture known cases (Charles-Markman 2013 for hyper-Kahler K3^[n]) against the primary source, pinning the exact theorem + the B->all-in-char-0 logic
outcome: confirmed
tags: [verification, primary-source, standard-conjectures, hyperkahler, k3n, verbitsky, cross-problem]
---

# Attempt 03 — Verify Charles–Markman 2013: standard conjectures for $K3^{[n]}$

Cycle-10 Continue on Hodge (cross-problem loop, second pass; yellow zone
73.1% session / 49.6% weekly, 0 subagents). Attempt-02's `Next` offered two
moves; this cycle takes **(i)** — verify the standard-conjecture known cases,
specifically **Charles–Markman 2013** for hyper-Kähler $K3^{[n]}$-type, the
load-bearing known-case fact named in `progress.md`'s to-verify list and the
named "Next" target. Same discipline that caught the YM Eriksson
viXra/conditional sharpening and Beal's (2,3,7) spherical mislabel.

## Verification: Charles–Markman — CONFIRMED (standard conjectures for $K3^{[n]}$)

**Charles & Markman**, *The Standard Conjectures for Holomorphic Symplectic
Varieties Deformation Equivalent to Hilbert Schemes of K3 Surfaces*,
**Compositio Mathematica 149**(3) (March 2013), 481–494, DOI
[10.1112/S0010437X12000607](https://doi.org/10.1112/S0010437X12000607).

- **Theorem 1.1:** the **Lefschetz standard conjecture** (Conjecture **B**,
  algebraicity of the inverse Lefschetz operator $\Lambda$) holds for every
  smooth projective variety of **$K3^{[n]}$-type** (i.e. deformation-equivalent
  to the Hilbert scheme of $n$ points on a K3 surface).
- **Corollary 1.2:** the **standard conjectures** (all of them) hold for any
  smooth projective variety of $K3^{[n]}$-type — because in **characteristic
  zero** the Lefschetz standard conjecture is the **strongest** standard
  conjecture, so it implies the Künneth-components conjecture (Conj. **C**),
  the standard conjecture of Hodge type, etc. **This is the precise logic
  behind `progress.md`'s "B/C known for $K3^{[n]}$": B is proved directly, and
  B ⇒ C (and the rest) in char 0.**

## Journal correction (minor)

The query guessed *J. Inst. Math. Jussieu*; the actual venue is
**Compositio Mathematica** (149(3), 2013). Recorded to keep the citation
trustworthy. (A separate companion paper, Charles, *Remarks on the Lefschetz
Standard Conjecture and Hyperkähler Varieties*, **Comment. Math. Helv.**
**88**(2) (2013), 449–468, DOI [10.4171/CMH/291](https://doi.org/10.4171/CMH/291),
gives a variational/local approach in degree 2 via Kodaira–Spencer maps +
hyperholomorphic bundles — a complementary, narrower result.)

## Mechanism — and its control-step shape (the cross-problem echo)

The proof is *not* a direct cycle construction; it is a **control** argument,
and that is the genuine sharpening for the obstruction map:

- **Algebraic cycles from relative extension sheaves** on moduli spaces of
  stable sheaves on a K3 surface provide the correspondences.
- **Verbitsky's theory of hyperholomorphic sheaves** lets these algebraic
  cycles be **deformed across the entire $K3^{[n]}$ deformation class** via
  **twistor lines** — the cycle classes are *transported* (controlled) from
  one variety to every deformation.
- **Mukai-lattice monodromy** $O^+_{\Lambda(S)}(v)$-equivariance of the
  correspondences + a surjectivity argument (Prop. 6.1, Cor. 6.2, induction
  via Cor. 2.4) finishes it.

So the engine is: **construct the cycles on one representative, then control
their deformation** to the whole class via hyperholomorphic sheaves + twistor
lines. This is the same **control-not-resolution** shape as the other five
problems — the *resolution* (the algebraic correspondences) is built on a
convenient representative (the Hilbert scheme); the *control* (deformation
across the class via Verbitsky) is what makes it work for *all* $K3^{[n]}$-type
varieties. The obstruction-spine echo: the standard conjectures are open in
general precisely because this hyper-Kähler-specific **deformation control**
(Verbitsky hyperholomorphic sheaves + twistor lines) has no analogue for a
general smooth projective variety. The "one-dimensional engine stops"
sub-pattern: the Picard-variety/exponential-sequence control works for
divisors; the Verbitsky-twistor control works for $K3^{[n]}$; **general
varieties have neither** — direction (A)'s open core.

## What this confirms for direction (A)

- `progress.md`'s line "Standard conjectures B/C (Grothendieck): ... known for
  surfaces, abelian varieties, hyper-Kähler $K3^{[n]}$ (Charles–Markman
  2013)" is **CONFIRMED and now primary-source-backed**, with the precise
  logic (B proved directly for $K3^{[n]}$; B ⇒ all standard conjectures incl.
  C in char 0) and the precise mechanism (Verbitsky + twistor deformation
  control).
- This sharpens the attempt-02 finding (B/C are *open special cases of HC
  itself* per Deligne §4) with a **positive known-case island**: the open
  special cases are *known* for $K3^{[n]}$-type — so direction (A) is not
  uniformly hopeless, it has a verified deformation-control precedent in one
  geometric class. The gap is that this precedent is class-specific
  (hyper-Kähler, relying on Verbitsky/twistor structure a general variety
  lacks).

## Honesty / scope

- Charles–Markman CONFIRMED against the primary source (Compositio Math.
  149(3), 2013); journal corrected; B ⇒ C-in-char-0 logic and the
  Verbitsky/twistor deformation-control mechanism recorded.
- No proof of HC; the standard conjectures remain open for general smooth
  projective varieties. The verification is the cycle's point — one
  `progress.md` to-verify item (Charles–Markman 2013) is now resolved.
- Other to-verify items remain (hard Lefschetz reduction exact statement;
  Atiyah–Hirzebruch & Kollár integral counterexamples; the 2024–25 preprints'
  actual claims; the $\ell$-adic Tate analogue) — natural attempt-04 targets.
- Outcome: **confirmed** (verification goal met, mechanism pinned + journal
  corrected + control-step echo), **partial** overall (frontier unchanged).

## Next (attempt-04)

Continue resolving the remaining to-verify items: the **Atiyah–Hirzebruch &
Kollár integral-Hodge counterexamples** (the wrinkle that forces the
$\mathbb Q$-version of HC) and the **$\ell$-adic Tate analogue** (open even
for $H^2$, the char-$p$ parallel) are the next most load-bearing. Or
status-check the most-cited recent claim (Shimizu 2025). The rotation
continues: next cross-problem cycle → collatz-conjecture (attempt-03).