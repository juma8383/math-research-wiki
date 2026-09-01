# Aaronson's $100,000 Quantum-Computing Prize

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. This is a physics + complexity open problem;
> its complexity avatar routes through [[PvsNP]].

## Statement (the prize, stated precisely)
**US$100,000** (at his discretion, smaller awards for "partial" results) to
anyone who demonstrates, convincingly, that **scalable quantum computing is
impossible in the physical world** — a fundamental physical reason scalable
QC fails, *and* the corresponding fast classical algorithm simulating the
quantum systems found in Nature. PREREQUEST CORRECTION `[summary, to-verify
against Aaronson's blog]`: per the 2026-08-31 scan, the $100,000
impossibility prize was offered in **2007 by an anonymous donor** with
**Aaronson and David Deutsch as judges** (the stub's "In 2012 Aaronson
offered..." misattributed the provenance); a smaller "plausible argument"
prize was effectively awarded to **Gil Kalai** (~2014, "The Quantum Computer
Puzzle"). 2025 status: still unclaimed; Aaronson has publicly floated raising
it to \$1M amid the Craig Wright dispute. The prize is **unclaimed** (2026).

So the underlying open problem is: **is scalable, fault-tolerant quantum
computation physically realizable?**

## Status
**OPEN.** No impossibility shown (prize unclaimed). No scalable fault-tolerant
quantum computer built either — the experimental state is *finite, noisy*
"quantum supremacy" demonstrations (Google Sycamore 2019, 53-qubit Random
Circuit Sampling; BosonSampling; and subsequent logical-qubit / surface-code
experiments), which are **conditional-hardness** results, not a scalable
fault-tolerant machine.

## Frontier (one line)
- **Supremacy (the slice):** quantum advantage demonstrated on finite/noisy
  systems; classical hardness is **conditional** on assumptions QUATH
  (Aaronson–Chen 2017) / XQUATH (Aaronson–Gunn 2020) — proving
  *unconditional* hardness would require resolving $P\ne\mathrm{PSPACE}$
  (open) `[to-verify]`.
- **Fault tolerance:** the threshold theorem says scalable QC is possible
  *if* error rates lie below a threshold — a **conditional** physical result;
  no machine has reached scalable fault-tolerant operation. The current
  finite-slice state moved post-stub: Google **Willow** (Dec 2024)
  below-threshold surface-code / logical-qubit scaling results are the
  strongest experimental footing to date `[summary]`.

## Control-step framing (one line)
Two-avatar structure, twin to [[birch_swinnerton_dyer]] / [[riemann_hypothesis]] —
**complexity avatar**: proving the quantum sampling tasks are
*unconditionally* classically hard is a lower-bound construction (would need
$P\ne\mathrm{PSPACE}$ — the [[PvsNP]] `[witness-needs-explicit-lb]` /
natural-proofs frontier); **physics avatar**: proving scalable QC is
impossible (to win the prize) would be a new physical theory (a [[yang_mills]]-
grade revolution in quantum mechanics). Resolution runs on the finite/noisy
supremacy slice; the control-to-scalable step is the wall on **both** faces.

## See also
- [[PvsNP]] — the complexity avatar: unconditional classical-hardness of RCS
  sampling needs a $P\ne\mathrm{PSPACE}$-type lower bound = the same
  non-compositional construction lock.
- [[yang_mills]] — the physics avatar: "is the physical theory complete /
  does scalable QC fail for a deep physical reason?" is a Millennium-grade
  physics question.
- [[birch_swinnerton_dyer]], [[riemann_hypothesis]] — the two-avatars
  (one tractable face, one open face) structural twin.