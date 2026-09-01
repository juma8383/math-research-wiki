# Perfect Cuboid Problem

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/PerfectCuboid.htm.

## Statement
Does there exist a rectangular cuboid with integer edges $a,b,c$, all three
integer face diagonals $\sqrt{a^2+b^2},\sqrt{a^2+c^2},\sqrt{b^2+c^2}$, **and**
an integer space diagonal $\sqrt{a^2+b^2+c^2}$?

## Status
**OPEN** (existence). An Euler brick (integer edges + face diagonals only) is
known (e.g. $(a,b,c)=(44,117,240)$); the space-diagonal condition is the
unsolved part.

## Frontier (one line)
No perfect cuboid found up to large bounds; no nonexistence proof. Weaker
relaxations (two integer diagonals) solved; the full four-condition system is
open.

## Control-step framing (one line)
Resolution on a slice (Euler bricks, i.e. dropping the space-diagonal
condition) → control = the fourth condition simultaneously — a simultaneous
Diophantine control / "one-dimensional engine stops" (each Pythagorean
condition is one engine; the four-way intersection is the non-compositional
control step, echoing [[birch_swinnerton_dyer]]'s two-summand composition).

## See also
- [[4d_euler_brick]], [[rational_distance]] — sibling Diophantine-geometry
  problems.