# Conway's Thrackle Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: TOPP Problem 30; Wikipedia, *Thrackle*.
> Prize: US$1,000 (Conway).

## Statement
A **thrackle** is a drawing of a graph in the plane such that every pair of
edges meets exactly once — either at a shared endpoint or at a proper
crossing (no edge crossings at vertices, no two edges meeting twice).
Conway's Thrackle Conjecture (late 1960s): for any thrackle on $n$ vertices,
the number of edges $m\le n$.

## Status
**OPEN.** Conway offered **US$1,000** for a resolution; unclaimed. Verified
by computer up to $n=11$ (Cairns & Nikolayevsky) `[to-verify]`.

## Frontier (one line — a two-sided bound squeeze)
- **Lower bound:** $m=n$ is *attained* (any odd cycle of length $\ge5$ draws
  as a thrackle), so the "Conway thrackle constant" $C_{78}\ge1$.
- **Upper bound:** $m\le1.393(n-1)$ (**Yian Xu 2021**, Appl. Math. Comput.,
  DOI 10.1016/j.amc.2020.125573), confirmed by Keszegh–Suk–Tardos–Zeng
  (2025, arXiv:2512.04795) `[to-verify]`. Decades of improvement: $2n-3$
  (Lovász–Pach–Szegedy 1997) → $\tfrac32(n-1)$ (Cairns–Nikolayevsky 2000)
  → $1.428n$ (Fulek–Pach 2011) → $1.3984n$ (Fulek–Pach 2019) → $1.393(n-1)$.
- **Solved special cases:** geometric/straight-line thrackles (Erdős; short
  proof by Perles), outerplanar, $x$-monotone (Pach–Sterling 2011).
- **Structural localization:** if false, a minimal counterexample consists
  of **two even cycles sharing a vertex** (the engine stops at this family).
  Fulek–Pach note their discharging method alone cannot push below
  $\approx1.375n$ without *new* forbidden configurations — a precise
  statement of where the current engine stops `[summary]`.
*(2026-08-31 scan: the frontier line verified current — 1.393 remains the
record, confirmed still cited as best by the 2025 KSTZ preprint; the
earlier `[to-verify]` is resolved. The "computer up to n=11 / Cairns–
Nikolayevsky" attribution is retained as to-verify.)*

## Control-step framing (one line)
The cleanest **two-sided-bound squeeze** control case (twin to
[[chromatic_number_of_the_plane]], $5\le\chi\le7$): the lower bound
$C_{78}\ge1$ (constructive — odd cycles attain equality) and the upper bound
$C_{78}\le1.393$ (Xu 2021) are both partial; the open content is **squeezing**
$1.393\to1$ to the exact value. The structural fact (a counterexample is two
even cycles sharing a vertex) localizes the wall — a "one-dimensional engine
stops" on a specific graph family.

## See also
- [[chromatic_number_of_the_plane]] — the two-sided-bound squeeze twin
  (Hadwiger–Nelson $5\le\chi\le7$); both combinatorial-geometry problems with
  partial lower+upper bounds and an open exact value.
- [[perfect_cuboid]], [[rational_distance]] — sibling Erdős-style geometric
  extremal / existence problems.