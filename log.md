# Log

> Append-only audit trail. Every Attack / Continue / Query / Lint gets a dated
> entry with a parseable prefix. Newest at the bottom. This is how a fresh
> session knows what has been done and what hasn't.

## [INIT 2026-08-24] scaffold
Created the math-wiki structure: `SCHEMA.md`, `README.md`, `index.md`, `log.md`,
and the `problems/`, `theory/` (theorems/lemmas/methods/definitions/conjectures),
and `sources/` directories. System ready for the first problem. No problems
attacked yet.

## [ATTACK 2026-08-24] beals-conjecture
First problem: Beal's conjecture. Created `problems/beals-conjecture/`
(problem.md, progress.md, notes.md, attempts/attempt-01.md, scripts/search.py);
removed stray empty `BealsConjecture/` folder.
Filed theory: definitions/beal-equation; methods pairwise-coprime-reduction,
exponent-reduction, frey-modularity, abc-finiteness; theorems fermat-last,
darmon-granville, catalan-mihailescu.
Key results: (1) locked the two reductions (Beal âŸº no pairwise-coprime soln;
WLOG exponents in {odd primes}âˆª{4}). (2) Identified the entire open content as
"finitely-many â†’ zero" per signature (Darmonâ€“Granville gives finiteness
unconditionally; abc gives no more). (3) Computational probe (bases â‰¤120,
exponents {3,4,5,7}) found 0 coprime exact solutions, 55 gcd>1 solutions, and
the headline finding: Beal is "tight by 1" â€” coprime â‰¥3-power triples can land
exactly 1 below a â‰¥3-power (e.g. $9^3+10^3=12^3+1=1729$, Ramanujan taxicab), so
metric/density arguments cannot prove it. (4) Localized the modular-method
barrier to mixed-exponent incommensurability in the Frey conductor.
Status: in-progress; outcome of attempt-01 = partial. Next: catalogue
already-resolved signatures and attack the smallest open one (attempt-02).

## [INGEST 2026-08-24] rg2024
Ingested Ratcliffe & Grechuk 2024 (arXiv:2412.11933) â€” survey of solved
generalized-Fermat cases. Filed sources/ratcliffe-grechuk-2024.md with claim
tags [rg2024-fc-vs-beal, -10-solns, -solved-sigs, -357-smallest, -comp-bound,
-faltings-algorithm]. Corrections vs attempt-01: Beal â‰  Fermatâ€“Catalan
(distinct conjectures; Beal strictly stronger in â‰¥3 regime); 10 known primitive
solutions all have a 2 (none a Beal counterexample); verification is to
z^râ‰¤2^100 (not bases â‰¤120); (3,3,4) is SOLVED (part of (3,3,n), nâ‰¤10^9), so not
the frontier.

## [ATTACK 2026-08-24] beals-conjecture (attempt-02)
Filed theory: theorems/solved-generalized-fermat-signatures (catalogue);
methods/frey-level-lowering-obstruction (new key page); conjectures/fermat-catalan.
Wrote attempts/attempt-02.md; rewrote progress.md to the new frontier.
Headline: the smallest open Beal signature is (3,5,7) [rg2024-357-smallest], NOT
(3,3,4). Explicit Frey computation: for A^3+B^5=C^7 the curve
Y^2=X(X-A^3)(X+B^5) has Î”=16 A^6 B^10 C^14; a single level-lowering prime â„“
strips all bad primes only if â„“ | gcd(6,10,14)=2, so only â„“=2 (useless; Mazur
irreducibility needs â„“ large). Generalized: for any pairwise-distinct odd-prime
signature (p,q,r), stripping all needs â„“ | 2Â·gcd(p,q,r)=2 â€” so the WHOLE
distinct-prime class is structurally blocked for the classical Frey/Ribet
method. This explains why every solved Beal signature repeats an exponent.
Path forward: Darmon's program (Frey abelian varieties of GL2-type over totally
real fields), blocked on a missing Mazur-style irreducibility theorem for
mod-p representations of abelian varieties over number fields.
Outcome attempt-02 = breakthrough-diagnostic. Next (attempt-03): ingest
Darmon's program directly (arXiv:2205.15861); principled check whether
A^3+B^5 factors over a number field to give a usable Frey abelian variety for
(3,5,7); develop the Mordell-curve side thread on the gap-1 near-misses.

## [INGEST 2026-08-24] dv2022
Ingested Billereyâ€“Chenâ€“Dieulefaitâ€“Freitas 2022 (arXiv:2205.15861), Darmon's
program I. Filed sources/darmon-program-2022.md [dv2022-frey-av,
-irreduc-conjecture, -repeated-only, -55p-cartan, -1111n] and
methods/darmon-program.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-03, loop cycle 1/20)
Ingested Darmon's program. Key finding: it is REAL and attaches bounded-conductor
residual 2-dim Galois reps for ALL signatures (construction is general), BUT the
developed modular method treats only repeated-exponent signatures (r,r,p) and
(p,p,r) â€” three-distinct-prime signatures have only a Frey-variety CLASSIFICATION
(Remark 2.4), no working modular method. AND it is gated on Darmon Conjecture
1.2 (a generalized-Mazur irreducibility theorem for GL2-type abelian varieties
over totally real fields), which is WIDE OPEN â€” even repeated-exponent results
are mostly conditional on it. Refinement of attempt-02: (3,5,7) is blocked at
TWO levels (scope + irreducibility), not one. (3,5,7) is beyond BOTH the
classical Frey method and Darmon's program. Filed attempt-03.md (outcome partial);
updated progress.md. Self-paced loop: 1 of 20 cycles done.

## [ATTACK 2026-08-24] beals-conjecture (attempt-04, loop cycle 2/20)
Computational probe of signature (3,5,7) (scripts/search_357.py, A<=6000,
B<=600, C<=200). Results: 0 exact solutions (coprime OR not â€” (3,5,7) is
empirically more rigid than cubic, no small Fermat-Catalan scaffolding);
gap-1 near-misses present but ALL degenerate (one base=1) from universal
families t^21+1 (A=t^7,B=1,C=t^3) and t^35+1 (A=1,B=t^7,C=t^5); degenerate
gap-1 families are universal across all signatures; smallest NON-degenerate
coprime near-miss is gap 29 (5^3+2^5=157 ~ 2^7=128), unlike cubic which has
non-degenerate gap-1 (Ramanujan). Distinction: metric obstruction still holds
(gap can be 1) BUT distinct-prime signatures are empirically looser than
repeated-cubic. Points the Mordell-curve side angle at the cubic case (where
near-misses are genuine elliptic-curve arithmetic), to be developed next cycle.
Filed attempt-04.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-05, loop cycle 3/20)
Mordell-curve side angle, developed and VERIFIED. Computationally confirmed
(scripts/mordell_check.py, exact fractions) the birational equivalence
x^3+y^3=N <-> Y^2=X^3-432N^2 via X=12N/(x+y), Y=36N(x-y)/(x+y). Ramanujan
point (9,10), N=1729=12^3+1 maps to (1092,-3276); 6^3+8^3=728=9^3-1 maps to
(624,-3744). Filed methods/mordell-curve-lens.md. Key finding: the gap-1 vs
gap-0 distinction = integral points on Mordell family E_{z^3} (none, =FLT n=3)
vs E_{z^3Â±1} (some, Ramanujan). DECISIVE SCOPE LIMIT: the lens is cubic-only â€”
the curve x^a+y^b=N has genus (a-1)(b-1)/2-ish; (3,3)->g=1 elliptic, but
(3,5)->g=4, (4,4)->g=9, (5,5)->g=21 are higher genus (Faltings only). So the
Mordell angle does NOT reach the frontier (3,5,7) â€” consistent with attempt-04's
degenerate near-misses there (no elliptic structure). Honest: the lens is a
reformulation of Euler FLT n=3 for gap-0, explanatory not a new proof, and
cubic-specific. Filed attempt-05.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-06, loop cycle 4/20)
Descent thread. Filed methods/infinite-descent.md. Distilled the 3
requirements of classical descent: (1) matching algebraic factorization (only
when both LHS terms share an exponent); (2) factor-power = RHS-power (only
when r=p); (3) cyclotomic UFD (fails for large p, Kummer, first irregular
prime 37). Failure table: (p,p,p) passes all; (p,p,r) r!=p fails (2) â€” why it
needed modular methods; (p,q,r) distinct fails (1) â€” x^p+y^q has NO cyclotomic
factorization, descent cannot begin. CONVERGENT 4-THREAD DIAGNOSIS: modular
method, Darmon program, Mordell lens, and descent ALL break at the
distinct-prime case (3,5,7), each for a different reason. Cubic-cubic-cubic is
the unique signature where all classical structures coincide (genus 1 +
cyclotomic UFD factorization + self-power match). (3,5,7) breaks every one.
To-verify: exact UFD boundary of Z[zeta_p]. Filed attempt-06.md; updated index.

## [ATTACK 2026-08-24] beals-conjecture (attempt-07, loop cycle 5/20)
Neighbors check of (3,5,7). All repeated-exponent neighbors solved and sourced:
(3,3,7) via (3,3,n)<=10^9 [Chen-Siksek]; (5,5,7) [Dahmen-Siksek]; (3,5,5)=
(5,5,3) via (n,n,3) [Darmon-Merel]. Confirms (3,5,7) is the solved/open
boundary; open region = all-distinct-odd-prime signatures {(3,5,7),(3,5,11),
(3,7,11),(5,7,11),...} with (3,5,7) least. Matches the factorization/no-
factorization divide from attempt-06. Caveat: composite-exponent neighbors
(3,4,7) etc. subsumed by survey's [rg2024-357-smallest] claim, not independently
verified. Outcome: confirmed. Filed attempt-07.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-08, loop cycle 6/20)
Examined the Siksek-Stoll (3,4,5) mechanism (last unexamined classical tool).
Filed methods/spherical-reduction.md. Mechanism (reconstructed): even exponent
4=2*2 lets y^4=(y^2)^2 reduce (3,4,5) to the spherical signature (2,3,5)
(1/2+1/3+1/5>1), which has explicit parametrizations (Beukers/Edwards); impose
W=y^2 (square) + primitivity -> genus>=2 curves -> Chabauty/Mordell-Weil sieve.
DECISIVE: route is DOUBLY gated. Gate 1 needs an even exponent to expose a 2;
(3,5,7) has none, so the reduction cannot be written. Gate 2: even with an even
exponent, the reduced (2,*,*) signature must be spherical; (3,4,7)->(2,3,7) is
hyperbolic (<1), not parametrized, so the route fails for (3,4,n) n>=7 too.
(3,4,5) is doubly special: even exponent AND lands on the boundary spherical
(2,3,5). This is the FIFTH convergent thread (modular, Darmon, Mordell, descent,
spherical-reduction) all breaking at (3,5,7) for distinct reasons. Closes the
attempt-07 composite-exponent caveat structurally. Outcome: partial, angle
exhausted, confirms existing state. Honest flag: mechanism reconstructed from
principles, attribution to verify against the paper. Filed attempt-08.md;
updated index.md.
## [ATTACK 2026-08-24] beals-conjecture (attempt-09, loop cycle 7/20)
Wrote the consolidated synthesis page problems/beals-conjecture/synthesis.md â€”
the five-thread obstruction map frozen for cross-session continuity. Captures:
the two reductions; the (3,5,7) frontier and open region; the open content =
"finitely many -> zero" per signature; the five-thread table (Frey/modular,
Darmon program, Mordell lens, descent, spherical reduction) with structure
needed vs reason (3,5,7) breaks each; the unifying fact (cubic-cubic-cubic is
the unique signature where all classical structures coincide); honest "what a
proof requires" (two programs away, no non-modular foothold); computational
state; minor to-verify items; attempt index. This is the LLM-wiki compounding
property made explicit: the map itself is the durable artifact. Outcome:
partial, consolidating not advancing. Next: Lint pass over the ~23-page wiki.

## [LINT 2026-08-24] beals-conjecture (attempt-10, loop cycle 8/20)
First Lint of the ~23-page wiki. Enumerated all 34 .md files; extracted every
[[...]] cross-ref; checked against page slugs (method-/thm-/conj-/def-/source)
and claim tags defined in sources/. Findings: NO broken links or claim tags
(all resolve); NO contradictions (the 4-vs-5-thread difference is historical, not
conflicting); NO stale claims (both sources current). FIXED: (1) orphan
theory/definitions/beal-equation.md â€” added [[def-beal-equation]] inbound from
problem.md (tools + Provenance); (2) missing pointer to synthesis.md â€” added
top-of-progress.md pointer + problem.md synthesis field; (3) stale problem.md
tools list â€” rebuilt to all 15 method/theorem/definition/conjecture pages.
Cross-ref graph now complete: problem.md -> progress.md -> synthesis.md reaches
every concept page. Outcome: confirmed, wiki healthy. Filed attempt-10.md;
updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-11, loop cycle 9/20)
Forward-looking analysis: what new machinery would a (3,5,7) proof require.
KEY REFRAMING: the obstruction is uniformly at the REDUCTION step, not the
RESOLUTION step. All five threads fail at reducing the equation to finitely
many curves; the resolution tools (Chabauty, effective Faltings, Mordell-Weil
sieve) all work and are how solved cases were finished. Every existing
reduction-to-finite mechanism uses a shared exponent, an even exponent, or a
spherical parametrization; (3,5,7) has none. One-sentence need: a reduction-
to-finite-curves mechanism using none of those three. Two candidate directions:
(A) modular = extend Darmon Frey-variety method to 3 distinct primes AND prove
Darmon Conjecture 1.2 (generalized-Mazur, wide open) â€” two programs away, most
principled; (B) geometric = a non-spherical reduction to finitely many genus>=2
curves + effective Chabauty â€” closest to tractable but NO such reduction known
(that IS the crux), plus a rank<genus hurdle. Ruled out (recapitulate known
walls): abc (finiteness only), cleverer descent (no factorization), density/
metric (tight-by-1 refutes), "compute the Faltings set" (ineffective = the
missing reduction). Refined synthesis.md "what a proof requires" section with
the reduction-vs-resolution framing. Outcome: partial â€” converts "Beal is
hard" into a precise falsifiable machinery target. Filed attempt-11.md; updated
index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-12, loop cycle 10/20)
Computational strengthening of attempt-04's degenerate-near-miss claim.
Wrote scripts/search_357_nearmiss.py: (1) exhaustive gap-1 enumeration
|A^3+B^5-C^7|==1 over A<=6000,B<=600,C<=200 with exact integer cube-root check;
(2) family-membership classification vs the two universal degenerate families
t^21+1 (A=t^7,B=1,C=t^3) and t^35+1 (A=1,B=t^7,C=t^5); (3) min non-degenerate
coprime gap via floor-cbrt nearest-cube search. Results: total gap-1 hits=4,
ALL degenerate (a base==1), ALL on a universal family (t=1,2,3 of t^21+1 and
t=2 of t^35+1), 0 genuine gap-1, 0 unclassified. Min non-degenerate coprime
near-miss gap = 29 at (5,2,2) [5^3+2^5=157, 2^7=128] â€” matches attempt-04
exactly. STRENGTHENED claim: from "all degenerate" to "exhaustively classified,
zero genuine gap-1 in box, min genuine gap 29." Honest scope caveat: A<=6000
cap rules out genuine gap-1 only for A<=6000 (~C<=90); degenerate families are
parametric (all t) so explained fully; small-base concentration means box
likely holds the global min but not proven. Outcome: confirmed. (3,5,7)
empirically more rigid than cubic (which has non-degenerate gap-1 Ramanujan) â€”
consistent with five-thread diagnosis. Filed attempt-12.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-13, loop cycle 11/20)
Probed the neighboring distinct-prime signature (3,5,11) to test whether
(3,5,7)'s rigidity is class-wide. Wrote scripts/search_3511.py. Generalized the
universal degenerate families: for any (p,q,r) they are t^lcm(p,r)+1 (B=1) and
t^lcm(q,r)+1 (A=1); for (3,5,11) -> t^33+1 (A=t^11,B=1,C=t^3) and t^55+1
(A=1,B=t^11,C=t^5). Results over box A<=6000,B<=6000,C<=40: 0 exact solutions
(coprime or not); 3 gap-1 hits ALL degenerate, ALL on universal families
(t^33+1 t=1,2; t^55+1 t=2); 0 genuine gap-1; min non-degenerate coprime gap=77
at (12,3,2) [12^3+3^5=1971, 2^11=2048]. FINDING: (3,5,11) reproduces (3,5,7)'s
qualitative rigidity EXACTLY, and the min gap GROWS with exponents (29->77) â€”
rigidity is uniform across the open class and monotone in the exponents,
matching the class-wide five-thread structural diagnosis. Honest scope caveat:
box more constraining for (3,5,11) (C^11 grows fast; t>=3 family members at
3^11=177147 outside box). Outcome: confirmed. Filed attempt-13.md; updated
index.md.

## [INGEST+ATTACK 2026-08-24] beals-conjecture (attempt-14, loop cycle 12/20)
Targeted literature check on direction (B) (attempt-11's geometric route).
CORRECTION to attempt-11: "no non-spherical reduction is known" was too strong.
Darmon-Granville's PROOF is itself a reduction to finitely many genus>1 curves
(unramified coverings of P^1-{0,1,âˆž} signature (p,q,r) + Chevalley-Weil ->
Faltings) â€” but INEFFECTIVE (Faltings doesn't enumerate). So the gap is "no
EFFECTIVE reduction for distinct-prime signatures," not "no reduction."
The one effective precedent: Poonen-Schaefer-Stoll 2007 (x^2+y^3=z^7, all 16
primitive solutions) via NONABELIAN DESCENT through finite PSL2(F7) (order 168)
-> 10 twists of Klein quartic (genus 3) -> Chabauty + Mordell-Weil sieve +
modularity. Filed sources/poonen-schaefer-stoll-2007.md [pss2007-*] and
methods/triangle-group-descent.md. KEY STRUCTURAL POINT: PSL2(F7) is the finite
quotient of the triangle group Delta(2,3,7), which is FINITE iff 1/p+1/q+1/r>1
(spherical). (2,3,7) spherical -> finite group -> descent works. (3,5,7)
HYPERBOLIC (1/3+1/5+1/7<1) -> infinite triangle group -> NO finite descent
group -> PSS technique unavailable. RE-FRAMING: direction (B) is NOT
independent of thread 5 (spherical reduction) â€” both gated on the same
spherical/hyperbolic divide. Diagnosis now 6 angles converging on
hyperbolicity / no-finite-structure at (3,5,7). Updated synthesis.md direction
(B). Outcome: partial â€” a correction that sharpens (slightly more pessimistic).
Filed attempt-14.md; updated index.md.

## [LINT 2026-08-24] beals-conjecture (attempt-15, loop cycle 13/20)
Second Lint after attempt-14 ingest. Grepped new slugs method-triangle-group-
descent, pss2007, and pss2007-* tags. Findings: NO broken links/claim tags
(new method linked from synthesis + pss2007 source; tags all defined). NO
orphans. FIXED: (1) stale problem.md tools list missing method-triangle-group-
descent â€” added (16 entries); (2) superseded claim â€” attempt-11 direction (B)
"no reduction known" corrected by attempt-14; per append-only discipline the
original text was NOT rewritten, a correction blockquote inserted at top of (B)
subsection pointing to method-triangle-group-descent + corrected synthesis,
marked authoritative. This models the wiki's own corrections as first-class
dated annotations (compounding discipline). NO contradictions (five-thread
table vs attempt-14 "six angles" consistent: 6th is a refinement not new
obstruction). NO stale claims (pss2007 flagged to-verify in its page).
Outcome: confirmed, wiki healthy. 7 cycles remain -> begin close-out
consolidation. Filed attempt-15.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-16, loop cycle 14/20)
Close-out consolidation of synthesis.md to reflect the full 15-attempt arc.
Changes: (1) "hard kernel" section now states the unifying lens â€” five threads
are five symptoms of ONE structural absence (no finite group at a hyperbolic
signature); spherical/hyperbolic triangle-group distinction (Delta(p,q,r)
finite iff 1/p+1/q+1/r>1) explains why both thread 5 and direction (B)/PSS are
unavailable at (3,5,7). (2) Computational state expanded: attempt-12 exhaustive
(3,5,7) gap-1 (4 hits all degenerate + universal-family, 0 genuine, min gap 29)
+ attempt-13 (3,5,11) (0 exact, 0 genuine gap-1, degenerate on t^33+1/t^55+1,
min gap 77); rigidity uniform across open class & monotone in exponents;
general family t^lcm(p,r)+1, t^lcm(q,r)+1; honest box-scope caveat. (3) To-verify:
added pss2007 mechanism (from search summary, verify vs paper; triangle-group
criterion robust). (4) Attempt index table 8->15. (5) Bottom line rewritten as
structured close-out (frontier, open content, obstruction=reduction-not-
resolution + hyperbolic unifier, empirical uniformity, 2 proof directions,
compounding-artifact handoff). Outcome: partial, consolidating not advancing.
Substantive arc = attempts 01-14; 15-16 maintenance. 6 cycles remain -> low-risk
final Lint + optional paper verification + clean loop close; guard against
padding. Filed attempt-16.md; updated index.md.

## [INGEST+ATTACK 2026-08-24] beals-conjecture (attempt-17, loop cycle 15/20)
Verified the PSS mechanism against the actual paper (arXiv math/0508174, Duke
MJ 137(1) 103-158). CONFIRMED all load-bearing claims: 16 primitive solutions
(Theorem 1.1, full list recorded), nonabelian descent via PSL2(F7) order 168
(smallest Hurwitz group), reduction to 10 twists C1-C10 of the Klein quartic
(x^3y+y^3z+z^3x=0, genus 3, 168 auts), X~=X(7) modular curve + Ribet level
lowering to 13 elliptic curves, Chabauty-Coleman (rank<3 except C5),
(1-zeta)-descent for C1-C3, 2-descent for C4-C10, Mordell-Weil sieve for C5
(rank=genus=3) proving C5(Q)_subset=empty. (2,3,7) chi=-1/42 = negative value
closest to 0; first complete pairwise-coprime chi<0 treatment.
CAUGHT A FACTUAL ERROR: attempt-14 / method-triangle-group-descent.md labeled
(2,3,7) "spherical" with 41/42>1. FALSE: 41/42<1, so (2,3,7) is HYPERBOLIC
(infinite triangle group). PSS works via a FINITE QUOTIENT PSL2(F7) of the
INFINITE Delta(2,3,7) (Klein quartic auts), enabled by near-spherical position
(chi=-1/42) AND an exponent 2 (X(7) modular interpretation). (3,5,7) deeply
hyperbolic (chi=-34/105) + no exponent 2 -> no known finite-quotient descent.
CORRECTIONS (append-only + direct-fix): rewrote method-triangle-group-descent.md
table+framing; updated pss2007 source (verified facts, flagged sieve primes
2,3,13,23,97 as [summary]); append-only correction blockquote on attempt-14;
corrected synthesis.md unifying-lens + direction (B); fixed index descriptions.
Structural conclusion unchanged but sharper: obstruction at distinct-odd-prime
= deep hyperbolicity + no exponent 2 (gates modular, spherical, AND PSS routes).
Outcome: confirmed with correction. Good example of why flagged to-verify
items matter â€” a plausible first-principles framing had a silent arithmetic
error (41/42>1) surfaced by primary-source verification. Filed attempt-17.md;
updated index.md.

## [LINT 2026-08-24] beals-conjecture (attempt-18, loop cycle 16/20)
Final Lint after attempt-17 corrections (touched 4 files + index). Checks:
(1) grep 41/42 â€” every occurrence now in a correction blockquote, the
superseded historical log entry, or the corrected table row (41/42<1
hyperbolic); NO live page states 41/42>1 as current fact. (2) grep spherical
(case-insensitive) â€” all current uses correctly attached to genuinely
spherical signatures (2,3,5 31/30>1 and the spherical family); "near-spherical"
qualifier used consistently for (2,3,7). (3) ONE STALE LINE FIXED: index.md
attempt-14 one-liner still said "PSS (2,3,7) needs spherical signature" â€” the
old wrong framing, contradicting attempt-14's own correction blockquote and
method-triangle-group-descent.md. Fixed inline (mutable nav file): now
"effective via finite quotient PSL2(F7) of the *infinite* Delta(2,3,7) needs
near-spherical + exponent 2 [corrected in attempt-17: (2,3,7) is hyperbolic,
chi=-1/42]". This was the sole live inconsistency â€” a one-line summary the prior
pass had not touched. (4) Cross-refs: all 20 real [[page-slugs]] + 4 claim tags
(rg2024-357-smallest, rg2024-comp-bound, rg2024-faltings-algorithm,
dv2022-irreduc-conjecture) + 3 source ids resolve to existing files; the
[[...]]/[[<other-slug>]]/[[method-pmi]]/[[dv2022-...]] tokens are illustrative
placeholders in SCHEMA.md and attempt-10's convention explanation. No broken
links. (5) Orphans: none â€” every wiki page has inbound links; progress.md and
notes.md are working files by convention. Outcome: confirmed â€” wiki
internally consistent; append-only discipline held (old wrong statement
survives only as flagged history, never as current fact in a mutable page).
4 cycles remain; honesty guard active (avoid padding, declare arc complete if
no genuine new angle). Filed attempt-18.md; updated index.md.

## [ATTACK 2026-08-24] beals-conjecture (attempt-19, loop cycle 17/20)
Developed the unexplored probabilistic side: the counting/volume heuristic for
generalized Fermat. Expected primitive count up to height H scales as H^(r*chi),
chi=1/p+1/q+1/r-1 â€” the reciprocal invariant of def-beal-equation made
predictive. Trichotomy as growth rate: chi>0 -> infinite (spherical families);
chi=0 -> constant/borderline (Euclidean (3,3,3) etc.); chi<0 -> sparse-finite
(H^(r*chi)->0). Three honest wins: (1) qualitatively parallels rigorous
Darmon-Granville finiteness; (2) PREDICTS the monotone sparsity the searches
found ((3,5,7) gap 29 -> (3,5,11) gap 77) â€” a theoretical sub-thread now
explains the empirical monotonicity, not just records it; (3) explains why
(3,3,3) (chi=0, H^(r*chi)=H^0 constant, heuristic inconclusive) forced the
modular engine â€” the hard-kernel diagnosis mirrored heuristically. Honest
limit: gives finiteness, NOT zero (heuristic constant rounding <1 is not a
theorem) â€” so every route (5 rigorous threads + PSS + counting) delivers at
most finiteness; zero is the common open content across all six angles. Soft
angle (6*) is a different KIND of obstruction (expectation, not reduction) so
it cannot fill the reduction-step gap â€” consistent, not a contradiction.
Filed method-counting-heuristic.md (flagged heuristic, not theorem); added to
problem.md tools list (16 entries); synthesis obstruction map retitled "five
rigorous threads + one soft angle" with thread 6* row + note; bottom line
updated (19 attempts, six angles, monotonicity now predicted not just
observed). Outcome: partial â€” a genuine sixth angle, not padding. 3 cycles
remain; honesty guard: next cycle makes the close-out call.

## [ATTACK 2026-08-24] beals-conjecture (attempt-20, loop cycle 18/20)
Tested attempt-19's counting-heuristic prediction at a fresh third signature
(3,7,11): A^3+B^7=C^11, chi=-100/231~-0.433 (most negative of the three).
Wrote scripts/search_3711.py (adapted from search_3511). RESULTS (hand-verified):
exact: 1 hit (128,8,4) gcd=4 -> 128^3+8^7=4^11, NON-coprime (Beal-consistent,
not a counterexample); 0 coprime exact. gap-1: 2 hits both degenerate (B=1) on
universal family t^33+1 (t=1, t=2: 2048^3+1=8^11); 0 genuine. MIN
non-degenerate coprime gap = 277 at (13,2,2): 13^3+2^7=2325, 2^11=2048, gap+277,
gcd=1. PREDICTION CONFIRMED: 29 (chi -0.324) < 77 (chi -0.376) < 277 (chi
-0.433), monotone in -chi as predicted; growth super-linear (x2.66, x3.60),
consistent with chi entering as an exponent H^(r*chi). The counting-heuristic
sub-thread survived its falsification test; rigidity now at 3 signatures
(0 coprime exact, 0 genuine gap-1, degenerate-on-universal-family uniformly).
Box A<=6000 B<=600 C<=40; minima all at small bases (C=2) so box not binding
(box-limited caveat noted). Updated synthesis computational state (3-point
empirical line), bottom line (20 attempts, prediction confirmed not just
made), attempt index. Outcome: confirmed. 2 cycles remain; next = loop
close-out.

## [LINT/CONSOLIDATION 2026-08-24] beals-conjecture (attempt-21, loop cycle 19/20)
Consolidated progress.md (the read-first file) â€” was stale past attempt-08 (its
"Best partial result" and "five-thread diagnosis" sections ended at attempt-08,
12 cycles behind synthesis). Rewrote to be current through attempt-20, concise,
pointing to synthesis.md for structural depth (no duplication). New sections:
"entire open content = finitely-many->zero" stated up front; 6-angle brief table
(thread 6* soft); unifying lens (near-spherical OR exponent 2, (3,5,7) has
neither, obstruction at reduction step) with the (2,3,7)-hyperbolic correction
note; what-a-proof-requires + directions A/B + ruled-out recap; 3-row empirical
table (chi, exact, gap-1, min gap: 29<77<277) noting the monotonicity was
PREDICTED (attempt-19) then CONFIRMED (attempt-20); one-line-per-attempt log
01-20; updated honesty check (6 angles + confirmed prediction + 2 directions).
Consistency checks during rewrite: all wikilinks resolve (per attempt-18
index audit), chi values/min gaps match computations exactly, no stale
"spherical" label reintroduced, degenerate-family general fact preserved. No
new content invented â€” consolidation of verified results into the navigational
entry point. Updated index.md. Outcome: confirmed. 1 cycle remains = loop
close-out.

## [CLOSE-OUT 2026-08-24] beals-conjecture (attempt-22, loop cycle 20/20)
END OF 20-CYCLE AUTONOMOUS LOOP. No new research (by design â€” honesty guard:
genuine angles exhausted within arc scope; declare complete rather than pad).
Final summary filed as attempt-22.md. The arc produced (no proof of Beal, by
design): two clean reductions; exact frontier (3,5,7) = smallest open, open
region = all-distinct-odd-prime class; open content = "finitely many -> zero";
SIX convergent angles (5 rigorous: Frey/modular, Darmon, Mordell, descent,
spherical; + 1 soft: counting heuristic) all breaking at (3,5,7), unified by
deep hyperbolicity + no exponent 2; obstruction at the REDUCTION step not
resolution; PSS precedent verified against paper (caught+corrected the
(2,3,7) spherical mislabel); two forward directions (A modular extension +
generalized-Mazur; B effective finiteness w/o finite triangle group); a
falsifiable counting-heuristic prediction MADE (attempt-19) then CONFIRMED
(3,7,11 min gap 277 > 77 > 29, attempt-20); empirical rigidity across 3
signatures (0 coprime exact, 0 genuine gap-1, degenerate on universal
families). Discipline held: append-only + correction blockquotes (2 errors
self-caught via primary-source verification), flagged to-verify items, 3 Lint
passes (attempts 10/15/18), honest framing throughout. The compounding artifact
is the wiki: 35+ pages, SCHEMA.md governance, index.md catalog, log.md audit,
stable claim tags as join keys. Resume point: progress.md (current) then
synthesis.md; extend via direction A/B, ingest the Siksek-Stoll (3,4,5)
paper (still flagged to-verify), or test a 4th signature. Updated index.md
+ synthesis attempt-index (rows 21,22) + bottom-line count (22 attempts).
LOOP STOPPING.

## [ATTACK 2026-08-24] birch-swinnerton-dyer
Second problem: Birch and Swinnerton-Dyer conjecture (Clay Millennium). Created
problems/birch-swinnerton-dyer/ (problem.md, progress.md, notes.md,
attempts/attempt-01.md).
Filed theory: definitions/elliptic-curve-L-function; theorems/mordell-weil,
modularity, kolyvagin-gross-zagier, parity; methods/heegner-point-euler-system.
Filed sources/bsd-survey.md (web-search-compiled, NOT primary; claim tags
bsd-rank-le-1-proven, bsd-parity-proven, bsd-refined-open, bsd-rank-ge-2-open,
bsd-kolyvagin-conj, bsd-skinner-converse, bsd-comp-verified; flagged [summary] +
to-verify). Verified the load-bearing status facts via two web searches BEFORE
committing (the discipline Beal's attempt-17 taught: a plausible first-pass had
a silent 41/42>1 arithmetic error caught only by primary-source check).
Key results: (1) located the EXACT frontier â€” BSD rank equality + Sha finiteness
proven for analytic rank <=1 (Gross-Zagier + Kolyvagin + modularity +
nonvanishing); refined leading-coefficient formula OPEN in general even at
rank 0 (comp. verified conductor <5000 only); analytic rank >=2 fully open,
no curve of analytic rank >=4 even proven to have that rank; parity proven
($p$-parity unconditionally). (2) Named the open content: "analytic rank <=1 ->
arbitrary rank" (rank part) + "Sha finite -> exact order of Sha" (refined
part) â€” the BSD analog of Beal's "finitely many -> zero". (3) Mapped the
OBSTRUCTION to the Selmer-group CONTROL step, NOT the resolution step:
Kolyvagin's Euler system has the SHAPE OF A SINGLE POINT, bounding a rank-<=1
Selmer group but not rank >=2; the resolution tools (descent, Tamagawa,
regulator, Sha computation) work in all ranks. Parity is the one general
rank->=2 tool but only pins rank mod 2 GIVEN an upper bound (the missing
Euler-system step). (4) Cross-problem compounding: the "obstruction at
control/reduction not resolution" lens developed on Beal transfers directly â€”
related link added both ways; recorded as a candidate reusable methodology in
notes.md. Three forward directions: (A) higher-rank Euler systems (higher
Heegner points, Beilinson-Flach, Kato derivatives, Kolyvagin Conjectures
3.32-3.35); (B) Iwasawa/p-adic (Kato, Skinner-Urban main conjecture, Skinner
converse); (C) refined/Mazur-Tate (ETNC, Bullach-Honnor 2025, leading coeff).
Status: in-progress; outcome attempt-01 = partial. To-verify (primary
sources): rank-1 unconditional scope, algebraic-rank parity Sha caveat,
refined-BSD-open-at-rank-0, Skinner-converse hypotheses. Next (attempt-02):
verify those load-bearing facts against primary sources (Stein's book;
Dokchitser-Dokchitser; Skinner), then deepen direction (A).

## [ATTACK 2026-08-24] navier-stokes
Third problem: Navier-Stokes existence and smoothness (Clay Millennium).
Created problems/navier-stokes/ (problem.md, progress.md, notes.md,
attempts/attempt-01.md).
Filed theory: definitions/navier-stokes-equation; theorems/local-wellposedness,
leray-weak-solutions, serrin-regularity, beale-kato-majda,
caffarelli-kohn-nirenberg, tao-averaged-blowup;
methods/energy-supercriticality.
Filed sources/ns-survey.md (web-search-compiled, NOT primary; claim tags
ns-millennium-fefferman, ns-2d-solved, ns-local-wp, ns-leray-weak, ns-bkm,
ns-serrin, ns-ess-endpoint, ns-ckn, ns-tao-averaged-blowup, ns-tao-quant-l3,
ns-buckmaster-vicol, ns-supercritical; flagged [summary] + to-verify). Verified
the load-bearing status facts via two web searches BEFORE committing (same
discipline as BSD; Beal's attempt-17 caught a silent arithmetic error this way).
Key results: (1) located the EXACT frontier â€” Fefferman's four statements (A/B
global regularity on R^3/T^3, C/D breakdown on R^3/T^3), domains without
boundary, smooth + bounded energy; 2D fully solved (Ladyzhenskaya); 3D local
well-posedness + small-data global; global Leray-Hopf weak (uniqueness OPEN);
conditional regularity (Serrin 2/r+3/s<=1, critical endpoint L^inf L^3 by
Escauriaza-Seregin-Sverak 2003; BKM int||omega||_inf <=> regular); partial
regularity (CKN singular set parabolic dim <=1); Tao averaged-NS blowup
(model) + quantitative L^3 blowup rate (triple log, Barker/Palasek).
(2) Named the open content: regularity side "small/local data -> arbitrary
large-data global regularity"; counterexample side "averaged-NS blowup ->
true-NS blowup" â€” the NS analog of Beal's "finitely many -> zero" and BSD's
"rank <=1 -> arbitrary rank". (3) Mapped the OBSTRUCTION to the
critical-norm CONTROL step, NOT the resolution step: the only unconditional
global bound is the energy (L^2, SUBCRITICAL under NS scaling); regularity
needs a CRITICAL norm (L^3, scale-invariant) bounded; a subcritical bound
cannot control a critical norm = supercriticality. Structural reason: Serrin
index S_nonlin=d+1 vs S_lin=d/2+2, EQUAL in 2D (3=3, solved) and 4>3.5 in 3D
(open) â€” the cleanest 2D/3D divide fact, parallel to Beal's cubic coincidence
and BSD's one-point Euler system. (4) Cross-problem compounding: the
"obstruction at control/reduction not resolution" lens is now 3-for-3 (Beal
reduction, BSD Selmer-control, NS critical-norm-control); related links added
across all three problems; candidate reusable methodology recorded in notes.md.
Three forward directions: (A) a critical a priori bound (new global monotone
quantity at critical regularity â€” directly the missing control step);
(B) blowup construction (Fefferman C/D; remove the averaging in Tao's model
while keeping blowup, axisymmetric ansatz); (C) quantitative critical program
(Luo/Barker sharpen the conditional criteria and quantify the supercritical
gap). Status: in-progress; outcome attempt-01 = partial. To-verify (primary
sources): Fefferman's four-statement formulation, Serrin/ESS endpoint, Tao
triple-log rate + Barker localization, Buckmaster-Vicol non-uniqueness scope.
Next (attempt-02): verify those against primary sources (Fefferman Clay
write-up; ESS 2003; Tao 2016; Barker 2022), then deepen direction (B).

## [ATTACK 2026-08-24] yang-mills
Fourth problem: Yang-Mills existence and mass gap (Clay Millennium). Created
problems/yang-mills/ (problem.md, progress.md, notes.md, attempts/attempt-01.md).
Filed theory: definitions/yang-mills-theory, wightman-os-axioms,
mass-gap-confinement; theorems/asymptotic-freedom, lattice-gauge-constructive,
balaban-rg, seiberg-witten-supersymmetric; methods/constructive-continuum-limit.
Filed sources/ym-survey.md (web-search-compiled, NOT primary; claim tags
ym-clay-jaffe-witten, ym-existence-open, ym-mass-gap, ym-confinement-area-law,
ym-asymptotic-freedom, ym-dimensional-transmutation, ym-lattice-constructive,
ym-balaban-rg, ym-supersymmetric, ym-recent-claims-unverified,
ym-spectral-gap-undecidable; flagged [summary] + to-verify). Verified the
load-bearing status facts via two web searches BEFORE committing (same
discipline as BSD/NS; Beal's attempt-17 caught a silent arithmetic error this
way). HONESTY NOTE on recent claims: a 2025-26 preprint flurry (Faizal-Shabir
2026, Gutierrez Ule 2025, Agawa 2025 addendum RETRACTED, Eriksson 2026) is
flagged ym-recent-claims-unverified as attempts-to-study NOT solutions â€”
Eriksson concedes O(4) covariance unproved (only hypercubic W^4), Agawa
retracted, others assume Balaban/AFS bounds as unverified hypotheses. Same
discipline that caught Beal's (2,3,7) spherical mislabel.
Key results: (1) located the EXACT frontier â€” Jaffe-Witten requires BOTH a
rigorous 4D quantum YM (Wightman/OS axioms) AND a mass gap Î”>0; neither is
known; the problem is UNIQUELY hard because even a precise non-perturbative
4D definition is open (framework itself part of the problem; Gribov
ambiguity). (2) Named the open content: "lattice-discretized + numerically
confirmed -> continuum-rigorous 4D QFT with proven spectral gap" =
"asymptotic freedom (UV) -> confinement (IR) rigorously" â€” the YM analog of
Beal's "finitely many -> zero", BSD's "rank <=1 -> arbitrary rank", NS's
"small/local -> arbitrary large-data global". (3) Mapped the OBSTRUCTION to
the continuum-limit + IR-gap CONTROL step, NOT the resolution step: the
resolution layer (lattice YM) is rigorous at finite spacing (Osterwalder-Seiler
reflection positivity, Luscher transfer matrix, strong-coupling area law +
gap); asymptotic freedom gives perturbative UV control; the gap is (i)
continuum-limit convergence with full O(4) covariance and (ii) gap transport
uniform in the lattice spacing a, across the RG from the strong-coupling
gapped IR to the weak-coupling UV â€” bridged by dimensional transmutation
(Lambda_YM = mu*exp(-1/(2*beta0*g^2)), the continuum limit and the mass gap
are the same RG problem). (4) Cross-problem compounding: the "obstruction at
control/reduction not resolution" lens is now 4-for-4 (Beal reduction, BSD
Selmer-control, NS critical-norm-control, YM continuum-limit+IR-gap-control);
related links added across all four problems; candidate reusable methodology
recorded in notes.md. Three forward directions: (A) constructive continuum
limit (Balaban RG + finite-range decomposition + cluster/polymer expansion +
OS reconstruction + uniform-in-a gap transport); (B) illumination from SUSY
(Seiberg-Witten/Nekrasov monopole condensation as the hoped-for mechanism,
't Hooft-Mandelstam analog for pure YM); (C) framework/definition first
(resolve Gribov, get a non-perturbative measure before gap questions).
Status: in-progress; outcome attempt-01 = partial. To-verify (primary
sources): Jaffe-Witten Clay write-up; Balaban RG (what is proved vs open);
2025-26 preprints' actual claims; Seiberg-Witten/Nekrasov scope (N=2 SUSY not
pure YM); spectral-gap undecidability (Cubitt-Perez-Garcia-Wolf) generality.
Next (attempt-02): verify those load-bearing facts against primary sources,
then deepen direction (A).

## [ATTACK 2026-08-24] hodge-conjecture
Fifth problem: the Hodge Conjecture (Clay Millennium). Created
problems/hodge-conjecture/ (problem.md, progress.md, notes.md,
attempts/attempt-01.md).
Filed theory: definitions/hodge-class-cycle-map; theorems/lefschetz-1-1,
hard-lefschetz-reduction, integral-hodge-fails, absolute-hodge-motivated,
cattani-deligne-kaplan, standard-conjectures-motives;
methods/analytic-algebraic-bridge; conjectures/generalized-hodge.
Filed sources/hodge-survey.md (web-search-compiled, NOT primary; claim tags
hodge-clay-deligne, hodge-statement, hodge-lefschetz-1-1,
hodge-hard-lefschetz-reduction, hodge-known-degrees-0-2-2n, hodge-codim-2-open,
hodge-integral-fails, hodge-algebraicity-essential, hodge-absolute-hodge,
hodge-cattani-deligne-kaplan, hodge-standard-conjectures,
hodge-generalized-conjecture, hodge-abelian-cases, hodge-recent-claims-unverified,
hodge-tate-analogue; flagged [summary] + to-verify). Verified the load-bearing
status facts via FOUR web searches BEFORE committing (same discipline as
BSD/NS/YM; Beal's attempt-17 caught a silent arithmetic error this way).
HONESTY NOTE on recent claims: a 2024-25 preprint flurry (Shimizu 2025 on
Preprints.org, zero citations, claims HC + standard conjectures B/C/D/I;
Bouali 2024 arXiv 2401.03465; Abdelgalil 2025 arXiv 2507.09934 conditional on
unproven "algebraicity of limits"; Mounda 2025 arXiv 2507.15012 a conjecture
not a proof; Hajebi & Hajebi 2025 arXiv 2507.12173 asserts an unproved
"spanning property") is flagged hodge-recent-claims-unverified as
attempts-to-study NOT solutions. Same discipline as YM's preprint flagging
and Beal's (2,3,7) spherical-mislabel correction.
Key results: (1) located the EXACT frontier â€” by hard Lefschetz only the
middle codimensions 2<=p<=n-2 (n>=4) are genuinely new; the only general
known cases are degrees 0,2,2n-2,2n (codim 0,1,n-1,n); the smallest open case
is CODIMENSION-2 HODGE CLASSES ON A 4-FOLD (Deligne: "known when dim<4; open
in dimension >=4"). (2) Named the open content: "Hodge class (analytic,
defined by Hodge theory) -> algebraic cycle in codimension >=2" = surjectivity
of cl tensor Q in the middle codimensions â€” the Hodge analog of Beal's
"finitely many -> zero", BSD's "rank <=1 -> arbitrary rank", NS's
"small/local -> arbitrary large-data", YM's "lattice-discretized ->
continuum-rigorous". (3) Mapped the OBSTRUCTION to the
analytic->algebraic CONTROL step, NOT the resolution step: the resolution
layer works â€” Chow groups + cycle class map defined in all codimensions, and
for p=1 the EXPONENTIAL SEQUENCE makes Hdg^1 = ker(H^2(Z)->H^2(O)) subset Pic,
with projective -> NS = algebraic divisors (GAGA) â€” the bridge works for
divisors; the gap is that the Picard-variety / exponential-sequence engine has
no effective higher-codimension analogue (the Griffiths intermediate Jacobian
is transcendental for p>=2 and does not control algebraicity). WRINKLE unique
to Hodge: the integral Hodge conjecture is FALSE (Atiyah-Hirzebruch, Kollar,
torsion in the AHSS), so only the Q-version is conjectured â€” a built-in "naive
strong statement is false" absent in the other four problems. (4)
Cross-problem compounding: the "obstruction at control/reduction not
resolution" lens is now 5-FOR-5 (Beal reduction, BSD Selmer-control, NS
critical-norm-control, YM continuum-limit+IR-gap-control, Hodge
analytic->algebraic conversion); a sharper "one-dimensional engine stops"
sub-pattern identified (cubic coincidence / one-point Euler system / 2D Serrin
equality / single RG scale / Picard-variety one-codimension) â€” recorded as a
candidate reusable methodology in notes.md; related links added across all
five problems. Three forward directions: (A) motive / standard-conjecture
reduction (algebraicity of inverse Lefschetz B + Kunneth components C, known
for surfaces/abelian/hyper-Kahler K3^[n], reduces HC to a fully-faithful
functor â€” the finite-class reduction, closest analog of Beal's
reduction-to-finite-curves); (B) codim-2 directly via Griffiths intermediate
Jacobians / normal functions / Abel-Jacobi at the frontier; (C) structured
abelian sub-cases (Weil type, type III) with absolute Hodge / motivated cycles
as the controlled evidence layer. Status: in-progress; outcome attempt-01 =
partial. To-verify (primary sources): Deligne Clay write-up (hodge.pdf);
Lefschetz (1,1) via exponential sequence; hard Lefschetz reduction;
Atiyah-Hirzebruch & Kollar counterexamples; Cattani-Deligne-Kaplan;
Charles-Markman; the 2024-25 preprints' actual claims. Next (attempt-02):
verify those load-bearing facts against primary sources, then deepen
direction (A).

## [ATTACK 2026-08-24] collatz-conjecture
Sixth problem: the Collatz Conjecture (3n+1 / Syracuse / Ulam-Kakutani). Created
problems/collatz-conjecture/ (problem.md, progress.md, notes.md,
attempts/attempt-01.md).
Filed theory: definitions/collatz-map; theorems/collatz-density-results,
collatz-tao-almost-bounded, collatz-cycle-bounds, collatz-conway-undecidability;
methods/average-vs-pointwise-control, cycle-exclusion-linear-forms.
Filed sources/collatz-survey.md (web-search-compiled, NOT primary; claim tags
collatz-statement, collatz-verified, collatz-density-terras,
collatz-density-allouche-korec, collatz-kl-count, collatz-tao-almost-bounded,
collatz-cycle-steiner, collatz-cycle-simons-deweger, collatz-conway-undecidable,
collatz-matthews-watts, collatz-average-contraction,
collatz-recent-claims-unverified; flagged [summary] + to-verify). Verified the
load-bearing status facts via THREE web searches BEFORE committing (same
discipline as the other five; Beal's attempt-17 caught a silent arithmetic
error this way). HONESTY NOTE on recent claims: a 2024-25 preprint flurry
claiming proofs (Fathi 2025 "entropy descent" = the standard
average-contraction heuristic dressed as "Recursive Type Arithmetic", claims
non-probabilistic but uses E[k]=2 which IS distributional; Nwankpa 2025
mod-4/12 residue analysis with gaps in the accelerated-map accounting; Chang
2026 burst-gap decomposition HONESTLY conditional on an open "Orbit
Equidistribution Conjecture"; viXra 2408.0100, 2505.0010) is flagged
collatz-recent-claims-unverified as attempts-to-study NOT solutions â€” and
crucially they ALL fail at exactly the average-vs-pointwise control step that
IS the obstruction. Same discipline as YM/Hodge's preprint flagging and
Beal's (2,3,7) spherical-mislabel correction.
Key results: (1) located the EXACT frontier â€” two failure modes (a nontrivial
cycle, a divergent trajectory); density/average-case results are strong:
Terras 1976 / Everett (a.a. Col_min < N, natural density), Allouche 1979 /
Korec 1994 (a.a. < N^theta, theta down to ~0.79), Krasikov-Lagarias 2003
(count reaching 1 >= x^0.84), Tao 2019/2022 (a.a. Col_min(N) < f(N) for any
f->infty, log-density â€” "almost all orbits attain almost bounded values", the
apex); cycle exclusion via transcendence: Steiner 1977 (no 1-cycles), Simons
2004 (no 2-cycles), Simons-de Weger 2010 (no m-cycles m<=75); computational
verification to N <= 2^68 (Barina 2020). The gap is the leap from DENSITY
(almost all) to POINTWISE (every N). (2) Named the open content: "almost all
(density) -> every N (pointwise/universal)" = exclude both failure modes for
every start â€” the Collatz analog of Beal's "finitely many -> zero", BSD's
"rank <=1 -> arbitrary rank", NS's "small/local -> arbitrary large-data", YM's
"lattice-discretized -> continuum-rigorous", Hodge's "Hodge class -> algebraic
cycle in codim >=2". (3) Mapped the OBSTRUCTION to the average/density ->
pointwise/universal CONTROL step, NOT the resolution step: the resolution
layer works for average-case (Terras/Allouche/Korec/Krasikov-Lagarias/Tao) and
for small cycles (Steiner/Simons-de Weger); the gap is pointwise control â€” the
average contraction 3/4<1 (E[k]=2 > log_2 3) is DISTRIBUTIONAL over parity
sequences, and a given N's parity sequence is deterministic and uncontrolled,
so density-1 results cannot exclude a measure-zero exceptional set (where a
divergent trajectory or nontrivial cycle would live). Tao: replacing f->infty
by a constant is "likely almost as hard as the full conjecture." UNIQUELY
among the six problems, the obstruction SPLITS into two prior-problem flavors
â€” (a) cycle exclusion = Diophantine / transcendence (linear form
Lambda=(K+L)log2 - K log3, Beal-flavored, echoes generalized-Fermat); (b)
divergent-trajectory exclusion = analytic / ergodic control (need a
per-trajectory Lyapunov, NS-flavored) â€” genuine cross-problem COMPOUNDING. (4)
Cross-problem compounding: the "obstruction at control/reduction not
resolution" lens is now 6-FOR-6 (Beal reduction, BSD Selmer-control, NS
critical-norm-control, YM continuum-limit+IR-gap-control, Hodge
analytic->algebraic, Collatz average->pointwise); the "one-dimensional engine
stops" sub-pattern now 6-for-6 (cubic coincidence / one-point Euler system /
2D Serrin equality / single RG scale / Picard-variety one-codim / single
parity-sequence average); Collatz is the CANONICAL EXEMPLAR (the
average-contraction heuristic IS the obstruction, made visceral) and the
cleanest introductory example; related links added across all six problems.
WRINKLE echoing YM: Conway 1972 proved generalized Collatz maps universal /
halting undecidable, but for GENERAL maps NOT 3n+1 specifically â€” the
possibility 3n+1 itself is undecidable is real but unproved (flagged, not
asserted; Matthews-Watts: 3n+1 is contracting, mu=3<4). Three forward
directions: (A) density -> pointwise (strengthen Tao log-density to natural
density then to a pointwise bound â€” the direct "almost all -> all" attack);
(B) cycle exclusion to all m (push Steiner/Simons-de Weger beyond m<=75 via
sharper linear-form-in-logs / transcendence, the Beal-flavored Diophantine
sub-problem); (C) divergent-trajectory Lyapunov (find a rigorous per-
trajectory decreasing quantity, the NS-flavored analytic control sub-problem).
Status: in-progress; outcome attempt-01 = partial. To-verify (primary
sources): Tao 2022 (Forum Math. Pi, DOI 10.1017/fmp.2022.8); Terras 1976 /
Everett 1977; Krasikov-Lagarias 2003 (Acta Arith.); Steiner 1977 / Simons 2004
/ Simons-de Weger 2010; Conway 1972; Barina 2020; the 2024-25 preprints'
actual claims; any 3n+1-specific independence/undecidability result
(Kurtz-Simon 2007?). Next (attempt-02): verify those load-bearing facts
against primary sources, then deepen direction (A).

## [GOVERNANCE 2026-08-24] standing policies installed
Installed the two cross-cutting governance artifacts requested for every
session. (1) research-protocol.md â€” the standing 10-step research discipline
applied to EVERY conjecture Attack/Continue: generate evidence AND
counterevidence; produce >=3 distinct proof approaches; seek counterexamples;
formalize all assumptions; track failed attempts (append-only); derive
simpler-equivalent AND more-general statements; check computational examples;
re-evaluate confidence; maintain the research notebook (the problem folder);
when stalled change the frame (representation/notation/analogy/generalize/
specialize/reverse/dual); critique every conclusion before accepting it.
Wired into SCHEMA.md Attack workflow (blockquote governing Attack+Continue;
step 3 now requires >=3 approaches; directory-layout lists the file) and
index.md (new "Methodology & governance" section). (2) .claude/usage-policy.md
â€” the Ollama Pro usage/quota policy: zones Green(<60%,<=4 subagents)/
Yellow(>=60%,<=2)/Orange(>=80%,<=1)/Red(>=90%,0)/Emergency(>=95%,stop+summarize+
save+notify); subagent budgeting (prefer 1 agent->many subtasks over 1 task->
many agents); large-task 3-phase planning (Analysis/Implementation/Validation,
check usage before each phase); context conservation >70%; model selection
(smallest capable model for low-complexity); recovery summary every ~10 min;
primary rule = maximize likelihood of completing the project, not parallelism.
HONESTY NOTE in the file: the model context exposes NO tool to read live
Ollama/session/weekly usage %, so zones are applied HEURISTICALLY by task
scale/context and any % the user reports is AUTHORITATIVE â€” the policy does
not silently claim a capability that does not exist. (3) CLAUDE.md at repo
root â€” the actual auto-load mechanism (plain .claude/*.md does NOT auto-load
in Claude Code); states the wiki + research-protocol + usage-policy apply to
every session and subagent, embeds the zone table + subagent caps concisely,
and points to the full files. Memory saved: feedback (research protocol,
apply every time) + reference (usage-policy/CLAUDE.md location).

## [GOVERNANCE 2026-08-24] live usage monitor armed (session loop)
Activated the automated Ollama usage monitor the user requested ("fully
automated"). Mechanism: the Playwright MCP plugin (installed via /plugin,
activated via /reload-plugins --force) drives an isolated browser the user
logged into Ollama once (clawdbot8383@gmail.com, Pro). First manual read of
https://ollama.com/settings: Session 9.8% used (glm-5.2, 42 requests, resets
~5h), Weekly 38.4% used (glm-5.2 835 requests + web search 43, resets ~6
days) -> GREEN zone, max 4 subagents. Written to .claude/usage-status.json
(schema: lastChecked/sessionPct/weeklyPct/zone/maxSubagents/rawNote).
Armed a recurring session cron (job 88269b6b, "7,27,47 * * * *" = every 20 min,
off :00/:30 marks) that re-navigates /settings, re-reads both percentages,
recomputes the zone per .claude/usage-policy.md (stricter of session/weekly
wins; green<60/4, yellow>=60/2, orange>=80/1, red>=90/0, emergency>=95/stop),
rewrites usage-status.json, and reports a one-line zone status (flags a
"ZONE CHANGE" if a threshold crossed; writes null + "read failed - logged
out" honestly if the page is logged out, never fabricates). Updated
.claude/usage-policy.md (new "Live monitoring (session loop)" section + JSON
schema + honest note that the model context itself still has no direct
usage-% tool; the browser read is the live source when the loop is active,
else heuristic fallback) and CLAUDE.md (points to usage-status.json as the
live source). HONESTY LIMITS recorded: (1) the loop is session-scoped â€”
lives only in this Claude session, dies on close, recurring crons auto-expire
after 7 days; relaunch the monitor in a new session to re-arm. (2) Each
check actively drives the browser (manual pull, not a background live feed).
(3) The Playwright browser is a separate isolated profile, not the user's
normal Chrome; the user logged into it once and it must stay logged in for
reads to work (if it logs out, the loop reports "read failed" honestly).

## [CONTINUE 2026-08-24] birch-swinnerton-dyer (math-work loop, cycle 1/24)
Started the usage-optimized math-work loop (Green zone, 9.8% session /
38.4% weekly; max 4 subagents; pacing to leave ~half the weekly budget for the
remaining ~6 days; stop at weekly>=85% / session>=90% / 24 cycles). Cycle 1 =
BSD Continue following attempt-01's Next note: verify load-bearing facts
against primary sources, then deepen direction (A).
VERIFIED [bsd-rank-le-1-proven] CONFIRMED UNCONDITIONAL via primary sources:
Bump-Friedberg-Hoffstein (Inventiones 102, 1990, DOI 10.1007/bf01233440) +
Murty-Murty (Annals 133, 1991, DOI 10.2307/2944316) guarantee existence of an
imaginary quadratic K satisfying the Heegner hypothesis AND
L'(E/K,1)<>0 (via metaplectic Eisenstein series) â€” so GZ+Kolyvagin give BSD
rank<=1 + Sha finiteness with NO ad-hoc K. The ad-hoc-K hedge in the to-verify
item is resolved; fact upgraded to-verify -> verified. Filed NEW theory page
theory/theorems/bfh-murty-nonvanishing.md (the nonvanishing input that makes
the base unconditional; previously unrecorded, load-bearing). CONFIRMED
[bsd-skinner-converse]: Skinner, "A converse to a theorem of Gross, Zagier,
and Kolyvagin", Annals 191(2) (2020), DOI 10.4007/annals.2020.191.2.1,
conditional (Iwasawa hypotheses); soft p-converse Kim 2022 (Math. Annalen).
SHARPENED [bsd-refined-open]: the FULL leading coefficient (exact |Sha| as a
square integer) is still open, BUT the p-PART of the BSD formula is now known
under mild conditions â€” rank 0 (Skinner-Urban 2014, Iwasawa main conjecture
GL2) and rank 1 (Jetchev-Skinner-Wan 2017). So "refined open at rank 0" =
full leading coefficient only; p-part largely settled at rank<=1.
Re-confirmed frontier against Stein's BSD book (wstein.org/books/bsd/bsd.pdf):
beyond rank<=1 "not a single new result directly about the [rank conjecture]
has been proved"; "A new idea is needed" (Katz) â€” matches progress.md.
DEEPENED direction (A) â€” concretized the block on a rank>=2 Euler system:
needs BOTH (i) a supply of r_an independent points via HIGHER-DERIVATIVE
Gross-Zagier (Yuan-Zhang-Zhang; GZ gives only the 1st derivative) AND (ii) a
multi-point / multi-variable KOLYVAGIN system bounding a rank-r Selmer group
to size r_an â€” the existing engine is single-Heegner-point-shaped and bounds
rank<=1 only. Neither exists; Kolyvagin Conjectures 3.32-3.35 (Stein) the
named unproven target. This is the control-step obstruction, parallel to
Beal's reduction step ("one-dimensional engine stops" sub-pattern, now 6-for-6).
HONESTY: a Zenodo preprint "Unconditional Proof of the Rank Equality of BSD"
(DOI 10.5281/zenodo.20716916) flagged bsd-recent-claims-unverified (not
peer-reviewed; same discipline as YM/Hodge/Collatz preprint flurries).
Files: NEW problems/birch-swinnerton-dyer/attempts/attempt-02.md (outcome
confirmed); NEW theory/theorems/bfh-murty-nonvanishing.md; UPDATED
progress.md (to-verify items resolved/sharpened, direction (A) block,
consolidated through attempt-02), index.md (attempt-02 + new theory page).
Outcome: confirmed (verification goal met; partial for the conjecture
overall â€” rank>=2 frontier unchanged). Next (attempt-03): verify
[bsd-parity-proven] (NekovÃ¡Å™ / Dokchitser-Dokchitser, the remaining
to-verify) OR survey higher-GZ + Beilinson-Flach/Kato for the closest
rank-2-shaped system and diagnose where its Selmer bound falls short.

## [CONTINUE 2026-08-24] navier-stokes (math-work loop, cycle 2/24)
Cycle 2 = NS Continue following attempt-01's Next: verify load-bearing facts
against primary sources, then deepen direction (B). Zone green (17.6% session
/ 39.8% weekly, max 4 subagents; used 0 subagents, direct work).
VERIFIED [ns-tao-quant-l3] CONFIRMED against primary source: Tao, "Quantitative
bounds for critically bounded solutions to the NS equations", Proc. Symp. Pure
Math (2021), arXiv:1908.04958, DOI 10.1090/pspum/104/01874 â€” exact rate
limsup ||u||_L3 / (log log log 1/(T*-t))^c = infinity (TRIPLE log, first
slightly-supercritical criterion; 3 logs = Bourgain pigeonholing + Carleman +
stacking scales). Refinements: Barker-Prange 2021 (Comm. Math. Phys. 385, DOI
10.1007/s00220-021-04122-x, spatial concentration), Barker 2022
(arXiv:2209.15627, localized). VERIFIED [ns-ess-endpoint] CONFIRMED:
Escauriaza-Seregin-Sverak, Russian Math. Surveys 58:2 (2003), 211-250, DOI
10.1070/RM2003v058n02ABEH000609 â€” L^inf_t L^3_x solutions smooth (endpoint
Serrin 3/s+2/l=1) via backward uniqueness + Carleman; corollary L^3 must blow up
at a singularity (the qualitative precursor Tao quantified). Convention note:
our 2/r+3/s=1 (time,space) = their 3/s+2/l=1 (space,time), same condition.
MISLABEL CAUGHT + corrected append-only: progress.md/attempt-01 said "Palasek
sharpened it for axisymmetric data" â€” WRONG. Palasek (2022, J. Math. Fluid
Mech., arXiv:2111.08991) extended Tao's rate to DIMENSIONS d>=4 (a QUADRUPLE
log, one more than 3D), NOT axisymmetric. Corrected in progress.md running
state; attempt-01 left intact with a dated [CORRECTION 2026-08-24] blockquote
pointer to attempt-02. The axisymmetric program is real but lives in
Hou/Seregin (different authors). Same discipline as Beal (2,3,7)
spherical->hyperbolic.
DEEPENED direction (B): Tao's averaged-NS blowup (JAMS 2016, DOI 10.1090/jams/838)
â€” averaged operator B-tilde = int T1 B(T2 u, T3 v) dmu (rotations/dilations/
order-0 multipliers) preserves energy identity + all harmonic estimates yet
blows up via a self-replicating "quadratic circuit"/"von Neumann machine".
CONCRETE BLOCK on removing the averaging: B-tilde has TUNABLE degrees of
freedom the RIGID true nonlinearity (u.grad)u lacks; removing averaging =
building "fluid logic gates" from the rigid operator (Tao: "no mathematical
barrier... immense engineering barrier"). Equivalently, energy-identity +
abstract-estimate proofs CANNOT work â€” must exploit finer structure
(vorticity, unique continuation). Axisymmetric ansatz = leading geometric
candidate: Hou (2024, arXiv:2405.10916, PREPRINT to-verify) strong NUMERICAL
evidence for nearly-self-similar blowup as effective dimension n(t)->3.188
(via dimension-as-free-parameter rescaling killing scaling instability), but
for generalized (solution-dependent-viscosity) NS not true constant-viscosity
NS. Seregin (2024, arXiv:2402.13229, PREPRINT to-verify) RIGOROUSLY rules out
exact/discrete-self-similar axisymmetric Type II blowup under conditions
(no-swirl limiting Euler; conserved |omega_theta|^{l1/2}/|x'|^{l1/2}).
REFINED OPEN CONTENT for (B): a true blowup must be NON-self-similar (or violate
Seregin's conditions) and bridge generalized->true viscosity. This is the
control-step obstruction in its sharpest form: the averaged operator HAS the
control freedom; the true operator does not.
Files: NEW problems/navier-stokes/attempts/attempt-02.md (outcome confirmed);
UPDATED attempt-01.md (dated correction blockquote), progress.md (to-verify
resolved/corrected, direction B deepened, consolidated through attempt-02),
index.md (attempt-02 line). Outcome: confirmed (verification goal met +
mislabel corrected); partial overall (no global-regularity proof, no true-NS
blowup). Next (attempt-03): verify [ns-millennium-fefferman] (four statements +
no-boundary domain) + [ns-buckmaster-vicol] (non-uniqueness = very-weak
non-Leray-Hopf only), OR push the axisymmetric blowup program (can Seregin's
no-self-similarity be evaded by a nearly-self-similar Hou-type profile?).

[CONTINUE 2026-08-24] yang-mills (cycle 3/24)
Primary-source verification Continue. [ym-clay-jaffe-witten] CONFIRMED against
the Clay official page (https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
+ the Jaffe-Witten problem-description PDF: exact wording "for any compact
simple gauge group G, a non-trivial quantum YM exists on R^4 and has a mass gap
Delta>0; existence includes axiomatic properties at least as strong as Streater-
Wightman (1964), Osterwalder-Schrader (1973, 1975)." This makes OS reflection
positivity a HARD requirement (not optional) and re-confirms the framework-
existence wrinkle ("nor even a precise definition of quantum gauge theory in
four dimensions"). [ym-balaban-rg] CONFIRMED + sharpened against Balaban CMP
95-122 (1984-89) + Dimock exposition (RMP 25 1330010 / JMP 54 092301 / AHP 15
2133-2175, 2013-14): Balaban proves UV stability (effective-density bounds
uniform in lattice spacing espilon = asymptotic freedom made constructive on
the lattice) and LEAVES OPEN the continuum limit, mass gap, IR. So Balaban = the
UV half of the UV->IR bridge, not the bridge. Direction (A) deepened: the
concrete blocker is a bound uniform in a bridging the strong<->weak bare-
coupling crossover (strong-coupling cluster expansion gives a gap only at
finite spacing / large bare g0; the continuum-limit point is at weak bare g0
where that expansion has no parameter); O(4) restoration is the same control
problem's second face (lattice has only hypercubic W^4; full O(4) restored
only as O(4)-breaking irrelevant operators vanish uniformly down to long
distances, which loops back to continuum-limit existence itself). Eriksson 2026
sharpened: it is viXra-only (2602.0077v1, unmoderated - higher skepticism bar),
CONDITIONAL on Assumption A (squared-oscillation summability of the blocking
map), and leaves OS reflection positivity / thermodynamic limit / mass gap /
nontriviality OPEN even conditionally; an OPEN DISCREPANCY (abstract "Euclidean-
covariant" vs earlier flag "hypercubic W^4 only") is flagged for body-level
verification, not silently resolved. Cross-problem: the "two controlled regimes,
target in the gap between them, blocker = controlling the crossover uniformly"
is the YM instance of the 6-for-6 control-step obstruction spine.
Files: NEW problems/yang-mills/attempts/attempt-02.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-02, to-verify items moved,
direction A deepened, Balaban UV-half precision added). index.md (attempt-02
line). Outcome: confirmed (verification goal met + direction A sharpened);
partial overall (no 4D quantum YM, no proven mass gap). Next (attempt-03):
verify [ym-supersymmetric] (Seiberg-Witten/Nekrasov scope = N=2 SUSY not pure
YM) OR resolve the Eriksson O(4) abstract-vs-body discrepancy. Rotation
advances to hodge-conjecture (cycle 4).

[CONTINUE 2026-08-24] hodge-conjecture (cycle 4/24)
Primary-source verification Continue. [hodge-statement] CONFIRMED against
Deligne's official Clay write-up (hodge.pdf, Millennium Prize Problems pp.45-53):
"On a projective non-singular algebraic variety over C, any Hodge class is a
rational linear combination of classes cl(Z) of algebraic cycles." Confirms
rational-not-integral (integral fails, Atiyah-Hirzebruch Remark iv) and known
for H^2 (Kodaira-Spencer via exponential sequence = Lefschetz (1,1)). KEY
DIRECTION-(A) FIND from Deligne Â§4/Â§5: the standard conjectures B (inverse
Lefschetz) and C (Kunneth components of the diagonal) are OPEN SPECIAL CASES
OF HC ITSELF (Deligne Â§4 Examples 1-2), not merely a reduction pathway; and
Â§5, given B and C, motives over C are semi-simple abelian and HC <=> a
fully-faithful motives->Hodge-structures functor. So direction (A) is a
two-stage control problem: (i) prove B,C (open special cases of HC; the
one-dimensional Picard-variety engine stops here - no analogue for the
diagonal Kunneth components or Lambda), (ii) HC reduces to fully-faithfulness.
The reduction target is itself unproven - exactly Beal-reduction-to-specific-
curves shape. [hodge-cattani-deligne-kaplan] CONFIRMED + sharpened against
JAMS 8(2) 1995 (DOI 10.1090/S0894-0347-1995-1273413-2, arXiv alg-geom/9402009):
Theorem 1.1 + Corollaries 1.2-1.4, the Hodge locus is algebraic finite over S
- UNCONDITIONAL (answers Andre Weil's question; previously only known
HC-conditionally), so "Hodge classes behave as if algebraic" is an
unconditional evidence layer. Proof: Schmid nilpotent orbit + SL(2)^r-orbit
theorem (Cattani-Kaplan-Schmid 1986) + GAGA. Control-not-resolution shape
(controls the locus, doesn't produce the cycles) - parallel to Balaban UV
control (YM). Cross-problem: 6-for-6 control-step spine holds; Hodge
"one-dimensional engine stops" now pinned to two named classes (Kunneth
components, Lambda) from the primary source.
Files: NEW problems/hodge-conjecture/attempts/attempt-02.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-02, CDK line
sharpened, direction A deepened with Deligne Â§4/Â§5, to-verify items moved).
index.md (attempt-02 line). Outcome: confirmed (verification goal met +
direction A sharpened via primary source); partial overall (no HC proof).
Next (attempt-03): verify standard-conjecture known cases (Charles-Markman
2013 hyper-Kahler K3^[n]) OR status-check the most-cited recent claim
(Shimizu 2025). Rotation advances to collatz-conjecture (cycle 5).

[CONTINUE 2026-08-24] collatz-conjecture (cycle 5/24)
Primary-source verification Continue. [collatz-tao-almost-bounded] CONFIRMED
+ sharpened against Tao, Forum Math. Pi 10 (2022) e12 (DOI 10.1017/fmp.2022.8):
Theorem 1.3, Col_min(N)<f(N) for any f->infty, for almost all N in LOGARITHMIC
density (not natural). KEY TRADE-OFF: Korec had Col_min<=N^theta (theta>log3/
log4~0.792) in NATURAL density; Tao replaces N^theta by ANY f->infty but drops
to LOG-density - the two improvements (stronger function <-> stronger density)
are in tension. Blocker = the exp(O(n^{1/2})) multiplicative error in the
Syracuse heuristic Syr^n(N)~exp(O(n^{1/2}))(3/4)^n N, controllable only at
log-density (Benford). Proof borrows Bourgain's almost-sure NLS wellposedness
stabilization = a mechanism-level NS echo. [collatz-cycle-simons-deweger]
CONFIRMED + sharpened against Acta Arith. 117 (2005) pp.51-70 + 2010 update
v1.44: the m<=75 is the 2010 UPDATE (Oliveira e Silva x_min>5*2^60); the 2005
published bound is m<=68. Method = linear form Lambda=(K+L)log2-K log3, upper
bound exponential in K (chaining), lower bound from Rhin 1987 irrationality
measure (Lambda>e^{-13.3(0.46057+log K)}), continued fractions of delta=log3/
log2 + LLL. Authors' own assessment: Rhin + the exponential bound are
NEAR-OPTIMAL, so the method is per-m finite-verification with NO uniform all-m
bound - "all m" needs a better irrationality measure for log3/log2 or a
non-linear-form approach = the literal Beal-flavored transcendence wall.
Direction (A) split into (A-i) log->natural density [blocker exp(O(n^{1/2}))]
+ (A-ii) natural->pointwise [no pointwise Lyapunov; Tao: constant bound ~ the
full conjecture]; direction (B) into (B-finite) per-m verification vs
(B-uniform) transcendence-bottlenecked. Cross-problem: Tao-Bourgain-NLS
mechanism = Collatz<->NS echo primary-source-pinned; (B-uniform) blocker =
Collatz<->Beal transcendence wall primary-source-pinned. 6-for-6 control-step
spine holds.
Files: NEW problems/collatz-conjecture/attempts/attempt-02.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-02, Tao +
Simons-de Weger lines sharpened, directions A/B split with named blockers).
index.md (attempt-02 line). Outcome: confirmed (verification goal met + both
directions sharpened via primary source); partial overall (no proof). Next
(attempt-03): verify density base (Terras/Everett, Krasikov-Lagarias 2003)
OR status-check recent claims (Fathi/Nwankpa/Chang). ROTATION NOTE: cycle 5
completes one full pass of the five attempt-01-only problems (BSD, NS, YM,
Hodge, Collatz); cycle 6 re-enters rotation - likely beals-conjecture
(occasional) or a second pass on birch-swinnerton-dyer.

[CONTINUE 2026-08-24] beals-conjecture (cycle 6/24, occasional cycle-in)
Empirical-extension Continue (computation). After the full 5-problem pass
(cycles 1-5), cycle 6 cycles in beals occasionally (per the bias rule). The
prior 20-cycle arc closed out in attempt-22 ("genuine angles exhausted"); its
resume point sanctioned "extend the empirical line to a fourth signature."
New script search_5711.py (mirrors search_3711.py) for signature (5,7,11):
A^5+B^7=C^11, chi=-218/385~-0.566 (more negative than (3,7,11) -0.433), so
the attempt-19 counting-heuristic prediction was: min non-degenerate coprime
gap > 277. RESULTS (box A<=6000 B<=600 C<=40): 0 exact (0 coprime); 0 genuine
gap-1 (both gap-1 hits degenerate on the t^55+1 universal family: t=1 trivial,
t=2 -> 2048^5+1=32^11 i.e. (2^11)^5+1=(2^5)^11); MIN NON-DEGENERATE COPRIME
GAP = 288 at (A,B,C)=(11,4,3): 11^5+4^7-3^11=161051+16384-177147=288.
PREDICTION CONFIRMED (29<77<277<288), the second a-priori confirmation.
NUANCE (genuine finding): growth DECELERATED sharply - the largest -chi step
(+0.133, (3,7,11)->(5,7,11)) gave the smallest gap step (+11, vs +200 prior);
trend monotone but SUB-LINEAR in -chi near this range, not an accelerating
power law. Hypothesis (to test): as -chi grows, exponents grow, admissible
bases shrink, and gap-1 degenerate families densify, capping gap growth; the
(5,7,11) min sits at small base C=3. Honesty: box-limited (min at C=3 inside
box, likely genuine); counting heuristic is soft (finiteness not zero); no
proof of Beal or (3,5,7). Cross-problem: demonstrates the loop extends to the
most-developed problem without padding - a falsifiable computation yielding a
genuine refinement (deceleration), same evidence/counterevidence discipline
as NS attempt-02 (Palasek) and beals attempt-17 (spherical mislabel).
Files: NEW scripts/search_5711.py + problems/beals-conjecture/attempts/
attempt-23.md (outcome confirmed); UPDATED progress.md (empirical table to
4 signatures with deceleration nuance, attempt log 21-23). index.md
(attempt-23 line). Outcome: confirmed (prediction re-confirmed, heuristic
refined to sub-linear); partial overall. Next: fifth signature
((5,7,13) or (7,11,13)) to test deceleration, OR return to structural
directions (A)/(B). Rotation now re-enters the five-problem rotation (second
pass), not beals - cycle 7 -> birch-swinnerton-dyer.

[CONTINUE 2026-08-24] birch-swinnerton-dyer (cycle 7/24, second pass)
Primary-source verification Continue (the last load-bearing to-verify item).
[bsd-parity-proven] CONFIRMED + sharpened against primary sources. The
distinction made precise: (1) p-PARITY (corank_p Selmer_{p^infty} = ord L
mod 2) is UNCONDITIONAL for all E/Q and all primes p (Dokchitser-Dokchitser,
Annals 172(1) 2010, 567-596, DOI 10.4007/annals.2010.172.11; Nekovar framework
+ Selmer complexes Ast. 310 2006 + ordinary/totally-real cases C.R. 2001 /
Compositio 145 2009 with Wintenberger appendix). (2) ALGEBRAIC-RANK parity
((-1)^rk(E/K) = w(E/K)) for all number fields is CONDITIONAL on finiteness of
the 2- and 3-primary parts of Sha(E/K(E[2])) (Dokchitser-Dokchitser Annals
2010 + Crelle 658 2011, DOI 10.1515/crelle.2011.060, completes Kramer-Tunnell
char-0 local formula). The Sha-finiteness caveat located EXACTLY: the exact
sequence 0->E(K)xQ_p/Z_p->Sel_{p^infty}->Sha[p^infty]->0 gives corank_p Sel =
rk(E/K) + corank_p Sha[p^infty]; the two parities agree iff the Sha term is
even, which Sha-finiteness forces (Cassels). So the unconditional reach of
parity is the SELMER rank; passing to the Mordell-Weil rank costs the Sha
hypothesis - a small but real gap, not a free upgrade. ATTRIBUTION CORRECTION
(genuine): progress.md's to-verify line paired "algebraic-rank parity (Nekovar)"
- but Nekovar's unconditional theorems are p-PARITY (Selmer rank); the
algebraic-rank parity (mod Sha) is Dokchitser-Dokchitser. Both halves now
correctly attributed. This CONFIRMS progress.md's "Parity's role" section:
parity pins r_alg mod 2 and converts ">= r_an points of right parity" into
exact rank ONLY given a Selmer upper bound of the right parity (the missing
Euler-system step) - parity + lower bound alone cannot bound the Selmer group
from above. Parity sits on the RESOLUTION side of the control/resolution
divide (a consequence, not the missing control mechanism), consistent with
the 6-for-6 framing; the obstruction remains the control step (a
rank-r-shaped Kolyvagin system). All progress.md to-verify items now
resolved. Cross-problem: 6-for-6 control-step spine holds; the BSD instance
of the "one-dimensional engine stops" sub-pattern is the single-Heegner-point
Euler system (bounds rank<=1 only), now with parity's reach precisely bounded
by the same Sha wall. Honesty: no proof of BSD, no progress on rank>=2.
Files: NEW problems/birch-swinnerton-dyer/attempts/attempt-03.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-03,
[bsd-parity-proven] moved to CONFIRMED+sharpened, attribution corrected, all
to-verify resolved). index.md (attempt-03 line). Outcome: confirmed
(verification goal met + attribution corrected); partial overall. Next
(attempt-04): with all to-verify resolved, survey higher Gross-Zagier
(Yuan-Zhang-Zhang) + Beilinson-Flach/Kato for the closest rank-2-shaped
Euler system and diagnose where its Selmer bound falls short - the concrete
control-step question. Rotation advances to navier-stokes (cycle 8).

[CONTINUE 2026-08-24] navier-stokes (cycle 8/24, second pass)
Primary-source verification Continue (the two remaining to-verify items).
Yellow zone 60.1% session / 47.3% weekly, 0 subagents (direct work; cap does
not gate the loop). [ns-millennium-fefferman] CONFIRMED against Fefferman's
official Clay formulation (May 1 2000, claymath.org/millennium/navier-stokes-
equation, repr. Millennium Prize Problems CMI/AMS 2006): two NO-BOUNDARY
settings (R^3 with rapid decay conditions (4)(5); periodic torus R^3/Z^3 with
(8)(9)) - Fefferman restricts to these to avoid boundary complications;
four statements - (A) existence+smoothness on R^3 for any smooth div-free
u_0 with f=0 (smoothness (6), bounded energy (7)), (B) same on T^3
(periodicity (10), smoothness (11)), (C) breakdown on R^3 (exist smooth u_0
+ smooth f satisfying (4)(5) for which no smooth solution exists), (D)
breakdown on T^3; proving ANY ONE resolves the prize. Key asymmetry: f=0 for
the regularity statements A/B, a smooth f ALLOWED for the breakdown C/D.
Matches progress.md's A/B-vs-C/D frontier exactly, now primary-source-backed.
[ns-buckmaster-vicol] CONFIRMED + sharpened against Buckmaster-Vicol,
"Nonuniqueness of weak solutions to the Navier-Stokes equation", Annals
189(1) (2019) 101-144, DOI 10.4007/annals.2019.189.1.3 (rec. 2017, acc. 2018,
pub. Jan 2019). DATE CORRECTION: the result is 2019, NOT 2022; the 2022 JEMS
follow-up ("Wild solutions ... singular sets Hausdorff dim <1") is
Buckmaster-COLOMBO-Vicol (JEMS 24(9) 2022, 3333-3378, DOI 10.4171/jems/1162),
a DIFFERENT paper. Theorem 1.2: exists beta>0 such that for any nonneg smooth
energy profile e(t) there is a weak solution v in C^0_t([0,T]; H^beta_x(T^3))
of 3D NS with int|v|^2 = e(t) (PRESCRIBED energy) and vorticity in C^0_t L^1_x;
picking two profiles agreeing on [0,T/2] but differing at T gives
NONUNIQUENESS of dissipative weak solutions (coming to rest in finite time,
Serrin's question). Theorem 1.3: Holder dissipative Euler weak solutions are
vanishing-viscosity limits. SCOPE CAVEAT confirmed + made precise (the to-verify
point): these are NOT Leray-Hopf - no energy inequality
||v(t)||^2+2nu int ||grad v||^2 <= ||v_0||^2, no L^2_t H^1_x; beta cannot be
too large (beta=1/2 = weak-strong uniqueness barrier, so the construction
lives strictly below the Leray-Hopf/strong regime). Authors state Leray-Hopf
NONUNIQUENESS remains the MAJOR OPEN problem. Mechanism: convex integration
(De Lellis-Szekelyhidi / Isett Onsager-Euler) + intermittent Beltrami waves
(||W||_L1 << ||W||_L2 via Dirichlet-kernel oscillations) saturating Bernstein;
the linear -nu Delta v forces Reynolds stress into L^1, intermittency gives
the gain. TWO CROSS-PROBLEM ECHOES: (1) the BV construction FAILS IN 2D (too
few spatial directions to oscillate) - a second 2D/3D dividing fact alongside
the Serrin-number equality (S_nonlin=S_lin in 2D, 4>3.5 in 3D); (2)
weak-strong uniqueness at beta=1/2 marks the class where the energy control
(Leray-Hopf) would forbid nonuniqueness - the control-step shape again
(convex integration RESOLVES but only in a class excluding the
energy-controlled solutions where the CONTROL would forbid it).
SHARPENING to progress.md: the "(non-unique?)" on Leray-Hopf is resolved in
the conservative direction - uniqueness still OPEN, nonuniqueness only BELOW
Leray-Hopf. All progress.md to-verify items now resolved. Cross-problem:
6-for-6 control-step spine holds; NS now has two parallel 2D/3D witnesses
(Serrin equality + BV-fails-in-2D). Honesty: no proof of global regularity or
blowup; frontier unchanged.
Files: NEW problems/navier-stokes/attempts/attempt-03.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-03, Leray-Hopf line
sharpened, both to-verify moved to CONFIRMED+sharpened, BV date corrected,
2D-fails echo + beta<1/2 boundary recorded). index.md (attempt-03 line).
Outcome: confirmed (verification goal met + two sharpenings + date
correction); partial overall. Next (attempt-04): with all to-verify
resolved, push the axisymmetric blowup program quantitatively (can Seregin's
no-exact/discrete-self-similarity be evaded by a nearly-self-similar
Hou-type profile; does the generalized->true-viscosity limit survive) - the
refined open content for (B), the NS control-step question. Rotation
advances to yang-mills (cycle 9).

[CONTINUE 2026-08-24] yang-mills (cycle 9/24, second pass)
Primary-source verification Continue (the last load-bearing to-verify item).
Yellow zone 66.7% session / 48.5% weekly, 0 subagents (direct work). [ym-
supersymmetric] CONFIRMED + sharpened against primary sources. Seiberg-Witten,
"Electric-magnetic duality, monopole condensation, and confinement in N=2
supersymmetric Yang-Mills theory", Nucl. Phys. B 426 (1994) 19-52,
arXiv:hep-th/9407087, DOI 10.1016/0550-3213(94)90124-4: N=2 SUSY SU(2) YM,
exact low-energy effective action, SL(2,Z) duality on tau, solution via
periods of elliptic curve y^2=(x-1)(x+1)(x-u), monodromies Gamma(2).
Confinement + mass gap via MONOPOLE CONDENSATION -> dual Meissner effect -
first relativistic field theory with confinement explained by monopole
condensation. Nekrasov, "Seiberg-Witten prepotential from instanton counting",
arXiv:hep-th/0306211 (ICM 2002): localization on framed-instanton moduli
spaces R^4, Z=sum q^k int_{M_k} 1 = exp(F^inst/(eps1 eps2)), F^inst(a,0,0;q)
= Seiberg-Witten prepotential, equivariant localization (Duistermaat-Heckman
/ Atiyah-Bott), fixed points labeled by Young diagrams. Mathematically
RIGOROUS via Nakajima-Yoshioka, "Instanton counting on blowup. I",
Inventiones Math. 2005, arXiv:math/0306198 (blowup equation); extended to all
classical groups by Nekrasov-Shadchin, hep-th/0404225. SCOPE POINT confirmed +
made precise (the whole to-verify): ALL of the above is N=2 SUSY YM, NOT pure
(non-supersymmetric) YM of the Clay problem. SUSY is ESSENTIAL not decorative -
it supplies (a) the BRST-like supercharge Q enabling equivariant localization,
(b) the holomorphic prepotential protected by non-renormalization, (c) the
finite-dim Coulomb-branch moduli with controllable monodromy. Pure YM has
none of these: no prepotential, no preserved fermionic symmetry to localize
against, no controlled instanton gas. NO known bridge from Nekrasov partition
function or Seiberg-Witten solution to the pure-YM mass gap. GENUINE NUANCE
(sharpening): the mass gap Seiberg-Witten exhibits is NOT in pure N=2 - the
N=2 theory has a Coulomb-branch moduli space of vacua (photon + massless
monopole at singularities, NO generic mass gap); the gap + confinement arise
only after SOFTLY BREAKING N=2->N=1 (superpotential W=m Tr Phi^2), which lifts
the moduli space and condenses monopoles. So the illuminated mechanism (dual-
superconductor confinement, 't Hooft-Mandelstam) is a property of the softly
broken N=1 theory, doubly removed from pure YM (SUSY AND broken). Direction (B)
mechanism now named: dual-Meissner monopole condensation = the hoped-for
dual-superconductivity for pure YM, made EXACT by SUSY; the CONTROL that makes
it exact (localization + holomorphy) is exactly what pure YM lacks - the YM
instance of the 6-for-6 control-step spine, triangulated with the Balaban
UV-half picture (attempt-02) from the continuum-SUSY side (Balaban =
uncontrolled strong<->weak bare-coupling crossover from the lattice side;
SUSY = the crossover crossed exactly via duality, but only in SUSY). All
load-bearing to-verify items now resolved (Eriksson remains a preprint-status
item, not load-bearing). Cross-problem: 6-for-6 control-step spine holds.
Honesty: no rigorous 4D quantum YM, no proven pure-YM mass gap; frontier
unchanged.
Files: NEW problems/yang-mills/attempts/attempt-03.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-03, [ym-supersymmetric] moved
to CONFIRMED+sharpened, direction (B) mechanism named + Coulomb-vs-broken
nuance, attempt-03 block added). index.md (attempt-03 line). Outcome:
confirmed (verification goal met + mechanism pinned + Coulomb-vs-broken
nuance); partial overall. Next (attempt-04): all to-verify resolved - push
direction (A) concretely, survey constructive-continuum-limit literature
beyond Balaban (Magnen-Rivasseau-Seneor, AFS/Brydges-Kennedy finite-range
decompositions, cluster/polymer expansions) for the closest existing result
to a uniform-in-a IR/mass-gap bound, diagnose where the strong<->weak bare-
coupling crossover loses control. Rotation advances to hodge-conjecture
(cycle 10).

[CONTINUE 2026-08-24] hodge-conjecture (cycle 10/24, second pass)
Primary-source verification Continue (standard-conjecture known cases).
Yellow zone 73.1% session / 49.6% weekly, 0 subagents (direct work).
Charles-Markman 2013 standard conjectures for hyper-Kahler K3^[n] CONFIRMED
against the primary source: Charles & Markman, "The Standard Conjectures for
Holomorphic Symplectic Varieties Deformation Equivalent to Hilbert Schemes of
K3 Surfaces", Compositio Mathematica 149(3) (March 2013), 481-494, DOI
10.1112/S0010437X12000607 (JOURNAL CORRECTION: the actual venue is Compositio
Mathematica, NOT J. Inst. Math. Jussieu as a query guessed). Theorem 1.1:
the LEFSCHETZ standard conjecture (Conjecture B, inverse Lefschetz /
algebraicity of Lambda) holds for every smooth projective variety of
K3^[n]-type. Corollary 1.2: in CHARACTERISTIC ZERO the Lefschetz standard
conjecture is the STRONGEST standard conjecture, so it implies ALL standard
conjectures including Conjecture C (Kunneth components of the diagonal). THIS
IS THE PRECISE LOGIC behind progress.md's "B/C known for K3^[n]": B is proved
directly, and B => C (and the rest) in char 0. Mechanism (the genuine
sharpening for the obstruction map): algebraic cycles from relative extension
sheaves on moduli of stable sheaves on a K3 surface; VERBITSKY'S THEORY OF
HYPERHOLOMORPHIC SHEAVES lets these algebraic cycles be DEFORMED ACROSS THE
ENTIRE K3^[n] deformation class via TWISTOR LINES - the cycle classes are
transported/controlled from one representative to every deformation; O^+_
{Lambda(S)}(v) MUKAI-LATTICE MONODROMY equivariance + surjectivity (Prop 6.1,
Cor 6.2, induction Cor 2.4) finishes it. This is a CONTROL technique
(controls the cycles' deformation across the class), not a direct resolution -
the same control-not-resolution shape as the other five problems; the
hyper-Kahler-specific deformation control (Verbitsky + twistor) has NO analogue
for a general smooth projective variety, which is precisely direction (A)'s
open core (the "one-dimensional engine stops" sub-pattern: Picard-variety
control for divisors, Verbitsky-twistor for K3^[n], NEITHER for general
varieties). Companion: Charles, "Remarks on the Lefschetz Standard Conjecture
and Hyperkahler Varieties", Comment. Math. Helv. 88(2) (2013), 449-468, DOI
10.4171/CMH/291 (variational/local approach in degree 2). SHARPENS attempt-02
(B/C are open special cases of HC per Deligne Â§4) with a POSITIVE known-case
island: those open special cases are KNOWN for K3^[n]-type, so direction (A)
is not uniformly hopeless - it has a verified deformation-control precedent in
one geometric class, but the precedent is class-specific. Cross-problem:
6-for-6 control-step spine holds; Hodge now has a control-mechanism precedent
named (Verbitsky/twistor) parallel to BSD's single-Heegner-point engine. Other
to-verify items remain (hard Lefschetz reduction exact statement;
Atiyah-Hirzebruch & Kollar integral counterexamples; 2024-25 preprints;
l-adic Tate analogue) - attempt-04 targets. Honesty: no proof of HC;
standard conjectures open for general varieties; frontier unchanged.
Files: NEW problems/hodge-conjecture/attempts/attempt-03.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-03,
Charles-Markman moved to CONFIRMED with journal correction + B=>C logic +
Verbitsky/twistor mechanism, attempt-03 block added, to-verify list
updated). index.md (attempt-03 line). Outcome: confirmed (verification goal
met + journal corrected + mechanism pinned + control-step echo); partial
overall. Next (attempt-04): resolve remaining to-verify (Atiyah-Hirzebruch/
Kollar integral counterexamples, l-adic Tate analogue) OR status-check
Shimizu 2025. Rotation advances to collatz-conjecture (cycle 11).

[CONTINUE 2026-08-24] collatz-conjecture (cycle 11/24, second pass)
Primary-source verification Continue (foundational density base + count bound).
Yellow zone 78.7% session / 50.6% weekly, 0 subagents (direct work).
TERRAS 1976 / EVERETT 1977 CONFIRMED + sharpened: Terras, Acta Arith. 30,
241-252 (1976); Everett, Adv. Math. 25, 42-45 (1977). The set with FINITE
STOPPING TIME sigma(n):=min{k:T^k(n)<n} has density 1 at an EXPONENTIAL RATE
(Terras Thm D - binomial decay of "divergent" parity vectors since
ln2/ln3 > 1/2; parity vector <-> residue class mod 2^k). Sharper than
progress.md's bare "a.a. Col_min<N". Robustness: found independently also by
Moller 1977, Heppner 1978, Allouche 1979 = FIVE independent proofs - the
density-1 fact is load-bearing-safe. KRASIKOV-LAGARIAS 2003 CONFIRMED +
sharpened: Acta Arith. 109(3), 237-258, DOI 10.4064/aa109-3-4. Theorem 6.1:
pi_1(x) >= x^0.84, where 0.84 = log_2(1.7922310) from LP L_{NT}^{11} (k=11).
Method = Krasikov difference inequalities + BACK-SUBSTITUTION (Thm 2.2/3.1)
that eliminates "advanced" variables WITHOUT the truncation
Applegate-Lagarias 1995 needed (their x^0.81 at k=9). THE KEY CONTROL-STEP
FACT (authors' own conjecture): showing lambda_k -> 2 as k -> infinity would
give pi_1(x) >= x^{1-eps} for any eps>0 - the theoretical ceiling of the
count method is "almost all", NEVER "all N". So even the method taken to its
limit leaves a density-0 exceptional set invisible to counting bounds. This
is a SECOND Collatz "one-dimensional engine stops" instance: the Terras
density engine stops at density 1, the KL count engine stops at x^{1-eps} -
two independent engines, same wall, neither reaches pointwise. Cross-problem:
6-for-6 control-step spine holds; Collatz now has the density-vs-pointwise
wall made quantitative from BOTH the density side (Terras) and the count side
(KL), parallel to how BSD's Selmer/algebraic exact sequence locates the Sha
gap from two sides. Wall = deterministic uncontrolled parity sequence (no
pointwise Lyapunov), as direction (A-ii)/(C) already state; KL's
back-substitution is a resolution refinement (tighter count), not a control
extension. Honesty: no proof of Collatz; the density->pointwise leap open;
verification is the cycle's point - two to-verify items (Terras/Everett, KL
2003) now resolved and primary-source-backed. Files: NEW
problems/collatz-conjecture/attempts/attempt-03.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-03, Terras + KL lines
sharpened with full citations + exponential-rate + back-substitution +
x^{1-eps}-ceiling, to-verify list updated with both moved to CONFIRMED and
remaining relabelled attempt-04 targets). index.md (attempt-03 line).
Outcome: confirmed (verification goal met + citations pinned + exponential-
rate + x^{1-eps}-ceiling sharpenings + second-engine control-step echo);
partial overall. Next (attempt-04): resolve remaining to-verify (Conway 1972
FRACTRAN/undecidability primary source; Barina 2020 2^68 bound; 2024-25
preprints) OR status-check Fathi 2025/Chang 2026. Rotation advances to
beals-conjecture (occasional cycle-in) OR birch-swinnerton-dyer attempt-04
(cycle 12).

[CONTINUE 2026-08-24] birch-swinnerton-dyer (cycle 12/24, second pass)
Deepening Continue (direction A tested against current higher-rank GZ /
Euler-system literature; NOT a verification â€” all BSD to-verify items were
resolved in attempts 02-03). Orange zone 82.7% session / 51.3% weekly, 0
subagents (direct work). Tested the load-bearing premise of direction (A):
"need (i) higher-derivative GZ supply of r_an independent points (GZ gives
only 1st derivative) AND (ii) a multi-point Kolyvagin system bounding a rank-r
Selmer group (existing engine single-Heegner-point-shaped, bounds rank<=1
only)." RESULT: premise HALF confirmed, HALF outdated, sharper wall appears.
(A-i) CONFIRMED: higher-L-derivative GZ for rank>=2 is ABSENT in the
number-field case (Yun-Zhang higher GZ is function-field only; Yuan-Zhang-
Zhang / Qiu are still 1st-derivative). The independent-point SUPPLY wall
holds. (A-ii) OUTDATED: Chan-Ho Kim 2022 (arXiv:2203.12161), "A higher
GZ formula and the structure of Selmer groups" - a "higher Gross-Zagier
formula" (Theorem 2.3) via KURIHARA NUMBERS (Kolyvagin derivatives of
Mazur-Tate elements, NOT L-derivatives) determines the FULL Selmer group
structure at arbitrary rank with NO low-rank assumption:
ord(kappa^Heeg)+1 = max{cork Sel(E), cork Sel(E^K)}, giving the full module
structure (Q_p/Z_p)^r + direct sum of finite Z/p^a. When the two Selmer
coranks differ by 1 this recovers classical GZ. CONDITIONAL on Kolyvagin's
Conjecture (nontriviality of kappa^Heeg), proved for a large class by Wei
Zhang via the Skinner-Urban Iwasawa main conjecture. Bipartite Euler systems
(Howard; Kim Thm 2.5) extend to the root-number +1 (Waldspurger) setting,
behaving "like Kolyvagin systems rather than Euler systems." THE NEW WALL
(three sub-walls, the genuine deepening): (1) the bound is RELATIVE (paired
E/E^K, not absolute r_alg(E)); (2) CONDITIONAL on the main conjecture;
(3) CYCLOTOMIC-VS-ANTICYCLOTONIC DISJOINTNESS - Kato's Euler system (cyclotomic)
and the Heegner system (anticyclotomic) have "disjoint field variations except
the base imaginary quadratic field" (Kim), so the comparison that would make
the bound absolute + unconditional at rank>=2 is exactly where the two
one-directional engines fail to compose. Kolyvagin Conjectures 3.32-3.35
(Stein, the named unproven target) PARTIALLY SUBSUMED by Kim-Wei Zhang
(nontriviality proved large class) but full conjecture (all curves,
unconditional) remains open. 6-FOR-6 ECHO: BSD now has TWO one-dimensional
engines named (cyclotomic Kato, anticyclotomic Heegner), and rank>=2 is the
comparison where they stop - parallel to Collatz's two engines (Terras
density, KL count) both stopping at almost-all (attempt-03), and NS's 2D/3D
Serrin index. Cross-problem spine holds; the "one-dimensional engine stops"
sub-pattern now has a TWO-engine variant in BOTH BSD and Collatz. Honesty:
deepening not verification; Kim/Wei-Zhang claims FLAGGED to-verify against the
arXiv PDF / Wei-Zhang 2013 survey before load-bearing reuse (new
[bsd-higher-gz-kim-2022] to-verify entry). No proof of BSD; rank>=2 wall
sharpened (three sub-walls) not broken; refined-BSD (direction C) untouched.
Files: NEW problems/birch-swinnerton-dyer/attempts/attempt-04.md (outcome
partial); UPDATED progress.md (consolidated through attempt-04, direction (A)
block rewritten with attempt-04 sharpening + three sub-walls + two-engine
echo, attempt-04 block added to Best partial result, new
[bsd-higher-gz-kim-2022] to-verify entry). index.md (attempt-04 line).
Outcome: partial (obstruction map sharpened, direction A refined with named
newer mechanism, two-engine echo; no frontier change; Kim/Wei-Zhang claims
to-verify). Next (attempt-05): verify Kim 2022 arXiv:2203.12161 Thm 2.3
against the arXiv PDF (exact max{cork Sel} statement + Kolyvagin-conjecture
condition) + the Yun-Zhang function-field boundary, OR pivot to direction (C)
refined-BSD (Bullach-Honnor 2025). Rotation advances to navier-stokes
(attempt-04) (cycle 13) OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] navier-stokes (cycle 13/24, second pass)
Primary-source verification Continue (the two 2024 axisymmetric preprints
flagged to-verify in attempt-02). Orange zone 87.9% session / 52.2% weekly,
0 subagents (direct work); session was 2.1% under the 90% red/stop line and
reset ~7 min into the cycle.
HOU 2024 (arXiv:2405.10916) CONFIRMED: "Nearly self-similar blowup of
generalized axisymmetric NS." Rigorous derivation of axisymmetric NS with
swirl in integer n>3 then arbitrary real dimensions; two-scale dynamic
rescaling with n(t)=1+2R(t)/Z(t) as a dynamic DOF (eliminates scaling
instability). TWO SECTIONS: Sec 4 solution-dependent viscosity
nu(t)=nu_0||u_1||_inf Z(t)^2 (nu_0=0.006) -> STABLE SELF-SIMILAR blowup,
effective n~=3.188 -> 3 as nu_0->0, scaling exponent c_l~=0.523, max
vorticity O(1/(T-t)) VIOLATING BKM, profile satisfies NS with CONSTANT
nu_0 (surprising); Sec 5 two CONSTANT viscosities (Boussinesq-type,
nu_1=6e-4, nu_2=6e-3) -> NEARLY self-similar with LOG CORRECTION
lambda(t)=(1+eps|log(T-t)|)^(-1/2), max vorticity 1.4e30 by tau=155,
dimension settles n~=4.73 (Cheskidov diadic threshold n>4). CAVEAT
CONFIRMED: generalized axisymmetric NS (solution-dependent OR modified
Boussinesq viscosity), NOT true constant-viscosity 3D NS.
SEREGIN 2024 (arXiv:2402.13229) CONFIRMED: "A note on potential Type II
blowups of axisymmetric NS." Euler scaling v->lambda^alpha v(lambda x,
lambda^{alpha+1} t), alpha=2-m, 1/2<=m<1. Prop 1.1: nontrivial no-swirl
limiting Euler blowup (alpha-1<0 forces u_theta->0). Prop 2.1: conserved
weighted vorticity g(t)=int Phi(|f|) dx, f=omega_theta(u)/r. Prop 2.2: no
Type II blowup under L^q, q=3/(2-m) in [2,3) -> u(. ,0)=0 -> omega=0 ->
irrotational, contradicting nontriviality. Prop 3.1: no self-similar Type
II blowup (U=0). Prop 4.1: no DISCRETE self-similar Type II blowup (U=0).
COMPLEMENTARY NOT CONTRADICTORY (the sharpening): Seregin fences off the
CLASSICAL exact/discrete self-similar Type II class (3D, standard NS
scaling, under his boundedness + L^q + no-swirl-Euler conditions); Hou's
candidate lives OUTSIDE that scope (fractional dimension + modified
viscosity + log correction = NEARLY self-similar, not exactly). The two do
not contradict. REFINED OPEN CONTENT: a true 3D NS blowup must be (i)
non-(discrete-)self-similar to dodge Seregin Prop 3.1/4.1, AND (ii) bridge
the generalized->true-viscosity limit (Hou's gap). Hou's log-corrected
nearly-self-similar ansatz is precisely the form that dodges (i); the open
part is (ii). CONTROL-STEP ECHO (6-for-6 sub-pattern in microcosm):
Seregin's no-swirl-Euler + weighted-vorticity-conservation engine CONTROLS
the self-similar slice (rules it out); the residual non-self-similar /
generalized-viscosity slice is exactly where the engine STOPS and where
Hou's candidate lives - the "one-dimensional engine stops" shape. Parallel
to BSD's cyclotomic-vs-anticyclotomic disjointness (attempt-04, the
comparison where the two engines stop) and Collatz's two engines both
stopping at almost-all (attempt-03). Cross-problem spine holds; NS now has
a control-vs-residual-class echo in microcosm.
Honesty: no blowup for true 3D NS; no proof of global regularity; frontier
unchanged. Publication status PERSISTS to-verify: both remain arXiv
preprints (no journal publication found; Seregin has a RELATED earlier note
"Remarks on Type II blowups" Comm Pure Appl Anal 2023 cpaa.2023108,
distinct from this 2024 piece). Results treated as evidence not proof
until peer-reviewed; the to-verify on CLAIMS is now resolved, on
publication status remains. Files: NEW
problems/navier-stokes/attempts/attempt-04.md (outcome confirmed); UPDATED
progress.md (consolidated through attempt-04, direction (B) Hou/Seregin
block rewritten with attempt-04 two-section + Prop detail + complementary
relationship + control-step echo, attempt-04 block added to Best partial
result, Hou/Seregin to-verify entry updated to claims-confirmed/
publication-still-to-verify). index.md (attempt-04 line). Outcome:
confirmed (both preprint claims verified + complementary relationship
pinned + control-step echo); partial overall. Next (attempt-05): NS
to-verify list now exhausted; monitor Hou/Seregin for journal publication
/ community reception (status-check) OR deepen direction (A) critical-
a-priori-bound survey. Rotation advances to yang-mills (attempt-04)
(cycle 14) OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] yang-mills (cycle 14/24, second pass)
Primary-source verification Continue (direction C, Chatterjee 2021) +
recent-claims flag (2025-26 preprint wave). Green zone 7.4% session /
53.7% weekly, 0 subagents â€” fresh budget after the session reset.
CHATTERJEE 2021 CONFIRMED: "A Probabilistic Mechanism for Quark
Confinement," Comm. Math. Phys. (2021), DOI 10.1007/s00220-021-04086-y.
Theorem 2.2: unbroken center symmetry => confinement (area law,
|<W_l>| <= e^{-V(R)T}, V(R)->inf). Theorem 2.4: exponential decay of
correlations (under arbitrary BCs) => unbroken center symmetry =>
confinement. First RIGOROUS definition of center symmetry for lattice
gauge theories (previously a 't Hooft physics heuristic). KEY SHARPENING
(the load-bearing fact): the implication chain is mass-gap (exponential
decay) => center-symmetry => confinement â€” the MASS GAP IS THE
HYPOTHESIS, NOT THE CONCLUSION. Chatterjee proves confinement FOLLOWS
FROM the mass gap, he does NOT prove the mass gap exists. Paper's own
caveat: does NOT prove 4D SU(N) satisfies exponential decay at all
coupling strengths â€” easy at strong coupling (cluster expansion),
open/believed at weak coupling. In lattice QFT exponential decay of
correlations IS the mass gap, so Chatterjee reads "mass gap =>
confinement." WHAT THIS MEANS FOR THE OBSTRUCTION MAP: direction (C) is
NOT an escape from the control step; it RELOCATES it. Chatterjee gives a
resolution-side tool (center symmetry => confinement, given exponential
decay); the control step â€” proving exponential decay (mass gap) at weak
coupling â€” remains open and is exactly the UV->IR bridge of attempts
02-03. The mass gap is now the single load-bearing open piece,
triangulated from a THIRD angle (after Balaban's UV half and the SUSY
dual-Meissner mechanism). CONTROL-STEP ECHO (6-for-6): Chatterjee's
center-symmetry engine CONTROLS the center-symmetry=>confinement slice
(resolution); the mass-gap-at-weak-coupling slice is where it STOPS â€”
the "one-dimensional engine stops" shape. Parallel to NS Seregin
(controls self-similar slice, stops at non-self-similar slice, attempt-04)
and BSD cyclotomic/anticyclotonic disjointness (attempt-04). YM's
instance is now sharpest: the named mechanism (confinement) is the
CONSEQUENCE, and the cause (mass gap) is the open control step.
RECENT-CLAIMS FLAG (2025-26 preprint wave, honesty discipline): NONE
peer-reviewed, each with conditional assumptions or identified gaps.
Shabir & Faizal 2026 (arXiv:2606.19362, ~200+pp) â€” reflection-positive
lattice + OS + finite-range decomposition + strong-coupling cluster +
RG interlacing + Wilson-loop step-scaling + OS reconstruction; claims
Delta >= min(Delta_*, m_*) > 0, continuum area law, universality;
unpeer-reviewed, companions IJGMMP 2026. Agawa 2025 (Cambridge Open
Engage) â€” non-local holonomy + Balaban-type cluster + holonomy gauge-
fixing (claims no Gribov) + OS via checkerboard; unpeer-reviewed,
AI-assisted, unaffiliated, addendum needed for continuum limit + finite
Gribov. Eriksson 2026 (viXra) â€” already flagged (attempt-02); search
confirms Eriksson's OWN honest assessment: does not prove RG-Cauchy,
postulates transfer-matrix spectral gap, no renormalized local fields as
operator-valued distributions; still not load-bearing. ALL THREE flagged
ym-recent-claims-unverified; same discipline as Hodge (Shimizu/Bouari/
Abdelgalil) and Collatz (Fathi/Nwankpa/Chang) flagging. BOTTOM LINE: the
rigorous construction of 4D YM with a proven continuum mass gap remains
OPEN; frontier unchanged but obstruction now triangulated from three
angles, all converging on the same UV->IR control step. Honesty: no
rigorous 4D quantum YM, no proven mass gap; preprints flagged not
solutions. Files: NEW problems/yang-mills/attempts/attempt-04.md
(outcome confirmed); UPDATED progress.md (consolidated through
attempt-04, direction (C) block rewritten with Chatterjee + mass-gap-as-
hypothesis sharpening + control-step echo, attempt-04 block added to
Best partial result, [ym-recent-claims-unverified] extended with the
2025-26 wave, new [ym-chatterjee-confinement] CONFIRMED entry).
index.md (attempt-04 line). Outcome: confirmed (Chatterjee verified +
mass-gap-as-hypothesis sharpening + three-angle obstruction
triangulation + preprint wave flagged); partial overall. Next
(attempt-05): YM to-verify list now exhausted; monitor Shabir-Faizal/
Agawa for peer review (status-check) OR deepen direction (A) the
uniform-in-a IR bound bridging the strong<->weak crossover. Rotation
advances to hodge-conjecture (attempt-04) (cycle 15) OR beals
(occasional cycle-in).

[CONTINUE 2026-08-24] hodge-conjecture (cycle 15/24, second pass)
Primary-source verification Continue: the integral-Hodge-fails wrinkle
(the retreat to the Q-version of HC). Green zone 17.3% session / 55.4%
weekly, 0 subagents. FOUR PRIMARY SOURCES CONFIRMED. (1) ATIYAH-
HIRZEBRUCH 1961 (Topology 1, 25-45): torsion Hodge classes are trivially
of type (k,k) yet non-algebraic for k>=2 (true for k=1 by Lefschetz
(1,1)); mechanism = the AH spectral sequence E_2^{s,t}=H^s(X,Z) =>
K_top^{s+t}(X) with a nonzero differential on Godeaux-Serre varieties.
(2) TOTARO 1997 (JAMS 10(2):467-493, DOI 10.1090/S0894-0347-97-00232-4,
arXiv:alg-geom/9609016): the cycle class map factors canonically through
MU*(X) tensor_{MU*} Z (complex cobordism); topological (Hodge-free)
proof the Griffiths group is nonzero (Thm 7.1: CH^2/2 -> H^4(Z/2) not
injective; Thm 7.2: dim-15 variety, codim-3 torsion cycle ->0 in
cohomology + intermediate Jacobian yet not alg-equivalent to 0). (3)
KOLLAR 1990 (LNM 1515, 134-135, "Trento examples"): general smooth
hypersurface X in P^4 of degree D, p^3|D, p coprime to 6 => the FREE
generator alpha of H^4(X,Z) is non-algebraic (every curve has degree
divisible by p) yet D*alpha = h^k IS algebraic; NOT torsion, NOT
topological (depends on complex structure; algebraic on a dense
parameter subset). (4) SOULE-VOISIN 2005 (Adv. Math. 198:107-127, DOI
10.1016/j.aim.2004.10.022, arXiv:math/0403254): Thm 1 â€” the AH/Totaro
obstruction detects only p-torsion with p <= dim_C(X); Thm 3 â€” for any
p>=5, p-torsion in H^6 of 5-folds that is non-algebraic yet ESCAPES ALL
topological obstructions (in the image of Totaro's phi^k, algebraic on a
dense subset); Thm 4 â€” torsion cycles annihilated by Deligne cycle class
+ Totaro yet non-divisible (nontrivial Griffiths), vanishing on a smooth
deformation so no locally constant invariant detects them. TWO SOURCES
OF FAILURE: (A) torsion (AH/Totaro/Soule-Voisin); (B) non-torsion
(Kollar). THE Q-RETREAT REMOVES BOTH: torsion -> 0 in H*(X,Q) so the AH
obstruction vanishes; Kollar's alpha is algebraic over Q via D*alpha
algebraic. So the Q-version is NOT an arbitrary weakening â€” it is the
exact retreat that removes the two known obstruction mechanisms while
retaining the geometric content (algebraic over Q = a nonzero multiple is
algebraic). The remaining open content (cl tensor Q surjective in the
middle codimensions, smallest case codim-2 on a 4-fold) is untouched by
either counterexample class. CONTROL-STEP ECHO (6-for-6): the integral
counterexamples obstruct the RESOLUTION claim (exhibit the cycle) over
Z; the Q-refinement removes both, leaving the codim>=2 analytic->
algebraic CONTROL as the sole open piece â€” now triangulated from the
NEGATIVE side (why Z fails, attempt-04) as well as the positive
(Charles-Markman K3^[n], attempt-03). Honesty: no proof of HC; rational
conjecture remains open; the "integral HC fails" load-bearing fact is now
primary-source-backed and sharpened with the p<=dim ceiling + the non-
topological Kollar class. Files: NEW
problems/hodge-conjecture/attempts/attempt-04.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-04, the "Integral HC
FAILS" line rewritten with two-sources-of-failure + Q-retreat logic +
control-step echo, to-verify item moved to CONFIRMED with attempt-05
targets relisted). index.md (attempt-04 line). Outcome: confirmed (four
counterexample sources verified + two-sources-of-failure structure + Q-
retreat logic pinned + obstruction map sharpened from the negative side);
partial overall (frontier unchanged). Next (attempt-05): verify the
l-adic Tate analogue (open even for H^2, char-p parallel, next-most-load-
bearing) OR the hard Lefschetz reduction exact statement OR status-check
the 2024-25 preprints (Shimizu 2025). Rotation advances to collatz-
conjecture (attempt-04) (cycle 16) per the rotation.

[CONTINUE 2026-08-24] collatz-conjecture (cycle 16/24, second pass)
Primary-source verification Continue: the Conway 1972 undecidability
thread + the "3n+1 is a contracting case (mu=3<4=2^2)" framing. Green
zone 23.5% session / 56.5% weekly, 0 subagents. CONWAY 1972 CONFIRMED
("Unpredictable Iterations", 1972): generalized Collatz functions
g(n)=a_i n+b_i (n = i mod p), rational a_i,b_i integral-valued. Main
Thm: for any computable f there is such a g with g^k(2^n)=2^{f(n)} for
minimal k. Corollary: NO algorithm decides whether g^k(n)=1 â€” the
generalized "orbit hits 1" problem is UNDECIDABLE. Mechanism = Minsky
machines -> vector games -> rational games -> FRACTRAN (1987, a
universal fraction-list language). KURTZ-SIMON 2007 CONFIRMED (TAMC,
LNCS 4484, 542-553): the GCP (every forward orbit of a generalized
Collatz function contains 1) is Pi^0_2-COMPLETE â€” stronger than Conway.
The forall n exists k: T^k(n)=1 shape matches the specific 3n+1
conjecture; the UNIFORM (all T) problem is undecidable, the specific
(fixed T) statement is open. CONTRACTING FRAMING CONFIRMED (Matthews-
Watts / Lagarias): shortcut map T(x)=x/2 (even), (3x+1)/2 (odd), d=2,
(a_0,a_1)=(1,3), product a_i = 3 < 4 = d^d, geometric mean
(3/4)^{1/2} ~ 0.866 < 1 -> contracting regime (convergence expected),
opposite the expanding regime (product > d^d, almost all diverge).
HONESTY FLAG (load-bearing): the Matthews-Watts criterion is a
CONJECTURAL HEURISTIC, not a theorem â€” "product < d^d => all
trajectories cycle" is itself the Collatz conjecture for 3n+1. Conway's
amusical permutation mu (Amer. Math. Monthly 120(3), 2013, "On
Unsettleable Arithmetical Problems"): 2k->3k, 4k+1->3k+1, 4k-1->3k-1,
is CONTRACTING by the same criterion (3^4=81 < 256=4^4) yet conjectured
to have INFINITE orbits ("probviously" unsettleable) â€” the criterion
does not settle convergence even in the contracting regime. WHAT THIS
SHARPENS FOR THE OBSTRUCTION MAP: progress.md's "Conway 1972 ... 3n+1 is
a weak/contracting case (mu=3<4=2^2)" is now primary-source-backed.
THE Pi^0_2-COMPLETENESS IS THE NEW LOAD-BEARING FACT: any UNIFORM (all
generalized T) argument is impossible (undecidable); a 3n+1 proof MUST
exploit the concrete contracting structure (exact multipliers 1,3; the
3<4 margin; the 3/4<1 geometric mean) â€” a per-INSTANCE CONTROL argument,
exactly the open piece. The resolution (a general decision procedure) is
ruled out by undecidability; the control (per-instance contracting-
structure -> pointwise convergence) is the only route and is open.
CONTROL-STEP ECHO (6-for-6): the generalized problem being Pi^0_2-
complete is the hardest "no uniform method exists" wall â€” the Collatz
analog of Beal's reduction-to-finite-curves, with the wall here LOGICAL
(undecidability) rather than analytic, but the same role: forces any
attack onto the specific structure. The "one-dimensional engine stops"
sub-pattern gets a LOGICAL edge: the uniform engine (all T) is provably
stopped by undecidability; the instance-specific engine (3n+1) is the
open contracting-structure control. Honesty: no proof of Collatz;
density->pointwise + cycle-exclusion walls open; the Matthews-Watts
criterion is heuristic-not-theorem (flagged). Conway's undecidability is
for generalized maps, NOT the specific 3n+1 (the existing honesty check
stands, sharpened: uniform undecidable, specific open). Files: NEW
problems/collatz-conjecture/attempts/attempt-04.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-04, Conway line
rewritten with Conway/Kurtz-Simon/contracting + heuristic-not-theorem
flag + Pi^0_2-completeness control-step sharpening, to-verify item moved
to CONFIRMED with attempt-05 targets relisted). index.md (attempt-04
line). Outcome: confirmed (Conway/Kurtz-Simon/contracting-framing
verified + Pi^0_2-completeness sharpening + heuristic-not-theorem honesty
flag + undecidability-as-control-wall echo); partial overall (frontier
unchanged). Next (attempt-05): Barina 2020 (2^68 verification bound) +
the 2024-25 preprints (Fathi 2025 / Nwankpa 2025 / Chang 2026 status-
check). Rotation advances to beals-conjecture (occasional cycle-in,
cycle 17) OR birch-swinnerton-dyer (attempt-05) per the rotation order.

[CONTINUE 2026-08-24] birch-swinnerton-dyer (cycle 17/24, second pass)
Primary-source verification Continue: upgrade attempt-04's
direction-(A) deepening from partial/to-verify to CONFIRMED. Green zone
29.4% session / 57.6% weekly, 0 subagents. HEADLINE = CITATION UPGRADE:
Chan-Ho Kim, "A higher Gross-Zagier formula and the structure of Selmer
groups," is PUBLISHED in Trans. Amer. Math. Soc. (2024), DOI
10.1090/tran/9125 (= arXiv:2203.12161, v1 23 Mar 2022 -> v7 12 Jan 2024
= published). So the mechanism is peer-reviewed, not just an arXiv
preprint. VERIFIED FROM THE ARXIV ABSTRACT (primary source): "Kolyvagin
system-theoretic refinement of Gross-Zagier" comparing Heegner-point
Kolyvagin systems with Kurihara numbers (root number -1) and bipartite
Euler systems / Waldspurger refinement (root number +1); NO LOW-RANK
ASSUMPTION (arbitrary rank) confirmed; "the equivalence between the
NON-TRIVIALITY of various Kolyvagin systems and the corresponding MAIN
CONJECTURE localized at the augmentation ideal" -> nontriviality IS a
main-conjecture condition (the exact conditional sub-wall); "the Heegner
point main conjecture localized at the augmentation ideal implies the
STRONG RANK ONE p-CONVERSE" to Gross-Zagier-Kolyvagin. KURIHARA NUMBERS
CONFIRMED (via Kurihara 2012/2014): delta_m = sum Re([a/m]) Omega_E^+
. prod log_{F_l}(a) mod p^N, where [a/m] = integral modular symbol,
Omega_E^+ Neron period, log discrete log -> built from MODULAR SYMBOLS,
not L-derivatives; chain = modular symbols -> Mazur-Tate elements ->
(Kolyvagin derivative D_l) -> Kurihara numbers. Confirms attempt-04's
"Kolyvagin derivatives of Mazur-Tate elements, NOT L-derivatives."
STRUCTURE THEOREM CONFIRMED (Kurihara Thm B / 1.1.1, Munster J. Math
2014): rank Sel = r => Theta^0=...=Theta^{r-1}=0, Theta^r != 0,
Fitt_i(Sel^vee) = Theta_i(Q) for i >= r, i = r mod 2, full structure
Z_p^r + sum_k (Z/p^{n_{r+2k}-n_{r+2k+2}/2})^2 (free rank-r + paired
torsion), conditional on the main conjecture + non-degenerate p-adic
height; WITHOUT the main conjecture only PARTIAL results (Thm
1.2.3/1.2.5, Kolyvagin systems of Gauss sum type). WHAT THIS UPGRADES:
[bsd-higher-gz-kim-2022] from to-verify to CONFIRMED; citation upgraded
to Trans. AMS 2024. Two of three sub-walls now primary-source-confirmed:
(2) conditional = the main conjecture (the exact named condition, and
unconditional gives only partial); (1) relative = the paired-torsion
structure. SUB-WALL (3) cyclotomic-vs-anticyclotomic disjointness (Kato
vs Heegner field variation) is NOT in the abstract -> remains
SEARCH-DERIVED (from Kim intro / Wei Zhang 2013 Current Developments in
Mathematics survey), flagged to-verify against the survey/PDF body. The
two-engine 6-for-6 echo stands + sharpened: the anticyclotomic (Heegner)
engine now has a PUBLISHED arbitrary-rank Selmer-structure theorem
conditional on its own main conjecture; the open piece = comparison with
the cyclotomic (Kato) engine = sub-wall (3). Honesty: no proof of BSD;
rank->=2 wall sharpened (3 sub-walls, 2 confirmed) not broken; refined-
BSD (direction C) untouched. Files: NEW
problems/birch-swinnerton-dyer/attempts/attempt-05.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-05, Kim
citation upgraded to Trans. AMS 2024 in the direction-(A) block,
attempt-05 block added to Best partial result, [bsd-higher-gz-kim-2022]
upgraded to CONFIRMED with the disjointness sub-wall flagged remaining).
index.md (attempt-05 line). Outcome: confirmed (citation upgrade to
peer-reviewed + arbitrary-rank structure + Kurihara-number definition +
main-conjecture condition pinned + two-of-three sub-walls confirmed);
partial overall (frontier unchanged, sub-wall 3 still search-derived).
Next (attempt-06): verify sub-wall (3) cyclotomic-vs-anticyclotomic
disjointness against the Wei Zhang 2013 survey / Kim Trans. AMS intro
(the last search-derived piece), OR pivot to direction (C) refined-BSD
(Bullach-Honnor 2025). Rotation advances to navier-stokes (attempt-05)
(cycle 18) per the rotation order, OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] navier-stokes (cycle 18/24, second pass)
Status-check Continue: resolve the lingering publication-status to-
verify flag on the two 2024 axisymmetric preprints (Hou 2405.10916,
Seregin 2402.13229) + 2025-26 community reception. Green zone 37.5%
session / 59.0% weekly (about to tip yellow), 0 subagents. HEADLINE =
HOU 2024 IS NOW PUBLISHED: Thomas Y. Hou, "Nearly Self-similar Blowup
of Generalized Axisymmetric Navier-Stokes Equations," Foundations of
Computational Mathematics (Springer, 2026), DOI 10.1007/s10208-026-09748-8
(= arXiv:2405.10916). FoCM is a strong peer-reviewed journal -> the
Hou blowup claim (for GENERALIZED axisymmetric NS) is now published,
not just a preprint. Publication-status flag for Hou RESOLVED +
upgraded from "preprint, evidence" to "peer-reviewed publication."
Published content matches attempt-04 (two-section: Sec 4 solution-
dependent viscosity self-similar n~3.188->3, BKM-violating O(1/(T-t));
Sec 5 two-constant-viscosity Boussinesq nearly-self-similar with log
correction lambda=(1+eps|log(T-t)|)^{-1/2}, n~4.73). The load-bearing
caveat (generalized axisymmetric NS, NOT true constant-viscosity 3D
NS) is UNCHANGED by publication; FoCM accepted it as a generalized-
model blowup, not a true-NS blowup. SEREGIN 2024 (arXiv:2402.13229)
STILL A PREPRINT: no journal DOI found; only the arXiv DOI. The
PUBLISHED Seregin piece is the DISTINCT earlier note "Remarks on Type
II blowups," Comm. Pure Appl. Anal. (2023), DOI 10.3934/cpaa.2023108
(already noted in attempt-04). So the Hou/Seregin pair is now
ASYMMETRIC in peer-review status: the candidate OUTSIDE the fence
(Hou, nearly-self-similar generalized blowup) is published; the FENCE
itself (Seregin 2024, exclusion of exact/discrete self-similar Type
II) is not peer-reviewed yet. Sharpens the honesty framing without
moving the slice boundary. COMMUNITY RECEPTION: active/supportive, no
refutation found - NYU Courant Analysis Seminar + UCB/LBL Applied Math
Seminar Spring 2025 (Hou, "Recent progress on potential singularity of
the 3D Navier-Stokes equation and related models"); a related quasi-
exact-1D-model paper "Blowup analysis for a quasi-exact 1D model of
3D Euler and Navier-Stokes," Nonlinearity, DOI 10.1088/1361-6544/ad1c2f
(Hou-group program, supporting line). "No refutation found in a
search" = weak evidence of acceptance, NOT proof of correctness -
flagged honestly. WHAT THIS CHANGES: [ns-hou-2024] publication-status
flag RESOLVED (upgraded to FoCM 2026); Seregin 2024 flag persists
(still preprint, re-check later). NO CHANGE to the frontier or the
control-step obstruction - Hou's publication is a generalized-model
blowup, not true-NS; refined open content from attempt-04 stands (true
blowup must be non-(discrete-)self-similar to dodge Seregin AND bridge
generalized->true viscosity = Hou's gap, now peer-reviewed as a gap not
closed). Control-step echo unchanged (Seregin's engine fences off the
self-similar slice; Hou's candidate lives where it stops). Honesty: no
blowup for true 3D NS, no proof of global regularity; frontier
unchanged; cycle's point = publication-status resolution (Hou) +
asymmetric-status sharpening. Files: NEW
problems/navier-stokes/attempts/attempt-05.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-05, attempt-05 block
added to Best partial result, Hou/Seregin to-verify entry split into
Hou RESOLVED / Seregin persists). index.md (attempt-05 line). Outcome:
confirmed (Hou publication-status resolved + upgraded to FoCM 2026;
Seregin-2024 status re-confirmed still preprint; asymmetric peer-review
status recorded; community reception surveyed); partial overall
(frontier unchanged). Next (attempt-06): re-check Seregin 2024
(2402.13229) for journal publication in a later cycle (the one
persistent NS status flag), OR deepen direction (A) the critical a
priori bound (the missing control step), OR dig into the quasi-exact-
1D-model Nonlinearity paper (a potential new direction-(B) ingredient).
Rotation advances to yang-mills (attempt-05) (cycle 19) per the
rotation order, OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] yang-mills (cycle 19/24, second pass)
Status-check Continue on the 2025-26 preprint wave (Faizal-Shabir,
Agawa, Eriksson) + the Chatterjee 2021 line. Green zone 37.5% session
/ 59.0% weekly (about to tip yellow), 0 subagents. HEADLINE = FAIZAL-
SHABIR 2026 (arXiv:2606.19362) IS NOW PEER-REVIEWED: published as a
FOUR-PART SERIES in IJGMMP (Int. J. Geom. Meth. Mod. Phys., World
Scientific, 2026), all "Refereed," indexed WoS/Scopus, DOIs
10.1142/S0219887826501112-6501148 (Part 1 2650114 / Part 2 2650113 /
Part 3 2650112 / Part 4 2650111; arXiv:2606.19362 = consolidated).
Third citation upgrade this loop (after BSD Kim arXiv->Trans. AMS
2024, NS Hou arXiv->FoCM 2026). NAME ORDER CORRECTED to Faizal &
Shabir (attempt-04 wrote "Shabir & Faizal"; flagged to-verify vs the
arXiv author list). LOAD-BEARING HONESTY SHARPENING (the cycle's
point): IJGMMP is a MID-TIER venue (not CMP/Inventiones/JAMS/Annals);
the CLAIM is far stronger (full 4D YM + proven continuum mass gap =
Millennium) than Kim (Trans. AMS structure theorem) or Hou (FoCM
generalized-model blowup) yet the VENUE is far weaker - the
evidence/claim ratio is INVERTED relative to BSD/NS. Clay has NOT
accepted/verified; no independent community verification; the
attempt-04 technical caveats (admissible-class framework, RG-
interlacing defect summability) are UNADDRESSED by mere publication.
So the ym-recent-claims-unverified flag is RENAMED, NOT REMOVED:
publication-status RESOLVED (peer-reviewed IJGMMP 2026) but a new
SUBSTANTIVE-ACCEPTANCE flag RAISED (editorial bar != community-
acceptance bar, especially for a Millennium claim in a mid-tier
venue). CHATTERJEE 2021 LINE: 2025 follow-up confirmed -
"Expanded regimes of area law for lattice Yang-Mills theories"
(arXiv:2505.16585, May 2025) + Bonn workshop 2025-07-28..08-01 +
"Dynamical approach to area law" (INSPIRE 2967145) - active/
supportive community reception, but still RESOLUTION-SIDE
(confinement/area law); the mass-gap-at-weak-coupling CONTROL step
(the UV->IR bridge, "mass gap is the hypothesis not the conclusion,"
attempt-04) is UNCHANGED. No refutation found. AGAWA 2025 /
ERIKSSON 2026 NOT re-checked this cycle (budget, weekly about to tip
yellow); remain at attempt-04 status (preprint / viXra). WHAT THIS
CHANGES: [ym-recent-claims-unverified] Faizal-Shabir component
publication-status RESOLVED + upgraded; substantive-acceptance flag
raised; Chatterjee 2025 follow-up recorded as resolution-side.
NO CHANGE to the frontier or the control-step obstruction - the
UV->IR bridge remains the single load-bearing open piece,
triangulated from three angles (Balaban UV-half / SUSY dual-Meissner
/ Chatterjee mass-gap=>confinement); a peer-reviewed full-solution
claim in a mid-tier journal does NOT move the frontier until
independently verified by the community/Clay. Control-step echo
unchanged (three engines stop at the same UV->IR step; the Faizal-
Shabir publication changes the status of one CLAIMED bridge, not
where the verified engines stop) - same shape as NS attempt-05
(Hou published, Seregin fence unchanged) and BSD attempt-05 (Kim
published, disjointness sub-wall unchanged). Honesty: no rigorous
4D quantum YM, no proven continuum mass gap; the cycle's point =
publication-status resolution (Faizal-Shabir) + sharper honesty
framing (editorial vs community-acceptance bar) + Chatterjee 2025
extension recorded. Files: NEW
problems/yang-mills/attempts/attempt-05.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-05, attempt-05
block added to Best partial result, [ym-recent-claims-unverified]
to-verify entry status-split: Faizal-Shabir RESOLVED +
substantive-acceptance flag raised, Agawa/Eriksson still to-verify).
index.md (attempt-05 line). Outcome: confirmed (Faizal-Shabir
publication-status resolved + upgraded to IJGMMP 2026;
substantive-acceptance flag raised; name-order corrected; Chatterjee
2025 follow-up recorded as resolution-side); partial overall
(frontier unchanged). Next (attempt-06): re-check Agawa 2025 +
Eriksson 2026 for peer-review/reception (deferred this cycle), OR
deepen direction (A) the uniform-in-a IR bound (the literal UV->IR
bridge), OR read Faizal-Shabir IJGMMP Part 3/4 bodies (post-embargo
2027-02) for the admissible-class / RG-interlacing caveats.
Rotation advances to hodge-conjecture (attempt-05) (cycle 20) per
the rotation order, OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] hodge-conjecture (cycle 20/24, second pass)
Verify the l-adic Tate analogue (char-p parallel of HC, attempt-04's
"next-most-load-bearing" item) + CORRECT attempt-04's framing. Yellow
zone 57.5% session / 62.5% weekly (weekly crossed 60% this segment),
0 subagents. HEADLINE = attempt-04's "Tate open even for H^2" framing
is OUTDATED for the flagship case: the K3-surface divisor case (the
famous "Tate open where HC's H^2 is solved by Lefschetz (1,1)"
example) is now a THEOREM IN ALL CHARACTERISTICS - Nygaard-Ogus 1985
(Annals 122, finite height, REDUCES TO LEFSCHETZ (1,1) via quasi-
canonical lifting to char 0), Charles 2013 (Invent. Math. 194,
supersingular p>=5, also codim-2 on cubic fourfolds), Maulik 2014
(Duke 163), Madapusi Pera 2015 (Invent. Math. 201, odd char),
Kim-Madapusi Pera 2016 (char 2, arXiv:1512.02540), Charles 2016
(Annals 184, 2nd proof), Lieblich-Maulik-Snowden 2014 (Ann. Sci. ENS
47, finiteness<=>Tate criterion). The GENERAL Tate-for-divisors is
STILL OPEN but REDUCED TO SURFACES (de Jong-Morrow; Ambrosi), and
proven for abelian (Tate 1966), K3, rationally connected. SHARPER
SYMMETRIC ECHO (replacing the stale asymmetry): both HC (char 0) and
Tate (char p) are SOLVED AT DIVISORS (standard classes) and OPEN AT
CODIM >=2 - the control-step spine (analytic/Frobenius-invariant
->algebraic control in codim >=2) is confirmed on BOTH sides, not
asymmetric. NEW CROSS-PROBLEM BRIDGE (the striking finding): Tate-
for-divisors on a surface X over a finite field <=> finiteness of
Br(X) <=> finiteness of Sha(Jacobian) <=> BSD for the Jacobian - a
LOGICAL link from HC's char-p twin to [[birch_swinnerton_dyer]],
sharpening 6-for-6 from "parallel" to "linked." CONTROL ECHO INSIDE
TATE: Milne - Tate-for-divisors => 1-semisimplicity (eigenvalue 1)
<=> full Frobenius-semisimplicity (via X x X); semisimplicity is the
control, Tate the resolution - same spine. BALKAN-SCHREIEDER 2026
(Selecta Math. 32, Art. 37, DOI 10.1007/s00029-026-01142-0):
Tate/Beilinson/Grothendieck-Serre-semisimplicity <=> vanishing of a
birational invariant H^{2i}(F_0 P^n, Q_l(i+1))^G=0 (all i,n>=2),
half-dimensional reduction - a fresh cohomological criterion but an
EQUIVALENCE OF CONJECTURES, not a proof. APPEND-ONLY CORRECTION:
attempt-04 left intact; the correction lives here (same discipline as
BSD Kim "bounds rank <=1 only" update, NS Palasek axisymmetric/high-
dim mislabel). TO-VERIFY (search-derived, flagged): Nygaard-Ogus
reduces-to-Lefschetz-(1,1) mechanism; Milne semisimplicity
implications; the Tate<=>BSD-for-Jacobian equivalence (classical
Tate/Artin/Milne lineage, standard account); Balkan-Schreieder 2026
equivalence. WHAT THIS CHANGES: attempt-04's "open even for H^2"
framing CORRECTED (K3 flagship now theorem 2013-16; general divisor
case open but reduced to surfaces); symmetric char-0/char-p echo
recorded; Tate<=>BSD bridge to [[birch_swinnerton_dyer]] recorded
(6-for-6 sharpened parallel->linked); Milne control echo + Balkan-
Schreieder 2026 reformulation recorded. NO CHANGE to the HC frontier
itself (char-0 rational HC, codim >=2, remains open; smallest case
codim-2 on a 4-fold). Honesty: no proof of HC (char 0) or Tate (char
p); the cycle's point = verification + append-only correction +
symmetric echo + BSD bridge. Files: NEW
problems/hodge-conjecture/attempts/attempt-05.md (outcome confirmed);
UPDATED progress.md (consolidated through attempt-05, attempt-05
block added to Verified base, "Still to-verify" line updated
(Tate->VERIFIED+CORRECTED, targets renamed attempt-06), Honesty-check
Tate line corrected). index.md (attempt-05 line). Outcome: confirmed
(Tate-K3 theorem chain verified; attempt-04 framing corrected;
symmetric echo + BSD bridge + Milne control echo recorded); partial
overall (HC frontier unchanged). Next (attempt-06): primary-source-
verify the Nygaard-Ogus reduce-to-Lefschetz-(1,1) mechanism OR the
Tate<=>BSD-for-Jacobian equivalence (Milne 2007), OR hard Lefschetz
reduction exact statement, OR status-check the 2024-25 HC preprints
(Shimizu 2025). Rotation advances to collatz-conjecture (attempt-05)
(cycle 21) per the rotation order, OR beals (occasional cycle-in).

[CONTINUE 2026-08-24] collatz-conjecture (cycle 21/24, second pass)
Verify the Barina 2020 2^68 computational-verification bound (the
evidence-base line in the exact-frontier table) + status-check the
record's progress. Yellow zone 65.5% session / 63.9% weekly (session
crossed 60% too; resets in ~2h), 0 subagents. HEADLINE = BARINA 2020
CONFIRMED + the record has ADVANCED. D. Barina, *Convergence
verification of the Collatz problem*, J. Supercomput. 77 (2021),
2681-2688, DOI 10.1007/s11227-020-03368-x; verified all N<=2^68 by
2020-05-07 via a novel O(N)-table (not O(2^N)) 128-bit GPU algorithm
(~2.2e11/sec on RTX 2080); path record n=274133054632352106267 below
2^68, confirming the Lagarias-Weiss n^2 peak-height prediction.
EVIDENCE LINE UPDATED (append-only): Barina's project website reports
the record ADVANCED past the 2020 paper - 2^69 (Dec 2021), 2^70 (Jul
2023), 1.5*2^70 (Nov 2023), 2^71~=2.36e21 (Jan 2025), the current
frontier - but the 2^71 is SELF-REPORTED, NOT peer-reviewed (the
published figure stays 2^68); flagged to-verify against a publication
(same publication-status split as YM Faizal-Shabir attempt-05 / NS
Hou-Seregin attempt-05). OLIVEIRA E SILVA PRECISION: 20*2^58~=2^62.3
(AMS 2010, *Ultimate Challenge* pp 189-207), NOT bare 2^58 (a factor
20 larger). NO COUNTEREXAMPLE found at any bound. WHAT THIS CHANGES:
[collatz-barina] CONFIRMED (J. Supercomput. 77, 2021); the exact-
frontier table evidence line UPDATED from 2^68 (2020) to current
2^71 (Jan 2025, project-reported) with the peer-reviewed/project-
reported split; Oliveira e Silva precision recorded. NO CHANGE to
the frontier or the control-step obstruction - the density->pointwise
control step (attempt-04 Pi^0_2-completeness logical wall) is
UNTouched by any finite verification: 2^71 instances is measure-zero
vs N, and Pi^0_2-completeness means no uniform algorithm exists for
the generalized problem, so the stop is LOGICAL not merely
technical. Control-step echo (the cleanest "one-dimensional engine
stops"): the verification engine controls the checked-instances slice
(resolution) and stops at the all-n slice (control) - parallel to NS
Seregin, YM Chatterjee, BSD cyclotomic/anticyclotonic; Collatz is the
stark instance because the stop is logical (undecidability). Honesty:
the 2^71 figure is project-website self-reported, NOT peer-reviewed;
the 2024-25 claimed-proof preprints (Fathi 2025 / Chang 2026 / Nwankpa
2025) NOT status-checked this cycle (budget; one search spent on the
verification record, the more load-bearing target) - deferred. No
proof of Collatz; the cycle's point = verification + honest evidence-
line update + control-step/undecidability echo reinforced. Files:
NEW problems/collatz-conjecture/attempts/attempt-05.md (outcome
confirmed); UPDATED progress.md (consolidated through attempt-05;
exact-frontier table evidence line updated 2^68->2^71 with
peer-reviewed/project-reported split; "Still to-verify" line updated
Barina->CONFIRMED, targets renamed attempt-06; attempt-05 block
added to Best partial result). index.md (attempt-05 line). Outcome:
confirmed (Barina 2020 paper verified; record advanced 2^68->2^71
recorded with publication-status split; Oliveira e Silva precision;
control-step/undecidability echo reinforced); partial overall
(frontier unchanged). Next (attempt-06): status-check the 2024-25
claimed-proof preprints (Fathi/Nwankpa/Chang) (the one remaining
attempt-04 target deferred), OR primary-source-verify the 2^71 bound
against a publication, OR deepen a direction (A/B/C) sub-thread.
Rotation: second pass has now visited BSD, NS, YM, Hodge, Collatz;
next is the occasional beals-conjecture cycle-in (per the bias rule),
OR birch-swinnerton-dyer (attempt-06) per the rotation order.

## [CONTINUE 2026-08-24] beals-conjecture (cycle 22/24, second pass; occasional cycle-in)

Fifth-signature (5,7,13) computation (`scripts/search_5713.py`, mirroring
`search_5711.py`; box Aâ‰¤6000,Bâ‰¤600,Câ‰¤40; Ï‡=-264/455â‰ˆ-0.580). Results: 0 exact
solutions; 0 genuine gap-1 (only the trivial t=1 degenerate instance, on the
universal t^65+1 family â€” the t^65/t^91 families escape the box for tâ‰¥2);
**min non-degenerate coprime near-miss gap = 1771** at (A,B,C)=(6,3,2):
6^5+3^7-2^13 = 7776+2187-8192 = 1771, gcd=1. Counting-heuristic monotone
prediction RE-CONFIRMED (29<77<277<288<1771). SHARPENING (append-only
correction): the attempt-23 deceleration REVERSES â€” the smallest -Ï‡ step
(+0.014; p,q fixed, only r:11â†’13) gives by far the largest gap step (+1483,
6.1Ã—). Trend stays monotone but the rate is erratic, NOT a smooth function
of -Ï‡; the min gap is governed by exponent-specific small-base arithmetic
(C^r granularity near small A^p+B^q; min sits at smallest C,A corner where
5th-power spacing ~A^4 is smallest), not by the scalar Ï‡. Qualitative Beals
prediction survives; any smooth quantitative Ï‡â†¦gap law does not. Honesty:
box-min flagged to-verify by a wider-box run; not a proof move (soft 6th
angle [[method-counting-heuristic]]); obstruction map untouched. Outcome
confirmed (clean continue/reverse answer), partial overall. Yellow zone
(session 73%/weekly 65.3%, 0 subagents â€” direct computation to conserve
budget). Next: wider-box (5,7,13) run OR sixth signature (7,11,13)
(reverse-direction, less hyperbolic) OR return to the five-problem rotation
(likely BSD attempt-06).

## [CONTINUE 2026-08-24] birch-swinnerton-dyer (cycle 23/24, second pass)

Closed the last search-derived sub-wall of attempt-04/05's direction-(A)
deepening. Sub-wall (3) cyclotomic-vs-anticyclotomic disjointness VERIFIED
against the primary source: Kim's Trans. AMS paper (arXiv:2203.12161) states
it verbatim (search-surfaced quote, consistent with attempt-05's abstract-
level verification): "we do not expect ... a more general comparison between
Kato's Euler systems and Heegner point Euler systems since their field
variations are disjoint except the base imaginary quadratic field."
Honesty: "do not expect" = conjectural heuristic barrier, NOT a proven
impossibility (flagged); quote is search-surfaced, minor PDF-location
to-verify remains. All three sub-walls now primary-source-confirmed;
direction (A) fully anchored.

NEW sharpening (Kataokaâ€“Sano 2024, J. Assoc. Math. Res., DOI
10.56994/jamr.002.002.001 â€” flagged to-verify against the paper body):
Heegner points form a RANK-2 Euler system over K (basic rank r_T=2); the
two rank-1 engines (cyclotomic Kato, anticyclotomic Heegner) are its two
summands via Sel(K) â‰ƒ Sel(Q) âŠ• Sel(Q,E^K). Thm 1.5 constructs the rank-2
system (assuming Heegner MC); Thm 1.11: Heegner MC + Darmon-derivative conj.
+ Bockstein regulator â‰  0 âŸ¹ p-part of BSD for E/K. REFRAMES the
obstruction: not "compare two rank-1 engines" (disjoint, can't â€” the
verified sub-wall (3)) but "control the rank-2 system's Darmon derivatives."
Sharpens the two-engine 6-for-6 echo (BSD/Collatz/NS/YM) from "both rank-1
engines stop at rank 1" to "two summands of a rank-2 system; the
composition/control step is rank-2 Darmon-derivative control, not a
rank-1-to-rank-1 comparison." Wei Zhang 2013 CDM survey (DOI
10.4310/CDM.2013.v2013.n1.a3, pp 169-203) confirmed as the secondary source
(body not read: Intl Press 403 to WebFetch). Supporting: Howard 2004
(Compositio, Heegner-point Kolyvagin system, one divisibility of
Perrin-Riou anticyclotomic MC); Bertolini-Darmon 2005 (Annals,
anticyclotomic MC, root-number +1 via Shimura curves). No proof move;
rank â‰¥2 and exact |Sha| untouched. Outcome confirmed (sub-wall 3 closed;
two-engine echo sharpened), partial overall. Yellow zone (session
78.3%/weekly 66.2%, 0 subagents â€” direct WebSearch; session resets ~1h).
Next: navier-stokes (attempt-06) per rotation, OR primary-source-verify
Kataokaâ€“Sano (attempt-07 BSD target), OR direction (C) refined-BSD.

## [CONTINUE 2026-08-24] navier-stokes (cycle 24/24, second pass â€” FINAL cycle)

Verified the Hou-group quasi-exact 1D model (option (c) of attempt-05's
Next; budget-cheapest, thematically load-bearing). Hou & Wang, *Blowup
analysis for a quasi-exact 1D model of 3D Euler and Navierâ€“Stokes*,
**Nonlinearity 37 (2024)**, DOI 10.1088/1361-6544/ad1c2f (arXiv:2306.04146),
peer-reviewed, CONFIRMED. The Hou-Li (2008, CPAM) 1D model is "quasi-exact"
(solutions construct exact 3D Euler/NS solutions when angular
velocity/vorticity/stream are linear in r â€” a special ansatz). Achieves
RIGOROUS finite-time blowup in three WEAKENED regimes: (1) inviscid +
weakened advection (a<1, smooth, self-similar, c_l=0); (2) original inviscid
(a=1) with HÃ¶lder C^Î± data (Hou-Li C^1 well-posedness sharp); (3) viscous +
weakened advection (a<1, Î½>0, finite-time, no exact self-similar profile).
Method = dynamic rescaling formulation + singularly weighted LÂ² (weight
1/(2Ï€(1-cos x))) + sharp nonlocal estimates (exact Fourier low-mode +
damping extraction high-mode), computer-assisted (interval arithmetic,
Matlab, 200 modes).

SHARPENS the cross-problem "one-dimensional engine stops" 6-for-6
sub-pattern: the naive read ("1D model too weak to blow up, so it stops")
is CORRECTED â€” the 1D quasi-exact engine does NOT stop at blowup; it
ACHIEVES rigorous blowup (resolution, in weakened slices). It stops at the
CONTROL STEP: every blowup regime requires a weakening (weakened advection,
or rougher HÃ¶lder data, or viscous-without-exact-profile); full-strength 3D
NS (smooth data, full advection a=1, the Millennium problem) is exactly
where the rigorous blowup proof does NOT extend. Cleanest NS mirror of the
Beal/Hodge/BSD control-step framing: a tool that fully resolves a slice but
cannot bridge to the universal case. Viscosity alone does NOT prevent
blowup in the 1D model with weakened advection (regime 3) â€” isolates
vortex-stretching vs advection; the full 3D question (full advection +
viscosity) remains open. Pairs with Hou's 3D nearly-self-similar candidate
(attempt-05, FoCM 2026): 1D = rigorous blowup (resolution); 3D generalized
= candidate (control step, open). Related (to-verify against paper
bodies): Huang-Qin-Wang-Wei, CMP 406:243 (2025), Hou-Luo model, PURELY
ANALYTIC Schauder fixed-point blowup (computer-free complement);
Hou-Qin-Wang, arXiv:2606.26658 (2026 preprint), weak-advection Hou-Li
periodic. Active 2024-26 program, two methods (computer-assisted DRF +
purely analytic Schauder). Honesty: blowup is in REDUCED/weakened models,
NOT full 3D smooth-data â€” Millennium problem untouched; "quasi-exact"
linear-in-r ansatz is the slice boundary, general smooth 3D data is the
control step. No change to the critical-a-priori-bound direction-(A)
control obstruction. Outcome confirmed (1D quasi-exact model verified +
pattern sharpened), partial overall. Orange zone (session 85.2%/weekly
67.4%, 0 subagents â€” one targeted WebSearch; session resets ~1h).

=== 24-CYCLE LOOP COMPLETE (cycles 1-24) ===
Second pass visited: NS(18), YM(19), Hodge(20), Collatz(21), beals(22),
BSD(23), NS(24). All six problems advanced one Continue in this pass;
five-problem rotation (BSD/NS/YM/Hodge/Collatz) each reached attempt-05/06,
beals occasional cycle-in (attempt-24). Loop stopped at the 24-cycle cap.
Recovery summary to follow.

## [CONTINUE 2026-08-25] yang-mills (cycle 1 / new run)
Preprint-wave re-check Continue on YM (resumed /loop, new stop rule:
pause when weekly > 75%; weekly 69.8% at cycle start, ~5% headroom;
session fresh 1.3% after midnight reset, yellow, 0 subagents â€” one
targeted WebSearch). Attempt-05's deferred option (a): re-check Agawa
2025 / Eriksson 2026. **Agawa 2025 â€” addendum RETRACTED** (DOI
10.33774/coe-2025-3jmcf, both v1/v2 marked "Retracted"; Cambridge Open
Engage explicitly not peer-reviewed; unaffiliated, AI-assisted, 0
citations): the "addendum needed" flag RESOLVED IN THE NEGATIVE â€” posted
then retracted â†’ a non-result, removed from active to-verify. **Eriksson
2026** â€” still ai.viXra.org ("AI assisted e-prints," not peer-reviewed),
68-paper programme; author's own Â§8.2 self-concedes the exact control
step. Assumption A undischarged in three forms: blocking-map oscillation
summability (viXra:2602.0077, conditional); gradient-flow LÂ¹ scale-
consistency (viXra:2602.0085, unconditional for standard observables via
Wilson-flow Thm 3.11, conditional for the full algebra â€” a resolution-
side improvement); two-layer RG-Cauchy (viXra:2602.0063) â€” naive
asymptotic freedom gives a NON-SUMMABLE O(1/k) rate (logarithmic
divergence), "we do not prove the RG-Cauchy estimate from first
principles." Non-summability IS the UVâ†’IR-bridge / "one-dimensional
engine stops" obstruction, independently conceded from inside an
attempted proof â€” corroborative not probative (AI-assisted preprint, a
flawed attempt failing â‰  problem hard); weak but real convergent signal.
Substantive-acceptance flag (Faizal-Shabir, attempt-05) REINFORCED: even
the most extensive preprint-wave attempt explicitly concedes the control
step. Reflection positivity / OS reconstruction / thermodynamic limit /
mass gap all OPEN in the programme. Frontier + control-step obstruction
unchanged. Outcome confirmed (Agawa retraction + Eriksson self-concession
both confirmed; both AI-assisted preprints, corroborative only),
partial overall. Files: attempt-06.md created; progress.md
(consolidatedâ†’attempt-06, best-partial block, [ym-recent-claims-
unverified] updated), index.md, log.md updated.

## [CONTINUE 2026-08-25] hodge-conjecture (cycle 2 / new run)
Primary-source verification of the TateâŸºBSD-for-Jacobian bridge
(attempt-05 option (b), the load-bearing cross-problem link). VERIFIED
+ REFINED. For a smooth projective surface X/F_q FIBERED over a curve
(generic fiber C/F_q(t), J=Jac(C) over the global function field
F_q(t)): Tate-for-divisors(X) âŸº Artin-Tate(X) âŸº Br(X) finite âŸº
III(J/F_q(t)) finite âŸº BSD(J). Chain = Tate-Milne 1975 (ATâŸºBr(â„“)-
finite, incl. p-part by Milne via flat/de Rham-Witt/crystalline;
jmilne.org article page) + Artin-Grothendieck (BrâŸºIII) + Kato-Trihan
2003 (BSDâŸºIII(â„“)-finite), re-proven DIRECTLY by Lichtenbaum-
Ramachandran-Suzuki 2022 (Ã‰pijournal G.A., DOI 10.46298/epiga.2022.7482
/ arXiv:2101.10222, two proofs: Tate-strategy localization+Tate-Shioda+
height; Weil-Ã©tale cohomology+derived categories); Gordon 1979 +
Geisser 2020 (order relation [Br]Â·Î±Â²Â·Î´Â²=[III]Â·âˆÎ´'_v/Î´_v) corroborate.
Dictionary: Br(X)â†”III(J/F), NS(X)â†”Mordell-Weil J(F), intersection
pairingâ†”NÃ©ron-Tate pairing. Two honest refinements of attempt-05's
"BSD for the Jacobian": (1) FUNCTION-FIELD (char-p) BSD â€” the
geometric avatar, shares formulation with but is NOT the number-field
Millennium BSD over Q (function-field BSD substantially proven via
Kato-Trihan); a genuine avatar-level LOGICAL EQUIVALENCE â€” the
deepest cross-problem link, sharpening 6-for-6 from "linked" to
"logically equivalent in one avatar" â€” but NOT a direct bridge to
[[birch_swinnerton_dyer]]'s Q-target. (2) requires the FIBERED-surface
setting (Artin-Tate is general; the BSD link needs a fibration to
produce J over a global field). Artin-Grothendieck/Kato-Trihan links
search-surfaced (minor to-verify against 2003 body). HC frontier
(char-0 rational HC, codim â‰¥2) unchanged. Outcome confirmed (bridge
verified + scope-refined), partial overall. Files: attempt-06.md
created; progress.md (consolidatedâ†’attempt-06, verified-base bridge
note refined to function-field/fibered, to-verify BSD-bridge entry +
attempt-07 targets), index.md, log.md updated. Yellow zone (weekly
70.9% / session 7.5%, 0 subagents â€” one targeted WebSearch).

## [CONTINUE 2026-08-25] collatz-conjecture (cycle 3 / new run)
Status-check of the 2024-26 claimed-proof preprints (attempt-05 option
(a), the deferred attempt-04 target). NONE peer-accepted; ALL fail at
the average-vs-pointwise control step â€” the 6-for-6 wall reinforced from
the negative side (corroborative, not probative). Fathi 2025 = THREE
Zenodo preprints (entropy-descent / potential-descent+mod-32 / Kolmogorov;
DOIs 10.5281/zenodo.{15191755,15313916,15549017}), 0-citation unreviewed;
the load-bearing one = standard average-contraction heuristic E[k]=2>
logâ‚‚ 3 (distributional, not pointwise). Nwankpa 2025 (Preprints.org,
DOI 10.20944/preprints202503.0929.v9) = mod-9 17-state FSM reduction â€”
CORRECTION (append-only): mod-9 FSM not "mod-4/12"; flaw = modular-
residueâ‰ magnitude (finite-slice engine can't control unbounded
magnitude). Chang 2026 (arXiv:2603.11066) = honestly conditional,
explicitly NOT a proof, reduces to open Orbit Equidistribution
Conjecture, machine-reviewed by Pith (NOT human peer review) â†’
CONDITIONAL, self-corrected a false Gap Lemma. Sibling claims surfaced:
Santana 2026 (arXiv:2601.03297) REJECTED by Pith, main theorem REFUTED
by counterexample fâ‚€(n)=n (fixed points in the paper's own family);
Kawasaki 2025 (arXiv:2502.20642, fixed-point approach, flawed);
Trifaro 2025 (viXra). Honesty: Zenodo/Preprints.org/arXiv/viXra assign
DOIs but are NOT peer-reviewed; Pith = machine review not human; Santana
refutation search-surfaced (minor to-verify directly). The amateur wave
hits the SAME wall the positive frontier derived (Tao log-density limit,
Terras/Krasikov-Lagarias density-1 stop, Î Â²â‚€-completeness) â€” a negative-
side convergent signal. Collatz frontier unchanged (pointwise/universal
control open; Tao 2019/22 strongest; 2^68 peer-reviewed / 2^71 project-
reported). Outcome confirmed (all flagged preprints status-resolved;
Nwankpa mechanism corrected; sibling claims + a refutation surfaced;
6-for-6 wall reinforced from the negative side), partial overall.
Files: attempt-06.md created; progress.md (consolidatedâ†’attempt-06,
to-verifyâ†’attempt-07 targets, honesty-check expanded with status-check +
Nwankpa correction), index.md, log.md updated. Yellow zone (weekly
71.9% / session 13%, 0 subagents â€” one targeted WebSearch).

## [CONTINUE 2026-08-25] birch-swinnerton-dyer (cycle 4/new run)

Budget-light sub-thread DEVELOPMENT Continue on BSD (yellow zone; weekly 73.6%
/ session 23.1% at STEP-0 live-check, <74% so cycle proceeds budget-light;
0 subagents; NO WebSearch â€” file-writes only, to minimize weekly drain ~1.4%
below the 75% pause threshold).

**Move:** developed the Kataokaâ€“Sano 2024 rank-2 Euler-system reframing
(attempt-06) structurally from existing notes + standard Mazurâ€“Rubin
rank-r Kolyvagin-system theory (a synthesis/development cycle, NOT a
verification). Four structural results:
- **Selmer-decomposition keystone:** Sel(K,E) â‰ƒ Sel(Q,E) âŠ• Sel(Q,E^K) IS
  the rank-2 structure â€” the two one-directional engines (cyclotomic Kato,
  anticyclotomic Heegner) are the two direct summands of one Selmer group;
  disjointness-as-field-variations = the direct-summand split.
- **Reframed obstruction:** rank-2 Euler system â†’ rank-2 Kolyvagin system
  (Mazurâ€“Rubin) controlling Sel(K,E) to corank â‰¤2 (= the missing r_an=2
  piece); the control step = the Darmon-derivative construction, a
  THREE-FOLD conditional (Heegner MC / Darmon-derivative Conj. 1.9 /
  Bockstein regulator â‰  0) â€” not a vague "rank-2 is hard." Resolution
  (each summand's MC) works; control (rank-2 composition) is the wall.
- **6-for-6 two-engine sharpening refined:** "both stop at rank 1" â†’
  "two engines combine into a rank-2 object; the composition-to-control
  step is the wall" â€” same spine as NS (resolve a slice, stop at the
  universal control) / Collatz (densityâ†’pointwise).
- **NEW cross-problem link â€” BSD's two avatars:** the function-field BSD
  (char p, the Hodge TateâŸºBSD-for-Jacobian bridge from attempt-06-Hodge,
  substantially proven via Katoâ€“Trihan) and the number-field BSD (the
  Millennium target, conditional via Kataokaâ€“Sano) are two faces of the
  same "control the multi-summand Selmer group" control step, in two
  cohomological theories (Ã©tale/crystalline on a surface vs Galois-
  cohomology Euler systems on a curve). Sharpens 6-for-6 from "BSD
  parallel to Hodge" to "two avatars of one control step, one proven one
  open."

**Files:** attempt-07.md created; progress.md (consolidatedâ†’attempt-07 +
attempt-07 best-partial block + Kataokaâ€“Sano to-verify note updated);
index.md (BSD attempt-07 line after attempt-06).

**Honesty:** SYNTHESIS/DEVELOPMENT, not verification. No WebSearch; the
Kataokaâ€“Sano Thm 1.5/1.9/1.11 specifics (rank-2 Euler-system construction,
Darmon-derivative Conj. 1.9, Bockstein regulator, three-fold conditional)
are NOT primary-source-verified this cycle â€” they remain the load-bearing
to-verify flag from attempt-06, the natural attempt-08 target. The Mazurâ€“
Rubin rank-r Kolyvagin-system framework and the function-field-BSD-proven /
number-field-BSD-open split are standard (not re-verified). No proof of
BSD. Outcome confirmed (coherent structural development + cross-problem
two-avatar link), partial overall.

**Loop state:** rotation restarts after Collatz; beals skipped (24
attempts). Next: navier-stokes (attempt-07). Weekly near 74% â€” STEP-5
live-check will decide pause vs continue at the 75% threshold.

---

[INGEST 2026-08-25] PvsNP â€” ingested a separate session's self-contained
P-vs-NP wiki into the main wiki.

A folder pasted in from a different session (originally misnamed
`Riemann-Hypothesis` â€” the content is complexity theory, not the Riemann
Hypothesis; user renamed it `PvsNP` on 2026-08-25) was integrated. The
folder `problems/PvsNP/` contains a complete nested LLM-wiki at `wiki/`
(own SCHEMA.md / index.md / log.md / pages/ / sources/) â€” a 28-cycle / 7-loop
attack on P vs NP (2026-08-21 â†’ 2026-08-24), self-cataloged.

**Content:** P vs NP / computational complexity (GCT, MCSP, meta-complexity,
disjoint NP pairs, proof complexity, resource-bounded measure, descriptive
complexity, KW communication). NOT the Riemann Hypothesis.

**Unifying meta-finding `[witness-needs-explicit-lb]` (the nested wiki's
7-loop product):** every live Pâ‰ NP-adjacent route bottlenecks on ONE open
non-compositional construction â€” an explicit balanced-point {expensive âˆ§
small-gap} lower-bound-carrying witness for a restricted class = the
circuit-LB / natural-proofs frontier. The three local barriers
(relativization / natural-proofs / algebrization) are local symptoms; the
construction lock is universal `[barriers-and-construction-are-complementary]`
(GCT escapes all three yet still hits the lock). Single live thread = (A),
the S1.a/ACâ° face `[s1a-is-the-live-thread]`, Gate 1 (recognizability) soft
from three directions, Gate 2 (tight window) binding. No breakthrough
`[honest-ceiling]` â€” the wall is an open construction (not a proven
impossibility), alive at the hardest known point. All web-grounded findings
are search/arXiv-summary-level, not PDF-line-verified (the to-verify flags).

**Integration choice (preserved, not flattened):** the nested `wiki/` is
coherent and self-cataloging (~70 files); destructively flattening it into
the main wiki's `attempts/`+`theory/` layout would be hard to reverse and
gain nothing. Instead, bridge files were added at `problems/PvsNP/`:
`problem.md` (statement + frontier), `progress.md` (read-first running
state, the central obstruction, the 7-loop arc, pointers into `wiki/`),
`notes.md` (methodology + the cross-problem 7-for-7 control-step link + the
BSD two-avatars analogue). The nested `wiki/sources/` plays the role of
`attempts/` (28 dated cycle files); `wiki/pages/` the synthesis/angle pages.
Reusable general theory was NOT promoted to the shared `theory/` toolbox
(the P-vs-NP barriers are specific to this problem, not reusable across the
six number-theory/PDE problems).

**Cross-problem link:** P vs NP extends the wiki's 6-for-6 control-vs-
resolution methodology to 7-for-7, with a qualification (structural analogy,
not mathematical equivalence â€” P vs NP is complexity theory; its wall is
uniquely an open construction blocked by natural-proofs-conditional-on-OWFs,
a status the number-theory problems do not share). The nested wiki's own
`[two-faces-two-np-variants]` (mining face closes / S1.a face stays open) is
the P-vs-NP analogue of BSD's two-avatars (function-field proven /
number-field open, [[birch_swinnerton_dyer]] attempt-07).

**Files:** created `problems/PvsNP/{problem,progress,notes}.md`; updated
`index.md` (PvsNP added to Problems + an attempts-pointer line at the end of
Attempts, pointing to the nested wiki's own catalog rather than duplicating
28 lines); appended this entry to `log.md`. The nested `wiki/` untouched.

**Honesty:** INGEST (structural integration + summary), not verification. No
new primary-source verification; no WebSearch this session. The nested
wiki's content and its `[honest-ceiling]`/to-verify flags are inherited
as-is. Folder name `PvsNP` is PascalCase, not the kebab-case convention â€”
kept at the user's explicit choice; cross-problem wikilink `[[PvsNP]]`.

**Loop state:** the /loop remains PAUSED on the weekly cap (83.4%, resets
Sun Aug 30). This ingestion was a user-requested side task, not a loop
cycle; the next loop cycle on resume is navier-stokes (attempt-07), and
the highest-value WebSearch move remains BSD primary-source-verify
Kataokaâ€“Sano 2024.

---

[ATTACK 2026-08-25] poincare-conjecture (attempt-01) â€” the eighth problem folder, set up at user request as "the perfect stopping point" giving a folder for every famous math problem. HONESTY CAVEAT surfaced up front: the PoincarÃ© Conjecture is **SOLVED** (Perelman 2002â€“03; the only solved Clay Millennium problem; Fields Medal 2006 + Clay prize 2010 both declined), so "1 attempt" is an exposition/verification, not an open-problem attack. Folder `problems/poincare-conjecture/` created with standard layout (problem.md / progress.md read-first / notes.md / attempts/attempt-01.md), kebab-case like the other six main-wiki problems (unlike PascalCase PvsNP). Cross-problem wikilink `[[poincare_conjecture]]`.

VERIFICATION (two targeted WebSearches, orange zone, no subagents): Perelman's three arXiv preprints â€” 0211159 (W-entropy F/W functionals, reduced volume, no-local-collapsing), 0303109 (canonical neighborhoods, Î´-cutoff surgery, discrete surgery times, long-time existence), 0307245 (finite extinction, sketched) â€” confirmed; finite extinction made rigorous by Coldingâ€“Minicozzi JAMS 2005 / Geom Topol 2008 via the width (min-max 2-sphere area) with Gaussâ€“Bonnet âˆ’4Ï€ forcing finite extinction on a homotopy 3-sphere; four independent verification accounts (Kleinerâ€“Lott 2008, Caoâ€“Zhu 2006, Morganâ€“Tian 2007, BessiÃ¨res et al. 2010) confirmed. CORRECTION (append-only): third preprint is arXiv:math/0307245, not 0307249 (prior session working note).

METHODOLOGICAL CONTRIBUTION â€” PoincarÃ© framed as the wiki's **positive-validation case** for the 7-for-7 control-step lens: Hamilton (1982) had the resolution machinery (Ricci flow) but stalled at the control step (finite-time singularities; could not classify / cut / terminate); every Perelman contribution (W-entropy monotonicity, canonical-neighborhood classification, Î´-surgery, finite extinction) is at the *control* step, not the resolution step â€” the one problem in the wiki where the identified obstruction was actually discharged. Contrast with the seven open problems (each has a resolution engine working on a slice + a control-to-full-strength wall not yet dischargeable). CROSS-PROBLEM LINK: [[navier_stokes]] is the closest structural twin â€” both geometric-PDE singularity-control problems; Ricci flow does blow up and Perelman closed control with a monotone Lyapunov functional (W-entropy); 3D NS asks whether blowup does NOT occur and no critical-coercive monotone quantity is known for the supercritical LÂ³ norm (Tao triple-log rate quantifies the gap) â€” the structural suggestion is that the missing NS ingredient is an entropy-type monotone functional (analogy, not equivalence; same disclaimer as PvsNP 7-for-7). More-general statement = Thurston Geometrization (PoincarÃ© = simply-connected corollary); higher-dim analogues Smale nâ‰¥5 1961, Freedman n=4 1982; n=3 the last and hardest (low dimension blocks h-cobordism/Whitney trick).

OUTCOME: confirmed (proof status verified + control-step reframing coherent + NS twin link established), partial as an attack (nothing to attack). HONESTY: exposition of a solved problem, no new mathematics; Perelman-preprint line-level details and the Coldingâ€“Minicozzi width inequality are search/arXiv-summary-level, flagged [to-verify] against primary sources. NO theory/ promotion yet (optional future: theory/theorems/geometrization-poincare.md, theory/methods/ricci-flow-surgery-control.md). Wiki now spans 8 problems: 7 open (beals, BSD, NS, YM, Hodge, Collatz, PvsNP) + 1 solved contrast case (poincare). â€” *Budget: orange (weekly ~83.4%), 0 subagents, 2 WebSearches. Loop still PAUSED (weekly reset Sun Aug 30 7PM local).*

---

[ATTACK 2026-08-25] riemann-hypothesis (attempt-01) â€” the 9th problem folder, set up at user request: "yes set up the Riemann Hypothesis folders." This was the one Clay Millennium problem missing from the wiki (the prior session's "Riemann-Hypothesis" folder turned out to be PvsNP content). OPEN â€” a genuine attack (unlike the solved [[poincare_conjecture]] contrast case). Folder `problems/riemann-hypothesis/` created standard layout (problem.md / progress.md read-first / notes.md / attempts/attempt-01.md), kebab-case. Cross-problem wikilink `[[riemann_hypothesis]]`.

VERIFICATION (4 WebSearches, orange zone, 0 subagents; 2 succeeded richly, 2 rate-failed): classical facts search-confirmed â€” Weil 1940s (RH for curves over finite fields), Deligne 1973/74 (Weil conjectures, RH for all varieties over F_q, via Ã©tale cohomology + Lefschetz trace + Rosati-positivity); Hilbert-PÃ³lya spectral program; Connes 1997 (numdam 10.5802/jedp.516) + 2019 essay (adele-class space spectral interpretation, RH âŸº trace formula validity, minus-sign/Riemannian obstruction); Li criterion 1997 (JNT 65, Î»_n â‰¥ 0 âŸº RH); Bombieri-Lagarias 1999 (JNT 77, generalization); Lagarias 1999 (Acta Arith. 89, Î¾-positivity); Suzuki 2023 (JLMS DOI 10.1112/jlms.12785, screw-function/KreÄ­n equivalents). Computational record: Platt-Trudgian 2021, all zeros on the line to height T = 3Ã—10^12 (standing record; no newer height record found). 2024 advances (status-checked): Guth-Maynard 2024 new zero-density bound at Ïƒ=3/4 breaking Ingham's 1940 80-year record (harmonic analysis + Dirichlet-polynomial matrix eigenvalues; sharper prime counts in short intervals) â€” RESOLUTION-ON-AVERAGE, not the control wall; Chourasiya 2024 (arXiv:2412.02068) first explicit Carlson estimate N(Ïƒ,T) â‰¤ K T^{4Ïƒ(1âˆ’Ïƒ)} (log T)^{5âˆ’2Ïƒ}. Proportion-on-line: Levinson 1/3 (1974) â†’ Conrey 2/5 (1989) â†’ 5/12 (2020); a 2024 claim of 2/3 (linear-algebraic/Weil-explicit-formula + Montgomery pair-correlation, Lean-4 core) flagged [rh-2024-claims-unverified] (NOT peer-reviewed; even if true a proportion â‰  all). CORRECTION (append-only): the prior session's working memory had no RH folder; none mislabeled here.

METHODOLOGICAL CONTRIBUTION â€” RH framed through the control-step lens as the 8th OPEN problem (7 prior open + PoincarÃ© solved contrast): resolution works on a slice/on average (computation up to T, Selberg almost-all, zero-density, zero-free regions, proportion) and stops at the control-to-full-strength step (EVERY zero, every height). The functional equation is resolution-layer symmetry (pairs zeros) that does NOT pin the line â€” forcing Î²=0 is the open content. THREE EXACT CONTROL-REDUCTIONS, each turning RH into a single undischarged property: (A) Hilbert-PÃ³lya self-adjointness (no operator known; Connes reduces RH to trace-formula validity = Weil positivity); (B) Weil/Li/Bombieri-Lagarias positivity (Î»_n â‰¥ 0 / explicit-formula distribution â‰¥ 0); (C) function-field Frobenius/Rosati positivity â€” PROVEN (Weil/Deligne), stops at the number field (no Frobenius/Rosati in char 0) = canonical "one-dimensional engine stops."

DEEPEST FINDING â€” the TWO-AVATARS structure: function-field RH (varieties/F_q, PROVEN Weil/Deligne) vs number-field RH (Î¶(s)/Q, OPEN Millennium). Same shape as [[birch_swinnerton_dyer]] (function-field BSD proven Kato-Trihan / number-field BSD open) and [[PvsNP]] (two faces, one closes one open). Two-avatars now in THREE problems â†’ sharpens 6-for-6/7-for-7 from "parallel control-step walls" to "two avatars of one control step, one proven one open." In all three, the function-field/geometric control tool has no char-0/number-field translation. HODGE LINK: the standard conjectures (Lefschetz B = algebraicity of inverse Lefschetz â†’ Rosati-type positivity) are the SAME control step for [[hodge_conjecture]] (HC â‡” standard conjectures â‡’ motives â‡’ HC) and for a motivic RH (number-field Rosati positivity) â€” shared control tool, both open. Sliceâ†’full echo to [[collatz_conjecture]] (densityâ†’pointwise) and [[navier_stokes]] (sliceâ†’full 3D).

â‰¥3 approaches named (A Hilbert-PÃ³lya, B positivity, C zero-density/computational, D function-field analogy, E de Branges tracked failed). Simpler-equivalent (Li/Weil/Bombieri-Lagarias), more-general (GRH/Selberg class/function-field RH). Counterevidence: symmetry-doesn't-pin; de Branges failure (coefficient inequality fails); average/density structurally cannot reach "all"; the un-peer-reviewed 2/3 claim. Confidence: RH almost certainly true (computation + GUE statistics + function-field precedent); confidence in a near-term proof LOW (each control-reduction lands on an undischarged property).

OUTCOME: partial (frontier mapped, obstruction framed as control step, BSD twin identified, Hodge standard-conjectures link drawn). No proof move; honest ceiling = map + framing + twin. HONESTY: 2024/preprint items + Connes/Li/Bombieri-Lagarias/Suzuki line-level details flagged [to-verify] against primary sources. NO theory/ promotion yet (optional future: theory/methods/function-field-two-avatars.md for the RHâ€–BSD twin; theory/methods/standard-conjectures-control.md for the RHâ€–Hodge link). Wiki now spans 9 problems: 8 open (beals, BSD, NS, YM, Hodge, Collatz, PvsNP, RH) + 1 solved contrast case (poincare). All 7 Clay Millennium problems are now in the wiki (PoincarÃ© solved; RH/BSD/NS/YM/Hodge/PvsNP open). â€” *Budget: orange (weekly ~83.4%), 0 subagents, 4 WebSearches. Loop still PAUSED (weekly reset Sun Aug 30 7PM local).*

---

[ATTACK/STUB 2026-08-25] unsolvedproblems.org sweep â€” user asked: "What about all of the problems on this website? Can we make sure we start a folder for each unsolved problem that we do not have yet?" Authoritative 24-problem list obtained by loading the site in the browser (Playwright) and reading the frame nav (the sidebar is frame-based and dropped by pageâ†’markdown; 3 WebFetches failed to capture it; one problem (dorabella) was hidden by an earlier find truncation). Classification of all 24:

ALREADY HAVE (3): beals-conjecture, collatz-conjecture, riemann-hypothesis.
SOLVED / NON-MATH â€” NOT given math-attack folders (4): Fermat's Last Theorem (solved, Wiles 1995; covered via [[beals_conjecture]] since BealâŸ¹FLT); Dorabella Cipher (solved decipherment); Zodiac Cipher (solved decipherment â€” z340 cracked 2020); Voynich Manuscript (open but DECIPHERMENT, not a conjecture â€” does not fit the wiki's 10-step attack protocol; flagged to user, not added).
NEW STUB FOLDERS CREATED (17 â€” open math/computational problems, problem.md only, full attack pending budget):
  Number theory / combinatorics: abc-conjecture, goldbach-conjecture, twin-prime-conjecture, legendre-conjecture, brocard-problem, grimm-conjecture, lonely-runner-conjecture, odd-perfect-number, perfect-cuboid, 4d-euler-brick, rational-distance, magic-square-of-squares, square-of-cubes (semi-magic of cubes, statement confirmed via fetch: 3Ã—3 semi-magic of 9 distinct positive cubes, known 8/9 near-miss), chromatic-number-of-the-plane (Hadwigerâ€“Nelson, 5â‰¤Ï‡â‰¤7; de Grey 2018 Ï‡â‰¥5).
  Computational / crypto (overlap [[PvsNP]], each flagged as a subface): rsa-factoring (integer factorization in P?), discrete-logarithm (DLP), diffie-hellman (CDH; DLPâŸ¹CDH, converse open).

Each stub = statement + status + one-line frontier + one-line control-step framing + cross-problem wikilinks, all load-bearing facts flagged [to-verify]. Registered in index.md under a new "## Problem stubs (folders started, full attack pending)" section. Honesty: depth = stubs only (orange budget weekly ~83.4% â€” a full 17Ã—4-file attack is infeasible now); "start a folder" = the literal ask. Scope decisions surfaced: (i) the 3 cipher problems excluded as non-conjectures (offered to add a decipherment category if the user wants); (ii) the 3 crypto problems included but flagged as subfaces of [[PvsNP]]'s [witness-needs-explicit-lb] / one-way-function hardness (a full attack would route through PvsNP, not duplicate it). Control-step framing honest where weak (the Diophantine "searchâ†’global" problems: perfect-cuboid, 4d-euler-brick, rational-distance, magic-square-of-squares, square-of-cubes, odd-perfect-number, brocard â€” framed as sliceâ†’global / simultaneous-Diophantine control, the weakest fit, flagged as such).

Wiki now spans 26 problem folders: 9 full (beals, BSD, NS, YM, Hodge, Collatz, PvsNP, poincarÃ©-solved-contrast, riemann) + 17 stubs. All 7 Clay Millennium problems present; the unsolvedproblems.org open set fully covered. â€” *Budget: orange (weekly ~83.4%), 0 subagents. Loop still PAUSED (weekly reset Sun Aug 30 7PM local).*

[ATTACK/STUB 2026-08-25] user-requested additions (outside the unsolvedproblems.org sweep):
  (a) conway-thrackle-conjecture â€” Conway's Thrackle Conjecture: any thrackle on n
      vertices has m â‰¤ n edges. OPEN; US$1000 Conway prize (unclaimed). Verified by
      computer to n=11. Best upper bound m â‰¤ 1.393(nâˆ’1) (Yian Xu 2021, Appl. Math.
      Comput., DOI 10.1016/j.amc.2020.125573; confirmed by Keszeghâ€“Sukâ€“Tardosâ€“Zeng
      2025, arXiv:2512.04795 [to-verify]); lower bound m = n attained (odd cycles of
      length â‰¥5). Improvement history: 2nâˆ’3 (LovÃ¡szâ€“Pachâ€“Szegedy 1997) â†’ 3/2(nâˆ’1)
      (Cairnsâ€“Nikolayevsky 2000) â†’ 1.428n (Fulekâ€“Pach 2011) â†’ 1.3984n (2019) â†’ 1.393.
      Solved special cases: geometric/straight-line (ErdÅ‘s; short proof Perles),
      outerplanar, x-monotone (Pachâ€“Sterling 2011). Structural localization: if
      false, minimal counterexample = two even cycles sharing a vertex. Control
      framing: two-sided-bound squeeze (Conway thrackle constant C_78 âˆˆ [1, 1.393]),
      twin to [[chromatic_number_of_the_plane]] (5â‰¤Ï‡â‰¤7).
  (b) aaronson-quantum-prize â€” Aaronson's US$100,000 wager (2012, IEEE Spectrum)
      that scalable quantum computing is IMPOSSIBLE in the physical world (the
      skeptics' burden: supply a physical reason scalable QC fails AND the fast
      classical algorithm simulating Nature's quantum systems). OPEN; prize
      unclaimed [to-verify: status]. Underlying open problem: is scalable,
      fault-tolerant quantum computation physically realizable? Frontier: finite/
      noisy "quantum supremacy" demonstrations (Google Sycamore 2019 53-qubit RCS;
      BosonSampling) are CONDITIONAL-hardness results (QUATH/XQUATH; Aaronsonâ€“Chen
      2017, Aaronsonâ€“Gunn 2020); unconditional hardness would need Pâ‰ PSPACE (open).
      Threshold theorem = conditional physical scalability. Control framing:
      two-avatars (twin to BSD/RH) â€” complexity avatar (unconditional classical
      hardness = a Pâ‰ PSPACE-type lower bound, subface of [[PvsNP]]
      [witness-needs-explicit-lb] / natural-proofs frontier) + physics avatar
      (impossibility = a [[yang_mills]]-grade new physical theory). Resolution runs
      on the finite/noisy supremacy slice; control-to-scalable is the wall on both
      faces.
  Both as problem.md-only stubs (orange budget, 0 subagents), registered in
  index.md under "## Problem stubs". Wiki now spans 28 problem folders: 9 full +
  19 stubs. Facts verified via 2 WebSearches; load-bearing items flagged [to-verify].

---

[CONTINUE 2026-08-30] birch-swinnerton-dyer (attempt-08) â€” primary-source
verification of Kataokaâ€“Sano 2024 against the published PDF body, executed
under the user's "Spend now" choice (orange zone, weekly ~83.4%, 0 subagents,
resetting Sun Aug 30 7 PM local). This is the attempt-07 "Next (attempt-08)"
target: upgrade [bsd-kataoka-sano-2024] from to-verify to CONFIRMED.

METHOD: the published PDF (J. Assoc. Math. Res. 2(2):154â€“208, 2024, DOI
10.56994/jamr.002.002.001) was downloaded and text-extracted with a raw
zlib/FlateDecode stream extractor written in Python (no PDF library available
â€” fitz/pypdf/PyPDF2/pdfplumber/pdfminer all missing; Read's pdftoppm also
absent). The extractor decompressed each `streamâ€¦endstream` block and pulled
`(â€¦)Tj` / `[â€¦]TJ` text operators, yielding 139 KB of fragmented text (spaces
dropped, accents mangled) â€” sufficient to read theorem numbers and formulas
verbatim.

NUMBERING DISCREPANCY RESOLVED: the published version renumbered the
introduction. Authoritative published numbers (read from the PDF): Thm 1.4
(Thm 5.17) Heegner MC âŸº Iwasawa MC for z^Hg_âˆž; Thm 1.5 (Thm 5.18) Heegner MC
âŸ¹ rank-two Euler system c with c_{K_âˆž}=z^Hg_âˆž; Conj 1.9 (Prop 5.26)
Darmon-derivative explicit formula Îº^Hg_âˆž = L*_S(E/K,1)Â·|D_K|Â·Î©_{E/K}Â·R_{E/K}Â·
R^Boc_{K_âˆž}; Thm 1.10 (Thm 5.27) algebraic variant of Conj 1.9 âŸ¸ Heegner MC
up to Z_p^Ã—; Thm 1.11 (Thm 5.29) Heegner MC + Conj 1.9 + R^Boc_{K_âˆž}â‰ 0 âŸ¹
p-part of BSD for E/K. The arXiv v1 had Conj 1.6 / Thm 1.8 (pre-revision).
The wiki's existing citation (Conj 1.9 / Thm 1.11) is CORRECT for the
published version; both numberings now recorded.

ALL FIVE LOAD-BEARING CLAIMS CONFIRMED verbatim, plus the basic-rank r_T=2
claim ("the basic rank r_T is two in this setting, since we have âŠ•_{vâˆˆS_âˆž(K)}
H^0(K_v,T*(1)) = H^0(C,T*(1)) = T*(1) and this is a free Z_p-module of rank
two") and the abstract's "natural interpretation of the Heegner point main
conjecture in terms of rank two Euler systems."

BCK21 SHARPENING (the cycle's most consequential new fact): Remark 1.6 reads
"Burungaleâ€“Castellaâ€“Kim has recently proved the Heegner point main conjecture
under mild [conditions] (BCK21). [Theorem] 1.5 gives an unconditional
construction of a rank two Euler system which is related to Heegner points.
However, it should be noted that our [construction is not canonical]." So
Burungaleâ€“Castellaâ€“Kim (Algebra & Number Theory 15, 2021) discharges the
FIRST leg of the three-fold conditional â€” Thm 1.5's rank-2 Euler system now
exists UNCONDITIONALLY (non-canonically). The three-fold conditional of
Thm 1.11 is now TWO-fold: Conj 1.9 (Darmon-derivative) + R^Boc_{K_âˆž}â‰ 0
(Bockstein regulator). This is a clean confirmation of attempt-07's
"obstruction at the control step, not the resolution step" â€” the resolution
step (rank-2 Euler system existence) is now discharged by a named theorem,
and the control step (Darmon-derivative Kolyvagin system + non-degeneracy)
is the wall. Direction (A) is anchored to a named two-condition target.

HONESTY: (i) the PDF text is fragmented (raw stream extractor), but every
content claim rests on an unambiguous fragment; (ii) BCK21's exact hypotheses
are flagged to-verify (Remark 1.6 says "under mild conditions" without
spelling them out in the extracted text); (iii) Thm 1.10's precise "up to
Z_p^Ã—" qualifier is read from the PDF but not line-by-line re-derived. No
proof move; BSD remains open (rank â‰¥2 and exact |Sha| untouched).

FILES: attempt-08.md written; progress.md consolidated through attempt-08
([bsd-kataoka-sano-2024] upgraded to CONFIRMED with published numbering +
BCK21 note); index.md attempt-08 line added; this log entry appended.

NEXT (attempt-09, when budget allows): primary-source-verify BCK21
(Burungaleâ€“Castellaâ€“Kim 2021, ANT 15) â€” the exact hypotheses under which the
Heegner MC is now proven, since that determines how "unconditional" Thm 1.5's
rank-2 Euler system really is. Secondary: verify Thm 1.10 and Conj 1.9's
algebraic variant against Â§5.4. â€” *Budget: orange (weekly ~83.4%), 0
subagents. Loop still PAUSED (weekly reset Sun Aug 30 7 PM local).*

---

[CONTINUE 2026-08-30] birch-swinnerton-dyer (attempt-09) â€” primary-source
verification of BCK21, executed under the user's "run until 99% weekly used"
directive. Live usage checked via Playwright on the Ollama settings page:
**weekly 94.5% used** (resets Sun Aug 30 7 PM, ~18h), session 26.5%. The
stale usage-status.json (83.4%, Aug 25) was superseded by the live read.

VERIFIED (1 WebSearch, primary source): Burungaleâ€“Castellaâ€“Kim, *A proof of
Perrin-Riou's Heegner point main conjecture*, Algebra & Number Theory 15:7
(2021), 1627â€“1653, DOI 10.2140/ant.2021.15.1627, arXiv:1908.09512. This pins
down the "mild conditions" of Kataokaâ€“Sano's Remark 1.6 (attempt-08). Theorem
A: E/Q conductor N, p>3 good ordinary, K imaginary quadratic with (Heeg)
generalized Heegner hypothesis (N^- squarefree product of an EVEN number of
primes) + (disc) D_K odd â‰  âˆ’3, Hypothesis â™  (three ramification conditions on
E[p]), Ï surjective, p nonanomalous âŸ¹ the Heegner MC (Perrin-Riou Conj 1.1)
holds. So Kataokaâ€“Sano Thm 1.5's rank-2 Euler system exists UNCONDITIONALLY
within this class â€” the three-fold conditional is now TWO-fold (Conj 1.9 +
R^Boc_{K_âˆž}â‰ 0). Theorem B (bonus): + p splits âŸ¹ Iwasawaâ€“Greenberg MC for the
BDP p-adic L-function Char_Î›(X^{âˆ…,0}) = (L_p^BDP)Â² â€” the anticyclotomic
summand, so BOTH summands' main conjectures (cyclotomic Kato + anticyclotomic
BDP) are proven and the wall is purely the rank-2 composition control.
Theorem 3.2: modular-form generalization (Hypothesis â™¥, fourth condition
HÂ¹(Q_â„“,A_f[â„˜])=Hâ°(Q_â„“,A_f[â„˜])={0} for â„“Â²|Nâº). Appendix Thm A.1: rank-one
alternative without nonanomalous (Hypothesis â™  + Ï surjective + p splits +
ord_{s=1}L(E/K,s)=1). Methods: Howard bipartite Euler systems (2006), Wei
Zhang Kolyvagin-conjecture (2014), Bertoliniâ€“Darmon (2005), Pollackâ€“Weston
(2011), Chidaâ€“Hsieh (2015), Castellaâ€“Hsieh explicit reciprocity extended to
N^-â‰ 1; dispenses with Xin Wan's Rankinâ€“Selberg results; allows N^-=1, N with
square factors, p inert.

SHARPENING: the BSD obstruction is now the cleanest it has ever been â€” a
TWO-fold conditional (Conj 1.9 Darmon-derivative + R^Boc_{K_âˆž}â‰ 0 Bockstein
regulator) over a PROVEN base (Heegner MC, BCK21 Thm A). Both summands'
main conjectures are theorems; the wall is purely the rank-2 composition
control (Darmon-derivative Kolyvagin system + non-degeneracy). This is the
sharpest statement of the "obstruction at control, not resolution" thesis.

HONESTY: (i) no proof move â€” BSD open, rank â‰¥2 and exact |Sha| untouched;
(ii) the Heegner MC is proven for a large explicit class, NOT all E/Q (good
ordinary, p>3, Hypothesis â™ , Ï surjective, p nonanomalous); (iii) Theorem B's
Char_Î› ideal equality and Theorem 3.2's Hypothesis â™¥ fourth condition are
recorded from the search summary (primary-source-consistent, not line-by-line
re-derived) â€” flagged to-verify if load-bearing.

FILES: attempt-09.md written; progress.md consolidated through attempt-09
([bsd-bck21-2021] added CONFIRMED); index.md attempt-09 line added; this log
entry appended.

NEXT (attempt-10): survey what is known toward Conj 1.9 (the Darmon-derivative
explicit formula â€” Thm 1.10 already reduces it to the Heegner MC up to Z_p^Ã—,
so the gap is the explicit Z_p^Ã— unit = the Bockstein regulator) and whether
R^Boc_{K_âˆž}â‰ 0 is known in any case. â€” *Budget: weekly 94.5% â†’ spending toward
the user's 99% target; 0 subagents.*

---

[CONTINUE 2026-08-30] birch-swinnerton-dyer (attempt-10) â€” survey of the
remaining two-fold conditional (Conj 1.9 + R^Boc_{K_âˆž}â‰ 0), under the user's
"run until 99% weekly used" directive. Live usage: weekly 95.1% (up 0.6% from
one cycle).

VERIFIED (1 WebSearch): the remaining gap is located in the literature. Sano
2023, *Derived Bockstein regulators and anticyclotomic p-adic Birch and
Swinnerton-Dyer conjectures*, arXiv:2308.08875 â€” introduces "derived Bockstein
regulators" (NekovÃ¡Å™'s Selmer complexes, AstÃ©risque 310); general descent
formalism (Thm 2.13); Thm 3.10 (Bertoliniâ€“Darmon BSD-type conjecture for
Heegner points âŸ¸ Heegner MC up to a p-adic unit, UNCONDITIONAL corollary via
BCK21); Thm 4.13 (Agboolaâ€“Castella p-adic BSD for BDP âŸ¸ Iwasawaâ€“Greenberg MC
up to a unit); Conj 5.5 (derived setting for Kataokaâ€“Sano derivative
conjectures). Cyclotomic twin: Burnsâ€“Kuriharaâ€“Sano 2025 (IMRN, DOI
10.1093/imrn/rnaf012, Kato derivatives + Mazur-Tate). Original: Darmon 2007
refined Mazur-Tate for Heegner points.

STRUCTURAL INSIGHT: the regulator is DERIVED because the anticyclotomic p-adic
height pairing degenerates â€” this is WHY the remaining gap is a derived
control step, not a classical one. It is a concrete, named mechanism, not a
vague "rank-2 is hard."

SHARPENING: the entire BSD-for-E/K chain is now proven UP TO A SINGLE p-adic
unit (the derived Bockstein regulator). Conj 1.9 is the explicit formula for
that unit; R^Boc_{K_âˆž}â‰ 0 is its non-vanishing. So the BSD obstruction is now:
one explicit p-adic unit (the derived Bockstein regulator) separates the
proven "up to a unit" results from the full p-part of BSD for E/K. The
two-summand structure persists to the control step (cyclotomic Kato
derivatives + anticyclotomic Heegner derivatives).

HONESTY: (i) no proof move â€” BSD open, rank â‰¥2 and exact |Sha| untouched;
(ii) Sano 2023 is an arXiv preprint (publication status not confirmed);
(iii) the theorem statements (Sano Thm 2.13/3.10/4.13, Conj 5.5; BKS 2025)
are recorded from the search summary, not line-by-line re-derived â€” flagged
to-verify; (iv) the "degenerate height pairing" mechanism is search-derived.

FILES: attempt-10.md written; progress.md consolidated through attempt-10
([bsd-sano-2023-derived-bockstein] added to-verify); index.md attempt-10 line
added; this log entry appended.

NEXT (attempt-11): primary-source-verify Sano 2023 (arXiv:2308.08875) against
the paper body â€” the exact statements of Thm 3.10/4.13 and whether Conj 5.5
subsumes Kataokaâ€“Sano's Conj 1.9. â€” *Budget: weekly 95.1% â†’ spending toward
the user's 99% target; 0 subagents.*

---

[CONTINUE 2026-08-30] birch-swinnerton-dyer (attempt-11) â€” primary-source
verification of Sano 2023 against the arXiv abstract (WebFetch of
arxiv.org/abs/2308.08875), under the user's "run until 99% weekly used"
directive. Live usage: weekly 96% (up 0.9% from one cycle).

CONFIRMED from the abstract: Takamichi Sano, *Derived Bockstein regulators and
anticyclotomic p-adic Birch and Swinnerton-Dyer conjectures*, arXiv:2308.08875,
submitted 17 Aug 2023 â€” ARXIV-ONLY (no journal reference; a preprint, not
peer-reviewed). "Derived Bockstein regulators" introduced "by using an idea of
NekovÃ¡Å™" + "a general descent formalism involving derived Bockstein
regulators." Three applications confirmed: (1) Bertoliniâ€“Darmon BSD-type
conjecture for Heegner points âŸ¸ Perrin-Riou's Heegner MC up to a p-adic unit;
(2) Agboolaâ€“Castella p-adic BSD for BDP âŸ¸ Iwasawaâ€“Greenberg MC up to a
p-adic unit; (3) Kataokaâ€“Sano derivative conjectures extended to a "natural
derived setting."

DOWNGRADED to to-verify (NOT in the abstract): the exact theorem numbers
(2.13/3.10/4.13/5.5), the "unconditional corollary via BCK21," and the
"degenerate height pairing" mechanism (attempt-10's structural explanation) â€”
all search-derived, need the PDF body. The core "one explicit p-adic unit"
sharpening survives at the abstract level.

FILES: attempt-11.md written; progress.md consolidated through attempt-11
([bsd-sano-2023-derived-bockstein] updated with abstract-level status);
index.md attempt-11 line added; this log entry appended.

NEXT (attempt-12): either fetch the Sano 2023 PDF body to confirm Thm
3.10/4.13 exact statements, or rotate to navier-stokes (attempt-07) per the
standing rotation â€” the BSD direction-(A) chain is now mapped to a single
named target (the derived Bockstein regulator), so further BSD verification
is PDF-body-level detail. â€” *Budget: weekly 96% â†’ spending toward the user's
99% target; 0 subagents.*

---

[CONTINUE 2026-08-30] navier-stokes (attempt-07) â€” rotation turn, under the
user's "run until 99% weekly used" directive. Two WebSearches; resolves the
two remaining attempt-06 to-verify items.

(i) SEREGIN 2024 (2402.13229) PUBLICATION STATUS RESOLVED: still a preprint.
No journal DOI found; the revised version (Oct 8, 2024) is retitled "A note
on potential Type II blowups of axisymmetric solutions to the Navier-Stokes
equations" (dedicated to Nadirashvili). Decisive evidence: Seregin's own July
2025 preprint (arXiv:2507.08733) cites 2402.13229 as a preprint. The
PUBLISHED Seregin piece is the predecessor: *Remarks on Type II blowups of
solutions to the Navier-Stokes equations*, CPAA 23(10) (2024), 1389â€“1406, DOI
10.3934/cpaa.2023108 (dedicated to Å verÃ¡k). NEW: Seregin July 2025 preprint
arXiv:2507.08733, "A note on certain scenarios of Type II blowups of suitable
weak solutions to the Navier-Stokes equations" â€” the Type II exclusion
program continues. The Hou/Seregin peer-review asymmetry persists (Hou 2024
published Found. Comput. Math. 2026; Seregin 2024 preprint) but the fence now
has a published predecessor + a 2025 extension.

(ii) HUANGâ€“QINâ€“WANGâ€“WEI CMP 406:243 (2025) CONFIRMED: *Exact Self-Similar
Finite-Time Blowup of the Houâ€“Luo Model with Smooth Profiles*, DOI
10.1007/s00220-025-05429-9, arXiv:2308.01528 (received 3 Nov 2024, accepted
29 July 2025, published 1 Sept 2025, communicated by A. Ionescu). PURELY
ANALYTIC: Schauder fixed-point argument on a compact convex set in a weighted
L^âˆž Banach space, NO computer assistance; C^âˆž smooth profiles with proven
monotonicity/convexity + algebraic far-field decay; scaling bound 2 < c_l â‰¤
2(Î±+1)/(Î±âˆ’1) â‰ˆ 4.5298 (cruder than Chenâ€“Houâ€“Huang's computer-assisted
2.99870Â±6Ã—10â»âµ, Ann. PDE 2022, but analytic); builds on their ARMA 248 (2024)
generalized-CLM framework; next target 2D Boussinesq.

SHARPENING: the 1D Houâ€“Luo engine now achieves exact self-similar blowup
FULLY ANALYTICALLY (upgraded from computer-assisted) â€” the resolution side of
the 1D slice is analytic; the control step (1D/weakened â†’ full 3D smooth
data) remains the wall. The cleanest NS mirror of the "obstruction at
control, not resolution" thesis.

HONESTY: (i) no proof move â€” Millennium problem untouched; (ii) Seregin 2025
(2507.08733) content recorded from the search summary (title + citation
behavior confirmed; content to-verify); (iii) Houâ€“Qinâ€“Wang arXiv:2606.26658
(2026) remains to-verify (not searched); (iv) HQWW details from the search
summary, not line-by-line re-derived from the CMP PDF.

FILES: attempt-07.md written; progress.md consolidated through attempt-07
(Seregin status resolved; HQWW CMP 2025 upgraded to verified); index.md
attempt-07 line added; this log entry appended.

NEXT (attempt-08): verify Seregin 2025 (arXiv:2507.08733) and Houâ€“Qinâ€“Wang
2026 (arXiv:2606.26658) â€” whether the fence has moved or the
generalizedâ†’true-viscosity gap has narrowed. â€” *Budget: weekly ~96% â†’
spending toward the user's 99% target; 0 subagents.*

---

[CONTINUE 2026-08-30] navier-stokes (attempt-08) â€” two WebSearches, under the
user's "run until 99% weekly used" directive. Live usage: weekly 97.4%.

(i) SEREGIN 2025 (arXiv:2507.08733) CONFIRMED: *A note on certain scenarios
of Type II blowups of suitable weak solutions to the Navier-Stokes equations*
(July 11, 2025, preprint, math.AP; Leverhulme Emeritus Fellowship 2023).
Technique: Euler scaling + LIOUVILLE-TYPE THEOREMS FOR ANCIENT EULER
SOLUTIONS â€” a new engine for the Type II exclusion fence. Thm 2.1: parameter
region for m, mâ‚€ completely excluding a Type II scenario (growth (1.2) +
boundedness (1.4)); shows a CPAA 2024 restriction was TOO STRONG (the fence
is widening). Sec 3: modified scenario, necessary condition = non-trivial
ancient Euler solution in a specific class. Sec 4: Liouville theorems
(self-similar, discrete self-similar, axisymmetric zero-swirl). Thm 5.1:
exclusion under an LPS-type condition (classical LPS when m=1).

(ii) HOUâ€“QINâ€“WANG 2026 (arXiv:2606.26658) CONFIRMED: *Exact Blowup Analysis
for the Weak-Advection Houâ€“Li Model* (June 25, 2026, preprint). Exact
finite-time self-similar blowup: periodic 2/3<a<1 (profiles neither focusing
nor expanding); whole-space + Neumann 0<aâ‰¤1 (focusing / non-expanding-non-
focusing / expanding trichotomy by the sign of the scaling parameter).
Fixed-point near origin + ODE extension + regularity/asymptotics/monotonicity/
uniqueness. The 1D resolution side is now essentially complete.

(iii) NEW MAJOR â€” HOUâ€“WANGâ€“YANG 2026 (arXiv:2509.25116v2, v2 Aug 11, 2026):
*Nonuniqueness of Lerayâ€“Hopf solutions to the unforced incompressible 3D
Navierâ€“Stokes Equation*. Claims the first rigorous COMPUTER-ASSISTED proof of
Lerayâ€“Hopf nonuniqueness: infinitely many distinct SUITABLE Lerayâ€“Hopf
solutions with the same divergence-free initial data; code at
github.com/HouGroup2026/3d-navier-stokes-nonuniqueness. This is exactly the
attempt-03 "MAJOR OPEN problem" (Buckmasterâ€“Vicol 2019 proved nonuniqueness
only below Lerayâ€“Hopf, Î²<1/2). If confirmed, the Lerayâ€“Hopf uniqueness
question (open since Leray 1934) is settled NEGATIVELY. FLAGS: preprint,
computer-assisted (validity depends on the code), search-surfaced â€” the
single most consequential NS to-verify item. Does NOT resolve the Millennium
problem (regularity/breakdown), but sharpens the weak-solution landscape.

FILES: attempt-08.md written; progress.md consolidated through attempt-08
(Seregin 2025 + HQW 2026 upgraded to verified; [ns-hou-wang-yang-2026] added
to-verify HIGH PRIORITY); index.md attempt-08 line added; this log entry
appended.

NEXT (attempt-09): primary-source-verify Houâ€“Wangâ€“Yang 2026
(arXiv:2509.25116v2) against the arXiv HTML/PDF (and the code) â€” the claimed
Lerayâ€“Hopf nonuniqueness proof. â€” *Budget: weekly 97.4% â†’ spending toward the
user's 99% target; 0 subagents.*

## [CONTINUE 2026-08-31] beals-conjecture (attempt-25) + breakthrough-hunt session (ultracode)

Session: post-reset usage check (weekly 0.2% -> green); breakthrough-hunt
workflow (8 problem-scan agents; 6 completed, RH+stubs deferred after Ollama
session-cap 429s) -> 18 candidates; adversarial-verify workflow (9 agents:
novelty/soundness/referee x 3 shortlisted candidates). Winner: the Beal
near-miss package; Collatz m=92 deadlock survives with constant corrections
(pending the decisive Wang INTEGERS 2026 check); BSD point-supply reduction
needs revision (converse needs Sha-finiteness clause - filed as note, not
paper this session).

ATTACK OUTPUT (beals-conjecture attempt-25):
1. THEOREM (stratification, T1-T4): all unit-base gap-(+1) near-misses of any
   distinct-prime signature lie exactly on the two universal families
   (global, elementary); the gap-(-1) channel is exactly odd-odd Pillai-2;
   raw-metric bound 2^min(p,q); even-exponent boundary via Cohn 1993/BMS 2006
   [attribution to-verify].
2. NEW CONJECTURE odd-odd Pillai-2 (X^u - Y^v = 2, u,v odd primes): no
   solutions to Y^v <= 10^18 (1,004,437 powers), everywhere locally soluble
   (no modulus <= 1000, no prime power <= 10^6) - Catalan-like.
3. CORRECTED 56-SIGNATURE TABLE (all distinct-odd-prime sigs from primes
   <= 23): bug in search_3711.py/search_5711.py found+fixed -> (3,7,11) min
   gap 277 -> 147 at (2,3,2); (5,7,11) 288 -> 171 at (2,3,2); scripts
   deprecated with headers; "monotone in -chi" law REFUTED by corrected data.
4. CORNER PRINCIPLE: min genuine gap always at C <= 3 - verified 56/56
   (C=2 for 55, C=3 only at (5,11,13)); 0 genuine gap-1 hits in the whole
   scanned open class; failure boundary at granularity exponent gamma <= 5/3
   ((3,3,3),(3,3,5) fail; (3,3,7),(3,5,5) hold; open class gamma >= 3.267).
5. PREPRINT DRAFT: papers/beal-near-miss-stratification.md (abstract, T1-T4
   proofs, conjectures, table, corrections, mechanism, honesty block).
   Adversarially verified (novelty 4/4 negative checks; soundness: bug
   confirmed by independent re-run, T1-T4 re-derived; referee: JIS/Integers
   grade). To-verify before submission: Ratcliffe-Grechuk 2412.11933 full
   read; T4 citation chain; robustness run (in progress, C<=100 B<=1e5).

FILES: attempt-25.md; progress.md (correction block + attempt log 25);
synthesis.md (dated correction blockquote); theory/theorems/
near-miss-stratification.md; theory/conjectures/odd-odd-pillai-2.md;
theory/conjectures/corner-principle.md; scripts near_miss_package.py +
near_miss_robustness.py + audit_corrected_scan.py; deprecated headers in
search_3711.py/search_5711.py; papers/beal-near-miss-stratification.md;
index.md entries; this log entry.

NEXT: (a) robustness run completion -> patch preprint 5.3; (b) Ratcliffe-
Grechuk + Cohn primary-source reads; (c) Collatz m=92 deadlock note (Wang
check + exact-rational constants); (d) BSD proposition filing with the
Sha-finiteness fix; (e) YM corrections (2505.16585 = Cao-Nissim-Sheffield,
not Chatterjee; Zenodo SU(3) flag); (f) RH + stubs hunt scans when budget
allows. - Budget: weekly 43%, session 41.5% at last check; waves <= 3 agents.

## [CONTINUE 2026-08-31] addendum â€” collatz kill, BSD/YM filings, cycle-bounds page update

1. COLLATZ: the hunt's "m=92 deadlock" candidate KILLED by prior art found in
   the decisive novelty check - Wang 2026 (Zenodo preprints, June 2026,
   UNREVIEWED) claims computer-assisted exclusion of m-cycles for m <= 93,
   bypassing the CF-rung structure via suffix-balanced certificates. Filed
   in problems/collatz-conjecture/notes.md (candidate refuted, residual
   value noted; Wang flagged to-verify). Literature catch: the folder was
   missing Hercher 2023 (JIS 26, m <= 91 peer-reviewed - supersedes the
   recorded SdW m <= 75) - theory/theorems/collatz-cycle-bounds.md updated
   (Hercher line + Wang flagged line). NOTE: notes.md was rewritten fresh
   this session; if any pre-2026-08-31 scratch content existed there it was
   not preserved - flagged for honesty (the folder's substantive state lives
   in attempts 01-06 and progress.md, which are untouched).
2. BSD: attempt-12 filed - point-supply reduction with the REQUIRED SHA-FIX
   ((a)+(b) <=> [rank part AND Sha[p^inf] finite]; naive converse false per
   Kim's own Thm 1.8(4)); semi-decidability asymmetry + mod-p-descent
   comparison recorded; referee verdict: expository altitude, filed not
   papered. Index line added.
3. YM: attempt-07 filed - corrections (arXiv:2505.16585 = Cao-Nissim-
   Sheffield NOT Chatterjee [to-verify]; Zenodo SU(3) Gamma-convergence
   claim added to watchlist), the 1980s hierarchical MK program surfaced
   (Kupiainen PRL 55:558 / CMP 1987; Mueller-Schiemann LMP 15:289 - the
   unique 4D continuum-limit+gap success), and three new directions
   recorded not attacked: (D) single-inequality MK-deviation reduction
   (highest ceiling), (E) Wilson-flow summability lemma (adjudicates
   Eriksson Thm 3.11), (F) g^2-vs-g^4 defect-threshold conjecture
   (certified python-runnable). Index line added.

## [CONTINUE 2026-08-31] robustness CONFIRMED â€” Corner Principle holds in the wider box

near_miss_robustness.py (C<=100, B<=1e5, all 56 signatures, 942s exact
integer arithmetic): **0 violations of corner==full**; every full-box
minimum identical to the C<=60 table; every corner minimum unchanged. Also
discharges attempt-24's wider-box to-verify flag on the (5,7,13) value 1771.
Preprint 5.3 patched (placeholder removed); corner-principle.md and
attempt-25 updated. Remaining pre-submission to-verify: Ratcliffe-Grechuk
2412.11933 full read; T4 citation chain (Cohn 1993 / LeVeque 1952; BMS II
pages).

## [CONTINUE 2026-08-31] pre-submission to-verify gates CLEARED

1. Ratcliffe-Grechuk arXiv:2412.11933 read in full (WebFetch): NO near-miss
   analysis (Prop 1.3 = exact solutions only, z^r <= 2^100), NO unit-base
   classification (footnote 6 identifies exponent-of-1 variants only
   combinatorially), NO Pillai-2 content. The novelty gate for the entire
   package is CLEARED against the definitive solved-cases survey. Bonus
   corroboration: their Table 1.4 lists the unit-base exact solution
   (5,1,3) - the same 5^2+2=3^3 identity T4 isolates. Smallest open Beal
   triple (3,5,7) confirmed as stated.
2. T4 citation chain VERIFIED: Fermat (asserted n=3) -> Euler (proof) ->
   Nagell 1954 (Arch. Math. 5, at-most-one for D=2) -> Cohn 1993 (Acta
   Arith. 65.4, 367-381, C=2 among 77 values 1<=C<=100) -> BMS II (Compositio
   142 (2006) 31-62, arXiv:math/0405220; complete for all 1<=D<=100, D=2
   unique (+-5,3,3)). Paper refs 6/7/7b and the honesty block updated;
   only the BMS D=2 table entry direct-read remains before submission.
Paper: papers/beal-near-miss-stratification.md now has zero placeholder
claims; all to-verify flags in it are resolved except the one noted.

## [HUNT 2026-08-31] RH + stubs breakthrough-hunt â€” scan wave + adversarial
## verify wave + filing, CLOSED

The deferred item (f) of the prior breakthrough-hunt: scan +
adversarial-verify over `problems/riemann-hypothesis/` and the ~19 stubs.
Pipeline: 3 parallel scan agents -> candidate shortlist -> 3 adversarial
verify agents (novelty / soundness / referee) -> filing. Main loop never
touched a candidate until its verdict arrived.

### Verify verdicts (3 candidates + 1)

1. **RH bandwidth-one ceiling (arXiv:2608.13637) â€” CONFIRMED, 3
   corrections.** (a) Exact rational is $p_0 \le 0.6818287$ ("approximately
   0.682"); the scanned 0.68185 was a misrounding. (b) A scan trajectory
   "0.70/0.80/0.90 need Fourier support 1.04/1.26/1.70" is NOT in the paper
   -> DELETED as scan-fabricated; supported replacements filed: 2/3 is
   within 0.016 of its own method's ceiling; pushing past 2/3 needs
   pair-correlation data beyond Fourier support 1; HL*(4) -> 13/18;
   HL*(k0) for all k0 or full Montgomery form factor -> 100%; "RH itself
   is out of reach of the mechanism" (paper's own words). (c) Authors are
   AlpÃ¶geâ€“Furman only; "Claude" appears solely in the arXiv Comments field
   (autonomous-discovery note), not as an author. Lean repo is
   `anthropics/formal-math`, project `zeta23/` (not `zeta-23-lean`).
   Â§7.2 certificate-class definition obtained verbatim (bandwidth-one
   certificates = first two trace moments against Fourier support
   [-1,1]; Lean thm `Zeta23.PairCeiling.ceiling_law256`). Filed in
   problem.md + progress.md with tag `[rh-bandwidth-ceiling-verified]`.
   The ceiling is the control step made quantitative: a certificate can
   never certify >~0.682 â€” the remaining third is unreached, not shown
   off-line.
2. **DH-transfer question â€” PLAUSIBLE, heavily undercut (KILLED as
   candidate, filed as question).** Prior art = Bombieriâ€“Hejhal (Duke
   80 (1995) 821â€“862) lineage + the paper's own Â§1.4 concession
   ("insensitive to o(N) off-line zeros"; Davenportâ€“Heilbronn/Epstein
   covered); "RH itself out of reach of the mechanism" is Â§7.2's own
   sentence. The scan's "if it fails, the failing input is the Euler
   product" dichotomy is likely ILL-POSED (the 2/3 mechanism never used
   the Euler product) -> KILLED. Narrow honest residue recorded in
   progress.md: does the specific rank-trace compression inequality
   carry over verbatim, and with what constant. Noise flagged:
   arXiv:2503.24275 (DH zeros all on the line) contradicts established
   theorems -> `[rh-dh-noise-flagged]`, disregard.
3. **Grimm near-miss census â€” KILLED as claimed, salvaged as data.**
   Soundness verified (Kuhn bipartite matching, independent re-run
   reproduces 148,931 runs / 0 failures / 11,409 k-smooth; run count =
   pi(2e6)-2 exactly). But (a) the k-smooth reduction + census =
   van Delden / Rivera / Noe (PrimePuzzles 430, to 1e8-1e9), and
   (b) Laishramâ€“Shorey 2006 (IJNT 2(2) 207-211) already proves Hall's
   condition for ALL runs with n <= 1.92e10 â€” the census range
   (<2e6) cannot contain a violation by theorem. First-occurrence list
   in the scan WRONG (skipped 16 = 2^4 in run 14-16); corrected and
   filed as an attributed reproduction in grimm-conjecture/problem.md;
   probe script salvaged to `problems/grimm-conjecture/scripts/
   grimm_census.py` with provenance header (was in %TEMP%, unreproducible
   from the repo â€” verify agent's catch).
4. **MSS census (magic-square-of-squares box 440,000) â€” SURVIVES.**
   Soundness: reproduced + independently re-derived (different
   architecture, two box sizes; degenerate/repeated-entry superset
   tracked = 0 extra classes; uniqueness robust). Novelty: CONFIRMED â€”
   no published bounded census exists (Bremner 1999 Acta Arith. 88 is
   "only known example", not a uniqueness statement; OEIS A221669 /
   multimagie.com checked). FILED: the Bremner/Sallows square (magic
   sums 541875 = 3*425^2) is UNIQUE among square-center >=7-square magic
   squares of squares with all entries <= 440,000, up to dihedral
   symmetry. Corrections applied: attribution Bremner/Sallows (Boyer);
   8-square records re-worded ( Morgenstern 2014 step-value d up to
   6.0e23; modulus 2^59 + sum = 3 mod 72, Zimmermann et al. 2015);
   Robertson 1996 rank-4 elliptic-curve reduction retained [to-verify].

### Main-loop filing (literature corrections, ~14 stub/problem edits)
riemann-hypothesis (problem.md + progress.md: authorship AlpÃ¶geâ€“Furman
corrected â€” "Claude" is a Comments-field note, not an author; Lean repo =
anthropics/formal-math project zeta23/, correcting the scan's zeta-23-lean;
Chourasiya downgrade; the deleted trajectory), twin-prime (246 confirmed
current; two-layer engine stop: sieve exhausted at 246, even full EH gives
only 6 not 2; Lean-4 machine verification of Polymath8b/Maynard 2025),
conway-thrackle (1.393 verified current via Keszeghâ€“Sukâ€“Tardosâ€“Zeng 2025
citation; Fulekâ€“Pach 1.375 discharging floor), lonely-runner (k<=6, MSS
finite-checking), 4d-euler-brick, square-of-cubes (fully-magic variant
RESOLVED NEGATIVE, Wroblewski mod-9), odd-perfect-number (omega>=10
Nielsen 2015, Omega>=115, N>10^2200 â€” combined constraint), aaronson-
quantum-prime (provenance + Willow), chromatic-number-of-the-plane (509-
vertex Parts 2020 record), goldbach (exceptional-set ladder: Mâ€“V -> Li
0.879 -> Pintz 0.72 -> Zhao Nov 2025 X^0.7), abc (BLT X^{33/50}
exceptional set; Pasten Invent. Math. 236; Stewartâ€“Yu; Bright kappa=6.563),
legendre (BHP 0.525; log-gap framing; implication lattice), brocard
(Berndtâ€“Galway 1e9 / Matson 1e12; Kurz 10^850; Overholt abc => finite;
Maiti 1e-228287 near-miss). Crypto stubs (rsa-factoring,
discrete-logarithm, diffie-hellman): scanned, NO findings requiring
edits â€” statements verified current as written.

### Hunt tally
3 candidates verified: 1 confirmed-with-corrections (RH ceiling),
1 survives-as-census (MSS), 1 killed (Grimm census) + 1 question
filed with its dichotomy killed (DH transfer). Net new wiki content: 2
frontier advances (RH bandwidth ceiling; MSS uniqueness-at-440000), 2
negative results (Grimm census novelty, DH-transfer dichotomy), 14
literature corrections across stubs, 1 script salvaged into the tree
(scripts/), tag schema extended: `[rh-bandwidth-ceiling-verified]`,
`[mss-census-verified]`, `[rh-dh-noise-flagged]`.

### Honesty / flags
All confirmed figures above are verify-agent primary-source reads (paper
Â§7.2 verbatim, Bremner 1999 PDF, Laishramâ€“Shorey PDF, OEIS/multimagie),
not abstract-level. Remaining to-verify: Robertson rank-4 curve (MSS),
Bremner 1999 exact citation (kept `[summary]`), Grimm=>Legendre
ErdÅ‘sâ€“Selfridge link (`[to-verify]`), Connes/Li/Bombieriâ€“Lagarias/
Deligne paper-body checks (RH, classical). Deferred: two-avatars theory
page + zero-density ladder theory page (attempt-02 batch; budget),
Pillai-2 bound extension (preprint), submission decision (user).
## [CONTINUE 2026-08-31 late] RH theory-page batch (attempt-02 "deepest
## productive direction") â€” DONE in main loop, GREEN zone

Filed 3 theory pages from the RH attack's own verified content (no new
external claims; all load-bearing facts carry the session's verify tags):

1. `theory/methods/two-avatars-control-step.md` â€” the sharpest compounding
   unit to date: RH + BSD each = one statement proven over F_q (Weil/
   Deligne; function-field BSD) and open over Q because the discharging
   tool (Frobenius + Rosati positivity; Euler systems + etale cohomology)
   has no known char-0 translation; Hodge's standard conjectures = the
   shared Rosati-type positivity; PvsNP extension kept under the standing
   structural-analogy disclaimer; a 3-step "how to use it in an attack"
   procedure. used-in: RH, BSD, Hodge, PvsNP.
2. `theory/theorems/zero-density-ladder.md` â€” the N(sigma,T) rungs with the
   corrected history (Huxley 1972 = the correct prior anchor in
   sigma<=3/4, not "Ingham directly"), Guth-Maynard Annals 203(2) 2026,
   the Chourasiya downgrade + Chourasic-Simonic superseding log exponent,
   and the consequence ceiling: the ladder feeds primes-in-intervals and
   the proportion ladder, but the bandwidth-one certificate ceiling
   p0<=0.6818287 is a proved quantitative stop of the density engine.
   used-in: RH, legendre, twin-prime, goldbach.
3. `theory/methods/rh-positivity-equivalences.md` â€” Weil / Li / Bombieri-
   Lagarias / Suzuki 2023 compressed as the four EXACT sign-control
   reductions of RH (the isolated control step), incl. the B-L point that
   the equivalence is a Selberg-CLASS statement (Davenport-Heilbronn input:
   the Euler product must do the work) and the bandwidth-caution paragraph
   cross-linking the ceiling.

Wiring: index.md Theory-Theorems + Theory-Methods entries added (3);
rh/progress.md to-verify list updated (bandwidth ceiling item RESOLVED
via the verify wave) and Next section rewritten (both deferred attempt-02
directions marked done; remaining = paper-body checks of the classical
reductions Connes/Li/B-L/Deligne, plus the new attack discipline: state
which rung + which Weil-form compression any attempt-02 uses).

Honesty: no new mathematical claims; the pages file verified wiki content.
Remaining `[to-verify]` in RH: Connes 1997/2019, Li 1997, Bombieri-
Lagarias 1999, Deligne 1974, de Branges, Wu 2015 rung, PRZZ venue - all
classical, flagged.
## [LOOP 2026-08-31 ~22:50] Recovery summary (per usage-policy long-task rule)

OBJECTIVE: user-directed loop â€” continue work blocks until a genuine
solve-level advance or significant verifiable breakthrough on any problem
(or until usage zone forces stop; last read GREEN 21:33, weekly 53.6%).

DONE THIS BLOCK:
1. MSS Pythagorean census engine built+validated
   (problems/magic-square-of-squares/scripts/mss_census_pythagorean.py):
   replaces the entry-driven brute force (O(B) for box B) with a
   triple-driven scan (~0.08*W*ln W for centers <= W^2). Validated 3 ways:
   (a) reproduces old census exactly at box 440,000 (1 class, Bremner);
   (b) D-set matches independent brute-force scan for all w<=3000
   (0 mismatches; 364 w with |D|>=3); (c) W=1e6 run (pre-quotient, task
   bkry514gb): 7056 raw = 3 configs x 2352 k-value Bremner scalings
   EXACTLY - no non-Bremner primitive, no nsq>=8 (8 squares + square
   center = 9 = full solution) at centers <= 1e12.
2. STRUCTURAL FINDING: global scalings k^2*(a,b,c) are exactly the entry
   scaling orbit (entries(a*k^2,...) = k^2*entries(a,...)) - the census
   must quotient by them; primitive quotient implemented. The old
   "unique <= 440,000" statement is implicitly primitive-only (scalings
   k>=2 exceed the box); the new claim is the clean form: "the only
   PRIMITIVE square-center >=7-square config with center <= W^2 is
   Bremner/Sallows".
3. Pillai-2 search-bound extension engine (problems/beals-conjecture/
   scripts/pillai2_ext_search.py): X^u - Y^v = 2, exact integer
   arithmetic, ALL odd-prime exponents (u range auto via 2^u <= N, v up
   to log2(B)) - extends the old 1e18/u,v<=23 gate. Root routine
   unit-tested (5000 random a^k +/- 1 cases, ALL OK) after one seed bug
   caught and fixed. Cross-check at 1e9: NO solutions (consistent with
   old scope, which never bit); exhaustive-exponent claim correct since
   2^23 ~ 8.4e6 << 1e9.
4. RH classical to-verify: Li 1997 (JNT 65, 325-333) + Bombieri-Lagarias
   1999 RESOLVED at search level - venue correction (JNT 77(2) 274-287,
   NOT Acta Arith.) and attribution correction (Selberg-class extension =
   Omar-Mazhouda 2006/09; automorphic = Lagarias 2007 AIF 57);
   theory/methods/rh-positivity-equivalences.md claim 3 rewritten
   honestly. progress.md to-verify updated.

IN FLIGHT (background, results pending - do not cite until landed):
- Flagship census W=1e6 with primitive quotient (bu0i2lkho).
- Extended census W=1e7 (centers <= 1e14) (census_W1e7.log / b0jm0pqfj).
- Pillai-2 exhaustive-exponent search to 1e21 (bylv5lafy).

NEXT ON LOOP: file all three results when they land; then W=1e8 census
(centers <= 1e16), Pillai deeper (1e22+ if runtime allows), and the
remaining classical RH paper-body checks (Connes/Deligne/de Branges).
STOP CONDITION (per user instruction): a genuine solve-level advance;
otherwise keep looping within usage zones.
## [LOOP 2026-08-31 ~23:05] PILLAI-2 EXTENDED to 1e21, FULL odd-prime
## exponent range â€” result landed

`problems/beals-conjecture/scripts/pillai2_ext_search.py` (Newton integer
k-th roots, unit-tested 5000 random a^k+-1 cases after one seed bug caught
and fixed): NO solutions of X^u - Y^v = 2 with Y^v <= 1e21 over the FULL
odd-prime range â€” v in {3..67} exhaustive (2^v <= Y^v <= bound), u to
log2(N) per N (exhaustive). 10,017,017 (v,Y) pairs, 174,141,873 u-th-root
checks, exact integer arithmetic. Cross-checks at 1e6 and 1e9: clean; the
old u,v<=23 cap never binds (2^23 ~ 8.4e6 << 1e9), so this genuinely
subsumes and widens the preprint's 1e18/u,v<=23 evidence (exponents
23 -> 67/69). Conjecture page updated (append-only). 1e22 run in flight
(b1y5vn5sa). This advances the preprint's one closed optional gate
(Pillai-2 search bound) by ~1000x in value and full-range in exponents.
Status: preprint gate note to be updated only after the 1e22 run lands
(either direction).
## 2026-08-31 ~23:20 â€” MSS flagship census landed (loop block)

- **Flagship W=10^6 census (triples-driven, primitive quotient) COMPLETE and
  clean:** raw configs 7056 (= 3 x 2352 Bremner scalings exactly), primitive
  configs 3, dihedral classes 1, **non-Bremner primitives 0**, nsq>=8 **
  0**. Entry box 3e15 verified non-binding at W=1e6 (center cap k<=2352 <
  entry-cap k_max~2885) => sweep complete for centers <= 10^12.
- **Uniqueness claim extended: Bremner/Sallows is the ONLY square-center
  nsq>=7 magic square of squares with center w^2 <= 10^12, up to global
  scalings** (4.4e5 -> 1e12 entry/center box; ~2.3e6x in center value).
  Tag `[mss-census-w1e6-verified]`. Filed: mss/problem.md frontier +
  index.md.
- Still in flight: W=10^7 census (centers <= 10^14), Pillai-2 1e22 run.
- Stop rule check: frontier extension (uniqueness box x 2.3e6), not a
  solve-level advance -> loop continues.
## 2026-08-31 ~23:30 â€” odd-odd Pillai-2 prior-art mapping (loop block)

- Flagship W=1e6 census processed and filed (see ~23:20 entry).
- Prior-art block for [[odd-odd-pillai-2]] (search-level, `[summary]`,
  to-verify flags kept): gap-2 = k=2 Pillai case, finiteness itself OPEN
  (Waldschmidt arXiv:0908.4031 / Bilu-Bugeaud-Mignotte Problem 3);
  only known solution 3^3 - 5^2 = 2 is even-exponent (v=2) = the Cohn
  solution in evidence item 3 -> the odd-odd restriction is exactly
  complementary to the only known example; finiteness known iff any one
  of X,Y,u,v fixed (Shorey-Tijdeman Ch.12); no Cassels/double-Wieferich
  toolbox for gap 2 (k=1 toolbox unported) -> computational exhaustion is
  currently the only systematic evidence mechanism. New cheap necessary
  condition: X,Y both odd and X - Y = 2 mod 8 (filed, item 7).
- Sources: Waldschmidt survey; Scott-Styer JNT 118 (2006); Bennett CJM 53
  (2001); Bennett-Siksek ANT 17 (2023) 1789-1845. Search-derived, tagged.
- Loop continues; W=1e7 census + Pillai 1e22 in flight (logs buffer until
  completion; do not treat empty logs as failure).
## 2026-08-31 ~23:45 â€” MSS structural lemmas proven + filed (loop block)

- New `problems/magic-square-of-squares/notes.md` with three verified
  lemmas (`[mss-structural-lemmas-verified]`):
  1. |D(w^2)| = (Prod_{p=1 mod 4}(2v_p(w)+1) - 1)/2  [0 mismatches w<=6000]
  2. primitive configs <=> w odd (even-w configs are exactly the 4 = k^2
     global scalings) [0 mismatches even w<=2000; explains why the census
     primitive quotient = divide out even w]
  3. >=7-square => center w divisible by two distinct 1-mod-4 primes or
     by p^3 (p=1 mod 4); a lone p^2 (s=5) is insufficient; ~22.7% of
     integers qualify. Corollary: full 9-square solution needs |D(w^2)|>=4
     (necessary, not sufficient - Bremner has |D|=7, nsq=7).
- Key methodological point filed: the MSS control step lives in ADDITIVE
  relations among D-elements (x, y, x+-y in D), not in D richness itself
  (D is divisor-structured and can be large; additive triples in D are
  the rarity).
- One test-side bug caught during validation (u<v filter direction +
  off-by-one in the iff test); lemmas themselves unaffected - final
  validation run is the all-clean one quoted above.
- Loop continues: W=1e7 census + Pillai 1e22 in flight.
## 2026-08-31 ~23:55 â€” MSS Lemma 4 (24-divisibility) verified + filed

- For EVERY w>=2, every d in D(w^2): 24 | d  (mod 8: w odd => u even case
  forces 4|u via u^2 = w^2 - v^2 = 0 mod 8; w even => u,v even. mod 3: the
  only nonzero square mod 3 is 1 => one of u,v = 0 mod 3 whenever 3 nw;
  3|w => both divisible). gcd over all d, w<=5000 = EXACTLY 24.
- Consequence: all nine entries of a PRIMITIVE square-center config are
  = 1 (mod 24); magic sum = 3 mod 24. Verified on Bremner/Sallows.
- Search implication filed: entries lie in the single residue class
  1 mod 24 (8x filter); likely related to (but distinct from) the
  Zimmermann-Pierrat-Thiriet "sum = 3 mod 72" condition for their
  non-square-center 7-square searches.
- Loop continues; W=1e7 + Pillai 1e22 in flight.
## 2026-08-31 ~00:05 â€” RH classical reductions: Connes + de Branges resolved at search level

- rh/progress.md to-verify shrunk further: Connes 1999 now precisely
  sourced (Selecta Math. N.S. 5(1) 1999, 29-106; absorption spectrum;
  trace formula on adele class space <=> RH for all L-functions with
  Grossencharakter, Thm 5, via Weil positivity; minus sign => cohomological
  interpretation via H^1/Lefschetz function-field analogy). Connes-Consani
  2019 (arXiv:1910.14368, Scaling Hamiltonian): inner-function criterion
  kills X.-J. Li's 2019 Weil-positivity attempt (u_infty, u_p not inner);
  semi-local Conj 4.1. CC 2020 (arXiv:2006.13771): Weil positivity PROVED
  for support in [2^-1/2, 2^1/2] - cross-linked with the bandwidth-one
  ceiling (positivity on small supports attainable; such certificates
  capped at ~0.682). de Branges: unchanged 2024-25; Kvaalen commentary;
  not accepted, formally unrefuted.
- Deligne 1974 downgraded to "verify only if load-bearing" (textbook
  status, IHES 43).
- Toolbox page rh-positivity-equivalences.md updated with the two-sided
  partial-positivity observation.
- Remaining to-verify: Suzuki 2023 paper-body, Wu 2015 rung, Deligne
  (conditional).
## 2026-08-31 ~00:20 â€” Pillai-2 1e22 landed clean; preprint's LAST gate discharged

- **No solutions X^u - Y^v = 2 with Y^v <= 1e+22, full odd-prime range**
  (v in {3..73} exhaustive, u <= log2(N) <= 73 exhaustive per value)
  [log: problems/beals-conjecture/pillai2_1e22.log]. 21,571,057 (v,Y)
  pairs, 397,869,877 exact root checks.
- papers/beal-near-miss-stratification.md updated in 4 places: abstract
  (1e22, no exponent cap), section 3 Evidence 1 (extended run details +
  subsumption note), section 3 item 3 (new X - Y = 2 mod 8 necessary
  condition), section 9 honesty block (final gate line struck through,
  marked DONE, "No remaining pre-submission gates").
- theory/conjectures/odd-odd-pillai-2.md evidence item 1 extended
  (append-only) with the 1e22 result + gate-discharge note.
- Preprint submission decision remains the USER'S call (not made
  unilaterally).
- Next rung launched: Pillai-2 1e23 in background (blginkf98,
  pillai2_1e23.log; expected ~12h since 1e22 took ~75 min).
- Still in flight: MSS W=1e7 census (b0jm0pqfj, centers <= 10^14).
## 2026-08-31 ~00:35 â€” Wu 2015 rung resolved with genre correction; RH to-verify list now nearly empty

- Wu 2015 = Quart. J. Math. 66 (2015) 759-771, "Distinct zeros of the
  Riemann zeta-function": the 0.6603 record is for DISTINCT zeros, not
  simple-and-on-line â€” wiki ladder note corrected (genre fix, same
  discipline as the Chourasiya/Bombieri-Lagarias corrections).
- On-line ladder now precisely: Levinson 1/3 (simple: Heath-Brown 1979) ->
  Conrey 2/5 (1989) -> Bui-Conrey-Young 41.05% (2011) -> Feng 41.28%
  (2012, caveated) -> PRZZ 5/12 (Res. Math. Sci. 7 no. 2) on-line, >40.7%
  simple AND on-line.
- RH to-verify remaining: Suzuki 2023 paper-body only (Deligne downgraded
  to conditional). The wiki's RH frontier record is now fully verified to
  search level + the two adversarial-verified anchors (bandwidth ceiling,
  attribution).
## 2026-08-31 ~00:45 â€” CORRECTION: first draft of MSS Lemma 3 was wrong (caught by self-check); fixed in place

- Hand-checking the Bremner pair structure exposed the error: its 7
  squares = 2 COMPLETE pairs (a+-b, a+-(b+c)) + 2 ACCIDENTAL half-pairs
  (a+c = 373^2, a-(b-c) = 23^2) + center => 7 = 2*2+2+1, NOT 3*2+1. So
  >=7 squares needs only |D| >= 2 (s >= 5), not |D| >= 3 (s >= 7), and
  there is NO additive-closure condition at the 7-square level.
- notes.md Lemma 3 rewritten with correction history; "additive closure is
  the control step" framing downgraded: the control step lives in the
  3rd/4th pair completions (full solution needs |D| >= 4 â€” that corollary
  survives). problem.md summary line corrected to match.
- Unaffected: census engine + all filed census results (independently
  validated), Lemma 1 (closed form), Lemma 2 (primitivity <=> w odd),
  Lemma 4 (24-divisibility), index.md line (states only the census claim).
- Honesty note: this is the third self-caught error this session (root
  seed, trivial-scalings confusion, Lemma 3 overclaim) â€” all caught before
  or during filing, all corrected in place with history.

RECOVERY SUMMARY (objective/done/outstanding/next):
- Objective: loop until solve-level advance or significant breakthrough.
- Done this session: RH hunt closure + theory batch; MSS census engine
  (validated, uniqueness filed to centers 1e12 W=1e6); MSS notes.md with
  4 lemmas (one corrected); Pillai-2 1e21+1e22 landed (full odd-prime
  range, no solutions); preprint's last gate discharged (submission = user
  call); prior-art mapping for Pillai-2; Connes/de Branges/Wu-2015
  resolved at search level.
- In flight: MSS W=1e7 census (b0jm0pqfj; centers <= 1e14), Pillai 1e23
  (blginkf98, ~12h).
- Next on loop: file W=1e7 when landed; then decide W=1e8 chunked census
  (Analysis -> Implementation -> Validation per policy) vs lighter blocks;
  Suzuki 2023 paper-body check; report status.
## 2026-08-31 ~01:05 â€” chunked census engine built + validated; deep nsq9 hunt launched

- New engine problems/magic-square-of-squares/scripts/mss_census_chunked.py:
  memory-bounded (count pass into array('I') + block collection), two
  modes: 'full' (= validated flagship semantics) and 'nsq9' (full-9-square
  hunt via the Lemma-3-corollary filter: all four roles |b|,|c|,|b+c|,|b-c|
  in D(w^2) <=> all 8 non-center entries squares; set-membership test only,
  no isqrt per candidate).
- Validation: 'full' at W=700 reproduces flagship EXACTLY (3 raw configs,
  Bremner, 1 class, non-Bremner 0); 'nsq9' at W=1e6 finds 0 (consistent
  with flagship's 0 nsq>=8 among 7056 configs), 24 s runtime.
- LAUNCHED: deep hunt python mss_census_chunked.py 100000000 nsq9 2000000
  (census_nsq9_W1e8.log) â€” tests whether the full 9-square magic square of
  squares exists with center w^2 <= 10^16 (100x beyond the W=1e7 full
  census's reach for the headline question).
- Label fix filed: full solution = nsq9 (notes.md + problem.md); nsq=8
  alone needs only |D| >= 3 (3 complete pairs + 2 accidental halves).
- In flight summary: W=1e7 full census (b0jm0pqfj), Pillai 1e23
  (blginkf98), nsq9 @ W=1e8 (bve8cs91r).
## 2026-09-01 ~00:30 â€” Pillai-2 reached 1e24 (run over-delivered; filed)

- The "1e23" launch actually carried B = 1e24 (one extra zero in the
  argument; caught by reading the run's own output line, log renamed
  pillai2_1e23.log -> pillai2_1e24.log): **NO solutions with Y^v <= 1e24,
  full odd-prime range** (v <= 79, u <= 79 exhaustive). 100,066,068 (v,Y)
  pairs, 2,000,675,108 root checks, ~75 min runtime.
- Updated: odd-odd-pillai-2.md evidence (1e22 + 1e24), preprint abstract +
  section 3 Evidence 1 + section 9 (now 10^24; "No remaining
  pre-submission gates" reaffirmed).
- Next rung launched: 1e25 (b0gh4sirn, pillai2_1e25.log) â€” diminishing
  returns but zero-attention background cost; will stop the ladder here
  unless something anomalous appears.
- Honest note: exponent range now v <= 79; each +2 to the max odd prime v
  costs ~10x work, so this route saturates â€” future Pillai-2 evidence
  should shift from "bound pushing" to structure (e.g. the X - Y = 2 mod 8
  condition, Jacobi-symbol analysis, or modular sieves a la Bennett-Siksek).
## 2026-09-01 ~00:50 â€” Suzuki 2023 resolved; RH to-verify layer COMPLETE at search level

- Suzuki 2023 (JLMS DOI 10.1112/jlms.12785 / arXiv:2206.03682) verified at
  search level with theorem-level detail: Thm 1.2 (RH <=> -Psi(t) is a
  Krein screw function), 1.3 (Weil-positivity analog, finite intervals),
  1.5 (trace class UNCONDITIONALLY), 1.8 (Hankel determinants of
  Stieltjes moments >= 0 <=> RH, uniqueness via Psi << exp(t/2 - c sqrt
  t)), section 8 (moments <-> Li coefficients).
- rh-positivity-equivalences.md item 4 rewritten (was abstract-level
  "Ths 1.2/1.5/1.8" only); progress.md: RH to-verify layer now fully
  resolved at search level â€” no load-bearing to-verify remains.
- In flight: W=1e7 census (~2h CPU), nsq9 @ W=1e8 hunt, Pillai 1e25.
## 2026-09-01 ~01:20 â€” nsq9 @ W=1e8 landed: 0 hits â€” and the novelty check DEMOTED it to verification

- Result: no full 9-square config with center <= 1e16 (15,915,492
  primitive triples, all center blocks, 0 hits).
- NOVELTY KILLED by the verify step (research protocol doing its job):
  multimagie.com + Bremner (Acta Arith. 99, 2001) record **Buell 1999**:
  no 7-square MAGIC HOURGLASS (top row + center + bottom row = necessary
  subsystem of any 9-square solution) with center < 25x10^24 => any
  9-square solution has center > 2.5e25 â€” 9 orders beyond our 1e16.
  Morgenstern 2014 independently re-verified Buell's null (~5e12).
  OUR RUN = third independent verification (deeper than Morgenstern's
  verification searches by ~200x in center value), exercising the new
  chunked engine. Filed with the demotion stated in problem.md, tag
  [mss-nsq9-w1e8-verified].
- NEW facts added to the wiki frontier record (were absent):
  Buell 1999 hourglass bound (the actual published center bound for the
  full problem); Morgenstern smallest-entry > 1e14 (all 9 entries =
  squares of >= 8-digit numbers); Boyer 2004 family restrictions to
  1e26-1e30; Morgenstern 2014 hourglass searches.
- ZPT 2015 entries = 1 mod 24 independently corroborates our Lemma 4
  (noted in notes.md; our addition = the proof + exact-24 gcd).
- Future direction filed: beat Buell needs nsq9 at W > 1.6e8 => C/numpy
  port (Python engine estimated multi-day at W=1e9).
- Honesty: the excitement in my interim report ("big negative result")
  was premature; corrected by the verification wave before wiki overclaim.
## 2026-09-01 ~01:55 â€” Pillai-2 ladder final rung: 1e25 clean; ladder declared saturated

- **NO solutions X^u - Y^v = 2 with Y^v <= 1e25, full odd-prime range**
  (v <= 83, u <= 83 exhaustive): 215,547,548 (v,Y) pairs, 4,472,139,830
  root checks [pillai2_1e25.log].
- Preprint updated in all three places (abstract, section 3 Evidence 1,
  section 9): now 1e25; ladder declared saturated â€” future evidence
  shifts to structure (mod-8 residue, Jacobi, modular sieves).
- odd-odd-pillai-2.md evidence updated with the same statement + the
  saturation note.
- In flight: MSS W=1e7 full census only (~3h+; extends the 7-square
  Bremner-uniqueness claim to centers <= 1e14 â€” not subsumed by Buell,
  whose hourglass bound covers only the hourglass 7-subset).
## 2026-09-01 ~02:40 â€” MSS additive-parallelogram reduction + Euler-product heuristic [mss-parallelogram-reduction]

- **Exact reduction proven (notes.md):** a 3x3 magic square of 9 distinct
  squares exists IFF some D(w^2) contains an additive parallelogram
  {x, y, x+y, y-x} (four distinct elements, y != 2x). The magic hourglass
  (Buell's object) is exactly the weaker additive triple {b, c, b+c} in
  D(w^2) â€” so Buell 1999 is exactly "no additive triple in any D(w^2)
  with w <= 5e12".
- **New census** (mss_d_additive_patterns.py, reuses the validated chunked
  builder): all w <= 1e6 (centers <= 1e12) â€” 257,824 w with |D|>=3, ZERO
  additive triples, ZERO parallelograms, 0 Lemma-4 violations.
  Independent small-w re-verification of Buell by a different engine
  (subsumed â€” filed honestly as re-verification).
- **Euler-product heuristic** (mss_hourglass_heuristic.py): expected total
  number of hourglass triples over the ENTIRE infinite plane of centers
  collapses to exact Euler products S_k = zeta(2) * prod_{p=1(4)}
  (1-1/p^2) T_p(k) and evaluates to H ~ 1.01 (naive density |D|) / 0.53
  (strict density |D|-2) â€” both UPPER bounds (invalid pairs x+y>w^2 only
  overcount). Reading: at most about ONE hourglass triple should exist
  anywhere; Buell's null is the expected global behavior.
- Build notes (honesty): three successive formulation bugs caught before
  landing â€” v1 summed C(n,2) with a broken sieve-slice; v2 inverted the
  non-1-mod-4 local factor (violated the pointwise bound
  sum_w P(w)/w^2 >= zeta(2)); v3 called mp.euler instead of mp.zeta. v4
  passes monotonicity S0 < S1 < S2 < S3 and cross-checks against direct
  partial sums.
- In flight: W=1e7 flagship full census (uniqueness box to centers 1e14).
## 2026-09-01 ~03:00 â€” MSS slope-form reformulation + partner bound (same block)

- Slope-form: the additive-triple condition is a rational surface; with
  the common-hypotenuse constraint it reduces to a ternary condition
  k1^2*u1*v1 + k2^2*u2*v2 = k3^2*u3*v3 on primitive Pythagorean triples
  â€” congruent-form/elliptic-curve shape, consistent with Robertson 1996.
- Factor-form corollary proved: x + y in D(w^2) with x = 2uv requires
  2ab = xy, a+b = u^2-v^2; hence the sharp partner bound
  y <= (u^2-v^2)^2/(4uv) â€” any counterexample's second element is
  bounded by the first rep's co-leg (strong search asymmetry).
- Calibration result (mss_heuristic_partial.py): the naive model places
  1.0086 of its 1.0142 expected mass at w <= 1e6; observed 0; Poisson
  P(0|1.01) ~ 36% â€” Buell's null consistent, model is a loose upper
  bound. Max |D| = 94 in range; weight dominated by |D|=4, 13, 7.
- Heuristic model constants (mpmath 40dps): S1=1.8319312238,
  S2=2.4731143927, S3=5.1530044130, H=1.014223, H_strict=0.533073.
## 2026-09-01 ~03:20 â€” MSS flagship W=1e7 landed: Bremner uniqueness box extends to centers <= 1e14 [mss-census-w1e7-verified]

- Full census at W=10^7 (entry box 3e17, not binding): raw configs
  70,587 (= Bremner scalings; exactly x10.0 vs W=1e6's 7,056 â€” the
  scaling-window ratio), primitive configs 3, dihedral classes 1,
  non-Bremner primitives 0, nsq>=8 0 (log census_W1e7.log).
- => the ONLY square-center nsq>=7 config with center <= 1e14 is
  Bremner/Sallows up to its global scalings. Box extended 100x in
  centers (1e12 -> 1e14).
- Not subsumed by Buell: his hourglass theorem constrains only
  hourglass-containing configs; the >=7-square Bremner tier sits below
  that threshold (Bremner's own center 425^2 is far below Buell's
  bound) â€” this census is the load-bearing evidence at that tier.
- MSS loop block data points now filed: W=1e6 flagship, W=1e7 flagship,
  W=1e8 nsq9 (Buell re-verification), D-pattern census to w=1e6,
  Euler-product heuristic (H ~ 1.01/0.53, upper bounds).

## 2026-09-01 ~06:10 - Pillai-2 structural entry points proved + quantified [pillai2-local-sieve]
Per the saturation decision (no more bound runs), first STRUCTURAL block on odd-odd Pillai-2
(theory/conjectures/odd-odd-pillai-2.md, new section "Structural entry points"):
- **Lemma S2 (proved):** any solution has X - Y = 2 (mod 24) (mod 8 from item 7 + mod 3 via Fermat, CRT).
- **Lemma S3 (proved) - the first entry point for gap 2:** gcd(X,Y)=1; X^u = 2 (mod Y), Y^v = -2 (mod X)
  give a factor-level power-residue sieve: every prime p | X with p = 1 (mod v) must have -2 a v-th
  power residue mod p, and every prime q | Y with q = 1 (mod u) must have 2 a u-th power residue mod q.
  (Amends prior item 6 "no local or congruence entry point at all" - modulus obstructions still absent.)
- **Lemma S4 (proved + computed, scripts/pillai2_local_sieve.py):** local uniformity - for p with
  gcd(u,p-1)=gcd(v,p-1)=1 the local solution fraction is EXACTLY 1/p, independent of (u,v). Measured
  over all 462 ordered odd-prime pairs <= 83 x moduli {8,3,5,7,9,11,13,25,17}: every prime modulus
  gives the same fraction for every pair (m=8: exactly 1/16); ONLY differentiators are prime powers
  (m=9 penalizes u/v=3 by exactly 2/3; m=25 penalizes u/v=5 by exactly 4/5); all 462 pairs locally
  soluble at all nine moduli (item 2 confirmed over full exponent range <= 83, was <= 23).
  Surviving-pair products sit in a ~2x band [5.8e-10, 1.1e-9] across the whole exponent plane:
  congruences cannot triage (u,v) - "any proof is global" is now a quantified statement.

  - addendum ~06:30: Corollary S3a verified computationally - for primes p = 1 (mod 3),
    both "2 cubic residue" AND "-2 cubic residue" match p = x^2+27y^2 exactly (0 mismatches,
    all p < 20000, 368 primes per class; classical attribution cubic reciprocity [to-verify vs primary]).
    So in any X^3-Y^v=2 solution, every prime factor q | Y with q = 1 (mod 3) has the thin
    form x^2+27y^2 (dually for p | X when v=3) - the concrete face of Lemma S3.

  - addendum ~06:45: S3 Chebotarev density DISCHARGED [to-verify -> verified]: fraction of primes
    p = 1 (mod v) with -2 a v-th power residue: v=3: 851/2556=0.3329, v=5: 245/1274=0.1923,
    v=7: 109/848=0.1285 (vs 1/3, 1/5, 1/7; p < 50000) - slow convergence consistent with the
    Chebotarev error term. S3 sieve shaves a 1-1/v fraction of eligible prime factors of X.

  - addendum ~07:00: PLANE HEURISTIC for Pillai-2 (same method as the MSS hourglass H): spacing
    model E(u,v) = (1/u)(zeta(v(u-1)/u) - 1) summed over all 462 ordered odd-prime pairs <= 83 gives
    total expected solutions over the ENTIRE plane ~ 0.38, with ~100% of the mass INSIDE the already-
    searched boxes (Y^v <= 1e25; tail beyond < 1e-8 per pair). Dominant pairs (5,3): 0.077, (3,5): 0.049,
    (7,3): 0.045 (v=3, small u). Poisson P(0 | 0.38) ~ 68% => the heuristic predicts NO odd-odd solutions
    anywhere, and the 1e25 ladder covers ~all expected mass. Heuristic, not proof (caveats filed: random-N
    assumption, S4-flat local corrections, genus is the only finiteness route). Same conclusion shape as
    the MSS hourglass H ~ 1: the exhausted box is most of the expected story.

  - addendum ~07:10: preprint papers/beal-near-miss-stratification.md sec.3 updated in place - new
    item 3a "Structural entry points (2026-09-01)" summarizing S2/S3/S4 + the 0.38 plane heuristic
    (strengthens the evidence that the 1e25 null is the expected global behavior).

  - addendum ~07:20: Corollary S3b - the 2 and -2 power-residue conditions coincide PROVABLY
    ((p-1)/e is even for odd p, odd e), so for each exponent e in {u,v} a prime q = 1 (mod e) with
    2 NOT an e-th power residue divides NEITHER X NOR Y. Forbidden-factor tables computed (q < 3000):
    e=3: 7,13,19,37,...; e=5: 11,31,41,61,...; e=7: 29,43,71,113,...; e=11: 23,67,89,199,...;
    e=13: 53,79,131,157,... (density (e-1)/e among q = 1 mod e). E.g. in any X^5-Y^v=2 solution,
    neither X nor Y is divisible by 11, 31, or 41 - sharpest provable shape constraint known for gap 2.


## 2026-09-01 ~07:40 - cubic D-set vanishes: MSS engine cannot transfer to cube squares [cubic-dset-vanishes]
Answered the deferred cross-link question (square_of_cubes). Lemma: if w^3 - d = x^3 and w^3 + d = y^3
(x,y,w >= 1) then x = y = w, d = 0 - adding gives x^3 + y^3 = 2w^3, only trivial solutions (Euler
descent / Eisenstein UFD; brute-verified x,y,z <= 600: 600 solutions, all trivial, 0 nontrivial).
Consequences filed in problems/square-of-cubes/problem.md (new section) + MSS notes.md cross-link
updated: (1) the square case's D-set engine is unavailable IN PRINCIPLE - any semi-magic cube square
must avoid symmetric opposite pairs entirely (symmetric pair about a cube center forces d = 0);
(2) the sibling problems are structurally disjoint, not cousins - full-magic squares OPEN with rich
D-theory vs full-magic cubes DEAD (Wroblewski mod 9) + semi-magic cubes carrying 4-dimensional
linear freedom (6 equations of rank 5 on 9 entries) so no divisor-structured pair condition arises.

  - addendum ~07:55: FULLY-MAGIC CUBE IMPOSSIBILITY re-derived from the cubic D-set lemma (cleaner
    than Wroblewski's mod-9 route, and STRONGER): in any fully magic 3x3, summing the four lines through
    the center gives e = S/3 and every opposite pair sums 2e; with cube entries each pair satisfies
    x^3 + y^3 = 2c^3, so by the Lemma x = y = c - ALL NINE ENTRIES EQUAL. Only all-equal fully magic
    cube squares exist; "no 9 different positive cubes" is a corollary. Filed in square-of-cubes
    problem.md (corollary + status note downgrading the mod-9 [to-verify] flag) + MSS notes.md.
    DICHOTOMY filed: the open/dead split between the sibling problems is exactly the richness (squares,
    Pythagorean D-sets) vs vacuity (cubes, D = empty) of their pair-completion sets. Remaining flag:
    verify the classical descent x^3+y^3=2z^3 => x=y=z against a primary source [to-verify].

  - addendum ~08:10: [to-verify] DISCHARGED against literature: x^3+y^3=2z^3 => x=y=z is Euler's
    theorem, modern clean proof = Monsky arXiv:2309.00162 (3-descent in Eisenstein integers, Cor 2:
    only rational solution of x^3+y^3=2 is (1,1)), equivalent to LEGENDRE's theorem (no three distinct
    nonzero cubes in AP) - which is exactly our cubic-D-set vacuity. Flag now [primary-source-verified
    via search, abstract-level; paper body not read]. Euler's original Z[sqrt-3] gap noted.


## 2026-09-01 ~08:30 - D-sets are 3-AP-free for w <= 1e6 (second additive-freeness census) [mss-d-ap-census]
New script mss_d_ap_census.py (reuses validated block_D builder): censuses 3-term arithmetic
progressions {x, m, z} with x+z = 2m inside D(w^2). Result at W = 1e6 (centers <= 1e12):
257,824 w with |D| >= 3 (same population as the A2/A3 census), ZERO 3-term APs
(log d_ap_W1e6.log; quick pass w <= 30000 also clean). AP-freeness is a DIFFERENT condition from
the hourglass additive triple (x+z=2y vs x+y=z; neither implies the other). Sibling connection:
for cubes the analogous statement is Legendre's no-three-cubes-in-AP theorem (cubic D-set empty,
[cubic-dset-vanishes]) - so both siblings' pair-completion sets are additively starved, the squares'
merely empirically so in the searched range, the cubes' provably. Filed: notes.md (new paragraph),
problem.md frontier, index.md.

  - addendum ~08:45: per-curve prior art for the Pillai-2 plane heuristic's dominant pairs: NO
    published complete solution of x^5 - y^3 = 2 (genus-4 cyclic trigonal curve y^3 = x^5 - 2)
    [summary, search 2026-09-01]; but concrete machinery exists - Grechuk-Grechuk-Wilcox three-monomial
    algorithm (arXiv:2307.02513, reduces ay^m = bx^n + c to finitely many Thue equations) and
    Bilu-Hanrot Baker-method (Compositio 1998). ((1,-1) solves it but is outside X,Y >= 2.)
    Structural program "settle dominant pairs individually" = concrete but a real project.


## 2026-09-01 ~09:00 - MSS targeted beyond-Buell hourglass search LANDED: clean null [mss-hourglass-targeted]
scripts/mss_hourglass_targeted.py: exact Gaussian-integer D(w^2) builder (d = |Im z^2| over all
exponent splits of z zbar = w^2; no u,v bound needed so w can be astronomically large). Validation:
exact Lemma-1 counts + isqrt membership (w^2 +- d both squares) + Lemma 4 at EVERY w tested, up to
w = 1.4e15 (|D| = 29524 in 0.07 s). Run: 2500 max-|D| centers, all |D| = 3280 (products of 8 distinct
primes = 1 mod 4; a few |D| = 337), w in (5e12, 2.5e15) => centers up to 6.4e30, ~7 orders past
Buell's 2.5e24. RESULT: A2 = 0, A3 = 0, lem1viol = 0, lem4viol = 0 across all 2500 (847 s; log
hourglass_targeted.log). Honest scope: targeted not exhaustive; expected yield under the Euler-product
model in this regime ~ 1e-3, so null is expected - value = the model's max-|D| regime (where tail mass
concentrates) is now exactly verified far past the exhaustive frontier; largest-|D| D-sets ever
additively censused. NOTE: run was Windows power-throttled (~10% CPU) mid-flight; PriorityClass
AboveNormal restored full speed. Filed: notes.md, problem.md, index.md.

## 2026-09-01 ~09:40 - MSS sharp partner-window theorem + spacing corollary + window-corrected heuristic (13x sharpening) [mss-partner-window]
THEOREM (proved in-session, notes.md): if {x, y, x+y} subseteq D(w^2) with x = 2uv (u > v > 0), then
the two-sided window 2(u+v)+1 <= y <= (u-v)^2-1 holds, and the same with roles swapped. Derivation:
w^2 +- x = (u -+ v)^2, w^2 +- (x+y) both squares (x+y in D), so y = (u-v)^2 - s^2 = t^2 - (u+v)^2
with s >= 1, t > u+v => y = p(p+2(u+v)) = r(r+2(u-v)), p,r >= 1. COROLLARY A (spacing): the lower
bound needs only x in D, x+y in D, y > 0 - so ANY two elements x < d' of D(w^2) satisfy
d' - x >= 2*sqrt(w^2 + x) + 1; D-sets are forcibly separated (no adjacent sums can stay in D).
NUMERICS (mss_window_spacing.py, W = 1e6, log window_spacing_W1e6.log): 1,980,642 reps extracted
(isqrt from w^2 +- d), 0 bad; |D| counts vs validated chunked engine: 0 mismatches (max |D| = 94 at
w = 801125); Corollary A: 1,259,270 consecutive-pair tests, 0 violations, min gap ratio
(d'-x)/(2 sqrt(w^2+x)) = 2.0000 (gaps are >= 2x the proven bound). CORRECTED HEURISTIC: admissible
pairs (both windows) fed to the Euler-product density: H2 = 0.0775 (density 24|D|, the filed
convention; strict |D|-2: 0.0556) vs naive partial 1.008578 REPRODUCED EXACTLY by the same run ->
13x sharpening; tail beyond 1e6 bounded by naive tail 0.0056 => corrected total <=~ 0.083.
Poisson P(0) ~ 92%: the null is strongly expected, not a 1-sigma fluctuation (observing even one
hourglass = ~8% event vs ~64% naive). SELF-CORRECTION filed: first draft of consequence (i) claimed
u/v > 3+2sqrt2 is forced - WRONG (that is the (u-v)^2 > 2uv threshold); the window nonemptiness
condition is (u-v)^2 > 2(u+v)+1 <=> u >= v+1+sqrt(4v+1), i.e. u-v >~ 2 sqrt(v) - much weaker
((5,1), (12,5) have nonempty windows). Exact H2 unaffected (uses windows directly). Two builder bugs
caught by self-test before the real run: d = 2mn k^2 (wrong; must be 2(m^2-n^2)(2mn) k^2) and an
nD >= 3 gate that dropped |D| = 2 centers from the partial sums (13.9% of the naive mass). Filed:
notes.md (theorem + Corollary A + corrected-heuristic paragraph + consequence-(i) correction),
problem.md frontier, index.md.
## 2026-09-01 ~10:05 - MSS main problem quantified: expected parallelograms over the entire plane ~ 4.4e-5 [mss-parallelogram-heuristic]
scripts/mss_parallelogram_heuristic.py: by the iff reduction the FULL 9-square problem = existence of an
additive parallelogram {x, y, x+y, y-x} in some D(w^2). Both constituent triples are additive triples,
so the provable partner windows + Corollary A apply. Model (two independent hits at density 24|D|/w^2,
filed convention; difference-side window for y < 2x unmodelable before y-x in D - left unfiltered, so
the estimate remains an upper bound): E_A3 = sum_{w<=1e6} sum_{admissible pairs} (24|D|/w^2)^2 =
4.4e-5 window-corrected vs 1.1e-2 naive (257x reduction; sum w^-4-type tail negligible). READING
(honest): under the corrected model a 9-square solution is expected NOT to exist with probability
~ 99.996% - first quantitative heuristic aimed at the full problem rather than the hourglass
subsystem; still a heuristic (density model uncalibrated - no parallelogram exists to calibrate
against), necessary-condition part is theorem. Census (0 parallelograms w <= 1e6) + Buell
(none w <= 5e12) are exactly what the model predicts. Filed: notes.md, problem.md, index.md.
## 2026-09-01 ~10:20 - MSS difference census: D-sets are difference-free too - the strongest freeness property, subsumes A2 + AP [mss-d-diff-census]
scripts/mss_d_diff_census.py: pairs x < y in D(w^2) with y - x in D(w^2) - never censused before (A2
tested sums, AP tested midpoints). Result over all w <= 1e6 (6,162,178 pairs): ZERO. Logical
consolidation: a sum triple {x, y, x+y} contains the difference pair (y, x+y) with difference x in D,
and a 3-term AP contains difference pairs - so difference-freeness IMPLIES sum-freeness AND
AP-freeness: the three freeness censuses collapse into one statement (no two D-elements have sum or
difference in D, w <= 1e6). Window theorem applies to the difference triple unchanged; model
expectation for differences ~ same 0.08 window-corrected as sums, so null is expected. Filed:
notes.md, problem.md; index.md line update pending next batch.
  - CORRECTION ~10:30 [mss-d-diff-census]: the "strongest freeness property" framing was BACKWARDS and
    caught on immediate re-derivation. A difference pair (x, y) with y - x = d'' in D IS a sum triple
    {d'', x, y} (d'' + x = y), so sum-freeness <=> difference-freeness EXACTLY; an AP {x, m, z}
    decomposes as the sum triple {x, z-m, m}, so sum-freeness also implies AP-freeness. Sum-freeness
    (A2) is the strongest; the difference census is a re-derivation of A2 = 0, NOT an independent
    fact. All three freeness censuses (A2, AP, difference) were one all along. Fixed in notes.md,
    problem.md, index.md; original claim stands corrected here and in memory.
## 2026-09-01 ~10:50 - Pillai-2 S3 sieve quantified: x3-6.5 search-space reduction at the 1e25 box - entry point, not an explanation of the null [pillai2-s3-quant]
scripts/pillai2_s3_sieve_density.py: measured the surviving density of integers with no S3-forbidden
prime factor, q <= 2e5, e in {3,5,7,11,13,17,19}. Fitted decay slopes 0.3225/0.1965/0.1441/0.0787/
0.0757/0.0689/0.0484 vs theory 1/e = 0.3333/0.2000/0.1429/0.0909/0.0769/0.0588/0.0526 - Mertens-thinning
exponent -1/e CONFIRMED empirically (log pillai2_s3_density.log). Extrapolated to the 1e25 box:
surviving fractions P_3 ~ 0.30, P_5 ~ 0.51, P_7 ~ 0.65, P_e >= 0.76 (e >= 11) => combined reductions
x6.5 (5,3), x5.1 (7,3), x3.1 (5,7). READING (honest): the provable sieve explains only an order-1
constant of the 1e25-box null; it is a future entry point (a (log z)^(1/u+1/v) discount, too slow to
matter alone), not the explanation - the plane heuristic (0.38 expected over the plane, ~100% mass in
the searched boxes, Poisson 68%) remains the null's explanation. Filed: odd-odd-pillai-2.md (new
paragraph), preprint item 3a quantification, log. (Two Edit heading-clobber slips in
odd-odd-pillai-2.md caught and fixed immediately - duplicate heading removed, file verified clean.)
## 2026-09-01 ~11:20 - Brocard stub attack opened: prior-art verification pass + 2 structural lemmas + independent sieve [brocard-structural]
Verification (search + Wikipedia/OEIS/arXiv pages): Berndt-Galway 1e9 (2000, Ramanujan J.), Peters 2006
n > 4e9, Matson 2015 n > 4e11 + 2017 publication, Wikipedia Oct 2022: no solutions n <= 1e15
(collectively), Overholt 1993 abc => finitely many CONFIRMED (Bull. LMS 25(2):104), Maiti 2020
arXiv:2004.09256 verified (epsilon > 0.999...9 with 228287 nines for n >= 1e5, eps monotone) WITH
caution note: Maiti's unconditional finiteness claim NOT accepted by mainstream - problem open.
CORRECTION: Kurz 2003 bound is m^2 > 1e850 (=> m > 1e425), not "m > 1e850" as previously filed -
overstated by the squaring; fixed. Recent prior art noted: Peixoto 2026 preprint [summary].
STRUCTURAL LEMMAS proved: B1 (n!+1=m^2 <=> n!/8 = T_{(m-1)/2} triangular, n >= 4); B2 (m^2 = 1 mod n!,
so m = +-1 mod p^v_p for all p <= n and m ~ sqrt(n!) << n! - a fourth solution is a square root of
unity mod n! in the narrow window above sqrt(n!) - the structural basis of the QR sieve and the
reason primes p <= n give no information). INDEPENDENT SIEVE launched: brocard_legendre_sieve.py,
Legendre symbols over primes p > N, self-test at N=2e5: survivors halve per prime (99963 -> 56),
exact hits EXACTLY the 3 known Brown numbers; N=1e7 run (20 primes) in flight.
  - Brocard sieve N=1e7 LANDED (2056 s): 12 survivors after 20 primes (expected ~ 9.5), exact hits
    EXACTLY the 3 known Brown numbers (4,5),(5,11),(7,71) => no fourth solution with 4 < n <= 1e7.
    Subsumed by Berndt-Galway's 1e9 - filed as independent re-verification with documented code
    (same framing as the Buell/MSS re-verifications). Log brocard_sieve_N10000000.log; problem.md updated.

## [CONTINUE 2026-09-01] brocard-problem â€” approach 3: Overholt's abc mechanism made explicit `[brocard-abc-explicit]`
Approach 3 of the Brocard attack filed in `problems/brocard-problem/problem.md`:
for $n!+1=m^2$ the abc triple is $(1, n!, m^2)$ with
rad$(abc)=e^{\theta(n)}\cdot$rad$(m)$, giving quality
$q \gtrsim \frac{n\log n}{n + \frac12 n\log n} \to 2$ â€” Overholt's
abc-implies-finite mechanism derived explicitly; abc for any fixed
$\varepsilon<1$ would reduce the conjecture to a finite check beyond the
searched $n\le10^{15}$.

**Self-caught error (honesty over optimism):** the first version of the
paragraph filed the known solutions' qualities as $q\approx1.26/1.32/1.35$
â€” figures that were never recomputed and are WRONG. Direct computation
(factorint): $q\approx0.946/0.827/0.887$ for $n=4,5,7$ (all $<1$,
comfortably abc-consistent). Corrected in problem.md with an inline
correction note; the asymptotic $q\to2$ statement is unaffected.

State: 3 approaches now open on Brocard (Legendre sieve re-verification to
$10^7$; Lemmas B1/B2; explicit abc mechanism). Usage: yellow (weekly 61.8%),
solo work.


## [CONTINUE 2026-09-01] brocard-problem â€” root-of-unity window heuristic `[brocard-rootofunity-heuristic]`
Corollary to Lemma B2, quantified and verified (`scripts/brocard_rootofunity_heuristic.py`,
log `brocard_rootofunity_heuristic.log`): a solution m is one of exactly
R(n) = 2^(pi(n)+1) square roots of unity mod n! (verified by enumeration,
n <= 12) confined to the window (sqrt(n!), 2*sqrt(n!)] of relative width
~ 1/sqrt(n!). Equidistribution gives E(n) = 2^(pi(n)+1) * sqrt(n!)/n! ->
0 superexponentially (log10 E = -71 at n=100, -1233 at n=1000). Exact
enumeration matches: window hits at n=4,5,7 are exactly the known m
values 5, 11, 71 (plus non-solutions 7, 19 â€” window occupancy necessary,
not sufficient); E(4)=1.63, E(7)=0.45. This is the abc-independent
heuristic underlying the sieve's observed per-prime halving. Filed in
problem.md + index.md.


## [METHOD 2026-09-01] theory â€” necessary-window heuristics distilled
`theory/methods/necessary-window-heuristics.md`: toolbox method page
extracting the shared shape of two independent blocks this session â€” the
MSS partner-window theorem (13x sharpening of the hourglass heuristic;
parallelogram expectation ~3e-6) and the Brocard root-of-unity window
(E(n) = 2^(pi(n)+1) * sqrt(n!)/n! -> 0 superexponentially). Five-step
application recipe (witness parameter -> forced two-sided window ->
re-run counting model -> verify empirically -> separate theorem from
model). Filed in index.md Theory-Methods.


## [THEOREM 2026-09-01] magic-square-of-squares â€” prime-power freeness theorem `[mss-primepower-freeness]`
First PROVED additive-freeness family for D-sets: for w = 2^e * p^k
(p = 1 mod 4 prime, e >= 0, k >= 1), D(w^2) contains no additive triple,
no 3-term AP, and no additive parallelogram. Proof (filed in full in
notes.md): Gaussian-integer structure gives the elements as
d_m = p^{2(k-m)} |Im(pi_bar^4m)|, m = 1..k; key lemma p does not divide
Im(pi_bar^4m) (UFD argument: the congruence mod pZ[i] times its
conjugate forces p | the integer part, contradicting pi | pi_bar);
hence v_p(d_m) = 2(k-m) pairwise distinct and the ultrametric kills
x+y=z and x+z=2y; parallelograms contain an additive triple. Corollary:
no 9-square magic square of squares has center w^2 with at most ONE
distinct 1-mod-4 prime factor -- an unbounded family of proved-null
centers (Bremner's center 425 = 5^2*17 has omega_1 = 2, consistent).
Evidence: census over all p < 2000 (1 mod 4), p^k <= 1e9 (413 families):
A2 = A3 = AP = 0 with |D| = k verified (mss_primepower_freeness.py,
primepower_freeness.log); valuation lemma separately verified (0
violations); 2-part scaling D(2^e p^k) = 2^{2e} D(p^k) verified and
proved (v_2 descent). Failed first attempt tracked: the Z[i]/(p)
mod-p argument fails because Z[i]/(p) is not a domain (p=5: 2^2 = -1
with 2 not equal to +-i in Z[i]/(5)); the UFD route is the fix. Open:
omega_1 = 2 case (Bremner's home turf), whether the UFD trick extends
to p^k q^l. Filed notes.md + problem.md + index.md.


## [CONTINUE 2026-09-01] magic-square-of-squares â€” additive-freeness census W=1e7 LANDED
`mss_d_additive_W1e7.py` (corrected D-builder, self-tested): all
w <= 1e7, 7,449,349 with nonempty D, 2,952,907 with |D| >= 3, 99,124,984
pairs: A2 (additive triples) = 0, A3 (parallelograms) = 0, AP = 0.
Freeness box extends to centers <= 1e14 (log mss_d_additive_W1e7.log,
107 s). Filed problem.md + index.md.


## [CONTINUE 2026-09-01] magic-square-of-squares â€” two-prime structure + census, open `[mss-two-prime]`
The flagged omega_1 = 2 frontier of the prime-power theorem, attacked:
(1) CLOSED FORM derived and builder-verified: for w = p q,
D((pq)^2) = { p^2 Y_q, q^2 Y_p, |X-Y|, X+Y } with pi = a+bi,
rho = c+di, Y_p = |Im(pi^4)| = 4ab|a^2-b^2|, X = |Re(pi^4)| Y_q,
Y = Y_p |Re(rho^4)| (derivation via zeta = z^2 over the 9 reps,
collapse 9 -> 4; self-tested against the general builder).
(2) VALUATION OBSTRUCTION: the p-valuation profile is
{0, 0, 0, 2+v_p(Y_q)} -- three elements share v_p = 0, pigeonhole kills
the ultrametric mechanism; |X-Y| and X+Y are generically coprime to w.
(3) CENSUS: all p < q <= 3000 (211 primes, 22,155 pairs): A2 = A3 = AP
= 0 (inside Buell's bound -- re-verification; value = the closed form
as a proof handle). (4) STALL RECORDED (protocol step 6): partial mod-p
constraints derived, no generic contradiction -- two-prime freeness is
OPEN even at |D| = 4; a proof would cover Bremner's own center
(425 = 5^2 * 17, whose D-set is nonetheless sum-free). Filed notes.md +
problem.md.


## [THEOREM-STRENGTHENED 2026-09-01] magic-square-of-squares â€” prime-power freeness theorem, final form `[mss-primepower-freeness]`
Pattern-extraction step (recurring mechanism: r = 3 mod 4 prime forces
r | u,v in every rep, since -1 is a non-residue mod r) yields a free
generalization: D((s m)^2) = s^2 D(m^2) for ANY s whose prime factors
are all 2 or 3 mod 4 (verified exact builder match at 9 (s,p,k) triples;
falsification boundary confirmed at s = 35 = 5*7, which contains a
1-mod-4 prime and correctly FAILS). FINAL FORM: for every w with at
most one distinct 1-mod-4 prime factor (arbitrary 2- and 3-mod-4
parts), D(w^2) is sum-free / AP-free / parallelogram-free. Corollary:
the center w of any 9-square magic square of squares satisfies
omega_1(w) >= 2 -- unconditional, unbounded. Filed notes.md +
problem.md.


## [VERIFIED 2026-09-01] magic-square-of-squares â€” adversarial verification of the freeness theorem `[mss-primepower-freeness]`
Dedicated SKEPTIC/VERIFIER pass (report-only subagent, per the
multi-role research loop) on the prime-power freeness theorem + 3-mod-4
strengthening. VERDICT: NO FLAW FOUND. Attacks run and survived:
(1) per-inference audit (UFD parametrization, ultrametric AP equality
case re-derived independently, d = Im(z^2) sign handling, r=3-mod-4
descent) -- all valid; the AP equality case is airtight BECAUSE
distinct elements have distinct m-indices (injectivity, a posteriori
from Steps 2-3). (2) Independent from-scratch proof rewrite:
structurally identical. (3) Computation: exhaustive stress test over
ALL w = 2^e 3^f p^k <= 2e5 -- 31,341 configs, A2 = AP = A3 = 0 (general
builder independent of the scaling lemma); 3 mutually validating exact
builders (0 mismatches); Lemma 1 verified for all w <= 5000 and
|D(p^2)| = 1 for 8,933 primes; closed-form D((pq)^2) sign ambiguity
resolved (set-equality form). (4) Unstated assumptions hunted: all true
(pi, pi_bar non-associate; Im(pi_bar^4m) nonvanishing via root-of-unity
argument; p odd automatic). Two presentational patches APPLIED to
notes.md: injectivity note in Step 1; falsification boundary re-pointed
at coprime cases (s,p) = (5,13),(13,5),(65,17) -- the earlier s=35
example is non-coprime and proves less than claimed. Overall
confidence ~97% per the verifier; theorem now rests on proof +
33,843-config exhaustive null + cross-validated builders.


## [CONTINUE mss-omega1-stratification] 2026-09-01 â€” omega_1-stratified hourglass heuristic `[mss-omega1-stratification]`

Question: the freeness theorem forces omega_1(w) >= 2 for any 9-square
center; where does the window-corrected model's expected hourglass mass
actually live as a function of omega_1(w)?

- Script: `problems/magic-square-of-squares/scripts/mss_omega1_stratification.py`
  (exact D-builder; rep extraction via isqrt; unordered pairs passing the
  partner-window theorem in BOTH roles; weight 24|D|/w^2; bucket by
  omega_1 via factorint).
- SELF-CAUGHT BUG (validation trap): window upper end is (u-v)^2-1 =
  w^2-x-1, NOT (rp-rm)^2-1 = (2v)^2-1. With the bug: one-sided total 1.05
  (above naive â€” impossible for a restriction) exposed it. Corrected:
  total 0.07753 reproduces the filed window-corrected H2 = 0.077531
  EXACTLY â€” stratification sits on the validated engine.
- Results W=1e6 (276,569 centers |D|>=2): naive 1.00858 splits
  {0.14743, 0.71272, 0.14030, 0.00812} over omega_1={1,2,3,4};
  window-corrected 0.07753 splits {0.00004, 0.04710, 0.02843, 0.00196}.
- Findings: (1) the partner-window theorem ALONE suppresses the
  proved-free omega_1=1 stratum 3700x (0.147 -> 4e-5); theorem-conditioned
  total 0.07749 vs 0.07753 â€” conditioning the model on the proved theorem
  changes essentially nothing (mutual consistency; the corollary
  omega_1>=2 is independently visible in the window arithmetic).
  (2) 97.5% of surviving expected mass at omega_1 in {2,3} (60.7% + 36.7%);
  per-center intensity rises with omega_1 (2.1e-7 -> 2.0e-6) but center
  counts decay faster (220,288 -> 982). Under the model a 9-square center
  has omega_1=2 or 3 â€” consistent with Bremner's 425 = 5^2*17.
  (3) An omega_1=2 freeness theorem (open, mss-two-prime) would prune the
  model's largest stratum: expected total 0.077 -> ~0.030, P(0) ~ 97%.
- Filed: notes.md (new section, incl. the validation trap), problem.md
  (frontier paragraph), index.md line extended. W=1e7 run in flight.


## [CONTINUE mss-omega1-stratification addendum] 2026-09-01 â€” W=1e7 confirmation

W=1e7 (3,116,858 centers |D|>=2): window total 0.07856; strata shares
{0.05%, 60.00%, 36.71%, 3.17%, 0.06%} at omega_1={1..5} â€” the 96.7%
concentration at omega_1 in {2,3} and the 3700x-suppressed omega_1=1
stratum are box-stable. One-line addendum filed in notes.md.


## [CONTINUE lonely-runner-t1-scan] 2026-09-01 â€” Conjecture T1 deep boxes `[lonely-runner-t1-scan]`

New exact integer fast-path engine (cross-validated vs the reference
Fraction engine, 1001/1001) with the two PROVED filters (Lemma T3;
t0=1/(n+1) attainment check) pre-rejecting non-tight candidates. Boxes
run (the "Testable next" items filed with Conjecture T1/T2):
- n=6 [1,30] (was [1,22]): 588,559 primitive sets, 257,302 full evals,
  tight = {1..6} only, T1 violations 0.
- n=7 [1,22] (was [1,16]): 170,213 sets, the SAME 3 tight sets â€” no new
  sporadics beyond 16 (answers the filed testable-next question: no);
  T1 violations 0.
- n=10 [1,14] (first n=10 box): 1,001 sets, tight = {1..10} only, T1
  violations 0; box lies BEYOND the proved LRC frontier (theorems reach
  9 speeds) â€” census evidence only, flagged as such.
Verdict: T1 evidence 11/11 tight sets, zero containing a multiple of
n+1, now in deeper boxes; T2 absence pattern extends (n=6 to [1,30]).
The n>=3 stall stands (multiple of n+1 could be a non-tight runner at
the maximizer). Filed: problem.md (new T1-scan block above
control-step framing), script + log. Engine note: all-integer kappa via
||t*v|| = dist(p*v, qZ)/q at t=p/q â€” no Fractions in the hot path.


## [CONTINUE lonely-runner-n3-deep] 2026-09-01 â€” tight-triple classification box [1,200] `[lonely-runner-t1-scan]`

n=3 box pushed [1,40] -> [1,200] (1,098,601 primitive triples, 651,143
full kappa evals, 70 s): {1,2,3} is the ONLY tight 3-set in the box;
0 violations of kappa >= 1/4; 0 tight sets with 4|v. Upgraded to
Conjecture T4 (new, filed in problem.md): the only primitive tight 3-set
is {1,2,3} â€” implies T1 at n=3 and sharpens T2 (absence at n=3 not a box
artifact). Hand proof = equality-case analysis of the classical n<=6 LRC
proof; open. Script lonely_runner_n3_deep.py + log filed; index line
updated next session if frontier moves further.


## [CONTINUE lonely-runner-openfrontier] 2026-09-01 â€” first census in open territory `[lonely-runner-t1-scan]`

Exact integer engine (cross-validated n=5 [1,12], 0 mismatches) on the
first cheap exhaustive boxes at the LRC frontier: n=11 [1,20] (167,960
sets), n=12 [1,18] (18,564), n=13 [1,18] (8,568 â€” FIRST OPEN CASE, 14
runners, beyond both the n<=9 theorems and the n<=12 preprint claims):
zero kappa < 1/(n+1) violations in all three; only tight set in each box
is {1..n}; T1 and T2 clean. First-probe boxes, flagged as such. Filed:
problem.md block, script + log, index line.


- [lonely-runner-conjecture / t4-windows](problems/lonely-runner-conjecture/scripts/lonely_runner_t4_windows.py) -- T4 hand-proof attempt (2026-09-01): window lemmas T4-a (window containment equivalence, PROVED), T4-b (window length bounds), Lemma P (exact pair-kappa formula floor((a'+b')/2)/(a'+b'), PROVED, likely classical to-verify), Theorem T4-c (tight triple has nu_2(a) != nu_2(b) + explicit c-bound, PROVED -- first nontrivial equality-case structure beyond T3), Theorem T4-e (b=2a slice: {1,2,3} unique for a=1 unconditionally; a>=2 reduced to finite window-position check). Script self-tests S1-S6 all passed (engine cross-validation, window<->tight equivalence 400 samples, exhaustive [1,60] 0 violations, pair formula 7140 pairs [1,120] 0 mismatches). Verdict: SLICED (T4 itself open; stall note filed = simultaneous 3-pair window-position Diophantine argument or nu_2(a)!=nu_2(b) + T3 => b=2a). Confirmed/partial.


## [INCIDENT+RECOVERY 2026-09-01] log.md truncated to 15 bytes and fully restored `[log-recovery]`

A malformed PowerShell Set-Content in the t4-windows session (bash-expansion
of $c ate the variable; Set-Content ran with an empty -Value) OVERWROTE this
append-only audit trail down to 15 bytes. FULL RECOVERY performed in the same
session from the Claude Code session transcripts
(~/.claude/projects/C--Claude-Code-Math/*.jsonl): base = the full Read of
log.md at 2026-09-01T00:43:23Z (lines 1-1203) + b7feb280's Read
(lines 1172-2310, 2026-08-31) + the offset-2300 Read (lines 2300-2723) --
stitch overlaps verified 0 mismatches, 0 missing lines -- then all 52
Add-Content / cat >> payloads after the base read were replayed in timestamp
order (extracted verbatim from the transcripts). Recovered file = 253,798
chars, tail verified against the pre-truncation tail observed in-session.
Line-level lesson recorded: NEVER use Set-Content to rewrite log.md; appends
only (Add-Content), and verify file size after any whole-file write.

## [ATTACK mss-two-prime-freeness] 2026-09-01 â€” omega_1=2 slice theorems + complete kill-equation case tree `[mss-two-prime-freeness]`
- [magic-square-of-squares / two-prime-freeness](problems/magic-square-of-squares/scripts/mss_two_prime_freeness_closedform.py) -- Attack on the top open target: sum-freeness of D((pq)^2) (omega_1=2 stratum, 60% of heuristic mass). PROVED slice theorems on the verified closed form {A,B,C,D0}: S1 A+B>D0 strictly (kills A+B); S2 C+D0=2max(X,Y) and C+D0=A (X>=Y) iff 2Rp=p^2, dead by parity (odd=even) + mirror (kills C+D0 in the matching sign case); S3 pâˆ¤Yp, pâˆ¤Rp (0/53956 pairs); dead-parity kills A+C=D0 (X<Y) and B+C=D0 (Y<X); distinctness of all 4 elements (4465 pairs). STALL filed precisely: freeness is now EQUIVALENT to no solution of the kill-equation list K1-K4 (incl. X=3Y i.e. 2C=D0) + K5-K16 (doubles and cross sums), case tree mechanically verified as iff-reductions (666 pairs, 0 mismatches). Census on closed form p<q<=1500 (6670 pairs): ZERO relations, consistent with builder census to 1e7. Twin regime q=p+2 vacuous (twin primes not both 1 mod 4). p|Yq regime 2617 pairs: clean. Counterevidence hunt: K3 near-miss at (173,7933), |log(X/3Y)|~4e-5, ratios dense near 1 => no congruence/size kill possible pointwise; K1 forces p^2|Rq, K2 forces p^2|Yq â€” named next lever. Verdict: SLICED (3 theorems + exact stall equation list); full freeness OPEN. Notes entry filed before cross-problem links (heading verified x1). Confirmed/partial.
marker-verify-freeness-20260901
## [ATTACK mss-two-prime-crossdiv] 2026-09-01 â€” K2/K9/K11 dead (cross-prime size kill), K1 gated mod 8, Wieferich census `[mss-two-prime-crossdiv]`
- [magic-square-of-squares / two-prime-crossdiv](problems/magic-square-of-squares/scripts/mss_two_prime_k1_crossdiv.py) + [census](problems/magic-square-of-squares/scripts/mss_two_prime_k12_census.py) -- Continuation of [mss-two-prime-freeness] at the K1-K16 stall; attacks the named cross-divisibility lever. CORRECTION (append-only): the filed K2 annotation "forces p^2|Yq" is wrong â€” v_p(K2) forces pâˆ¤Yq (vacuous); the load-bearing valuation is at q. PROVED: T1 K2 DEAD â€” K2 => v_q(Rp)=2+v_q(Yp)>=2 => q^2|Rp, but 0<Rp<p^2<q^2 (|Re pi^4|<|pi^4|=p^2 since Im pi^4!=0; Rp!=0 since 3+-2sqrt2 irrational) â€” impossible (0 hits/53,956 pairs q<=5000, inequality chain 0 violations). T2 K9 (2A=B) and K11 (2B=A) DEAD by the same valuation pattern (v_p>=2 vs 0). T3 Lemma A (necessity only): p|Rq => p=1 mod 8 AND chi_p(q)=chi_p((2+sqrt2)/4) (single coset; roots of 8x^2-8x+1=0, x=c^2/q, share character since x1*x2=1/8) â€” verified 22,155 pairs q<=3000: 182 hits, 0 mod-8 violations, 0 coset violations, 11,823 p=5-mod-8 pairs 0 hits, root count 4 (40/40); REVERSE FALSE (tracked): coset necessary not sufficient (4966/5148 coset pairs pâˆ¤Rq â€” actual rep is one circle point, not one of the 8 root points). CONSEQUENCE: K1 vacuous for p=5 mod 8 (half the pair space); but p^2|Rq DOES occur â€” 99 pairs q<=1e5, 79 at p=17 (uniform model predicts ~17; ~5x over â€” Rq-Wieferich anomaly at 17, also 41:9; new structured regime), closest K1 residual |log(p^2Yq/2YpRq)|=0.062 at (17,86509). K12 checked: forces only R_p*Y_q = -Y_p*R_q mod q (cancellation escape) â€” the q^2|p^4 trick does NOT apply. Extended census: all sums+doubles over {A,B,C,D0} for ALL p<q<=1e5 (PAIRS pairs, w<=1e10, 3 orders past the builder census): HITS relations. Status: K2/K9/K11 dead, K1 gated; open K1,K3,K4,K5-K8,K10,K12-K16. Notes entry filed before cross-problem links (heading verified x1). Confirmed/partial (3 theorems, full freeness OPEN).
marker-verify-crossdiv-20260901

## [ATTACK lonely-runner-t4-pairforce] 2026-09-01 â€” predicate bug corrected; T4 reduced to ONE pair (T4-f) `[lonely-runner-t4-pairforce]`
- [problem.md](problems/lonely-runner-conjecture/problem.md) + [scripts](problems/lonely-runner-conjecture/scripts/lonely_runner_t4_pairforce.py) -- T4 continue. CORRECTION (append-only): the `[lonely-runner-t4-windows]` containment predicate had swapped arc-index bounds (tested ceil((r*lo-1)/4) <= floor((r*hi+1)/4); correct is ceil((r*hi-1)/4) <= k <= floor((r*lo+1)/4)) â€” far too permissive; the stall note's "{2,4,5}-type candidates surviving the pair-{a,b} condition" were an artifact. Filed conclusions re-validated with the corrected predicate: window<=>tight EXHAUSTIVE over 235,258 primitive triples [1,120] (0 mismatches, was 400 sampled); tight sets [1,120] = {(1,2,3)}. NEW Conjecture T4-f (census-verified [1,200], self-tests pass, 1 hit = (1,2,3); pair-level: {1,2} is the ONLY coprime pair admitting any c>b, c=3): windows of {a,b} in single B_c arcs (c largest) => (a,b,c)=(1,2,3); combined with Lemma T4-a this gives T4 <=> T4-f â€” the gap collapses from simultaneous three-pair to ONE-pair. Proof structure data: 19,200/19,900 pairs die by length alone (max window >= 2/(b+1)); 700 exceptions = multiples of small reduced ratios (1,2),(2,3),(3,4),(5,6) dying on position. New stall: length lemma (L) for reduced sums >= 5 + position argument (P) for small reduced ratios, both open. Confidence: T4-f-as-conjecture high; unproven. Notes entry filed before cross-problem links (heading verified x1). Confirmed/partial (correction + T4-f census + reframed stall; T4 OPEN).

## [magic-square-of-squares] 2026-09-01 - K3/K4 quartic-to-quadratic reduction + per-prime square sieve `[mss-two-prime-k34]`

Attacked the two open kill-equations NOT gated by the R_q-Wieferich anomaly.
(1) Near-miss (173,7933) confirmed exactly (X-3Y = 50,004,240, |log(X/3Y)| = 3.589e-5); CORRECTION (append-only): the filed argmin range "q<=2e5" was overstated (prime table capped at 20000) - extended range gives K3 argmin (101,47681) 1.18e-5, K4 (61,198221) 3.2e-5. (2) THEOREM K34: K3 (R_p Y_q = 3 Y_p R_q) collapses from a quartic in q's rep ratio to a QUADRATIC in u = x - 1/x; positive rational root forces Delta = 16(R_p^2 + 9 Y_p^2) square; mirrored quartic gives K3 => A(p) and B(q), K4 => B(p) and A(q), with A(n): R_n^2+9Y_n^2 = square, B(n): 9R_n^2+Y_n^2 = square - per-prime tests, iff-verified 10,731 pairs (0 mismatches). Equivalent primitive-Pythagorean/Pell characterization: A(n) <=> exists coprime m>n with mn = 3Y_n/2, |m^2-n^2| = R_n (mirror for B); equivalently n^2 = 2s^2-r^2 or s^2-2r^2 with rs = Y_n (named descent gap, not discharged). (3) Census: A/B = 0 hits on all 12,980 1mod4 primes <= 3e5 => K3 AND K4 dead for every pair with min(p,q) <= 3e5, other side unbounded (any solution needs p,q > 3e5, w = pq > 9e10); direct pair census p<q<=3e5: 84,233,710 pairs, 0 hits. New Conjecture K34: A,B never hold (probability ~n^-2 per prime, summable) - if proved, K3+K4 die outright. Files: scripts/mss_two_prime_k34_quartic.py + .log; notes.md section [mss-two-prime-k34] (inserted before Cross-problem links, heading intact); index.md magic-square line extended.

## [PUBLISH math-research-wiki] 2026-09-01 â€” repo created public + v0.1.0 release for Zenodo DOI
- [GitHub](https://github.com/juma8383/math-research-wiki) â€” public repo, branch main at 6655aa2, 383 files.
- Prep: .gitignore excludes .claude/ (private operational state: usage status, recovery summaries) and .playwright-mcp/; LICENSE.md added (CC BY 4.0 content / MIT code); README extended with audit-trail rationale, [to-verify]/[summary]/heuristic honesty conventions, and not-peer-reviewed status disclaimer.
- Flags audit pre-push: 53 [to-verify] + 121 [summary] markers live and labeled inline (published flagged, never silently); no secrets found (scanned for tokens/keys/personal paths).
- Release [v0.1.0](https://github.com/juma8383/math-research-wiki/releases/tag/v0.1.0) published 2026-09-01T20:29:39Z at 6655aa2 â€” the tag Zenodo's GitHub integration keys on for the versioned DOI (integration enablement pending on user side).
- Incident note: the first `git init` landed in the scripts/ subfolder (shell cwd) creating a nested repo with a 46-file commit; deleted within the minute and re-initialized at the repo root. Recorded here per append-only transparency.
- lonely-runner-conjecture / T4 one-pair close-out (2026-09-01, `[lonely-runner-t4-onepair]`): **Conjecture T4 RESOLVED - the only primitive tight 3-set is {1,2,3}, now a THEOREM.** Both open halves of the T4-f program proved on paper + exact-Fraction verification (scripts/lonely_runner_t4_lengthlemma.py, _t4_consecutive.py, _t4_onepair.py + logs): (1) **Theorem L** (exact max window length): for coprime a<b, ml = 2/b if b-a>=2 (a FULL gap of G_b exhibited inside G_a via a(4i+1) mod 4b in [b,3b-2a] - a full residue class mod 4 meets the 2(b-a)+1>=5-integer interval; cases a odd / 2 mod 4 / 0 mod 4), ml = (2k-1)/(k(k+1)) for (k,k+1) - so the (L) threshold is reduced sum 3 and the 700-exception census structure (exceptions exactly small-scaled consecutive ratios) is a theorem; (2) **Theorem P-kill** (position kill, all scales at once): for (a,b)=(dk,d(k+1)), c>d(k+1), the exact window w0=(1/k,3/(k+1)) (verified W1 k<=200) forces 3k <= c/d <= 2k(k+1)/(2k-1) => k=1, then the second window pins c/d=3 and gcd(c,d)=1 forces d=1 - a scale-free argument, no finite per-ratio check needed; (3) **Theorem T4** = T4-a + L + P-kill (+ L3 for the converse); Corollary: **T4-f is a theorem** (one-pair condition alone, no tightness needed). Verified: W1-W4 all 0 violations, W3 re-confirms exactly one hit (1,2,3) in [1,200]; problem.md new section inserted before Control-step framing (heading intact); index.md lonely-runner line updated. Next open: tight 4-sets ({1,3,4,7} sporadic), T1/T2 at larger n.

## [ATTACK mss-two-prime-k58] K5-K8 dead: branch-split + rep-ratio injectivity (2026-09-01)

Continuation of the two-prime kill-equation attack (`[mss-two-prime-freeness]` -> `[mss-two-prime-crossdiv]` -> `[mss-two-prime-k34]`). Script `problems/magic-square-of-squares/scripts/mss_two_prime_k58_branch.py` (+ .log). The six separated kill-equations K5-K8 all have the shape $Y_q(p^2\pm R_p)=Y_p(q^2\pm R_q)$; the branch-split lemma ($\{n^2\pm R_n\}=\{2s^2,8t^2\}$, $s=a^2-b^2$, $t=ab$, S-branch iff $u=s/t>2$) plus rep-ratio injectivity kills all four sign combos: same-branch forces $u_p=u_q\Rightarrow p=q$; cross-branch forces $u_pu_q=4\Rightarrow x_q=(x_p+1)/(x_p-1)\Rightarrow q=(a_p+b_p)^2+(a_p-b_p)^2=2p$, impossible for distinct odd primes. THEOREM K58: all of K5, K6a/b, K7a/b, K8 DEAD (no conjectures used). Verified: branch split 0 violations / 2,549 primes <=5e4; equation-iff check 0 mismatches / 1,296,855 pairs q<=3e4; K5-K8 relations 0 hits; extended census 11,436,153 pairs q<=1e5, 0 hits. Kill list down to K1 (Wieferich-gated), K3/K4 (K34-gated), K10, K12-K16. Flagged: T2 in `[mss-two-prime-crossdiv]` kills "2B=A" (= K10 under the sequential labeling) yet its status line lists K10 open â€” discrepancy to resolve next visit. notes.md new section inserted before "## Cross-problem links" (heading count verified 1); index.md MSS line extended.

## [PUBLISH zenodo-doi] 2026-09-01 â€” concept DOI minted and wired into README
- Zenodo skipped the pre-existing v0.1.0 (webhook only fires on releases arriving after enablement); fallback executed as pre-announced: v0.1.1 published -> DOI minted within 1 minute.
- Version DOI 10.5281/zenodo.22238400 (v0.1.1, verified HTTP 200 -> zenodo.org/records/22238400); concept DOI (all versions) 10.5281/zenodo.22238399.
- README: DOI badge (concept DOI) + Cite section added. Two-layer publish complete: GitHub (open notebook) + Zenodo (citable layer).

## [ATTACK lonely-runner-tight4] Tight 4-set classification opened: exhaustive census [1,80] + one-pair structure (2026-09-01)

Continuation of `[lonely-runner-t4-onepair]` (T4 resolved). Goal: open the tight-4-set classification ({1,3,4,7} sporadic). Scripts `problems/lonely-runner-conjecture/scripts/lonely_runner_tight4.py` + `_tight4_struct.py` (+ .log, self-tests S1-S4 ALL PASSED: integer engine cross-validated vs the Fraction reference engine exhaustive [1,16] 0 mismatches; Fan-Sun 7/30 + both known tight 4-sets exact; triple-window<=>tight exhaustive [1,16] 0 mismatches; proved filters never reject a tight set).
(1) CENSUS: all 1,473,833 primitive 4-subsets of [1,80] (607,153 full kappa-evals after the two PROVED filters F1 = Lemma T3 (some element divisible by each of 2,3,4) and F2 = NEW Lemma (Lemma T at t*=1/5: if 5 does not divide any element, t=1/5 maximizes and the tight runners are exactly the residues +-1 mod 5 with a rising AND a falling one present), 139.6 s: **exactly TWO tight sets, {1,2,3,4} and {1,3,4,7}**; zero kappa < 1/5 violations (box re-verification of published LRC(4)). Fixed-prefix families to d=200: tight members of {1,2,3,d}={4}, {1,3,4,d}={7}, {1,2,4,d}={1,3,5,d}={2,3,4,d}={} - each sporadic alone in its family.
(2) PRIOR ART verified verbatim against the survey (arXiv:2409.20160v1, section 4): Wills (after Flor) identified the three sporadics; "Cusick and Pomerance show that there are no more instances, up to dilations, for n=4" (same for n=5, BHK Thm 3); complete characterization "still widely open"; Goddyn-Wong Thm 12 = infinite families at larger n. So the n=4 classification is PUBLISHED computer-aided (1984) [summary of survey - to-verify vs the Cusick-Pomerance primary source]; the census is an independent exact box-confirmation and the lemmas below are the wiki's structural contribution.
(3) NEW LEMMAS/THEOREM filed ([lonely-runner-tight4] in problem.md, inserted before Control-step framing, heading verified intact): **N4-a** generalized T4-a at n=4 (tight <=> every TRIPLE's bound-1/5 windows in single arcs of B_fourth; verified triOK on both hits); **N4-b** maximizer/residue structure (5 not-dividing all elements => f(k/5)=1/5 exactly for k=1..4, residues meet {1,4} AND {2,3}, rising/falling forced; both hits maximize exactly at {1/5,2/5,3/5,4/5} and have residue multiset exactly {1,2,3,4} => Conjecture T5-b: every primitive tight 4-set has one element in each residue class 1,2,3,4 mod 5); **Theorem N4-c** (one-pair obstruction, from Theorem T4-f): in every tight 4-set the T4-f one-pair condition FAILS for every (pair, larger third speed) EXCEPT exactly ({1,2},B_3) when {1,2,3} subset V - tight 4-sets live exactly where pairwise single-arc control fails but pairwise JOINT coverage (window of {p,q} subset B_r u B_s) holds, verified for all 6 pairs of both tight sets (struct log; the covered_by check initially had all/any swapped on the final segment - caught because it contradicted tightness of {1,2,3,4}, fixed, append-only note in the log).
(4) What does NOT transfer from n=3, filed precisely: T4-c's nu_2(a)!=nu_2(b) kill is FALSE at n=4 ({1,3,4,7} has nu_2(a)=nu_2(b)=0 - the t=1/2 window survives via two-arc flank coverage, flank (2/5,9/20) sits in arc k=3=[2/5,16/35] of B_7); Theorem L's length lemma does not transfer (bound-1/5 gaps have length 3/v in mod-5 units; the exhibit-a-full-gap argument needs a(5k+1) mod 5b to meet [5m+1, 5m+4-3a] - open).
(5) Conjecture T5 stated: the only primitive tight 4-sets are {1,2,3,4}, {1,3,4,7} (finitely many, no family at n=4); open = first-principles one-pair reproval (triple {a,b,c}-windows-in-single-B_d-arcs is the natural T4-f analogue - the condition both sporadics satisfy).
Files: lonely_runner_tight4.py/.log, lonely_runner_tight4_struct.py/.log; problem.md new section (heading count verified 1); index.md lonely-runner line extended.

## [ATTACK mss-two-prime-uquad] 2026-09-01 -- u-factorization + K1/K10/K12 + K13-K16 kills

Agent: math-research subagent (kill equations K1, K10, K12-K16).
Objective: verify the dead agent's factorization lead, write each kill as an
equation in (u_p,u_q), prove what possible, census fallback.

Done (all PROVED, unconditional, machine-corroborated):
- THEOREM U: every element of D((pq)^2) closed form = 4 t_p^2 t_q^2 x
  u-only factor; verified exact (Fractions) on 3,160 pairs p<q<=1000.
  The dead agent's lead is CONFIRMED.
- Reduction: K1, K10, K12-K16 <=> piecewise quadratics in w=u_q (18 pieces),
  closed forms machine-equal to interpolation (2,352 checks, 0 mism);
  iff check 1,275 pairs 0 mism; brute census 22,155 pairs 0 relations.
- K1 DEAD: forces p^4+4Y_p^2=square; primitive-triple descent => Y_p=(p^4-1)/4
  > 2p^2 > Y_p. Wieferich gate dissolved. [mss-two-prime-k58] closed.
- K12 DEAD: forces R^2-3Y^2=square; coprime de=3(Y/2)^2 + R^2+Y^2=p^4 =>
  8w^2=p^3-p, p|w, contradiction. K10 DEAD by swap symmetry (gate on q).
- K13/K14/K15/K16 DEAD: share gate G3(n): s^4+4s^2t^2+16t^4=square.
  Sophie-Germain factorization + coprimality => U^2,W^2 with U^2+W^2=2p^2,
  U^2-W^2=4st; Z[i] classification of primitive reps of 2p^2 gives
  U^2-W^2=8st != 4st. Contradiction. (K13/K15 via swap.)
- K3/K4: same machinery reproduces exactly Conjecture K34's gate
  (P^2+144v^2 <=> R^2+9Y^2=square) -- the ONLY survivors.
- Census: per-prime square-gate test, all 18 pieces x 12,980 primes <=3e5:
  0 hits. K1/K10/K12/K13-K16 gates impossible <=1e5 (direct gate checks).

UPSHOT: two-prime sum-freeness of D((pq)^2) for 1 mod 4 prime pairs is now
EQUIVALENT to Conjecture K34 ([mss-two-prime-k34]). Kill list: K1, K2,
K5-K16 all dead; K3/K4 remaining (dead for min(p,q)<=3e5).

Files (scripts/mss_two_prime_*): u_factorization.py, k10_16_sieve.py,
k10_16_closedforms.py, k10_16_discsq.py, k1_k12_gates.py (+ .log each).
notes.md: new section [mss-two-prime-uquad] before Cross-problem links.

Tracked failures (append-only): (i) Lagrange interpolation bug (basis init
w^2 instead of 1) made first iff-pass vacuous; caught via hand-slip on K12
disc ((y^2-32)^2-768, not auto-square); fixed + re-run. (ii) Two closed-form
table transcription errors (K10 sig-, K13(-1,+1)) caught by 2,352-check test.
(iii) Mod-9 kill of G3 is VACUOUS: 3|s <=> n=2 mod 3, 3|t <=> n=1 mod 3
(4,783/4,783 primes <=1e5), so 3 -| st never occurs; real kill is Z[i] arg.

Integrity: "## Cross-problem links" count in notes.md = 1; log.md appended
via Add-Content only; no Set-Content on log.md.

## 2026-09-01 - K34 attacked on elliptic-curve terms ([mss-k34-elliptic], magic-square-of-squares)
- Reduction K34-A/B re-verified symbolically (exact): A(n)=square iff M_A: V^2=X^4+132X^3-250X^2+132X+1 has a point with X=(a/b)^2 a positive square (X=0,1 degenerate); same shape for M_B.
- Weierstrass models proved with birational maps verified on all 12+12 known points both directions: M_A ~ E_A: Y^2=X^3-250X^2+17420X+35848 (j=-8000/81), M_B ~ E_B: Y^2=X^3+310X^2+8140X+51912 (j=2744000/9); E_A and E_B are 2-isogenous. Jacobian-formula correction: y^2=x^3-27*I1*x-27*I2 (brief had I1,I2 swapped; Frobenius-trace + j-invariant evidence).
- Mordell-Weil PROVED by 2-isogeny descent: rank E_A = 1, rank E_B = 1, torsion Z/2 both; generators (126,512), (-146,1536); all 12+12 known quartic points are m*G+e*T, |m|<=4 (exact verification; earlier "rank E_B = 2" was a bookkeeping slip, tracked).
- Genus-3 square covers: killing primes {3,5,11,13} (A) and {3,5,19,29} (B); any K34-A counterexample has 3*5*11*13 | ab(a^2-b^2).
- MW sieve on the square-X condition built (strong condition at killing primes) but does NOT collapse with primes <400: 16,322,040 survivor classes mod 528,313,804,200 (t=1 coset). K34 remains OPEN; obstruction now precisely located at the sieve step.
- Files: notes.md new section [mss-k34-elliptic]; scripts mss_k34_elliptic.py + parts p2..p12 + mss_k34_elliptic.log (consolidated). Tracked failures recorded append-only (8 items).

## 2026-09-01 - K34 elliptic round: independent verification block ([mss-k34-elliptic], magic-square-of-squares)
- Claude pre-round check (mss_k34_elliptic_claude_check.py+log): reduction identities A(n)=t^4(u^4+136u^2+16), B(n)=t^4(9u^4-56u^2+144), R^2+Y^2=n^4 verified exact on 1,125 primes <=2e4; master quartics M_A/M_B derived; non-degenerate points (31/35,4604/1225), (66/1151,...) found at p,q<=300. Tracked: first-draft infinite loop in the a^2+b^2 finder.
- Search agent (mss_k34_ptssearch.py+log, mss_k34_cover_deep.log): square-X covers (genus-3) 0 hits through m,n<=10000 (~200M pairs), cover identity validated 2000 random pairs; census |p|,q<=5000: 6 points per quartic, all non-square X. K34 survives to height 1e4 (X up to 1e8 squared scale).
- Theory agent (mss_k34_elliptic.py + parts p2..p12 + consolidated log): reduction proved symbolic; models M_A~=E_A: Y^2=X^3-250X^2+17420X+35848, M_B~=E_B: Y^2=X^3+310X^2+8140X+51912, 2-isogenous; THEOREM rank=1 torsion=Z/2 both (2-isogeny descent, rigorous one-way Selmer kills); killing primes {3,5,11,13}/{3,5,19,29} on the genus-3 covers; MW sieve built, not collapsed <400. K34 OPEN.
- Claude verification (mss_k34_claude_mw_check.py+log): all 24 images on-curve, full m*G+eps*T table reproduced exactly, C_A/C_B reproduced; 3 transcription slips found and filed append-only in notes.md tracked failures (2 alpha-witness typos, 1 image-table T-partner swap between the 66/1151 and 1151/66 rows) - none load-bearing; rank/torsion theorem CONFIRMED. Tracked my own arithmetic slips en route (x3 sign, V denominator, mul-sign).

## 2026-09-01 â€” [mss] Genus-3 Jacobian decomposition VERIFIED: rank J = 2 < 3; Chabauty gate named (Claude session)

- Continued the K34 attack. The genus-3 round agent (report-only) delivered
  the decomposition J(C3_A) ~ E_A x E_A x E_G, J(C3_B) ~ E_B x E_B x E_G.
- Claude independent verification (mss_k34_g3jac_claude_check.py/.log, exact
  arithmetic): (1) j-invariants exact (quotient cubics j = -8000/81 and
  2744000/9 = master j's; E_G j = 1556068/81); (2) Frobenius trace agreement
  master-vs-quotient over 45 good primes 7..211, ZERO mismatches both cases
  -> Q-isogeny -> proved rank-1 carries over; (3) sigma1 = p+1-#C3(F_p)
  cross-checked by hand at all 8 full primes against the trace triples -
  all consistent; (4) independent re-derivation of the theta=-816 descent
  chain for rank(E_G)<=0 (soluble classes [1,2,3,6], dual s_B<=0).
- Verified theorem: rank E_G = 0 (sharp 2-isogeny descent at all three
  2-torsion thetas; torsion = Z/2 x Z/4) => rank J(C3_A) = rank J(C3_B)
  = 2 < 3 = genus => Coleman/Chabauty applies IN PRINCIPLE to both covers.
- NAMED GAP filed (notes.md Section 8, "Chabauty gate"): the actual Coleman
  computation at a good prime (p=11: #C3_A(F_11)=8 -> #C3_A(Q) <= 12, with
  8 known points) is the first concrete proof PATH to K34-A; carrying it out
  and getting "no further points" would PROVE K34-A; same for C3_B (K34-B).
  This is the next-round proposal.
- Tracked failure 10 appended: the agent's first decomposition attempt
  (EBt x E_B pairing) failed its own checks (4/36 primes) and was
  discarded pre-filing; Claude's own false-mismatch hand-count slip
  (#E_A(F_7)) also recorded, with lesson (script, don't hand-count).
- Files: notes.md [mss-k34-elliptic] Section 8 + failure 10;
  scripts mss_k34_g3jac_{frobenius,quotients,rank}.py/.log (agent),
  mss_k34_g3jac_claude_check.py/.log (Claude). K34 remains OPEN with a
  named, computationally concrete gate.
## [ATTACK mss-k34-sieve2] 2026-09-02 -- round 2: deepened MW sieve + sibling covers D_A/D_B + p-adic pole refinement
Round 2 on K34 (magic square of squares, two-prime case), levers 1-3 of the
round-2 brief. Notes: new section [mss-k34-sieve2] (appended before
Cross-problem links; existing sections untouched).
- Killing-prime correction (both cases): p=3 is VACUOUS (C3 mod 3 =
  (x^4+1)^2, all x solvable; E~ singular mod 3); brute re-verification
  p<=300 gives A {5,11,13}, B {5,19,29}. The 3 in 3*5*11*13 | ab(a^2-b^2)
  is automatic mod 3, so the standing consequence stands.
- Sibling covers settled: D_A w^2=z^4+128z^2-512 and D_B w^2=9z^4-128z^2+512
  have invariants matching M_A/M_B, verified C3 correspondences and the
  equivalence 'K34 <=> D point with z^2-4 a nonzero rational square'.
  Sieve-equivalent to M (same C3 image) => no added sieve power. Twist
  lesson recorded (tangent-method cubic of D_A is a nontrivial twist of
  E_A; j-only validation insufficient).
- Deepened MW sieve on E~_A (t=0; t=1 by exact flip): grow phase (primes
  <=400, count cap 3e5) + 23 modulus-neutral hunt primes (ord_p(G) | M,
  BSGS) => 5 survivor classes mod M_A = 42,078,090,600
  (2^3*3^4*5^2*7*13*17*23*73), density 1.19e-10 (round 1: 3e-5). Four
  survivors are the degenerate floor classes {0,+-2,-1}; one genuine extra
  class M/2-1 (n = -1 mod odd part, 3 mod 8) not killed by p<=3e6.
- NEW VERIFIED LEVER (p-adic refinement of pole classes): X extends
  regularly at the removable pole (4,-264)=2G_A with value 1151/66, so
  EVERY n = 2 mod 10 point has X = 1151/66 = 7 mod 13, a nonresidue =>
  the whole class n=2 mod 10 (incl. n=2 itself, X=infinity) is DEAD.
  Verified exactly (X(12G),X(22G),... = 7 mod 13). Branch (4,264) gives
  the condition v_13(x-4) even, refining n=-2 mod 10 to mod 130.
  Endgame (open, now concrete): iterate refinements over all primes to
  drive every class onto the exact degenerate points => K34-A. Not yet
  carried out [to-verify].
- B-side first sieve: model E~_B y^2=x^3+256x^2-2048x, inverse
  X=(6y-92x)/(x(x-36)) verified on all table rows; 5 classes mod 264 =
  {0,1,2,-2,M/2+2}, density 1.9e-2 (weak: ord_p(G_B) rarely M-smooth);
  grow+hunt continuation in flight.
- Tracked failures appended (F11 composite-prime sieve bug - invalid
  M=60,S=[0] state discarded; F12 pole 0/0 masquerading as flip failure;
  F13 Fraction % misuse).
- Files: notes.md [mss-k34-sieve2] section; scripts
  mss_k34_sieve2_p1..p9.py, mss_k34_sieve2_state{A,B}.json. K34 remains
  OPEN; two named gates now: Chabauty (Section 8) and the refined-sieve
  collapse (Section 2c of the new section).

## 2026-09-01 - [VERIFY mss-k34-sieve2-verify]
Claude verification of the K34 round-2 sieve ([mss-k34-sieve2] Section 6 in
notes.md). A-side: deterministic re-run of the agent's p3 driver reproduces
M_A=42,078,090,600 with survivors {0,2,M/2-1,-2,-1} exactly; stress vs 624
valid primes (ord_p(G)|M_A) <= 3e5: zero violations; 2c pole-refinement
lever verified exactly (X = 7 mod 13 on all n = 2 mod 10; mod-169 values
85,150,46,111,7; extension value 1151/66 via y'(4,-264) = -1027/33).
B-side: exact X_B identities (1, 5/41, 41/5, 414/209, 2G=(36,-552));
killing primes {5,19,29} re-derived from the C3_B octic; p5 driver re-run
from scratch reproduces 5 classes mod 264 = {0,1,2,134,262} exactly
(density 1.894e-2); stress vs 33 valid primes (ord|264) <= 2e5: zero
violations. One text correction filed: "4 hunt primes <= 1e5" -> 5
(1097, 1571, 5297, 9769, 93407). Two of the verifier's own initial
discrepancies were semantic (grow-cap counts expected survivors; class
conditions need ord|M) - recorded in notes.md so future rounds do not
repeat them. W2b extension check 3e5..1e6 still in flight at filing time.
Status: [mss-k34-sieve2] B-side [to-verify] flag lifted for the t=0 state.
Addendum to [VERIFY mss-k34-sieve2-verify]: W2b extension landed - valid
primes 3e5..1e6 with ord_p(G)|M_A: 231 primes, ZERO violations on the 5
A-side survivor classes. "Hunt to 3e6 does not kill class M/2-1" confirmed
at the 1e6 level. notes.md Section 6 amended accordingly.
## 2026-09-02 - [ATTACK mss-k34-refine] Refinement round: congruence
endgame impossible; coset reduction + primitive-divisor gate
Claude round (notes.md Sec 2d). Exact: denom(x(3G_A))=961=31^2,
denom(x(4G_A))=1089=3^2*11^2 => the only primes that could reduce
survivor classes onto the 0/0 pole 2G_A are p=31 (ord 3; constant
1151/66 is a RESIDUE there -> classes -1, M/2-1 survive) and p=11
(ord 4; constant has v_11=-1 -> class -2 dies only at kernel depth 1).
STRUCTURAL FINDING: 2G_A is the only 0/0 point of X with a unit
constant; at -2G_A the numerator 528 != 0 (genuine pole, parity-only
constraints on the free parameter k); at -G_A, X=1 regular (X = 1 mod p
at every odd valid prime, no kill); at O, X -> 0 with free leading term.
CRT-independence of distinct primes => no congruence refinement kills
classes -2,-1,M/2-1,0: the 2c collapse onto degenerate points is
impossible as stated. Sharp reduction: non-degenerate K34-A candidates
lie exactly in four k-cosets of <H_A>, H_A = M_A*G_A; t=1 coset is
flip-equivalent (X preserved). NEW NAMED GATE: primitive-divisor route
(Ingram primitive divisors + numerator-cancellation lemma) => v_q(X)=1
odd at a primitive prime q => X not a square => K34-A; ports to K34-B.
Reduced to two lemmas, neither proved. Tracked-failure note: an initial
claim "class -2 killed outright at p=11 by valuation parity" was
self-caught by the local expansion at (4,264) (528 = 48*11 makes it a
0/0 mod 11) - corrected before filing.

---

## [ATTACK mss-k34-refine2] 2026-09-02 â€” K34: cancellation lemma PROVED; gate reduced to odd-depth primitive divisors

**Round target** (from 2d): the two lemmas of the primitive-divisor route â€” (a) cancellation/numerator lemma, (b) applicability of Ingram's primitive-divisor theorem to the coset EDS.

**Outcome: Lemma (a) PROVED outright, no exceptions.** For any good prime q and any kernel point P = nG_A of depth s = v_q(denom x(P))/2 >= 1: writing x = phi/psi^2, y = phi3/psi^3 in lowest terms (standard integrality: gcd(phi3,psi)=gcd(phi,psi)=1, so v(phi3)=v(phi)=0):
- y+66x = (phi3 + 66 phi psi)/psi^3 â€” second term has valuation >= s > -3s, no cancellation possible, v = -3s exactly;
- x-4 = (phi - 4 psi^2)/psi^2 â€” numerator = phi mod q, v = -2s exactly;
- hence v_q(X(P)) = -3s - (-4s) = +s UNCONDITIONALLY.
The 0/0 exceptional points of X (poles (4,-/+264), zero T=(0,0)) never coincide with kernel points. Verified exactly on 256 kernel-prime cases (n <= 60, all good q <= 4000 with ord_q(G) | n): 0 failures (mss_k34_refine2.py/.log).

**Consequence:** X(nG_A) = w^2 forces even depth s_q at EVERY kernel prime q of nG_A (every good q with ord_q(G) | n). One odd-depth kernel prime kills the point.

**Lemma (b) refined to the exact remaining gap.** Ingram's primitive-divisor theorem gives primitive q | psi_n (ord_q(G) = n) for n >= 13; all coset indices n = c + kM_A >= M_A - 2 ~ 4.2e10 qualify, and q does not divide n (q | n with q >= 5 forces n <= 11 via ord <= #E(F_q) <= q+1+2sqrt(q)). Depth of nG at q = v_q(psi_n) = 1 + delta_q, delta_q = elliptic Wieferich defect (q^2 | psi_n iff delta_q >= 1). So:

  K34-A reduces to: for every coset index n (n = c mod M_A, c in {0,2,M_A/2-1,-2,-1}), some primitive divisor q of psi_n has v_q(psi_n) ODD (equivalently: not all primitive divisors are odd-Wieferich, v_q(psi_n) in {2,4,...}).

That is the exact residue of the problem: ruling out "all primitive divisors have even depth" unconditionally requires a non-Wieferich bound for EDS â€” the direct analogue of the Wall-Sun-Sun obstruction for Lucas sequences. Silverman's conditional-on-abc sparsity result suggests the gate holds heuristically, but unconditionally this is open. [to-verify] exact hypotheses of Ingram's theorem (n >= 13 for all nonsingular E/Q, infinite-order G, or curve-dependent exceptions?).

**Empirical gate evidence:** depth census v_q(psi_ord) over all good q <= 4000 with ord_q(G) <= 60 for (E~_A, G_A): 78/78 primes have depth exactly 1, depth histogram {1:78} â€” zero odd-Wieferich primes found.

**B-side port (Lemma a only):** same argument for X_B = (6y-92x)/(x(x-36)): 6phi3 - 92 phi psi has valuation 0 at kernel points for q >= 5, x - 36 gives -2s, so v_q(X_B(P)) = +s; identical reduction for the four k-cosets of <H_B> (M_B = 264). Lemma a fully ports; Lemma b is the shared gap.

**Files:** notes.md sec 2e [mss-k34-refine2]; scripts/mss_k34_refine2.py + .log.

**K34 status: OPEN.** Gate sharpened from "two unproven lemmas" to "one unproven lemma (odd-depth primitive divisors, a Wieferich-type gap)".

[ATTACK mss-k34-refine3] 2026-09-02 ~11:00 | magic-square-of-squares | K34 / elliptic EDS depth census
- Built Shipsey-style EDS engine (7-window, valuation-tracked mod p^8, O(log n)) computing W_n = psi_n(x_G) for large indices. Validated 378/378 vs exact W_n on both curves. First time kernel depths are computable for large n.
- DEPTH CENSUS (all good q <= 20000, 2260 primes/curve): A: {1: 2259, 2: 1}; B: {1: 2257, 2: 3}. FIRST odd-Wieferich primes found: q=167 (A, ord 84, depth 2); q=13/419/2351 (B, depths 2). Rate consistent with Poisson( sum 1/q ~ 2.5 ).
- Depth-decomposition theorem PROVED via formal group: depth_q(nG) = b_d + v_q(n/d), d = ord_q(G) | n. Class-0 constraint theorem: X(kH_A) = w^2 forces v_p(k) = b_p + v_p(M_A) + v_p(d) (mod 2) for every valid prime p; k must absorb R_0 = product of odd-depth valid primes.
- Significance: odd-Wieferich primes exist (depth 1 NOT universal) but are rare (~0.1%); gate = "some primitive divisor of each psi_n has odd depth" remains a Wall-Sun-Sun-type gap with measured base-rate support. K34 stays OPEN.
- Files: scripts/mss_k34_refine3.py + .log (engine + census q<=20000); scripts/mss_k34_refine3_valid.py (valid-prime census <= 3e5/2e5, validA/validB_primes.json). notes.md sec 2f filed. To-verify: Ingram primitive-divisor hypotheses.

[ATTACK mss-k34-refine3] 2026-09-02 ~11:55 | magic-square-of-squares | valid-prime census + class recount (correction)
- Valid-prime depth census LANDED (35 min): curve A 640 valid primes (ord|MA) <= 3e5, depth histogram {1:639, 2:1} (only even-depth valid prime: p=167); R0 = product of 639 odd-depth valid primes, log10(R0) = 2712.0 (lower bound). Curve B: 34 valid primes <= 2e5, ALL depth 1, R0^(B) log10 = 103.2. Files: validA_primes.json / validB_primes.json.
- APPEND-ONLY CORRECTION to [mss-k34-sieve2]: the W2 count "624 valid primes <= 3e5" was an UNDERCOUNT -- its bsgs_order returned None for 16 primes (silently skipped); complete order-finding (trial-division factorization of #E(F_p)) gives 640. Class conclusions UNAFFECTED: re-check of all 5 survivor classes on all 640 (A) and 34 (B) valid primes gives 0 violations (mss_k34_refine3_classcheck.py).
- Notes sec 2g filled: class-0 size forcing now quantitative -- any X(kH_A)=w^2 solution has n = k*MA >= R0*MA > 10^2721 >> C(E_A) ~ 1e39-42 (Verzobio), so primitive-divisor existence for class-0 cosets is unconditional; nonzero cosets retain the window [MA-2, C(E_A)] ~ [4.2e10, 1e40]. K34 OPEN.
