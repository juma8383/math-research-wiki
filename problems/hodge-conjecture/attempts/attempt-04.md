---
type: attempt
problem: hodge_conjecture
attempt: 4
date: 2026-08-24
approach: Verify the Atiyah-Hirzebruch & Kollar integral-Hodge counterexamples (the wrinkle forcing the Q-version of HC) against primary sources, pinning the two sources of failure + the Totaro/Soule-Voisin sharpening
outcome: confirmed
tags: [verification, primary-source, integral-hodge, torsion, kollar, totaro, soule-voisin, cross-problem]
---

# Attempt 04 — Verify why integral HC fails (Atiyah-Hirzebruch / Kollar / Totaro / Soule-Voisin)

Cycle-15 Continue on Hodge (cross-problem loop, second pass; green zone
17.3% session / 55.4% weekly, 0 subagents). Attempt-03's `Next` named the
**Atiyah-Hirzebruch & Kollár integral-Hodge counterexamples** — "the wrinkle
that forces the $\mathbb Q$-version of HC" — as the next most load-bearing
to-verify item. The `progress.md` "Verified base" line only asserts
"Integral HC FAILS: Atiyah-Hirzebruch, Kollár — only $\mathbb Q$
conjectured" without primary-source backing; this cycle verifies it against
the four primary papers and sharpens the obstruction map with the
two-sources-of-failure structure. Same discipline that caught the YM
Eriksson viXra/conditional sharpening, the BSD Kim-2022 "bounds rank $\le1$
only" update, and Beal's $(2,3,7)$ spherical mislabel.

## The load-bearing wrinkle: HC is stated over $\mathbb Q$, not $\mathbb Z$

Hodge's 1950 original was for **integral** classes: is every
$\alpha\in H^{2k}(X,\mathbb Z)$ of type $(k,k)$ the class of an algebraic
cycle? This **integral Hodge conjecture is FALSE**, and the failure has
**two genuinely independent sources** — which is precisely why the
conjecture was retreated to the **rational** ($\mathbb Q$) version that
remains open. Both sources are now primary-source-verified.

### Source 1 — torsion: Atiyah-Hirzebruch 1961 (Topology)

**Atiyah & Hirzebruch**, *Analytic cycles on complex manifolds*, **Topology
1** (1961), 25–45.

- A **torsion** class $\alpha$ ($n\alpha=0$) maps to $0$ in
  $H^{2k}(X,\mathbb C)$, hence is **trivially** of type $(k,k)$ — Hodge had
  apparently believed such classes are always algebraic.
- This is **true for $k=1$** (Lefschetz $(1,1)$: divisors), but
  Atiyah-Hirzebruch showed it **fails for $k\ge2$**.
- Mechanism: the **Atiyah-Hirzebruch spectral sequence**
  $E_2^{s,t}=H^s(X,\mathbb Z)$ (even $t$) $\Rightarrow K_{\text{top}}^{s+t}(X)$.
  If $\alpha$ is algebraic, its image under every differential $d_r$ ($r\ge2$)
  vanishes; they built **Godeaux-Serre varieties** (quotients of complete
  intersections by finite group actions) carrying a torsion Hodge class with
  a **nonzero differential**, hence non-algebraic.

### Totaro 1997 (JAMS) — the cobordism reinterpretation + the bound

**Burt Totaro**, *Torsion algebraic cycles and complex cobordism*, **J.
Amer. Math. Soc. 10**(2) (1997), 467–493, DOI
[10.1090/S0894-0347-97-00232-4](https://doi.org/10.1090/S0894-0347-97-00232-4),
arXiv:alg-geom/9609016.

- The cycle class map **factors canonically** as
  $\mathrm{CH}^k(X)\to (MU^*(X)\otimes_{MU^*}\mathbb Z)^{2k}\to
  H^{2k}(X,\mathbb Z)$, where $MU^*(X)$ is the **complex cobordism** ring.
  The second map is an isomorphism when $H^*(X,\mathbb Z)$ is torsion-free
  but **can fail to be surjective in the presence of torsion** — a torsion
  class outside the image of the first map cannot be algebraic.
- A **topological** (Hodge-free) proof that the Griffiths group is nonzero;
  Thm 7.1: smooth projective varieties with
  $\mathrm{CH}^2(X)/2\to H^4(X,\mathbb Z/2)$ **not injective**; Thm 7.2: a
  dimension-15 smooth projective variety with a codim-3 torsion cycle mapping
  to $0$ in both cohomology and the intermediate Jacobian yet **not
  algebraically equivalent to $0$**.
- **Soulé-Voisin bound (below, Thm 1):** the order of a non-algebraic
  torsion class detected this way is divisible only by **primes
  $p\le\dim_{\mathbb C}(X)$** — so the topological obstruction has a
  built-in ceiling.

### Source 2 — non-torsion: Kollár 1990 (Trento examples)

**János Kollár**, *Trento examples*, in *Lecture Notes in Math. **1515***
(Springer, 1990), 134–135.

- Let $X\subset\mathbb P^4$ be a **general** smooth hypersurface of degree
  $D$. By Lefschetz + Poincaré duality, $H^4(X,\mathbb Z)\cong\mathbb Z\alpha$
  with $\langle\alpha,h^2\rangle=1$, and $D\alpha=h^2$ is algebraic (plane
  section).
- **Kollár's theorem:** if $p^3\mid D$ for a prime $p$ coprime to $6$, then
  for **general** $X$ every curve $C\subset X$ has degree divisible by $p$;
  hence the **free generator $\alpha$ is not algebraic** (any algebraic class
  would need degree divisible by $p$, but $\alpha$ pairs to $1$ with $h$).
- Key: $\alpha$ is **not torsion** — a free generator — and **$D\alpha$ is
  algebraic**, so the **rational** HC is **not** contradicted. The
  obstruction is **not topological**: it depends on the complex structure,
  and $\alpha$ becomes algebraic on a **dense** (countable union of proper
  algebraic) subset of the parameter space.

### Soulé-Voisin 2005 (Adv. Math.) — combining both, escaping the bound

**Christophe Soulé & Claire Voisin**, *Torsion cohomology classes and
algebraic cycles on complex projective manifolds*, **Advances in
Mathematics 198** (2005), 107–127, DOI
[10.1016/j.aim.2004.10.022](https://doi.org/10.1016/j.aim.2004.10.022),
arXiv:math/0403254.

- **Thm 1:** if $p>\dim_{\mathbb C}(X)$ and $\alpha\in H^{2k}(X,\mathbb Z)$
  is $p$-torsion, then all AH differentials vanish and $\alpha$ lies in the
  image of Totaro's $\phi^k$ — i.e. **the AH/Totaro obstruction only detects
  small-prime (relative to dimension) non-algebraic torsion**.
- **Thm 3:** building on Kollár's degeneration, for **any prime $p\ge5$**,
  $p$-torsion classes in $H^6(X,\mathbb Z)$ on smooth projective **5-folds**
  that are **non-algebraic** yet **escape all topological obstructions** (in
  the image of $\phi^k$, algebraic on a dense parameter subset) — beyond the
  $p\le\dim$ ceiling of the torsion/topological methods.
- **Thm 4:** torsion cycles annihilated by the Deligne cycle class map
  (cohomology + Abel-Jacobi) **and** by Totaro's invariants, yet
  **non-divisible** (nontrivial in the Griffiths group), vanishing on a
  smooth deformation — so **no locally constant invariant** detects them.

## Why this forces the $\mathbb Q$-version (the load-bearing conclusion)

The rational HC sidesteps **both** sources cleanly:

| Source of failure | Over $\mathbb Z$ | Over $\mathbb Q$ |
|---|---|---|
| Torsion (Atiyah-Hirzebruch/Totaro/Soulé-Voisin) | torsion trivially $(k,k)$ but non-algebraic ($k\ge2$) | **torsion $\mapsto0$** in $H^*(X,\mathbb Q)$ — obstruction vanishes |
| Non-torsion (Kollár) | free generator $\alpha$ non-algebraic | $D\alpha$ algebraic $\Rightarrow$ $\alpha$ algebraic **over $\mathbb Q$** |

So the $\mathbb Q$-version is **not an arbitrary weakening**: it is the exact
retreat that removes the two known obstruction mechanisms while retaining
the essential geometric content (algebraic over $\mathbb Q$ = a nonzero
multiple is algebraic). The remaining open content — surjectivity of
$\mathrm{cl}\otimes\mathbb Q$ in the middle codimensions — is untouched by
either counterexample class.

## What this confirms / sharpens for the obstruction map

- `progress.md`'s line "Integral HC FAILS: Atiyah-Hirzebruch, Kollár — only
  $\mathbb Q$ conjectured" is **CONFIRMED and now primary-source-backed**
  with the **two-sources-of-failure** structure (torsion: AH 1961 /
  Totaro 1997 / Soulé-Voisin 2005; non-torsion: Kollár 1990) and the
  Soulé-Voisin **$p\le\dim$ ceiling** + **escape-all-topological** sharpening.
- The wrinkle reinforces the **analytic$\to$algebraic control** spine of
  the Hodge attack: even the *integral* cycle class map fails in codim
  $\ge2$ for two independent reasons, and the retreat to $\mathbb Q$ is
  precisely the move that removes both obstructions — leaving the
  codim-$\ge2$ analytic$\to$algebraic control as the sole open piece, now
  triangulated from the negative side (why $\mathbb Z$ fails) as well as
  the positive (Charles-Markman $K3^{[n]}$, attempt-03).
- **Cross-problem echo (control-not-resolution):** the integral
  counterexamples are obstructions to the *resolution* claim (exhibit the
  cycle) that the $\mathbb Q$-refinement *removes* — so the obstruction for
  the open conjecture is *not* "is there a cycle" (that is the resolution,
  already known-false over $\mathbb Z$ and *open-but-expected* over
  $\mathbb Q$) but the **control** of the analytic$\to$algebraic bridge in
  codim $\ge2$. Same spine as the other five; Hodge's wrinkle is that the
  control step is sharpened *negatively* by two proven failure modes of its
  integral avatar.

## Honesty / scope

- Four primary sources verified: Atiyah-Hirzebruch (Topology 1, 1961),
  Totaro (JAMS 10(2), 1997, DOI 10.1090/S0894-0347-97-00232-4),
  Kollár (LNM 1515, 1990), Soulé-Voisin (Adv. Math. 198, 2005, DOI
  10.1016/j.aim.2004.10.022). The two-sources-of-failure structure + the
  $\mathbb Q$-retreat logic are recorded.
- No proof of HC; the rational conjecture remains open (smallest case
  codim-2 on a 4-fold). The verification is the cycle's point: the
  "integral HC fails" load-bearing fact is now primary-source-backed and
  sharpened with the $p\le\dim$ ceiling + the non-topological Kollár class.
- Remaining to-verify (attempt-05 targets): **hard Lefschetz reduction
  exact statement**; the **$\ell$-adic Tate analogue** (open even for
  $H^2$, the char-$p$ parallel — arguably next-most-load-bearing);
  the **2024-25 preprints' actual claims**; a **status-check of Shimizu
  2025** (most-cited recent claim, zero citations at attempt-01).
- Outcome: **confirmed** (all four counterexample sources verified, the
  two-sources-of-failure structure + $\mathbb Q$-retreat logic pinned, the
  obstruction map sharpened from the negative side), **partial** overall
  (frontier unchanged).

## Next (attempt-05)

The Hodge to-verify list now has its load-bearing integral-failure item
resolved. Natural next moves: (a) verify the **$\ell$-adic Tate analogue**
(open even for $H^2$, the characteristic-$p$ parallel — the "HC is the
supposedly-easier char-0 side, yet the char-$p$ analogue fails even for
$H^2$" framing is a sharp cross-problem echo), or (b) the **hard Lefschetz
reduction exact statement**, or (c) status-check the **2024-25 preprints**
(Shimizu 2025 et al.). The rotation continues: next cross-problem cycle
$\to$ collatz-conjecture (attempt-04) per the rotation, OR beals
(occasional cycle-in).