---
type: method
name: Pairwise-coprime reduction (Beal)
created: 2026-08-24
tags: [number-theory, reduction]
used-in: [[beals_conjecture]]
provenance: []
---

# Pairwise-coprime reduction

**Statement.** For any solution of $A^x+B^y=C^z$,

$$\gcd(A,B,C)=1 \iff A,B,C \text{ are pairwise coprime}.$$

**Proof.** Only the forward direction is nontrivial. If a prime $p\mid A$ and
$p\mid B$, then $p\mid A^x$ and $p\mid B^y$, so $p\mid (A^x+B^y)=C^z$, hence
$p\mid C$; then $p\mid\gcd(A,B,C)$, contradiction. Symmetric for the other two
pairs. ∎

**Why it matters / when to reach for it.** Use this to rewrite Beal's
"common-prime-factor" condition ($\gcd>1$) as the cleaner **"no pairwise-coprime
solution"** form. This is the form that connects to the generalized Fermat /
primitive-solution literature (Darmon–Granville, Frey curves all assume
primitivity). Whenever working Beal or any $A^x+B^y=C^z$ equation, reduce to the
pairwise-coprime (primitive) case first; the non-coprime solutions are
"scalings" and carry no structural difficulty (e.g. $3^3+6^3=3^5$ is
$3^3(1+2^3)$, $\gcd=3$).

See [[method-exponent-reduction]] for the companion reduction on the
exponents.