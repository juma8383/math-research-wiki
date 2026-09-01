# ABC Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Statement +
> status + one-line control-step framing only. The full 10-step
> research-protocol attack (progress/notes/attempts) is pending budget.
> Load-bearing facts flagged `[to-verify]`. Source page:
> unsolvedproblems.org/index_files/abc.htm.

## Statement
For coprime positive integers $a+b=c$, let $\mathrm{rad}(abc)$ be the product
of the distinct prime divisors. The ABC conjecture (Masser–Oesterlé, 1985):
for every $\varepsilon>0$ there is $K_\varepsilon$ with
$c < K_\varepsilon\,\mathrm{rad}(abc)^{1+\varepsilon}$.

## Status
**OPEN.** Mochizuki's claimed proof via Inter-Universal Teichmüller (IUT,
2012–21) is **not broadly accepted** (publication in PRIMS 2021; widespread
controversy / Scholze–Stix objection 2018) — treat as unresolved. Verified
computationally on vast ranges `[to-verify: best computation]`.

## Frontier (one line)
The $(1+\varepsilon)$-quality bound holds on all checked triples (ABC@home:
*all* $\approx14.4\cdot10^6$ triples with $c<10^{18}$ enumerated; record
quality still Reyssat 1987, $q\approx1.6299$) `[summary]`; the uniform
constant $K_\varepsilon$ is the open content. **Unconditional records**
(2026-08-31 hunt scan, all `[summary]/[to-verify]` vs abstracts): upper
$\log c\ll \mathrm{rad}^{1/3}(\log\mathrm{rad})^3$ (Stewart–Yu 2001);
exceptional set — **Browning–Lichtman–Teräväinen 2024: $\{c<
\mathrm{rad}(abc)^{1-\varepsilon}\}\cap[1,X]$ is $O(X^{33/50})$**
(arXiv:2410.12234 — the density→pointwise wall given an explicit power
saving, directly parallel to Goldbach's ladder); **Pasten 2024** (Invent.
Math. 236): first unconditional subexponential-type bound (restricted to
$a\le c^{1-\eta}$, via Shimura curves); lower record Bright 2024
($\kappa=6.563$).

## Control-step framing (one line)
Resolution on slices (verified triples up to a bound) → control = the
inequality for *all* triples uniformly — a density→pointwise / uniform-constant
control wall, the same spine as [[riemann_hypothesis]] / [[collatz_conjecture]].

## See also
- [[beals_conjecture]] — abc ⇒ Darmon–Granville finiteness for Beal
  (attempt-03); abc is the load-bearing external conjecture in Beal's
  resolution layer.
- [[riemann_hypothesis]], [[collatz_conjecture]] — density→pointwise control.