# Notes — Beal's Conjecture

> Loose scratch: observations not yet worthy of a full attempt, candidate
> reformulations, sparks to chase. Promote good ones into attempts.

## Sparks

- **Mordell-curve reformulation of the gap.** The gap-1 near-misses satisfy
  $A^x + B^y = C^z + 1$. For the cubic-cubic-cubic sub-case $a^3+b^3=c^3+k$,
  fixing $k$ ties to integral points on Mordell-type curves. Is there a uniform
  bound on coprime solutions to $a^3+b^3-c^3 = k$ as $k$ ranges? (Catalan
  [[thm-catalan-mihailescu]] is the $k=1$, two-term case.) Worth a literature
  check.

- **abc does not suffice.** Worked through in attempt-01: the abc conjecture
  yields, for $1/p+1/q+1/r<1$, that $C$ is bounded — i.e. finiteness per
  signature, *no stronger* than the unconditional Darmon–Granville. So abc is
  not the missing ingredient for the "zero" claim. File this so we don't
  revisit. [[method-abc-finiteness]]

- **Parametric coprime families with $\gcd>1$.** Many exact solutions are
  scalings of a single primitive relation, e.g. $3^3+6^3=3^5$ is
  $3^3(1+2^3)=3^3\cdot 9 =3^5$. General pattern: if $u^x+v^y = w$ with $w$ a
  perfect $z$-th power and a common factor $d$ is "built in", you get a
  Beal-consistent family. Cataloguing these might reveal *why* the coprime
  case is empty — the only way to close is to share a factor.

- **Modularity on a *stack*?** The Frey obstruction is that three different
  exponents give incommensurate local data. Could one attach not an elliptic
  curve but a higher-dimensional abelian variety (a "Frey variety" à la
  Darmon–Merel / Bennett–Skinner) whose modularity is now accessible? This is
  the live research direction; needs a real literature dive.

- **Descent angle.** For a putative primitive solution, can one run an
  infinite-descent on the *exponents* (reduce $(p,q,r)\to$ smaller) the way FLT
  classical proofs do for $n=3,4$? The mixed-exponent case breaks the symmetry
  descent exploits. Pin down where.

## Dead ends (so far)

- "Sum is too far from a perfect power" — **refuted** by the gap-1 near-misses
  (Ramanujan $1729$). Do not pursue metric/density arguments.

## To verify

- Exact statement and attribution of Darmon–Granville (1995); confirm it is
  unconditional on Faltings (Mordell) only, no abc.
- Full list of signatures resolved to *zero* to date (Darmon–Merel,
  Bennett–Skinner, $(2,3,n)$ results, etc.).
- Whether the Frey-curve conductor computation for, say, signature $(3,3,5)$
  is already in the literature and what it yields.