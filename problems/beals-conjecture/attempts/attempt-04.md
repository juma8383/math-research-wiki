---
type: attempt
problem: beals_conjecture
attempt: 04
date: 2026-08-24
approach: Computational probe of the frontier signature (3,5,7): exact solutions + non-degenerate near-miss structure
outcome: partial
tags: [computation, signature-357, near-miss, degenerate-families]
loop_cycle: 2 of 20
---

# Attempt 04 — Empirical structure of the frontier signature $(3,5,7)$

attempt-01 found Beal "tight by 1" via the *general* search (mixed exponents),
notably the non-degenerate $9^3+10^3=12^3+1$. This cycle probes $(3,5,7)$
**specifically** — does the tight-by-1 phenomenon persist for a pairwise-distinct
prime signature, and is it non-degenerate? Script: `scripts/search_357.py`
($A\leq6000,\ B\leq600,\ C\leq200$; max sum $\sim7.8\times10^{13}$).

## Results

1. **Exact coprime solutions: 0.** Beal holds in range.
2. **Exact solutions of ANY kind: 0.** Unlike the cubic case (which had many
   $\gcd>1$ solutions, e.g. $3^3+6^3=3^5$), $(3,5,7)$ has *no* small solutions
   at all. The signature is empirically **more rigid** — there is no small
   "Fermat-Catalan-with-a-2" scaffolding (like $1+2^3=3^2$) to scale up, because
   the three distinct exponents don't align.
3. **Gap-1 near-misses: present, but ALL degenerate** (one base $=1$). They come
   from two infinite universal families:
   - $A=t^7,\ B=1,\ C=t^3$: $\;A^3 = t^{21} = C^7$, so $A^3+1 = C^7+1$ (gap 1).
     e.g. $128^3+1 = 8^7+1 = 2097153$.
   - $A=1,\ B=t^7,\ C=t^5$: $\;B^5 = t^{35} = C^7$, so $1+B^5 = C^7+1$ (gap 1).
     e.g. $1+128^5 = 32^7+1$.
   These exist because $A^p=C^r \iff A=t^{r/g}, C=t^{p/g}$ with $g=\gcd(p,r)$
   (here $\gcd(3,7)=\gcd(5,7)=1$). **Degenerate gap-1 near-misses are universal
   across ALL signatures** (set one base to 1 and equate the other two terms).
4. **Smallest NON-degenerate coprime near-miss: gap 29** —
   $5^3+2^5=157$, nearest $2^7=128$. The next: $13^3+2^5=2229 \sim 3^7=2187$
   (gap 42), $5^3+128^5 \sim 32^7$ (gap 125, but $B=128=2^7$ ties into the
   degenerate family). Filtering cleanly: non-degenerate near-misses for
   $(3,5,7)$ are *much looser* than the cubic case.

## Interpretation

- The **metric obstruction of attempt-01 still holds for $(3,5,7)$**: gap-1
  near-misses exist (degenerate), so "the sum is never close to a perfect
  power" is false. A density/metric proof cannot work here either.
- But there is a **new structural distinction**: for the cubic-cubic-cubic
  signature, gap-1 near-misses can be **non-degenerate** (Ramanujan
  $9^3+10^3=12^3+1$, $6^3+8^3=9^3-1$) — these are *arithmetic* coincidences on
  the elliptic curve $X^3+Y^3=Z^3\pm1$. For $(3,5,7)$, the only gap-1's are the
  *trivial* $1+$ perfect-power families; non-degenerate coincidences start at
  gap ~29. So distinct-prime signatures appear **empirically looser** than
  repeated-cubic ones — consistent with their being harder to attack (no
  exploitable near-miss arithmetic).

## What this suggests

The non-degenerate gap-1 near-misses in the cubic case trace to integral points
on the elliptic curve $X^3+Y^3 = Z^3 \pm 1$ (rank considerations). The
*absence* of such for $(3,5,7)$ hints the corresponding higher-genus object
($X^3+Y^5=Z^7\pm1$) has no small integral points — but this is exactly the
higher-genus/Faltings regime, not an elliptic curve. **This points the
Mordell-curve side angle (next cycle) at the cubic-cubic case, where the
arithmetic is genuine, rather than at $(3,5,7)$ where the near-misses are
trivial.**

## Caveat

"Min non-degenerate gap = 29" is range-dependent ($A\leq6000,B\leq600$); a
non-degenerate gap-1 for $(3,5,7)$ at huge bases cannot be ruled out by this
search. The robust claims are: (a) zero exact solutions in range, (b) all
in-range gap-1's are degenerate, (c) degenerate gap-1 families are universal.

## Next cycle

Promote the **Mordell-curve / elliptic-curve side angle** for the
**cubic-cubic-cubic** sub-case ($X^3+Y^3=Z^3\pm1$), where the non-degenerate
gap-1 near-misses live and the curve is genuinely elliptic — a non-modular
angle that may illuminate *why* the gap is exactly 1 and never 0.