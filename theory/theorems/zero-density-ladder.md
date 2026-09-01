---
type: theorem
name: Zero-density ladder (N(σ,T) bounds)
created: 2026-08-31
tags: [number-theory, analytic-number-theory, zeta, zero-density]
used-in: [[riemann_hypothesis], [legendre_conjecture], [twin_prime_conjecture], [goldbach_conjecture]]
provenance: [[riemann-hypothesis-attempt-01], [guth-maynard-annals-2026]]
---

# The zero-density ladder

## Statement

$N(\sigma,T)$ := number of zeros of $\zeta(s)$ with $\Re(s)\ge\sigma$,
$0<\Im(s)<T$. The ladder bounds $N(\sigma,T)\ll T^{c(\sigma)+o(1)}$; each
rung lowers $c(\sigma)$. RH is the endpoint $c(\sigma)\equiv0$; every rung is
a *density* statement — it never forces any individual zero onto the line.

## The rungs (verified through the 2026-08-31 hunt)

- **Ingham 1940:** $c(\sigma)=\dfrac{3(1-\sigma)}{2-\sigma}$ — the base of
  the ladder, stood as the anchor for the whole $\sigma$-range for decades.
- **Huxley 1972:** $c(\sigma)=\dfrac{12(1-\sigma)}{5}$ — the intervening
  best in the range $\sigma\le\tfrac34$ (the accurate history: Guth–Maynard
  is the first *substantive* improvement **since Huxley in that range**, not
  "since Ingham" — the earlier wiki wording was corrected 2026-08-31).
- **Guth–Maynard 2024** (Annals of Math. (2) **203** (2026), no. 2, 623–675;
  arXiv:2405.20552) `[verified]`: $c(\sigma)=\dfrac{15(1-\sigma)}{3+5\sigma}$,
  so $c(3/4)=\tfrac{30}{13}\approx2.31<2.5$. Method: new "flexible"
  large-values estimates for Dirichlet polynomials (replacing the rigid
  Huxley approach); consequence PNT in intervals
  $x^{17/30+o(1)}$.
- **Log-exponent refinement (Chourasiya–Simonič line):** for the *Carlson-type*
  $(\log T)^{\delta(\sigma)}$ factor: Chourasiya 2024 (arXiv:2412.02068)
  advertised $\delta=5-2\sigma$ but an automated audit (Pith) flags the proof
  as written concludes Carlson's original $(\log T)^4$
  `[rh-chourasiya-flagged]`; Chourasiya–Simonič 2025 (arXiv:2507.15184)
  explicitly supersedes with $\delta=\dfrac{7-5\sigma}{2-\sigma}$. Cite the
  superseding estimate, not the advertised one.

## Consequence ceiling (why the ladder cannot climb to RH)

Converting the best ladder rung + best zero-free region into "primes in every
short interval" hits a **log gap, not an exponent gap**: even the conjectural
end of the density ladder leaves interval exponents bounded away from the
$2\sqrt x$ scale Legendre needs — the residual obstruction is the logarithmic
factor, not the power of $x$ [[legendre_conjecture]]. Dually the ladder
feeds the proportion-on-line ladder (Levinson → Conrey → PRZZ → Wu →
Alpöge–Furman $\ge0.6725$) via Weil-type positivity on mollified moments —
and there the *certificate ceiling*
$p_0\le0.6818287$ (`[rh-bandwidth-ceiling-verified]`,
[[riemann_hypothesis]]) is a proved limit on any Fourier-support-1
certificate: the density engine quantitatively cannot certify all zeros.

## When to reach for it

Any attack that needs "few zeros off the line" as an input (prime gaps
[[twin_prime_conjecture]], primes in intervals [[legendre_conjecture]],
Goldbach exceptional sets [[goldbach_conjecture]]): take the best rung, but
state which rung you used — several claimed 2024–26 results silently assume
a rung stronger than proven (that is exactly the Chourasiya failure mode).

## See also

- [[riemann_hypothesis]] — frontier table; the ladder is the
  resolution-on-average layer.
- [[method-average-vs-pointwise-control]] — the density→pointwise wall the
  ladder runs into.