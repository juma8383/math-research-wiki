---
type: attempt
problem: beals_conjecture
attempt: 08
date: 2026-08-24
approach: Examine the Siksek–Stoll (3,4,5) mechanism (even-exponent → spherical reduction + Chabauty) and test transferability to the distinct-prime frontier
outcome: partial
tags: [even-exponent, spherical-signatures, parametrization, chabauty, scope-limit]
loop_cycle: 6 of 20
---

# Attempt 08 — The (3,4,5) route, and why it stops there

The one classical tool flagged in attempt-07 as not-yet-examined: how the
sporadic solved signature $(3,4,5)$ was cracked (Siksek–Stoll), and whether any
of that machinery reaches toward $(3,5,7)$. Filed
[[method-spherical-reduction]].

## The mechanism (reconstructed)

$(3,4,5)$ is solved by exploiting the **even exponent $4=2\cdot2$**: write
$y^4=(y^2)^2=W^2$, reducing $x^3+y^4=z^5$ to $x^3+W^2=z^5$, i.e. signature
$(2,3,5)$. The signature $(2,3,5)$ is **spherical**
($1/2+1/3+1/5=31/30>1$), and spherical signatures have **explicit
parametrizations** of all primitive solutions (Beukers 1998; for $(2,3,5)$
the 27 Edwards families, 2004). The Siksek–Stoll step (reconstructed): take the
$(2,3,5)$ parametrization, impose the extra "$W$ is a perfect square"
condition $W=y^2$ plus primitivity, and the survivors lie on genus-$\geq2$
curves resolved by **Chabauty / Mordell–Weil sieve**.

> Honesty flag: the mechanism is reconstructed from general principles (even
> exponent → $2$-signature → spherical parametrization → impose-square →
> Chabauty). The attribution to Siksek–Stoll and the exact computational step
> should be verified against their paper. The *structural* conclusion below
> does not depend on the computational details.

## The decisive finding: the route is *doubly* gated, and (3,5,7) fails both gates

Gate 1 — **an even exponent must be present** to expose the hidden $2$.
$(3,5,7)$ has exponents $3,5,7$, all odd primes. **No reduction to a
$(2,\cdot,\cdot)$ signature exists at all** — the very first step cannot be
written down.

Gate 2 — **even with an even exponent, the reduced $(2,\cdot,\cdot)$ signature
must be spherical** ($(2,2,n),(2,3,3),(2,3,4),(2,3,5)$) to get the
parametrization boost. The window is narrow:
- $(3,4,5)\to(2,3,5)$ ✓ — the *largest* spherical signature, the boundary case.
- $(3,4,7)\to(2,3,7)$ is **hyperbolic** ($1/2+1/3+1/7<1$) — *not* parametrized,
  so the route fails for $(3,4,7)$ too.

So the $(3,4,5)$ success is genuinely special: it has an even exponent **and**
it lands exactly on the spherical boundary $(2,3,5)$. Neither neighbor of the
form $(3,4,n)$ with $n\geq7$ benefits.

## Synthesis — the fifth convergent thread

This is the **fifth** independent structural reason (after modular method
[[method-frey-level-lowering-obstruction]], Darmon program
[[method-darmon-program]], Mordell lens [[method-mordell-curve-lens]], descent
[[method-infinite-descent]]) that the distinct-odd-prime frontier is beyond
current methods. The full diagnosis now spans *five* angles, all breaking at
$(3,5,7)$ for distinct reasons:

| thread | structure it needs | why (3,5,7) breaks it |
|---|---|---|
| modular / Frey | one level-lowering prime strips all bases ($\ell\mid2\gcd$) | only $\ell=2$; useless |
| Darmon program | repeated-exponent signature | distinct-prime only classified, undeveloped |
| Mordell lens | genus 1 (cubic-cubic) | genus 4 |
| descent | cyclotomic factorization of $x^p+y^q$ | no factorization for $p\neq q$ |
| spherical reduction (this) | an even exponent → a $2$-signature → spherical | no even exponent; reduction nonexistent |

## Bonus: closes the attempt-07 caveat

Attempt-07 left the composite-exponent neighbors $(3,4,n)$ as an unverified
caveat, relying on the survey's "smallest open = $(3,5,7)$" claim. This cycle
clarifies the *structural* side: even if $(3,4,n)$ for $n\geq7$ were open, the
spherical-reduction route would not touch them (they reduce to hyperbolic
$(2,3,n)$, not spherical). The route is not a transferable tool for the
distinct/composite-prime frontier; it is a narrow bridge that happens to land
exactly on $(2,3,5)$ from $(3,4,5)$.

## Honest outcome

**partial — angle exhausted, confirms existing state.** No new attack vector;
this cycle's value is closing the last "unexamined classical tool" gap and
raising the convergent diagnosis from four threads to five. The frontier
$(3,5,7)$ is now confirmed unreachable by *every* classical tool, each for an
independent reason. What remains is genuinely new-machinery territory.

## Next cycles

- **Synthesis page**: a consolidated "state of the attack" capturing the
  five-thread diagnosis as a reference page (high value for future sessions).
- **Lint pass**: wiki is now ~22 pages — check orphans/contradictions,
  especially cross-refs to the new method page.
- Beyond classical tools: a speculative cycle on what genuinely-new machinery
  the distinct-prime case would require (honest framing — likely nothing
  actionable, but maps the "what would a proof need" question).