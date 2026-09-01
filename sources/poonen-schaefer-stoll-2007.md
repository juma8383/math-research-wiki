---
type: source
id: pss2007
title: "Twists of X(7) and primitive solutions to x^2 + y^3 = z^7"
authors: Poonen, Schaefer, Stoll
year: 2007
venue: Duke Math. J. 137(1), 103–140
url: https://doi.org/10.1215/s0012-7094-07-13714-1
ingested: 2026-08-24
tags: [pss2007-237-solns, pss2007-klein-quartic, pss2007-psl2-7, pss2007-nonabelian-descent, pss2007-mordell-weil-sieve]
---

# Poonen–Schaefer–Stoll 2007 — $x^2+y^3=z^7$

> arXiv: math/0508174; Duke Math. J. 137(1), 103–158 (2007).
> Originally ingested from a search-result summary in attempt-14; **verified
> against the paper's abstract/Theorem 1.1 in attempt-17**. Items still from the
> summary only (not re-confirmed against full text) are flagged "[summary]".

## [pss2007-237-solns] Complete solution of $x^2+y^3=z^7$ (VERIFIED)

Theorem 1.1 gives all **16 primitive integer solutions** (verified): $(\pm1,-1,0)$,
$(\pm1,0,1)$, $\pm(0,1,1)$, $(\pm3,-2,1)$, $(\pm71,-17,2)$,
$(\pm2213459,1414,65)$, $(\pm15312283,9262,113)$, $(\pm21063928,-76271,17)$.
This is the **first complete treatment of a pairwise-coprime $(p,q,r)$ with
$\chi<0$** — significant because it marks $(2,3,7)$ as the boundary of
tractability ($\chi=-1/42$, the negative value closest to $0$).

## [pss2007-klein-quartic] Reduction to twists of the Klein quartic (VERIFIED)

The nonabelian descent reduces the problem to rational points on **10 twists
$C_1$–$C_{10}$ of the Klein quartic** $X: x^3y+y^3z+z^3x=0$ (genus 3, 168
automorphisms), after a local-solubility filter. $X\cong X(7)$ as a modular
curve (twists = exotic level-7 structures on elliptic curves); irreducible
7-torsion cases are reduced via **Ribet level lowering + modularity** to 13
elliptic curves of low conductor.

## [pss2007-psl2-7] Nonabelian descent via $\mathrm{PSL}_2(\mathbb F_7)$ (VERIFIED)

The descent is **nonabelian**, through the finite simple group
$\mathrm{PSL}_2(\mathbb F_7)$ of order 168 — a **finite quotient of the
*infinite* (hyperbolic) triangle group $\Delta(2,3,7)$**, realized as the
automorphism group of the Klein quartic. *(Correction, attempt-17: an earlier
note called $\Delta(2,3,7)$ "spherical"/finite — wrong, since
$1/2{+}1/3{+}1/7=41/42<1$; it is hyperbolic.)* The crucial enablers are the
**near-spherical position** ($\chi=-1/42$, closest to $0$) and the **exponent
$2$** (giving the $X(7)$ modular-curve interpretation); see
[[method-triangle-group-descent]].

## [pss2007-nonabelian-descent] Chabauty + descents for the easy curves (VERIFIED)

For curves with $\operatorname{rank}J<\operatorname{genus}=3$ (all except
$C_5$), rational points are determined by **Chabauty–Coleman**. $C_1,C_2,C_3$
(μ₇-twists with CM by $\mathbb Z[\zeta_7]$) are handled by
**$(1-\zeta)$-descent**; $C_4$–$C_{10}$ by **2-descent** (using Weierstrass
points of the Klein quartic), which also determines the Mordell–Weil ranks.

## [pss2007-mordell-weil-sieve] Mordell–Weil sieve for the hard curve (VERIFIED, detail [summary])

The difficult curve $C_5$ has $\operatorname{rank}=\operatorname{genus}=3$
(Chabauty inapplicable); it is settled by a **Mordell–Weil sieve** +
component-group information from Néron models, proving $C_5(\mathbb Q)_{\text{subset}}=\varnothing$.
[summary, not re-confirmed against full text] the specific sieve primes
$2,3,13,23,97$.

## Relevance to Beal

PSS is the canonical *effective* instance of "reduce a generalized Fermat
equation to finitely many genus-$\ge2$ curves + resolve them" — the template of
direction (B) in attempt-11. It works because $(2,3,7)$ is **near-spherical**
($\chi=-1/42$) **and has an exponent $2$** (the $X(7)$ modular interpretation).
The Beal frontier $(3,5,7)$ is **deeply hyperbolic** ($\chi=-34/105$) **with no
exponent $2$** → no known finite-quotient descent and no modular-curve
interpretation → the PSS technique is unavailable [[method-triangle-group-descent]].
PSS *demonstrates* the geometric route can work in principle; the
near-spherical/$2$-exponent requirement *explains* why it does not reach the
distinct-odd-prime regime.