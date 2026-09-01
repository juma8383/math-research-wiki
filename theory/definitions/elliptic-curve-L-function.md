---
type: definition
name: Elliptic curve L-function and BSD setup
created: 2026-08-24
tags: [number-theory, elliptic-curves, L-functions]
used-in: [[birch_swinnerton_dyer]]
provenance: []
---

# Elliptic curve L-function and the BSD setup

For an elliptic curve $E/\mathbb Q$ of conductor $N$, the **Hasse-Weil
L-function** is the Euler product
$$L(E,s)=\prod_p L_p(p^{-s})^{-1},\quad
L_p(T)=\begin{cases}1-a_pT+pT^2 & p\nmid N\\1-a_pT & p\|N\\1 & p^2\mid N\end{cases}$$
converging for $\Re s>3/2$, with $a_p=p+1-\#E(\mathbb F_p)$. By the modularity
theorem [[thm-modularity]] there is a weight-2 newform $f$ of level $N$ with
$L(E,s)=L(f,s)$, so $L(E,s)$ extends to an **entire** function with a functional
equation relating $s$ and $2-s$ (center $s=1$).

## Ranks

- **Algebraic rank** $r_{\text{alg}}=\operatorname{rank}E(\mathbb Q)$
  (Mordell-Weil [[thm-mordell-weil]]): $E(\mathbb Q)\cong
  E(\mathbb Q)_{\text{tors}}\oplus\mathbb Z^{r_{\text{alg}}}$.
- **Analytic rank** $r_{\text{an}}=\operatorname{ord}_{s=1}L(E,s)$, the order
  of vanishing at the central point.

## BSD (Birch and Swinnerton-Dyer)

**Rank conjecture.** $r_{\text{alg}}=r_{\text{an}}$.

**Refined conjecture.** The leading Taylor coefficient satisfies
$$\frac{L^{(r_{\text{an}})}(E,1)}{r_{\text{an}}!}=
\frac{\Omega_E\,R_E\,|\text{Sha}(E/\mathbb Q)|\,\prod_p c_p}
{|E(\mathbb Q)_{\text{tors}}|^2},$$
where $\Omega_E$ is the real Néron period, $R_E$ the regulator (height pairing
of a basis of the free part), $\text{Sha}$ the Tate-Shafarevich group, and
$c_p=[E(\mathbb Q_p):E_0(\mathbb Q_p)]$ the Tamagawa numbers.

This setup is the anchor of the BSD attack: the conjecture predicts both the
order of vanishing (rank) and the leading term (an arithmetic-invariant
formula). See [[birch_swinnerton_dyer]].