---
type: attempt
problem: beals_conjecture
attempt: 23
date: 2026-08-24
approach: Cross-problem loop cycle 6 (occasional beals cycle-in). Extend the empirical line to a fourth signature (5,7,11) via a box-limited computation, testing the attempt-19 counting-heuristic prediction (min non-degenerate coprime gap grows monotonically with -chi), confirmed at (3,7,11) in attempt-20
outcome: confirmed
tags: [computation, counting-heuristic, empirical-extension, prediction-confirmed, cross-problem]
---

# Attempt 23 — Fourth signature (5,7,11): prediction confirmed, growth decelerates

Cross-problem math-work loop, cycle 6. Beals was cycled in occasionally (per the
rotation bias rule) now that the five attempt-01-only problems each have an
attempt-02. The prior 20-cycle beals arc closed out in attempt-22 with the
honesty guard "genuine angles exhausted within this arc's scope"; the resume
point there explicitly sanctioned *"Extend the empirical line to a fourth
signature if a new prediction is worth testing."* This cycle does exactly that
— a falsifiable computation, not a re-derivation or padding.

## The prediction being tested

The counting heuristic (attempt-19, the soft 6th angle
[[method-counting-heuristic]]) predicts that the **min non-degenerate coprime
near-miss gap** grows monotonically as $\chi=1/p+1/q+1/r-1$ grows more negative.
Confirmed at three signatures:

| signature | $-\chi$ | min coprime gap |
|---|---|---|
| $(3,5,7)$  | $0.324$ | 29 |
| $(3,5,11)$ | $0.376$ | 77 |
| $(3,7,11)$ | $0.433$ | 277 |

The $(3,7,11)$ value (277) was *predicted* (attempt-19) before it was computed
(attempt-20). This run adds a fourth point: **$(5,7,11)$**, $\chi=-218/385\approx
-0.566$ — more negative than $(3,7,11)$ — so the prediction is **min gap $>277$**.

## Computation

Script: `scripts/search_5711.py` (mirrors `search_3711.py` exactly, adapted to
$A^5+B^7=C^{11}$). Box: $A\le6000$, $B\le600$, $C\le40$ (same shape as the
$(3,7,11)$ run). Universal degenerate gap-1 families for $(5,7,11)$:
- $t^{55}{+}1$: $A=t^{11},B=1,C=t^{5}$ ($A^5=t^{55},C^{11}=t^{55}$, gap $+1$) — $[\mathrm{lcm}(5,11)=55]$
- $t^{77}{+}1$: $A=1,B=t^{11},C=t^{7}$ ($B^7=t^{77},C^{11}=t^{77}$, gap $+1$) — $[\mathrm{lcm}(7,11)=77]$

## Results

- **Exact solutions $A^5+B^7=C^{11}$:** **0** (0 coprime). No Beal
  counterexample in the box — consistent with all prior signatures.
- **Gap-1 near-misses $|A^5+B^7-C^{11}|=1$:** **2 total, 0 genuine** (both
  degenerate). Both lie on the $t^{55}{+}1$ universal family:
  - $t=1$: $A=B=C=1$ (trivial);
  - $t=2$: $A=2048=2^{11},B=1,C=32=2^{5}$ — $(2^{11})^5+1=(2^5)^{11}$, i.e.
    $2^{55}+1=2^{55}+1$.
  - **All gap-1 hits on a universal family: True.** Same rigidity as the
    prior three signatures (every gap-1 near-miss is degenerate on a
    $t^{\mathrm{lcm}(\cdot,\cdot)}{+}1$ family; **0 genuine** gap-1).
- **Min non-degenerate coprime gap: $\boxed{288}$** at $(A,B,C)=(11,4,3)$:
  $$11^5+4^7-3^{11}=161051+16384-177147=288,\quad \gcd(11,4,3)=1.$$

## Prediction confirmed — with a nuance

The monotone trend **holds**: $29<77<277<288$. The counting-heuristic
prediction (min gap $>277$) is **confirmed** at a fourth signature. This is the
second *a-priori* confirmation (the first was $(3,7,11)$ in attempt-20).

**But the growth decelerated sharply:**

| step | $-\chi$ increase | min-gap increase |
|---|---|---|
| $(3,5,7)\to(3,5,11)$  | $+0.052$ | $29\to77$ ($+48$) |
| $(3,5,11)\to(3,7,11)$ | $+0.057$ | $77\to277$ ($+200$) |
| $(3,7,11)\to(5,7,11)$ | $+0.133$ | $277\to288$ ($+11$) |

The largest $-\chi$ jump ($+0.133$, more than double the prior step) produced
the **smallest** gap increase ($+11$). So the trend is monotone but **sub-linear
in $-\chi$** in this range — not the accelerating growth the three prior points
might have suggested. This is a genuine, falsifiable nuance: a fourth data
point refined the heuristic from "grows with $-\chi$" to "grows with $-\chi$ but
decelerating." It does **not** refute the counting heuristic (which only
predicts growth, not a rate), but it bounds how cleanly the rate tracks $-\chi$.

**Hypothesis for the deceleration (to test, not asserted):** as $-\chi$ grows
the exponents grow, the admissible bases shrink (the box's binding constraint
shifts toward smaller $C$), and the gap-1 degenerate families become denser
relative to the genuine search space — so the *nearest* non-degenerate
coprime hit can sit close to a degenerate family's "edge," capping the gap
growth. The $(5,7,11)$ minimum sits at the small base $C=3$ (between the
$t^{55}{+}1$ family's $C=2^5=32$ and the trivial $C=1$), consistent with this.
A fifth signature (e.g. $(5,7,13)$ or $(7,11,13)$) would test whether the
deceleration continues or reverses.

## Honesty / scope

- **Box-limited.** $C\le40$ is the binding constraint (the min sits at $C=3$,
  well inside; $A,B$ ranges over-cover). Same caveat as the prior runs:
  "minima sit at small bases ($C=2$), so boxes likely contain the genuine
  minima" — here the min is at $C=3$, still small, so the box very likely
  contains the genuine minimum. Not a proof that 288 is the global minimum;
  a strong empirical lower bound for the box.
- **The counting heuristic is a heuristic, not a theorem** (the soft 6th
  angle). Confirmation of a monotone trend is evidence *for the heuristic*,
  not a proof of Beal — it gives "small expected count / finiteness, not zero"
  (the same wall as always; attempt-19).
- No proof of Beal, no proof of even $(3,5,7)$. Outcome: **confirmed** (the
  specific prediction was confirmed; the heuristic refined), **partial**
  overall.

## Cross-problem compounding

This cycle-in demonstrates the loop's discipline extends to the most-developed
problem without padding: a *falsifiable* computation that produced a genuine
refinement (deceleration), not a re-derivation. The counting-heuristic angle
is Beals' instance of the cross-problem "evidence/counterevidence" branch of
the [[research-protocol]] (generate evidence AND counterevidence) — and the
fourth data point is mild counterevidence *for the rate* while confirming the
*direction*. Same honesty-over-optimism discipline that caught the Palasek
mislabel (NS attempt-02) and the $(2,3,7)$ spherical mislabel (beals attempt-17).

## Next

- **Fifth signature** (e.g. $(5,7,13)$, $-\chi\approx0.582$, or $(7,11,13)$)
  to test whether the deceleration continues or reverses — the natural
  extension of this empirical line.
- Or return to the structural directions (A)/(B) from attempt-22's resume
  point — extending Darmon's Frey-variety method, or an effective-finiteness
  mechanism bypassing the finite-triangle-group requirement.
The rotation continues: next cross-problem cycle re-enters the five-problem
rotation (second pass), not beals.