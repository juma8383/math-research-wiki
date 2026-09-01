# Chromatic Number of the Plane (Hadwiger–Nelson)

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/ChromaticNumber.htm.

## Statement
The chromatic number $\chi(\mathbb R^2)$ of the plane = the fewest colors
needed to color $\mathbb R^2$ so that no two points at distance $1$ share a
color (the unit-distance graph on $\mathbb R^2$).

## Status
**OPEN** (exact value). Bounds $5\le\chi(\mathbb R^2)\le7$; the exact value is
$\in\{5,6,7\}$.

## Frontier (one line)
**Lower bound:** $\chi\ge5$ (Aubrey de Grey 2018 — a 1581-vertex unit-distance
graph requiring 5 colors). Smallest known 5-chromatic unit-distance graph:
**509 vertices (Parts 2020**, Geombinatorics 29(4):137–166, 2442 edges — the
Heule chain reached 517/529→525→510→**509**; the earlier "~510 by
Exoo–Ismailescu" was imprecise) `[summary]`. No 6-chromatic unit-distance
graph is known. Recent variant: Haugland 2026, 5-chromatic Moser-spindle-*free*
graph on 2131 vertices `[summary]`. **Upper bound:** $\chi\le7$ (hexagonal
tiling, 1969). The 5–7 gap is open. Measurable variant $5\le\chi_m\le7$
also open.

## Control-step framing (one line)
The cleanest two-sided-bound control case in the wiki: the **lower bound**
(constructive — exhibit a unit-distance graph needing $k$ colors = resolution
on a finite slice) and the **upper bound** (a coloring/tiling = control) are
both partially discharged; the open content is **squeezing** 5↔7 to the exact
value, i.e. a higher-chromatic graph (→6 or →7) or a better coloring (→6 or
→5). This is the control step as a two-sided squeeze — a sharper form of the
slice→full wall.

## See also
- [[lonely_runner_conjecture]] — view-obstruction / covering-systems
  machinery shared.