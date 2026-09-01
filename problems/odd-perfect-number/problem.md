# Odd Perfect Number Problem

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/OddPerfect.htm.

## Statement
Does an **odd** perfect number exist? (A positive integer $N$ equal to the
sum of its proper divisors, $\sigma(N)=2N$, with $N$ odd.)

## Status
**OPEN.** Even perfect numbers are completely classified (Euclid–Euler:
$2^{p-1}(2^p-1)$ with Mersenne prime $2^p-1$). No odd perfect number is known.

## Frontier (one line)
*(2026-08-31 hunt-scan update — the earlier "at least 9 distinct prime
factors" was one publication cycle stale, corrected.)* No odd perfect number
below $10^{1500}$ (Ochem–Rao 2012, Math. Comp.); **unpublished maintained
bound $N>10^{2200}$** (Ochem–Rao page, updated 2/2025) `[to-verify]`.
Structural: $\equiv1\pmod{12}$ (Eulerian form $N=p^\alpha m^2$,
$p\equiv\alpha\equiv1\pmod4$); **$\omega(N)\ge10$ distinct prime factors**
(Nielsen 2015, Math. Comp. — supersedes Nielsen 2007's $\ge9$; $\ge12$ if
$3\nmid N$); **$\Omega(N)\ge101$ with multiplicity** (Ochem–Rao 2012;
pushed to $\ge115$ on the maintained page) with the combined constraint
$\Omega\ge\max(115,\,2\omega+51,\,(99\omega-187)/37)$; largest prime factor
$>10^8$.

## Corrections (append-only, 2026-09-01)
1. The Frontier line "$\equiv1\pmod{12}$" was **incomplete**. The correct
   statement (Touchard 1953; proof history below) is the **disjunction**
   $N\equiv1\pmod{12}$ **or** $N\equiv9\pmod{36}$. Lemma O2 below proves it.
2. Common secondary retellings of Descartes' spoof write its pseudo-prime as
   $23\cdot457$; **false**: $23\cdot457=10511$ and
   $22021=19^2\cdot61$ (verified exactly by script, see Census block).
3. The combined constraint $(99\omega-187)/37$ was unattributed. Attribution:
   A. Clayton–J. Hansen, *Integers* **23** (2023), A79
   (arXiv:2303.11974) `[summary]`.
4. The maintained-page figures $10^{2200}$, $\Omega\ge115$, component
   $>10^{1000}$ are upgraded from `[to-verify]` to **verified against the
   maintained page** (P. Ochem's status page, updated 2/2025) — but they
   remain **unpublished** and are not peer-reviewed results.
5. Task-brief error caught during the attack: the Descartes spoof's
   pseudo-prime is $19^2\cdot61$, not $23\cdot457$ (see 2).

## Verified frontier (2026-09-01, primary-verified)
Each item checked against a primary or author-hosted source on 2026-09-01;
flags carried per wiki convention.

| Result | Source (verified 2026-09-01) | Status |
|---|---|---|
| No OPN $<10^{1500}$; $\Omega\ge101$; some component (prime power $p^a\mid N$) $>10^{62}$ | P. Ochem, M. Rao, *Math. Comp.* **81** (2012), 1869–1877, DOI 10.1090/S0025-5718-2012-02589-9 (ams.org landing page) | published |
| $\omega(N)\ge10$ distinct prime factors | P. P. Nielsen, *Math. Comp.* **84** (2015), DOI 10.1090/S0025-5718-2015-02941-x; **Theorem 3.8 verified verbatim** from the author-posted PDF ("Ther e ar e no o dd p erfe ct numb ers with less than 10 distinct prime factors" — extraction artifact `scripts/nielsen_text.txt`) | published |
| $\omega\ge9$; $\omega\ge12$ if $3\nmid N$ | P. P. Nielsen, *Math. Comp.* **76** (2007), 2109–2126, DOI 10.1090/S0025-5718-07-01990-4 | published |
| Largest prime factor $>10^8$ | T. Goto, Y. Ohno, *Math. Comp.* **77** (2008), 1859–1868, DOI 10.1090/S0025-5718-08-02050-4 | published |
| 2nd-largest prime factor $>10^4$; 3rd $>100$ | D. E. Iannucci, *Math. Comp.* **68** (1999), 1749–1760 (DOI 10.1090/S0025-5718-99-01126-6); *Math. Comp.* **69** (2000), 867–879 `[summary]` | published |
| $\Omega\ge2\omega+51$; $\omega\ge115$ under small-prime exclusions | P. Ochem, M. Rao 2014 `[summary]` — exact hypothesis of the 115 statement `[to-verify]` | published |
| Special prime $p< (3N)^{1/3}$ | Acquaah–Konyagin, *Int. J. Number Theory* **8** (2012), 1537–1540 `[summary]` | published |
| Upper bounds $N<2^{4^{\omega}}$-type | Heath-Brown 1994; Nielsen 2003 (*Integers* **3**, A14 — confirmed via Nielsen 2015's reference list); Zelinsky 2019 (IJNT 15, arXiv:1810.11734); Bibby–Vyncke–Zelinsky 2021 (Integers, arXiv:1908.09420) `[summary]` | published |
| $N>10^{2200}$; $\Omega\ge115$; component $>10^{1000}$ | P. Ochem's maintained status page, updated 2/2025 | **unpublished** (page-verified) |
| Touchard congruences $N\equiv1\ (12)$ or $N\equiv9\ (36)$ | J. Touchard, *Scripta Math.* **19** (1953), 35–39 `[summary]`; original proof defective, repaired by Hall 1958 `[summary]`; expository proof E. Lascano, *Math. Magazine* (2011) `[summary]`. **Re-proved below (Lemma O2)** | classical |
| Spoof perfect numbers: Descartes 1638; Dittmer *Math. Comp.* **83** (2014) (DOI 10.1090/s0025-5718-2013-02793-7); BYU spoof group arXiv:2006.10697; Voight negative-base spoof (MASS selecta, AMS 2003); Banks–Güloğlu–Nevans–Saidak CRM Proc. **46** (2008) `[summary]` | published |

2024–2026 preprint wave: searches found several claimed partial results in
preprint only; **none refereed/accepted**; no claimed full proof survived
scrutiny `[summary]`.

## Spoof counterevidence (why this problem resists multiplicative methods)
Descartes (1638, letter to Mersenne) produced
$D=3^2\cdot7^2\cdot11^2\cdot13^2\cdot22021=198585576189$ which is "perfect"
if $22021$ is (falsely) treated as prime. Script-verified exactly:

```
  Descartes spoof D = 198585576189
  spoof sigma (22021 treated as prime) == 2D ? OK
  factor(22021) = {19: 2, 61: 1}
  true sigma(D)/D = 23622/11011 = 2.1453092362  (D abundant: True)
  spoof over-count factor: true/spoof abundancy = 11811/11011
  spoof Euler-form: 22021 mod 4 = 1 (Euler p=1 mod 4), exponent 1 (odd): OK
  spoof D mod 12 = 9, D mod 36 = 9
  spoof passes Touchard congruence: True
  Voight spoof V = -22017975903 (negative base -127)
  spoof sigma(V) == 2V exactly ? OK
```

The spoof **satisfies the Euler form and the Touchard congruences**; only
primality (of $22021=19^2\cdot61$), positivity, and coprimality of the
"primes" separate it from a perfect number. Dittmer and the BYU group
pushed this further (spoofs with $\le5$ prime factors exhaustively studied).
**Lesson:** any proof that uses only multiplicativity of $\sigma$ and the
Euler/Touchard structure is doomed — the control step must invoke genuine
arithmetic (primality, congruence of *values*, size) beyond structure.

## Structural lemmas (proved 2026-09-01; sweeps in `scripts/opn_census.py`)

Throughout: $N$ hypothetical OPN, $\sigma(N)=2N$, $N$ odd,
$N=p_0^{\alpha}m^2$ Euler form with $p_0$ the **special prime**.

### Lemma O1 (2-adic dichotomy; Euler form with clean proof)
**Claim.** For an odd prime $p$ and odd $a$: $v_2(\sigma(p^a))=1$ **iff**
$p\equiv1\pmod4$ **and** $a\equiv1\pmod4$. Consequently an OPN has
$p_0\equiv\alpha\equiv1\pmod4$, and every other prime divisor of $N$ has
even exponent.

**Proof.** $\sigma(p^a)=(p^{a+1}-1)/(p-1)$. If $p\equiv3\pmod4$ and $a$
odd, the $a+1$ (even many) terms $1+p+\dots+p^a\equiv1-1+1-\dots\pmod4$
pair up as $(1+3)\equiv0\pmod4$, so $4\mid\sigma(p^a)$. If $p\equiv1
\pmod4$ then each term is $\equiv1\pmod4$, so $\sigma(p^a)\equiv a+1
\pmod4$, and $v_2=1\iff a+1\equiv2\pmod4\iff a\equiv1\pmod4$. Now
$\sigma(N)=\sigma(p_0^{\alpha})\sigma(m^2)=2N$ with $N$ odd forces
$v_2(\sigma(N))=1$; $\sigma(m^2)=\prod_q\sigma(q^{2c})$ is a product of
odd numbers (each $\sigma(q^{2c})$ is a sum of an odd number of odd
terms), so $v_2(\sigma(p_0^\alpha))=1$, giving $p_0\equiv\alpha\equiv1
\pmod4$. ∎

**LTE form.** For $a$ odd,
$v_2(\sigma(p^a))=v_2(p^{a+1}-1)-v_2(p-1)=v_2(p+1)+v_2(a+1)-1$; setting
this $=1$ re-proves the dichotomy.

**Sweep:** 3322 $(p,a)$ pairs ($p<2000$, odd $a\le21$): 0 mismatches.
**Worked example:** $p=13,\ a=5$: $\sigma(13^5)=1+13+169+2197+28561+
371293=402234=2\cdot201117$, so $v_2=1$, matching $13\equiv1\pmod4$,
$5\equiv1\pmod4$. LTE cross-check: $v_2(13^6-1)-v_2(12)=3-2=1$ ✓.
Counterexample side: $p=5,\ a=9$ ($a\equiv1\pmod4$, fine) vs $p=17,\
a=5$ same; and $p=3,\ a=1$: $\sigma=4$, $v_2=2\ne1$ — correctly fails
since $3\equiv3\pmod4$.

### Lemma O2 (Touchard congruences, with proof)
**Claim.** An OPN satisfies $N\equiv1\pmod{12}$ or $N\equiv9\pmod{36}$.
Refinement: if $3\mid N$ then $9\mid N$.

**Proof.** By Lemma O1, $N=p_0^\alpha m^2$, $p_0\equiv\alpha\equiv1
\pmod4$, so $N\equiv m^2\equiv1\pmod4$ ($m$ odd). Mod 3: if $3\nmid N$,
every $q\equiv2\pmod3$ dividing $N$ has even exponent (else
$3\mid\sigma(q^a)$, forcing $3\mid 2N$ — contradiction), so $N\equiv1
\pmod3$; with $N\equiv1\pmod4$, CRT gives $N\equiv1\pmod{12}$. If
$3\mid N$: $3\equiv3\pmod4$ so $3\neq p_0$, hence $v_3(N)=2c\ge2$, i.e.
$9\mid N$; then $N\equiv9$ or $27\pmod{36}$, and $N\equiv1\pmod4$
selects $N\equiv9\pmod{36}$. ∎

**Refinement (mod-3 inputs).** For $p\equiv2\pmod3$: $3\mid\sigma(p^a)
\iff a$ odd. For $p\equiv1\pmod3$, $p\ne3$: $\sigma(p^a)\equiv a+1
\pmod3$, so $3\mid\sigma(p^a)\iff a\equiv2\pmod3$. Sweep: 5967 pairs,
0 mismatches. **Worked example:** Descartes spoof $D\equiv9\pmod{36}$
(above) — a spoof passes Touchard, consistent with the fence above.

### Lemma O3 (abundancy window + Euler budget)
**Claim.** With $S$ = set of primes dividing $N$ ($|S|=\omega\ge10$) and
$t_p=\sigma(p^{a_p})/p^{a_p}$:

- (i) $\prod_{p\in S}\left(1+\tfrac1p\right)<2$;
- (ii) $\sum_{p\in S}\tfrac1{p-1}>\log 2$;
- (iii) [budget] for **every** choice $p_0\in S$, $p_0\equiv1\pmod4$:
  $\tfrac1{p_0}+\sum_{p\in S,\,p\neq p_0}\left(\tfrac1p+\tfrac1{p^2}\right)<1$;
- (iv) [Euler corollary] $\sum_{p\in S}\tfrac1p<1$.

**Proof.** (i) $t_p\ge1+\tfrac1p$ with strict inequality for $p\mid m^2$
(exponent $\ge2$), and $\prod t_p=2$, $|S|\ge2$. (ii) $t_p<
\tfrac{p}{p-1}$ and $\log t_p<-\log(1-\tfrac1p)=\sum_{j\ge1}\tfrac1{jp^j}
\le\tfrac1{p-1}$; sum: $\log2=\sum\log t_p<\sum\tfrac1{p-1}$. (iii) Put
$u_p=t_p-1=\tfrac1p+\tfrac1{p^2}+\dots+\tfrac1{p^{a_p}}$. For
$p\ne p_0$, $a_p=2c$ so $u_p\ge\tfrac1p+\tfrac1{p^2}$; $u_{p_0}\ge
\tfrac1{p_0}$. And $\prod(1+u_p)=2$ expands to $1+\sum u_p+\dots=2$
with all higher terms positive, so $\sum u_p<1$; the budget sum is $\le
\sum u_p<1$. (iv) $\sum\tfrac1p\le\sum u_p<1$. ∎

**Honesty note (box framing).** The window does **not** bound the largest
prime: for the 9-set $\{3,11,13,17,19,23,29,31,37\}$,
$\prod(1+1/p)=\tfrac{3715891200}{1859834119}=1.99797$ and $\sum\tfrac1{p-1}
=0.9437>\log2$, so adding any prime $P>983.81$ (exact threshold
$P>\pi_{9}/(2-\pi_9)$, script `_window_claim.py`) keeps the 10-set inside
the window. Hence Census A is a census of a **stated box**, not a
classification.

## Census (script `scripts/opn_census.py`, log `scripts/opn_census.log`, run 2026-09-01, total 130.9 s)

Self-tested: $\sigma(6)=\sigma(28)=\sigma(496)=\sigma(8128)=\sigma(33550336)
=2n$ exact; $12,945,22021$ non-perfect; $945=\{3^3,5,7\}$,
$\sigma/n=128/63$ (smallest odd abundant — abundance is cheap, perfection is
not). Census A: all $k$-subsets of odd primes $\le100$ passing window (i)+(ii),
then Euler budget (iii), **exact rational re-check on every survivor**
($\prod\frac{p+1}{p}<2$ exact; $\sum\frac1{p-1}>\log2$ via 25-digit rational
lower bound $6931471805599453094172321/10^{25}$):

```
  --- k=10 (general omega>=10, Nielsen 2015)
  DFS nodes explored: 2060065
  prime-set structures in box passing window (i)+(ii): 589031
  (window,p0) pairs passing window + Euler budget (iii): 2530775
  sum log(1+1/p) over survivors: min 0.469644, max 0.693147  (log 2 = 0.693147)
  smallest prime in a budget-surviving set: 3 ; special-prime values used: [5, 17, 53, 73, 89, 97]
    e.g. S=[3, 5, 7, 67, 71, 73, 79, 83, 89, 97] p0=5 budget=764965958354335078284427397651/852029175000474374729128432605 (= 0.897817)
    e.g. S=[3, 5, 7, 67, 71, 73, 79, 83, 89, 97] p0=97 budget=41183328384230259977431692583/43919029639199710037583939825 (= 0.937710)
  min-prime distribution of window survivors: [(3, 523832), (5, 65199)]
  exact rational re-check of window on float survivors: 589031/589031 pass

  --- k=12 with 3 !| N (Nielsen 2007)
  DFS nodes explored: 896483
  prime-set structures in box passing window (i)+(ii): 255402
  (window,p0) pairs passing window + Euler budget (iii): 1473637
  smallest prime in a budget-surviving set: 5 ; special-prime values used: [5, 13, 17, 53, 89, 97]
    e.g. S=[5, 7, 11, 13, 17, 19, 23, 53, 79, 83, 89, 97] p0=5 budget=1927169287836863584083410108644599/2488768288076408264427254502794045 (= 0.774347)
  min-prime distribution of window survivors: [(5, 255402)]
  exact rational re-check of window on float survivors: 255402/255402 pass
```

Census B — independent $\sigma$-sieve over all odd $n\le10^7$ (numpy
`sig[i::2*i] += i` over odd divisors), self-tested against exact $\sigma$
on 500 random odd $n$ (0 mismatches) and against the known even perfects:

```
  odd n <= 10000000 with sigma(n) == 2n : 0  (none)
  odd n <= 10000000 in Touchard classes (1 mod 12: 833334, 9 mod 36: 277778) = 11.11%
  sieve vs exact sigma on 500 random odd n: OK (0 mismatches)
```

**Reading.** The abundancy window + Euler budget leave **589031 prime-set
structures** (k=10 box) and **2530775 (window, p0) pairs** alive in the box —
elementary constraints alone are far from excluding existence (consistent
with the spoof fence: spoofs pass all of these). Max in-box budget observed
$0.9377$ (p0=97 in the example set) — the budget is close to saturated,
which is the quantitative hook for direction D1.

## Candidate directions (opened 2026-09-01; ≥3 per protocol)
- **D1 — Budget refinement.** (iii) uses only $1/p+1/p^2$; for $p\mid m^2$
  with $c\ge2$, $u_p\ge\frac1p+\frac1{p^2}+\frac1{p^3}+\frac1{p^4}$, and
  $u_{p_0}\ge\frac1{p_0}+\frac1{p_0^2}$ if $\alpha\ge5$. Re-running the
  census with the strengthened budget should kill the boundary sets
  (budget $\to0.9377$ max) — cheap, exact, mechanical.
- **D2 — Factor-chain exclusion (Ochem–Rao roadblocks).** Use Census A's
  surviving small-prime sets as branching skeletons and run the
  branch-and-bound over *exponent chains* (per Ochem–Rao 2012), targeting
  the Touchard class $N\equiv9\pmod{36}$ (3-branch) which Census B shows is
  the sparser class (277778 vs 833334 of odds $\le10^7$).
- **D3 — Spoof fence.** Any candidate attack must use more than
  multiplicativity; the discriminating invariants on spoofs are primality
  of pseudo-primes ($22021=19^2\cdot61$), positivity (Voight's negative
  base), and coprimality. Seek an invariant that is (a) spoof-robust and
  (b) still restrictive on real $N$ — the current lemmas are NOT
  spoof-robust enough to be the control step.
- **D4 — Euler-form size line (Dris/Sorli).** Conjecture $p_0^{\alpha}<m^2$
  (Dris) / $\alpha=1$ (Sorli): test whether (ii)+(iii) within the census box
  can *force* $\alpha=1$ for budget-surviving $(S,p_0)$ pairs (the special
  primes used, $[5,17,53,73,89,97]$, all appear with small $p_0$ budget
  slack $<0.11$ — quantitative handle).

## Confidence re-evaluation (2026-09-01)
- Existence of an OPN: judged **very unlikely** (unchanged by this attack);
  every elementary structural axis (2-adic, mod-3, abundancy, budget) is
  satisfiable on spoofs — the wall is exactly the control step, matching
  the wiki-wide 6-for-6 pattern.
- Lemmas O1–O3: high confidence — elementary proofs above + 9289 swept
  $(p,a)$ pairs with 0 mismatches + exact rational census checks.
- Census counts: exact within the stated box (all survivors stored and
  re-checked rationally; no float-only claims filed).
- `[to-verify]` items: Ochem–Rao 2014 exact 115-hypothesis; 2024–26
  preprint details.

## Control-step framing (one line)
Resolution on a slice (none below $10^{1500}$; ever-tightening structural
constraints) → control = a global nonexistence proof (or a single existence) —
the slice→full control wall; the open content is bounding the *Euler form*
$N=p^\alpha m^2$ (with $p\equiv\alpha\equiv1\pmod4$) away from existence.

## See also
- [[abc_conjecture]] — multiplicative/rad-type control on $\sigma(N)/N$.