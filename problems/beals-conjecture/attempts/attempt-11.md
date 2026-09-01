---
type: attempt
problem: beals_conjecture
attempt: 11
date: 2026-08-24
approach: Forward-looking analysis — what genuinely-new machinery would a (3,5,7) proof require; honest reframing of the obstruction
outcome: partial
tags: [new-machinery, reduction-vs-resolution, forward-looking, honest-assessment]
loop_cycle: 9 of 20
---

# Attempt 11 — What would actually crack $(3,5,7)$?

With five classical tools mapped to five independent failures (synthesis.md),
this cycle asks the forward question honestly: *if* a proof of the
distinct-prime case exists, what new machinery must it invent? The point is not
to manufacture hope but to name, as precisely as possible, where real progress
would have to come from — and to rule out the directions that *sound* promising
but recapitulate a known obstruction.

## The sharpened reframing: obstruction is at *reduction*, not *resolution*

This is the key insight of the cycle. Across all five threads, the failure is
**not** at the *resolution* step (proving the finite/zero result on a given
curve) but at the *reduction* step (getting from the Diophantine equation to a
finite, tractable geometric object):

| thread | reduction mechanism it lacks | resolution it *would* have |
|---|---|---|
| Frey/modular | a single level-lowering prime (only $\ell=2$) | Ribet descent + modularity (works when reduction exists) |
| Darmon program | developed modular method for distinct primes | same, on GL₂-type varieties |
| descent | cyclotomic factorization of $x^p+y^q$ | the descent step (works when factorization exists) |
| Mordell lens | genus 1 (needs cubic-cubic) | integral-point computation (works at g=1) |
| spherical reduction | an even exponent + spherical landing | Chabauty on the resulting curves |

The crucial observation: **the resolution tools are all available** —
Chabauty/Coleman, Mordell–Weil sieve, effective Faltings (Baker-type bounds),
quadratic Chabauty all *can* resolve a given genus-$\geq2$ curve in practice,
and this is exactly how the sporadic solved cases were finished (e.g.
$(3,4,5)$ ended in Chabauty on the genus-$\geq2$ curves produced by the
spherical reduction). **What is missing for distinct primes is any mechanism
that reduces $A^p+B^q=C^r$ to a *finite* collection of curves to run those
resolution tools on.**

So the honest one-sentence statement of what's needed:

> A proof of $(3,5,7)$ requires a **reduction-to-finite-curves mechanism that
> does not rely on a shared exponent, an even exponent, or a spherical
> parametrization.**

Every existing reduction mechanism uses one of those three; $(3,5,7)$ has none.

## Two candidate new-machinery directions

### (A) Modular — extend Darmon's Frey-variety program

The Frey abelian variety *construction* is general (distinct-prime signatures
are classified, Remark 2.4 in [[dv2022]]). What is undeveloped is the
*modular method* on it, plus the irreducibility input. Concretely a proof needs
**both**:
1. A level-lowering theorem for residual 2-dim Galois representations of
   GL₂-type abelian varieties over the totally real field
   $K=\mathbb Q(\zeta_r)^+$, for three-distinct-prime signatures.
2. **Darmon Conjecture 1.2** — generalized-Mazur irreducibility for these
   representations [[dv2022-irreduc-conjecture]] — currently wide open.

This is the most *principled* direction (it generalizes the engine that
actually closed FLT and the repeated-exponent cases). It is "two programs away,"
not one theorem. Real, but very hard.

### (B) Geometric/computational — a non-spherical reduction + effective Chabauty

> **CORRECTED by attempt-14 / cycle 12.** The claim below that "no such
> reduction is known" is **too strong**: Darmon–Granville's covering descent
> (Chevalley–Weil + Faltings) *is* such a reduction to finitely many genus-$>1$
> curves, but it is **ineffective**. The effective precedent (Poonen–Schaefer–
> Stoll, $(2,3,7)$) needs a **spherical** (finite) triangle group; $(3,5,7)$ is
> hyperbolic, so the technique is unavailable. See
> [[method-triangle-group-descent]] and the refined synthesis.md. The text is
> kept here unchanged as the append-only record; treat the correction as
> authoritative.

The alternative: find *some* way to reduce $A^3+B^5=C^7$ to finitely many
genus-$\geq2$ curves *without* a spherical parametrization, then resolve each by
effective Chabauty/Mordell–Weil sieve. This is closest to "tractable now"
(Chabauty is mature), but **no such reduction is known** — and that missing
reduction is precisely the crux. It would be a genuinely new idea, not a
refinement of an existing one. A second hurdle: even granted finitely many
curves, Chabauty needs $\operatorname{rank} J < \operatorname{genus}$, which is
not guaranteed for the curves that would arise.

## Directions that sound promising but recapitulate a known wall (ruled out)

- **abc conjecture** — gives only Darmon–Granville-strength finiteness
  [[method-abc-finiteness]]; no "finitely many → zero" upgrade. Not a path.
- **A cleverer descent** — descent needs the cyclotomic factorization of
  $x^p+y^q$, which does not exist for $p\neq q$ [[method-infinite-descent]].
  No algebraic factorization → no descent, regardless of cleverness.
- **Density / metric / approximation arguments** — refuted empirically by
  "tight-by-1" (attempt-01): coprime triples can land exactly 1 below a
  $\geq3$-power, so no gap-based argument can exclude solutions.
- **Just compute the finite Faltings set** — Faltings is *ineffective* in
  general; effective bounds exist but only reduce to finite curves, which is
  exactly the missing reduction above. Not a shortcut.

## Honest verdict

No actionable proof of $(3,5,7)$ — or of any distinct-prime signature — is in
sight. The cycle's value is the sharpened, unified statement of *why*:
the obstruction is uniformly at the **reduction** step, and the only two
candidate directions ((A) modular-program extension, (B) non-spherical
geometric reduction) are each a major open project with a clearly named
missing piece. This converts "Beal is hard" from a vague impression into a
precise, falsifiable machinery target — and rules out four tempting dead ends
by name. A future session extending this does not re-ask "is there a proof";
it asks "is there a non-spherical reduction to finite curves" or "is
Conjecture 1.2 provable for these specific representations."

## Next cycles

- **Strengthen the degenerate-near-miss claim** computationally: confirm the
  universal families $t^{21}+1$, $t^{35}+1$ account for *all* small $(3,5,7)$
  gap-1 near-misses (attempt-04 found them degenerate; verify exhaustiveness).
- A **second Lint** near the loop's end.
- Possibly: examine whether direction (B)'s "non-spherical reduction" has any
  nascent literature (a targeted ingest) — honest: likely little exists, but
  worth one check before declaring the direction empty.