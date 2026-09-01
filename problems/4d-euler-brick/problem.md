# 4D Euler Brick

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/4DEulerBrick.htm.

## Statement
A 4-dimensional analogue of the Euler brick: a 4D box with integer edges
$a,b,c,d$ and integer 2D face diagonals (all six) — the 3D and 4D body
diagonal variants are further strengthenings. *(The 2026-08-31 hunt scan
resolved the earlier `[to-verify: which diagonals]` against Boyer's Euler-
brick catalog: even the face-diagonals-only 4D Euler brick is OPEN — brute
force to $d=10^6$ found nothing — so the earlier stub line "variants with
integer face diagonals are constructible" was WRONG; corrected.)*

## Status
**OPEN** — already at the face-diagonals-only level.

## Frontier (one line)
No 4D Euler brick with all six 2D face diagonals integral is known (search to
$d=10^6$ empty `[summary]`, Boyer's catalog); the near-miss record is
$(693,140,480,2376)$ — all integer 4D body diagonals, 7 of 8 conditions
satisfied — with the family $(ab,ac,bc,a^2)$ from any 3D Euler brick
satisfying 5/6 face conditions + the 4D diagonal. Necessary conditions known
(one odd edge + three even; divisibility chains incl. $4\cdot16\cdot64$,
$27$, $9$, $3$, $5$, $11$, $13$, $19$) — candidate micro-theorem materials
(filed under verification).

## Control-step framing (one line)
Resolution on a slice (some diagonals integral) → control = all diagonals
simultaneously — a higher-dimensional simultaneous-Diophantine control step,
the 4D face of the [[perfect_cuboid]] wall.

## See also
- [[perfect_cuboid]] — the 3D parent problem; same control step, one
  dimension up.