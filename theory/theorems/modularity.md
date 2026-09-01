---
type: theorem
name: Modularity theorem (Taylor-Wiles, BCDT)
created: 2026-08-24
tags: [number-theory, elliptic-curves, modular-forms]
used-in: [[birch_swinnerton_dyer]]
provenance: []
---

# Modularity theorem

Every elliptic curve $E/\mathbb Q$ is **modular**: there is a weight-2 newform
$f$ of level $N$ (the conductor) with $a_p(f)=a_p(E)$ for all $p$, hence
$L(E,s)=L(f,s)$.

- **Wiles 1995** (with Taylor): semistable curves (proved FLT as a corollary).
- **Breuil-Conrad-Diamond-Taylor 2001**: all $E/\mathbb Q$.

## Role in BSD

Modularity is what makes $L(E,s)$ an **entire** function with a functional
equation (center $s=1$), so the analytic rank
$r_{\text{an}}=\operatorname{ord}_{s=1}L(E,s)$ is even defined
[[def-elliptic-curve-L-function]]. Without modularity, the BSD *statement* has
no analytic side. It is therefore a **prerequisite**, not a tool that resolves
BSD: it supplies the L-function, but not its special value.