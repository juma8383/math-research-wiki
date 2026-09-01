# Notes — Riemann Hypothesis

> Methodology + cross-problem links. Running notes for [[riemann_hypothesis]].
> OPEN (the Millennium target). The deepest structural observation: RH has the
> same **two-avatars** structure as [[birch_swinnerton_dyer]] and [[PvsNP]] —
> function-field proven / number-field open.

## The control-step pattern — RH as the 8th open problem

The wiki's methodology: **the obstruction is at the control/reduction step,
not the resolution step** (7-for-7 across [[beals_conjecture]],
[[birch_swinnerton_dyer]], [[navier_stokes]], [[yang_mills]],
[[hodge_conjecture]], [[collatz_conjecture]], [[PvsNP]]), with a
**"one-dimensional engine stops"** sub-pattern. RH fits cleanly:

- **Resolution machinery works on a slice / on average.** Computational
  verification (zeros on the line up to height $T=3\cdot10^{12}$) is a slice.
  Selberg's almost-all theorem, zero-density estimates, zero-free regions,
  and proportion-on-the-line results are *average / density* control. All
  work; none is the wall.
- **The wall is control to full strength.** Going from "up to $T$ / almost
  all / $\ge X\%$" to "every zero, every height" is the open step. This is the
  **same spine as Collatz** (density / average → pointwise / every $N$) and
  **NS** (resolve a slice → control to full 3D): the resolution engine stops
  at the universal / pointwise / all-zeros control step.
- **The functional equation is resolution, not control.** The symmetry
  $\zeta(s)=\chi(s)\zeta(1-s)$ pairs zeros about $\Re=\tfrac12$ but does not
  pin them — a zero off the line is allowed (paired with its mirror). This is
  the clean statement of why symmetry is *not* the control tool: it is
  resolution-layer information that fails to discharge the control step.

## ≥3 distinct approaches (research-protocol step)

Per the standing 10-step protocol, ≥3 distinct proof approaches are named.
Each reduces RH to a single control property that is then not dischargeable:

### (A) Hilbert–Pólya / spectral interpretation
RH ⟺ the non-trivial zeros $\rho=\tfrac12+i\gamma$ are the eigenvalues of a
self-adjoint operator $D$ on a Hilbert space (then the $\gamma$ are real and
the functional-equation symmetry pins the line). **The control tool would be
self-adjointness; no such operator is known.** Connes (1997, *Trace formula in
noncommutative geometry and the zeros of the Riemann zeta function*; 2019,
*An essay on the Riemann Hypothesis*) builds a spectral interpretation from
the adele-class space $X=\mathbb A/k^\times$, reinterprets the explicit
formula as a trace formula, and reduces RH to the validity of that trace
formula (a Weil-positivity statement). The obstruction Connes names: an
"absorption spectrum" with a minus-sign problem — the Riemannian-space
analogue (Selberg trace formula) has the right sign, the adelic one does not
without extra structure (the arithmetic site / scaling site / tropical
"characteristic one" geometry is the attempt to supply it). **Engine: the
spectral interpretation runs; it stops at self-adjointness / the trace-formula
positivity.** Berry–Keating $H=xp$ is the semiclassical toy operator
(candidate, not realized). This is the control step.

### (B) Weil / Bombieri–Lagarias / Li positivity
RH ⟺ the positivity of the explicit-formula distribution (Weil's criterion:
$\sum_\rho h(\rho)\ge0$ for a wide class of test functions $h$, equivalently a
distribution on the critical line is positive). Li (1997) gave the
discrete-equivalent **Li criterion**: RH ⟺ $\lambda_n\ge0$ for all $n$, where
$\lambda_n=\frac{1}{n!}\frac{d^n}{ds^n}[s^{n-1}\log\xi(s)]_{s=1}$. Bombieri–
Lagarias (1999) generalized Li's criterion to a class of L-functions /
sequences. Suzuki (2023, J. London Math. Soc.) gives screw-function (Kreĭn)
equivalents tying Weil positivity to Li coefficients via moments $\mu_n$.
Lagarias (1999, Acta Arith. 89) gives a positivity property of $\xi$. **The
control step = proving the positivity / $\lambda_n\ge0$ for all $n$ — an exact
reduction to a sign control that is not dischargeable.** This is the
cleanest "RH = a positivity statement" face; it is also the bridge to (A)
(Connes's trace formula *is* Weil positivity).

### (C) Zero-density / computational / proportion (resolution on slices)
The analytic-number-theory engine: verify on the line up to height $T$
(Platt–Trudgian $3\cdot10^{12}$), bound $N(\sigma,T)$ (Ingham 1940 → Huxley
→ **Guth–Maynard 2024** breaks Ingham's 80-year record at $\sigma=\tfrac34$;
Chourasiya 2024 explicit Carlson), prove a proportion on the line (Levinson
$\tfrac13$ 1974 → Conrey $\tfrac25$ 1989 → $\tfrac{5}{12}$ 2020; a 2/3 claim
2024 un-peer-reviewed). **This is the resolution layer; it is average/slice
control, structurally incapable of reaching "every zero."** The Guth–Maynard
advance is the strongest 2024 move but stays on the average side. The control
gap (average → all) is exactly the Collatz echo.

### (D) Function-field analogy (the engine that works, then stops)
RH for curves / varieties over finite fields is a **theorem** (Weil 1940s
for curves; Deligne 1973/74 for all varieties — the Weil conjectures), via
étale cohomology + the Lefschetz trace formula + the **positivity of the
Rosati involution** / Riemann–Roch (Frobenius eigenvalues are Weil numbers,
all conjugates $|\alpha|=q^{-n/2}$). Milne's survey (*The Riemann Hypothesis
over Finite Fields*, ALM 35, 2015) and Kowalski's (*Some Aspects and
Applications of the RH over Finite Fields*) are the references. **The engine
stops at the number field**: there is no Frobenius and no Rosati positivity in
characteristic 0, so the function-field control tool does not translate to
$\zeta(s)$. This is the canonical "one-dimensional engine stops" instance
(the function-field engine is one-dimensional in the sense that it relies on
the canonical Frobenius endomorphism, a finite-field-specific object).

### (E) de Branges (tracked failed approach, append-only)
Louis de Branges repeatedly claimed RH via coefficient inequalities in
Hilbert spaces of entire functions; the load-bearing inequality (needed to
control the coefficients of $\xi$) does not hold, and the approach is not
accepted. Recorded here per the protocol's "track failed attempts" rule
(append-only); a pre-2015 survey by Connes & others documents the failure.
Flagged to-verify against de Branges's manuscripts for the precise obstruction.

## Cross-problem links

### [[birch_swinnerton_dyer]] — the two-avatars twin (deepest)
RH and BSD share the **exact** two-avatars structure:

| | Function-field / geometric avatar | Number-field / arithmetic avatar |
|---|---|---|
| **RH** | RH for varieties over $\mathbb F_q$ — **PROVEN** (Weil; Deligne) | RH for $\zeta(s)$ over $\mathbb Q$ — **OPEN** |
| **BSD** | function-field BSD — **PROVEN** (Kato–Trihan) | number-field BSD over $\mathbb Q$ — **OPEN** (Millennium) |

In both, the function-field control tool (Frobenius/Rosati for RH;
étale-Euler-system for BSD) has no known characteristic-0 / number-field
translation — the engine stops. This is the same shape as [[PvsNP]]'s
`[two-faces-two-np-variants]` (mining face closes / S1.a face open). The
two-avatars structure now appears in **three** wiki problems (RH, BSD, PvsNP),
suggesting it is a general feature of Millennium-grade arithmetic / complexity
problems: a geometric / function-field / black-box face that closes and an
arithmetic / number-field / constructive face that stays open. This sharpens
6-for-6 / 7-for-7 from "parallel control-step walls" to "two avatars of one
control step, one proven one open."

### [[hodge_conjecture]] — the standard-conjectures link
Deligne proved RH over finite fields *without* the standard conjectures (via
clever reductions to curves + the Weil positivity on curves). But the
*motivic* / uniform route to RH — and the route that would give a
number-field analogue — would go through a Weil cohomology + standard
conjectures framework (Grothendieck). The **standard conjectures** (esp.
Lefschetz standard conjecture B = algebraicity of the inverse Lefschetz
operator, giving the Rosati-type positivity) are *the same* control step as
the Hodge conjecture's reduction (HC ⇔ standard conjectures B, C ⇒ motives
Tannakian ⇒ HC reduces to specific classes — see [[hodge_conjecture]]
attempt-02). So the standard conjectures are a **shared control step** for
Hodge (the analytic→algebraic bridge) and for a motivic RH (the number-field
Rosati positivity). Both are open; both hinge on the same positivity /
algebraicity of correspondences. This is a genuine Hodge↔RH link at the level
of the control tool, not just the lens.

### [[collatz_conjecture]] and [[navier_stokes]] — the slice→full control wall
The density→pointwise gap (Collatz) and the slice→full-3D control gap (NS)
are the same shape as RH's average→all-zeros gap. In all three the resolution
engine controls a slice / average and stops at the universal / pointwise /
every-instance control. RH's "almost all zeros near the line + zero-free
regions + verified up to $T$" ‖ Collatz's "a.a. orbits bounded + cycles
excluded up to $m=75$ + verified to $2^{71}$" ‖ NS's "2D solved + small-data
global + conditional regularity".

## Why RH is NOT a solved problem (contrast with [[poincare_conjecture]])
RH is open; the contrast case [[poincare_conjecture]] is the one problem where
the control step (Ricci-flow singularity control) *was* discharged — by
Perelman's $W$-entropy. For RH the analogous "right control tool" (a self-
adjoint operator, a proven positivity, or a number-field Rosati) is *not*
known. Poincaré is the existence proof that such walls can fall; RH is the
canonical instance of one still standing.