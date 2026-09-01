---
type: theorem
name: near-miss stratification (unit-base gap-1 of generalized Fermat signatures)
created: 2026-08-31
tags: [number-theory, generalized-fermat, near-misses, pillai]
used-in: [[beals_conjecture]]
provenance: [[beal-near-miss-stratification-preprint]]
---

# Near-miss stratification theorem

**Setting.** Signature $(p,q,r)$ of pairwise distinct primes; the *universal
families* are $\mathcal{F}_1=\{(t^r,1,t^p)\}$ and $\mathcal{F}_2=\{(1,t^r,t^q)\}$
(both satisfy $A^p+B^q-C^r=+1$ identically); a *unit-base* triple has some
base $=1$.

**Theorem.**
- **T1 (unconditional, global).** Every unit-base gap-(+1) near-miss
  ($A^p+B^q-C^r=+1$) lies exactly on $\mathcal{F}_1\cup\mathcal{F}_2$.
  *Proof (one paragraph):* $B=1\Rightarrow A^p=C^r\Rightarrow$ (by
  $\gcd(p,r)=1$ + UFD) $A=t^r,\ C=t^p$; symmetric for $A=1$;
  $C=1\Rightarrow A=B=1$. Conversely both families have gap $+1$ identically.
- **T2 (exact reduction).** The unit-base gap-(−1) channel is exactly
  $X^r-Y^p=2$ and $X^r-Y^q=2$ — the odd-odd restriction of Pillai's $k=2$
  equation ([[odd-odd-pillai-2]]). ($C=1$ is impossible: $A^p+B^q\ge2$.)
- **T3 (raw-metric bound).** Quasi-degenerate triples ($A^p=C^r$ or
  $B^q=C^r$, i.e. $(t^r,B,t^p)$ / $(A,t^r,t^q)$) have gap exactly $B^q$ /
  $A^p$; hence raw min gap $\le2^{\min(p,q)}$ (at $(2,3^r,3^q)$ /
  $(3^r,2,3^p)$, $t=3$); and $\gcd(t^r,B,t^p)=\gcd(t,B)$. Metrics that do
  not exclude this layer measure the layer, not the problem.
- **T4 (even-exponent boundary; conditional on the classical complete
  solution of $x^2+2=y^n$ — Cohn 1993 / BMS 2006, attribution to-verify).**
  If the signature contains $2$ (say $p=2$), the $B=1$ sub-channel of the −1
  side is $x^2+2=y^n$, whose unique solution $5^2+2=3^3$ forces $r=3$:
  the sub-channel exists only at signatures $(2,q,3)$ via the single triple
  $(5,1,3)$; the $A=1$ sub-channel is odd-odd Pillai-2 again. So Beal's
  all-odd restriction removes precisely the surviving identity.

**Consequence (conditional on [[odd-odd-pillai-2]]).** The universal
families are the ONLY unit-base gap-1 near-misses of every Beal-open
(all-odd-distinct) signature, globally, with no bound on bases.

**When to reach for it.** Any analysis of near-misses / small gaps of
generalized Fermat equations: first strip the universal families and the
quasi-degenerate layer (T1/T3) — what remains is the genuine problem
([[corner-principle]], [[beals_conjecture]] attempt-25). Also the template
for "empirical regularity → theorem + exactly-identified open problem"
conversion.

**Caveats.** For *near-misses* (unlike exact Beal solutions),
$\gcd(A,B,C)=1$ is weaker than pairwise coprimality (e.g. $(2,3,2)$); state
which metric is used. T4's citation chain is flagged to-verify.

Full write-up: [papers/beal-near-miss-stratification.md](../../papers/beal-near-miss-stratification.md).