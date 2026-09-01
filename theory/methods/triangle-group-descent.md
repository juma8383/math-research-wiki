---
type: method
name: Triangle-group / nonabelian descent (the (2,3,7) route and its scope limit)
created: 2026-08-24
tags: [number-theory, nonabelian-descent, triangle-groups, chabauty, scope-limit]
used-in: [[beals_conjecture]]
provenance: []
---

# Triangle-group / nonabelian descent

The geometric reduction behind Poonen–Schaefer–Stoll's complete resolution of
$x^2+y^3=z^7$, and why the same route is unavailable for all-distinct-odd-prime
signatures. (Mechanism synthesized from the literature on the (2,3,7) case;
triangle-group finiteness criterion is standard.)

## The reduction that already exists: Darmon–Granville covering descent

[[thm-darmon-granville]] does more than assert finiteness: its *proof* is a
**reduction to finitely many curves**. Via unramified coverings of
$\mathbb P^1\setminus\{0,1,\infty\}$ of signature $(p,q,r)$ plus the
Chevalley–Weil theorem, infinitely many primitive solutions of
$Ax^p+By^q=Cz^r$ would yield infinitely many rational points on a curve of
genus $>1$ over a number field — contradicting Faltings. So a
"reduce-to-finitely-many-curves" mechanism **does exist in general**. The
catch: Faltings is **ineffective** — it proves the finite set exists but
neither enumerates it nor shows it is empty. (This corrects the over-strong
claim in attempt-11 that "no such reduction is known.")

## Making it effective: the (2,3,7) precedent (Poonen–Schaefer–Stoll)

Poonen–Schaefer–Stoll (2007) made the reduction *effective* for $x^2+y^3=z^7$,
determining all 16 primitive solutions. The engine was **nonabelian descent**
through the finite simple group $\mathrm{PSL}_2(\mathbb F_7)$ (order 168):
- the descent reduces the problem to rational points on **10 twists of the
  Klein quartic** (genus 3),
- those with $\operatorname{rank}J<\operatorname{genus}$ are settled by
  **Chabauty–Coleman**,
- the hard case ($\operatorname{rank}=\operatorname{genus}=3$) is finished by a
  **Mordell–Weil sieve** + modularity/level-lowering (Ribet).

This is precisely the "reduce to finitely many genus-$\ge2$ curves + resolve"
template of direction (B) in attempt-11 — and it *worked*.

## Why it stops there: the near-spherical boundary and the exponent 2

> **Correction (attempt-17, cycle 15):** an earlier version of this section
> mislabeled $(2,3,7)$ as "spherical." In fact $1/2+1/3+1/7=41/42<1$, so
> $(2,3,7)$ is **hyperbolic** (infinite triangle group) — it is the hyperbolic
> signature *closest to* the spherical boundary ($\chi=1/p{+}1/q{+}1/r-1=-1/42$,
> the negative value nearest $0$). The text below is the corrected framing;
> the structural conclusion (PSS does not transfer to $(3,5,7)$) is unchanged.

The finite group $\mathrm{PSL}_2(\mathbb F_7)$ is a **finite quotient of the
*infinite* triangle group $\Delta(2,3,7)$** — realized as the automorphism group
(order 168) of the Klein quartic, which is the modular curve $X(7)$. Two things
make PSS work at $(2,3,7)$, and $(3,5,7)$ has neither:

| signature | $1/p{+}1/q{+}1/r$ | type | $\chi$ | triangle group | finite quotient for descent? |
|---|---|---|---|---|---|
| $(2,3,5)$ | $31/30>1$ | **spherical** | $+1/30$ | finite (icosahedral $A_5$) | n/a — *parametrized* (thread 5) |
| $(2,3,7)$ | $41/42<1$ | hyperbolic | $-1/42$ (nearest 0) | **infinite** | **yes**: $\mathrm{PSL}_2(\mathbb F_7)$ via Klein quartic/$X(7)$ — PSS |
| $(3,5,7)$ | $71/105<1$ | hyperbolic | $-34/105$ (far from 0) | **infinite** | **no known** natural finite quotient / modular descent |

1. **Near-spherical position.** $(2,3,7)$ is the hyperbolic signature with
   $\chi$ closest to $0$ ($-1/42$); its triangle group, though infinite, has the
   distinguished finite quotient $\mathrm{PSL}_2(\mathbb F_7)$ tied to the Klein
   quartic. $(3,5,7)$ has $\chi=-34/105$, far deeper into the hyperbolic region;
   no analogous distinguished finite quotient / descent is known. (The
   triangle group $\Delta(3,5,7)$ is residually finite, so it *has* finite
   quotients in principle — but none known that yield a tractable modular-curve
   descent for $A^3+B^5=C^7$.)
2. **An exponent $2$.** The PSS modular interpretation rests on $X(7)$, the
   modular curve classifying elliptic curves with full level-$7$ structure, and
   the equation $x^2+y^3=z^7$ connects to elliptic curves precisely because of
   the $x^2$ term. $(3,5,7)$ has **no exponent $2$**, so the $X(7)$-type modular
   interpretation does not attach — the same "no $2$ available" obstruction as
   the modular method (thread 1) and the spherical reduction (thread 5).

So the obstruction at $(3,5,7)$ is two-fold: **deep hyperbolicity** (no
near-spherical finite quotient) **and no exponent $2$** (no modular-curve
interpretation). The Darmon–Granville covering descent still gives
*ineffective* finiteness, but the *effective* PSS step is unavailable.

## Synthesis: direction (B) is gated on the same "needs a 2" structure

Attempt-11 treated the geometric direction (B) as independent of the
spherical-reduction thread (5). The corrected triangle-group lens shows they
share a root: the PSS effective descent needs an **exponent $2$** (for the
$X(7)$ modular structure) — exactly the ingredient thread 5 needs (an even
exponent exposing a $2$) and thread 1 needs (a usable Frey/level structure).
$(3,5,7)$ lacks a $2$ in every role. So direction (B) is not an independent
escape; it is gated on the same absence of a $2$ and the same deep-hyperbolic
position. For all-distinct-odd-prime signatures, the modular, geometric, and
spherical routes are all blocked for related underlying reasons.

## When to reach for it

For a generalized Fermat signature, the PSS-style effective descent is a
candidate only when **both** hold: (a) the signature is **at or near the
spherical boundary** ($\chi=1/p{+}1/q{+}1/r-1$ close to $0$, so the infinite
triangle group has a distinguished finite quotient like $\mathrm{PSL}_2(\mathbb
F_7)$), and (b) the signature **contains a $2$** (giving an $X(r)$ modular-curve
interpretation). Spherical signatures ($\chi>0$) are instead *parametrized*
(thread 5, no descent needed). Deeply hyperbolic signatures with no $2$ — the
all-distinct-odd-prime regime, e.g. $(3,5,7)$ — satisfy neither condition: no
known natural finite quotient for descent and no modular-curve interpretation,
so only the ineffective Darmon–Granville finiteness remains.