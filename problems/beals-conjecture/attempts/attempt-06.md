---
type: attempt
problem: beals_conjecture
attempt: 06
date: 2026-08-24
approach: Pin down why classical infinite descent (FLT n=3,4) cannot run on mixed/distinct exponents
outcome: partial
tags: [descent, cyclotomic, UFD, structural-obstruction]
loop_cycle: 4 of 20
---

# Attempt 06 — Why descent dies for mixed exponents

The non-modular counterpart to the modular-method obstruction
[[method-frey-level-lowering-obstruction]]. Classical infinite descent closed
FLT for $n=3$ (Euler, Eisenstein integers) and $n=4$ (Fermat, Pythagorean
triples). Why does the same engine not touch $x^p+y^q=z^r$ with mixed/distinct
exponents? Filed [[method-infinite-descent]] with the full analysis.

## The three requirements of descent

Distilled from the two classical proofs:

1. **Matching algebraic factorization** — split the LHS into conjugate linear
   factors. Exists only when the two LHS terms share an exponent
   ($x^n+y^n=\prod(x+\zeta_n^k y)$; or the Pythagorean square structure for
   $n=4$).
2. **Factor-power = RHS-power** — the factorization makes each factor "want to
   be" a $p$-th power; descent closes only if the RHS is the *same* power ($z^p$).
3. **Cyclotomic UFD** — the factorization ring $\mathbb Z[\zeta_p]$ must be a UFD
   (true for $p=3$; fails for large $p$ — Kummer; first irregular prime $37$).

## Where each fails

| requirement | $(p,p,p)$ FLT | $(p,p,r)$, $r\neq p$ | $(p,q,r)$ distinct (e.g. $(3,5,7)$) |
|---|---|---|---|
| (1) matching factorization | ✓ | ✓ | **✗ — $x^p+y^q$ has no conjugate factorization** |
| (2) factor-power=RHS-power | ✓ | **✗** ($r\neq p$) | ✗ |
| (3) cyclotomic UFD | ✓ small $p$ | ✓ small $p$ | n/a |

## The key finding

**For $(3,5,7)$ descent fails at requirement (1): $x^3+y^5$ admits no cyclotomic
factorization, so no descent can even begin.** This is the descent-method
analogue of the Frey obstruction (no usable level-lowering prime) — both
ultimately stem from the same source: three *incommensurate* exponents give no
single prime-power structure to exploit.

For the intermediate $(p,p,r)$ case, descent fails at requirement (2): the
factors "want" to be $p$-th powers but the RHS is an $r$-th power. *This is
exactly why $(p,p,r)$ signatures required the modular method rather than
descent* — connecting this thread back to attempt-02/03.

## Synthesis with prior cycles

All three non-modular/modular threads now converge on the same structural fact:

- **Modular method** [[method-frey-level-lowering-obstruction]]: distinct
  exponents ⟹ no single level-lowering prime strips all bases ($\gcd(2p,2q,2r)=2$).
- **Darmon program** [[method-darmon-program]]: even the abelian-variety
  generalization is developed only for repeated exponents; distinct-prime case
  undeveloped.
- **Mordell lens** [[method-mordell-curve-lens]]: elliptic structure exists
  only at genus 1 = cubic-cubic; dies at $(3,5,7)$ (genus 4).
- **Descent** (this cycle): no cyclotomic factorization for $x^p+y^q$, $p\neq q$.

**Convergent conclusion:** the cubic-cubic-cubic case is the *unique* signature
where classical methods converge — genus 1 (Mordell), cyclotomic UFD
factorization (Euler descent), and self-power match (FLT). Every departure
(repeated but $\neq$ exponent; or distinct exponents) breaks at least one of
these, and the distinct-prime case $(3,5,7)$ breaks *all* of them. This is a
clean, multi-angle confirmation that $(3,5,7)$ is the genuinely hard kernel, not
just "the next one on the list."

## Honest outcome

**partial — but consolidating.** No proof, but the four threads now form a
coherent structural diagnosis: Beal's difficulty is not a single wall but the
simultaneous absence of every available classical tool at the distinct-prime
frontier. The to-verify item (exact UFD boundary of $\mathbb Z[\zeta_p]$) is
minor and noted.

## Next cycles (refining the frontier, not restarting)

- **Neighbors check:** confirm $(3,5,5)$, $(3,3,7)$, $(5,5,3)$ are resolved
  (repeated-exponent) — verifying $(3,5,7)$ is truly the *boundary* between
  solved and open.
- **Even-exponent factorization** that solved $(3,4,5)$ (Siksek–Stoll) — does
  any of it transfer toward $(3,5,7)$?
- **Synthesis page:** write a consolidated "state of the attack" capturing the
  convergent four-thread diagnosis, as a reference for future sessions.
- **Lint pass** soon — the wiki has grown to ~20 pages; check orphans/contradictions.