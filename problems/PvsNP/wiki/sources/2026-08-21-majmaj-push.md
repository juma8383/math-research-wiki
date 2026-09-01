# Source — MAJ∘MAJ CAPP derandomization push (2026-08-21)

**Tags:** `[honest-ceiling]` `[majmaj-capp-route]` `[chen-williams-2019]` `[chen-ren-2020]` `[hmpt-1993]` `[tell-2018-quantified]` `[dilv-2024]` `[n2-wall]` `[chen-tell-2019]` `[majmaj-symmetry-deflated]` `[mining-program]`

**Provenance (honest):** Main-loop research push (no subagent fan-out — the prior `mcsp-deep-dive` fan-out exhausted the dispatching API account's session-usage limit, HTTP 429, so subagents remain unavailable). Grounded by web search against primary literature:
- Chen–Williams, *Stronger connections between circuit analysis and circuit lower bounds, via PCPs of proximity*, CCC 2019 ([10.4230/LIPIcs.CCC.2019.19](https://dl.acm.org/doi/10.4230/LIPIcs.CCC.2019.19)).
- Chen–Ren, *Strong average-case lower bounds from non-trivial derandomization*, STOC 2020 / SIAM J. Comput. 2022, ECCC TR20-010 ([10.1145/3357713.3384279](https://doi.org/10.1145/3357713.3384279); [ECCC](https://eccc.weizmann.ac.il/report/2020/010/)).
- Hajnal–Maass–Pudlák–Szegedy–Turán, *Threshold circuits of bounded depth*, JCSS 46(2):129–154, 1993 (FOCS 1987) ([10.1109/SFCS.1987.59](https://doi.org/10.1109/sfcs.1987.59); [JCSS](https://igi-web.tugraz.at/PDF/34.pdf)).
- Tell, *Quantified derandomization of linear threshold circuits*, STOC 2018.
- Derksen–Ivanov–Lee–Viola, *Pseudorandomness, symmetry, smoothing: I*, 2024.
- Servedio–Tan 2018 (depth-2 SYM/THR∘AND PRG); Viola 2019 (*Constant-error pseudorandomness proofs from hardness require majority*).

No proof of P≠NP, no lower bound, and no derandomization is claimed. The product is a **corrected map** and a **constructively sharpened open program**. `[honest-ceiling]` upheld throughout.

---

## The task (user's request)

> "Actually attack the MAJ∘MAJ CAPP question — survey the PRG/derandomization literature for symmetric-threshold classes, check whether MAJ∘MAJ's structure escapes the `[n2-wall]` single-polynomial obstruction, and either build the derandomization or prove the PRG lower bound."

Three sub-questions:
1. Does MAJ∘MAJ escape the `[n2-wall]` single-polynomial obstruction?
2. Is there a symmetry-exploiting PRG mechanism (small-bias / k-wise / NW-reconstruction) for MAJ∘MAJ?
3. Build the derandomization, or prove the PRG lower bound.

---

## Headline finding — a premise corrected `[majmaj-symmetry-deflated]`

The `maxip-push` source framed the reframed target `[majmaj-capp-route]` as a **"strictly weaker … not covered by the SETH Max-IP lower bounds"** route, with the open question *"does MAJ∘MAJ's majority-symmetry admit a PRG general THR∘THR lacks?"*

**This premise is directly contradicted by Chen–Williams (CCC 2019):** they prove a non-trivial `1/poly(n)`-error CAPP for poly-size **MAJ∘MAJ** exists **if and only if** one exists for poly-size **THR∘THR**. The two classes are **CAPP-equivalent** — a PRG/CAPP for either yields one for the other via the reduction. Therefore:

- The **SAT → CAPP** weakening (and the `AND2∘C / OR2∘C / ⊕2∘C` PCPP drop) is a *genuine* weakening and *does* escape the SETH Max-IP approximation lower bounds. **That part of the maxip-push framing survives.**
- The **MAJ∘MAJ vs THR∘THR** distinction is **illusory on the derandomization axis**: MAJ's symmetry does *not* make CAPP easier. A PRG that MAJ∘MAJ has but "general THR∘THR lacks" would *violate* the Chen–Williams iff. So the live open question is **not** "does MAJ∘MAJ admit a special PRG" — it is "does *any* non-trivial CAPP exist for this CAPP-equivalent pair at all."

This is an honest *downward* correction of my own prior source. Recorded as `[majmaj-symmetry-deflated]`.

---

## (1) Does MAJ∘MAJ escape the `[n2-wall]`?

**No — on two independent axes.**

- **Approximate-degree axis (the SAT route):** the `[n2-wall]` is a theorem about *single-polynomial approximate-degree representations* — threshold gates have F_p-approximate degree `Θ√t` `[alman-williams-2015]`, and MAJ shares *exactly* this approximate degree (MAJ is a symmetric threshold; symmetric threshold functions have approximate degree `Θ√t`). Composed degree `Θ√(mt)` is tight for THR∘THR *because* it is already tight for the sub-circuit OR∘AND that lives inside it — and MAJ∘MAJ likewise contains hard sub-structures. So on the single-polynomial SAT axis, MAJ∘MAJ hits the **same** wall as THR∘THR. The symmetry of MAJ gives no approximate-degree advantage over general THR.

- **CAPP-difficulty axis (the derandomization route):** by the Chen–Williams iff above, MAJ∘MAJ and THR∘THR are equally hard to derandomize. So MAJ∘MAJ does **not** escape the wall on the derandomization axis either.

**Conclusion:** MAJ∘MAJ does not escape the `[n2-wall]` obstruction. The only genuine escape from the single-polynomial SAT wall was already the **SAT → CAPP** step (Chen–Williams), not the MAJ∘MAJ specialization. The maxip-push framing conflated these two weakenings; this push separates them.

---

## (2) Is there a symmetry-exploiting PRG mechanism? — two natural routes, both bounded away

### Small-bias + noise — bounded away for threshold tests `[dilv-2024]`
Derksen–Ivanov–Lee–Viola (2024), *Pseudorandomness, symmetry, smoothing: I*:
- **Theorem 9 (negative):** small-bias distributions convolved with noise do **not** fool threshold tests (and small-space / small-depth tests) better than uniform — there exist threshold tests distinguishing small-bias+noise from uniform.
- **Theorem 7 (positive but narrow):** k-wise uniformity convolved with noise *does* fool **symmetric functions** with error `2^{-Ω(k)}`.

The implication for MAJ∘MAJ:
- A single MAJ gate *is* a symmetric threshold, so k-wise+noise (Thm 7) fools a *single* MAJ gate.
- But **MAJ∘MAJ is not symmetric over the input**: each bottom gate sees a *different* subset of variables, and the top gate aggregates. The composed function is not a symmetric function of the `n` input bits. So the symmetric-function PRG (Thm 7) does **not** lift directly to MAJ∘MAJ. This is a real, named obstruction to the "lift the symmetric-function PRG" idea.
- And the *cheap* small-bias+noise mechanism (the one that would seed the whole class cheaply) is *bounded away* for the threshold test itself (Thm 9).

So: the two most natural pseudorandomness mechanisms (small-bias+noise; k-wise+noise lifted from single symmetric functions) **do not** give a PRG for MAJ∘MAJ. No symmetry-exploiting PRG is known; the natural candidates are bounded away. `[dilv-2024]`

(Viola 2019, *Constant-error pseudorandomness proofs from hardness require majority*, adds a meta-observation: constant-error PRG *proofs/constructions* require TC⁰ power — a constraint on the *machinery* available to build such a PRG, not directly on fooling, but relevant to what derandomization tools are even in scope.)

### NW / hardness→randomness — the open *mining* program `[mining-program]`
Chen–Ren (STOC 2020) identify the constructive open problem precisely:
- **Known exponential lower bound:** Hajnal–Maass–Pudlák–Szegedy–Turán (JCSS 1993, FOCS 1987) prove IP2 (Inner Product mod 2) requires depth-2 threshold circuits of size ≥ `2^{(1/2−ε)n}` (Lemma 3.2; with arbitrary first-layer weights but polynomial output weight, `2^{(1/3−ε)n}`, Thm 3.6). This is a known explicit exponential lower bound against depth-2 threshold = a lower bound against MAJ∘MAJ (MAJ gates are a special case of threshold gates). `[hmpt-1993]`
- **The gap:** a circuit lower bound does **not** automatically yield a CAPP. The standard hardness→randomness conversion (Nisan–Wigderberg) turns a *hard, efficiently-computable* function into a PRG, but it requires a **reconstruction / list-decoding** tailored to the class being fooled. IP2 is explicit and efficiently computable, so the NW framework applies in principle; the missing piece is a reconstruction that fools **MAJ∘MAJ / THR∘THR** specifically. This is the "mining" question: *mine the known MAJ∘MAJ lower bound into a non-trivial CAPP*. `[mining-program]`
- **The payoff (Chen–Ren Thm 1.13):** a `2^n / n^{ω(1)}` CAPP for poly-size MAJ∘MAJ ⟹ **NEXP ⊄ MAJ∘MAJ∘MAJ = TC⁰₃**, *and* (via the Chen–Williams iff) NEXP ⊄ THR∘THR. Since exponential MAJ∘MAJ lower bounds are already known, Chen–Ren explicitly state TC⁰₃ lower bounds are "within reach." `[chen-ren-2020]`

So the genuine, *constructive* opening is not "exploit MAJ symmetry for a cheap PRG" (bounded away) but "build an NW-style reconstruction for threshold classes that converts the HMPT lower bound into a CAPP." This is a recognized hard open problem, not something I can resolve here — but it is now precisely located.

---

## (3) Build the derandomization, or prove the lower bound? — honest verdict

**Neither was achieved, and neither is claimed.** Both are recognized hard open problems:
- **Building the derandomization** = the mining program above = an NW reconstruction for MAJ∘MAJ / THR∘THR = a major result (would yield the first NEXP ⊄ THR∘THR and NEXP ⊄ TC⁰₃). Not solved.
- **Proving a PRG lower bound for MAJ∘MAJ** (showing no sub-linear-seed PRG fools it) would be a major *hardness-of-derandomization* result. The `[n2-wall]` and DILV Thm 9 *point toward* threshold being hard to fool, but a full PRG lower bound is not established. Not solved.

### The genuine quantitative lever that *is* within reach — quantified derandomization `[tell-2018-quantified]`
Tell (STOC 2018), *Quantified derandomization of linear threshold circuits*:
- A quantified-derandomization (q.d.) — circuits that accept/reject all but `B(n) = 2^{n^{1−1/5d}}` inputs — for TC⁰ of any constant depth `d ≥ 2` with `n^{1+exp(-d)}` wires, in `n^{O((log log n)²)}` time.
- A PRG for depth-2 linear threshold with `n^{3/2−Ω(1)}` wires, seed `Õ(log n)`, for the *promise* setting `B(n) = 2^{n^{Ω(1)}}`.
- **The lever:** a *modest improvement* of the wire bound `n^{1+exp(-d)} → n^{1+O(1/d)}` (i.e. the constant `c > 1` in `n^{1+c^{-d}}`) ⟹ non-trivial derandomization of **all** TC⁰ ⟹ **NEXP ⊄ TC⁰**. This is exactly the `[chen-tell-2019]` bootstrap lever already recorded in the wiki, now confirmed as the live quantified-derandomization improvement target.

This is the honest "next pushable thing": Tell already gives the q.d. PRG for the *promise* setting at `n^{3/2−Ω(1)}` depth-2 wires; the open improvement is the wire-count constant. It is a *promise* derandomization (not full CAPP), but it is the closest existing result to the target and the improvement is modest in the technical sense.

---

## Net honest outcome

1. **A premise of my own prior source is corrected** `[majmaj-symmetry-deflated]`: the maxip-push framing of `[majmaj-capp-route]` as a target where "MAJ∘MAJ's symmetry might admit a special PRG" is **deflated** — Chen–Williams (CCC 2019) proves MAJ∘MAJ and THR∘THR are CAPP-*equivalent*, so the symmetry yields no derandomization advantage. The *real* weakening (SAT→CAPP, plus the PCPP `AND2∘C` drop) survives and is what escapes SETH.
2. **MAJ∘MAJ does not escape the `[n2-wall]`** on either axis (approximate degree shared with THR; CAPP-equivalent to THR∘THR).
3. **Both natural PRG mechanisms are bounded away** `[dilv-2024]`: small-bias+noise fails threshold tests (Thm 9); k-wise+noise fools only single symmetric functions and does not lift to the non-symmetric MAJ∘MAJ composition (Thm 7).
4. **The genuine constructive opening is the mining program** `[mining-program]` `[hmpt-1993]` `[chen-ren-2020]`: convert the known HMPT exponential lower bound for depth-2 threshold (IP2 ∉ 2^{(1/2−ε)n}) into a non-trivial CAPP via an NW reconstruction for threshold classes. Payoff (Chen–Ren Thm 1.13): `2^n/n^{ω(1)}` CAPP for MAJ∘MAJ ⟹ NEXP ⊄ THR∘THR *and* NEXP ⊄ TC⁰₃.
5. **The within-reach quantitative lever is Tell's quantified-derandomization wire-count improvement** `[tell-2018-quantified]` (the `c>1` in `n^{1+c^{-d}}`, = the `[chen-tell-2019]` bootstrap lever), a *promise* derandomization, not full CAPP.
6. **No derandomization built; no PRG lower bound proved.** Both are recognized hard open problems. `[honest-ceiling]` upheld — the product is a corrected, sharpened, falsifiable map: one deflated premise, two bounded-away mechanisms, one constructive mining target, one within-reach quantitative lever.

### What changed vs the maxip-push source
- `[majmaj-capp-route]` description must be **corrected**: drop "MAJ∘MAJ's symmetry admits a PRG general THR∘THR lacks" — that is contradicted by the Chen–Williams iff. Replace with: the real weakening is SAT→CAPP (and the PCPP drop), and the live question is whether *any* non-trivial CAPP exists for the CAPP-equivalent pair.
- Add the mining program as the constructive sharpening, and Tell's q.d. lever as the within-reach quantitative target.
- Net: the MAJ∘MAJ push did **not** find an easier target (it proved the target is as hard as THR∘THR), but it **did** correct the framing and locate the genuine constructive opening (NW reconstruction for threshold classes) and the within-reach lever (quantified-derandomization wire count).

### Unverified / flagged for pre-publication check
- The claim that HMPT's depth-2 threshold lower bound applies *specifically* to MAJ∘MAJ (weight-restricted majority) gates: HMPT is for general threshold gates; MAJ is the unweighted special case, so the lower bound *transfers* (a lower bound against a larger class is a lower bound against the subclass), but whether a *stronger* bound is known specifically for unweighted MAJ∘MAJ is not separately verified here — flagged.
- DILV Thm 7's exact error bound `2^{-Ω(k)}` and Thm 9's exact advantage — quoted from the search summary; verify against the paper before any external use.
- Tell's exact wire bounds `n^{1+exp(-d)}` / `n^{3/2−Ω(1)}` and the `B(n)` promise — quoted from the search summary; verify.