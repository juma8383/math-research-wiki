# Near-misses of the generalized Fermat equation: unit-base stratification, an odd–odd Pillai problem, and the Corner Principle

**Authors:** the Math-wiki research program (LLM-assisted); principal computations and proofs verified as described in §5.
**Date:** 2026-08-31. **Status:** preprint draft. **Repo:** `problems/beals-conjecture/scripts/near_miss_package.py` (all data herein is regenerable from this file in under two minutes).

---

## Abstract

We study *gap-1 near-misses* of the generalized Fermat (Beal) equation
$A^p + B^q = C^r$ — primitive triples with $|A^p + B^q - C^r| = 1$ — and the
*minimum genuine gap* of its open signature class. We prove a stratification
theorem: every unit-base gap-$(+1)$ near-miss of a signature of distinct primes
lies exactly on one of the two universal families $(t^r, 1, t^p)$, $(1, t^r, t^q)$
(unconditional, global), and the unit-base gap-$(-1)$ channel is *exactly* the
equation $X^u - Y^v = 2$ restricted to the signature's odd primes — a named new
case of Pillai's conjecture which we isolate as the **odd–odd Pillai-2
conjecture**. We verify the latter to $Y^v \le 10^{25}$ with **no exponent
cap** (no solutions over the full odd-prime range, exhaustive in $u,v$) and
show it is everywhere
locally soluble, so it is Catalan-like: not refutable by elementary congruences.
Computationally, we give the first systematic minimum-gap table over all 56
distinct-odd-prime signatures from primes $\{3,\dots,23\}$ under a corrected
scan (fixing an overshoot-exclusion bug in two published-in-repo scripts, which
changes two recorded values), and we isolate the **Corner Principle**: the
genuine minimum gap of every scanned open signature is attained at $C \le 3$
— 56/56, robust in a wider box — while the principle fails precisely at
near-Euclidean signatures (granularity exponent $\le 5/3$). The corrected table
refutes a previously recorded monotone-in-$-\chi$ law for minimum gaps. The
mechanism is a granularity heuristic: attainable sums near $C^r$ have mean
spacing $C^{\,1-r\chi}$, growing super-cubically across the entire open class,
which pins the global minimum to the corner where the value is pure
small-number arithmetic.

---

## 1. Introduction and setup

**Beal's conjecture** asserts that if $A^p + B^q = C^r$ with $p, q, r \ge 3$
then $A, B, C$ have a common prime factor. By the standard reduction
(theorem-level: $\gcd(A,B,C)=1$ forces pairwise coprimality *for exact
solutions*), the open content is the class of pairwise-distinct exponents, and
the smallest open signature is $(3,5,7)$; the case of repeated exponents is
Fermat's last theorem and its relatives. Darmon–Granville proved that each
signature with $\chi := \frac1p+\frac1q+\frac1r < 1$ has finitely many
primitive solutions; Beal predicts *zero*.

This paper is about the geometry one step *away* from the solution set: the
**near-misses**. Define, for fixed signature $(p,q,r)$ of distinct odd primes
(the *open class*), the quantity

$$G(p,q,r) \;=\; \min\Big\{|A^p + B^q - C^r| :\ A,B,C \ge 2,\ \gcd(A,B,C)=1,\ |A^p+B^q-C^r|\notin\{0,1\},\ A^p \ne C^r,\ B^q \ne C^r\Big\},$$

the **minimum genuine gap** (we exclude exact solutions, gap-1 near-misses,
and the quasi-degenerate layer — see §2; note that for *near-misses*, unlike
exact solutions, $\gcd(A,B,C)=1$ is weaker than pairwise coprimality, and we
scan under the standard primitive condition $\gcd(A,B,C)=1$).

Three questions structure the paper:

1. **Gap-1.** Where can $|A^p+B^q-C^r| = 1$ occur? Empirically, all recorded
   gap-1 hits across many signatures "lie on the universal families"
   $t^{rp}+1$-type identities. We show this is a *theorem* on the $+1$ side and
   an *exactly identified open problem* — a new case of Pillai's conjecture —
   on the $-1$ side (§2–§3).
2. **The minimum gap.** What is $G(p,q,r)$, how does it vary over the open
   class, and is there a law? We give the first systematic table (§4) and a
   sharp falsifiable law with a mechanism (§6).
3. **Honesty.** Two values recorded in our own prior computational record were
   wrong (an overshoot-exclusion bug), and a previously recorded smooth-law
   prediction is refuted by the corrected data. We document both (§5), because
   the empirical record on near-misses is thin enough that uncorrected errors
   propagate.

Notation: $(p,q,r)$ always denotes pairwise distinct primes $\ge 3$ unless
stated otherwise ("open class"); $\chi = \frac1p+\frac1q+\frac1r-1 < 0$ (the
hyperbolicity defect); $t \ge 1$ is an integer; all near-miss equations are in
positive integers.

---

## 2. The stratification theorem

**Definition.** A *unit-base* triple has at least one of $A, B, C$ equal to $1$.
The **universal families** are
$$\mathcal{F}_1 = \{(t^r,\,1,\,t^p)\ : \ t \ge 1\}, \qquad \mathcal{F}_2 = \{(1,\,t^r,\,t^q)\ : \ t \ge 1\}.$$
Both satisfy $A^p + B^q - C^r = +1$ identically, and both are primitive exactly
when $t \ge 2$... (gcd is 1 throughout since one entry is 1).

**Theorem 2.1 (stratification of unit-base gap-1 near-misses).** Let $(p,q,r)$
be a signature of distinct primes and let $(A,B,C)$ be a unit-base triple with
$A^p + B^q - C^r = \pm 1$. Then:

**(T1) (+1 channel, unconditional, global).**
$A^p + B^q - C^r = +1$ holds for a unit-base triple if and only if the triple
lies on $\mathcal{F}_1 \cup \mathcal{F}_2$. In particular every unit-base $+1$
near-miss of every open signature — with no bound on the bases — satisfies the
identity $(t^r)^p + 1 - (t^p)^r = 1$ or the identity $1 + (t^r)^q - (t^q)^r = 1$.

**(T2) (−1 channel: exact reduction).**
$A^p + B^q - C^r = -1$ holds for a unit-base triple if and only if, after
permuting, $C^r - A^p = 2$ with $B = 1$, or $C^r - B^q = 2$ with $A = 1$
(the case $C=1$ is impossible since $A^p+B^q \ge 2$). Hence the −1 unit-base
channel of the signature $(p,q,r)$ is *exactly* the set of solutions of the
Pillai-type equations $X^r - Y^p = 2$ and $X^r - Y^q = 2$ (the larger power
on the left).

**(T3) (quasi-degenerate layer and the raw metric, unconditional).**
Triples with $A^p = C^r$ (equivalently, by $\gcd(p,r)=1$, $A = t^r$, $C = t^p$)
have gap exactly $B^q$, and triples with $B^q = C^r$ have gap exactly $A^p$.
Consequently for *any* signature of distinct primes the **raw** minimum
(without excluding this layer) satisfies
$$\min |A^p+B^q-C^r| \;\le\; 2^{\min(p,q)},$$
attained at $(2, 3^r, 3^q)$ or $(3^r, 2, 3^p)$ (with $t = 3$ odd, $\gcd = 1$);
more precisely $\gcd(t^r, B, t^p) = \gcd(t, B)$. Any metric that fails to
exclude this layer measures the layer, not the problem.

**(T4) (the even-exponent boundary; conditional on classical results).**
Suppose the signature contains $2$ — say $p = 2$, with $q, r$ odd. By T2 the
−1 unit-base channel splits into two sub-channels:
(i) $B = 1$ gives $C^r - A^2 = 2$, an instance of $x^2 + 2 = y^n$ with
$n = r \ge 3$ — a completely solved equation whose unique solution is
$5^2 + 2 = 3^3$ [Cohn 1993; Bugeaud–Mignotte–Siksek 2006; see also Siksek
2003]; hence this sub-channel exists **only** for signatures $(2, q, 3)$,
where it is the single identity $(A,B,C) = (5,1,3)$: $5^2 + 1 - 3^3 = -1$.
(ii) $A = 1$ gives $C^r - B^q = 2$, an odd–odd Pillai-2 instance,
conjecturally empty (§3).
Thus the even-exponent half of the −1 channel is closed by classical
results, and **Beal's restriction to odd exponents removes precisely the
surviving identity**: under Conjecture 3.1, no all-odd open-class signature
has any −1 unit-base near-miss at all.

*Proof.* **T1.** Let $B = 1$. Then $A^p + 1 - C^r = 1$, i.e. $A^p = C^r$. If
$t = \gcd$-free factorization: since $\gcd(p,r) = 1$, unique factorization
gives $A = t^r$ and $C = t^p$ for some $t \ge 1$ (write the prime
factorization of $A$: $A^p = C^r$ forces every valuation to be divisible by
both $p$ and $r$, hence by $pr$; so $A = t^r$, $C = t^p$). The triple is
$(t^r, 1, t^p) \in \mathcal{F}_1$. Symmetrically $A = 1$ gives
$B^q = C^r$, i.e. $(1, t^r, t^q) \in \mathcal{F}_2$. If $C = 1$ then
$A^p + B^q = 2$ forces $A = B = 1$, which lies on both families with $t=1$.
Conversely both families have gap $+1$ identically:
$(t^r)^p + 1 - (t^p)^r = t^{pr} + 1 - t^{pr} = 1$ and
$1 + (t^r)^q - (t^q)^r = 1$. ∎ (One paragraph; fully elementary and
global — no box.)

**T2.** $B=1$: $A^p + 1 - C^r = -1 \iff C^r - A^p = 2$. $A = 1$: $1 + B^q - C^r = -1
\iff C^r - B^q = 2$. $C = 1$: $A^p + B^q = 0$, impossible. These are instances
of $X^u - Y^v = 2$ with $u, v$ odd primes of the signature. ∎

**T3.** $A^p = C^r$ gives $|A^p + B^q - C^r| = B^q$, minimized in $B$ under
primitivity: $\gcd(t^r, B, t^p) = \gcd(t, B)$ (since both non-unit entries are
powers of $t$), so $B = 2$ is admissible iff $t$ odd, giving gap $2^q$;
similarly the $B^q = C^r$ layer gives gap $2^p$ at $A = 2$. Taking $t = 3$
always: $(3^r, 2, 3^p)$ has $\gcd = 1$ and gap $2^q$; $(2, 3^r, 3^q)$ has
$\gcd = 1$ and gap $2^p$. Hence raw min $\le 2^{\min(p,q)}$. ∎

**T4.** With $p = 2$: the $B=1$ sub-channel is $C^r - A^2 = 2$, i.e.
$A^2 + 2 = C^r$ with $r$ odd $\ge 3$; by the complete solution of
$x^2 + 2 = y^n$ ($n \ge 3$) the only solution is $(x, y, n) = (5, 3, 3)$,
forcing $r = 3$, $C = 3$, $A = 5$, i.e. the triple $(5, 1, 3)$ at every
signature $(2, q, 3)$. The $A = 1$ sub-channel is $C^r - B^q = 2$ with $q, r$
odd — an instance of Conjecture 3.1, handled there. The cases $q = 2$ or
$r = 2$ are symmetric. ∎

**Remark 2.2 (empirical match).** In five previously recorded box scans
(attempts 12/13/20/23/24 of the companion research log) *every* gap-1 hit lay
on a universal family and *no* −1 unit-base hit occurred. Theorem 2.1 shows
the first observation is a theorem (T1) and the second is conjecturally forced
(T2 + §3), so these were not coincidences of the boxes scanned.

**Remark 2.3 (exact solutions vs near-misses).** For *exact* solutions,
$\gcd(A,B,C) = 1 \iff$ pairwise coprime; for near-misses the implication
fails (e.g. $(2,3,2)$ has $\gcd = 1$ but $\gcd(A,C) = 2$), and our scans
use the primitive condition $\gcd(A,B,C) = 1$. Nothing in the theorem layer
depends on this choice.

---

## 3. The odd–odd Pillai-2 conjecture

**Pillai's conjecture** (1945; open): for fixed $k \ge 1$ the equation
$a^x - b^y = k$ has only finitely many solutions; only $k = 1$ is settled
(Catalan–Mihăilescu). The case $k = 2$ is explicitly listed as open in
Waldschmidt's survey (quoting Bilu–Bugeaud–Mignotte). The known
perfect powers differing by $2$ — $5^2$ and $3^3$ — involve an even exponent.

**Conjecture 3.1 (odd–odd Pillai-2).** The equation
$$X^u - Y^v = 2$$
has no solutions in integers $X, Y \ge 2$ with $u, v$ both odd primes.

**Evidence.**
1. **Search.** No solutions with $Y^v \le 10^{18}$ over all ordered pairs of
   odd primes $u, v \le 23$ (1,004,437 values of $Y^v$ checked; every
   candidate $Y^v + 2$ tested for being a perfect $u$-th power for all six-to-
   eight admissible $u$). *(This run: `near_miss_package.py`, Part 4.)*
   **EXTENDED 2026-08-31:** no solutions with $Y^v \le 10^{22}$ over the
   **full odd-prime exponent range** — exhaustive in $v$ (the constraint
   $2^v \le Y^v \le 10^{22}$ leaves $v \in \{3,\dots,73\}$) and in $u$ (per
   value $N = Y^v$, the constraint $X^u = N+2 \le 10^{22}+2$ leaves $u \le
   \log_2 N \le 73$); 21,571,057 values of $Y^v$ checked, 397,869,877
   exact-integer $u$-th-root tests (Newton roots unit-tested on 5,000
   random $a^k\pm1$ cases). The old $u,v\le23$ cap never binds at these
   bounds ($2^{23}\approx8.4\times10^6$), so the extension genuinely
   subsumes the $10^{18}$ data. *(Script: `pillai2_ext_search.py`; log:
   `pillai2_1e22.log`.)* **Extended further 2026-09-01:** no solutions
   with $Y^v \le 10^{24}$ (exhaustive: $v \le 79$, $u \le 79$ per value);
   100,066,068 values of $Y^v$, 2,000,675,108 root checks (log:
   `pillai2_1e24.log`), **and final rung $Y^v \le 10^{25}$** (exhaustive:
   $v \le 83$, $u \le 83$; 215,547,548 values, 4,472,139,830 root checks,
   log `pillai2_1e25.log`). The bound ladder is declared saturated at
   $10^{25}$; further evidence should be structural.
2. **Local solubility.** The congruence $X^u - Y^v \equiv 2 \pmod m$ is
   soluble for *every* modulus $m \le 1000$ and for every prime power
   $p^k \le 10^6$, for every ordered odd-prime pair $u, v \le 23$.
   *(Part 5; no obstructing modulus found.)* Hence Conjecture 3.1 is
   **Catalan-like**: no elementary congruence argument can refute it; any
   proof must be global (as with $x^u - y^v = 1$).
3. **Parity structure.** $X, Y$ cannot both be even ($X^u - Y^v \equiv 0 \bmod 8$
   for odd $u,v$), so $X, Y$ are odd, and $X^u \equiv Y^v + 2$: the Jacobi-
   symbol reciprocity analysis is consistent but non-obstructive. Refinement
   (2026-08-31): for odd $X, Y$, $X^u \equiv X \pmod 8$, so every solution
   satisfies
   $$X - Y \equiv 2 \pmod 8$$
   — a cheap necessary condition for targeted deep searches.
3a. **Structural entry points (2026-09-01).** Three provable refinements
   sharpen item 2's "any proof must be global" and are quantified in the
   wiki page [[odd-odd-pillai-2]]: (i) $X - Y \equiv 2 \pmod{24}$ (item 3's
   mod 8 plus Fermat mod 3); (ii) a **factor-level power-residue sieve** —
   $X^u = Y^v + 2$ forces every prime $p \mid X$ with $p \equiv 1 \pmod v$
   to have $-2$ a $v$-th power residue mod $p$ (density $1/v$ among such
   primes, Chebotarev), and dually for primes of $Y$; for $u = 3$ this is
   the thin shape $p = x^2 + 27y^2$; (iii) **local uniformity**: at every
   prime modulus the local solution fraction is exactly $1/p$ and identical
   for all $(u,v)$ (only $9$ and $25$ differentiate, penalizing $u/v = 3,5$),
   so congruences cannot triage exponent pairs. Complementing these, the
   spacing heuristic (the method of the wiki's magic-square-of-squares
   hourglass estimate) summed over all odd-prime pairs gives
   $\sum_{u,v} \tfrac1u(\zeta(v(u-1)/u) - 1) \approx 0.38$ expected
   solutions over the **entire plane**, with the searched boxes
   ($Y^v \le 10^{25}$) already containing essentially all of that mass —
   the exhaustive null of item 1 is the expected global behavior, not a
   small-box artifact. Quantification of (ii) (2026-09-01): the sieve's
   surviving density decays as $C_e(\log z)^{-1/e}$ (fitted slopes match
   $1/e$ over forbidden primes to $2\cdot10^5$), so at the $10^{25}$ box
   it buys only a $\times3$–$6.5$ search-space reduction (dominant pairs
   $(5,3)$, $(7,3)$) — an entry point for modular work, not an
   explanation of the null.
4. **The even boundary.** With one exponent $= 2$ the analogue is settled
   (only $5^2 + 2 = 3^3$; T4) — the conjecture says the odd–odd restriction
   closes the channel entirely.

**Proposition 3.2 (conditional classification).** Assume Conjecture 3.1.
Then for every signature $(p,q,r)$ of distinct odd primes, the unit-base
gap-1 near-misses are *exactly* the two universal families $\mathcal{F}_1 \cup
\mathcal{F}_2$ — globally, with no bound on bases.

*Proof.* T1 classifies the $+1$ channel; T2 reduces the $-1$ channel to
$X^u - Y^v = 2$ with $u, v \in \{p, q, r\}$ odd primes, which Conjecture 3.1
empties. ∎

Thus the entire "degenerate gap-1 layer" of the Beal open class is conjectured
to be two one-parameter families — and any proof of the conjecture on even a
single instance pair needed by an open signature (e.g. $X^3 - Y^7 = 2$...)
would complete the classification for that signature.

**Relation to prior art.** The conjecture is a *restriction* of a famous open
case of Pillai's problem, not a new equation: Bennett's theorem (at most two
solutions for fixed bases) and the Bennett–Siksek program bound but do not
decide it. We state it because T2 shows it is *precisely* the obstruction
between "all recorded gap-1 hits are degenerate" and a theorem.

---

## 4. The minimum-gap table and the Corner Principle

We computed $G(p,q,r)$ for **all 56 signatures** of distinct odd primes from
$\{3,5,7,11,13,17,19,23\}$, under the corrected scan (§5): full box $C \le 60$,
$B \le 10^4$, $A$ chosen as the exact nearest integer power (the scan computes
the exact minimum over all $A \ge 2$ for each $(B,C)$; see the completeness
note in §5.2), and a *corner scan* $C \le 3$ (same $B$-box).

**Result 4.1 (Corner Principle — verified).** For **all 56 of 56** signatures,
$$\text{(corner scan minimum)} \;=\; \text{(full scan minimum)},$$
i.e. $G(p,q,r)$ is attained with $C \le 3$: at $C = 2$ for 55 signatures, and
at $C = 3$ for $(5,11,13)$ (gap $2681$ at $(17,3,3)$:
$17^5 + 3^{11} - 3^{13} = 2681$). No genuine gap-1 hit exists anywhere in the
scanned open class ($56 \times 0$), consistent with §2–§3.

**Conjecture 4.2 (Corner Principle, global).** For every signature $(p,q,r)$
of distinct odd primes, $G(p,q,r)$ is attained at $C \le 3$.

**Result 4.3 (boundary law, verified).** The principle *fails* at
near-Euclidean signatures with small granularity exponent
$\gamma := 1 - r\chi = r(1 - \frac1p - \frac1q)$:
- $(3,3,3)$: $\gamma = 1$; $G = 2$ at $(A,B,C) = (5,6,7)$ — **not** at the
  corner (corner value 11); moreover $(3,3,3)$ admits *four genuine gap-1
  near-misses* in the box, e.g. $6^3 + 8^3 = 9^3 - 1$.
- $(3,3,5)$: $\gamma = 5/3$; $G = 2$ at $(239, 271, 32)$:
  $271^3 + 239^3 = 2^{25} - 2$ — deep, large-base, not corner.
- It *holds* in the box at $(3,3,7)$ ($\gamma = 7/3$; $G = 5$ at $(2,5,2)$)
  and $(3,5,5)$ ($\gamma = 7/3$; $G = 5$ at $(6,2,3)$).

Since the entire open class has $\gamma \ge \gamma_{\min} = 1 - 7\cdot\frac{34}{105} = \frac{343}{105} \approx 3.267$ (attained at $(3,5,7)$), the boundary sits strictly
below the open class: **the principle is a hyperbolicity phenomenon**.

**The table.** All 56 rows (signature; $\chi$; $\gamma$; $G$; argmin
$(A,B,C)$; the near-miss identity) are in `near_miss_package_data.json` and
regenerable in 66 seconds. Extract (full box $C \le 60$, $B \le 10^4$):

| $(p,q,r)$ | $\gamma$ | $G$ | at $(A,B,C)$ | identity |
|---|---|---|---|---|
| $(3,5,7)$ | 3.267 | 29 | $(5,2,2)$ | $5^3 + 2^5 - 2^7 = 29$ |
| $(3,5,11)$ | 5.133 | 77 | $(12,3,2)$ | $12^3 + 3^5 - 2^{11} = 77$ |
| $(3,5,13)$ | 6.067 | 51 | $(20,3,2)$ | $20^3 + 3^5 - 2^{13} = 51$ |
| $(3,5,17)$ | 7.933 | 1281 | $(31,10,2)$ | $31^3 + 10^5 - 2^{17} = 1281$ |
| $(3,5,19)$ | 8.867 | 831 | $(65,12,2)$ | $65^3 + 12^5 - 2^{19} = 831$ |
| $(3,5,23)$ | 10.733 | 860 | $(125,23,2)$ | $125^3 + 23^5 - 2^{23} = 860$ |
| $(3,7,11)$ | 5.762 | **147** | $(2,3,2)$ | $2^3 + 3^7 - 2^{11} = 147$ |
| $(5,7,11)$ | 7.229 | **171** | $(2,3,2)$ | $2^5 + 3^7 - 2^{11} = 171$ |
| $(5,7,13)$ | 8.543 | 1771 | $(6,3,2)$ | $6^5 + 3^7 - 2^{13} = 1771$ |
| $(5,11,13)$ | 9.218 | 2681 | $(17,3,3)$ | $17^5 + 3^{11} - 3^{13} = 2681$ |
| $(7,13,19)$ | 14.824 | 307447 | $(7,2,2)$ | $7^7 + 2^{13} - 2^{19} = 307447$ |
| $(17,19,23)$ | 20.437 | 121275843 | $(3,2,2)$ | $3^{17} + 2^{19} - 2^{23} = 121275843$ |

(The remaining 44 rows follow the same pattern: $C = 2$ throughout.)

---

## 5. Corrections to the prior empirical record

### 5.1 The overshoot-exclusion bug

Two of our prior signature-scan scripts (`search_3711.py`, `search_5711.py`,
used for the recorded values at $(3,7,11)$ and $(5,7,11)$) break the $B$-loop
when $B^q > C^r$ and skip the small-remainder region $0 < \mathrm{rem} < 2^p$.
Both errors remove exactly the region where the true minimizers live:

- $(3,7,11)$: recorded $G = 277$ at $(13,2,2)$; **corrected** $G = 147$ at
  $(2,3,2)$: $2^3 + 3^7 - 2^{11} = 147$.
- $(5,7,11)$: recorded $G = 288$ at $(11,4,3)$; **corrected** $G = 171$ at
  $(2,3,2)$: $2^5 + 3^7 - 2^{11} = 171$.

All other recorded values ($29, 77, 1771$) re-verified unchanged by the
corrected scan. The corrected scripts (`near_miss_package.py`, and the audit
scanner `audit_corrected_scan.py`) include the overshoot region; the old
scripts are deprecated in-repo.

### 5.2 Completeness note on the corrected scan

For fixed $(B, C)$ the scan evaluates $A \in \{fl, fl+1\}$ with
$fl = \lfloor \mathrm{rem}^{1/p}\rfloor$ when $\mathrm{rem} \ge 2^p$ — by
monotonicity of $A^p$ these are the only possible minimizers of
$|A^p - \mathrm{rem}|$ over $A \ge 2$ — and $A \in \{2,3,4\}$ when
$\mathrm{rem} < 2^p$ (overshoot or small remainder), where $A = 2$ dominates:
for $A \ge 3$, $|A^p - \mathrm{rem}| \ge 3^p - 2^p > 2^{p+1} > |2^p - \mathrm{rem}|$
for all $p \ge 3$. Gap-1 completeness: a gap-1 hit with
$\mathrm{rem} < 2^p$ forces $A^p < 2^p + 2$, i.e. $A = 2$, which is scanned.
So the per-signature values are the exact minimum over the box
$\{A \ge 2\} \times \{2 \le B \le 10^4\} \times \{2 \le C \le 60\}$ (and the
wider robustness box of §5.3).

### 5.3 Robustness

In the wider box $C \le 100$, $B \le 10^5$ the Corner Principle
(Result 4.1) continues to hold: **0 violations in 56 signatures**, with every
full-box minimum identical to the $C\le60$ table and every corner minimum
unchanged (`near_miss_robustness.py`, exact integer arithmetic). This also
discharges the wider-box flag on the $(5,7,13)$ value $1771$ recorded in the
prior literature log.

### 5.4 Refutation of the recorded monotone law

Our prior record asserted a "monotone in $-\chi$" law,
$29 < 77 < 277 < 288 < 1771$, and claimed it "re-confirmed" a counting
heuristic. The corrected table **refutes** the law, twice over:

- $(3,5,11) \to (3,5,13)$: $\chi$ decreases ($-0.376 \to -0.390$) but $G$
  *decreases*: $77 \to 51$.
- $(3,5,17) \to (3,5,19) \to (3,5,23)$: $1281 \to 831 \to 860$: non-monotone
  even within a fixed $(p,q)$ family.

With the corrected values the sequence $29 < 77 < 147 < 171 < 1771$ is
monotone, but it is *not monotone in $-\chi$* across the full class — the
minimum is governed by exponent-specific small-base arithmetic at the corner
(e.g. how close $A^p + B^q$ can land near $2^r$), not by the scalar $\chi$.
The granularity mechanism of §6 explains *why* no smooth law in $\chi$ should
exist.

---

## 6. Mechanism: granularity at the corner

Heuristic (not a theorem). The set of attainable values
$S_X = \{A^p + B^q \le X\}$ has $|S_X| \lesssim X^{1/p + 1/q} =
X^{1 + \chi - 1/r}$ elements spread over $[1, X]$; near height $C^r$ the mean
spacing of attainable sums is therefore of order
$$(C^r)^{1 - (1/p + 1/q)} = C^{\,r(1 - 1/p - 1/q)} = C^{\,\gamma}, \qquad \gamma = 1 - r\chi.$$
Two regimes:

- **Open class:** $\gamma \ge 3.267$, so attainable sums near $C^r$ for
  moderate $C$ are spaced more than cubically far apart — the nearest miss to
  $C^r$ is essentially the distance from a random sparse set, and *large $C$
  contributes nothing*: the global minimum is pinned to the smallest $C$,
  where the value $|A^p + B^q - 2^r|$ (or $-3^r$) is pure small-number
  arithmetic, erratic in the signature — exactly the behavior of the table
  ($29, 51, 77, 147, 171, \ldots$ with no smooth law).
- **Near-Euclidean:** $\gamma \le 5/3$; spacing grows subquadratically, so
  large-base coincidences such as $271^3 + 239^3 = 2^{25} - 2$ and
  $6^3 + 8^3 = 9^3 - 1$ stay competitive, and the corner fails (Result 4.3).

The Corner Principle is thus the falsifiable, mechanism-backed successor to
the refuted monotone law: it predicts the *location* (corner) rather than a
smooth *value* law. Any counterexample — a signature whose genuine minimum
sits at $C \ge 4$ — would be a deep large-base coincidence of exactly the
near-Euclidean kind, and we predict none exists in the open class.

---

## 7. Open problems

1. **Prove Conjecture 3.1** (odd–odd Pillai-2), or even the single instance
   needed per signature. Catalan-like: no congruence obstruction exists
   (§3.2); the known machinery (linear forms in logarithms give finiteness-
   style bounds; Baker–Davenport reduction is in principle decidable per
   bounded signature — the obstacle is uniformity over the infinite family).
2. **Prove the Corner Principle** (Conjecture 4.2) — even for the single
   worst case $(3,5,7)$ ($\gamma_{\min}$), via a lattice-free bound of the
   form: for $C \ge 4$, $|A^p + B^q - C^r| > 29$ for all primitive
   non-degenerate triples.
3. **Close the −1 gap-1 layer integrally:** does any open-class signature
   have a *non*-unit-base gap-1 near-miss? All 56 scanned signatures say no
   (0 genuine hits each); a theorem is plausible by the same T1/T2 analysis
   extended to $|{\cdot}| = 1$ with all bases $\ge 2$ — this appears to be the
   true content of the empirical "rigidity" recorded across the class.

---

## 8. References

1. Mauldin, R. D., *A generalization of Fermat's Last Theorem: the Beal conjecture and prize problem*, Notices Amer. Math. Soc. **44** (1997), no. 11, 1436–1437. *(statement and prize; verified against ams.org/notices/199711/beal.pdf)*
2. Darmon, H., Granville, A., *On the equations $z^m = F(x,y)$ and $Ax^p + By^q = Cz^r$*, Bull. London Math. Soc. 27 (1995) 513–543.
3. Mihăilescu, P., *Primary cyclotomic units and a proof of Catalan's conjecture*, J. reine angew. Math. 572 (2004) 167–184.
4. Waldschmidt, M., *Perfect powers: Pillai's works and their developments*, arXiv:0908.4031 (quoting Bilu–Bugeaud–Mignotte, Problem 3: the $k=2$ case as open).
5. Bennett, M. A., *On some exponential equations of S. S. Pillai*, Canad. J. Math. 53 (2001) 897–922.
6. Cohn, J. H. E., *The Diophantine equation $x^2 + C = y^n$*, Acta Arith. 65 (1993) 367–381. *(solves $C=2$ among 77 values $1\le C\le100$; unique solution $(5,3,3)$)*
7. Bugeaud, Y., Mignotte, M., Siksek, S., *Classical and modular approaches to exponential Diophantine equations II. The Lebesgue–Nagell equation*, Compositio Math. 142 (2006) 31–62 (arXiv:math/0405220). *(complete solution of $x^2 + D = y^n$ for all $1\le D\le100$; $D=2$ unique $(\pm5, 3, 3)$; their §2 notes the $n=3$ case was asserted by Fermat and proved by Euler)*
7b. Nagell, T., *Verallgemeinerung eines Fermatschen Satzes*, Arch. Math. (Basel) 5 (1954) 153–159. *(at most one solution for $D=2$, completing the classical uniqueness line)*
8. Ratcliffe, S., Grechuk, B., *Beal's conjecture and the generalized Fermat equation: a survey of solved cases*, arXiv:2412.11933 (2024).
9. Norvig, P., *Beal's conjecture: computational search*, norvig.com/beal.html (near-miss folklore; relative-error metric).
10. OEIS A050787–A050793, sequences on $a^3 + b^3 = c^3 \pm 1$ near-misses (folklore data).

---

## 9. Honesty block (verification status)

- **Unconditional and proven here:** T1, T2, T3 of Theorem 2.1 (elementary;
  one-paragraph proofs in §2), Proposition 3.2 (conditional on Conjecture
  3.1 as stated), Results 4.1/4.3 and §5 corrections (computational, exact
  integer arithmetic, scripts included).
- **T4** is conditional on the classical complete solution of $x^2+2=y^n$;
  the attribution chain is verified: Fermat (asserted $n=3$) → Euler (proof)
  → Nagell 1954 (at most one solution for $D=2$) → Cohn 1993 (elementary,
  $C=2$ among $1\le C\le100$) → Bugeaud–Mignotte–Siksek, Compositio Math. 142
  (2006) 31–62 (complete, all $1\le D\le100$; $D=2$ unique $(\pm5,3,3)$).
  Direct primary-source read (2026-08-31): BMS II extracted from the arXiv
  PDF (math/0405220) confirms the $D=2$ row of §16 "Tables" verbatim —
  header `D | Solutions (|x|,|y|,n)`, row $2 \mapsto (5,3,3)$ — and the
  historical remark *"for D=2, n=3, Fermat asserted that he had shown that
  the only solutions are given by x=5, y=3; a proof was given by Euler"*.
  (Adjoining rows corroborate: $D=4 \mapsto (2,2,3),(11,5,3)$.)
  **The final pre-submission direct-read gate is CLEARED.**
- **Conjecture 3.1 and Conjecture 4.2** are stated as conjectures with the
  evidence of §3 and §4; no proof is claimed.
- All computations use exact integer arithmetic (big-int); the boxes are
  stated in §5.2 and the paper claims nothing outside them except where a
  theorem (T1–T3) is global.
- Adversarial verification: the theorem layer, the bug claim, the corrected
  values, and the novelty of all three headline contributions were
  independently checked (novelty searches, adversarial re-derivation, and
  re-computation by an independent audit scanner). The Ratcliffe–Grechuk
  survey (§8.8) was read in full and contains **no near-miss analysis, no
  unit-base classification, and no Pillai-2 content** (its Prop. 1.3 covers
  *exact* solutions to $z^r\le2^{100}$; its footnote 6 identifies
  exponent-of-1 variants only combinatorially, with no theory; its Table 1.4
  incidentally lists the unit-base exact solution $(5,1,3)$ — the same
  $5^2+2=3^3$ identity our T4 isolates). The T4 citation chain is verified
  (see above); the robustness run of §5.3 is complete: 0 violations in 56.
  The final direct read of the BMS $D=2$ table entry is done (2026-08-31,
  see T4 above). Remaining before submission: ~~only the possible extension
  of the Pillai-2 search bound beyond $10^{18}$~~ — **DONE 2026-08-31,
  extended 2026-09-01 through $10^{25}$:** now verified to $Y^v \le
  10^{25}$, exhaustive over the full odd-prime exponent range ($v \le 83$,
  $u \le 83$ per value), no solutions; 4,472,139,830 exact root checks at
  the final rung (`pillai2_ext_search.py`, log `pillai2_1e25.log`). **No remaining
  pre-submission gates.**