---
type: method
name: Exponent reduction to {odd primes} ∪ {4}
created: 2026-08-24
tags: [number-theory, reduction]
used-in: [[beals_conjecture]]
provenance: []
---

# Exponent reduction to {odd primes} ∪ {4}

**Statement.** To prove Beal it suffices to rule out primitive solutions to
$A^p+B^q=C^r$ with each of $p,q,r$ an **odd prime or $4$**.

**Proof.** Let $x\geq 3$ be any exponent.
- If $x$ has an odd prime divisor $\ell$, then $A^x = (A^{x/\ell})^\ell$,
  reducing the exponent to $\ell\geq 3$.
- If $x$ has no odd prime divisor, then $x=2^k$ with $k\geq 2$ (since $x\geq 3$
  forces $x\geq 4$). Then $A^x = (A^{2^{k-2}})^4$, reducing the exponent to $4$.

Applying this to all three exponents keeps all of them $\geq 3$ and lands each in
$\{\text{odd primes}\}\cup\{4\}$. ∎

**Why it matters.** Cuts the exponent space from all integers $\geq 3$ to a
discrete, well-structured set tied to primes. This is the standard setup for the
generalized Fermat program: signatures $(p,q,r)$ with $p,q,r$ prime (or $4$)
and $1/p+1/q+1/r\leq 1$. Each such signature is then attacked individually
(Frey curves, modular methods). The reduction does *not* reduce the number of
cases to finitely many — there are infinitely many signatures — but it
standardizes them.

**When to reach for it.** At the start of any Beal/generalized-Fermat attack:
first apply [[method-pairwise-coprime-reduction]], then this, so the target is a
clean signature $(p,q,r)\in\{\text{odd primes}\}\cup\{4\}^3$ with
$1/p+1/q+1/r\leq 1$.