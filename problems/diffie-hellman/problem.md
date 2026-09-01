# Diffie–Hellman Problem

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/DiffieHellman.htm.
> Computational-complexity problem; a full attack routes through [[PvsNP]].

## Statement
The **Computational Diffie–Hellman (CDH)** problem in a cyclic group
$\langle g\rangle$: given $g^a$ and $g^b$, compute $g^{ab}$. (The
**Decisional** variant DDH: distinguish $g^{ab}$ from a random group
element.) Is CDH hard in polynomial time (classical)?

## Status
**OPEN.** CDH is no harder than the discrete logarithm problem (DLP solves
CDH: recover $a$ from $g^a$, output $(g^b)^a$); the **converse** (DLP ⟸ CDH)
is open in general. DDH is hard in some groups, easy in others.

## Frontier (one line)
In generic groups CDH ≈ DLP ($\Omega(\sqrt q)$, Shoup 1997); in concrete
groups, a CDH lower bound independent of DLP is open — DDH is believed hard
in "gap" groups but unproven `[to-verify]`.

## Control-step framing (one line)
A subface of [[PvsNP]]'s `[witness-needs-explicit-lb]`: CDH ⟸ DLP is a
one-directional reduction (the DLP "engine" covers CDH); proving the
*independent* hardness of CDH (or DDH) is a separate non-compositional
lower-bound construction — the "two one-directional engines" pattern
echoing [[birch_swinnerton_dyer]]'s cyclotomic/anticyclotonic disjointness.

## See also
- [[PvsNP]] — parent complexity problem.
- [[discrete_logarithm]] — DLP ⟹ CDH; the reverse is the open composition.