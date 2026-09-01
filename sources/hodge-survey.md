---
type: source
id: hodge-survey
title: "Hodge Conjecture status — compiled from web-search summaries"
author: "(compiled, not a primary source)"
date: 2026-08-24
provenance: "web searches; URLs below; NOT verbatim primary sources — flagged [summary]"
tags: [hodge-clay-deligne, hodge-statement, hodge-lefschetz-1-1, hodge-hard-lefschetz-reduction, hodge-known-degrees-0-2-2n, hodge-codim-2-open, hodge-integral-fails, hodge-algebraicity-essential, hodge-absolute-hodge, hodge-cattani-deligne-kaplan, hodge-standard-conjectures, hodge-generalized-conjecture, hodge-abelian-cases, hodge-recent-claims-unverified, hodge-tate-analogue]
used-in: [[hodge_conjecture]]
---

# Hodge Conjecture status survey (compiled from web searches)

> Compiled 2026-08-24 from four web searches; **not a verbatim primary
> source**. Each `[summary]` claim should be re-verified against primary
> sources before load-bearing use. URLs:
> https://www.claymath.org/millennium/hodge-conjecture/ (Clay page);
> https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf (Deligne write-up);
> https://publications.ias.edu/sites/default/files/hodge.pdf (IAS mirror);
> https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/voisinhodge.pdf (Voisin survey);
> https://arxiv.org/pdf/alg-geom/9709030 (Gordon survey, abelian varieties);
> https://www.jmilne.org/math/articles/LFF.pdf (Milne, standard conjectures);
> https://doi.org/10.56994/jomp.001.001.002 (Voisin 2025, coniveau).

## [hodge-clay-deligne] Clay Millennium problem (Deligne 2000)
[summary] One of 7 Millennium problems ($1M). Deligne's official write-up
(*Millennium Prize Problems*, Clay 2006, pp.45–53). On a non-singular
projective variety over C, every Hodge class is a Q-linear combination of
classes cl(Z) of algebraic cycles. [used-in: [[hodge_conjecture]] [[def-hodge-class-cycle-map]]]

## [hodge-statement] Hodge class / cycle class map
[summary] Hdg^p(X)=H^{2p}(X,Q)∩H^{p,p}(X); cycle class map cl:CH^p(X)⊗Q→Hdg^p(X);
the conjecture is surjectivity rationally. Defined analytically (Hodge
decomposition); cycles algebraic (Chow's theorem: analytic subspaces =
algebraic on projective). [used-in: [[def-hodge-class-cycle-map]]]

## [hodge-lefschetz-1-1] Lefschetz (1,1) theorem (codim 1, PROVEN)
[summary] Lefschetz 1924: every integral (1,1) class is a Z-linear combination
of divisor classes. Via exponential sequence: Hdg^1=ker(H^2(Z)→H^2(O))⊂Pic;
projective → NS=algebraic divisors (GAGA). The one codimension where the
analytic→algebraic bridge works integrally. [used-in: [[thm-lefschetz-1-1]]]

## [hodge-hard-lefschetz-reduction] Hard Lefschetz reduction
[summary] L^{n-k}: H^k ≅ H^{2n-k} via cup product with hyperplane class L
(algebraic). Reduces HC in degree 2p to degree 2(n-p). Hence only degrees
0,2,2n-2,2n known generally; the genuinely new cases are middle codimensions
2≤p≤n-2 (n≥4). [used-in: [[thm-hard-lefschetz-reduction]]]

## [hodge-known-degrees-0-2-2n] Only general known cases
[summary] H^0, H^2 (Lefschetz (1,1)), H^{2n-2} (hard Lefschetz ← H^2), H^{2n}
— codimensions p∈{0,1,n-1,n}. These are the ONLY cases known for integral
Hodge classes (per Atiyah–Hirzebruch / Kollár). [used-in: [[thm-hard-lefschetz-reduction]] [[thm-integral-hodge-fails]]]

## [hodge-codim-2-open] Frontier: codimension 2 on a 4-fold
[summary] Deligne: "known when the solution set has dimension <4; open in
dimension 4 and higher." Smallest open case: codim-2 Hodge classes on a smooth
projective 4-fold (a (2,2) class in H^4 not hit by divisors/Lefschetz).
[used-in: [[hodge_conjecture]] [[thm-hard-lefschetz-reduction]]]

## [hodge-integral-fails] Integral Hodge conjecture is FALSE
[summary] Atiyah–Hirzebruch, and Kollár (explicit): integral Hodge classes in
codim ≥2 need not be algebraic (torsion in the Atiyah–Hirzebruch spectral
sequence). Only the Q-version conjectured. (Integral version holds for p=1,
consistent with Lefschetz (1,1).) [used-in: [[thm-integral-hodge-fails]]]

## [hodge-algebraicity-essential] Projective hypothesis essential
[summary] Zucker: Kähler (non-projective) complex tori can have Hodge classes
not from analytic cycles. Mumford / Voisin: Hodge classes on general complex
tori not from Chern classes of coherent sheaves. The projective (algebraic)
hypothesis cannot be dropped. [used-in: [[hodge_conjecture]]]

## [hodge-absolute-hodge] Absolute Hodge (Deligne)
[summary] A Hodge class is absolute Hodge if it stays Hodge under every
Aut(C). Deligne: ALL Hodge classes on abelian varieties are absolute Hodge —
strongest general evidence (algebraic classes are tautologically absolute
Hodge). André: motivated cycles extend this, forming a Tannakian category
where HC holds tautologically (assuming the Lefschetz standard conjecture).
[used-in: [[thm-absolute-hodge-motivated]]]

## [hodge-cattani-deligne-kaplan] Hodge locus is algebraic
[summary] Cattani–Deligne–Kaplan: in a smooth projective family, the Hodge
locus of a Hodge class is a countable union of closed algebraic subsets.
Evidence: Hodge classes behave "as if" algebraic at the level of loci (only a
countable union, not necessarily one algebraic set — a quantitative gap).
[used-in: [[thm-cattani-deligne-kaplan]]]

## [hodge-standard-conjectures] Standard conjectures B, C (Grothendieck)
[summary] B (Lefschetz standard): inverse Lefschetz operators Λ algebraic —
known for abelian varieties (Lieberman/Kleiman), surfaces, hyper-Kähler
K3^{[n]} (Charles–Markman 2013). C (Künneth): Künneth components of the
diagonal algebraic — known for i∈{0,1,2n-1,2n} always; all i for surfaces.
B ⇒ numerical = homological ⇒ motives Tannakian; with C, HC reduces to a
fully-faithful functor Mot→Hodge. [used-in: [[thm-standard-conjectures-motives]]]

## [hodge-generalized-conjecture] Generalized Hodge Conjecture (Grothendieck)
[summary] Grothendieck's coniveau version: Hodge substructures of coniveau ≥r
come from cohomology supported on codim-≥r algebraic subsets. Usual HC = GHC
at k=2r. Hodge's original stronger form is FALSE (Grothendieck). Coniveau 1
known (reduces to Lefschetz (1,1)); coniveau ≥2 largely open. [used-in: [[conj-generalized-hodge]]]

## [hodge-abelian-cases] Abelian-variety sub-cases (known)
[summary] HC known for: products of elliptic curves (Tate/Murty); Fermat type
of prime degree or m≤20 (Shioda); simple of prime dimension (Tankeev/Ribet);
fourfolds types I/II (Moonen–Zarhin); some Weil-type fourfolds K=Q(i) or
Q(√−3), det H=1 (Schoen); stably nondegenerate with no type-III factors
(Hazama). Open: general abelian, esp. Weil type, type III (Albert).
[used-in: [[thm-absolute-hodge-motivated]] [[hodge_conjecture]]]

## [hodge-recent-claims-unverified] Recent claimed solutions (NOT peer-accepted)
[summary] 2024–25 preprint flurry: Shimizu 2025 (Preprints.org
10.20944/preprints202509.1435.v1, zero citations, claims HC + standard
conjectures B/C/D/I); Bouali 2024 (arXiv 2401.03465, v1–v13, degeneration +
nearby cycles induction); Abdelgalil 2025 (arXiv 2507.09934, complete
intersections unconditional, general case CONDITIONAL on unproven
"algebraicity of limits"); Mounda 2025 (arXiv 2507.15012, a CONJECTURE not a
proof, LMHS/monodromy); Hajebi & Hajebi 2025 (arXiv 2507.12173, asserts an
unproved "spanning property"). NONE peer-reviewed or community-accepted;
several carry acknowledged gaps. Treated as attempts-to-study, NOT solutions.
[used-in: [[hodge_conjecture]]]

## [hodge-tate-analogue] Tate conjecture (l-adic analogue)
[summary] The l-adic analogue: cycle class map CH^p⊗Q_l → H^{2p}(X,Q_l(1))
surjective (over finite fields / number fields). OPEN even for H^2 (divisors)
in the arithmetic setting — so HC (char 0, supposedly easier) being open is
consistent; the Tate side is harder still. Linked to standard conjectures
(full Tate ⇒ Lefschetz standard). [used-in: [[hodge_conjecture]]]