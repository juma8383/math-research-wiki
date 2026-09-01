---
type: source
id: bsd-survey
title: "BSD status — compiled from web-search summaries"
author: "(compiled, not a primary source)"
date: 2026-08-24
provenance: "web searches; URLs below; NOT verbatim primary sources — flagged [summary]"
tags: [bsd-rank-le-1-proven, bsd-parity-proven, bsd-refined-open, bsd-rank-ge-2-open, bsd-kolyvagin-conj, bsd-skinner-converse, bsd-comp-verified]
used-in: [[birch_swinnerton_dyer]]
---

# BSD status survey (compiled from web searches)

> Compiled 2026-08-24 from two web searches; **not a verbatim primary
> source**. Each `[summary]` claim should be re-verified against the cited
> primary sources before load-bearing use. URLs:
> https://williamstein.org/books/bsd/bsd.pdf (Stein, *BSD: A Computational
> Approach*); https://annals.math.princeton.edu/2010/172-1/p11
> (Dokchitser-Dokchitser);
> https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n2-p01-s.pdf
> (Skinner, converse); https://mathoverflow.net/questions/477214/ (refined BSD
> discussion); https://ar5iv.labs.arxiv.org/html/2511.07203 (Bullach-Honnor,
> Mazur-Tate).

## [bsd-rank-le-1-proven] BSD for analytic rank ≤ 1 — THEOREM
[summary] Gross-Zagier 1986 (Heegner-point height ↔ $L'(E/K,1)$) + Kolyvagin
1988-90 (Euler system bounds Selmer group) + modularity (Wiles/BCDT) +
nonvanishing (Bump-Friedberg-Hoffstein, Murty-Murty, Waldspurger, ensuring a
suitable imaginary quadratic $K$ exists) ⟹ for $r_{\text{an}}\le1$:
$r_{\text{alg}}=r_{\text{an}}$ AND $\text{Sha}(E/\mathbb Q)$ finite, with an
explicit upper bound on $|\text{Sha}|$. (Stein's book, Theorem 1.2.)
[used-in: [[thm-kolyvagin-gross-zagier]] [[method-heegner-point-euler-system]]]

## [bsd-parity-proven] Parity
[summary] Dokchitser-Dokchitser 2010 (Annals): $p$-parity (Selmer-rank parity =
analytic-rank parity) unconditionally for all $E/\mathbb Q$, all $p$. Nekovář:
full algebraic-rank parity assuming $\text{Sha}$ finite.
[used-in: [[thm-parity]]]

## [bsd-refined-open] Refined / leading-coefficient BSD — OPEN in general
[summary] The leading-coefficient formula (exact $|\text{Sha}|$, a perfect
square) is **open in general even at analytic rank 0**. Verified
computationally: Grigorov-Jorza-Patrikis-Stein-Tarniţa 2009 (Math. Comp. 78,
conductor ≤1000, rank ≤1, up to excluded primes); Miller 2011 (LMS J. Comput.
Math., 16,714 of 16,725 curves of conductor <5000, rank ≤1). General
properties ($c(E)/c_1(E)\in\mathbb Z$, is a square, $=|\text{Sha}|$) are NOT
proven for all curves. [used-in: [[birch_swinnerton_dyer]]]

## [bsd-rank-ge-2-open] Rank ≥ 2 — OPEN
[summary] No elliptic curve of analytic rank ≥2 has the **full** BSD formula
proven. No curve of analytic rank ≥4 has even its analytic rank proven (the
conductor-234446 rank-4 candidate is only known to have $r_{\text{an}}\in
\{2,4\}$). [used-in: [[birch_swinnerton_dyer]]]

## [bsd-kolyvagin-conj] Kolyvagin's higher-rank conjectures — OPEN
[summary] Kolyvagin's Conjectures 3.32–3.35 (Stein's book) would extend his
Euler-system method to higher analytic rank; unproven. Named target for
direction (A). [used-in: [[thm-kolyvagin-gross-zagier]]
[[method-heegner-point-euler-system]]]

## [bsd-skinner-converse] The Iwasawa / converse direction
[summary] Skinner 2020 (Annals): a converse to Gross-Zagier-Kolyvagin for
semistable curves (algebraic rank 1 + $\text{Sha}$ finite ⟹ analytic rank 1)
under conditions, via Iwasawa theory over imaginary quadratic fields +
$p$-adic $L$-functions. Bhargava-Skinner: a positive proportion of curves (by
height) have both algebraic and analytic rank 1, combining Bhargava-Shankar
average Selmer-group bounds with Skinner's converse. [used-in:
[[birch_swinnerton_dyer]]]

## [bsd-comp-verified] Computational evidence
[summary] BSD verified on thousands of curves (rank 0–3) in Cremona's database
via SAGE/Magma (descents, Heegner points, Kato/Skinner-Urban Iwasawa,
Stein-Wuthrich): rank matches, leading coefficients match up to computable Sha
bound. Overwhelming but not a proof — analogous to Beal's empirical rigidity.
[used-in: [[birch_swinnerton_dyer]]]