---
type: method
name: Level-lowering obstruction for pairwise-distinct odd-prime signatures
created: 2026-08-24
tags: [number-theory, elliptic-curves, modular-forms, frey-curve, level-lowering]
used-in: [[beals_conjecture]]
provenance: []
---

# Level-lowering obstruction for pairwise-distinct odd-prime signatures

The structural reason the classical Frey/modularity/level-lowering machine
[[method-frey-modularity]] — which killed FLT and solved the repeated-exponent
signatures [[thm-solved-generalized-fermat-signatures]] — **cannot close** on
signatures $(p,q,r)$ of three pairwise distinct odd primes (e.g. Beal's
smallest open case $(3,5,7)$).

## Setup (signature $(p,q,r)$, distinct odd primes)

For a putative primitive $A^p+B^q=C^r$, the natural Frey-type curve is

$$E:\ Y^2 = X(X - A^p)(X + B^q).$$

Its three roots are $0,\ A^p,\ -B^q$, so the elliptic discriminant is

$$\Delta = 16\,(A^p\, B^q\, C^r)^2 = 16\, A^{2p}\, B^{2q}\, C^{2r}$$

(using $A^p+B^q=C^r$). Bad reduction is at primes dividing $2ABC$.

## The level-lowering arithmetic

Ribet's level lowering at a prime $\ell$ strips a bad prime $q\mid ABC$ (multiplicative
reduction, $q\neq\ell$) only when $\ell \mid v_q(\Delta)$. So:

| primes dividing | $v_q(\Delta)$ is a multiple of $\ell$ when |
|---|---|
| $A$ | $\ell \mid 2p$ |
| $B$ | $\ell \mid 2q$ |
| $C$ | $\ell \mid 2r$ |

To strip **all** bad primes with a single level-lowering prime $\ell$ requires

$$\ell \mid 2p,\quad \ell \mid 2q,\quad \ell \mid 2r
\;\Longrightarrow\; \ell \mid 2\gcd(p,q,r).$$

For pairwise distinct odd primes $p,q,r$: $\gcd(p,q,r)=1$, so the only
possibility is $\ell=2$.

## The obstruction

Mod-$2$ level lowering is governed by parity / the $2$-torsion structure and is
not a useful irreducibility setting — and **Mazur's irreducibility theorem**
($\bar\rho_{E,\ell}$ irreducible for semistable $E$ and $\ell>163$, with refined
bounds) does not apply at the small primes $\ell\in\{p,q,r\}$ anyway. Hence:

> **No odd prime $\ell$ strips all three bases for a pairwise-distinct odd-prime
> signature.** Any level lowering leaves a conductor carrying primes from at
> least two of $\{A,B,C\}$, which vary with the (unknown) putative solution, so
> the argument cannot terminate at a *fixed* contradiction level.

## Contrast: why repeated-exponent signatures fall

For $(p,p,r)$: $\Delta \propto A^{2p}B^{2p}C^{2r}$. Level lowering at $\ell=p$
strips **both** $A$- and $B$-primes (since $p\mid 2p$), leaving only $C$-primes in
the residual conductor — a structurally simpler, single-base residual that
additional methods (image-of-inertia conditions, multi-Frey, Kraus-type
arguments, Chabauty) can often close. This is how $(3,3,n)$,
$(5,5,7)$, etc. were solved [[thm-solved-generalized-fermat-signatures]].

For $(p,p,p)$ (FLT): $\Delta\propto(ABC)^{2p}$, lowering at $\ell=p$ strips
**everything** → residual level a power of $2$ → no weight-2 form → instant
contradiction.

## Why $(3,5,7)$ is exactly the frontier

$(3,5,7)$ is the smallest Beal signature (all $\geq3$, $1/p+1/q+1/r<1$) with
three pairwise distinct odd primes [rg2024-357-smallest]. By the obstruction
above, it is the smallest signature **structurally immune** to the classical
single-Frey/single-level-lowering argument. Concretely:

$$\Delta = 16\, A^{6}\, B^{10}\, C^{14},\qquad
\gcd(6,10,14)=2,$$

so only $\ell=2$ divides all three exponents $6,10,14$ — useless for level
lowering. Closing $(3,5,7)$ requires **new machinery**: higher-dimensional Frey
varieties over number fields (Darmon's program — Frey abelian varieties of
$\mathrm{GL}_2$-type over totally real fields), where the relevant mod-$p$
representations live on abelian varieties rather than elliptic curves, and no
Mazur-style irreducibility theorem is yet available. **That missing
irreducibility theorem is the crux of the crux.**

## When to reach for it

Use this to *diagnose* a signature before attempting Frey methods: compute
$\gcd(2p,2q,2r)=2\gcd(p,q,r)$. If it is $2$ (pairwise distinct odd primes), the
classical method is blocked — go directly to the number-field / abelian-variety
program, or to descent/factorization if a special algebraic factorization
exists. If it is $>2$ (a repeated odd prime), the classical method is in play
with a tractable residual.