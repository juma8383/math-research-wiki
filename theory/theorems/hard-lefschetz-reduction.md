---
type: theorem
name: Hard Lefschetz and the known-degree reduction
created: 2026-08-24
tags: [algebraic-geometry, hodge-theory, lefschetz]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# Hard Lefschetz and the known-degree reduction

## Hard Lefschetz theorem

On a smooth projective $X$ of dimension $n$ with hyperplane (Kähler) class
$\omega\in H^2(X,\mathbb Q)$, cup product with powers of $\omega$ gives
isomorphisms
$$L^{n-k}:H^k(X,\mathbb Q)\xrightarrow{\sim}H^{2n-k}(X,\mathbb Q).$$

## Reduction of the Hodge conjecture [hodge-hard-lefschetz-reduction]

Since $L$ is the class of an algebraic divisor (hence algebraic), if a Hodge
class $\xi\in\mathrm{Hdg}^p(X)$ is $L^{n-2p}\eta$ for $\eta\in H^{2p}(X)$ of
type $(p,p)$... more cleanly: hard Lefschetz reduces HC in degree $2p$ to HC in
degree $2(n-p)$. Consequently the only degrees known unconditionally are
$$H^0,\ H^2,\ H^{2n-2},\ H^{2n}$$
i.e. codimensions $p\in\{0,1,n-1,n\}$ [hodge-known-degrees-0-2-2n]:
- $p=0$: $[X]$; $p=n$: $[\mathrm{pt}]$ — trivial.
- $p=1$: Lefschetz $(1,1)$ [[thm-lefschetz-1-1]].
- $p=n-1$: hard Lefschetz applied to $p=1$.

## Role in the obstruction

The genuinely **new** open content is the middle codimensions
$2\le p\le n-2$ (requiring $n\ge4$). The smallest open case is **codimension
2 on a 4-fold** — a $(2,2)$ Hodge class in $H^4$ not lying in the Lefschetz
slice generated from divisors. Deligne: "known when $\dim<4$; open in
dimension $\ge4$" [hodge-codim-2-open]. Hard Lefschetz is the reduction that
*isolates* the frontier: it shows the divisor engine plus Lefschetz handles
the boundary codimensions, and the obstruction is precisely the middle.