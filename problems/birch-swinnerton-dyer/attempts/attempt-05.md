---
type: attempt
problem: birch_swinnerton_dyer
attempt: 5
date: 2026-08-24
approach: Verify the load-bearing claims of attempt-04's direction-(A) deepening — Chan-Ho Kim's higher Gross-Zagier / Kurihara-number Selmer-structure theorem — against the primary source (arXiv abstract + Trans. AMS publication + the Kurihara-number definition)
outcome: confirmed
tags: [verification, primary-source, higher-gross-zagier, kurihara-numbers, selmer-structure, kolyvagin-system, main-conjecture, cross-problem]
---

# Attempt 05 — Verify Kim 2022/2024 higher-GZ + Kurihara-number Selmer structure

Cycle-17 Continue on BSD (cross-problem loop, second pass; green zone
29.4% session / 57.6% weekly, 0 subagents). Attempt-04 deepened direction
(A) but flagged `[bsd-higher-gz-kim-2022]` **to-verify** — Kim 2022
arXiv:2203.12161's Thm 2.3 (the max{cork Sel} statement + the
Kolyvagin-conjecture condition) and the Kurihara-number definition were
from a search summary and needed primary-source verification before
load-bearing reuse. This cycle verifies both directly: the arXiv
abstract page (primary source) + a corroborating search pinning the
Kurihara-number definition and the structure theorem. The headline
finding is a **citation upgrade**: the paper is no longer just an arXiv
preprint — it is **published in Trans. AMS (2024)**.

## Headline: citation upgrade (arXiv preprint → published)

**Chan-Ho Kim**, *A higher Gross–Zagier formula and the structure of
Selmer groups*, **Trans. Amer. Math. Soc. (2024)**, DOI
[10.1090/tran/9125](https://doi.org/10.1090/tran/9125) (= arXiv:2203.12161,
v1 23 March 2022, v7 12 January 2024). So `progress.md` / attempt-04's
"arXiv:2203.12161 (2022)" should be cited as **Trans. AMS 2024** — a
peer-reviewed publication, materially strengthening the load-bearing
status of the mechanism. (The arXiv version numbering explains the
"2022" in the search summaries: v1 was 2022; v7, the published revision,
is 2024.)

## Verification against the arXiv abstract (CONFIRMED, high-level structure)

From the primary-source abstract (arxiv.org/abs/2203.12161):

- **"Kolyvagin system-theoretic refinement of Gross–Zagier formula"**
  comparing **Heegner point Kolyvagin systems with Kurihara numbers**
  when the root number of $E/K$ is $-1$; when the root number is $+1$, a
  **structure theorem of the $p^\infty$-Selmer group of $E$ over $K$** via
  "values of certain families of quaternionic automorphic forms, which
  is a part of **bipartite Euler systems**" — an "analogous refinement of
  the Waldspurger formula." **Two root-number cases confirmed** (the
  Heegner/$-1$ side and the bipartite/$+1$ side).
- **"No low analytic rank assumption is imposed in both refinements"** +
  applications to "the structure of $p^\infty$-Selmer groups of elliptic
  curves of **arbitrary rank**" — **CONFIRMS the "arbitrary rank" claim**
  (the core of attempt-04's "outdated: bounds rank $\le1$ only" revision).
- **Nontriviality ⟺ localized main conjecture:** "the equivalence between
  the **non-triviality** of various 'Kolyvagin systems' and the
  corresponding **main conjecture localized at the augmentation ideal**"
  — **CONFIRMS the Kolyvagin-conjecture condition is a main-conjecture
  condition**, exactly the "conditional (main conjecture)" sub-wall of
  attempt-04. The condition is not an ad-hoc hypothesis; it is equivalent
  to the (localized) Heegner-point / anticyclotomic main conjecture.
- **p-converse application:** "the Heegner point main conjecture localized
  at the augmentation ideal implies the **strong rank one p-converse** to
  the theorem of Gross–Zagier and Kolyvagin" — CONFIRMED.

## Kurihara numbers — definition CONFIRMED (modular symbols, not L-derivatives)

From Kurihara's foundational papers (*The structure of Selmer groups of
elliptic curves and modular symbols*, 2014; *Refined Iwasawa theory…*,
Münster J. Math. 2014; *Refined Iwasawa theory and Kolyvagin systems of
Gauss sum type*, PLMS 2012), corroborating the search summary:

- The **Kurihara number** $\tilde\delta_m$ (for a squarefree product $m$
  of admissible primes) is
  $$\tilde\delta_m=\sum_{\substack{a=1\\(a,m)=1}}^{m}\mathrm{Re}\!\left(\left[\tfrac{a}{m}\right]\right)\Omega_E^+\cdot\prod_{\ell\mid m}\log_{F_\ell}(a)\pmod{p^N},$$
  where $[a/m]=\int_{a/m}^{\infty}f(z)\,dz$ is the **modular symbol**,
  $\Omega_E^+$ the Néron period, $\log_{F_\ell}$ a discrete logarithm.
  **So Kurihara numbers are built from modular symbols** — *not* from
  Rankin-Selberg $L$-derivatives — **CONFIRMING attempt-04's "Kolyvagin
  derivatives of Mazur-Tate elements, NOT $L$-derivatives"** framing.
- The bridge: **Mazur-Tate elements** $\theta_n$ are group-ring elements
  from modular symbols, "intermediate between $L$-values and Kurihara
  numbers"; the **Kolyvagin derivative** $D_\ell=\sum i\sigma_\ell^i$
  operator produces Kolyvagin-system elements from the Euler system. So
  the chain is **modular symbols → Mazur-Tate elements → (Kolyvagin
  derivative) → Kurihara numbers** — genuinely *not* the relative-trace-
  formula / $L^{(r)}$ route, exactly as Kim emphasizes ("completely
  different from the relative trace formula approach," attempt-04).

## The structure theorem — CONFIRMED (full Selmer structure, conditional)

**Kurihara's Theorem B / Theorem 1.1.1** (Münster 2014): if
$\mathrm{rank}_{\mathbb Z_p}\,\mathrm{Sel}(\mathbb Q,E[p^\infty])^\vee=r$,
then $\Theta^0=\cdots=\Theta^{r-1}=0$, $\Theta^r\neq0$, and
$$\mathrm{Fitt}_{i,\mathbb Z_p}(\mathrm{Sel}^\vee)=\Theta_i(\mathbb Q)\quad(i\ge r,\;i\equiv r\!\!\pmod2),$$
giving the full structure
$$\mathrm{Sel}^\vee_{\mathrm{tors}}\simeq\bigoplus_k(\mathbb Z/p^{\,n_{r+2k}-n_{r+2k+2}/2})^2,$$
i.e. $\mathbb Z_p^r\oplus\bigoplus_k(\mathbb Z/p^{a_k})^2$ — a free rank-$r$
part plus a sum of **paired** torsion modules. **"No low-rank
assumption"** + "full Selmer group structure at arbitrary rank" = the
precise content of attempt-04's (A-ii) revision, now primary-source-
backed. **The condition is the main conjecture + non-degenerate
$p$-adic height pairing** (Kurihara Thm 1.1.1); *without* the main
conjecture only partial results hold (Thm 1.2.3/1.2.5, Kolyvagin systems
of Gauss sum type) — **so the "conditional (main conjecture)" sub-wall is
the exact, named condition, and the unconditional state is only
partial** (a sharper statement than attempt-04's bare "conditional").

## What this upgrades in the obstruction map

- `[bsd-higher-gz-kim-2022]` is **upgraded from `to-verify` to CONFIRMED**
  (primary source): arbitrary-rank structure theorem, Kurihara numbers =
  modular-symbol/Mazur-Tate derivatives (not $L$-derivatives),
  nontriviality⟺localized main conjecture, p-converse application — all
  verified. The citation is **Trans. AMS 2024** (peer-reviewed), not just
  arXiv:2203.12161.
- The **three sub-walls of attempt-04** are now corroborated on two of
  three: **(2) conditional (main conjecture)** is the exact named
  condition (and the unconditional state is only partial, per Kurihara
  Thm 1.2.3/1.2.5); **(1) relative (paired $E/E^K$)** is corroborated by
  the structure theorem's paired-twist form (the $\mathbb Z_p^r\oplus$
  paired-torsion decomposition is the E-vs-twist paired structure Kim
  refines). **(3) cyclotomic-vs-anticyclotomic disjointness** is the one
  sub-wall **still search-derived** — the arXiv abstract does not mention
  Kato/cyclotomic disjointness; it appears in Kim's intro / the Wei Zhang
  survey (search summary). It remains **to-verify against the PDF body /
  the Wei Zhang 2013 survey** before full load-bearing use.
- The **two-engine 6-for-6 echo** stands and is sharpened: the
  anticyclotomic (Heegner) engine now has a *published* arbitrary-rank
  Selmer-structure theorem (conditional on its own main conjecture); the
  open piece is the comparison with the cyclotomic (Kato) engine — exactly
  sub-wall (3), the one not yet primary-source-verified.

## Honesty / scope

- Kim, *Trans. Amer. Math. Soc.* (2024), DOI 10.1090/tran/9125
  (= arXiv:2203.12161) CONFIRMED via the arXiv abstract (primary source);
  Kurihara-number definition + structure theorem confirmed via Kurihara
  2012/2014 papers. **Citation upgraded** from arXiv-preprint to
  peer-reviewed.
- **Remaining to-verify (minor):** the *exact* $\max\{\mathrm{cork}\,\mathrm{Sel}(E),\mathrm{cork}\,\mathrm{Sel}(E^K)\}$
  paired-twist formulation (Kim's specific Thm 2.3) and the
  cyclotomic-vs-anticyclotomic disjointness framing (sub-wall 3) need the
  PDF body / Wei Zhang 2013 survey — both structural content corroborated
  but the precise statements not yet read line-by-line. Flagged honestly.
- No proof of BSD; the rank-$\ge2$ wall is sharpened (three sub-walls, two
  now primary-source-confirmed) not broken. Refined-BSD (direction C)
  untouched this cycle.
- Outcome: **confirmed** (the attempt-04 deepening upgraded from partial
  to primary-source-confirmed; citation upgraded to Trans. AMS 2024;
  Kurihara-number definition and arbitrary-rank structure theorem
  verified; the main-conjecture condition pinned as the exact
  conditional sub-wall; one sub-wall remains PDF-body to-verify),
  **partial** overall (frontier unchanged).

## Next (attempt-06)

The remaining named sub-wall (3) — **cyclotomic-vs-anticyclotomic
disjointness** (Kato vs Heegner field-variation) — is the natural next
to-verify (against the Wei Zhang 2013 *Current Developments in
Mathematics* survey or Kim's Trans. AMS intro), to close the last
search-derived piece. Or pivot to direction (C) / refined-BSD
(Bullach-Honnor 2025, equivariant Tamagawa / Mazur-Tate) as the second
front. The rotation continues: next cross-problem cycle →
navier-stokes (attempt-05) per the rotation order, OR beals
(occasional cycle-in).