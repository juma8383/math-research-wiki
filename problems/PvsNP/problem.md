# P vs NP

> Problem statement. For the running state of the attack, read
> [progress.md](progress.md) first. The detailed work lives in the
> self-contained nested wiki at [wiki/](wiki/) — its catalog is
> [wiki/index.md](wiki/index.md), its audit trail [wiki/log.md](wiki/log.md).

## Statement

Is $\mathrm P = \mathrm{NP}$? Equivalently: does every problem whose solution can
be *verified* in polynomial time also admit a polynomial-time *algorithm*?
The canonical complete problem is SAT. $\mathrm P\subseteq\mathrm{NP}$ is
trivial; the open question is the reverse containment.

A Millennium-grade problem (one of the seven Clay Millennium Prize
Problems, $1M prize), and the central question of theoretical computer
science. Unlike the other five Millennium problems in this wiki (BSD,
Navier–Stokes, Yang–Mills, Hodge — number theory / PDE / geometry), P vs NP
is a **complexity-theory** problem. It is the hardest known point in the
barrier landscape (relativization / natural proofs / algebrization).

## The exact frontier

No super-polynomial circuit lower bound is known for any "natural" class
above $\mathrm{ACC}^0$. The field's frontier sits at:

- **Williams (2011):** $\mathrm{NEXP}\not\subseteq\mathrm{ACC}^0$
  (algorithmic method — non-natural, non-relativizing).
- **Murray–Williams (2017):** $\mathrm{NTIME}[n^{\mathrm{polylog}\,n}]
  \not\subseteq \mathrm{P/poly}$.
- **Chen–Tal–Wang (2026):** an $f\in\mathrm E^{\mathrm{NP}}$ requiring
  $n^{2.5-\varepsilon}$-size $\mathrm{THR}\circ\mathrm{THR}$ (superquadratic
  gate barrier broken).

The gap to $\mathrm P\neq\mathrm{NP}$ is: $\mathrm{NP}\not\subseteq\mathrm{P/poly}$
(equivalently, NP-hardness of MCSP under uniform-$\mathrm{AC}^0$ many-one
reductions — Route A, the highest-upside bridge). No such reduction is
known. See [progress.md](progress.md) for the obstruction.

## See also

- [progress.md](progress.md) — read-first running state + the central
  obstruction + pointers into the nested wiki.
- [notes.md](notes.md) — methodology + the cross-problem 7-for-7 control-step
  link.
- [wiki/](wiki/) — the detailed work (28 cycles, 7 loops; own SCHEMA / index
  / log / pages / sources).