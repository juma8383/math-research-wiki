# Attempt 07 — Exponent-word sieve for positive Syracuse cycles

> **Provenance:** external AI session (GitHub Copilot), produced 2026-09-02;
> integrated into the wiki by Claude **after independent verification**
> (see §V below — probe re-run + normalization check reproduced exactly,
> `scripts/copilot_probe_replay.py` + `.log`). Status upgraded `to-verify`
> → **verified (probe + lemma)** on the two computational claims; literature
> figures remain `[summary, to-verify]` where flagged. The attack does NOT
> claim a proof; outcome **partial**. Date: 2026-09-02.

## Scope and assumptions

Work only with positive odd integers and the accelerated Syracuse map
$T(n)=\dfrac{3n+1}{2^{v_2(3n+1)}}$.

This attack addresses only **nontrivial positive cycles**. It does not
address divergent trajectories. All computational claims below concern
finite bounded searches and are not evidence of global convergence.
(Provenance note: the affine cycle identity below is **classical** — it is
the standard formula underlying every cycle-exclusion paper since Steiner;
the attempt's new content is the bounded probe, the divisibility-vs-replay
distinction, and the cyclic-normalization bound of §5.)

## 1. Verified base

Let a hypothetical odd cycle have odd entries $(n_0,\ldots,n_{k-1})$,
indices mod $k$, and put
$a_i=v_2(3n_i+1)\ge1$, $A_j=\sum_{i<j}a_i$, $A=A_k$.
Iterating $2^{a_i}n_{i+1}=3n_i+1$ gives the exact identity

$$(2^A-3^k)\,n_0=S(a_0,\ldots,a_{k-1}),\qquad
S=\sum_{j=0}^{k-1}3^{k-1-j}\,2^{A_j}.$$

Because $S>0$ and $n_0>0$, necessarily $2^A>3^k$, i.e. $A>k\log_2 3$.
Conversely an exponent word $a$ can encode a positive odd cycle only if:

1. $D=2^A-3^k>0$;
2. $D\mid S$, so $n_0=S/D$ is integral;
3. replaying the recurrence gives odd integers at every step with the
   exact claimed valuations;
4. the replay returns to $n_0$.

**The divisibility condition is necessary but not sufficient** — exact
valuation replay is load-bearing (spurious words exist otherwise).

## 2. Counterevidence and hazards

- Cycle exclusion does not prove Collatz: a divergent positive trajectory
  is a separate failure mode (the wiki's (a)/(b) split).
- The analogous statement over all integers is false: negative cycles
  exist; positivity is essential.
- Treating the $a_i$ as independent geometric random variables is a
  heuristic, not a pointwise proof; conditioning on survival can destroy
  the apparent negative drift (the wiki's average-vs-pointwise wall).
- Bounding $A-k\log_2 3$ alone cannot enumerate all words: $A$ has no
  established absolute upper bound for a hypothetical cycle.
- $D\mid S$ alone admits spurious words unless exact valuations are
  replayed.

## 3. Three distinct directions

**A. Arithmetic exponent-word sieve.** For fixed $(k,A)$ enumerate
compositions of $A$ into $k$ positive parts; reject by $D\nmid S$, then
replay exact valuations. The immediate research target is not brute-force
extension but a proof that admissible words occupy sharply restricted
residue classes modulo selected primes dividing $D$.
*Break test:* words with large isolated $a_i$ make the prefix powers
$2^{A_j}$ sparse and can evade low-modulus filters; any density estimate
must be uniform in such lopsided compositions.
*Confidence:* high for the identity and finite sieve; low that
divisibility alone scales to a global theorem.

**B. Product/logarithmic rigidity.** Multiplying $2^{a_i}n_{i+1}=3n_i+1$
around the cycle:

$$2^A=3^k\prod_{i=0}^{k-1}\Bigl(1+\frac1{3n_i}\Bigr),\qquad
0<A\log2-k\log3=\sum_i\log\Bigl(1+\frac1{3n_i}\Bigr)<\frac13\sum_i\frac1{n_i}.$$

With $m=\min_i n_i$: $0<A\log2-k\log3<k/(3m)$ — a hypothetical cycle
forces $(A,k)$ to be an exceptionally good rational approximation to
$\log_2 3$. Continued fractions then force large $k$ once a lower bound
for $m$ is imported from verified computation.
*Break test:* the inequality is weak without a large $m$ lower bound; a
huge cycle-length lower bound stays silent about divergence.
*Confidence:* high as a cycle-control mechanism; zero as a convergence
argument. **(Wiki note: this is exactly the Simons–de Weger/Hercher
mechanism — see the m≤91 update in progress.md; the attempt independently
re-derives its shape.)**

**C. Reverse-tree / residue-cover descent.** For odd target $y$, odd
predecessors have the form $x=(2^a y-1)/3$ with parity of $a$ determined
by $y\bmod 3$. Build finite residue classes mod $2^r3^s$ with certified
descent words; a complete finite cover would prove every orbit reaches a
smaller integer.
*Break test:* residue classes split indefinitely at the boundary — a
certificate valid mod $2^r3^s$ may lose descent after lifting because the
affine constant changes. **This is the control-step obstruction verbatim:
average contraction does not provide a uniform pointwise descent
certificate** [[method-average-vs-pointwise-control]].
*Confidence:* medium for larger certified covers; low for finite closure
without a compactness/monotonicity lemma.

## 4. Computational probe (independently re-run — verified)

Enumerated every positive composition with
$1\le k\le9$, $\lfloor k\log_2 3\rfloor+1\le A\le\lfloor k\log_2 3\rfloor+9$:
**1,119,904 exponent words**, each checked for $D\mid S$ and full exact
valuation replay.

| k | min A | words | integral | exact cycles | nontrivial |
|---|---|---|---|---|---|
| 1 | 2 | 9 | 1 | 1 | 0 |
| 2 | 4 | 63 | 1 | 1 | 0 |
| 3 | 5 | 282 | 1 | 1 | 0 |
| 4 | 7 | 1,350 | 1 | 1 | 0 |
| 5 | 8 | 4,347 | 1 | 1 | 0 |
| 6 | 10 | 18,480 | 1 | 1 | 0 |
| 7 | 12 | 77,190 | 1 | 1 | 0 |
| 8 | 13 | 202,995 | 1 | 1 | 0 |
| 9 | 15 | 815,188 | 1 | 1 | 0 |

The sole exact cycle in each row is a repeated coding of the trivial odd
cycle $1\mapsto1$. **Bounded sanity check only** — proves nothing about
words outside the stated $(k,A)$ region. *(Independent re-run
`scripts/copilot_probe_replay.py`: all counts reproduced exactly,
2026-09-02.)*

## 5. New partial lemma: cyclic normalization (verified numerically)

A cycle has $k$ cyclic rotations of its exponent word. Rotate so the
cumulative discrepancy $\Delta_j=A_j-jA/k$ starts at a cyclic minimum
(equivalently: start at the argmin of the cyclic partial sums). Then all
prefix discrepancies satisfy $\Delta_j\ge0$ (direct: every other prefix
sum is $\ge$ the chosen minimum; the cycle-lemma citation is a stronger
statement than needed). Since $A/k>\log_2 3$,

$$2^{A_j}\ge2^{jA/k}>3^j\quad(1\le j<k),$$

and substitution into $S$ gives the strict bound $S>\sum_{j=0}^{k-1}3^{k-1-j}3^j
=k3^{k-1}$, hence for this normalized rotation

$$n_0=\frac{S}{2^A-3^k}>\frac{k\,3^{k-1}}{2^A-3^k}.$$

*Verification:* the re-run script checks both properties exhaustively over
all 1,119,895 words with $k\ge2$ in the probe box — **0 prefix-discrepancy
violations, 0 bound violations** (ties/periodic words included: choosing
the first argmin still forces all $\Delta_j\ge0$).

*Honest limits:* valid but presently too weak — the denominator
$2^A-3^k$ can be huge when $A-k\log_2 3$ is uncontrolled. Its value is
structural: **the decisive control variable is exactly the near-resonance
gap $A\log2-k\log3$**, which continued-fraction methods already exploit
(Sinisalo's table of best upper approximations to $\log_2 3$; the
semi-convergent 114,208,327,604/72,057,431,991 gives the "first candidate"
cycle shape with 72,057,431,991 odd steps, requiring verification to
$\approx4.36\times10^{21}$ to exclude `[summary, to-verify]`).

## 6. Simpler and more general formulations

- **Sharper frontier:** exclude a nontrivial positive cycle for words with
  $A-k\log_2 3\le C/k$ by combining the normalized-prefix estimate with a
  continued-fraction gap — isolates the near-resonant case where cycles
  are most plausible.
- **Generalization:** for $T_q(n)=(qn+1)/2^{v_2(qn+1)}$, odd $q\ge3$:
  $(2^A-q^k)n_0=\sum_j q^{k-1-j}2^{A_j}$. The obstruction persists:
  arithmetic resonance controls cycles; pointwise control of divergent
  trajectories is separate. Comparing $q$ values where divergence is
  computationally common may reveal which descent lemmas are special to
  $q=3$.

## 7. Next concrete deductions

1. Prove the cyclic-normalization lemma in full formality (ties and
   periodic words — numerically clean here; a written proof is short).
2. Replace raw composition enumeration with dynamic programming for
   $S\bmod D$ grouped by prefix-sum residues — reaches larger $k$ without
   exponential duplicate work.
3. For each surviving residue state, track an interval bound on the
   reconstructed $n_i$; prune states forcing an even iterate or violating
   exact valuation.
4. Keep cycle and divergence claims in separate ledgers (the wiki's (a)/(b)
   split, unchanged).

## 8. Honesty / confidence

- Exact affine cycle identity: 0.99 (classical; verified).
- Bounded computation as reported: 0.98 → **1.0 after independent re-run**.
- Cyclic-normalization lower bound: 0.85 → **~0.99 numerically** (all words
  in the box); written proof with tie handling still to be typeset.
- Exponent-word sieve producing a materially stronger finite cycle bound: 0.45.
- Any route here proving full Collatz convergence without a new uniform
  control lemma: 0.05.
- **No claim in this attempt is a proof of the Collatz conjecture.**

## 9. Verification record (this wiki, 2026-09-02)

- Probe re-run: `scripts/copilot_probe_replay.py` + `.log` — table counts
  reproduced exactly (1,119,904 words; per-row integers/cycles/nontrivial
  identical).
- Normalization lemma: 0 prefix-discrepancy violations, 0
  $S>k3^{k-1}$ violations over all 1,119,895 $k\ge2$ words in the box.
- Literature: **Hercher 2023 (J. Integer Seq. 26 (2023), Art. 23.3.5): no
  $m$-cycles for $m\le91$** — improves the wiki's filed $m\le75$
  (Simons–de Weger 2010); uses $X_0=695\cdot2^{60}$; continued-fraction
  machinery of exactly the §3-B shape. Filed as an append-only frontier
  update in progress.md. Wang 2026 Zenodo preprints claiming $m\le93$/$94$
  = unreviewed, flagged `[collatz-recent-claims-unverified]`.
- The "recently published computational frontier $\approx2^{71.02}$" figure
  cited by the Copilot session: **not confirmed to that precision** — the
  search-surfaced verification bounds are $695\cdot2^{60}\approx2^{69.44}$
  (Hercher's input) and the project-reported $2^{71}$ (already flagged
  `to-verify` in progress.md). Kept `[to-verify]`.