# Grimm's Conjecture

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/GrimmsConjecture.htm.

## Statement
For any run of $n$ consecutive composite integers $m{+}1,\dots,m{+}n$, there
exist $n$ **distinct** primes $p_1,\dots,p_n$ with $p_i\mid(m+i)$.

## Status
**OPEN.** (Grimm 1969.)

## Frontier (one line)
Verified for large ranges; the all-runs statement is open. Weaker: the
count of distinct prime divisors of $\prod(m+i)$ is $\ge n$ is known (and
not enough — distinctness of the assignment is the gap).

**Unconditional range (verify-wave CONFIRMED against primary, 2026-08-31):**
**Laishram–Shorey 2006** (*International J. Number Theory* 2, no. 2 (2006)
207–211, DOI 10.1142/S1793042106000498) `[summary]`: Grimm holds for all runs with
$n\le p_{N_0}$ where $N_0=8.5\times10^8$ and $p_{N_0}=19\,236\,701\,629
>1.9\times10^{10}$ — method: **Hall's marriage theorem** (explicitly) +
Sylvester–Erdős reduction + verified $p_{N+1}-p_N-1<(\log p_N)^2$ up to
$N_0$. Corollary: $\omega\big(\prod(m+i)\big)\ge k$ for those runs.

**k-smooth reduction + census literature (verify-wave: novelty of a
2026-08-31 scan census KILLED — prior art):** since any prime factor
$\ge k$ of a run entry is automatically distinct, **only $k$-smooth
composites need analysis** — reduction due to **Jan van Delden**
(primepuzzles.net/puzzles/puzz_430.htm, tested to $10^8$; C. Rivera
extended the failure-free scan to $10^9$; T. D. Noe did explicit
bipartite matching in Mathematica, validating the 71-composite gap
31397–31468). Hands (UTA thesis 2022) formalizes the Hall-violation
characterization. A session census to $2\times10^6$ (148,931 runs, 0
matching failures, 11,409 $k$-smooth positions; script
`scripts/grimm_census.py`) is a **corollary of known results** (the
Laishram–Shorey hall-proof range dwarfs it) and is kept only as a
correctly-attributed reproduction: its true $k$-smooth first-occurrence
list is **8, 9 (run 8–10); 16 = 2⁴ (run 14–16); 24, 25, 27 (run
24–28); 32; 36; …** with $k$ = run *length* $q-p-1$ (criterion
$\max_i\{$prime factors$\}\le$ length). An earlier scan wording
("first occurrences 8, 24, 25, 27") skipped 16 and mis-described the run
— corrected. Grimm $\Rightarrow$ Legendre via Erdős–Selfridge: standard
published remark, retained `[to-verify]`.

## Control-step framing (one line)
Resolution on slices (verified ranges; counting lower bounds) → control = a
perfect matching of primes to positions for *all* runs — a Hall's-condition
/ assignment control step (pointwise matching, not average count).

## See also
- [[collatz_conjecture]], [[goldbach_conjecture]] — average/count → pointwise
  control family.