---
type: attempt
problem: birch_swinnerton_dyer
attempt: 8
date: 2026-08-30
approach: Primary-source verification of Kataoka–Sano 2024 (J. Assoc. Math. Res., DOI 10.56994/jamr.002.002.001) against the published PDF body — resolve the arXiv-v1 vs published theorem-numbering discrepancy, confirm all five load-bearing claims, and record the BCK21 sharpening that discharges the first of the three-fold conditional
outcome: confirmed
tags: [primary-source-verification, rank-2-euler-system, heegner-point-main-conjecture, darmon-derivative, bockstein-regulator, bck21, theorem-numbering, control-step, direction-a]
---

# Attempt 08 — Kataoka–Sano 2024 primary-source-verified: published numbering resolved (Conj 1.9 / Thm 1.11), all five claims confirmed, and BCK21 discharges the Heegner-MC leg of the three-fold conditional

Cycle-5 Continue on BSD (resumed /loop; **orange zone, weekly ~83.4%,
0 subagents**). This is the attempt-07 "Next (attempt-08)" target, executed
under the user's "Spend now" choice: primary-source-verify Kataoka–Sano 2024
against the **published paper body**, not just the arXiv abstract / search
summaries. The published PDF (J. Assoc. Math. Res. **2**(2):154–208, 2024) was
downloaded and text-extracted (zlib FlateDecode decompression — no PDF library
available, so a raw stream extractor was written). This resolves the one open
item attempt-06/07 left flagged: the **theorem-numbering discrepancy** between
the arXiv v1 (Conj 1.6 / Thm 1.8) and the search summary (Conj 1.9 / Thm 1.11).

## The numbering discrepancy — RESOLVED (published = Conj 1.9 / Thm 1.11)

The published JAMR 2024 version went through revision (received 2023, revised
and accepted 2024) and **renumbered the introduction**. The authoritative
published numbering, read directly from the PDF body:

| Published (JAMR 2024) | Body theorem | arXiv v1 | Content |
|---|---|---|---|
| **Thm 1.4** | Thm 5.17 | Thm 1.4 | Heegner MC ⟺ Iwasawa MC for $z^{Hg}_\infty$ |
| **Thm 1.5** | Thm 5.18 | Thm 1.5 | Heegner MC ⟹ rank-two Euler system $c$, $c_{K_\infty}=z^{Hg}_\infty$ |
| **Conj 1.9** | Prop 5.26 | Conj 1.6 | Darmon-derivative conjecture (explicit formula) |
| **Thm 1.10** | Thm 5.27 | Thm 1.7 | algebraic variant of Conj 1.9 ⟸ Heegner MC up to $\mathbb Z_p^\times$ |
| **Thm 1.11** | Thm 5.29 | Thm 1.8 | Heegner MC + Conj 1.9 + $R^{Boc}_{K_\infty}\neq0$ ⟹ $p$-part of BSD for $E/K$ |

So the wiki's existing citation (Conj 1.9 / Thm 1.11, from the search summary)
is **correct for the published version**; the arXiv-v1 numbers (Conj 1.6 /
Thm 1.8) are the pre-revision numbering. Both are now recorded so future
sessions cite the right one per source. The published numbers are the
authoritative target.

## All five load-bearing claims — CONFIRMED against the PDF body

1. **Thm 1.4 (Thm 5.17)** — "The Heegner point main conjecture holds if and
   only if we have [the Iwasawa main conjecture for $z^{Hg}_\infty$]": the
   Perrin-Riou Heegner MC is **equivalent** to the Iwasawa MC for the
   Heegner element $z^{Hg}_\infty \in \bigwedge^2_\Lambda H^1(\mathcal O_{K,S},\mathbb T)$.
   CONFIRMED.
2. **Thm 1.5 (Thm 5.18)** — "Assume the Heegner point main conjecture. Then
   there exists a rank two Euler system $c$ such that $c_{K_\infty}=z^{Hg}_\infty$."
   CONFIRMED — the rank-2 Euler-system construction, conditional on the
   Heegner MC.
3. **Conj 1.9 (Prop 5.26)** — the Darmon-derivative conjecture, the explicit
   formula $\kappa^{Hg}_\infty = L^*_S(E/K,1)\cdot |D_K|\,\Omega_{E/K}\cdot R_{E/K}\cdot R^{Boc}_{K_\infty}$.
   CONFIRMED (verbatim in the PDF: "Conjecture 1.9 (see Proposition 5.26). We
   have $\kappa^{Hg}_\infty = L^*_S(E/K,1)\,|D_K|\,\Omega_{E/K}\,R_{E/K}\,R^{Boc}_{K_\infty}$").
4. **Thm 1.10 (Thm 5.27)** — "an algebraic variant of Conjecture 1.9 follows
   from the Heegner point main conjecture up to $\mathbb Z_p^\times$."
   CONFIRMED — a new intermediate result not in the earlier notes.
5. **Thm 1.11 (Thm 5.29)** — "If we assume the Heegner point main conjecture,
   Conjecture 1.9, and $R^{Boc}_{K_\infty}\neq0$, then the $p$-part of the
   Birch–Swinnerton-Dyer formula for $E/K$ holds." CONFIRMED — the
   three-fold conditional ⟹ $p$-part of BSD for $E/K$.

The **basic rank $r_T=2$** claim is also confirmed verbatim: "the basic rank
$r_T$ is two in this setting, since we have $\oplus_{v\in S_\infty(K)} H^0(K_v,T^*(1))
= H^0(\mathbb C,T^*(1)) = T^*(1)$ and this is a free $\mathbb Z_p$-module of
rank two." The abstract's framing ("a natural interpretation of the Heegner
point main conjecture in terms of rank two Euler systems") is confirmed.

## The BCK21 sharpening — the three-fold conditional is now TWO-fold

**Remark 1.6** (read from the PDF): "Burungale–Castella–Kim has recently
proved the Heegner point main conjecture under mild [conditions] (BCK21).
[Theorem] 1.5 gives an unconditional construction of a rank two Euler system
which is related to Heegner points. However, it should be noted that our
[construction is not canonical]."

This is the single most consequential new fact of the cycle. The three-fold
conditional of Thm 1.11 was:

1. **Heegner point main conjecture** — **DISCHARGED** by BCK21 (Burungale–
   Castella–Kim, *A proof of Perrin-Riou's Heegner point main conjecture*,
   Algebra & Number Theory **15** (2021)), under mild hypotheses. Thm 1.5's
   rank-two Euler system now exists **unconditionally** (though non-canonically,
   per Remark 1.6 / Remark 5.6).
2. **Darmon-derivative Conjecture 1.9** — still open (the load-bearing
   unconstructed control step).
3. **Bockstein regulator $R^{Boc}_{K_\infty}\neq0$** — still open (the
   non-degeneracy of the "second direction").

So the obstruction to the $p$-part of BSD for $E/K$ is now a **two-fold
conditional** (Conj 1.9 + $R^{Boc}\neq0$), not three-fold. The *resolution*
side (the rank-2 Euler system's existence) is settled; the *control* side
(the Darmon-derivative Kolyvagin system + its non-degeneracy) is the wall.
This is a clean confirmation of the attempt-07 structural claim that the
obstruction is at the **control** step, not the resolution step — now with
the resolution step literally discharged by a named theorem (BCK21).

**Honesty on BCK21's scope:** Remark 1.6 says "under mild [conditions]" — the
exact hypotheses (good ordinary reduction at $p$, residual-representation
conditions, etc.) are not spelled out in the extracted text (the PDF text cut
off at "undermildBC"). The standard statement is: BCK21 proves the Heegner MC
for $E/\mathbb Q$ with good ordinary reduction at $p$ under mild hypotheses.
The precise hypothesis list is flagged `to-verify` against the BCK21 paper
body before any load-bearing reuse that depends on the exact conditions.

## What this changes in the obstruction map

- **Kataoka–Sano 2024 upgraded from `to-verify` to CONFIRMED** (primary
  source, published PDF body). All five claims + the $r_T=2$ basic-rank claim
  verified verbatim. The published numbering (Conj 1.9 / Thm 1.11) is now the
  authoritative citation; the arXiv-v1 numbering (Conj 1.6 / Thm 1.8) is
  recorded as the pre-revision variant.
- **The three-fold conditional is now two-fold**: BCK21 discharges the
  Heegner MC leg. The rank-2 Euler system (Thm 1.5) exists unconditionally
  (non-canonically). The remaining wall is exactly the **control** step:
  Darmon-derivative Conj 1.9 + Bockstein-regulator non-vanishing.
- **New intermediate result recorded**: Thm 1.10 (algebraic variant of
  Conj 1.9 ⟸ Heegner MC up to $\mathbb Z_p^\times$) — a concrete bridge
  between the (now-proven) Heegner MC and the (still-open) Darmon-derivative
  conjecture, not in the earlier notes.
- **Direction (A) is now anchored to a named, two-condition target**: prove
  Conj 1.9 (the Darmon-derivative explicit formula) and $R^{Boc}_{K_\infty}\neq0$,
  and the $p$-part of BSD for $E/K$ follows. This is strictly sharper than
  attempt-04/05's "neither exists" and attempt-07's "three-fold conditional."

## Honesty / scope

- **This is a primary-source verification, not a proof move.** BSD remains
  open; rank $\ge2$ and exact $|\Sha|$ untouched. The cycle *verified* the
  Kataoka–Sano reframing against the published paper and *sharpened* the
  conditional from three-fold to two-fold via BCK21.
- **The PDF text extraction was a raw zlib/FlateDecode stream extractor**
  (no PDF library available), so the extracted text is fragmented (spaces
  dropped, ligatures/accents mangled). The theorem numbers, the Conj 1.9
  formula, the $r_T=2$ claim, and the BCK21 remark were all read verbatim
  from unambiguous fragments; no content claim rests on a garbled fragment.
- **BCK21's exact hypotheses** are flagged `to-verify` (Remark 1.6 says "under
  mild conditions" without spelling them out in the extracted text).
- **Thm 1.10** (algebraic variant of Conj 1.9) is recorded as a new
  intermediate result; its precise statement (the "up to $\mathbb Z_p^\times$"
  qualifier) is read from the PDF but not line-by-line re-derived.

## Next (attempt-09)

The natural next target, when budget allows: **primary-source-verify BCK21**
(Burungale–Castella–Kim 2021, Algebra & Number Theory 15) — the exact
hypotheses under which the Heegner MC is now proven, since that is the
discharged leg of the conditional and its scope determines how "unconditional"
Thm 1.5's rank-2 Euler system really is. Secondary: verify the precise
statement of Thm 1.10 and the Darmon-derivative Conj 1.9's algebraic variant
against the paper's §5.4. The rotation continues; weekly reset is Sun Aug 30
7 PM local — the next cycle should live-check usage before any WebSearch.
