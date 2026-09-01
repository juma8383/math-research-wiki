---
type: method
name: RH positivity equivalences (Weil / Li / Bombieri–Lagarias / Suzuki)
created: 2026-08-31
tags: [number-theory, zeta, explicit-formula, equivalence, obstruction]
used-in: [[riemann_hypothesis]]
provenance: [[riemann-hypothesis-attempt-01]]
---

# RH positivity equivalences — the exact sign-control reductions

> **When to reach for it.** You want RH converted into a *single* checkable
> condition (an inequality, a sign, a spectrum) instead of a quantifier over
> all zeros. These four equivalences are the standard compressions; they are
> *exact*, so any attack must either discharge the sign condition with new
> machinery or fail. Reaching for them is easy; discharging them has never
> been done — they are the cleanest known statements of the RH control step.

## The four equivalents (all classical, `[summary]` — verify against paper
bodies before load-bearing reuse)

1. **Weil positivity (explicit formula).** For test functions $h$ with
   compactly supported Fourier transform, the Weil distribution
   $$\sum_\rho \widehat h(\rho)\widehat h(1-\bar\rho) \le
   \int h'\,\overline{h'} + (\text{prime terms})$$
   for all admissible $h$ ⟺ RH. The distribution is Hermitian but
   indefinite off the line; RH ⟺ its positivity on the whole space.
2. **Li's criterion (Li 1997, JNT 65, 325–333).** With
   $\lambda_n=\frac{1}{(n-1)!}\frac{d^n}{ds^n}\left[s^{n-1}\log\xi(s)\right]_{s=1}
   =\sum_\rho\left[1-\left(1-\tfrac1\rho\right)^n\right]$,
   RH ⟺ $\lambda_n\ge0$ for all $n$. The $\lambda_n$ are real (functional
   equation) and $\lambda_1=1$; the sequence is provably $\ge0$ up to
   computations (for the first many $n$) — and $\lambda_n<0$ for one $n$
   would be a *finite certificate* of a counterexample to RH.
3. **Bombieri–Lagarias 1999** (*J. Number Theory* **77** (1999), no. 2,
   274–287, doi:10.1006/jnth.1999.2392 — *not* Acta Arithmetica; an earlier
   wiki/conjecture-page genre of citation said the class extension was
   theirs). Their actual theorem is stronger and more structural: positivity
   of the Li sequence for all $n$ follows from a general inequality for
   **arbitrary multisets** of complex numbers satisfying the four-fold
   symmetry $\rho,1-\rho,\bar\rho,1-\bar\rho$ — the criterion is therefore
   *not zeta-specific* at this level — plus an arithmetic formula for
   $\lambda_n$ via the Guinand–Weil explicit formula and the equivalence
   with Weil's positivity criterion. The **Selberg-class** extension in
   particular is later work: **Omar–Mazhouda 2006** (JNT 125, 50–58) /
   **2009** (JNT 130, 1098–1108), and Lagarias 2007 (Ann. Inst. Fourier 57,
   1689–1740) for automorphic $L$-functions. Same consequence as recorded
   below for Davenport–Heilbronn-type inputs: functions with functional
   equation but no Euler product have the symmetry, so the *symmetry alone
   cannot carry RH* — the Euler product must do the work.
4. **Suzuki 2023 (screw functions / Kreĭn).** Suzuki, *Aspects of the
   screw function corresponding to the Riemann zeta-function* (J. London
   Math. Soc., DOI 10.1112/jlms.12785; arXiv:2206.03682) — paper-body
   verified at search level 2026-09-01: **Thm 1.2:** RH ⟺ $g(t)=-\Psi(t)$
   (Ψ built from von Mangoldt + Hurwitz–Lerch + gamma terms) is a screw
   function in Kreĭn's class $\mathcal G_\infty$; **Thm 1.3:** Weil-
   positivity analog on finite intervals $\mathfrak C_0(a)$; **Thm 1.5:**
   the kernel operator $G_g[a]$ on $L^2(-a,a)$ is trace class
   *unconditionally* (so the machinery is unconditional even though the
   positivity is not); **Thm 1.8:** RH ⟺ all Hankel determinants
   $\det\Delta_n,\det\Delta_n^{(1)}\ge0$ built from the Stieltjes moments
   $\mu_n=\int_0^\infty 4^{-1}e^{-t/2}\Psi(t)t^n\,dt$ (Stieltjes-moment
   uniqueness via $\Psi(t)\ll e^{t/2-c\sqrt t}$); §8 gives explicit
   moment ↔ Li-coefficient relations. A fifth exact sign-control
   compression: the same positivity, discretized into Hankel
   determinants.

## Control-step shape (why this toolbox matters)

Each is an **exact** reduction of a universal quantifier over zeros to a
sign condition — the control step isolated. The shared failure: *no
positivity input*. The Weil form's prime side is only bounded below by
positivity of $|\cdot|^2$ terms; the missing piece is exactly a positivity
statement that is *itself* RH-equivalent in strength.

**Bandwidth caution (new 2026-08-31, `[rh-bandwidth-ceiling-verified]`):**
the Alpöge–Furman ceiling $p_0\le0.6818287$ shows what happens when one
*computes* with finite compressions of the Weil form: any certificate
reading only the first two trace moments at Fourier support 1 is provably
capped at ≈0.682 of zeros certified. Positivity discharges for *all* zeros
are outside that class — but the ceiling is a quantitative warning that the
finite-compression engine has a proved stopping point.

**Partial positivity in the literature (search-verified 2026-08-31,
`[summary]`):** the Connes–Consani program has *proved* Weil positivity
only on restricted test classes — arXiv:2006.13771 (Sonin spaces, prolate
spheroidal wave functions) gives positivity for support in
$[2^{-1/2},2^{1/2}]$ with boundary conditions, and arXiv:1910.14368
diagnoses the general obstruction via an inner-function criterion (the
cutoff factors $u_\infty,u_p$ fail to be inner — unbounded in the right
half-plane), killing X.-J. Li's 2019 attempt. The two facts are the same
story from two sides: positivity is attainable on *small* Fourier supports
(Connes–Consani constructively), and even the widest certificates that
stay inside small support are provably capped (the bandwidth-one ceiling,
quantitatively). Any Weil-positivity discharge must therefore either
handle unrestricted support or escape the finite-compression class
entirely.

## See also

- [[riemann_hypothesis]] — the three control-reductions in progress.md;
  (B) is this page.
- [[thm-zero-density-ladder]] — the average/density engine these
  equivalences would need to beat.
- [[method-two-avatars-control-step]] — the Rosati-positivity parallel in
  the geometric avatar.