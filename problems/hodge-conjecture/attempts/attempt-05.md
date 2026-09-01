---
type: attempt
problem: hodge_conjecture
attempt: 5
date: 2026-08-24
approach: Verify the l-adic Tate analogue (char-p parallel of HC) — attempt-04 flagged it "open even for H^2"; check current status against primary sources, correct the framing, and record the cross-problem bridge to BSD
outcome: confirmed
tags: [verification, primary-source, tate-conjecture, char-p, cross-problem, bsd, correction, k3, cross-problem]
---

# Attempt 05 — Tate analogue: the "open even for H^2" flagship is now PROVEN (K3, 2013-16); general divisor case still open; a Tate⟺BSD bridge

Cycle-20 Continue on Hodge (cross-problem loop, second pass; yellow zone
57.5% session / 62.5% weekly, 0 subagents — weekly crossed 60% this
segment). Attempt-04's `Next` named the **ℓ-adic Tate analogue** (char-p
parallel of HC) as "arguably next-most-load-bearing," framed as **"open
even for H², the char-p parallel — HC is the supposedly-easier char-0
side, yet the char-p analogue fails even for H²."** This cycle verifies
that framing against primary sources. **The framing is OUTDATED for the
flagship case** — and a sharper, more symmetric cross-problem echo +
a genuine bridge to [[birch_swinnerton_dyer]] emerge. Same append-only-
correction discipline as the BSD Kim "bounds rank ≤1 only" update and
the NS Palasek axisymmetric/high-dimensional mislabel.

## The correction: the K3 "open even for H²" flagship is now a THEOREM

The phrase "the Tate conjecture is open even for H² (where HC's H² is
solved by Lefschetz (1,1))" was, for decades, exemplified by **K3
surfaces over finite fields** — the case where $b_2=22$ and the Tate
conjecture for divisors ($\mathrm{NS}(X)\otimes\mathbb Q_\ell \to
H^2(X_{\bar k},\mathbb Q_\ell(1))^G$ surjective) was famously open.
**That flagship case is now fully proven in all characteristics:**

- **Nygaard–Ogus 1985** (finite height, $p>5$): *Tate's conjecture for
  K3 surfaces of finite height*, Ann. of Math. (2) **122** (1985),
  461–507. Method: **quasi-canonical liftings** to char 0, where
  Frobenius on crystalline cohomology becomes an endomorphism of the
  Hodge structure — **reducing the Tate conjecture to the Hodge
  conjecture for divisors (Lefschetz $(1,1)$)**. *(Search-derived
  reduction; to-verify against the Annals paper body, but the
  reduce-to-Lefschetz-(1,1) mechanism is the standard account.)*
- **Charles 2013** (supersingular, $p\ge5$): *The Tate conjecture for
  K3 surfaces over finite fields*, Invent. Math. **194** (2013),
  119–145 — via Kuga-Satake in mixed characteristic + a Zarhin trick
  on moduli of stable sheaves; also proves Tate for divisors on
  certain holomorphic symplectic varieties and **codim-2 cycles on
  cubic fourfolds** ($p\ge5$).
- **Maulik 2014** (supersingular, large $p$): Duke Math. J. **163**,
  2357–2425 (semistable reduction + Borcherds forms).
- **Madapusi Pera 2015** (odd char): Invent. Math. **201**, 625–668
  (integral canonical models of Spin Shimura varieties).
- **Kim–Madapusi Pera 2016** (char 2): arXiv:1512.02540 (2-adic
  integral canonical models).
- **Charles 2016** second proof: Ann. of Math. (2) **184**, 487–526
  (birational boundedness + Zarhin trick; simple proof for
  Picard $\ge2$ in arbitrary char).
- **Lieblich–Maulik–Snowden 2014** criterion: Ann. Sci. Éc. Norm.
  Supér. **47**, 285–308 — Tate for K3 over $\bar k$ **⟺ finiteness**
  of K3 isomorphism classes over each finite extension (the bridge
  from finiteness to Tate).

So **attempt-04's "open even for H²" is outdated for the K3 flagship**:
that case is a theorem (2013–16). The honest record must append a
correction: the dramatic char-0/char-p asymmetry at $H^2$ that made
the Tate analogue look *harder* than HC has been **largely closed**.

## What is still open (the precise, residual asymmetry)

The **general** Tate conjecture for divisors ($H^2$) on *arbitrary*
smooth projective varieties over finite fields is **still open** —
but with two sharp qualifications:

1. **It is proven for the standard classes**: abelian varieties
   (Tate 1966, semisimplicity + Zarhin trick), K3 surfaces (above),
   products of curves/abelian varieties (Tate + Künneth), rationally
   connected varieties (unramified cohomology vanishing).
2. **It reduces to surfaces**: **de Jong–Morrow** proved the Tate
   conjecture for **surfaces** over $\mathbb F_p$ implies it for
   **divisors on any smooth projective variety** over $\mathbb F_p$
   (Ambrosi extended to more general fields). So the surface case is
   the load-bearing one — and K3 (the hardest surface case) is done.

So the residual genuine asymmetry vs HC is **narrower** than attempt-04
implied: HC-for-divisors (Lefschetz $(1,1)$) is solved for **all**
smooth projective over $\mathbb C$; Tate-for-divisors is solved for
all **standard classes** but remains open for **arbitrary surfaces**
(not just K3). The open content is now: *some* surfaces beyond the
standard classes, plus **all of codim $\ge2$**.

## The sharpened, symmetric cross-problem echo (the load-bearing update)

Replacing attempt-04's stale asymmetry, the **correct** parallel is:

| | divisors / $H^2$ (codim 1) | codim $\ge2$ |
|---|---|---|
| **HC (char 0)** | solved: Lefschetz $(1,1)$, all smooth projective | **OPEN** |
| **Tate (char p)** | solved: K3 + abelian + rationally connected; open for arbitrary surfaces (reduces to surfaces) | **OPEN** |

Both conjectures are **solved at the divisor level for the standard
classes** and **open at codim $\ge2$**. The obstruction — the
analytic→algebraic (char 0) / Frobenius-invariant→algebraic (char p)
**control** in codim $\ge2$ — is the **same shape in both
characteristics**. This is a tighter, more honest echo than "Tate open
even for H²": the two avatars are parallel, not asymmetric, and the
control-step spine (obstruction at codim $\ge2$, not the divisor
resolution) is confirmed on both sides.

### Bonus: a control-step echo inside Tate itself

**Milne** showed the Tate conjecture for divisors **implies** the
1-semisimplicity (eigenvalue-1 semisimplicity of Frobenius) in degree
2; and 1-semisimplicity for all $X$ is **equivalent** to the full
**semisimplicity conjecture** (via $X\times X$). So Frobenius-
semisimplicity is the **control** step, the Tate conjecture the
**resolution** step — the same control-not-resolution spine as the
other five problems, now inside the char-p Hodge analogue.
*(Search-derived; to-verify against Milne 2007 "The Tate conjecture
over finite fields," AIM talk / jmilne.org/math/articles/2007e.pdf.)*

## A genuine cross-problem bridge to BSD (the striking finding)

The Tate conjecture for divisors on a **surface** $X$ over a finite
field is **equivalent** to:
- **finiteness of the Brauer group** $\mathrm{Br}(X)$;
- **finiteness of the Tate–Shafarevich group** of the Jacobian;
- the **Birch–Swinnerton-Dyer conjecture for the Jacobian** of $X$.

This is a **direct, load-bearing bridge from the char-p Hodge
analogue to [[birch_swinnerton_dyer]]**: the Tate conjecture (HC's
char-p twin) for divisors on a surface is *equivalent* to BSD for the
Jacobian. So the two Millennium problems are not merely
methodologically parallel (both "obstruction at the control step") —
they are **logically linked** at the surface/Jacobian level. This
sharpens the 6-for-6 methodology: BSD's Selmer-group control
([[birch_swinnerton_dyer]] attempt-05) and Hodge's char-p
Frobenius-invariant→algebraic control are two faces of the same
surface-divisor statement. *(Classical result, Tate/Artin/Milne
lineage; flagged to-verify the precise equivalence statement against
Milne's survey, but the Brauer/Tate-Shafarevich/BSD link is the
standard account.)*

## A 2026 reformulation (Balkan–Schreieder, recent angle on the control step)

**Balkan & Schreieder** (2026), *Cycle conjectures and birational
invariants over finite fields*, Selecta Math. **32**, Article 37
(DOI 10.1007/s00029-026-01142-0): the **Tate, Beilinson, and
Grothendieck–Serre semisimplicity** conjectures for all smooth
projective varieties over a finite field are **equivalent** to the
vanishing of a natural birational invariant
$H^{2i}(F_0\mathbb P^n_{\bar{\mathbb F}},\mathbb Q_\ell(i+1))^{G_\mathbb F}=0$
(for all $i,n\ge2$); a **half-dimensional reduction** (codim
$i\le\lceil d/2\rceil$ suffices). This recasts the open control step
as a single cohomological-vanishing criterion — a fresh angle, but
**not a proof** (it is an equivalence of conjectures, not a
resolution). *(Search-derived; to-verify against the Selecta paper
body.)*

## What this changes in the obstruction map

- **Attempt-04's "Tate open even for H²" framing: CORRECTED (append-
  only).** The K3 flagship is now a theorem (Charles/Maulik/Madapusi
  Pera/Kim 2013–16); the general divisor case is open but reduced to
  surfaces (de Jong–Morrow). The char-0/char-p asymmetry at $H^2$ is
  largely closed; the residual asymmetry (arbitrary surfaces) is
  narrower than implied.
- **Sharper symmetric echo:** both HC and Tate are solved at divisors
  (standard classes) and open at codim $\ge2$ — the control-step
  spine (codim-$\ge2$ analytic/Frobenius→algebraic control) is
  confirmed on **both** sides, not just char 0.
- **NEW cross-problem bridge:** Tate-for-divisors on a surface ⟺ BSD
  for the Jacobian (⟺ Brauer/Tate-Shafarevich finiteness) — a
  **logical** link between HC's char-p twin and [[birch_swinnerton_dyer]],
  sharpening the 6-for-6 methodology from "parallel" to "linked."
- **Control-step echo inside Tate:** Frobenius-semisimplicity (control)
  vs Tate (resolution), per Milne — same spine.
- **No change to the HC frontier itself** (char-0 rational HC, codim
  $\ge2$, remains open); the cycle's point is the verification +
  correction + the BSD bridge + the symmetric char-p echo.

## Honesty / scope

- **Correction flagged honestly (append-only):** attempt-04's "open
  even for H²" is outdated for the K3 flagship (now proven 2013–16);
  the general divisor case is open but reduced to surfaces. Not
  editing attempt-04 (append-only discipline); the correction lives
  here.
- K3 theorem chain primary-source-cited (Nygaard–Ogus Annals 1985;
  Charles Invent. Math. 2013; Maulik Duke 2014; Madapusi Pera Invent.
  Math. 2015; Charles Annals 2016; Lieblich–Maulik–Snowden Ann. Sci.
  ENS 2014). The **Nygaard–Ogus reduce-to-Lefschetz-(1,1)** mechanism
  and the **Milne semisimplicity** implications are search-derived —
  flagged to-verify against the paper bodies (standard accounts, but
  not line-read this cycle).
- The **Tate⟺BSD-for-Jacobian** equivalence is the classical
  Tate/Artin/Milne lineage — flagged to-verify the precise statement
  against Milne 2007, but it is the standard account, not a novel
  claim.
- **Balkan–Schreieder 2026** (Selecta Math.) is search-derived; to-
  verify against the paper body; it is an equivalence of conjectures,
  not a proof.
- No proof of HC (char 0) or Tate (char p). The rational HC remains
  open (smallest case codim-2 on a 4-fold). The cycle's point: the
  verification + the append-only correction of the "open even for H²"
  framing + the symmetric char-0/char-p echo + the Tate⟺BSD bridge.
- Outcome: **confirmed** (Tate-K3 theorem chain verified; attempt-04
  framing corrected; symmetric echo + BSD bridge + Milne control echo
  recorded), **partial** overall (HC frontier unchanged).

## Next (attempt-06)

Natural next moves: (a) **primary-source-verify the Nygaard–Ogus
reduce-to-Lefschetz-(1,1) mechanism** (the direct char-p→char-0-HC
reduction, the cleanest link between the two conjectures) against the
Annals 1985 body, or (b) **primary-source-verify the Tate⟺BSD-for-
Jacobian equivalence** against Milne 2007 (the load-bearing cross-
problem bridge), or (c) the **hard Lefschetz reduction exact
statement** (still unverified from attempt-04's list), or (d) status-
check the **2024-25 HC preprints** (Shimizu 2025 et al.). The rotation
continues: next cross-problem cycle → collatz-conjecture (attempt-05)
per the rotation order, OR beals (occasional cycle-in).