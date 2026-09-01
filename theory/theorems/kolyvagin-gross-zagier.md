---
type: theorem
name: Gross-Zagier-Kolyvagin theorem (BSD for analytic rank <= 1)
created: 2026-08-24
tags: [number-theory, elliptic-curves, heegner-points, euler-systems]
used-in: [[birch_swinnerton_dyer]]
provenance: [[bsd-survey]]
---

# Gross-Zagier-Kolyvagin theorem

For $E/\mathbb Q$:
- **Gross-Zagier (1986).** Given an imaginary quadratic $K$ satisfying the
  Heegner hypothesis, the Heegner point $P_K\in E(K)$ has Néron-Tate height
  $\hat h(P_K)\propto L'(E/K,1)$; so $P_K$ non-torsion $\Leftrightarrow
  L'(E/K,1)\neq0$. (Extended to all ranks/orders by Zhang, Yuan-Zhang-Zhang.)
- **Kolyvagin (1988-90).** When a Heegner point is non-torsion, its derived
  cohomology classes form an **Euler system** that bounds the Selmer group,
  forcing $\operatorname{rank}E(\mathbb Q)\le r_{\text{an}}$ and $\text{Sha}$
  finite (with an explicit upper bound on $|\text{Sha}|$).

**Theorem (combined, with modularity + nonvanishing).** If $r_{\text{an}}\le1$
then $r_{\text{alg}}=r_{\text{an}}$ and $\text{Sha}(E/\mathbb Q)$ is finite
[bsd-rank-le-1-proven].

## The Heegner-hypothesis point

The rank-1 case needs an imaginary quadratic $K$ satisfying the Heegner
hypothesis *with a non-torsion Heegner point*. **Nonvanishing results**
(Bump-Friedberg-Hoffstein, Murty-Murty, Waldspurger) guarantee such $K$ exist
when $r_{\text{an}}=1$, so the theorem is unconditional given modularity.
[to-verify: confirm this makes the rank-1 theorem fully unconditional.]

## Why it stops at rank 1

Kolyvagin's Euler system has the **shape of a single point**: one non-torsion
Heegner point produces a one-dimensional family of cohomology classes, which
can bound a Selmer group of rank $\le1$ but **not** rank $\ge2$. This is the
central obstruction — see [[method-heegner-point-euler-system]]. Kolyvagin's
own **Conjectures 3.32–3.35** [bsd-kolyvagin-conj] would extend the method to
higher rank but remain unproven.