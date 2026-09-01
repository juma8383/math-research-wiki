---
type: theorem
name: Parity theorem for elliptic curves
created: 2026-08-24
tags: [number-theory, elliptic-curves, L-functions, parity]
used-in: [[birch_swinnerton_dyer]]
provenance: [[bsd-survey]]
---

# Parity theorem

**Parity conjecture.** $r_{\text{alg}}\equiv r_{\text{an}}\pmod2$ for
$E/\mathbb Q$.

**Status [bsd-parity-proven]:**
- **$p$-parity (unconditional).** Dokchitser-Dokchitser (2010, Annals): for
  every $E/\mathbb Q$ and every prime $p$, the parity of the
  $p^\infty$-Selmer rank equals the parity of $r_{\text{an}}$. Unconditional.
- **Algebraic-rank parity.** Nekovář: $r_{\text{alg}}\equiv r_{\text{an}}\pmod2$
  holds (under the hypothesis that $\text{Sha}$ is finite; combined with
  Kolyvagin this gives full parity whenever $r_{\text{an}}\le1$).
  [to-verify: precise unconditional scope of the algebraic-rank parity.]

## What parity does and does not give

Parity is the **single general rank statement available for
$r_{\text{an}}\ge2$**. It pins the rank modulo 2: if you establish a lower
bound $\operatorname{rank}\ge r_0$ by finding points, and
$r_0\equiv r_{\text{an}}\pmod2$, then parity *forces* $r_{\text{alg}}=r_0$
**provided** an upper bound of the same parity is already known. So parity
converts "at least $r_{\text{an}}$ points and the right parity" into exact rank
— *but only if an upper bound exists*. The missing upper-bound step is exactly
the Euler-system obstruction [[method-heegner-point-euler-system]]: parity +
lower bound cannot, on its own, bound the Selmer group from above.