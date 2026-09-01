---
type: attempt
problem: beals_conjecture
attempt: 05
date: 2026-08-24
approach: Develop the Mordell-curve/elliptic side angle for the cubic case; verify the birational map; determine its scope
outcome: partial
tags: [elliptic-curves, mordell-curves, integral-points, genus, verified]
loop_cycle: 3 of 20
---

# Attempt 05 — Mordell-curve lens on the cubic-cubic gap-1 phenomenon

The non-modular thread flagged in attempts 01/04. Goal: turn the Ramanujan
gap-1 near-misses ($9^3+10^3=12^3+1$) into a genuine elliptic-curve statement,
verify it, and determine whether the angle reaches beyond the cubic case.

## Verified equivalence

Computationally verified (`scripts/mordell_check.py`): the curve
$x^3+y^3=N$ is birationally equivalent to the Mordell curve

$$E_N:\ Y^2 = X^3 - 432\,N^2,\qquad X=\tfrac{12N}{x+y},\ Y=\tfrac{36N(x-y)}{x+y}.$$

Checks (all exact, via `fractions.Fraction`):
- $9^3+10^3=1729=12^3+1$: $(x,y)=(9,10)$ → $(X,Y)=(1092,-3276)$ on
  $Y^2=X^3-432\cdot1729^2$. ✓
- trivial $1^3+12^3=1729$ → $(1596,-52668)$ on same curve. ✓
- $6^3+8^3=728=9^3-1$ → $(624,-3744)$ on $Y^2=X^3-432\cdot728^2$. ✓

Filed as [[method-mordell-curve-lens]].

## Reframing the gap-1 vs gap-0 distinction

- **Gap 0** ($x^3+y^3=z^3$, FLT $n=3$): $N=z^3$, Mordell curve $E_{z^3}: Y^2=X^3-432z^6$.
  Euler's FLT $n=3$ ⟺ this family has **no non-trivial** integral points.
- **Gap 1** ($x^3+y^3=z^3\pm1$): $N=z^3\pm1$, Mordell curve $E_{z^3\pm1}$. This
  family **does** have non-trivial integral points for some $z$ (Ramanujan
  $z=12$→1729, $z=9$→728).

So "why gap 1 never 0" = "why does $E_{z^3}$ have no non-trivial integral points
while $E_{z^3\pm1}$ sometimes does?" — an integral-points-on-a-Mordell-family
question. Siegel's theorem gives finiteness per $N$, not a uniform zero.

## The decisive finding: the lens is cubic-only

Genus of the smooth projective model of $x^a+y^b=N$ is
$g=\frac{(a-1)(b-1)-(\gcd(a,b)-1)}{2}$:
- $(3,3)\to g=1$ (elliptic — the lens applies);
- $(3,5)\to g=4$, $(4,4)\to g=9$, $(5,5)\to g=21$ — **higher genus**.

**The Mordell/elliptic lens exists only for the cubic-cubic signature.** For
every other Beal signature — crucially including the frontier $(3,5,7)$, whose
$x^3+y^5=N$ has genus $4$ — the "sum of two powers" curve is genus $\geq 2$,
where only Faltings (finiteness, ineffective; effective only at rank-0 Jacobian
[[rg2024-faltings-algorithm]]) is available, and there is no explicit
integral-point theory. This *explains* attempt-04's empirical observation that
$(3,5,7)$ near-misses are degenerate: there is no elliptic structure to generate
genuine non-degenerate near-misses there.

## Honest outcome

**partial.** The angle is real and now verified, and it gives a clean
conceptual account of the cubic gap-1 phenomenon — but it is (a) essentially a
reformulation of Euler's FLT $n=3$ for the gap-0 case, and (b) **cubic-specific**:
it dies at genus $\geq 2$ and does not reach the Beal frontier $(3,5,7)$. Its
value is explanatory, not a route to a proof of general Beal. It does confirm a
structural theme: the cubic case is special (genus 1, rich near-miss arithmetic,
classical descent works); everything beyond is higher-genus and currently
inaccessible to either descent or the modular method.

## Next cycle

The "descent" thread: pin down *why* classical infinite descent (Euler $n=3$,
Fermat $n=4$) cannot be run for mixed/odd-prime exponents — the symmetry it
exploits. This complements the Mordell lens (descent is the cubic/ quartic
engine that the lens reframes) and clarifies what a non-modular proof would need
to replace.