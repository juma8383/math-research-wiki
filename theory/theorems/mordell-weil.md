---
type: theorem
name: Mordell-Weil theorem
created: 2026-08-24
tags: [number-theory, elliptic-curves, diophantine-geometry]
used-in: [[birch_swinnerton_dyer]]
provenance: []
---

# Mordell-Weil theorem

For an elliptic curve $E$ over a number field $K$, the group of rational
points $E(K)$ is a **finitely generated abelian group**:
$$E(K)\cong E(K)_{\text{tors}}\oplus\mathbb Z^{r},$$
with finite torsion and finite rank $r$ (the **Mordell-Weil rank**).

## Why it matters for BSD

The Mordell-Weil rank $r=r_{\text{alg}}$ is the algebraic side of BSD
[[def-elliptic-curve-L-function]]. The theorem guarantees $r$ is finite — so
"algebraic rank" is well-defined — but gives **no effective bound** on $r$ in
general. The **descent** step (computing a Selmer group) bounds $r$ above for a
given curve; finding independent points bounds it below. BSD asserts the
result equals the analytic rank.

## The finite-generation mechanism

Proved via descent: for any $n\ge2$, the weak Mordell-Weil theorem gives
$E(K)/nE(K)$ finite (via the $n$-Selmer group); the canonical height pairing
then forces $E(K)/\text{tors}$ to be a lattice, hence free of finite rank. This
descent / Selmer machinery is the **resolution** layer that works in all ranks
— the gap is elsewhere, in *control of the Selmer group's size*; see
[[method-heegner-point-euler-system]].