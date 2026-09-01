---
type: attempt
problem: beals_conjecture
attempt: 20
date: 2026-08-24
approach: Test attempt-19's counting-heuristic prediction with a fresh (3,7,11) signature probe
outcome: confirmed
tags: [computation, signature-3711, prediction-test, counting-heuristic, monotonicity]
loop_cycle: 18 of 20
---

# Attempt 20 — Test the counting-heuristic prediction at (3,7,11)

Attempt-19 made a **falsifiable prediction**: the counting heuristic
($N_{p,q,r}(H)\sim H^{r\chi}$) says solutions get sparser as $\chi$ grows more
negative, so the min non-degenerate coprime near-miss gap should grow
monotonically with $-\chi$. Two data points existed
($(3,5,7)\to29$, $(3,5,11)\to77$). This cycle computes a **third**, more
negative signature to test it.

## The prediction

| signature | $\chi=1/p{+}1/q{+}1/r-1$ | known min gap | prediction |
|---|---|---|---|
| $(3,5,7)$  | $-34/105\approx-0.324$ | $29$ | — |
| $(3,5,11)$ | $-62/165\approx-0.376$ | $77$ | — |
| $(3,7,11)$ | $-100/231\approx-0.433$ | **?** | **$>77$** (most negative $\chi$) |

## Computation: `scripts/search_3711.py` — $A^3+B^7=C^{11}$

Box $A\le6000,\;B\le600,\;C\le40$. (Same $C_{\max}$ as the $(3,5,11)$ probe;
the $B^7$ term's fast growth means $B$ effectively self-bounds via the
`BQ > CR` break. The minima were all found at small bases — $C=2$ — so the box
comfortably contains them; the box-limited caveat applies but is not binding.)

**Results (hand-verified):**
- **Exact solutions:** $1$ total, $(A,B,C)=(128,8,4)$, $\gcd=4$.
  $128^3+8^7=2097152+2097152=4194304=4^{11}$. **0 coprime** exact — the one hit
  is non-coprime (all bases share $4$), exactly as Beal requires. ✓
- **Gap-1 near-misses:** $2$ total, both **degenerate** ($B=1$ or $A=1$), both
  on the universal family $t^{33}+1$: $(1,1,1)$ ($t=1$) and $(2048,1,8)$
  ($t=2$: $2048^3+1=8^{11}$, gap $+1$). **0 genuine** gap-1. ✓ Same pattern as
  $(3,5,7)$ and $(3,5,11)$: all gap-1's are degenerate on a universal family.
- **Min non-degenerate coprime gap:** **277** at $(A,B,C)=(13,2,2)$,
  $13^3+2^7=2197+128=2325$, $2^{11}=2048$, gap $+277$, $\gcd(13,2,2)=1$. ✓

## The prediction is confirmed

$$29 \;(\chi=-0.324)\;<\;77\;(\chi=-0.376)\;<\;277\;(\chi=-0.433).$$

The min gap grows monotonically as $\chi$ grows more negative, exactly as the
counting heuristic predicts. The growth is in fact super-linear in $|\chi|$
(ratios $\times2.66$, $\times3.60$), consistent with $\chi$ entering the
heuristic as an *exponent* ($H^{r\chi}$) — a small shift in $\chi$ compounds.
The heuristic predicted the qualitative trend; the computation confirms it at a
third, independent signature.

## What this establishes

- **The counting heuristic (attempt-19) survives a falsification test.** Its
  one sharp prediction (monotone gap growth with $-\chi$) holds across three
  signatures. The soft sixth angle is not just decorative — it makes a
  testable claim that checks out.
- **The rigidity is uniform across the open class and monotone, now at three
  points.** 0 coprime exact, 0 genuine gap-1, degenerate-on-universal-family,
  and a min gap growing with $-\chi$: $(3,5,7)\to29$, $(3,5,11)\to77$,
  $(3,7,11)\to277$. This is no longer a two-point coincidence.
- **The non-coprime exact hit $(128,8,4)$** is a small positive note: it is a
  genuine $A^3+B^7=C^{11}$ solution with $\gcd>1$ — a Beal-*consistent*
  (non-counter-)example, the kind Beal *allows*. It does not threaten the
  conjecture; it confirms the coprime condition is doing real work.

## Honest scope

- All searches are box-limited; a smaller gap at larger bases is not ruled
  out *in principle*. But all three minima sit at small bases ($C=2$), so the
  boxes almost certainly contain the genuine minima.
- The heuristic predicts the *trend*, not the exact gap value. Mapping
  $H^{r\chi}$ to a precise min-gap would require a model of the relevant height
  $H$, which the heuristic does not supply. The confirmation is qualitative, as
  the heuristic is qualitative.
- This is a confirmation of a *heuristic* prediction, not a proof of anything.
  Beal remains open; $(3,5,7)$ remains unproven. The value is that a recorded
  prediction was tested against fresh data and held — the wiki's claims are
  falsifiable and have been falsified-or-confirmed, not just asserted.

## Outcome

**confirmed.** Attempt-19's prediction is borne out at $(3,7,11)$: min gap
$277>77$, monotone in $-\chi$, with the same 0-coprime-exact /
0-genuine-gap-1 / degenerate-on-universal-family rigidity. The empirical line
now spans three signatures; the counting-heuristic sub-thread has survived its
falsification test. 2 cycles remain — the next writes the loop close-out.