---
type: method
name: Infinite descent (FLT n=3, n=4) and why mixed exponents break it
created: 2026-08-24
tags: [number-theory, descent, cyclotomic, UFD]
used-in: [[beals_conjecture]]
provenance: []
---

# Infinite descent — and why mixed exponents break it

The non-modular engine that closed FLT for $n=3$ (Euler) and $n=4$ (Fermat).
Understanding its three structural requirements explains *why* it cannot reach
the mixed/distinct-exponent Beal cases — complementing the modular-method
obstruction [[method-frey-level-lowering-obstruction]] and the cubic-only
Mordell lens [[method-mordell-curve-lens]].

## The two classical descents

### Fermat, $n=4$ ($x^4+y^4=z^4$, actually $x^4+y^4=z^2$)
$(x^2,y^2,z)$ is a Pythagorean triple, so (primitive) $x^2=m^2-n^2,\ y^2=2mn,\ z=m^2+n^2$. Then $y^2=2mn$ with $\gcd(m,n)=1$ forces $m=a^2,\ n=2b^2$ (a product of
coprime factors equalling a square ⟹ each is a square, up to the 2). This yields
a *smaller* solution — descent. Contradiction.

### Euler, $n=3$ ($x^3+y^3=z^3$)
Factor in the Eisenstein integers $\mathbb Z[\omega]$, $\omega=e^{2\pi i/3}$:
$$x^3+y^3=(x+y)(x+\omega y)(x+\bar\omega y).$$
$\mathbb Z[\omega]$ is a **UFD**; the three factors are "almost coprime" (up to
the prime $1-\omega$); UFD + the unit structure forces each factor to be a cube
up to a unit, producing a smaller solution — descent. (This is exactly the
gap-0 statement the Mordell lens [[method-mordell-curve-lens]] reformats as
"$E_{z^3}$ has no non-trivial integral points".)

## The three requirements (and where each fails for mixed exponents)

1. **A matching algebraic factorization.** Descent needs to split the LHS into
   conjugate linear factors whose "almost-coprimality" forces each to be a
   perfect power. This exists only when the *two LHS terms share one exponent*:
   $x^n+y^n=\prod_k(x+\zeta_n^k y)$ (cyclotomic), or the square/Pythagorean
   structure for $n=4$.
   - **Fails for $p\neq q$** (e.g. $(3,5,7)$): $x^p+y^q$ admits **no**
     conjugate-linear factorization. *The first descent step does not exist.*
     This is the fundamental obstruction for the fully-distinct case.

2. **The factor-power must match the RHS-power.** The factorization makes each
   LHS factor "want to be" a $p$-th power (from the $x^p+y^p$ structure). Descent
   closes only when the RHS is *the same* power: $z^p$. 
   - **Fails for $(p,p,r)$ with $r\neq p$**: factors want to be $p$-th powers, but
     the equation only supplies an $r$-th power on the RHS. The mismatch prevents
     the "smaller solution" construction from closing. *This is why $(p,p,r)$
     needed the modular method [[method-frey-modularity]], not descent.*

3. **Unique factorization in the factorization ring.** Even when (1) and (2)
   hold, descent needs the cyclotomic ring $\mathbb Z[\zeta_p]$ to be a UFD.
   - $\mathbb Z[\omega]$ (for $p=3$) is a UFD ✓. But in general
     $\mathbb Z[\zeta_p]$ is **not** a UFD once $p$ is large enough (Kummer's
     discovery). Kummer salvaged factorization-style proofs for **regular
     primes** ($p$ not dividing the class number $h_p$) via ideal theory, but
     **irregular primes** (the first is $p=37$) break it. The failure of unique
     factorization in cyclotomic rings is historically what forced the move from
     descent/factorization to ideal theory and ultimately to the modular method.
     (Exact UFD boundary for $\mathbb Z[\zeta_p]$ — to verify.)

## Summary table

| requirement | FLT $(p,p,p)$ | $(p,p,r)$, $r\neq p$ | $(p,q,r)$ distinct |
|---|---|---|---|
| (1) matching factorization | ✓ ($p=p$) | ✓ ($p=p$) | **✗ no factorization** |
| (2) factor-power = RHS-power | ✓ ($r=p$) | **✗** ($r\neq p$) | ✗ |
| (3) cyclotomic UFD | ✓ small $p$ | ✓ small $p$ | n/a |

The Beal frontier $(3,5,7)$ fails at requirement (1) — there is simply no
cyclotomic factorization of $x^3+y^5$. No descent can even begin.

## When to reach for it

Only for **equal-LHS-exponent** equations with **small** exponents where the
cyclotomic ring is a UFD — i.e. the classical FLT $n=3,4$ territory (and a few
small primes via Kummer). For anything mixed or with large primes, descent is
structurally unavailable; the modular method (or nothing) remains.

## Cross-reference
This is the descent companion to [[method-mordell-curve-lens]] (which reframes
the *cubic* descent in elliptic-curve language) and to
[[method-frey-level-lowering-obstruction]] (the modular-method version of "why
distinct exponents resist"). All three converge: the cubic case is the unique
meeting point of (genus 1) + (cyclotomic UFD factorization) + (FLT self-power
match) — which is why it alone fell to classical methods.