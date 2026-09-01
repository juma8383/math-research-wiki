# Progress — Riemann Hypothesis

> Running state. **Read this first when resuming.** Consolidated through
> **attempt-01** (2026-08-25).

## Status — OPEN (the Millennium target)

The Riemann Hypothesis is **open**. It is the one Clay Millennium problem that
was missing from the wiki (now added as the 9th problem — 8 prior: 7 open +
the solved [[poincare_conjecture]] contrast case). Unlike Poincaré this is a
genuine attack; unlike [[PvsNP]] it is squarely classical analytic number
theory, sharing the number-theory / geometry substrate of [[beals_conjecture]],
[[birch_swinnerton_dyer]], [[hodge_conjecture]].

## The exact frontier

See [problem.md](problem.md). In one line: all zeros verified on the line up
to height $3\cdot10^{12}$ (Platt–Trudgian 2021); zero-free regions and zero-
density estimates control zeros *near* $\Re=1$ and *on average*; $\ge 41.7\%$
of zeros provably on the line (2020); the open content is **every** zero.

## The central obstruction — the control step, not the resolution step

The wiki's 7-for-7 methodology ("the obstruction is at the control/reduction
step, not the resolution step"; "one-dimensional engine stops") reads cleanly
here, in the same shape as [[collatz_conjecture]] (density → pointwise) and
[[navier_stokes]] (slice → full):

- **Resolution machinery works on slices / on average.** (i) Computational
  verification places the first $\sim10^{13}$ zeros on the line — a slice (up to
  height $T$). (ii) Density results — Selberg's theorem (almost all zeros lie
  within *any* strip $|\Re(s)-\tfrac12|<\varepsilon$), zero-density estimates
  (Ingham/Huxley/Guth–Maynard bounding $N(\sigma,T)$), and proportion results
  (Levinson/Conrey: $\ge\tfrac13,\tfrac25,\dots$ of zeros on the line) — control
  zeros *on average*. (iii) Zero-free regions rule out zeros near $\Re=1$.
  These are the resolution layer; they work.
- **The wall is the control step to full strength.** Promoting "checked up to
  $T$" / "almost all" / "at least $X\%$" to **every zero, every height** is
  exactly the open step. The functional equation gives a *symmetry*
  ($\Re(s)\leftrightarrow1-\Re(s)$), which is a resolution-layer fact — but
  symmetry pairs zeros without pinning them; forcing $\beta=0$ is control.
  This is the precise analogue of Collatz's "density → pointwise" gap: average
  / density control is *not* the same as pointwise / universal control.

The wall has **three exact control-reductions** (each turns RH into a single
property one then cannot discharge):

1. **Hilbert–Pólya (spectral).** RH ⟺ the non-trivial zeros are eigenvalues of
   a self-adjoint operator $D$ on a Hilbert space (then real eigenvalues +
   the functional-equation symmetry ⟹ zeros on the line). The control tool
   *would be* self-adjointness; **no such operator is known**. Connes (1997,
   2019) builds a spectral interpretation from the adele-class space /
   noncommutative geometry and reduces RH to the validity of a trace formula
   (a Weil-positivity statement) — but the operator is not constructed as
   self-adjoint on a space whose spectrum is *exactly* the zeros; the
   "absorption spectrum" has a minus-sign / Riemannian-space obstruction
   (Connes's own framing). **Control step = self-adjointness, undischarged.**
2. **Weil / Bombieri–Lagarias / Li (positivity).** RH ⟺ the positivity of a
   distribution (Weil's explicit-formula distribution $\ge0$ for all test
   functions); equivalently (Li 1997, Bombieri–Lagarias 1999) the **Li
   coefficients** $\lambda_n=\frac{1}{n!}\frac{d^n}{ds^n}\big[s^{n-1}\log\xi(s)\big]_{s=1}\ge0$
   for all $n$; Suzuki 2023 (J. London Math. Soc., DOI 10.1112/jlms.12785)
   gives screw-function (Kreĭn) equivalents. **Control step = proving the
   positivity / $\lambda_n\ge0$ for all $n$ — not done.** Each is an *exact*
   reduction of RH to a sign/positivity control; none is dischargeable with
   current tools.
3. **Function-field analogy (the engine that works, then stops).** RH *for
   curves and varieties over finite fields* is a THEOREM — Weil (1940s) for
   curves, Deligne (1973/74) for all varieties (the Weil conjectures), via
   étale cohomology + the Lefschetz trace formula + the **positivity of the
   Rosati involution** / Riemann–Roch (Frobenius eigenvalues are Weil numbers,
   $|\alpha|=q^{-n/2}$). The engine stops at the number field: there is **no
   Frobenius and no Rosati positivity in characteristic 0**, so the
   function-field control tool does not translate to $\zeta(s)$. This is the
   cleanest "one-dimensional engine stops" instance: a control tool that
   exists in one avatar (function field) and is absent in the other (number
   field).

## The two-avatars structure (the deepest cross-problem link)

RH has the same **two-avatars** structure already found in
[[birch_swinnerton_dyer]] (attempt-07) and [[PvsNP]] (notes.md):

- **Function-field avatar:** RH for varieties over $\mathbb F_q$ — **PROVEN**
  (Weil; Deligne). The geometric avatar.
- **Number-field avatar:** RH for $\zeta(s)$ over $\mathbb Z/\mathbb Q$ —
  **OPEN** (the Millennium target). The arithmetic avatar.

This is the *same* shape as BSD's function-field BSD (proven via Kato–Trihan,
the Hodge-link avatar) vs number-field BSD (open, the Millennium). RH and BSD
are thus **twin two-avatar problems**: in each, the function-field /
geometric avatar is proven and the number-field / arithmetic avatar is open,
and the obstruction in both is that the function-field control tool
(Frobenius/Rosati for RH; Euler-system + étale cohomology for BSD) has no
known characteristic-0 / number-field translation. This sharpens the wiki's
6-for-6 / 7-for-7 from "parallel control-step walls" to "two avatars of the
same control step, one proven one open" — a structural equivalence at the
methodological level, now seen in RH, BSD, and PvsNP alike. (Structural
analogy, not mathematical equivalence — same disclaimer as the PvsNP
extension.)

## 2024-26 advances (status re-checked by the 2026-08-31 hunt scan)

- **Guth–Maynard 2024** — now **published**: *Annals of Math.* (2) **203**
  (2026), no. 2, 623–675 (arXiv:2405.20552). Exact statement:
  $N(\sigma,T)\le T^{\frac{15(1-\sigma)}{3+5\sigma}+o(1)}$; PNT in intervals
  $x^{17/30+o(1)}$. NUANCE (scan correction): the previous best in the range
  $\sigma\le\tfrac34$ was **Huxley 1972** ($12/5$), not Ingham directly —
  the accurate claim is "first substantive improvement since Ingham 1940 in
  the $\sigma\le\tfrac34$ range." **Resolution-on-average.**
- **Chourasiya 2024** (arXiv:2412.02068) — **DOWNGRADED** `[rh-chourasiya-flagged]`:
  an automated audit (Pith Review) flags that the proof as written concludes
  the original Carlson exponent $(\log T)^4$, not the advertised $5-2\sigma$
  (imported KLN lemma hypotheses unverified for the mollifier), and
  Chourasiya–Simonič 2025 (arXiv:2507.15184) explicitly supersedes it with
  log exponent $(7-5\sigma)/(2-\sigma)$. The wiki's earlier
  "improves the log exponent from 4 to $5-2\sigma$" line was WRONG as a fact
  about what Chourasiya achieved. Same publication-status discipline as NS /
  Collatz / YM claimed-result flags.
- **`[rh-2026-claims-non-journal]`** (was `[rh-2024-claims-unverified]` —
  identified and upgraded 2026-08-31): the $\ge\tfrac23$ claim is
  **arXiv:2608.13637 (Aug 2026)**, Alpöge–Furman (two authors; the arXiv
  Comments field notes autonomous-AI discovery — do not credit Claude as an
  author): $\ge0.6725$ of zeros
  **simple AND on the critical line**, $\ge\tfrac56$ distinct (prior record
  $\tfrac{5}{12}$ (PRZZ 2020); intermediate rung Wu 2015 $\ge0.6603$, absent
  from the wiki's earlier ladder). Method: unconditional Montgomery theorem
  (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, Acta Arith. 214, 2024) +
  von Neumann rank–trace inequality + Sylvester's law of inertia on finite
  compressions of Weil's Hermitian form; Theorems A/B Lean-4 formalized
  (`github.com/anthropics/formal-math`, project `zeta23/` — the earlier
  `zeta-23-lean` URL was the scan's; no `sorry`), read by Conrey/Goldston,
  **no journal peer review**. Still proportion-only; does not touch the
  control-to-all wall — as predicted.
- **Bandwidth-one ceiling — VERIFY-CONFIRMED 2026-08-31** `[rh-bandwidth-ceiling-verified]`
  (adversarial verify: §7.2 verbatim quotes obtained): the exact rational
  is $p_0\le0.6818287$ ("approximately 0.682") — the 0.68185 in the scan
  was a misrounding; a "0.70/0.80/0.90 need support 1.04/1.26/1.70"
  trajectory in the scan is **not in the paper and was deleted as
  scan-fabricated**. Supported §7.2 trajectory: past-$\tfrac23$ needs
  pair-correlation data beyond Fourier support 1; HL$(4)^*\Rightarrow
  \tfrac{13}{18}$; HL$(k_0)^*$ for all $k_0$ or full Montgomery form factor
  $\Rightarrow$ 100%; "RH itself is out of reach of the mechanism." See
  [problem.md](problem.md) for the full corrected statement.
- **DH-transfer question (verify-wave verdict: PLAUSIBLE, heavily
  undercut — filed as a question, not a result).** The scan asked whether
  arXiv:2608.13637's bandwidth-one certificate machinery **transfers to
  Davenport–Heilbronn-type zeta functions** (functional equation + positive-
  proportion on-line, but ≍T zeros off the line and *no Euler product*),
  so that RH-holding and RH-failing inputs are treated identically by the
  method. Verdict: correct moral, **established prior art** — the paper's
  own §1.4 concedes the inputs are insensitive to $o(N)$ off-line zeros
  (Bombieri–Hejhal Duke 80 (1995) 821–862 lineage; Selberg 1999; Karatsuba;
  Bombieri–Ghosh RMS 66 (2011) survey; Rezvyakova Izv. Math. 2026 gives
  unconditional positive proportion for Epstein zeta; Dousselin
  arXiv:2311.10285), and "RH itself is out of reach of the mechanism" is
  the paper's own §7.2 concession. Only narrow residue is genuinely open:
  whether the *specific rank-trace compression inequality* carries over
  verbatim and with what constant — and the honest frame is that
  bandwidth-one certificates can at most certify a positive-proportion
  on-line lower bound, never that the off-line proportion vanishes (for DH
  that set has $\asymp T$ elements). The scan's "if it fails, the failing
  input is the Euler product" dichotomy is **likely ill-posed and KILLED**.
  Noise flag: arXiv:2503.24275 claims DH zeros are *all* on the line —
  contradicts established theorems; disregard `[rh-dh-noise-flagged]`.

## Attempt log

- **attempt-01 (2026-08-25):** first attack. Statement + exact frontier
  verified (computational Platt–Trudgian $3\cdot10^{12}$; zero-free Korobov–
  Vinogradov; zero-density Ingham→Guth–Maynard 2024; proportion Levinson/Conrey
  → 5/12, plus the un-peer-reviewed 2/3 claim). Obstruction named = the
  control step (slice/average → every zero), with three exact control-
  reductions (Hilbert–Pólya self-adjointness; Weil/Li/Bombieri–Lagarias
  positivity; function-field Frobenius/Rosati proven, stops at the number
  field). Two-avatars structure identified = the [[birch_swinnerton_dyer]]
  twin (function-field proven / number-field open). ≥3 approaches + simpler
  equivalents (Li, Weil, Bombieri–Lagarias) + more-general statement (GRH /
  Selberg class / function-field RH) + computational evidence + counterevidence
  (de Branges failure; symmetry-doesn't-pin) + cross-problem lens. Outcome:
  **partial** (frontier mapped, obstruction framed; no proof move). Verified
  via 4 WebSearches (2 succeeded richly, 2 rate-failed); classical facts
  (Weil/Deligne, Hilbert–Pólya, Connes, Li, Bombieri–Lagarias, Suzuki 2023)
  search-confirmed; preprint/2024 details flagged to-verify against primary
  sources.

## To-verify (the load-bearing flags)

Status after the 2026-08-31 hunt scan (search-verified, not paper-body read):
Guth–Maynard (Annals 203(2) 2026, arXiv:2405.20552) — CONFIRMED published with
exact exponent; `[rh-2024-claims-unverified]` RESOLVED-UPGRADED to the precise
arXiv:2608.13637 identity + non-journal status; Chourasiya 2024 flag DOWNGRADED
(audited/superseded); Suzuki 2023 (JLMS DOI 10.1112/jlms.12785, Ths 1.2/1.5/1.8)
CONFIRMED at abstract level; Platt–Trudgian 2021 CONFIRMED (BLMS,
DOI 10.1112/blms.12460 — $3\,000\,175\,332\,800$, all zeros simple, and
downstream $\Lambda\le0.2$). Still open (not paper-body re-read):

~~The **bandwidth-one ceiling** and the §7.2 certificate-class details of
arXiv:2608.13637~~ — **RESOLVED 2026-08-31** by the adversarial verify wave:
exact rational $p_0\le0.6818287$ (`[rh-bandwidth-ceiling-verified]`); §7.2
verbatim; scan trajectory deleted as fabricated; attribution + Lean repo
corrected. See also the new theory pages: [[method-rh-positivity-equivalences]],
[[thm-zero-density-ladder]], [[method-two-avatars-control-step]].
~~**Li 1997**, **Bombieri–Lagarias 1999**~~ — **RESOLVED at search level
2026-08-31 (loop block):** Li 1997 = JNT 65, 325–333 (both forms of
$\lambda_n$ equal); **Bombieri–Lagarias 1999 = JNT 77(2), 274–287 (NOT Acta
Arith.)**, actual theorem: Li positivity from the four-fold zero symmetry
for *arbitrary multisets* + Guinand–Weil arithmetic formula + equivalence
with Weil positivity; the **Selberg-class extension is Omar–Mazhouda 2006/09
(JNT)**, and automorphic = Lagarias 2007 (AIF 57, 1689–1740) — the
attribution of the class statement to B–L was imprecise in this session's
positivity-equivalences page and the conjecture-page genre; page corrected.
Still open (paper-body standard):
- ~~Suzuki 2023~~ — **RESOLVED at search level 2026-09-01 (loop block):**
  theorems verified in detail (1.2: RH ⟺ $-\Psi(t)$ a Kreĭn screw
  function; 1.3: Weil-positivity analog on finite intervals; 1.5: trace
  class unconditionally; 1.8: Hankel/Stieltjes-moment determinants ≥ 0
  ⟺ RH; §8: moments ↔ Li coefficients). Toolbox page updated. **The
  RH to-verify layer is now fully resolved at search level** (remaining
  `[to-verify]`s: none load-bearing).
- ~~**Connes 1997/2019**, de Branges~~ — **RESOLVED at search level
  2026-08-31 (loop block):** **Connes 1999** = *Selecta Math.* (N.S.) **5**
  (1999), no. 1, 29–106 (IHES preprint M/98/72): critical zeros =
  **absorption spectrum**, non-critical zeros = resonances; the minus
  sign in Berry's $N_{osc}(E)$ shows the spectral interpretation must be
  *cohomological* (analogy with $H^1$ in the Lefschetz formula over
  function fields); the global trace formula on the adèle-class space
  ($C_k$ action) is **equivalent to RH for all L-functions with
  Grössencharakter** (Thm 5, via Weil-distribution positivity) — the
  precise "control step = trace-formula validity" statement. **Connes–
  Consani 2019** = arXiv:1910.14368 (*Scaling Hamiltonian*, J. Operator
  Theory): reconciles absorption vs Berry–Keating emission via Maslov
  phases, and **diagnoses the obstruction** — analyzing Li's 2019
  Weil-positivity attempt via an inner-function criterion (Lemma
  3.4/Cor 3.5): the cutoff factor functions $u_\infty, u_p$ are **not
  inner** (unbounded in the right half-plane), so the attempt fails;
  proposes semi-local framework (Conj 4.1, Scaling Site). **Connes–Consani
  2020** (arXiv:2006.13771, Sonin spaces / prolate spheroidal functions):
  Weil positivity **proved** for test functions supported in
  $[2^{-1/2},2^{1/2}]$ with boundary conditions — note this dovetails
  with the Alpöge–Furman bandwidth-one ceiling: positivity is only
  attainable on *small* Fourier supports, and the ceiling quantifies what
  such certificates can see. **de Branges** — no 2024–25 development; not
  accepted; Kvaalen's detailed commentary (2016, ~70 pp) finds false
  statements and unproven key steps in the 2015/2017 drafts; de Branges
  himself reportedly could not reconstruct a key 2006 step (MathOverflow);
  remains formally unrefuted but consensus = no valid proof `[summary]`.
- Suzuki 2023 (JLMS DOI 10.1112/jlms.12785, Ths 1.2/1.5/1.8) — abstract
  level confirmed by scan; paper-body read pending.
- **Deligne 1974** (Weil conjectures) — classical, heavily textbook-cited
  (Publ. Math. IHÉS 43); verify only if it ever becomes load-bearing in
  an attack.
- ~~Wu 2015 $\ge0.6603$ rung + PRZZ 2020 $\tfrac{5}{12}$ venue~~ —
  **RESOLVED at search level 2026-08-31 (loop block), with a genre
  correction:** Wu 2015 = Xianchang Wu, *Distinct zeros of the Riemann
  zeta-function*, **Quart. J. Math. 66 (2015), 759–771**: $\ge0.6603$ is the
  record for **DISTINCT zeros** (counting multiplicity), *not* the
  simple-and-on-line ladder — our earlier ladder note folded it into the
  wrong rung. The on-line proportion ladder is: Levinson 1974 ($>1/3$;
  simple by Heath-Brown 1979) → Conrey 1989 ($>2/5$) → Bui–Conrey–Young
  2011 (41.05%) → Feng 2012 (41.28%, caveated) → **PRZZ 2020** (Pratt–
  Robles–Zaharescu–Zeindler, *Res. Math. Sci.* 7, no. 2: $>5/12$ on the
  line, $>40.7\%$ simple AND on the line). Wu's distinct-zeros record was
  superseded by the $\ge5/6$ distinct claim of arXiv:2608.13637; his paper
  also gives 0.86957 for zeros of $\xi'$ on the line. Both now `[summary]`-
  verified; ladder in problem.md reads correctly through PRZZ.

## Next

- ~~Primary-source verification of the 2024-26 advances~~ — **DONE
  2026-08-31** (hunt scan + adversarial verify wave: Guth–Maynard Annals
  listing; arXiv:2608.13637 §7.2 verbatim + ceiling figure; Chourasiya
  downgraded; authorship/Lean-repo corrected).
- ~~Two-avatars `theory/methods/` page~~ — **DONE 2026-08-31**:
  [[method-two-avatars-control-step]] (with the Hodge standard-conjectures
  link), plus [[thm-zero-density-ladder]] and
  [[method-rh-positivity-equivalences]] (Weil/Li/Bombieri–Lagarias/Suzuki
  compressed into the toolbox).
- Remaining open directions: paper-body verification of the classical
  reductions (Connes 1997/2019, Li 1997, Bombieri–Lagarias 1999, Deligne
  1974) — the last `[to-verify]` layer in the frontier table; and any
  attempt-02 must state *which* zero-density rung and *which* Weil-form
  compression it uses, given the proved bandwidth-one ceiling.
- No claim to progress on RH itself; honest ceiling = frontier mapped,
  obstruction framed, twin identified, ceiling quantified.