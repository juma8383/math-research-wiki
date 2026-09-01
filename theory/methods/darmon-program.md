---
type: method
name: Darmon's program (Frey abelian varieties of GL2-type)
created: 2026-08-24
tags: [number-theory, arithmetic-geometry, abelian-varieties, modular-forms, hilbert-modular]
used-in: [[beals_conjecture]]
provenance: [[dv2022]]
---

# Darmon's program — Frey abelian varieties of GL₂-type

The successor to the classical Frey-curve method [[method-frey-modularity]],
designed for signatures where no elliptic Frey curve exists. Source: [[dv2022]].

## Core idea

Replace the Frey **elliptic curve** by a higher-dimensional **Frey abelian
variety** $A$ over $\mathbb Q$ that becomes of **GL₂-type** over a totally real
field $K$. Concretely [dv2022-frey-av]:

- Start from Kraus' hyperelliptic curve $C_r(a,b)$; its Jacobian $J_r$ has
  dimension $(r-1)/2$.
- $J_r$ becomes of GL₂-type over $K=\mathbb Q(\zeta_r)^+$, the maximal totally
  real subfield of the $r$-th cyclotomic field.
- Residual 2-dimensional Galois representations with **bounded conductor** are
  attached to a putative solution (Theorem 2.8: determinant = $p$-adic
  cyclotomic character → trivial-character modularity), for *all* signatures.

This is the abelian-variety analogue of the Frey curve + modularity + level
lowering recipe, lifted to totally real fields (Hilbert modular forms).

## The blocking ingredient [dv2022-irreduc-conjecture]

**Darmon's Conjecture 1.2:** there exists $C(L,F)$ such that for primes
$\mathfrak p$ of large norm, the mod-$\mathfrak p$ image contains
$\mathrm{SL}_2(\mathbb F_{\mathfrak p})$. **Status: wide open.** This is the
generalization of **Mazur's theorem** (which classifies mod-$p$ images for
elliptic curves over $\mathbb Q$ and yields irreducibility for large $p$). **No
analogous general theorem exists for abelian varieties of GL₂-type over totally
real fields.** This single gap is what keeps the program conditional. This
confirms and sharpens the "crux of the crux" identified in attempt-02 of
[[beals_conjecture]].

## Scope — repeated exponents only [dv2022-repeated-only]

Crucially, the *developed* modular method treats **$(r,r,p)$ and $(p,p,r)$** —
signatures with a **repeated exponent**. Darmon *classified* Frey
representations for three-distinct-prime signatures $(p,q,r)$, but **these are
not developed** (Remark 2.4 in [[dv2022]]). So:

> Darmon's program, like the classical Frey method, is fundamentally a
> **repeated-exponent** tool. The three-distinct-prime case — including Beal's
> frontier $(3,5,7)$ — has a Frey-variety *classification* but no working modular
> method, and is additionally blocked by the open irreducibility conjecture.

## Partial / conditional results

- $(11,11,n)$: no nontrivial primitive solutions when $2\mid a+b$ or $11\mid a+b$
  (unconditional, Thm 1.5 [dv2022-1111n]).
- $(5,5,p)$: reduces to CM forms, needs only the **Cartan case** of the
  conjecture; conditional on Conjecture 1.3 → no solutions for large $p$
  [dv2022-55p-cartan].
- $(7,7,*)$: second volume.

## When to reach for it

For a signature with a **repeated odd prime** exponent where the classical Frey
elliptic curve is insufficient (e.g. larger $r$ where no semistable Frey curve
over $\mathbb Q$ has the right conductor), Darmon's program is the right frame —
but expect the result to be **conditional** on Conjecture 1.2/1.3 unless a
propagation trick (as for $(11,11,n)$) is available.

For a **three-distinct-prime** signature like $(3,5,7)$: the program does not yet
apply. See [[method-frey-level-lowering-obstruction]] for why the classical
method is blocked there, and the open irreducibility conjecture above for why
the abelian-variety generalization is not yet ready. **$(3,5,7)$ is beyond the
current reach of BOTH the classical and the Darmon programs.**