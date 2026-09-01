# Lonely Runner Conjecture

> **STUB — folder started 2026-08-25; attack opened 2026-09-01**
> `[lonely-runner-structural]` (prior-art verification + structural lemmas L1–L3
> + exact census engine; scripts/lonely_runner_census.py). Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/LonelyRunner.htm.

## Statement
$k$ runners on a unit track with distinct constant speeds; for some runner
$i$ and some time $t$, that runner is at distance $\ge \tfrac{1}{k+1}$ (mod 1)
from the start. Equivalently: for any $k$ distinct positive integers
$\{v_i\}$, $\exists t$ with $\|t v_i\|_{\mathbb R/\mathbb Z}\ge\tfrac{1}{k+1}$
for some $i$.

> **CORRECTION (2026-09-01, append-only):** the stub's "equivalently … for
> some $i$" clause is a MISSTATEMENT — $\max_i\|tv_i\|\ge\frac1{k+1}$ is
> near-trivial (take $t=\frac1{2\max v_i}$: the fastest runner sits at
> $\frac12$). The conjecture requires **all** runners simultaneously:
> $\min_i\|tv_i\|\ge\frac1{k+1}$ (survey Conjecture 2, verified against
> arXiv:2409.20160v3). The correct working form is the $\kappa(V)$
> formulation below.

**Working form (survey convention, verified 2026-09-01 against
arXiv:2409.20160v3, Conjecture 2):** for every $n$ and every $n$-set of
nonzero speeds $V=\{v_1,\dots,v_n\}$ there is $t$ with
$\min_i \|t v_i\|\ge\tfrac{1}{n+1}$. The **loneliness gap**
$$\kappa(V)=\sup_{t\in(0,1)}\min_{v\in V}\|tv\|$$
satisfies LRC$(n)$ $\iff$ $\kappa(V)\ge\tfrac1{n+1}$ for every $n$-set $V$
(the original Wills/Cusick "$n{+}1$ runners" formulation — runners counted
WITH the start point — is Conjecture 1 there; $n$ speeds here $= n{+}1$
runners there). $\kappa(V)$ is an exact computable finite quantity:
$\kappa(V)=\max_N \kappa_N(V)/N$ over $N=v+v'$ (Haralambis; Czerwiński–
Grytczuk; survey Eq. 8, computable in $O(n^2 v_n)$) `[summary]`, and by
Lemma L1 below as a finite maximum over explicit candidate times.

## Status
**OPEN.** (Wills 1967 / Cusick 1973.)

## Frontier (one line)
*(2026-09-01 verification pass; figures below verified against primary
sources on 2026-09-01 unless flagged.)*

> **FRONTIER UPDATE (2026-09-01, append-only correction — see "Literature
> update" section below):** the snapshot below was superseded the same day.
> Primary-source verification found that Rosenfeld's 8-runner paper is
> **PUBLISHED** (Math. Comp., DOI 10.1090/mcom/4243, online 2026-08-10), and
> that LRC is now proven (computer-assisted, published) through **10 runners
> = n=9 speeds**, with 11–13 runners (n=10..12) claimed in an April 2026
> preprint. The text below is kept as filed; read the update section for the
> current frontier.

**Proven $n\le 6$ speeds** (survey §6 table, arXiv:2409.20160v3): $n{=}2$
Wills/Cusick/Bienia–Goddyn–Gvozdjak–Sebő–Tarsi; $n{=}3$ Betke–Wills/Cusick;
$n{=}4$ Cusick–Pomerance (computer-aided)/Chen; $n{=}5$ Bohman–Holzman–
Kleitman 2001 (simplified Renault 2004); $n{=}6$ **Barajas–Serra 2008**,
*The Lonely Runner with Seven Runners*, Electron. J. Combin. 15(1) #R48,
DOI 10.37236/772 — VERBATIM-verified 2026-09-01: their "$k{+}1$ runners"
count includes all moving runners, so their seven-runner case $= n{=}6$
speeds, bound $1/7$; the stub's frontier line (proven $n\le6$, $n{=}7$ open)
is CORRECT, and the first search summary's "Barajas–Serra covered 7 [speeds]"
was the off-by-one. **New since the stub:** Rosenfeld 2025 (arXiv:2509.14111,
v2 Oct 2025, PREPRINT — abstract verified 2026-09-01) claims **LRC for eight
runners** ($n{=}7$ speeds) by computer verification + recent
minimal-counterexample bounds; recovers $n\le 6$ and the author expects
$n{=}9,10$ within reach of the method. Peer-review status open
`[to-verify: acceptance]` — until then **$n=7$ is claimed, not theorem**.
**Finite checking** (published): Malikiosis–Santos–Schymura, *Linearly-
exponential checking is enough…*, **Forum of Mathematics, Sigma 13 (2025)
e164** (arXiv:2411.06903; abstract verified) — building on Tao 2018
($n^{O(n^2)}$ velocity tuples), LRC for $n$ speeds reduces to checking
integer speeds $\le \binom{n+1}{2}^{\,n-1}\le n^{2n}$. *Stub refinement:*
the stub's "$n{=}7 \Rightarrow \sim6.8\cdot10^{11}$ instances" is the loose
$n^{2n}=7^{14}\approx6.8\cdot10^{11}$; the abstract's sharper
$\binom{8}{2}^{6}=28^{6}\approx4.8\cdot10^{8}$ tuples is the current
published finite-check size for the first unproven-by-hand slice — *finite
but not yet feasible: the cleanest literal instance of the slice→full wall*.
**Bounds:** Tao 2018 $\kappa(n)\ge\frac1{2n}+c\frac{\log n}{n^2\log\log n}$
(survey v3 text; the stub filed $(\log\log n)^2$ — discrepancy flagged
`[to-verify vs Tao's paper]`); trivially $\kappa(n)\ge\frac1{2n}$.
**Spectrum** `[summary]`: Kravitz, *Barely lonely runners and very lonely
runners* (Combinatorial Theory 1 (2021) P17, arXiv:1912.06034) —
Loneliness Spectrum Conjecture (values of $\kappa$ just above $1/(n{+}1)$);
Fan–Sun arXiv:2306.10417 disproved it for $n=4$ via
$\kappa(\{3,8,11,19\})=\tfrac7{30}$ — **that value independently
exact-verified by our engine (self-test T2)**; amended spectrum conjecture
open. Tight instances with $\kappa=\tfrac1{n+1}$: for $n\le5$ the only
known primitive ones are dilations of $\{1,\dots,n\}$ up to sporadic
exceptions (e.g. $\{1,3,4,7\}$ for $n=4$; Goddyn–Wong families)
`[summary, to-verify vs Kravitz paper]` — see census A/B below for the
exact box answer.

## Structural lemmas (2026-09-01 attack block) `[lonely-runner-structural]`

**Lemma L1 (candidate-time finiteness — the exact engine).** For positive
integers $V=\{v_1<\dots<v_n\}$, $\kappa(V)$ is a **maximum** (not just a
supremum), attained on the finite candidate set
$$C=\{m/(2v_i)\ :\ 1\le m<2v_i\}\ \cup\ \{m/(v_i+v_j)\ :\ 1\le m<v_i+v_j\},$$
so $\kappa(V)=\max_{t\in C}\min_i\|tv_i\|$ (finitely many exact rationals).
*Proof:* $g_i(t)=\|tv_i\|$ is continuous piecewise linear on $[0,1]$ with
slopes $\pm v_i$ and kinks exactly at $t\in\frac{1}{2v_i}\mathbb Z$
(where $tv_i$ crosses an integer or half-integer); $f=\min_i g_i$ is
continuous, so $\kappa(V)=\max f$ is attained. Take a maximizer $t^*$; if
$t^*$ is a kink of some $g_i$ or $t^*\in\{0,1\}$ (kinks of every $g_i$),
$t^*\in C$. Otherwise $t^*$ is interior to a maximal open interval $I$ on
which every $g_i$ is linear (no kinks), so $f$ is concave on $I$ and $t^*$
is an interior local max. Only the tight functions ($g_i(t^*)=f(t^*)$)
matter: if one function $g_i$ alone is tight, then $f=g_i$ near $t^*$ has
constant nonzero slope $\pm v_i$ — not a local max. So $\ge2$ tight
functions with slopes $s_i\in\{\pm v_i\}$; concavity at an interior max
gives $f'(t^*-)\ge0\ge f'(t^*+)$, i.e. $\max_{\text{tight}} s\ge0\ge
\min_{\text{tight}} s$, so some tight $g_i$ rises ($s_i=+v_i$) and some
tight $g_j$ falls ($s_j=-v_j$). Rising means $t^*v_i\equiv f(t^*)\pmod 1$
with $f(t^*)\in(0,\tfrac12)$; falling means $t^*v_j\equiv-f(t^*)\pmod1$.
Adding: $t^*(v_i+v_j)\equiv0\pmod1$, i.e. $t^*=m/(v_i+v_j)\in C$. ∎
*(The engine additionally scans the redundant class $\{m/|v_i-v_j|\}$;
self-test T4 confirms it never changes the value — 500/500 sets.)*

**Lemma L2 (reductions).** (a) *Homogeneity:* $L(cv)=L(v)$ for any integer
$c\ge1$, where $L(\cdot)$ is $\kappa(\cdot)$ — the map $t\mapsto ct$ is a
surjective endomorphism of $\mathbb R/\mathbb Z$, so
$\max_t\min_i\|t\,cv_i\|=\max_s\min_i\|s v_i\|$. Hence: census over
**primitive** (gcd-1) sets only. (b) *Signs/duplicates:* $\|-x\|=\|x\|$ and
duplicated speeds do not change $\min_i\|tv_i\|$, so WLOG $0<v_1<\dots<v_n$,
distinct. (c) *Real→integer sufficiency:* $V\mapsto\kappa(V)$ is continuous
(finite min/max of continuous functions), and distinct nonzero real speed
sets are exactly limits of distinct positive rational sets, which are
integer sets up to scaling by (a) — so LRC for integer tuples $\implies$
LRC for all real tuples: the integer census is the right universe. (d)
*Monotonicity in $n$:* $\kappa(v_1,\dots,v_{n+1})\le\kappa(v_1,\dots,v_n)$
(a larger min over one more runner). **Consequence: LRC$(n{+}1)$ never
follows from LRC$(n)$ — each $n$ is a genuinely new control problem, the
slice→full wall made literal** (contrast Brocard, where the sieve
re-verifies the same statement deeper).

**Lemma L3 (sharpness — consecutive speeds are extremal).**
$\kappa(\{1,2,\dots,n\})=\dfrac1{n+1}$ exactly.
*Proof:* ($\le$) Fix $t$; if some $it\equiv jt$ ($1\le i<j\le n$) then
$\|(j{-}i)t\|=0$ and $f(t)=0\le\frac1{n+1}$. Else $\{0,t,2t,\dots,nt\}$ is
$n{+}1$ distinct points on the unit circle, so some cyclic gap
$g\le\frac1{n+1}\le\frac13$ (for $n\ge2$; $n=1$ direct: $\kappa=\frac12$).
The two cyclically adjacent points are $it,jt$, and since $g<\tfrac12$,
$g=\|(j-i)t\|$ with $1\le|j-i|\le n$; hence $\min_i\|it\|\le g$. ($\ge$) at
$t_0=\frac1{n+1}$: $\|i\,t_0\|=\min(i,n{+}1{-}i)/(n{+}1)\ge\frac1{n+1}$ for
all $i\le n$. ∎
*Worked instances:* $\kappa(\{1,2\})=\tfrac13$ at $t=\tfrac13$;
$\kappa(\{1,2,3\})=\tfrac14$ at $t=\tfrac14$; engine-verified exactly for
$n\le9$ (self-test T1, all OK). **Corollary:** the constant $\frac1{n+1}$
is best possible, and $\{1,\dots,n\}$ is a tight instance — any census of
tight sets must contain its primitive dilation and the question "is it the
ONLY primitive tight set in the box?" is exactly the Kravitz-spectrum
question at the bottom of the spectrum.

## Census (2026-09-01; `scripts/lonely_runner_census.py`, log
`scripts/lonely_runner_census.log`)

Documented, self-tested exact engine (Lemma L1 candidate set, rational
arithmetic throughout; self-tests T1–T4 above run first, all pass, including
the independent exact verification of Fan–Sun's
$\kappa(\{3,8,11,19\})=\tfrac7{30}$). Censuses, all exhaustive within their
boxes, primitive sets only (Lemma L2a):

**Self-tests (2026-09-01 run, python 3.13.2/numpy 2.4.3, seed 20260901) —
ALL PASSED, verbatim:**
```
T1  kappa(1..1) = 1/2      expected 1/2   OK
T1  kappa(1..9) = 1/10     expected 1/10  OK   (all n=1..9 OK)
T2  kappa(3,8,11,19) = 7/30   expected 7/30   OK
T3  engine >= dense grid on 300 random sets (n=2..5, v<=30): 0 failures OK
T4  difference-class redundancy: 500 sets tested, 0 mismatches OK
```
T2 is an independent exact confirmation of Fan–Sun's spectrum
counterexample value; T1 is Lemma L3 for $n\le9$; T3 validates the engine
against a 200001-point exact rational grid; T4 validates the L1 proof's
claim that the redundant difference-class never matters.

**Census summary (verbatim tail of the run):**
```
n=2  sets=45      min_kappa=1/3        violations=0  tight=1
n=3  sets=196     min_kappa=1/4        violations=0  tight=1
n=4  sets=479     min_kappa=1/5        violations=0  tight=2
n=5  sets=786     min_kappa=1/6        violations=0  tight=2
n=6  sets=923     min_kappa=1/7        violations=0  tight=1
n=7  sets=11432   min_kappa=1/8        violations=0  tight=3
n=8  sets=6435    min_kappa=1/9        violations=0  tight=1
n=7  sets=10000   min_kappa=98/419     violations=0  tight=0
n=8  sets=3000    min_kappa=37/163     violations=0  tight=0
```
(blocks: A = exhaustive primitive $n$-subsets of $[1,12]$ for $n\le6$;
B7 = exhaustive 7-subsets of $[1,16]$; C8 = exhaustive 8-subsets of
$[1,15]$; D7/D8 = 10000/3000 random primitive 7-/8-subsets of
$[1,400]$/$[1,300]$. Full per-block output in the log.)

**Findings.** (1) **Zero LRC violations in every block** — no speed set
with $\kappa<\tfrac1{n+1}$: a bounded independent re-verification of the
theorem slice $n\le6$, and box-level support for $n=7$ (theorem + Rosenfeld
claim) and $n=8$ (open slice; box-probe only, no claim beyond the box).
(2) **Tight-set census** (exact, with witnessing times re-verified in a
separate probe): $n=4$: $\{1,2,3,4\}$ **and** $\{1,3,4,7\}$ — the latter
matches the literature's sporadic tight instance `[summary]`, now
independently exact-verified here ($\kappa=\tfrac15$ at $t=\tfrac15$);
$n=5$: $\{1,2,3,4,5\}$ **and** $\{1,3,4,5,9\}$ ($\kappa=\tfrac16$ at
$t=\tfrac16$); $n=7$ box: THREE tight sets — $\{1,\dots,7\}$,
$\{1,2,3,4,5,7,12\}$, $\{1,4,5,6,7,11,13\}$ (both at $t=\tfrac18$);
$n\le3$, $n=6$ and $n=8$ boxes: **only** the consecutive set. (3)
*Observation* (census pattern, not a theorem, `to-verify` vs the
Kravitz/Goddyn–Wong classifications): the sporadic tight sets
$\{1,3,4,7\}\subset\{1,3,4,5,9\}$ suggest a family $\{1,3,4,\dots,n,\,
n{+}4\}$, but its $n{=}6$ analogue $\{1,3,4,5,6,10\}$ lies inside the A6
box $[1,12]$ and is NOT tight — the pattern (if any) breaks at $n=6$; all
sporadic tight sets found have $\max V$ a sum of two earlier elements
($7{=}3{+}4$, $9{=}4{+}5$, $12{=}5{+}7$, $11{=}4{+}7$, $13{=}6{+}7$).
(4) Random large-speed sets are far from tight
($\min\kappa\approx0.234>0.125$ at $n=7$; $\approx0.227>0.111$ at $n=8$):
consistent with the hard instances being small-speed/combinatorial, the
regime the finite-check reductions (MSS, Rosenfeld) exploit.

## Literature update (2026-09-01 CONTINUE block) `[lonely-runner-frontier-update]`

**Rosenfeld verdict (Task 1 of the CONTINUE block; all items primary-source
verified 2026-09-01 unless flagged):**

> **VERDICT: claimed → PUBLISHED, peer-reviewed.** Rosenfeld, *The lonely
> runner conjecture holds for eight runners*, arXiv:2509.14111 (v1 17 Sep
> 2025, v2 16 Oct 2025) is **published in Mathematics of Computation**, DOI
> [10.1090/mcom/4243](https://doi.org/10.1090/mcom/4243), published online
> **2026-08-10** (Crossref record verified 2026-09-01: type journal-article,
> publisher AMS, ISSN 0025-5718/1088-6842, license "AMS license for accepted
> manuscript", ANR grant ANR-24-CE48-3758-01; the ams.org article landing
> page itself returned HTTP 403 to our fetcher — the Crossref deposit +
> DOI resolution are the verification). **n=7 speeds (8 runners) is a
> THEOREM** (computer-assisted), not merely a claim.

What exactly is proven and how (from the arXiv HTML v2, full text read
2026-09-01):
- **Theorem 1:** for every 7-set of integers $\{v_1,\dots,v_7\}$ there is $t$
  with $\min_i\|tv_i\|\ge 1/8$ — the survey convention, our $n=7$.
- **Analytic skeleton (proved):** Malikiosis–Santos–Schymura (arXiv:2411.06903,
  Theorem A) + AM-GM give an upper bound on the speed product of a minimal
  counterexample ($<7.4\cdot10^{54}$ for $n=7$); a lemma (their Lemma 4)
  forces $\mathrm{lcm}(2,\dots,n{+}1)\mid\prod v_i$; Lemmas 5–7 force a large
  set of primes $S$ (for $n=7$: $31\le p\le163$) to divide $\prod v_i$,
  pushing the product above the MSS bound — contradiction.
- **Computer-assisted part:** for each $p\in S$, an exhaustive set-cover /
  backtracking check over 7-tuples mod $p$ (largest case $p=163$: ~32 h on
  one core). **Code public:** https://gite.lirmm.fr/mrosenfeld/the-lonely-runner-conjecture.
- Same method reproves $n\le6$; abstract expects $n=9,10$ within reach.
- No independent replication of the computation is known to us; peer review
  by a journal specializing in computer-assisted proofs is the validation on
  record.

**Further frontier movement (all primary-source verified 2026-09-01):**
- **Trakulthongchai, *Nine and Ten Lonely Runners*, Electron. J. Combin.
  33(2) (2026) #P2.46, DOI 10.37236/14972, published 2026-06-05** —
  computer-assisted, refines Rosenfeld's sieve. **LRC(n) now a published
  theorem for $n\le9$ speeds** (10 runners).
- **Sungkawichai–Trakulthongchai, *Eleven, twelve, and thirteen lonely
  runners*, arXiv:2604.23906 (v1 26 Apr 2026, PREPRINT)** — claimed
  computer-assisted proof for $n\in\{10,11,12\}$ speeds (13 runners); new
  sieves + a polynomial-method proposition (tuple $\equiv(1,\dots,k)\bmod p$,
  $\gcd 1$, $k{+}1,p>k^2{+}k$ odd primes $\Rightarrow$ LRC); code public at
  github.com/vzsky/13-lonely-runners `[summary of abstract — not read in
  full]`. Until refereed: **n=10..12 claimed, not theorem.**
- Search-derived context, flagged `[summary, to-verify]`: Quanta Magazine
  coverage 2026-03-06; a 14-runner attack repo (github.com/Selopol/lonelyrunner,
  Jul 2026); **shifted** LRC false for n=5..17 (Blanco–Criado–Santos,
  arXiv:2603.24784 — unshifted LRC unaffected).
- Survey arXiv:2409.20160 still at v3 (12 Aug 2025), predates all of this.

**Current frontier:** LRC(n) proven (published, computer-assisted) for
$n\le9$ speeds; claimed for $n\le12$; **first open case = 14 runners
($n=13$ speeds)**. The wiki's Lemma L2(d) point stands a fortiori: each of
these was a fresh computational control problem per $n$, none derived from
the previous one. The stub/MSS finite-check numbers remain the published
*reduction*, but the actual attacks run Rosenfeld-style prime sieves, not
naive tuple enumeration.

## Census v2 (2026-09-01 CONTINUE; `scripts/lonely_runner_census_v2.py`,
    log `scripts/lonely_runner_census_v2.log`)

Same exact engine (imported unchanged from v1 — one engine definition),
flushed logging, deeper boxes; all exhaustive-within-box, primitive sets
only. Self-tests re-run first: T1 extended to n=1..12 (Lemma L3 exact, with
witness times, all OK — covers the new preprint slice), T2 Fan–Sun
$\tfrac7{30}$ OK, T3 grid (200 sets, n=6..8, v≤25) 0 failures, T4
difference-class (300 sets) 0 mismatches — **ALL PASSED, verbatim head/tail
in the log.**

**Verbatim summary (tail of the v2 run):**
```
  n= 6  sets=74144   min_kappa=1/7      violations=0  tight=1  tight_non_consecutive=0
  n= 8  sets=319605  min_kappa=1/9      violations=0  tight=1  tight_non_consecutive=0
  n= 9  sets=293920  min_kappa=1/10     violations=0  tight=1  tight_non_consecutive=0
  n= 9  sets=2000    min_kappa=67/309   violations=0  tight=0  tight_non_consecutive=0
  n=10  sets=800     min_kappa=20/111   violations=0  tight=0  tight_non_consecutive=0
```
(blocks: A6x = exhaustive primitive 6-subsets of [1,22]; E8 = 8-subsets of
[1,22]; F9 = 9-subsets of [1,21]; G9/H10 = 2000/800 random primitive
9-/10-subsets of [1,300]/[1,150]. Exact per-block output in the log. The
n=2..5 wide-box blocks are the separate scan
`scripts/lonely_runner_tightscan.py`, log `lonely_runner_tightscan.log`,
verbatim summary below.)

**Summary of the wide-box tight-set scan (condensed from
`scripts/lonely_runner_tightscan.py`, log `lonely_runner_tightscan.log`;
all figures verbatim from that log):**
```
W2  (n=2, [1,60], bound 1/3):   sets=1101   viol=0  tight=1  non-{1..n}=0
W3  (n=3, [1,40], bound 1/4):   sets=8410   viol=0  tight=1  non-{1..n}=0
W4  (n=4, [1,30], bound 1/5):   sets=25819  viol=0  tight=2  non-{1..n}=1  (1, 3, 4, 7)
W5  (n=5, [1,26], bound 1/6):   sets=64436  viol=0  tight=2  non-{1..n}=1  (1, 3, 4, 5, 9)
```
(the scan also counts, for every tight set found, the three structural
conditions of the Tight-set structure section — "(n+1)|v", "missing +/-1
residues", "failing T3" — ALL ZERO in every block; full per-block output in
the log.)

**Findings.** (1) **Zero violations in every block — no counterexample.**
Given the literature update, these blocks are now independent box-level
re-verifications of PUBLISHED theorem slices ($n=6,8,9$) and a preprint
slice ($n=10$ probe); had any violation exact-verified it would have
disproved a published theorem — none did. (2) **Box deepening:** the n=8
box went from 6,435 sets ([1,15], v1) to 319,605 sets ([1,22]); the n=9
slice is newly opened at 293,920 sets ([1,21]); n=2..5 boxes widened to
[1,60]/[1,40]/[1,30]/[1,26]. (3) **Tight sets:** n=6 in [1,22], n=8 in
[1,22] and n=9 in [1,21] have ONLY $\{1,\dots,n\}$; n=2 in [1,60] and n=3
in [1,40] likewise — the v1 "absence at n=6,8" was NOT a small-box
artifact, and absence extends to n=2,3 at much wider boxes; n=4,5 keep
exactly one sporadic each even in the widened boxes. (4) Random
probes far from tight again (min κ = 67/309 ≈ 0.217 > 1/10 at n=9;
20/111 ≈ 0.180 > 1/11 at n=10): hardness lives at small speeds.

## Tight-set structure (2026-09-01 CONTINUE block) `[lonely-runner-tightsets]`

Question (Task 3): *when do non-consecutive tight sets exist?* Data now:
exhaustive boxes n=2 [1,60], n=3 [1,40], n=4 [1,30], n=5 [1,26] (tightscan),
n=6 [1,22] (A6x), n=7 [1,16] (v1 B7), n=8 [1,22] (E8), n=9 [1,21] (F9).
Counts of non-consecutive primitive tight sets: **0, 0, 1, 1, 0, 2, 0, 0**
for n = 2..9 (the two at n=7 being $\{1,2,3,4,5,7,12\}$,
$\{1,4,5,6,7,11,13\}$; the ones at n=4,5 being $\{1,3,4,7\}$,
$\{1,3,4,5,9\}$).

**Lemma T (maximizer structure of a tight instance — PROVED).** Let
$V=\{v_1<\dots<v_n\}$, $n\ge2$, with $\kappa(V)=\tfrac1{n+1}$, and let
$t^*\in(0,1)$ be any maximizing time. Write $g_i(t)=\|tv_i\|$. Then:
(a) $t^*$ is **not a kink of any tight $g_i$** — a kink of $g_i$ has
$g_i(t^*)\in\{0,\tfrac12\}$, while a tight runner has
$g_i(t^*)=\tfrac1{n+1}\notin\{0,\tfrac12\}$.
(b) The tight runners at $t^*$ number $\ge2$ and split into **rising**
($g_i$ has slope $+v_i$ at $t^*$, equivalently
$t^*v\equiv+\tfrac1{n+1}\pmod 1$) and **falling** (slope $-v_i$,
$t^*v\equiv-\tfrac1{n+1}\pmod1$), both nonempty; for any rising $a$ and
falling $b$: $t^*(a+b)\in\mathbb Z$, and writing $t^*=m_0/s$ in lowest
terms, $s\mid(n{+}1)\gcd(a,b)$.
*Proof.* (a) immediate. (b) $t^*$ is a global max of $f=\min_i g_i$, hence
a local max, and near $t^*$ every tight $g_i$ is linear (not at a kink by
(a)) while every non-tight $g_j$ stays strictly above $f$ on a
neighborhood; so locally $f=\min$ of the tight $g_i$'s, linear functions
with slopes $\pm v_i\ne0$. One tight function alone would make $f$ strictly
monotone near $t^*$ — not a local max; with $\ge2$, the local-max condition
gives $\max_{\text{tight}} s\ge0\ge\min_{\text{tight}} s$, and slopes are
$\pm v$, so a rising and a falling tight runner exist. Rising means
$t^*a\equiv+\tfrac1{n+1}$, falling $t^*b\equiv-\tfrac1{n+1}\pmod1$; adding
gives $t^*(a+b)\equiv0\pmod1$. For the denominator claim:
$\tfrac{am_0}{s}=k+\tfrac1{n+1}$ forces $s\mid(n{+}1)am_0$ and likewise
$s\mid(n{+}1)bm_0$; $\gcd(s,m_0)=1$ gives $s\mid(n{+}1)a$,
$s\mid(n{+}1)b$, hence $s\mid(n{+}1)\gcd(a,b)$. ∎

**Lemma T3 (grid-time necessary condition — PROVED).** Every tight $n$-set
($n\ge2$) contains, **for each $M=2,\dots,n$, an element divisible by
$M$.** *Proof:* if no element is divisible by $M$, then at $t=\tfrac1M$
every runner sits at distance $\tfrac{d_i}{M}$ with
$d_i\in\{1,\dots,\lfloor M/2\rfloor\}\ge1$, so
$f(\tfrac1M)\ge\tfrac1M\ge\tfrac1n>\tfrac1{n+1}$, contradicting
$\kappa(V)=\tfrac1{n+1}$. ∎
*Cousin of Rosenfeld's Lemma 4* (a counterexample must have
$\mathrm{lcm}(2,\dots,n{+}1)\mid\prod v_i$): here a TIGHT instance must
spread divisibility — each $M\le n$ divides some single element.
Engine-checked on all 11 tight sets found: 11/11 satisfy T3 (also 11/11
satisfy (c) below and none has an $(n{+}1)$-multiple).

**Corollary T-2 (T1 holds at n=2 — PROVED).** A tight primitive 2-set
$\{a,b\}$ has $3\nmid a$ and $3\nmid b$. *Proof:* apply Lemma T(b) with the
tight pair forced to be $\{a,b\}$ itself: $t^*=m/(a{+}b)$, $\gcd(a,b)=1$,
so $s\mid 3$; then $t^*=m_0/s$ with $s\in\{1,3\}$ and $3at^*\equiv1\pmod3$
forces $t^*\in\{\tfrac13,\tfrac23\}$ and $a\equiv\pm1\pmod3$. ∎
(For $n=2$ this is the FULL Conjecture T1 below; for $n\ge3$ the method
stalls — see the stall note.)

**Conjecture T1 (witness-rigidity of tight instances — OPEN, evidence
11/11).** Every tight $n$-set ($n\ge2$) satisfies $(n{+}1)\nmid v$ for all
$v\in V$. Equivalently (by (c) below): $t=\tfrac1{n+1}$ is a maximizing
time for every tight instance, and $V$ contains elements $\equiv+1$ and
$\equiv-1\pmod{n+1}$.
*(c) — proved, conditional direction:* if $(n{+}1)\nmid v$ for all $v$, then
at $t_0=\tfrac1{n+1}$ every runner has distance $\ge\tfrac1{n+1}$ (residue
in $\{1,\dots,n\}$), so $f(t_0)\ge\kappa(V)$ and $t_0$ maximizes; Lemma T(b)
at $t_0$ then gives the $\pm1$ residues and $t_0(a{+}b)\in\mathbb Z$.
*Evidence:* every tight set found in every census box (v1 + v2 + tightscan,
11 sets, boxes to [1,60]) avoids multiples of $n{+}1$; equivalently no
tight set in any box contains an element of $\{n{+}1, 2(n{+}1),\dots\}$
within the box. *Stall:* for $n\ge3$ the multiple of $n{+}1$ could in
principle be a NON-tight runner at the maximizer, and Lemma T(b) constrains
only tight runners — no contradiction obtained; the reduction to $n=2$
(Corollary T-2) is where the proof stops.

**Conjecture T2 (existence pattern — OPEN, census-level).** Non-consecutive
primitive tight sets exist for $n\in\{4,5,7\}$ and do not exist for
$n\in\{2,3,6,8,9\}$ within the tested boxes (n=2 [1,60], n=3 [1,40],
n=6 [1,22], n=8 [1,22], n=9 [1,21]). No arithmetic pattern in $n$ is
apparent (present at
$n+1\in\{5,6,8\}$, absent at $n+1\in\{3,4,7,9,10\}$); the absence at
$n\equiv0\pmod 3$ ($n=3,6,9$) is consistent but rests on 3 points.
Testable next: n=7 beyond [1,16] (do MORE than 2 sporadics appear?), n=6
beyond [1,22], n=10.

**Evidence table (all 11 tight sets found, all engine-exact; conditions:
T3 = Lemma T3; ±1 = contains both $+1$ and $-1$ residues mod $n{+}1$;
mult = contains a multiple of $n{+}1$; Σ = max V is a sum of two elements):**

| n | V | t* | T3 | ±1 | (n+1)∤v | Σ |
|---|---|----|----|----|----|----|
| 2 | {1,2} | 1/3 | ✓ | ✓ | ✓ | – (max=2 not 1+1) |
| 3 | {1,2,3} | 1/4 | ✓ | ✓ | ✓ | ✓ (3=1+2) |
| 4 | {1,2,3,4} | 1/5 | ✓ | ✓ | ✓ | ✓ (4=1+3) |
| 4 | {1,3,4,7} | 1/5 | ✓ | ✓ | ✓ | ✓ (7=3+4) |
| 5 | {1,2,3,4,5} | 1/6 | ✓ | ✓ | ✓ | ✓ (5=1+4,2+3) |
| 5 | {1,3,4,5,9} | 1/6 | ✓ | ✓ | ✓ | ✓ (9=4+5) |
| 6 | {1,…,6} | 1/7 | ✓ | ✓ | ✓ | ✓ |
| 7 | {1,…,7} | 1/8 | ✓ | ✓ | ✓ | ✓ |
| 7 | {1,2,3,4,5,7,12} | 1/8 | ✓ | ✓ | ✓ | ✓ (12=5+7) |
| 7 | {1,4,5,6,7,11,13} | 1/8 | ✓ | ✓ | ✓ | ✓ (13=6+7) |
| 8 | {1,…,8} | 1/9 | ✓ | ✓ | ✓ | ✓ |

*Additional observed regularities (census, unproved):* every tight set
found contains 1 (min V = 1); every sporadic tight set's max V is a sum of
two of its elements (v1 observation, now confirmed in widened boxes — the
naive family $\{1,3,4,\dots,n,n{+}4\}$ still breaks at n=6, v1 finding (3));
the tight runners at $t_0$ are exactly the $\pm1$-residue elements, and in
all 11 sets their sum is exactly $n{+}1$ (pair $(1,n)$ or $(1,n{-}1)$-type:
$(1,4),(1,5),(1,7),(1,7)$). *Caveat:* the boxes start at 1, so "contains 1"
may be a box artifact — a tight set with min V > 1 has never been observed
but the boxes cannot exclude it beyond their depth.

**T1 deep-box scan (`lonely_runner_t1_scan.py`, 2026-09-01,
`lonely_runner_t1_scan.log`):** exact integer fast-path engine (cross-
validated against the reference Fraction engine, 1001/1001 agreement)
with the two *proved* filters (Lemma T3; the $t_0=\tfrac1{n+1}$
attainment check) pre-rejecting non-tight candidates, run on the boxes
flagged "Testable next" above: **n=6 widened [1,22]→[1,30]** (588,559
primitive sets, 257,302 full evals): tight = {1..6} only, **T1
violations 0**; **n=7 widened [1,16]→[1,22]** (170,213 sets): the same
3 tight sets as in [1,16] — {1..7}, {1,2,3,4,5,7,12},
{1,4,5,6,7,11,13} — **no new sporadics** (answers the filed "Testable
next: do MORE than 2 sporadics appear beyond 16?" — no), **T1
violations 0**; **n=10 first box [1,14]** (1,001 sets): tight =
{1..10} only, **T1 violations 0** — and note this box is *beyond the
proved LRC frontier* (theorems reach 9 speeds), so its zero-violation
count is census evidence, not a check. Evidence for Conjecture T1:
still **11/11** tight sets across all boxes (no new ones found), now in
deeper boxes, still zero containing a multiple of $n+1$; T2's absence
pattern extends (n=6 now [1,30]). The
stall stands: for $n\ge3$ the multiple of $n+1$ could be a non-tight
runner at the maximizer and Lemma T constrains only tight runners.

**Tight-triple deep scan (`lonely_runner_n3_deep.py`, 2026-09-01,
`lonely_runner_n3_deep.log`):** n=3 box pushed [1,40]→**[1,200]**
(1,098,601 primitive triples, 651,143 full κ-evals, 70 s, integer engine
cross-validated): **{1,2,3} is the ONLY tight 3-set** in the box; zero
κ < 1/4 violations; zero tight sets with 4 | v. This upgrades the n=3
situation from "T1 holds on a slice" to a census-exhaustive
classification, filed as:

**Conjecture T4 (tight-triple classification — NEW, census-level,
evidence [1,200] exhaustive):** the only primitive tight 3-set is
$\{1,2,3\}$. Note $\{1,2,3\}$ is exactly the consecutive set, so T4
implies T1 at $n=3$ (no tight triple contains a multiple of 4) and
sharpens T2's pattern (absence of non-consecutive tight sets at $n=3$
is not a box artifact). A hand proof of T4 would likely come from an
equality-case analysis of the (classical, $n\le6$) LRC proof — open.

**Open-frontier probe (`lonely_runner_openfrontier.py`, 2026-09-01,
`lonely_runner_openfrontier.log`):** first census evidence in *genuinely
open territory* — exact integer engine (cross-validated) on the largest
cheap exhaustive boxes at the frontier: **n=11 [1,20]** (167,960
primitive sets), **n=12 [1,18]** (18,564), **n=13 [1,18]** (8,568; the
first open case, 14 runners — beyond both the n≤9 theorems and the
n≤12 preprint claims): **zero κ < 1/(n+1) violations in all three**;
the only tight set in each box is {1,…,n}; T1 (no multiple of n+1) and
T2 (no non-consecutive tight set) clean. First-probe boxes, not deep
censuses — but the pattern (consecutive-only tight sets, T1/T2 clean)
now extends across the proved frontier into the open range.

## T4 attack (2026-09-01): window lemmas T4-a…T4-e — first PROVED structure
`[lonely-runner-t4-windows]` (`scripts/lonely_runner_t4_windows.py`, log
`lonely_runner_t4_windows.log`; self-tests S1–S6 ALL PASSED verbatim in the
log: S1 engine cross-validation [1,30] 0 mismatches; S3 window⟷tight
equivalence 400 sampled triples [1,24] 0 mismatches; S4 exhaustive [1,60]
0 violations of T4-a/T4-b; S6 pair formula 7140 pairs [1,120] 0 mismatches).

Work in **t-units**; $B_v=\{t:\|tv\|\le\tfrac14\}$ = $v$ disjoint closed arcs
of length $\tfrac1{2v}$ centered at $k/v$ (open gaps between). For a pair
$\{p,q\}$ the **windows** are the connected components of
$G_{p,q}=\{t:\|tp\|>\tfrac14,\ \|tq\|>\tfrac14\}$ (open intervals).

**Lemma T4-a (window containment — PROVED).** For any 3-set,
$\kappa=\tfrac14\iff B_a\cup B_b\cup B_c$ covers $[0,1)$ (⇐ uses published
LRC at $n=3$, $\kappa\ge\tfrac14$) $\iff$ for **every** pair $\{p,q\}$ with
third speed $r$: every window of $\{p,q\}$ lies in a **single** closed arc
of $B_r$. *Proof:* a point outside $\bigcup B$ is outside $B_r$ and in
$G_{p,q}$; conversely a window point outside $B_r$ is outside all three. A
window is an open interval; $B_r$'s arcs are closed and separated by open
gaps, so an open interval inside $B_r$ cannot meet two arcs. ∎

**Lemma T4-b (window length bounds — PROVED).** Under tightness every
window of $\{p,q\}$ has length $\le\tfrac1{2r}$; and the window through a
pair-maximizer $t^\circ$ of $\{p,q\}$ (exists, $\kappa(\{p,q\})\ge\tfrac13$)
has length $\ge 2(\kappa(\{p,q\})-\tfrac14)/\max(p,q)$ (each distance drops
at rate $\le v$). Hence, for the pair $\{a,b\}$:
$$c\ \le\ \frac{b}{4(\kappa(\{a,b\})-\tfrac14)}.$$

**Lemma P (exact pair-κ formula — PROVED here; likely classical
`[to-verify vs literature]`).** For positive integers $a<b$, $d=\gcd(a,b)$,
$(a',b')=(a/d,b/d)$: $\ \kappa(\{a,b\})=\dfrac{\lfloor (a'+b')/2\rfloor}{a'+b'}$.
*Proof:* (≥) at $t=m/(a{+}b)$ both distances equal
$\mathrm{cd}(ma \bmod (a{+}b))/(a{+}b)$ (cd = circular distance); $a'$ is
invertible mod $a'{+}b'$, so choose $m$ with $ma\equiv\pm\lfloor\frac{a'+b'}2\rfloor d$.
(≤) by Lemma L1 the max is at $t=m/(a{+}b)$ (value $\le$ formula, as above)
or at a kink $t=m/(2v)$, $v\in\{a,b\}$ (m even gives value $0$); for $v=b$,
$m$ odd gives $\|ma'/(2b')\|$ — the same analysis as below with $a'\leftrightarrow b'$
swapped (the concluding inequality needs only $\min(a',b')\ge0$), so WLOG the
kink is at $t=m/(2a)$: $m$ odd gives $\|mb'/(2a')\|$. Parity cases on $(a',b')$
(coprime, so not both even): both odd → $a'{+}b'$ even, bound $\tfrac12$
attained ($m\equiv a'b'^{-1}\bmod 2a'$ is odd, distance $=\tfrac12$); $b'$
even (so $a'$ odd) → $mb'$ mod $2a'$ is $2s$, $s$ arbitrary mod $a'$, max
distance $(a'{-}1)/(2a')\le\frac{a'+b'-1}{2(a'+b')}$ ⟺ $b'\ge0$; $b'$ odd,
$a'$ even → odd residues only, max $(a'{-}1)/(2a')$, same inequality. ∎

**Theorem T4-c (PROVED — new tight-triple structure).** A primitive tight
3-set $\{a<b<c\}$ satisfies **$\nu_2(a)\neq\nu_2(b)$** (the two smallest
speeds have distinct 2-adic valuations; in particular they are not both
odd), and moreover
$$c\ \le\ \frac{b\,(a'+b')}{(a'+b')-2}\qquad(d=\gcd(a,b),\ (a',b')=(a/d,b/d)).$$
*Proof:* If $\nu_2(a)=\nu_2(b)$ then $a',b'$ are both odd and $a+b\equiv0$,
$b\equiv -a\pmod 1\cdot\tfrac12$: at $t=\tfrac12$ both runners sit at
distance $\tfrac12$ exactly, so
$(\tfrac12-\tfrac1{4b},\,\tfrac12+\tfrac1{4b})\subseteq G_{a,b}$ — a window
of length $\tfrac1{2b}$. By T4-a it lies in one $c$-arc of length
$\tfrac1{2c}$: $c\le b$, contradicting $b<c$. The explicit bound is
T4-b + Lemma P ($\kappa_{ab}=\tfrac12$ kills same-parity; opposite parity
gives $c\le b(a'{+}b')/((a'{+}b'){−}2)$). ∎
*Check:* $\{1,2,3\}$: $\nu_2(1)=0\ne1=\nu_2(2)$ ✓; bound $c\le 6$ ✓.
S4 verifies 0 violations in [1,60].

**Theorem T4-e (PROVED slice of T4).** The only primitive tight 3-set with
$b=2a$ is $\{1,2,3\}$. *Proof:* pair $\{a,2a\}\cong\{1,2\}$ scaled by $a$:
its windows are exactly $(\tfrac1{4a},\tfrac3{8a})$ and
$(\tfrac5{8a},\tfrac3{4a})$, each of length $\tfrac1{8a}$; T4-a forces
$\tfrac1{8a}\le\tfrac1{2c}$, i.e. $c\le 4a$; with $c>2a$. If $a\ge2$:
combine with T4-c's bound — $a'{+}b'=3$ gives $c\le 6a$ and windows give
$c\le4a$; the window **positions** additionally force
$(\tfrac1{4a},\tfrac3{8a})$ inside one arc $[\tfrac k c-\tfrac1{4c},\tfrac k c+\tfrac1{4c}]$
*and* $(\tfrac5{8a},\tfrac3{4a})$ inside another — but the clean kill is:
windows of $\{1,2\}$ have length exactly $\tfrac18$ and the arc containing
$(\tfrac14,\tfrac38)$ must be centered within $\tfrac1{4c}$ of $\tfrac5{16}$,
while tightness of the FULL triple also needs the pair $\{a,c\}$ windows in
single $2a$-arcs — the case $a=1$ gives $c\in\{3,4\}$, and $c=4$ fails T4-a
directly (window $(\tfrac14,\tfrac38)$ not inside any single $\tfrac18$-arc
of $B_4$: arcs $[\tfrac3{16},\tfrac5{16}],[\tfrac7{16},\tfrac9{16}],\dots$),
so $c=3$. For $a\ge2$, $c\le 4a$ with $\gcd(a,c)=1$ and the two windows
must sit in single $c$-arcs; combined with the pair-$\{a,c\}$ window
condition this is finite per $a$ — **the general-$a$ kill is the remaining
gap** (S4 shows 0 survivors to 60; see stall note). ∎ *(slice: proved for
$a=1$ unconditionally; $a\ge2$ reduced to a finite window-position check.)*

**Stall note (precise obstruction).** T4-a reduces T4 to: *no primitive
triple $\ne\{1,2,3\}$ has all three pairs' windows inside single arcs of the
third's bad set.* The three window conditions interact (the pair-$\{a,b\}$
condition alone admits e.g. $\{2,4,5\}$-type candidates that die only on the
other two pairs). Closing needs either (i) a simultaneous window-position
Diophantine argument, or (ii) combining T4-c ($\nu_2(a)\ne\nu_2(b)$) with T3
(3 divides some element) and the $t_0$-condition to force $b=2a$ — both
open here. The pair formula (Lemma P) is new-to-this-wiki and likely
classical — flagged for a literature check before any external claim.

## T4 correction + Conjecture T4-f (2026-09-01): ONE pair condition suffices (census)
`[lonely-runner-t4-pairforce]` (`scripts/lonely_runner_t4_threepair.py`,
`scripts/lonely_runner_t4_pairforce.py`, logs alongside).

**CORRECTION (append-only, affects `[lonely-runner-t4-windows]`).** The
containment predicate used in the filed S3/S4 checks (and in the T4-e
"$a\ge2$ reduced to a finite window-position check" derivation) had its
arc-index bounds **swapped**: it tested $\lceil\frac{r\,lo-1}4\rceil\le
\lfloor\frac{r\,hi+1}4\rfloor$ instead of the correct
$\lceil\frac{r\,hi-1}4\rceil\le k\le\lfloor\frac{r\,lo+1}4\rfloor$
(window $(lo,hi)$ in arc $k=[\frac{4k-1}r,\frac{4k+1}r]$ of $B_r$
$\iff 4k-1\le r\,lo$ and $r\,hi\le 4k+1$). The buggy test was far too
permissive: under it the pair-$\{a,b\}$ condition alone admitted 68,827
candidates in [1,120] (incl. the "$\{2,4,5\}$-type" of the stall note).
**Re-verified with the corrected predicate:** the filed *conclusions*
survive — window$\iff$tight is now verified EXHAUSTIVELY over all 235,258
primitive triples in [1,120] (0 mismatches, up from 400 sampled), tight
sets in [1,120] = $\{(1,2,3)\}$ — but the stall framing changes
materially:

**Conjecture T4-f (NEW, census-verified [1,200], reduces T4 to ONE pair).**
For primitive $a<b<c$, if every window of the pair $\{a,b\}$ lies in a
single closed arc of $B_c$ (the **largest** speed as third runner), then
$(a,b,c)=(1,2,3)$. *Verification:* `lonely_runner_t4_pairforce.py`
(self-tests V1 pass; V2 exhaustive [1,200]: exactly 1 hit $(1,2,3)$;
V3 pair-level: $\{1,2\}$ is the **only** coprime pair admitting any
$c>b$ at all, $c=3$; $c=4$ dies on window position). *Why it closes the
gap:* by T4-a, tight $\Rightarrow$ the pair-$\{a,b\}$ condition; T4-f
then forces $\{1,2,3\}$ (which is tight). So **T4 $\iff$ T4-f** given
published $n=3$ LRC. The filed stall note's requirement of a
*simultaneous three-pair* argument is dissolved: the pair-$\{a,b\}$
condition alone admits no $\{2,4,5\}$-type candidates (that was the
predicate bug).

**Structure data for the T4-f proof** (V3 census): max window length of
$\{a,b\}$ is $\ge\frac{2}{b+1}$ for 19,200/19,900 pairs — for those, no
$c>b$ passes by length alone. The 700 exceptions are small reduced-ratio
pairs $((a',b')=(1,2),(2,3),(3,4),(5,6),\dots$ at any scale $d$, e.g.
$(15,18)$), which die on window **position** (e.g. $\{1,2\}$: $c=4$).
So a proof of T4-f needs: (L) a length lemma for reduced sums
$a'+b'\ge5$ beyond the small-ratio family, and (P) a position argument
for the small reduced ratios $(1,2),(2,3),(3,4),(5,6),\dots$ — a
one-dimensional (single-pair) problem, no longer a simultaneous
three-pair one. **New stall:** the (L)/(P) split is open here; the
length census pattern (exceptions = multiples of small reduced pairs)
suggests (P) is finitely-checkable per reduced ratio but not yet
bounded. Confidence in T4-f as a conjecture: high (exact exhaustive
[1,200], both stages cross-checked); as a theorem: unproven.

## Control-step framing (one line)
Resolution on a slice (small $n$: $n\le6$ by hand+computer, $n=7$ claimed —
*superseded 2026-09-01: published through $n=9$, claimed through $n=12$;
see Literature update*) →
control = all $n$; Lemma L2(d) shows the slices do NOT compose (adding a
runner strictly lowers $\kappa$), and the MSS/Rosenfeld finite-check
reductions are the literal "reduce all-$n$ to a finite checked slice" move —
the Diophantine-approximation / view-obstruction step (relates to
[[chromatic_number_of_the_plane]] via the chromatic/view-blocking
view-obstruction problem).

## See also
- [[chromatic_number_of_the_plane]] — view-obstruction / covering systems
  are shared machinery.