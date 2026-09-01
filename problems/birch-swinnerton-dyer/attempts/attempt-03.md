---
type: attempt
problem: birch_swinnerton_dyer
attempt: 3
date: 2026-08-24
approach: Verify the last load-bearing to-verify item [bsd-parity-proven] against primary sources (Nekovar; Dokchitser-Dokchitser), pinning the exact unconditional scope and the Sha-finiteness caveat
outcome: confirmed
tags: [verification, primary-source, parity, sha-finiteness, attribution-correction, cross-problem]
---

# Attempt 03 — Verify [bsd-parity-proven]: p-parity unconditional, algebraic parity mod Sha

Cycle-7 Continue on BSD (cross-problem loop, second pass). The first pass
filed attempt-02 (rank-≤1 base verified, two to-verify items resolved,
direction-(A) block concretized). Attempt-02's `Next` offered two moves; this
cycle takes **(i)** — verify the one remaining to-verify item
`[bsd-parity-proven]` against primary sources, the same verification
discipline that caught the (2,3,7) spherical mislabel (beals) and the
Palasek mislabel (NS). The to-verify text in `progress.md` read:
*"precise unconditional scope of algebraic-rank parity (Nekovář) vs the
p-parity (Dokchitser-Dokchitser); Sha-finiteness caveat."*

## The two statements, kept distinct

Parity is **not one theorem but a chain**. Keeping the links separate is the
whole point of the to-verify item — the open content lives in the gap between
them.

1. **p-parity (Selmer-rank parity).** For a prime $p$,
   $$\mathrm{corank}_{\mathbb Z_p}\,\mathrm{Sel}_{p^\infty}(E/K)\;\equiv\;\mathrm{ord}_{s=1}L(E/K,s)\pmod 2\;\equiv\;-\;w(E/K).$$
   This concerns the **$p^\infty$-Selmer rank**, not the Mordell-Weil rank.

2. **Algebraic-rank parity.**
   $$(-1)^{\mathrm{rk}(E/K)}\;=\;w(E/K).$$
   This concerns the **Mordell-Weil rank** $\mathrm{rk}(E/K)$ itself.

The chain between them is the exact sequence
$$0\to E(K)\otimes\mathbb Q_p/\mathbb Z_p\to\mathrm{Sel}_{p^\infty}(E/K)\to\Sha(E/K)[p^\infty]\to 0,$$
so $\mathrm{corank}_p\,\mathrm{Sel}_{p^\infty}=\mathrm{rk}(E/K)+\mathrm{corank}_p\,\Sha[p^\infty]$.
The two parities agree **iff $\mathrm{corank}_p\,\Sha[p^\infty]$ is even** —
which the Cassels pairing makes automatic *under the standard
Sha-finiteness conjecture* (finite $\Sha\Rightarrow$ zero $p^\infty$-corank).
**That is the Sha-finiteness caveat, located exactly.** It is load-bearing:
parity is the one general rank-$\ge2$ tool `progress.md` records
("Parity's role"), and its unconditional reach stops at the Selmer rank.

## Verification against primary sources — CONFIRMED

**Dokchitser–Dokchitser**, *On the Birch-Swinnerton-Dyer quotients modulo
squares*, Annals Math. **172**(1) (2010), 567–596 (DOI 10.4007/annals.2010.172.11):
- **p-parity for all $E/\mathbb Q$, all primes $p$ — UNCONDITIONAL.**
- **Algebraic-rank parity** $(-1)^{\mathrm{rk}(E/K)}=w(E/K)$ for all number
  fields $K$, **conditional on finiteness of the $2$- and $3$-primary parts
  of $\Sha(E/K(E[2]))$** — i.e. "Sha finiteness $\Rightarrow$ parity," the
  standard caveat, made precise (only the $2$- and $3$-primary parts, after
  the $2$-torsion field extension).

**Dokchitser–Dokchitser**, *Root numbers and parity of ranks of elliptic
curves*, Crelle **658** (2011), 39–64 (DOI 10.1515/crelle.2011.060;
arXiv:0906.1815): completes the global/local picture, including the
characteristic-$0$ **Kramer–Tunnell** local formula (the last open case was
$v\mid 2$, additive reduction, ramified $2$-torsion field), via a
global-to-local "deform to totally real fields" argument.

**Nekovář**:
- *On the parity of ranks of Selmer groups II*, C.R. Acad. Sci. Paris
  **332** (2001), 399–404 (arXiv:math/0101271): for $E/\mathbb Q$ with good
  **ordinary** reduction at $p$, $r_{\rm an}(E/\mathbb Q)\equiv
  s_p(E/\mathbb Q)\pmod 2$, via anticyclotomic $\mathbb Z_p$-extensions +
  Heegner points + (Cornut–Vatsal) nonvanishing.
- *Selmer complexes*, Astérisque **310** (2006): the general
  Selmer-complex machinery; $p$-parity for potentially ordinary reduction.
- *On the parity of ranks of Selmer groups IV* (appendix Wintenberger),
  Compositio Math. **145** (2009), 471–494 (DOI 10.1112/S0010437X09003959):
  $p\neq 2$ Selmer-rank parity over totally real fields, modular or
  integral-$j$ curves; the Wintenberger appendix gives the potential
  modularity needed for analytic continuation/functional equation.

**Dokchitser**, *Notes on the Parity Conjecture*, arXiv:1009.5389 (2010):
self-contained exposition; "$\Sha$ finite $\Rightarrow$ parity."

## Attribution correction (genuine, flag it)

`progress.md`'s to-verify line paired *"algebraic-rank parity (Nekovář) vs
p-parity (Dokchitser-Dokchitser)."* The primary sources correct the
**algebraic-rank** attribution: **Nekovář's unconditional theorems are
p-parity (Selmer-rank parity)**, not the algebraic-rank parity. The
**algebraic-rank parity** (with the Sha caveat) is **Dokchitser–Dokchitser**.
So both halves of the chain are now correctly attributed:

| statement | unconditional scope | authors |
|---|---|---|
| p-parity (Selmer rank) | all $E/\mathbb Q$, all $p$ | Dokchitser–Dokchitser (Annals 2010); Nekovář framework + ordinary/totally-real cases |
| algebraic-rank parity | all $K$, **mod Sha$_{2,3}$ finiteness** | Dokchitser–Dokchitser (Annals 2010, Crelle 2011) |

This is not cosmetic: the unconditional reach of parity is the **Selmer** rank,
and passing to the Mordell-Weil rank costs the Sha hypothesis — exactly the
gap the obstruction analysis leans on. Recording the correct attribution
keeps the load-bearing distinction trustworthy.

## What this confirms for the obstruction map

- `progress.md`'s "Parity's role" section is **correct and now
  primary-source-verified**: parity pins $r_{\rm alg}\pmod 2$; combined with a
  lower bound of $r_{\rm an}$ independent points of the right parity it would
  give exact rank — **but only given a Selmer upper bound of the right
  parity**, i.e. the missing Euler-system step. Parity + lower bound alone
  cannot bound the Selmer group from above. The verification confirms the
  **unconditional reach of parity is the Selmer rank** (p-parity, all $E/\mathbb Q$);
  the algebraic-rank statement is exactly one Sha-finiteness hypothesis
  further — a small but real gap, not a free upgrade.
- This places parity *on the resolution side* of the control/resolution
  divide (it is a consequence, not the missing Selmer control mechanism),
  consistent with the 6-for-6 framing: the obstruction is the **control
  step** (a rank-$r$-shaped Kolyvagin system), and parity is one of the
  working resolution tools, not the missing one.

## Honesty / scope

- `[bsd-parity-proven]` **CONFIRMED + sharpened.** p-parity unconditional for
  all $E/\mathbb Q$ and all $p$; algebraic-rank parity for all number fields
  **conditional on $\Sha_{2,3}$-finiteness**. The Sha caveat is real,
  located exactly (the $p^\infty$-corank of $\Sha$ term in the
  Selmer/algebraic-rank exact sequence), and load-bearing.
- **One attribution corrected:** "algebraic-rank parity (Nekovář)" → the
  algebraic-rank parity is Dokchitser–Dokchitser; Nekovář's unconditional
  contribution is p-parity (Selmer rank).
- No proof of BSD; no progress on rank $\ge 2$ (the frontier). The
  verification is the whole point of the cycle — the last to-verify item in
  `progress.md` is now resolved.
- Outcome: **confirmed** (the verification goal met, the attribution
  corrected), **partial** overall (rank $\ge2$ open as before).

## Next (attempt-04)

With all `progress.md` to-verify items now resolved, the natural next move
is attempt-02's option **(ii)**: survey the **higher Gross–Zagier**
(Yuan–Zhang–Zhang) + **Beilinson–Flach / Kato** derivative literature for
the closest existing rank-2-shaped system and diagnose exactly where its
Selmer bound falls short of rank 2 — the concrete control-step question,
the BSD instance of the cross-problem obstruction.