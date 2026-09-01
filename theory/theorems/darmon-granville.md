---
type: theorem
name: Darmon–Granville finiteness
created: 2026-08-24
tags: [number-theory, exponential-diophantine, arithmetic-geometry]
used-in: [[beals_conjecture]]
provenance: []
---

# Darmon–Granville finiteness

**Statement.** Fix integers $p,q,r\geq 2$ with

$$\frac{1}{p}+\frac{1}{q}+\frac{1}{r} < 1.$$

Then the generalized Fermat equation $X^p+Y^q=Z^r$ has only **finitely many**
*primitive* (pairwise-coprime) solutions in positive integers.

**Mechanism.** Darmon & Granville (1995) realize the equation as a family of
curves and apply Faltings' theorem (the Mordell conjecture): for fixed
$(p,q,r)$ in the hyperbolic regime, the relevant curve has genus $\geq 2$, so
only finitely many rational/integer points.

**Relevance to Beal.** Every Beal signature has $1/x+1/y+1/z\leq 1$, and every
one except $(3,3,3)$ is strictly $<1$. So Darmon–Granville gives *finiteness* of
primitive solutions per signature unconditionally; $(3,3,3)$ is FLT
[[thm-fermat-last]] (zero solutions). **The entire open content of Beal is
upgrading "finitely many" to "zero" for each signature** — i.e. showing each
finite Darmon–Granville set is empty.

**Important contrast.** This is *finiteness*, not *nonexistence*. The abc
conjecture gives the same finiteness (see [[method-abc-finiteness]]); neither
alone reaches the "zero" claim that Beal needs.

**Provenance note.** Exact attribution and statement to be verified against the
1995 paper; the finiteness-via-Faltings core is standard. (See notes.md
to-verify list.)