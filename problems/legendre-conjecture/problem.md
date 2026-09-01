# Legendre's Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/LegendreConjecture.htm.

## Statement
For every integer $n\ge1$ there is a prime $p$ with $n^2 < p < (n+1)^2$.

## Status
**OPEN.**

## Frontier (one line)
Best unconditional: a prime in $[x-x^{0.525},\,x]$ for large $x$ (Baker–
Harman–Pintz 2001, untouched 20+ years) — at $x=n^2$ that is interval length
$n^{1.05}$, far too long for the $2\sqrt x=2n$ gap: the gap is **not** the
$\sqrt{\cdot}$ exponent but the **log factor** — even RH gives only
$(x,x+O(\sqrt x\log x))$, one extra log over the $\approx2\sqrt x$ needed
(Cramér-style; the precise obstruction is the log, not the exponent).
Heuristic verification to $n\approx6.9\cdot10^9$ via prime-gap tables
`[summary]` (the Goldbach shared-gap tables). **Implication lattice**
(2026-08-31 scan): **Andrica** ($g_n<2\sqrt{p_n}+1$, verified to
$p_n<1.6\cdot10^{18}$) ⟹ Legendre; **Grimm ⟹ Legendre** (Erdős–Selfridge
route); Oppermann strictly stronger than Legendre.

## Control-step framing (one line)
Resolution on a slice (verified to large $n$; conditional on RH) → control =
every $n$ — density→pointwise control; the prime-in-short-interval estimate
is the control step, directly gated on [[riemann_hypothesis]]-quality control.

## See also
- [[riemann_hypothesis]] — RH is the load-bearing conditional; Legendre is a
  downstream "two-avatar" symptom (function-field analogue proven, number-
  field open).
- [[goldbach_conjecture]], [[twin_prime_conjecture]] — sibling prime-
  distribution problems.