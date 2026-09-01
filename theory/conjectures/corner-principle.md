---
type: conjecture
name: corner principle
status: open
raised-by: [[beals_conjecture]]
created: 2026-08-31
evidence: computational (56/56 signatures, corrected scans; robust under a wider box) + mechanism (granularity exponent)
---

# The Corner Principle

**Statement.** For every signature $(p,q,r)$ of pairwise distinct odd
primes, the **minimum genuine gap**
$$G(p,q,r)=\min\{|A^p+B^q-C^r|:\ A,B,C\ge2,\ \gcd(A,B,C)=1,\ |\cdot|\notin\{0,1\},\ A^p\ne C^r,\ B^q\ne C^r\}$$
is attained at $C\le3$.

**Evidence (all 56 signatures from primes $\{3,\dots,23\}$).**
Corner scan ($C\le3$) equals full box scan ($C\le60$, $B\le10^4$, exact
nearest $A$) for **56/56** signatures: $C=2$ for 55; $C=3$ only at
$(5,11,13)$ (2681 at $(17,3,3)$). 0 genuine gap-1 hits in the whole scanned
open class. **Wider robustness box $C\le100$, $B\le10^5$: 0 violations in 56
signatures, all minima identical to the $C\le60$ table**
(`near_miss_robustness.py`, confirmed 2026-08-31).
`problems/beals-conjecture/scripts/near_miss_package.py`, data in
`near_miss_package_data.json`.

**Boundary law (the principle is a hyperbolicity phenomenon).** With
granularity exponent $\gamma:=1-r\chi=r(1-\frac1p-\frac1q)$:
- FAILS at $(3,3,3)$ ($\gamma=1$; $G=2$ at $(5,6,7)$, corner value 11, and
  *four genuine gap-1 near-misses*, e.g. $6^3+8^3=9^3-1$) and $(3,3,5)$
  ($\gamma=5/3$; $G=2$ at $(239,271,32)$: $271^3+239^3=2^{25}-2$).
- HOLDS at $(3,3,7)$ and $(3,5,5)$ ($\gamma=7/3$ each; $G=5$).
- The open class has $\gamma\ge3.267$ (min at $(3,5,7)$) — strictly above
  the failure boundary ($\gamma\le5/3$).

**Mechanism (heuristic).** Attainable sums $A^p+B^q$ near height $C^r$ have
mean spacing $\sim C^{\gamma}$; when $\gamma$ is super-cubic (whole open
class) large $C$ contributes only sparse values and the global min is pinned
to the corner, where it is small-number arithmetic — erratic, no smooth law
in $\chi$ (this is why the attempt-19 monotone prediction failed; see
[[counting-heuristic]]). Near the Euclidean line ($\gamma$ small) deep
large-base coincidences stay competitive and the corner fails.

**What would disprove it.** Any open-class signature whose genuine minimum
sits at $C\ge4$ — a deep large-base coincidence; predicted not to exist.

**Status.** Open conjecture with verified finite evidence + mechanism;
proving it even for $(3,5,7)$ alone ("for $C\ge4$, $|A^3+B^5-C^7|>29$ for all
primitive non-degenerate triples") is the natural first target.

Related: [[near-miss-stratification]], [[odd-odd-pillai-2]], [[beal-equation]].