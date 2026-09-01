---
type: theorem
name: Nonexistence of small nontrivial Collatz cycles (Steiner, Simons, Simons–de Weger)
created: 2026-08-24
tags: [number-theory, transcendence, diophantine, collatz]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# No small nontrivial Collatz cycles

A nontrivial cycle of $m$ odd values $o_0,\dots,o_{m-1}$ satisfies the cycle
equation (total $L$ halvings over $m$ odd steps):
$$2^L=\prod_{i=0}^{m-1}\frac{3o_i+1}{o_i},\qquad
\Lambda=(K+L)\log2-K\log3\ \text{exponentially small},$$
where $K=\sum(\text{odd-step contributions})$. If such a cycle exists, the
linear form $\Lambda$ in logarithms must be *exponentially* small
[[method-cycle-exclusion-linear-forms]].

## Results (transcendence rules out small cycles)

- **Steiner (1977)**: no nontrivial **1-cycles** [collatz-cycle-steiner].
- **Simons (2004)**: no nontrivial **2-cycles**.
- **Simons–de Weger (2010)**: no nontrivial **$m$-cycles for $1\le m\le75$**;
  explicit upper/lower bounds on $K,L,x_{\min}$ for $m\ge76$
  [collatz-cycle-simons-deweger].
- **Hercher (2023)** [updated 2026-08-31, breakthrough-hunt session]: no
  nontrivial **$m$-cycles for $m\le91$** — J. Integer Sequences 26 (2023),
  Article 23.3.5, arXiv:2201.00406; seeds the ladder with $X_0=695\cdot2^{60}$
  (Barina-type verification), CF smallest-denominator lemma (Lemma 22),
  improving SdW's $m\le75/83$. Also: verifying convergence to
  $1536\cdot2^{60}$ would force $K>1.375\times10^{11}$ odd cycle members.
- **Wang (2026)** [flagged UNREVIEWED — Zenodo preprints
  10.5281/zenodo.20557259 / 20588490 / 20589910, June 2026]: claims
  **$m\le93$** via a reproducible "suffix-balanced block method" (exact
  rational interval arithmetic + CF-denominator certificates + SdW-type
  bounds), bypassing the CF-rung structure that stalls Hercher's program at
  $m=92$ (the 2026-08-31 "m=92 deadlock" analysis in
  problems/collatz-conjecture/notes.md). Full read `to-verify`; if it
  verifies, the exclusion frontier moves to $m\le93$.

Mechanism: lower bounds on linear forms in logarithms
(Laurent–Mignotte–Nesterenko, Rhin) force $\Lambda$ to be only
subexponentially small — contradicting the exponential smallness a cycle
requires, for bounded $m$. Continued-fraction approximations to $\log3/\log2$
and diophantine-approximation lattice methods.

## Role in the obstruction

This is the **cycle-exclusion resolution layer** — it works up to $m\le75$.
The gap (direction (B)) is pushing to **all $m$**: the transcendence bounds
that suffice for $m\le75$ degrade for large $m$, and no argument rules out
cycles of arbitrarily large period. This sub-problem is **Diophantine /
transcendence** in flavor — the Collatz echo of Beal's generalized-Fermat
character [[beals_conjecture]] [[method-cycle-exclusion-linear-forms]].
Computational verification ($x_{\min}>5.76\times10^{18}$, $N\le2^{68}$
[collatz-verified]) corroborates but does not replace the analytic exclusion.