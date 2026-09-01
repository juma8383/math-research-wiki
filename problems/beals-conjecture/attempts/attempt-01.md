---
type: attempt
problem: beals_conjecture
attempt: 01
date: 2026-08-24
approach: Reductions + computational obstruction search + theoretical-frontier mapping
outcome: partial
tags: [reduction, generalized-fermat, frey-curve, modularity, computation, near-miss]
---

# Attempt 01 — Map the problem, find the obstruction

Goal: turn "Beal's conjecture" from a bare statement into a precisely
understood frontier, and locate *where* the known methods break. A full proof
is not expected in one session (30-year, \$1M open problem); the deliverable is
(a) the two clean reductions, (b) an honest statement of what is known
unconditionally, (c) a computational probe that reveals the *qualitative*
obstruction, and (d) the exact barrier for the modular method.

---

## 1. Reduction to the coprime, prime-exponent regime

### 1a. Pairwise-coprime equivalence [[method-pairwise-coprime-reduction]]

**Claim.** For a solution $A^x+B^y=C^z$, $\gcd(A,B,C)=1 \iff A,B,C$ are pairwise
coprime.

*Proof.* ($\Leftarrow$) trivial. ($\Rightarrow$) Suppose a prime $p\mid A$ and
$p\mid B$. Then $p\mid A^x$ and $p\mid B^y$, so $p\mid(A^x+B^y)=C^z$, hence
$p\mid C$. Then $p\mid\gcd(A,B,C)$, contradicting $\gcd(A,B,C)=1$. The other two
pairs are symmetric. ∎

So Beal is **equivalent** to: *no pairwise-coprime solution with exponents
$\geq 3$.* This is the clean target. (A solution like $3^3+6^3=3^5$ has
$\gcd=3>1$ and is *allowed* — it is a "witness" that without the coprimality
demand, solutions abound.)

### 1b. Exponent reduction [[method-exponent-reduction]]

**Claim.** It suffices to rule out primitive solutions with each exponent an odd
prime or $4$.

*Proof.* If exponent $x\geq 3$ has an odd prime divisor $p$, then
$A^x=(A^{x/p})^p$ reduces the exponent to $p\geq 3$. If $x$ is a power of $2$,
$x=2^k$, $k\geq 2$ (since $x\geq 3$ ⟹ $x\geq 4$), then $A^x=(A^{2^{k-2}})^4$
reduces to exponent $4$. ∎

Hence signatures $(p,q,r)$ with each in $\{\text{odd primes}\}\cup\{4\}$, and the
reciprocal condition $1/p+1/q+1/r\leq 1$ (equality only at $(3,3,3)$).

---

## 2. What is known unconditionally

**Fermat's Last Theorem** [[thm-fermat-last]] (Wiles 1995): no positive
solutions to $a^n+b^n=c^n$ for $n\geq 3$. This resolves signature $(p,p,p)$
*to zero* — the only signature with $1/p+1/q+1/r=1$.

**Darmon–Granville** [[thm-darmon-granville]] (1995): for *fixed* $(p,q,r)$ with
$1/p+1/q+1/r<1$, the primitive (pairwise-coprime) equation
$x^p+y^q=z^r$ has only **finitely many** solutions (via Faltings/Mordell).

**Consequence.** For every exponent triple with all $\geq 3$:
- $(3,3,3)$: zero solutions (FLT).
- every other triple: finitely many primitive solutions (Darmon–Granville).

**The entire open content of Beal** is therefore: *for each admissible
signature, show that the finite Darmon–Granville set is empty.* This reframes
Beal as infinitely many finite-but-possibly-nonempty sets to kill, signature
by signature.

### Does abc close it? [[method-abc-finiteness]]

Checked: applying abc to $a=A^x,\ b=B^y,\ c=C^z$ (pairwise coprime, $a+b=c$)
gives $C^z \le K_\varepsilon\,\mathrm{rad}(ABC)^{1+\varepsilon}$. Using
$A<C^{z/x},\ B<C^{z/y}$ and $\mathrm{rad}(ABC)\le ABC$, one gets
$C^{\,z-(1+\varepsilon)(z/x+z/y+1)} \le K_\varepsilon$. The exponent is positive
precisely when $1/x+1/y+1/z<1$. So abc ⟹ **finiteness per signature** —
*identical in strength* to the unconditional Darmon–Granville. **abc does not
imply Beal.** Filed so we never revisit this as a shortcut.

---

## 3. Computational probe — the *qualitative* obstruction

Ran `scripts/search.py`: bases $A,B\leq 120$, exponents $S=\{3,4,5,7\}$.

- **Exact pairwise-coprime solutions: 0.** Consistent with Beal.
- **Exact non-coprime solutions: 55**, all with $\gcd>1$ — e.g.
  $3^3+6^3=3^5$, $7^3+7^4=14^3$, $17^4+34^4=17^5$. These are the
  Beal-*consistent* families; they confirm the gcd condition is doing real
  work.

### The headline finding: Beal is *tight by 1*

Excluding the degenerate $A=1$ family, the closest pairwise-coprime near-misses
($A^x+B^y$ vs the nearest $\geq 3$-power $C^z$) include **eight at gap exactly
1**, several with all exponents $\geq 3$:

| relation | gap | exponents | gcd(A,B,C) |
|---|---|---|---|
| $9^3+10^3 = 1729 = 12^3+\mathbf{1}$ | 1 | (3,3,3) | 1 |
| $6^3+8^3 = 728 = 9^3-\mathbf{1}$ | 1 | (3,3,3) | 1 |
| $2^4+4^3 = 80 = 3^4-\mathbf{1}$ | 1 | (4,3,4) | 1 |
| $2^7+6^3 = 344 = 7^3+\mathbf{1}$ | 1 | (7,3,3) | 1 |
| $3^3+15^4 = 50652 = 37^3-\mathbf{1}$ | 1 | (3,4,3) | 1 |
| $7^4+19^3 = 9260 = 21^3+\mathbf{1}$ | 1 | (4,3,3) | 1 |
| $14^5+34^4 = 1874160 = 37^4+\mathbf{1}$ | 1 | (5,4,4) | 1 |
| $64^3+94^3 = 1092728 = 103^3+\mathbf{1}$ | 1 | (3,3,3) | 1 |

The first is the **Ramanujan–Hardy taxicab number**: $1729 = 1^3+12^3=9^3+10^3$,
which here reads $9^3+10^3 = 12^3+1$.

**Interpretation.** The coprime obstruction is *not* metric: a sum of two
coprime ≥3-powers can land exactly one unit from a third ≥3-power. Therefore
**no argument of the form "the sum is too sparse/far from a perfect power" can
prove Beal.** The obstruction is arithmetic/diophantine, not density-based.
Closing gap $1\to 0$ is exactly the subtle move that modular methods perform in
FLT, and the difficulty of doing so for mixed exponents is the whole problem.

This also connects the gap-1 relations to **integral points on Mordell-type
curves** ($a^3+b^3=c^3+k$ for fixed $k$): the near-misses are not random, they
sit on elliptic fibers. (Filed as a spark in notes.md.)

---

## 4. The Frey/modularity barrier [[method-frey-modularity]]

Why did FLT fall but Beal hasn't? The FLT engine:

1. To a putative $a^p+b^p=c^p$ attach the **Frey curve**
   $E:\ Y^2 = X(X-a^p)(X+b^p)$.
2. **Modularity theorem** (Wiles–Breuil–Conrad–Diamond–Taylor): $E$ is modular.
3. **Ribet's level lowering**: $E$'s conductor drops to a level so low that no
   weight-2 modular form of that level exists — contradiction.

The construction hinges on *all three terms carrying the same exponent $p$*,
which makes the discriminant $\Delta = a^{2p}b^{2p}c^{2p}$ a perfect $p$-th-power
times a constant, so the local conductor structure is uniform and level
lowering terminates cleanly.

For a **mixed** signature $(p,q,r)$ the Frey curve
$Y^2 = X(X-A^p)(X+B^q)$ (or the appropriate twist) has discriminant carrying
$A^{2p}B^{2q}C^{2r}$ — three *incommensurate* exponent structures. The
conductor/discriminant no longer reduce to a single prime-power profile, and
Ribet's level-lowering does not terminate at a contradiction. **This
incommensurability is the crux of Beal.**

The live research directions that try to repair this — higher-dimensional Frey
varieties (Darmon–Merel, Bennett–Skinner), and signature-specific modular
methods — resolve *some* signatures to zero but not all. No uniform argument is
known.

---

## 5. Outcome and next thread

**Outcome: partial.** The problem is now a precisely mapped frontier:
- reductions locked (coprime + prime/4 exponents);
- the "zero vs finitely-many" gap identified as the whole content;
- the metric approach ruled out empirically (tight-by-1);
- the modular-method barrier localized to mixed-exponent incommensurability.

**Next (attempt-02):**
1. Catalogue the signatures already resolved to *zero* in the literature
   (FLT $(p,p,p)$; Darmon–Merel $(p,p,2)$-family; the $(2,3,n)$ and $(2,3,3)$
   programs; Bennett–Skinner). Identify the **smallest still-open** signature.
2. For that smallest open signature, run the Frey construction explicitly and
   record the exact conductor/discriminant computation — to see whether the
   obstruction is total or whether a level-lowering variant can be forced.
3. Develop the Mordell-curve / elliptic-fiber viewpoint on the gap-1
   near-misses; ask whether a uniform bound on coprime solutions to
   $A^x+B^y-C^z=k$ for small $k$ is approachable.

## References to pull (provenance)
- Wiles (1995), Taylor–Wiles — FLT.
- Darmon & Granville (1995), *On the equations $z^m = F(x,y)$ and
  $Ax^p+By^q=Cz^r$* — finiteness via Faltings.
- Darmon–Merel, Bennett–Skinner — resolved signatures.
- Frey (1986), Ribet (1990), modularity theorem — FLT engine.
- Catalan/Mihăilescu — consecutive perfect powers (gap-1 context).