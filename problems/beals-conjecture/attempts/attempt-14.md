---
type: attempt
problem: beals_conjecture
attempt: 14
date: 2026-08-24
approach: Targeted literature check on direction (B) — does a non-spherical reduction to finitely many genus>=2 curves exist for distinct-prime signatures
outcome: partial
tags: [literature-check, nonabelian-descent, triangle-groups, spherical-hyperbolic, correction]
loop_cycle: 12 of 20
---

> **CORRECTION (attempt-17, cycle 15):** the table below labels $(2,3,7)$ as
> "spherical" with $41/42>1$. That is a **factual error**: $41/42<1$, so
> $(2,3,7)$ is **hyperbolic** (infinite triangle group). PSS works via a
> **finite quotient** $\mathrm{PSL}_2(\mathbb F_7)$ of the *infinite*
> $\Delta(2,3,7)$ (the Klein quartic), enabled by the near-spherical position
> ($\chi=-1/42$) **and the exponent $2$** (the $X(7)$ modular interpretation).
> The structural conclusion — PSS does not transfer to $(3,5,7)$ — is
> unchanged, but the reason is "deep hyperbolicity + no exponent 2," not
> "spherical vs hyperbolic." The corrected table and framing live in
> [[method-triangle-group-descent]] and synthesis.md. The text below is kept
> unchanged as the append-only record.

# Attempt 14 — Direction (B) literature check (and a correction to attempt-11)

Attempt-11 named "a non-spherical reduction of $(3,5,7)$ to finitely many
genus-$\ge2$ curves" as the crux of the geometric direction (B) and stated "no
such reduction is known." This cycle checks the literature and finds that
statement was **too strong** — and that the geometric route is *less*
independent of thread 5 than framed.

## Correction: the reduction already exists — but is ineffective

Darmon–Granville [[thm-darmon-granville]] is not merely a finiteness assertion:
its *proof* is a reduction to finitely many curves. Via unramified coverings of
$\mathbb P^1\setminus\{0,1,\infty\}$ of signature $(p,q,r)$ plus the
Chevalley–Weil theorem, infinitely many primitive solutions would yield
infinitely many rational points on a genus-$>1$ curve over a number field,
contradicting Faltings. So a "reduce to finitely many curves" mechanism
**exists in general**. The catch: Faltings is **ineffective** — it proves the
finite set exists but neither enumerates it nor shows it is empty. The honest
gap is therefore not "no reduction is known" but "**no effective reduction is
known** for all-distinct-odd-prime signatures." (Attempt-11 corrected.)

## The one effective precedent: Poonen–Schaefer–Stoll (2,3,7)

PSS 2007 [[pss2007]] made the reduction effective for $x^2+y^3=z^7$, listing all
16 primitive solutions. The engine: **nonabelian descent via the finite group
$\mathrm{PSL}_2(\mathbb F_7)$** (order 168), reducing to **10 twists of the
Klein quartic** (genus 3), then Chabauty–Coleman (where
$\operatorname{rank}J<\operatorname{genus}$) plus a Mordell–Weil sieve +
modularity/level-lowering for the hard $\operatorname{rank}=\operatorname{genus}$
case. Filed [[method-triangle-group-descent]] and a source page [[pss2007]].

## The structural reason it stops there: spherical vs hyperbolic triangle groups

$\mathrm{PSL}_2(\mathbb F_7)$ is the finite quotient of the **triangle group**
$\Delta(p,q,r)$, which is **finite iff $1/p+1/q+1/r>1$** (spherical):

| signature | invariant | type | triangle group | nonabelian descent |
|---|---|---|---|---|
| $(2,3,7)$ | $>1$ | spherical | finite ($\mathrm{PSL}_2(\mathbb F_7)$) | ✓ (PSS) |
| $(3,5,7)$ | $<1$ | **hyperbolic** | **infinite** | **✗ no finite descent group** |

For $(3,5,7)$ the triangle group is infinite → there is **no finite quotient**
to play the role of $\mathrm{PSL}_2(\mathbb F_7)$ → the nonabelian-descent step
that made (2,3,7) effective has no analogue. The ineffective
Darmon–Granville finiteness remains, but the effective PSS step is
unavailable.

## The key re-framing: direction (B) folds into thread 5

Attempt-11 treated the geometric direction (B) as an *independent* possible
escape from the spherical-reduction obstruction (thread 5). The triangle-group
lens shows they are **not independent**: the only known effective geometric
reduction (PSS (2,3,7)) relies on a **spherical** (finite) triangle group —
the *same* spherical/hyperbolic divide that bounds thread 5. For
all-distinct-odd-prime (hyperbolic) signatures, **both** the modular
effectiveness and the geometric effectiveness are blocked, and for a related
underlying reason: no finite group structure to exploit.

This is a *sharper* and more honest diagnosis, not a weaker one. The wiki now
records six angles (the five threads plus this triangle-group lens, which is
strictly a refinement of how threads 5 and B relate), all converging on the
hyperbolic / no-finite-structure obstruction at $(3,5,7)$.

## Updated two-direction picture

- **(A) Modular** — unchanged: extend Darmon's Frey-variety method to three
  distinct primes + prove generalized-Mazur irreducibility. Two programs away.
- **(B) Geometric** — *revised*: the reduction exists (Darmon–Granville) but is
  ineffective; making it effective needs a finite descent group, which requires
  a spherical signature; $(3,5,7)$ is hyperbolic, so the PSS technique is
  unavailable. To make (B) work for $(3,5,7)$ one would need an entirely new
  effective-finiteness mechanism that does *not* rely on a finite triangle
  group — a genuinely new idea, not a transplant of PSS.

## Honest outcome

**partial — a correction that sharpens the picture.** Attempt-11's "no
reduction known" was an overstatement; the correction (reduction exists but is
ineffective; effectiveness needs spherical structure) is more precise and
slightly more pessimistic, since it shows the geometric escape route is gated
on the same spherical divide as the rest. The convergent diagnosis is now
tighter: $(3,5,7)$'s hyperbolicity (no finite triangle group) blocks the
effective geometric route, just as it blocks the spherical-reduction route.

## Next cycles

- A second Lint (the wiki has grown again; new pages
  triangle-group-descent, pss2007, plus synthesis refinement — check linking).
- Optionally verify the PSS mechanism against the actual paper (flagged in the
  source page as extracted from a search summary).
- Begin consolidating toward a final "state of the attack" close-out as cycles
  run low.