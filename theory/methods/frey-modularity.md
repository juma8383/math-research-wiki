---
type: method
name: Frey curve / modularity / level lowering
created: 2026-08-24
tags: [number-theory, arithmetic-geometry, elliptic-curves, modular-forms]
used-in: [[beals_conjecture]]
provenance: []
---

# Frey curve / modularity / level lowering

The engine that proved FLT [[thm-fermat-last]] and that Beal's mixed-exponent
case resists.

## The recipe (equal-exponent / FLT case)

Given a putative $a^p+b^p=c^p$ ($p\geq 5$ prime):
1. **Frey curve.** Attach $E:\ Y^2 = X(X-a^p)(X+b^p)$, semistable.
2. **Discriminant.** $\Delta = (abc)^{2p}$ (up to constant) — a perfect
   $2p$-th-power times a fixed constant. This uniform prime-power structure is
   the key.
3. **Modularity.** By the modularity theorem (Wiles et al.), $E$ corresponds to
   a weight-2 newform of level $N$ (the conductor).
4. **Ribet level lowering.** Ribet (1990) shows the modular form lowers to a
   newform of minimal level $2$ — but no weight-2 form of level $2$ exists.
   Contradiction. Hence no Frey curve, hence no FLT solution.

## Why mixed exponents break it (the Beal crux)

For a signature $(p,q,r)$ with $p,q,r$ not all equal, the Frey curve
$Y^2=X(X-A^p)(X+B^q)$ has discriminant carrying $A^{2p}B^{2q}C^{2r}$ — three
**incommensurate** exponent structures rather than one uniform $p$-power
profile. The conductor/discriminant no longer reduce to a single prime-power
shape, so Ribet's level lowering does not terminate at a contradiction. The
modular method therefore closes some signatures but not all; **no uniform
mixed-exponent argument is known**.

## Live repair directions

- **Higher-dimensional Frey varieties** (Darmon–Merel, Bennett–Skinner):
  attach abelian varieties of GL$_2$-type rather than elliptic curves, whose
  modularity is now partly accessible. Resolves some signatures.
- **Signature-specific attacks:** the $(2,3,n)$ and related programs handle
  mixed signatures one at a time, often combining modular methods with
  classical descent.

## When to reach for it

This is *the* framework for any attempt on a specific Beal signature after
[[method-exponent-reduction]]. The first concrete step on a target signature is
always: write the Frey curve, compute the conductor and discriminant
explicitly, and check whether level lowering closes. (Catalogued as the
attempt-02 plan in [[beals_conjecture]].)