---
type: conjecture
name: odd-odd Pillai-2
status: open
raised-by: [[beals_conjecture]]
created: 2026-08-31
evidence: computational (10^18 exhaustive per-bounded search) + local solubility (no obstructing modulus) + even-exponent case completely solved + structural lemmas S2-S4 (mod-24 difference, power-residue sieve, local uniformity) + plane heuristic (~0.38 expected solutions over the ENTIRE plane, ~all mass inside the 1e25 boxes)
---

# Odd–odd Pillai-2

**Statement.** The equation $X^u - Y^v = 2$ has no solutions in integers
$X, Y \ge 2$ with $u, v$ both odd primes. (The $u=v$ case is trivially
impossible by factorization, e.g. $X^3-Y^3=(X-Y)(X^2+XY+Y^2)=2$; the content
is $u\ne v$.)

**Provenance.** A *named restriction* of the famous open $k=2$ case of
Pillai's conjecture (explicitly listed as open in Waldschmidt's survey
arXiv:0908.4031, quoting Bilu–Bugeaud–Mignotte Problem 3; only $k=1$ is
solved — Catalan–Mihăilescu). Isolated in
[[beals_conjecture]] attempt-25 because the stratification theorem
([[near-miss-stratification]] T2) shows it is *exactly* the obstruction
between "all recorded gap-1 near-misses are degenerate" and a theorem: under
it, the universal families $(t^r,1,t^p)$, $(1,t^r,t^q)$ are the only unit-base
gap-1 near-misses of every Beal-open signature, globally.

**Evidence.**
1. No solutions with $Y^v \le 10^{18}$ over all ordered odd-prime pairs
   $u,v\le23$ (1,004,437 powers checked; exact integer arithmetic) —
   `problems/beals-conjecture/scripts/near_miss_package.py` Part 4.
   **EXTENDED 2026-08-31 (loop block, `scripts/pillai2_ext_search.py`):
   no solutions with $Y^v \le 10^{21}$ over the FULL odd-prime exponent
   range** — $v\in\{3,\dots,67\}$ (exhaustive: $Y\ge2 \Rightarrow 2^v\le
   Y^v\le B$), $u\le\log_2 N$ per $N$ (exhaustive: $X\ge2\Rightarrow u\le
   \log_2(Y^v+2)\le69$). $10{,}017{,}017$ $(v,Y)$ pairs, $174{,}141{,}873$
   integer $u$-th-root checks, exact integer arithmetic, Newton roots
   unit-tested on 5000 random $a^k\pm1$ cases. Cross-checks: no
   solutions at $10^6$ or $10^9$ (the old $u,v\le23$ cap never binds at
   these bounds — $2^{23}\approx8.4\times10^6$ — so the extension at
   $10^{21}$ genuinely subsumes the $10^{18}$ data and widens exponents
   $23\to67/69$). **Further extended 2026-08-31→09-01: no solutions with
   $Y^v \le 10^{22}$, then $10^{24}$, then $10^{25}$, full odd-prime
   range** ($v\in\{3,\dots,83\}$ at the final bound, exhaustive,
   $u\le\log_2 N$ exhaustive per value): the $10^{25}$ run checked
   $215{,}547{,}548$ $(v,Y)$ pairs and $4{,}472{,}139{,}830$ root checks
   (`scripts/pillai2_ext_search.py`, logs `pillai2_1e22.log`,
   `pillai2_1e24.log`, `pillai2_1e25.log`). This discharges the preprint's
   final pre-submission gate ([near-miss-stratification], §9). **Bound-
   pushing declared saturated at $10^{25}$** — future evidence should be
   structural (mod-8 residue $X-Y\equiv2\pmod8$, Jacobi reciprocity,
   Bennett–Siksek-style modular sieves), not ladder extensions.
2. Everywhere locally soluble: no obstructing modulus $m\le1000$, no prime
   power $p^k\le10^6$, all odd-prime pairs $\le23$ (Part 5). Catalan-like:
   not refutable by congruences; any proof is global.
3. The even-exponent analogue is completely solved: $x^2+2=y^n$ has the
   unique solution $5^2+2=3^3$ [Cohn 1993 / BMS 2006; attribution
   to-verify against LeVeque 1952, Siksek 2003].

**Prior-art mapping (2026-08-31 loop block, search-level `[summary]`,
to-verify against paper bodies before load-bearing reuse).**
4. The odd-odd restriction is genuinely untouched territory, and the page's
   scope is exactly complementary to the only known example: the *only*
   gap-2 solution with both exponents $>1$ known is $3^3-5^2=2$ — i.e.
   $5^2+2=3^3$, the even-exponent (v=2) case of item 3. The search-to-$10^{18}$
   table for gap 2 finds exactly that one pair, consistent with this page's
   exhaustive odd-odd negative at the same bound.
5. Global status of $x^p-y^q=2$: it is the $k=2$ case of Pillai's conjecture
   and **not even finiteness is known** in the four-variable problem
   (Waldschmidt survey arXiv:0908.4031, quoting Bilu–Bugeaud–Mignotte
   Problem 3 — the wiki's standing citation, reconfirmed). Finiteness IS
   known once any one of $X,Y,u,v$ is fixed (Shorey–Tijdeman, *Exponential
   Diophantine Equations* Ch. 12). Framework results: Scott–Styer (JNT 118,
   2006, generalized Pillai classification); Bennett (Canad. J. Math. 53,
   2001: fixed bases ⟹ at most 2 solutions); Bennett–Siksek (Algebra &
   Number Theory 17 (2023) 1789–1845, prime-power gaps: $x^2\pm q^\alpha
   =y^n$ for primes $q<100$). abc ⟹ quantitative Pillai (Tijdeman/Waldschmidt).
6. **No Cassels/Inkeri/Mihăilescu-style divisibility or double-Wieferich
   criterion is known for gap 2** (the $k=1$ toolbox is unported) — which
   sharpens the page's "no obstructing modulus / any proof is global" line:
   there is currently *no local or congruence entry point at all* for
   odd-odd, so the computational exhaustion route (this page's evidence 1)
   is the only systematic evidence-generating mechanism presently available.
   **Amended 2026-09-01** (see the Structural entry points section below):
   a provable *factor-level* power-residue sieve now exists (Lemma S3), and
   the flatness of the local landscape is quantified (Lemma S4) — modulus
   obstructions still absent.
7. Structural corollary of the even-base kill: any solution has $X,Y$ both
   odd, hence $X-Y\equiv2\pmod 8$ (odd bases, $x^u\equiv x\bmod 8$ for odd
   $u$) — a cheap necessary condition for targeted future searches.

## Structural entry points (2026-09-01 loop block) `[pillai2-local-sieve]`

All three items below are **proved here** (two lines each), and the third
is **quantified computationally** over the full exponent range. They amend
item 6 above ("no local or congruence entry point at all"): modulus-style
obstructions remain absent (item 2), but there IS a provable
**factor-level** entry point, plus a quantified statement that the local
landscape is flat.

**Lemma S2 (mod-24 difference).** Any solution has $X-Y\equiv 2\pmod{24}$.
*Proof:* item 7 gives $X-Y\equiv2\pmod 8$; mod 3, $X^u\equiv X$ and
$Y^v\equiv Y\pmod 3$ (Fermat: $x^2\equiv1$ for $3\nmid x$, and $u,v$ odd;
the $3\mid x$ cases are $0\equiv0$), so $X-Y\equiv 2\pmod 3$; CRT. ∎

**Lemma S3 (power-residue sieve — the first entry point).** $\gcd(X,Y)=1$
($\gcd\mid 2$ and both odd). Reducing $X^u=Y^v+2$ mod $Y$ and $Y^v\equiv-2$
mod $X$, then applying the power-residue criterion in the cyclic group
$\mathbb{F}_q^\times$ ($a$ is a $g$-th power iff $a^{(q-1)/\gcd(e,q-1)}=1$):
- (i) every prime $p\mid X$ with $p\equiv1\pmod v$ satisfies
  $(-2)^{(p-1)/v}\equiv1\pmod p$ — $-2$ must be a $v$-th power residue;
- (ii) every prime $q\mid Y$ with $q\equiv1\pmod u$ satisfies
  $2^{(q-1)/u}\equiv1\pmod q$ — $2$ must be a $u$-th power residue.
For $p\not\equiv1\pmod v$ (resp. $q\not\equiv1\pmod u$) the power map is
surjective and gives no constraint. ∎ By Kummer/Chebotarev, among primes
$p\equiv1\pmod v$ the fraction with $-2$ a $v$-th power is $1/v$
(computationally confirmed: $v=3$: $0.3329$; $v=5$: $0.1923$;
$v=7$: $0.1285$ vs $1/v = 0.3333/0.2000/0.1429$, all $p<50000$ — slow
convergence consistent with the Chebotarev error term) — so the sieve
shaves a $1-1/v$ fraction of the eligible prime factors of $X$
(compounding over the factorization). This is the first *provable*
restriction on the primes $X,Y$ may contain — a hook for
Bennett–Siksek-style modular work — though it obstructs no modulus (item 2
is untouched).

**Corollary S3a (the sieve made explicit for $u=3$ or $v=3$).** For
primes $p\equiv1\pmod3$, $2$ is a cubic residue mod $p$ $\iff$
$p=x^2+27y^2$; the same form also matches $-2$ exactly. Verified
computationally, 0 mismatches, all $p<20000$ (368 primes of each class;
`problems/beals-conjecture/scripts/` verification runs 2026-09-01; the
classical criterion is cubic reciprocity — Euler/Jacobi `[to-verify vs
primary]`). Hence in any solution of $X^3-Y^v=2$, every prime factor
$q\mid Y$ with $q\equiv1\pmod3$ is of the form $x^2+27y^2$ (and dually
for $p\mid X$ when $v=3$) — a thin, checkable shape constraint on the
prime factors, the concrete face of Lemma S3.

**Corollary S3b (forbidden-prime tables; 2 and $-2$ coincide).** For odd
prime $p$ and odd $e$, $(p-1)/e$ is even, so
$(-2)^{(p-1)/e}=2^{(p-1)/e}$ identically — **the sieve conditions for
$-2$ (factors of $X$) and $2$ (factors of $Y$) are the same list**.
Consequently, for each exponent $e\in\{u,v\}$: a prime $q\equiv1\pmod e$
with $2$ NOT an $e$-th power residue mod $q$ divides **neither** $X$ nor
$Y$. Computed tables (excluded factors, $q<3000$; density $(e-1)/e$ among
$q\equiv1\pmod e$): $e=3$: 7, 13, 19, 37, 61, 67, …; $e=5$: 11, 31, 41,
61, 71, 101, …; $e=7$: 29, 43, 71, 113, 127, 197, …; $e=11$: 23, 67, 89,
199, 353, 397, …; $e=13$: 53, 79, 131, 157, 313, 443, … E.g. in ANY
solution of $X^5-Y^v=2$, neither $X$ nor $Y$ is divisible by 11, 31, or
41. These are checkable arithmetic restrictions on the prime
factorizations of $X$ and $Y$ — the sharpest provable shape constraint
currently known for gap 2.

**Lemma S4 (local uniformity — computed + proved).** For odd primes
$u,v$ and an odd prime $p$ with $\gcd(u,p-1)=\gcd(v,p-1)=1$, the maps
$x\mapsto x^u$, $y\mapsto y^v$ are bijections on $\mathbb{Z}/p$, so
exactly $p$ residue pairs solve $x^u-y^v\equiv2$: the local fraction is
exactly $1/p$, *independent of $(u,v)$*. Computed over all 462 ordered
pairs of odd primes $\le83$ and moduli $8,3,5,7,9,11,13,25,17$
(`problems/beals-conjecture/scripts/pillai2_local_sieve.py`):
- every prime modulus gives the **same** fraction for every pair
  ($m{=}8$: exactly $1/16$; $m{=}p$: exactly $1/p$) — no modulus in sight
  prefers any $(u,v)$ over any other;
- the **only** differentiators are the prime powers: $m=9$ penalizes
  pairs with $u=3$ or $v=3$ by exactly $2/3$ ($0.0741$ vs $0.1111$), and
  $m=25$ penalizes $u=5$ or $v=5$ by $4/5$ ($0.0320$ vs $0.0400$);
- all 462 pairs are locally soluble at all nine moduli (confirms item 2,
  now over the full exponent range $\le83$ rather than $\le23$).
*Reading:* the surviving-pair product sits in a factor-$\sim$2 band
$[5.8\times10^{-10},\,1.1\times10^{-9}]$ across the whole exponent plane —
congruences cannot target any $(u,v)$, so per-curve work (genus
$\ge\frac{(u-1)(v-1)}{2}\ge4$ superelliptic curves) cannot be triaged by
local methods; combined with item 6 this sharpens "any proof is global"
into a quantified statement.

**Plane heuristic (2026-09-01, same block) — the 10^25 box is most of the
story.** Applying the spacing heuristic proven on [[magic_square_of_squares]]
(the hourglass H): for fixed $(u,v)$, a solution needs $Y^v+2$ to be an
exact $u$-th power; $u$-th powers near $Y^v$ are spaced $\approx uX^{u-1}$
with $X\approx Y^{v/u}$, so $P\approx 1/(u\,Y^{v(u-1)/u})$ and
$$E(u,v)\approx\tfrac1u\bigl(\zeta\bigl(\tfrac{v(u-1)}u\bigr)-1\bigr),$$
which converges for every odd-prime pair (worst exponent $2$, at
$(u,v)=(3,3)$-type). Summed over all 462 ordered pairs $\le83$:
**total expected solutions over the ENTIRE plane $\approx 0.38$**, with
essentially **100% of that mass inside the already-searched boxes**
($Y^v\le10^{25}$: tail beyond $Y\le10^{25/v}$ is $<10^{-8}$ of each
$E(u,v)$). Dominant pairs: $(5,3)$ $0.077$, $(3,5)$ $0.049$, $(7,3)$
$0.045$ — $v=3$ with small $u$ carries the mass. *Reading (honest):*
Poisson $P(0\mid0.38)\approx68\%$ — the heuristic predicts the odd-odd
equation likely has **no solutions anywhere**, and the 10^25 ladder
already covers ~all of the heuristic's predicted mass, so the exhaustion
is not a small box but most of the expected story. Caveats: (i) the
spacing model treats $Y^v+2$ as random relative to $u$-th powers; Lemma
S4 shows the local corrections are $(u,v)$-flat, so the *relative*
structure is robust but the absolute constant could rescale; (ii)
heuristic, not proof — the genus argument is the only known route to
actual finiteness.

**Per-curve prior art (2026-09-01, search-level `[summary]`).** The
dominant pairs of the plane heuristic — $(5,3)$, $(3,5)$, $(7,3)$ — are
genus-4 superelliptic curves ($y^3=x^5-2$ etc., cyclic trigonal); **no
published complete solution of $x^5-y^3=2$ exists** (search 2026-09-01),
but the machinery exists: the general three-monomial algorithm of
Grechuk–Grechuk–Wilcox (arXiv:2307.02513, reducing $ay^m=bx^n+c$ to
finitely many Thue equations) and Bilu–Hanrot's Baker-method solution of
binomial superelliptic equations (Compositio 1998). (Note $(1,-1)$
solves $x^5-y^3=2$ but is outside our $X,Y\ge2$.) So the structural
program "settle the dominant pairs individually, covering most of the
heuristic mass" is concrete but a genuine computational number theory
project, not a wiki-side block.

**S3 sieve quantification (2026-09-01, later block;
`pillai2_s3_sieve_density.py`).** How much search space does the
provable forbidden-prime sieve (Lemma S3/S3b) actually remove? Measured
over forbidden primes $q\le2\cdot10^5$ for $e\in\{3,5,7,11,13,17,19\}$:
the surviving density of integers with no forbidden prime factor decays
exactly as the Mertens-thinning prediction $C_e(\log z)^{-1/e}$ —
fitted slopes $0.3225/0.1965/0.1441/0.0787/0.0757/0.0689/0.0484$ vs
theory $1/e=0.3333/0.2000/0.1429/0.0909/0.0769/0.0588/0.0526$. At the
$10^{25}$ box this extrapolates to surviving fractions $P_e\approx0.30$
($e=3$), $0.51$ ($e=5$), $0.65$ ($e=7$), $\ge0.76$ ($e\ge11$), i.e.
**combined search-space reductions of only $\times6.5$ for the dominant
pair $(5,3)$, $\times5.1$ for $(7,3)$, $\times3.1$ for $(5,7)$**.
*Reading (honest):* the sieve is real and provable but explains only an
order-1 constant of the $10^{25}$-box null — it is a future entry point
(any modular/exhaustive attack gets a $\sim(\log z)^{1/u+1/v}$
discount, growing too slowly to matter alone), not an explanation of
the null; the explanation remains the plane heuristic above ($\approx
0.38$ expected solutions over the whole plane, $\sim100\%$ of mass
inside the searched boxes, Poisson $P(0)\approx68\%$).

**What would prove/disprove it.** Disprove: any single solution of
$X^u-Y^v=2$ with $u,v$ odd primes. Prove: even one instance pair (e.g.
$X^5-Y^3=2$) completes the unit-base gap-1 classification for every
signature containing that pair (via [[near-miss-stratification]] T2).

**Status.** Open. Related: [[beal-equation]], [[near-miss-stratification]],
[[corner-principle]].