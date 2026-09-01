---
type: attempt
problem: beals_conjecture
attempt: 12
date: 2026-08-24
approach: Computationally strengthen attempt-04's degenerate-near-miss claim — exhaustively classify all (3,5,7) gap-1 near-misses and confirm min non-degenerate gap
outcome: confirmed
tags: [computation, near-miss, signature-357, degenerate-families]
loop_cycle: 10 of 20
---

# Attempt 12 — Exhaustive (3,5,7) gap-1 near-miss classification

Attempt-04 found $(3,5,7)$ gap-1 near-misses but noted they were "all
degenerate (one base $=1$)" without an exhaustive classification. This cycle
strengthens that to a precise statement via `scripts/search_357_nearmiss.py`.

## What the script does

1. **Gap-1 enumeration**: for every $C\in[1,200]$, both signs
   $A^3+B^5=C^7\pm1$, every $B\in[1,600]$, test whether $A^3=C^7\pm1-B^5$ is a
   perfect cube (exact integer cube-root check), within $A\le6000$.
2. **Family membership**: classify each hit against the two universal
   degenerate families
   - $t^{21}+1$: $A=t^7,\;B=1,\;C=t^3$ ($A^3+B^5=t^{21}+1=C^7+1$, gap $+1$),
   - $t^{35}+1$: $A=1,\;B=t^7,\;C=t^5$ ($A^3+B^5=1+t^{35}=C^7+1$, gap $+1$).
3. **Min non-degenerate coprime gap**: floor-cube-root nearest-cube search
   over all $(C,B)$ for $|A^3+B^5-C^7|$ with $A,B,C\ge2$ and $\gcd(A,B,C)=1$.

## Results

```
total gap-1 hits:            4
degenerate (a base==1):      4
genuine (all bases>=2):      0
all gap-1 on a universal family: True
unclassified gap-1 hits:     0
```
The four hits, all degenerate, all on a universal family:

| A | B | C | gap | family |
|---|---|---|---|---|
| 1 | 1 | 1 | +1 | $t^{21}+1$ ($t=1$) |
| 128 | 1 | 8 | +1 | $t^{21}+1$ ($t=2$) |
| 2187 | 1 | 27 | +1 | $t^{21}+1$ ($t=3$) |
| 1 | 128 | 32 | +1 | $t^{35}+1$ ($t=2$) |

Min non-degenerate coprime near-miss gap: **29** at $(A,B,C)=(5,2,2)$
($5^3+2^5=157$, $2^7=128$, $157-128=29$) — exactly matching attempt-04.

## Strengthened claim (vs attempt-04)

- attempt-04: "gap-1 near-misses present but all degenerate, from universal
  families $t^{21}+1$, $t^{35}+1$."
- attempt-12 (this): **exhaustively classified** — every gap-1 hit in the
  searched box ($A\le6000,B\le600,C\le200$) is degenerate AND lies on one of the
  two universal families; **zero** genuine (all-bases-$\ge2$) gap-1 near-misses
  exist in the box; the smallest genuine coprime near-miss is gap 29.

## Honest scope caveat

The gap-1 search caps $A\le6000$, so it rules out genuine gap-1 only for
$A\le6000$ (roughly $C\lesssim90$ with small $B$). Genuine gap-1 with large $A$
and large $C$ is *outside* the box and not ruled out by this computation. Two
mitigants: (1) the degenerate families are *parametric* (any $t$), so the
degenerate gap-1 phenomenon is fully explained for all $t$, not just those in
the box; (2) near-miss gaps concentrate at small bases (the global min, gap 29,
is at $A=5$), so the box very likely contains the genuine minimum — but
"likely," not "proven." The result is a strong empirical strengthening, not a
theorem.

## Outcome

**confirmed.** Attempt-04's degenerate-near-miss claim is now exhaustively
verified within the searched box: all gap-1 hits degenerate + on universal
families, 0 genuine gap-1, min genuine coprime gap 29. The distinct-prime
signature $(3,5,7)$ is empirically more rigid than cubic (which has
non-degenerate gap-1 Ramanujan-type near-misses) — consistent with the
five-thread diagnosis that no elliptic/cubic structure survives at $(3,5,7)$.

## Next cycles

- Targeted ingest: check whether direction (B) of attempt-11 — a
  *non-spherical reduction* to finitely many genus-$\ge2$ curves — has any
  nascent literature (one honest check before declaring it empty).
- A second Lint near loop end.
- Remaining cycles can also re-examine a neighboring distinct-prime signature
  (e.g. $(3,5,11)$) computationally to test whether the rigidity is uniform
  across the open class.