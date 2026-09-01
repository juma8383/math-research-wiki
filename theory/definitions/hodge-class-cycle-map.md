---
type: definition
name: Hodge classes, algebraic cycles, and the cycle class map
created: 2026-08-24
tags: [algebraic-geometry, hodge-theory, algebraic-cycles]
used-in: [[hodge_conjecture]]
provenance: [[hodge-survey]]
---

# Hodge classes, algebraic cycles, and the cycle class map

## Hodge decomposition

For a compact Kähler manifold $X$ of complex dimension $n$ (e.g. smooth
projective over $\mathbb C$), Hodge theory gives
$$H^k(X,\mathbb C)=\bigoplus_{p+q=k}H^{p,q}(X),\qquad
\overline{H^{p,q}}=H^{q,p}.$$

## Hodge classes [hodge-statement]

A **Hodge class** of codimension $p$ is a rational cohomology class of pure
type $(p,p)$:
$$\mathrm{Hdg}^p(X):=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)\subset H^{2p}(X,\mathbb C).$$
These are defined *analytically* (via Hodge theory / harmonic forms).

## Algebraic cycles and the cycle class map

An **algebraic cycle** of codimension $p$ is a formal $\mathbb Q$-combination
of closed algebraic subvarieties $Z\subset X$ of codimension $p$. The group is
$\mathrm{CH}^p(X)$ (Chow group, modulo rational equivalence). Each $Z$ has a
**cycle class** $\mathrm{cl}(Z)\in H^{2p}(X,\mathbb Z)$ of type $(p,p)$, giving
the cycle class map
$$\mathrm{cl}:\mathrm{CH}^p(X)\otimes\mathbb Q\longrightarrow\mathrm{Hdg}^p(X).$$
By Chow's theorem, on a projective variety algebraic cycles = closed analytic
subspaces, so $\mathrm{cl}(Z)$ is the same analytic/algebraic class.

## The Hodge Conjecture [hodge-clay-deligne]

$\mathrm{cl}\otimes\mathbb Q$ is **surjective** for every $p$ — every Hodge
class is a $\mathbb Q$-linear combination of algebraic-cycle classes. This is
the conjecture that the analytic objects (Hodge classes) are all algebraic
(cycles). The obstruction is controlling this analytic→algebraic conversion in
codimension $\ge2$ [[method-analytic-algebraic-bridge]]. Anchor of the
[[hodge_conjecture]] attack.