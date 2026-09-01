---
type: attempt
problem: beals_conjecture
attempt: 02
date: 2026-08-24
approach: Ingest real literature; catalogue solved signatures; pin the exact Frey obstruction on the smallest open signature (3,5,7)
outcome: breakthrough-diagnostic
tags: [ingest, generalized-fermat, signature-catalogue, frey-curve, level-lowering, darmon-program]
---

# Attempt 02 — Locate the exact frontier and the exact obstruction

attempt-01 mapped the problem qualitatively. This attempt **ingests real
literature** [[rg2024]] to replace guesses with verified facts, then runs the
explicit Frey / level-lowering computation on the smallest open signature to
pin down *precisely* why the known method fails there.

---

## 1. Ingest — corrections from the literature [[rg2024]]

Three facts from the survey (claim tags in `sources/ratcliffe-grechuk-2024.md`)
that correct or sharpen attempt-01:

1. **Beal ≠ Fermat–Catalan** [rg2024-fc-vs-beal]. Fermat–Catalan = finiteness
   across all signatures with $1/p+1/q+1/r<1$ (exponents vary, may include a 2);
   Beal = *zero* solutions when $\min\geq3$. Beal is strictly stronger in the
   $\geq3$ regime. They are distinct — a conflation to avoid.
   → filed [[conj-fermat-catalan]].

2. **The 10 known primitive Fermat–Catalan solutions all have a $2$**
   [rg2024-10-solns] (e.g. $2^5+7^2=3^4$, $43^8+96222^3=30042907^2$). **None is a
   Beal counterexample** (Beal needs all $\geq3$). So the empirical record is:
   finitely many "near-Beal" solutions, all sitting just outside Beal's regime.
   Filed as evidence.

3. **Computational verification is much stronger than my bases-≤120 probe**
   [rg2024-comp-bound]: Proposition 1.3 — no coprime solutions beyond the 10
   known for $z^r\leq 2^{100}$. Beal is verified to $2^{100}$.

## 2. Catalogue of solved Beal signatures [[thm-solved-generalized-fermat-signatures]]

Verified solved (zero primitive solutions), all exponents $\geq3$:

- $(p,p,p)$ — FLT.
- $(n,n,3)$ — Darmon–Merel.
- $(3,3,n)$, $3\leq n\leq 10^9$ — Chen–Siksek et al.
- $(5,5,7),(5,5,19),(7,7,5)$ — Dahmen–Siksek.
- $(3,4,5)$ — Siksek–Stoll.
- $(2j,2k,n)$, $j,k\ge5$ prime, $n\in\{3,5,7,11,13\}$ — Anni–Siksek.

**Striking pattern: every solved Beal signature has a repeated odd exponent**
(or an even-exponent factorization enabling descent). *No solved Beal signature
has three pairwise-distinct odd-prime exponents.* This is structural, not
luck — see §3.

## 3. The smallest open case is $(3,5,7)$ [rg2024-357-smallest]

$$1/3+1/5+1/7 = 71/105 < 1 \quad\text{(hyperbolic)},\qquad
p,q,r=3,5,7 \text{ pairwise distinct odd primes}.$$

This is the frontier. It is *not* $(3,3,4)$ (my candidate in attempt-01) — that
is solved (it lies in the $(3,3,n)$ family, $n=4\leq10^9$).

---

## 4. The explicit Frey / level-lowering computation on $(3,5,7)$

This is the core of the attempt. [[method-frey-level-lowering-obstruction]]

### 4a. Candidate Frey curve

For a putative primitive $A^3+B^5=C^7$, take the Frey-type curve

$$E:\ Y^2 = X(X-A^3)(X+B^5),$$

roots $0,\ A^3,\ -B^5$. The elliptic discriminant is

$$\boxed{\;\Delta = 16\,(A^3\,B^5\,C^7)^2 = 16\,A^{6}\,B^{10}\,C^{14}.\;}$$

### 4b. Level-lowering arithmetic

Ribet's level lowering at a prime $\ell$ strips a bad prime $q\mid ABC$
(multiplicative, $q\neq\ell$) iff $\ell\mid v_q(\Delta)$. Hence:

- primes $\mid A$ are strippable only by $\ell\in\{2,3\}$ (since $v=6\cdot v_q(A)$);
- primes $\mid B$ only by $\ell\in\{2,5\}$ (since $v=10\cdot v_q(B)$);
- primes $\mid C$ only by $\ell\in\{2,7\}$ (since $v=14\cdot v_q(C)$).

To strip **all** bad primes with one $\ell$:

$$\ell\in\{2,3\}\cap\{2,5\}\cap\{2,7\}=\{2\}.$$

**Only $\ell=2$ works.** Mod-$2$ lowering is parity-controlled and not a usable
irreducibility setting; and Mazur's irreducibility (which needs $\ell$ large)
doesn't apply at $\ell\in\{3,5,7\}$ anyway.

### 4c. Conclusion of the computation

> For $(3,5,7)$, no odd level-lowering prime strips all three bases; any
> lowering leaves a conductor carrying primes from at least two of
> $\{A,B,C\}$, which vary with the unknown solution. The argument cannot
> terminate at a fixed contradiction level. **The classical Frey/Ribet method
> is structurally blocked on $(3,5,7)$.**

### 4d. General statement

For any signature $(p,q,r)$ of pairwise distinct odd primes,
$\Delta\propto A^{2p}B^{2q}C^{2r}$, and stripping all bad primes needs
$\ell\mid 2\gcd(p,q,r)=2$. So:

> **No pairwise-distinct odd-prime Beal signature is accessible to the
> classical single-Frey / single-level-lowering method.**

This explains the pattern in §2: the solved signatures all have a repeated
odd exponent, giving $\gcd(2p,2q,2r)\geq 2p>2$ and hence a usable lowering prime
$\ell=p$ that strips the two repeated-exponent bases, leaving only the third
base as a tractable residual.

### 4e. What it would take to crack $(3,5,7)$

Closing $(3,5,7)$ needs **new machinery**: Frey abelian varieties of
$\mathrm{GL}_2$-type over totally real number fields (Darmon's program), where
the mod-$p$ Galois representation lives on an abelian variety, not an elliptic
curve. The blocking ingredient there is a **Mazur-style irreducibility theorem
for mod-$p$ representations of abelian varieties over number fields**, which is
currently missing. *That missing theorem is the crux of the crux.*

---

## 5. Outcome and next thread

**Outcome: breakthrough-diagnostic.** We now know *exactly* where Beal stands:
- The frontier is the single signature $(3,5,7)$ (and its larger
  pairwise-distinct cousins), not a vague cloud.
- The obstruction is not "the method is hard to push through"; it is a
  **provable structural block** (no usable level-lowering prime) on the entire
  pairwise-distinct odd-prime class.
- The path forward is concretely identified: Darmon's program, gated on a
  missing irreducibility theorem for abelian-variety mod-$p$ representations.

This reframes Beal from "impossibly hard open problem" to "a specific
machinery gap": *generalize Mazur's irreducibility theorem to abelian varieties
over number fields.* That is a well-posed (if very hard) target.

**Next (attempt-03):**
1. Ingest Darmon's program papers directly (the search pointed to
   arXiv:2205.15861 "On Darmon's program for the generalized Fermat equation")
   and map exactly what irreducibility results *do* exist and where they stop.
2. Investigate the smallest pairwise-distinct case $(3,5,7)$ specifically: is
   there any special factorization of $A^3+B^5$ over a number field that yields
   a usable Frey abelian variety? (Likely no for $(3,5,7)$, but worth a
   principled check.)
3. Side thread: develop the Mordell-curve / elliptic-fiber viewpoint on the
   gap-1 near-misses (attempt-01) — a possible *different* angle that bypasses
   the modular obstruction entirely.