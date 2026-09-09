---
type: method
name: quartic-jacobian-fusion
created: 2026-09-07
tags: [number-theory, elliptic-curves, descent, computational]
used-in: [[magic_square_of_squares]]
provenance: private notes (K34 leaf-quartic round; classical 2-isogeny descent à la mwrank/eclib)
---

# Method — Quartic Jacobian fusion (one Jacobian, many quartics)

## Trigger pattern

A working notebook keeps a **family of diagonal binary quartics**
$y^2 = aX^4 + cX^2Z^2 + eZ^4$ (several $(a,e)$ sign/split arrangements of the
same coefficient budget) that it treats as separate unsolved objects, each
with its own census and its own ad-hoc kill machinery. Whenever the family
members share the **binary-quartic invariants**

$$I = 12ae + c^2,\qquad J = 72ace - 2c^3,$$

they share ONE Jacobian $E:\ y^2 = x^3 - 27Ix - 27J$ — and the whole family
becomes a single elliptic-curve computation. Check `I,J` first, before any
per-quartic work.

## What you get (all classical, all machine-computable)

1. **Descent-cover dictionary.** If $E$ has rational 2-torsion
   $T=(0,0)$ (test $e\cdot c^2$ structure; here $e \mid c^2$ patterns),
   the quartics $C_d:\ y^2 = dX^4 + cX^2 + c^2/d\,(ae\text{-family})$ are
   exactly the $\alpha$-covers of $E_a:\ y^2 = x^3 + cx^2 + (ae)x$ via
   $(X,y)\mapsto(dX^2,\ dXy)$, and
   $$C_d(\mathbb{Q})\neq\varnothing \iff d\in\operatorname{image}(\alpha),\quad
     \alpha(P)=x(P)\bmod\mathbb{Q}^{*2},\ \alpha(T)=c^2/\dots\ (=\ ae\ \text{class}).$$
   The image is computable: $\alpha(P)\alpha(P')=1$-class for doubles
   (duplication formula), $\alpha(P+T)=\alpha(P)\cdot\alpha(T)$; generators
   from the MW basis; Selmer bound from mwrank's first descent
   (`S^phi` ranks + els gens). **Classes outside the image = insoluble
   quartics — a proof, not a census.** Nontrivial classes = Sha[φ] elements.
2. **Rank-1 parametrization.** If $\operatorname{rank}(E_a)=1$ with
   generator $P$ and the class $d$ IS in the image, every rational point of
   $C_d$ comes from $T + 2mP$ (the fiber). Branch conditions imposed by the
   surrounding problem (parity, divisibility of $r,s$) become group-theoretic
   conditions on $m$ (often simple congruence classes of $m$).
3. **Fermat/Germain loops decode to the group law.** Completing-square +
   coprime-split descent steps on the quartic, re-applied to their own
   output, often equal the **index-halving map** $T+2mP\mapsto$ child of
   $m/2$ (verified exactly, index by index). When this holds, the "descent
   tree" cannot loop infinitely NOR close by descent — every chain lands on
   the killed residue class. Test it before hunting contradictions: the loop
   may be the parametrization in disguise.

## Procedure (what was actually run)

- Compute $(I,J)$ for every quartic in the family (one line of exact
  integer arithmetic; sympy/PARI not needed).
- If equal: `ellfromeqn` (PARI) for each → identical minimal model; mwrank
  on the clean model $y^2=x^3+cx^2+(ae)x$ (rational 2-torsion at origin)
  for rank + unconditional MW basis + Selmer groups.
- Verify the cover map pointwise at every already-known quartic point
  (there are usually degenerate ones: $X=0$, $X=\pm1$) and symbolically.
- Compute image(α) from the mwrank generator; compare leaf classes;
  insoluble leaves drop out; the live leaf gets the fiber parametrization.
- Re-run the old census conclusions with the box caveat (the fiber point
  at the smallest admissible index may sit OUTSIDE every filed box).
- For any descent loop on the live leaf: verify the loop child against the
  half-index fiber point EXACTLY (integers, `isqrt` only — do not factor).

## Pitfalls (all hit in the founding round)

- PARI `ellfromeqn` on symbolic input returns the GENERIC template — read
  the numeric model by substituting coefficients yourself.
- mwrank's "E"/"E′" labels and $(c,d)$ els conventions do NOT match raw
  coefficients; decode via the 2-torsion-shift before quoting.
- Quartic discriminants/`poldisc` of dehomogenized forms differ by
  square factors from the binary-form discriminant — for class membership
  use $(I,J)$ and the cover dictionary, not raw `poldisc` square classes.
- The completing-square split constants ($(c_1,c_2)$ with $c_1c_2=72$ in
  the founding case) are pinned by the quartic, but the ROLE assignment
  (which side is $c_1$) flips with the index's 2-adic class — test both.

## Founding instance

K34 leaf quartics of the magic-square-of-squares wiki: four "separate"
open quartics → one Jacobian → three proved insoluble + one parametrized +
its descent loop identified as the halving map (notes.md §2j of
`mss-k34-jacobian`, 2026-09-07).