---
type: attempt
problem: birch_swinnerton_dyer
attempt: 1
date: 2026-08-24
approach: First attack — establish the BSD statement, locate the exact frontier (rank <=1 known, rank >=2 + refined open), name the open content, map the obstruction
outcome: partial
tags: [frontier, obstruction-map, heegner-points, euler-systems, parity, cross-problem]
---

# Attempt 01 — Establish the frontier and obstruction for BSD

First cycle on BSD. Mirrors Beal attempts 01–02: get the clean form, locate the
exact frontier, name the open content, and map where the obstruction sits.

## Statement established [[def-elliptic-curve-L-function]]

BSD for $E/\mathbb Q$: (rank) $r_{\text{alg}}=r_{\text{an}}$; (refined) the
leading Taylor coefficient at $s=1$ equals
$\Omega_E R_E |\text{Sha}|\prod c_p / |E(\mathbb Q)_{\text{tors}}|^2$. Two
distinct open pieces (rank part; refined/leading-coefficient part).

## The exact frontier

| piece | $r_{\text{an}}\le1$ | $r_{\text{an}}\ge2$ |
|---|---|---|
| rank equality | **proven** (Kolyvagin-Gross-Zagier [[thm-kolyvagin-gross-zagier]]) | **open** |
| Sha finiteness | **proven** | **open** |
| leading coeff. (exact $\|\text{Sha}\|$) | open in general (comp. verified) | open |

Parity [[thm-parity]] holds in all ranks ($p$-parity unconditionally).

## Open content (analog of Beal's "finitely many → zero")

- Rank part: **"analytic rank ≤ 1 → arbitrary rank."**
- Refined part: **"Sha finite → exact order of Sha."**

## The obstruction: control step, not resolution step

The *resolution* layer works in all ranks and finished the verified cases:
descent/Selmer (upper bounds, [[thm-mordell-weil]]), Tamagawa/regulator/period/
Sha computation, Heegner points. The gap is the **Selmer-group *control***
mechanism: Kolyvagin's Euler system is **one-point-shaped** — it bounds a
Selmer group of rank $\le1$, not $\ge2$ [[method-heegner-point-euler-system]].
For rank $\ge2$ one needs $r_{\text{an}}$ independent points (a
higher-derivative Gross-Zagier) AND an Euler system bounding the full Selmer
group to size $r_{\text{an}}$; neither is known in general. Kolyvagin's own
higher-rank conjectures [bsd-kolyvagin-conj] are the named unproven target.

Parity [[thm-parity]] is the one general rank-$\ge2$ tool, but it only pins
rank mod 2 *given* an upper bound — it cannot itself bound the Selmer group
from above.

## Cross-problem compounding [[beals_conjecture]]

The diagnostic lens developed on Beal transfers directly:
- **Beal** obstruction = the *reduction-to-finite-curves* step (resolution
  tools work; no reduction mechanism without shared/even/spherical structure).
- **BSD** obstruction = the *Selmer-group-control* step (resolution tools work;
  no Euler system of rank-$\ge2$ shape).

Both are "obstruction at the control/reduction step, not the resolution step."
This methodology is reusable; recorded in `notes.md` as a candidate
methodology page. `related` link added both ways across the two problems.

## Forward directions

- **(A)** Higher-rank Euler systems: higher Heegner points, Beilinson-Flach,
  Kato derivatives, Kolyvagin Conjectures 3.32–3.35 [bsd-kolyvagin-conj].
- **(B)** Iwasawa/$p$-adic: main conjecture (Kato, Skinner-Urban) +
  Skinner's converse [bsd-skinner-converse] → $p$-parts / converse.
- **(C)** Refined/Mazur-Tate: ETNC, Bullach-Honnor 2025 → leading coefficient.

## Theory toolbox filed this cycle

`def-elliptic-curve-L-function`, `thm-mordell-weil`, `thm-modularity`,
`thm-kolyvagin-gross-zagier`, `method-heegner-point-euler-system`,
`thm-parity`; source `bsd-survey` (search-compiled, flagged [summary] /
to-verify).

## Honesty / to-verify

Status facts ingested from web-search summaries, **not primary sources**;
flagged in `bsd-survey` and `progress.md`: the rank-1 unconditional scope,
algebraic-rank parity's Sha caveat, refined-BSD-open-at-rank-0, and
Skinner-converse hypotheses. These are the first items to verify against the
papers — the Beal PSS verification caught a real factual error this way, so
verification is not a formality.

## Next

Verify the load-bearing status facts against primary sources (Stein's book;
Dokchitser-Dokchitser; Skinner), then deepen direction (A): what concretely
blocks a higher-rank Euler system from bounding a rank-$\ge2$ Selmer group?