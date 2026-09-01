---
type: attempt
problem: beals_conjecture
attempt: 24
date: 2026-08-24
approach: Fifth-signature (5,7,13) computation extending the counting-heuristic empirical line (min non-degenerate coprime near-miss gap vs -chi); test whether the attempt-23 deceleration continues or reverses
outcome: confirmed
tags: [computation, counting-heuristic, near-miss, cross-problem, deceleration-reversal, correction]
---

# Attempt 24 — (5,7,13): monotone HOLDS but the deceleration REVERSES (gap explodes 288→1771)

Cycle-22 Continue on Beals (cross-problem loop, second pass; **occasional
cycle-in** per the bias rule — first Beals visit this pass, after BSD/NS/YM/
Hodge/Collatz all reached attempt-05). Yellow zone (session 73% / weekly
65.3%, max 2 subagents; **0 subagents used** — direct computation to conserve
the session budget, which climbs toward the 80% orange trigger; resets in
~2h). Attempt-23's `Next` verbatim sanctioned this run:

> **Fifth signature** (e.g. $(5,7,13)$, $-\chi\approx0.582$, or $(7,11,13)$) to
> test whether the deceleration continues or reverses — the natural extension
> of this empirical line.

This cycle runs the $(5,7,13)$ probe (`scripts/search_5713.py`, mirroring
`search_5711.py`). $\chi=1/5+1/7+1/13-1=-264/455\approx-0.5802$ (so $-\chi\approx
0.580$, marginally more negative than $(5,7,11)$'s $-0.566$).

## Computation (box A≤6000, B≤600, C≤40)

- **Exact solutions** $A^5+B^7=C^{13}$: **0** (consistent — no nontrivial
  coprime solution, as Beals predicts for this signature).
- **Gap-1** $|A^5+B^7-C^{13}|=1$: **1** instance, the trivial degenerate
  $(A,B,C)=(1,1,1)$ on the universal $t^{65}+1$ family ($t=1$). **No genuine
  gap-1 near-miss** (all bases ≥2) — consistent with Beals.
  - *Box caveat (honest):* the two universal degenerate families for
    $(5,7,13)$ — $t^{65}+1$ ($A=t^{13},B=1,C=t^5$, $\mathrm{lcm}(5,13)=65$) and
    $t^{91}+1$ ($A=1,B=t^{13},C=t^7$, $\mathrm{lcm}(7,13)=91$) — **escape the box
    for $t\ge2$**: $t^{65}$ needs $A=t^{13}\le6000\Rightarrow t=1$ only
    ($2^{13}=8192>6000$), and $t^{91}$ needs $C=t^7\le40\Rightarrow t=1$ only
    ($2^7=128>40$). So "all gap-1 on a universal family" is here
    near-vacuous (only $t=1$ in box), unlike $(5,7,11)$ where the box caught
    several degenerate $t$. The families exist parametrically; the box just
    truncates them at $t=1$. Does not affect the min-gap result.
- **Min non-degenerate COPRIME near-miss gap: $\boxed{1771}$** at
  $(A,B,C)=(6,3,2)$, gap $=+1771$:
  $$6^5+3^7-2^{13}=7776+2187-8192=1771,\qquad\gcd(6,3,2)=1.$$

## The empirical line — updated (five signatures)

| $(p,q,r)$ | $\chi$ | $-\chi$ | min coprime gap | $\Delta$gap | $\Delta(-\chi)$ |
|---|---|---|---|---|---|
| $(3,5,7)$  | $-34/105\approx-0.324$ | 0.324 | 29  | — | — |
| $(3,5,11)$ | $-62/165\approx-0.376$ | 0.376 | 77  | +48  | +0.052 |
| $(3,7,11)$ | $-100/231\approx-0.433$| 0.433 | 277 | +200 | +0.057 |
| $(5,7,11)$ | $-218/385\approx-0.566$| 0.566 | 288 | +11  | +0.133 |
| $(5,7,13)$ | $-264/455\approx-0.580$| 0.580 | **1771** | **+1483** | **+0.014** |

The naive prediction "min gap grows monotonically as $-\chi$ grows" is
**CONFIRMED**: $29<77<277<288<1771$ — still strictly increasing. But the
**deceleration observed at $(5,7,11)$ (attempt-23: largest $-\chi$ jump
$+0.133$ gave the smallest gap increase $+11$) does NOT continue — it
REVERSES, sharply:** here the **smallest** $-\chi$ jump ($+0.014$, barely
moving — both triples share $p=5,q=7$, only $r$ changes $11\to13$) gives by
far the **largest** gap increase ($+1483$, a $6.1\times$ jump).

## What this means for the counting heuristic [[method-counting-heuristic]]

The honest sharpening: **the min gap is NOT a smooth function of $-\chi$.**
The five points are monotone in $-\chi$ but the rate is wildly erratic — the
last step moves $-\chi$ by 2.4% of its range yet the gap by 85% of the
observed range. Two consequences:

1. **The $-\chi$-alone heuristic is too coarse.** The specific exponent
   *structure* — here $r=11$ vs $r=13$, i.e. the granularity of attainable
   $C^r$ values near small $A^p+B^q$ — dominates over the scalar $\chi$. The
   $(5,7,11)\to(5,7,13)$ step isolates this: $p,q$ fixed, only the
   right-hand exponent grows, and the gap jumps $6\times$.
2. **The min is governed by small-base arithmetic, not by $\chi$.** A
   structural reason: the min gap sits at the smallest-scale corner
   ($(A,B,C)=(6,3,2)$ here, $(11,4,3)$ for $(5,7,11)$). At small $C$, the
   relevant $A$ is tiny ($\sim5\text{–}6$) and the local 5th-power spacing
   ($6^5-5^5=4651$) sets the gap scale; at larger $C$, $A$ grows and the
   5th-power spacing ($\sim A^4$) grows with it, so gaps grow. The min is
   systematically at the smallest $C,A$ — i.e. it probes the *fine
   arithmetic coincidence* at small bases, which is not captured by the
   smooth density/counting parameter $\chi$.

So the empirical line supports the *qualitative* Beals prediction ("coprime
near-misses get rarer / gaps grow as the signature gets more hyperbolic")
but **refutes any smooth quantitative $\chi\mapsto\mathrm{gap}$ law**: the
relationship is monotone-but-erratic, dominated by exponent-specific
arithmetic. This is the same "control is not smooth in the natural
parameter" flavor as the cross-problem 6-for-6 obstruction — but here it
is a *negative* result for the heuristic's predictive power, recorded
honestly (append-only; attempt-23's "deceleration" framing is left intact
and corrected by this point).

## Honesty / scope

- **Prediction "min gap > 288" CONFIRMED** ($1771\gg288$); monotonicity of
  the five-point line preserved.
- **Deceleration hypothesis (attempt-23: sub-linear, small increases)
  REFUTED** by this point — the increase is the largest observed, on the
  smallest $-\chi$ step. Append-only correction: attempt-23's framing was
  based on four points; the fifth reverses its rate trend.
- **Box caveat (restated):** this is a strong empirical *lower bound for the
  box* $A\le6000,B\le600,C\le40$, **not a proof that 1771 is the global
  minimum** over all $A,B,C$. The structural argument (min sits at smallest
  $C,A$; 5th-power spacing grows with $A$) makes 1771 robust as the box min,
  but a smaller gap at some large $C$ with a rare small-$A$ coincidence is
  not logically excluded. Flagged `to-verify` by a wider-box run if the
  line is pursued.
- The degenerate-family box-truncation caveat (only $t=1$ in box) is noted
  above; it does not touch the min-gap result.
- **Not a proof of Beals.** This is the soft 6th angle
  [[method-counting-heuristic]]; the five rigorous threads (Mordell-type
  finiteness, ABC-implication, modularity, etc.) remain the load-bearing
  structure. No change to the obstruction map (the open content "finitely
  many → zero" is untouched); this sharpens only the empirical heuristic's
  *predictive* reliability, in the negative direction.
- Outcome: **confirmed** (the run cleanly answers attempt-23's
  "continue-or-reverse" question: monotone continues, deceleration
  reverses), **partial** overall (heuristic sharpened but no proof move).

## Next (attempt-25)

Natural next moves for this empirical line: (a) a **wider-box run** on
$(5,7,13)$ (raise $C_{\mathrm{MAX}}$ and $A_{\mathrm{MAX}}$) to test the
1771 box-min's robustness / chase a possible smaller large-$C$ coincidence,
OR (b) a **sixth signature** — $(7,11,13)$ ($\chi=1/7+1/11+1/13-1\approx
-0.536$, *less* negative than $(5,7,13)$: a reverse-direction point that
would test whether the gap *decreases* for less-hyperbolic triples, a
stronger monotonicity probe), OR (c) leave the empirical line and return
to the rotation (the five-problem rotation resumes next cycle per the
bias rule — likely BSD attempt-06 or another problem's attempt-06).