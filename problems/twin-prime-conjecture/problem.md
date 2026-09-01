# Twin Prime Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/TwinPrimes.htm.

## Statement
There are infinitely many primes $p$ with $p+2$ prime.

## Status
**OPEN.**

## Frontier (one line)
Bounded gaps: Zhang (2013) proved some bounded prime gap occurs infinitely
often (initially $7\times10^7$); the Polymath8b/Maynard–Tao refinement gives
infinitely many prime pairs with gap $\le 246$ unconditionally ($\le 6$ under
full Elliott–Halberstam, $\le 12$ under GEH) — the 246 record is **current
as of 2025** (verified by the 2026-08-31 scan; no improvement since), and
the whole Polymath8b/Maynard argument has been **machine-verified in Lean 4**
(2025, `primegaps.axiommath.ai`, with Ono). The *exact-gap-2* infinitude is
open.

## Control-step framing (one line)
Resolution on a slice ("*some* bounded gap infinitely often" — a relaxed
regime) → control = gap **exactly 2** infinitely often; the engine runs at
gap $\le246$, stops at gap $2$ — a "one-dimensional engine stops" instance.
Sharper (2026-08-31 scan): the stop is **two-layered** — at distribution
level $\theta=\tfrac12$ the Maynard sieve is numerically *exhausted* at 246,
and even the strongest available control upgrade (full Elliott–Halberstam)
yields only 6, **not 2** — the control wall survives the strongest available
control upgrade.

## See also
- [[riemann_hypothesis]] — sieve/distribution-of-primes control (GUE, pair
  correlation) underlies the gap analysis.
- [[legendre_conjecture]] — sibling prime-distribution problem.