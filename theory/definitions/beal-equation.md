---
type: definition
name: Beal equation / generalized Fermat equation
created: 2026-08-24
tags: [number-theory, exponential-diophantine]
used-in: [[beals_conjecture]]
provenance: []
---

# Beal equation / generalized Fermat equation

The **Beal equation** is

$$A^x + B^y = C^z, \qquad A,B,C,x,y,z \in \mathbb Z_{>0},\ x,y,z \geq 3.$$

**Beal's conjecture** asserts every solution has $\gcd(A,B,C)>1$.

It is a special case of the **generalized Fermat equation**

$$X^p + Y^q = Z^r$$

studied via the *signature* $(p,q,r)$. The **reciprocal (Euler) invariant** is
$1/p+1/q+1/r$:
- $>1$: spherical / infinite families (e.g. Pythagorean-type).
- $=1$: Euclidean / borderline — only $(3,3,3),(2,4,4),(2,3,6)$ and perms.
- $<1$: hyperbolic — Darmon–Granville gives *finiteness* of primitive solutions.

Beal lives entirely in the $\leq 1$ regime (all exponents $\geq 3$ forces
$1/x+1/y+1/z\leq 1$, equality only at $(3,3,3)$).

**Primitive / coprime form.** A solution is *primitive* if $\gcd(X,Y,Z)=1$; by
[[method-pairwise-coprime-reduction]] this is equivalent to pairwise coprime
whenever the equation holds. Beal ⟺ "no primitive solution with all exponents
$\geq 3$."