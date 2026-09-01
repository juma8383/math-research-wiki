# Goldbach's Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/Goldbach.htm.

## Statement
**Strong (binary) Goldbach:** every even integer $>2$ is the sum of two
primes. **Weak (ternary):** every odd integer $>5$ is the sum of three
primes.

## Status
Weak/ternary **PROVEN** (Helfgott 2013, Annals). Strong/binary **OPEN**.

## Frontier (one line)
Strong Goldbach verified for all evens up to $4\times10^{18}$
(Oliveira e Silva–Herzog–Pardi 2014; the project page confirms no attempt
past it) — record still current as of 2026. **The exceptional-set ladder**
(the precise measure of the control wall, filed by the 2026-08-31 hunt scan;
all `[summary]`, primary sources to-verify): # of *unproved* evens $\le X$:
Montgomery–Vaughan 1975 $E(X)\ll X^{1-\delta}$ → Li 2010 $X^{0.879}$ →
Pintz 2018 $X^{0.72}$ → **Zhao Nov 2025 $E(X)\ll X^{0.7}$** (arXiv:2511.05631,
Linnik constant 5 — proved by the same zero-packet/Linnik machinery family as
Grimm's $g(n)$ bounds). Under GRH: $E(X)\ll X^{1/2+\varepsilon}$. The stub's
earlier generic "almost all" line is superseded by this ladder.

## Control-step framing (one line)
Resolution on a slice (verified to $4\times10^{18}$, plus average / "almost
all even" results) → control = *every* even — the canonical
density→pointwise control wall, twin to [[riemann_hypothesis]] and
[[collatz_conjecture]].

## See also
- [[riemann_hypothesis]] — GRH/prime-distribution control feeds the circle-
  method minor arcs; RH-type control is the obstruction to pushing "almost
  all" to "all."
- [[collatz_conjecture]] — same average→pointwise gap.