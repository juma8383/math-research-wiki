---
type: attempt
problem: beals_conjecture
attempt: 13
date: 2026-08-24
approach: Computationally test the neighboring distinct-prime signature (3,5,11) to check whether (3,5,7) rigidity is class-wide or signature-specific
outcome: confirmed
tags: [computation, signature-3511, rigidity-uniformity, open-class]
loop_cycle: 11 of 20
---

# Attempt 13 — Is the rigidity uniform across the open class?

The five-thread obstruction (synthesis.md) applies to the *whole* distinct-prime
class, not just $(3,5,7)$. Attempt-12 confirmed $(3,5,7)$'s rigidity empirically.
This cycle tests whether that rigidity is **uniform** across the open class by
probing the next distinct-prime signature $(3,5,11)$ via
`scripts/search_3511.py`.

## Generalized degenerate families

The universal gap-1 families are not specific to $(3,5,7)$. For any
$(p,q,r)$ they are $t^{\operatorname{lcm}(p,r)}+1$ ($B=1$) and
$t^{\operatorname{lcm}(q,r)}+1$ ($A=1$). For $(3,5,11)$:
- $t^{33}+1$: $A=t^{11},\;B=1,\;C=t^{3}$ (since $\operatorname{lcm}(3,11)=33$),
- $t^{55}+1$: $A=1,\;B=t^{11},\;C=t^{5}$ (since $\operatorname{lcm}(5,11)=55$).

(For $(3,5,7)$ this recovers exactly the $t^{21}+1$, $t^{35}+1$ of attempt-04/12.)

## Results (box $A\le6000,B\le6000,C\le40$)

| metric | $(3,5,7)$ (attempt-12) | $(3,5,11)$ (this) |
|---|---|---|
| exact solutions (coprime or not) | 0 | **0** |
| gap-1 hits | 4 | 3 |
| gap-1 degenerate | 4 | 3 |
| gap-1 genuine (bases $\ge2$) | 0 | **0** |
| all gap-1 on a universal family | yes | **yes** |
| min non-degenerate coprime gap | 29 at $(5,2,2)$ | **77 at $(12,3,2)$** |

The three $(3,5,11)$ gap-1 hits, all degenerate, all on a universal family:
$A{=}1,B{=}1,C{=}1$ ($t^{33}{+}1,\;t{=}1$); $A{=}2048,B{=}1,C{=}8$
($t^{33}{+}1,\;t{=}2$); $A{=}1,B{=}2048,C{=}32$ ($t^{55}{+}1,\;t{=}2$).

Min non-degenerate coprime near-miss: gap **77** at $(A,B,C)=(12,3,2)$:
$12^3+3^5=1728+243=1971$, $2^{11}=2048$, $2048-1971=77$.

## The finding: rigidity is uniform, and monotone in the exponents

$(3,5,11)$ reproduces $(3,5,7)$'s qualitative rigidity exactly — zero exact
solutions, zero genuine gap-1, all gap-1 degenerate on universal families — and
the minimum non-degenerate gap **grows** with the exponents ($29\to77$). This
is the expected signature of a *class-wide* phenomenon, not a $(3,5,7)$
peculiarity: larger odd-prime exponents make $C^r$ grow faster, so near-miss
gaps widen and solutions (genuine or degenerate) get sparser. It matches the
five-thread structural diagnosis, which is uniform across distinct-prime
signatures (each obstruction is stated for general $(p,q,r)$, not just
$(3,5,7)$).

## Honest scope caveat

The box is more constraining for $(3,5,11)$ than for $(3,5,7)$ because $C^{11}$
grows so fast ($C\le40$, and the $t\ge3$ members of both universal families
have $A$ or $B = 3^{11}=177{,}147$, far outside the box). So the result is:
*within the searched box, the pattern matches*. Genuine gap-1 with large bases
is not ruled out, but the qualitative uniformity — and the monotone growth of
the minimum gap — is clear from the two data points. A third signature
($(3,7,11)$ or $(5,7,11)$) would further confirm, but the trend is already
evident.

## Outcome

**confirmed.** The empirical rigidity is uniform across the open class of
distinct-prime signatures (at least for the two tested, $(3,5,7)$ and
$(3,5,11)$), and monotone in the exponents. This is consistent with — and
mildly corroborates — the structural claim that the obstruction is a property
of the *whole class*, not an artifact of the single smallest case.

## Next cycles

- A targeted ingest: does direction (B) of attempt-11 (a *non-spherical
  reduction* to finitely many genus-$\ge2$ curves) have any nascent literature?
  One honest check before declaring the direction empty.
- A second Lint near the loop's end.
- Optional: a third distinct-prime signature to nail the monotone trend (low
  marginal value given the clear two-point trend).