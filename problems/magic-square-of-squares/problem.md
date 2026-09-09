# Magic Square of Squares (Euler's problem)

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/MagicSquare.htm.

## Statement
Does there exist a $3\times3$ magic square (all rows, columns, and both
diagonals equal) whose nine entries are **distinct perfect squares**?

## Status
**OPEN.** (Euler, 1770s.) Many near-misses; no example. A $3\times3$ magic
square of *distinct* integers is trivial; the all-squares constraint is the
open part.

**State of the attack (2026-09-07, notes.md §§2d–2j):** the two-prime
($\omega_1=2$) sum-freeness gate — Conjecture K34 — is the single standing
obstruction, reduced to square-X points on the genus-1 quartics $M_A, M_B$
and further to an elliptic-coset structure: candidate indices $n$ lie in 5
classes mod $M_A=4.2\cdot10^{10}$ (resp. $M_B=264$), with kernel-depth
parity the exact obstruction (Lemma 2 proved). Two structural results
sharpen the remaining gap: class-0 hypothetical solutions are forced to
$n\ge R_0M_A>10^{2721}$, past the effective (Verzobio) primitive-divisor
constant; and a validated depth-parity sieve (new kill layer) removes
42–78% of the remaining candidate space per nonzero coset. Named proof
paths: Chabauty–Coleman on $C3_A$ at $p=11$ (rank $J=2<3$), and the
Wall–Sun–Sun-type odd-depth primitive-divisor gate (Lang/abc-conditional
routes exist). **§2j (2026-09-07, `[mss-k34-jacobian]`):** the descent
tree's terminal layer is now fully analyzed — the four leaf quartics share
ONE Jacobian $E_a: y^2=x^3+32x^2+238x$ (they are its four α-descent covers,
$ae=238$); rank$(E_a)=1$ unconditional (mwrank), image$(\alpha)$ =
{1, 238, −14, −17}; **three of the four leaves are PROVED INSOLUBLE**
(nontrivial Sha[φ] elements) — the (8,9)/(9,8) sub-tree and the ℤ[√2] UFD
descent are closed; the live leaf C_238 is parametrized by the rank-1 fiber
$T_a+2mP_a$, its first admissible point (852, 3727, 25318369) sits outside
the filed census boxes (the "0 hits" was box-limited), and the Fermat/Germain
loop on it is exactly the index-halving map (verified m = 2..28) closing
benignly at odd indices — stall item (ii) resolves negatively; the remaining
tamable piece is the lift-condition lemma $s\pm2\rho\sigma\ne\square$
(census-failed at every tested index; Jacobian of the (1,72) quartic is the
twist partner ≅ E_a, so the same α-descent machinery applies). **§2k
(2026-09-08, `[mss-k34-liftgate]`):** §2j's lift test corrected (append-only)
— the K34-A candidate-chain lift is n²−4u²(rs)² = r⁸·N(s²/r²) with
N(x) = x⁴−4x³−604x²−952x+56644: a THIRD quartic D with Jacobian
J_L : y² = x³−27894240x+56491485696 (rank 1 unconditional, mwrank; generator
(2472, 51408); shifted image(α^L) = {1, 238, 271, 64498} — the 238
recurrence). D's known points: (0, ±238) and (−33/2, ±5/4); no positive-
square-x point found. The K34-A candidate lift is thus the class-1 fiber of
α^L on J_L — **structurally identical to K34-A itself** (same square-x
question shape, one level up): the lift gate does not collapse, and the
new structural question is whether the lift tower (covers of the same curve
**§2l (2026-09-08, `[mss-k34-liftgate2]`):** two-parents structure — every
admissible leaf point has TWO layer-1 parents: Parent A (u, ±rs, n), the
K34-A chain, is a **FIXED POINT** of the Germain step (split (238r⁴, s⁴)
recovers the leaf point itself — no descent contradiction available on the
K34-A chain; the §2j halving map ran on Parent B, whose child lands in the
killed (1,238) cell). New provable **sign gate**: the candidate lift
n − 2urs ≥ 0 ⟺ P(Y) = 56644Y⁴−952Y³−604Y²−4Y+1 ≥ 0 (Y = (r/s)², integer
form s⁸−4r⁶s²−604r⁴s⁴−952r²s⁶+56644r⁸ ≥ 0; no rational factorization);
inside the admissible window the boundary is the quartic irrational
X* = 0.1974773589… — **dead band X ∈ (X*, 238^-1/4), 22.4% of the window,
proved dead**. Full gate sweep m = 2..60 (16 admissible points, integers
to 10³⁶⁰): **0 candidates** — sign kills m = 2, 58; the D-gate (product
square) fails at all 14 alive indices. The K34-A candidate gate is now
22.4% dead by theorem + census-failed to m = 60 on the rest; the named
next step is proving N(X²) never square on the admissible fiber (= no
positive-square-x point on the C₁ cover y² = 8x⁴+1016x²+9 — the §2k
tower shape). K34 remains open. **§2m (2026-09-08, `[mss-k34-tower1]`):**
7–17 kernel lemma PROVED — gcd(n+2urs, n−2urs) = 1 unconditionally (odd
p | gcd ⟹ p ∈ {7,17}; the valuation lemma kills 7|s, 17|s always:
v₇(238r⁴)=1 odd contradicts u² square; 7|n ⟺ 7|s) — so the **D-gate is
EXACTLY the lift condition** (no gcd artifact possible). Direct lift census
m = 2..240: 59 admissible indices, 9 sign-dead, 50 alive, **0 lifts**
(exact integers to 708110 bits). Tower height 1: a C₁ square-x point = a
rational point of the GENUS-3 curve Z : y² = 8w⁸+1016w⁴+9; PARI
hyperellcharpoly: **Jac(Z) splits into 3 elliptic factors at 11/11 split
primes** — one is J_L (rank 1 unconditional), the other two are a
quadratic-twist pair (traces (t,−t) at every split prime; ranks open).
Correction: the §2k "E_Z = Prym" claim retracted (wrong substitution).
NAMED GATE: if the ±pair has rank 0, rank Jac(Z) = 1 < 3 ⟹ Chabauty on Z;
Z(ℚ) has only the degenerate points (0,±3) ⟹ no square-x on C₁ ⟹ the
K34-A candidate chain closes unconditionally. K34 remains open.
**§2n (2026-09-08, `[mss-k34-tower2]`):** mod-5 correction — the tower
curve for the lift gate is Z_D : V² = w⁸−4w⁶−604w⁴−952w²+56644 (w = s/r),
NOT the C₁-octic (round-4 claim self-caught pre-filing and corrected).
**W₅(Z_D) = {0, ±1}** (proved): s ≡ 0, ±r (mod 5) required — kills 17 of
the 50 alive indices (provable). ±pair identification: the 7-prime
candidate A=2178,B=225 discarded (fails 4 of 11 trace constraints);
full-filter search running. K34 remains open. **Addendum-2:** the §2m
3-way split is for the C₁-octic tower; for the lift-gate tower the involution
(w,V) ↦ (−w,−V) has quotient **P : y² = x·N(x) (genus 2, rational Weierstrass
point x=0)**, and **Jac(Z_D) ~ J_L × Jac(P) CONFIRMED 9/9 primes**
(t(Z_D) = ap(J_L) + t(P), p = 23…59 exact) — rank Jac(Z_D) = 1 + rank Jac(P);
P's charpoly is a quadratic SQUARED at p=23, 41 (Jac(P) ~ E × E^χ). The
Chabauty gate needs rank Jac(P) ≤ 1; P's rational Weierstrass point makes a
hand 2-descent on Jac(P) the realistic next computation. K34 remains open.
**§2o (2026-09-08, `[mss-k34-tower3]`):** the **full Z_D mod-p sieve kills
ALL 50 alive admissible fiber indices (m ≤ 240)** — w = s/r mod p ∈ W_p
necessary for every p ≤ 499 (exact; p | r excluded via the rational infinity
points); first-killing primes p = 7, 29, 41, … (all exact). P(ℚ) search:
only the branch point (0,0) in p ≤ 3000, q ≤ 40. The complete closure still
needs the Jac(P) rank gate (Chabauty on Z_D) or a descent argument — the
sieve kills finite ranges only. **§2p (2026-09-08, `[mss-k34-tower4]`):**
**±pair RESOLVED — K = ℚ(√238)**: Jac(P)'s charpolys split exactly at the
split primes of ℚ(√238) and are irreducible palindromic at exactly the inert
primes (27/27 verified, exact) — **Jac(P) = Res_{K/ℚ}(E_K), rank Jac(P) =
rank E(ℚ(√238))**. Chabauty on Z_D needs rank E(ℚ(√238)) ≤ 1 (standard
2-descent over K — next). The 238 recurrence is structural: leaf-Jacobian
family, lift-gate Jacobian J_L, and the Prym base field. K34 remains open.
**§2q:** K verified 34/34 primes (new-prime predictions 157, 163, 179, 197,
211, 223, 241 all confirmed: split ⟹ x³-term charpolys, inert ⟹ palindromic
even forms); E_a DISCONFIRMED as the factor (p=101: factor traces (−12,+18)
vs ap(E_a)=10 — coincidence caught pre-filing); analytic rank of Jac(P)
(model-independent) in flight. K34 remains open. **§2r (2026-09-08,
`[mss-k34-tower6]`):** **analytic rank Jac(P) = 0** — sum a_p/p flat at
~−0.7 through p = 5000 (bad primes {2,3,7,17,271}; rank 1 would add ~+1.0
per log-log unit, rank 2 ~+2.0; no slope observed) — so **rank Jac(Z_D) =
1 < 3: Chabauty applies to Z_D**, #Z_D(ℚ) ≤ #Z_D(F_p) + 4 at good p.
Known Z_D(ℚ) = degenerate orbit only; if Coleman yields exactly that, the
K34-A candidate lift fails for every m and the leaf chain closes
unconditionally. Rank 0 is analytic evidence; rigorous completion via
2-descent on Jac(P) or L(1) nonvanishing. Two Chabauty targets: C3_A
(main gate) and Z_D (leaf chain), both rank 1 < 3. K34 remains open.
**§2u (2026-09-08, `[mss-k34-tower9]`):** the **Z_D sieve density
quantified**: ρ = ∏_{5≤p≤499} |W_p|/p ≈ 8.92×10⁻²⁵⁵ (exact per-prime QR
computations) — for any height-bounded candidate box the expected
survivors is (#candidates)·ρ: the mod-p layer is essentially exhaustive
for any enumerable set, and the bottleneck is exactly the HEIGHT BOUND
(which effective Chabauty supplies once rank Jac(P) = 0 is rigorous).
The closure program is now explicit: (1) rank Jac(P) = 0 rigorous;
(2) height bound; (3) Coleman on Z_D. K34 remains open. **§2x (2026-09-08, `[mss-k34-sage2]`):**
**SageMath 10.9 INSTALLED** (Miniforge/conda-forge, user-local) — Simon
2-descent over number fields now live (the tool for rank E(ℚ(√238)));
Jac(P) confirmed SIMPLE over ℚ (irreducible charpoly at 31/53/59) splitting
over K as E × E^σ; Stoll's genus-2 two-descent remains Magma-only; Sage's
bundled gp spawn broken in this env (local standalone gp via subprocess
works). Next named: construct the Prym curve E/K from its trace signature,
then rank E(K) via simon_two_descent over K. K34 remains open.
**§2y (2026-09-08, `[mss-k34-richelot]`):** **RICHELOT STRUCTURE FOUND
(exact)** — N(x) = (x²−2x+238)² − 1084x² with 1084 = 4·271: the
decomposable shape y² = x(h²−d·x²); the two elliptic quotients over
L = ℚ(√−271) are E± : y² = x³+(±2√−271−2)x²+238x (conjugate, L-rational
2-torsion at (0,0)); **rank Jac(P) = rank E₊(ℚ(√−271))** via the Richelot
isogeny — the rank gate is an explicit Sage descent over L (running).
Reconciliation: K = ℚ(√238) (Frobenius-factorization field) and
L = ℚ(√−271) (Richelot isogeny field) are different, both real. K34
remains open. **§2aj (2026-09-09, `[mss-k34-selmer2i]`):** **RANK GATE
CLOSED UNCONDITIONALLY** — Sage's NF descent wedged at 24h (killed,
tracked failure 28); replaced by a hand 2-isogeny descent (b = 238
rational ⇒ explicit candidates; exact local conditions incl. 2-adic ring
model + points-at-infinity): Sel(φ) = {1,238} (dim 1; {7,34} die
2-adically, ZERO solutions mod P³), Sel(φ′) = {1} (dim 1; c=2
valuation-blocked at 2) ⇒ **rank E₊(ℚ(√−271)) = 0 PROVED**; rank Jac(P) = 0
upgraded from BSD-conditional (§2r) to unconditional; Sha[φ] = (Z/2)²,
Sha[φ′] = Z/2. **rank Jac(Z_D) = 1 < 3 unconditional: Chabauty gate
PASSES**; named remaining: height bound, then Coleman on Z_D. K34
remains open.
**§2s (2026-09-08, `[mss-k34-tower7]`):** the hand 2-descent on Jac(P) is
NOT directly available — Gordon-Grant/Stoll requires all five Weierstrass
points rational, but **N(x) has NO rational root** (all divisors of
56644 = 2²·7²·17² tested); the Galois descent from ℚ(J[2]) is the missing
ingredient. **rank Jac(P) = 0 honestly filed as ANALYTIC/BSD-CONDITIONAL**
(flat sum through p = 5000); the Chabauty-on-Z_D gate is conditional at the
first link and computational at the last. No proof of K34-A claimed. K34
remains open. Addendum: numerical L(s) evaluation running (5 s-values,
primes ≤ 30000; cache-then-evaluate pattern noted for future runs).
**L(s) job killed 2026-09-08 as redundant** once the rigorous Sage descent
on rank E₊(ℚ(√−271)) was in flight (§2y); its last logged value
L(1.5) = 0.783 corroborates non-vanishing L. Re-runnable via k34j_ls_eval.gp.
**§2i (2026-09-03):** the primitive-divisor attribution is
corrected to Verzobio 2023 (PJM 325, effective constant computed for our
models: $10^{41}$–$10^{44}$, so the entire nonzero-coset window sits BELOW
it — existence there is ineffective-only); the four K34-descent leaf
quartics re-censused on extended boxes with corrected parity classes
(0 hits, ~470k pairs); layer-1 survivor bookkeeping reconciled (16/12/2 =
filter differences; only the degenerate $X=1$ mirror pair passes the
lift); Bennett–Walsh 1999 scope clarified (one-parameter — does not reach
our two-variable leaf quartics). K34 remains open.

## Frontier (one line)
No example found despite extensive search; no impossibility proof.
Related: $4\times4$ magic squares of squares *do* exist (Euler).
**Published center/step bounds (added 2026-09-01, `[summary]` via
multimagie.com + Bremner Acta Arith. 99 (2001)):** the strongest is
**Buell 1999** (preprint, cited in Bremner's *On squares of squares II*,
Acta Arith. 99): no **magic hourglass** (7-square subset = top row +
center + bottom row — a *necessary subsystem* of any full 9-square
solution) with central cell $<25\times10^{24}$, hence any 9-square
solution has center $>2.5\times10^{25}$. Morgenstern 2014 independently
re-verified Buell's null (broader searches to ~$5\times10^{12}$ center);
Morgenstern 2006/15 (smallest-entry paper): all 9 entries must be squares
of $\ge$ 8-digit numbers ($>10^{14}$); Boyer 2004: no $>6$-square
solutions for vast families of 1-mod-4 center types up to
$10^{26}$–$10^{30}$. 8-square records are step-value searches (see the
census bullet below).
**2026-08-31 census, adversarially verified `[mss-census-verified]`:**
this session enumerated **all square-center $\ge7$-square magic squares of
squares with entries $e\le440{,}000$** (parametrization around center
$a=u^2+v^2$: entries $a\pm b,\ a\pm c,\ a\pm(b+c),\ a\pm(b-c)$ with
$\{b,c,b\pm c\}\subset D_0=\{2uv:u^2+v^2=a\}$; all $C(4,2)$ role-pairings
solved; dihedral-canonicalized) — **exactly ONE class up to dihedral
symmetry: the Bremner/Sallows square** (rows/columns/diagonals
$541875=3\cdot425^2$, center $425^2=180625$). Soundness confirmed by an
independent re-derivation script (`scratch_verify_independent.py`,
different architecture, two box sizes; degenerate/repeated-entry
superset also clean). **Novelty confirmed:** no published bounded census
exists — Bremner (Acta Arith. 88 (1999) 289–297) is the "only known
example" (attribution: **Bremner/Sallows**), not a uniqueness statement;
OEIS A221669 / multimagie.com confirm. Scope caveat: uniqueness is
square-center + entries $\le440000$ + $\ge7$ squares only — non-square
centers untouched. Also corrected from the verify: the 8-square search
records are a **step-value** search to $d\le6\times10^{23}$
(Morgenstern 2014; not "all entries $\le6\times10^{23}$"), plus mod-$2^{59}$
solutions and sum $\equiv3\pmod{72}$ for 7-square configurations
(Zimmermann–Pierrat–Thiriet 2015); Robertson (Math. Mag. 69 (1996) 289–293)
reduces the problem to an elliptic curve of rank 4 `[to-verify vs primary]`.
**2026-09-01 additive-parallelogram reduction `[mss-parallelogram-reduction]`:**
the full problem is now *exactly* an additive-combinatorics statement —
**a 9-distinct-square solution exists iff some $D(w^2)$ contains an
additive parallelogram** $\{x,\,y,\,x+y,\,y-x\}$ (four distinct elements);
the hourglass (Buell's object) is exactly the weaker *additive triple*
$\{b,c,b+c\}\subseteq D(w^2)$, so Buell's theorem ⟺ no additive triple in
any $D(w^2)$ with $w\le5\cdot10^{12}$. New census (`mss_d_additive_patterns.py`):
zero additive triples AND zero parallelograms for all $w\le10^6$ (centers
$\le10^{12}$) — independent small-$w$ re-verification of Buell by a
different engine; **W=10⁷ extension LANDED (2026-09-01,
`mss_d_additive_W1e7.py`, corrected D-builder, 107 s): A2=A3=AP=0 over
2,952,907 $w$ with $|D|\ge3$ (99.1M pairs)** — the freeness box extends
to centers $\le10^{14}$. **3-term-AP census (`mss_d_ap_census.py`, same range):
zero 3-term arithmetic progressions in any $D(w^2)$** — a second
additive-freeness property, distinct from the triple condition
($x+z=2y$ vs $x+y=z$); for the cubic sibling the analogous statement is
Legendre's no-three-cubes-in-AP theorem (the cubic D-set is empty,
`[[square_of_cubes]]`). **Targeted beyond-Buell search
(`mss_hourglass_targeted.py`): zero additive triples/parallelograms at
2500 max-|D| centers (|D|=3280, products of 8 distinct 1-mod-4 primes)
with $w\in(5\cdot10^{12},\,2.5\cdot10^{15})$ — centers to
$6.4\cdot10^{30}$, ~7 orders past Buell, via an exact Gaussian-integer
$D(w^2)$ builder (validated: Lemma-1 counts, isqrt membership, Lemma 4
at every $w$). Targeted, not exhaustive — expected yield under the model
$\sim10^{-3}$; the max-|D| regime where the model's tail mass
concentrates is now verified far past the exhaustive frontier.** New heuristic (`mss_hourglass_heuristic.py`): the
expected total number of hourglass triples over the ENTIRE infinite plane
of centers collapses to exact Euler products and evaluates to
**$H\approx1.01$ (naive density) or $0.53$ (strict density $|D|-2$)** —
both upper bounds ⟹ *at most about one hourglass should exist anywhere*;
Buell's null is the expected global behavior, not a small-box artifact
(details + honest caveats in notes.md).
**Sharp partner-window theorem + corrected heuristic
(`mss_window_spacing.py`, 2026-09-01):** *provable* two-sided window —
if $\{x,y,x+y\}\subseteq D(w^2)$ with $x=2uv$, then
$2(u{+}v)+1\le y\le(u{-}v)^2-1$ (both roles), with the testable spacing
corollary $d'-x\ge2\sqrt{w^2+x}+1$ for ANY two elements $x<d'$ of
$D(w^2)$ (verified: 1,259,270 consecutive-pair tests over $w\le10^6$,
0 violations; empirically gaps are $\ge2\times$ the bound). Feeding the
windows (theorem, not model) back into the Euler-product density gives
the corrected expected total **$H_2\lesssim0.08$** (strict $0.056$) —
a $13\times$ sharpening of the naive $1.01$: the null is now the
strongly expected outcome ($P(0)\approx92\%$), not a $1\sigma$
fluctuation. **Main problem quantified
(`mss_parallelogram_heuristic.py`): the expected number of additive
parallelograms — the exact 9-square condition — over the ENTIRE infinite
plane of centers is $\approx4.4\cdot10^{-5}$** (window-corrected; naive
$1.1\cdot10^{-2}$, cut $257\times$; model, not proof — density model for
the two independent hits, uncalibrated by necessity) — under the
corrected model a solution is expected not to exist with probability
$\approx99.996\%$, and Buell's null is exactly what the model predicts. **Difference census
(`mss_d_diff_census.py`): zero pairs with $y-x\in D(w^2)$ over all
6.16M pairs, $w\le10^6$ — a consistency check, not new territory: a
difference pair IS a sum triple, so sum-freeness ⟺ difference-freeness
exactly, and sum-freeness also implies AP-freeness ($x+(z-m)=m$) — the
three freeness censuses were one all along (sum-freeness strongest).**

**2026-08-31 loop block — census engine upgraded (validated), deep runs in
flight.** The uniqueness census was re-dered on a **Pythagorean-triple
engine** (`scripts/mss_census_pythagorean.py`): every square pair
$a\pm d$ around a square center $a=w^2$ ⟺ triple $(u,v,w)$ with $d=2uv$,
and primitive triples $(m,n)$ scaled by $k$ sweep all centers $w^2\le W^2$
in $\sim0.08\,W\log W$ work — versus $O(B)$ for the entry-driven engine at
box $B$. Validated three ways: (i) exact reproduction of the 440,000
census (Bremner, 1 class); (ii) D-set vs independent brute-force scan for
all $w\le3000$: 0 mismatches; (iii) first $W=10^6$ run: 7056 raw configs =
3 $\times$ 2352 Bremner scalings **exactly** — zero non-Bremner
primitives, zero nsq$\ge8$ (which, with square center, would be the full
9-square solution) at centers $\le10^{12}$. **Structural finding:** global
scalings $k^2(a,b,c)$ = the entry-scaling orbit, so the census claim takes
its clean primitive-quotient form — "the only *primitive* square-center
$\ge7$-square config with center $w^2\le W^2$ is Bremner/Sallows" — the
published-search box ($\le440{,}000$) was implicitly primitive-only; the
triple engine extends $W$ by orders of magnitude at negligible cost.
**Flagship W=10⁶ LANDED `[mss-census-w1e6-verified]`; extended W=10⁷
LANDED `[mss-census-w1e7-verified]` (2026-09-01):** W=10⁷ (centers ≤
10¹⁴): raw 70,587 (= Bremner scalings; ×10.0 vs W=10⁶, the scaling-window
ratio), primitive 3, dihedral classes **1**, non-Bremner **0**, nsq ≥ 8
**0** — the Bremner/Sallows uniqueness box extends to **centers ≤ 10¹⁴**
(log `census_W1e7.log`; NOT subsumed by Buell — his theorem bounds only
hourglass-containing configs, while the ≥7-square Bremner-type tier is
below that threshold and genuinely needs this census). At W=10⁶: raw 7056
(= 3 × 2352 Bremner scalings exactly), primitive 3, classes 1,
non-Bremner 0, nsq ≥ 8 0 — entry box 3×10¹⁵ not binding at that
W (max k = 2352 from the center cap < k_max from the entry cap ≈ 2885), so
the sweep is *complete* for centers ≤ 10¹². **Claim now filed: the ONLY
square-center ≥7-square magic square of squares with center w² ≤ 10¹² is
Bremner/Sallows, up to its global scalings** (box extension 4.4×10⁵ →
10¹², ≈2.3×10⁶ in center value). W=10⁷ (centers ≤ 10¹⁴) in flight.
**nsq9 deep hunt (2026-09-01) — independent verification, not a new
frontier** `[mss-nsq9-w1e8-verified]`: the chunked engine's full-solution
hunt (`scripts/mss_census_chunked.py`, mode nsq9 = all four role
quantities |b|,|c|,|b+c|,|b−c| ∈ D(w²) ⟺ all 8 non-center entries
square) at W=10⁸ found **0 full 9-square configs with center ≤ 10¹⁶**.
Honest verdict after the novelty check: this is **subsumed by Buell
1999** (hourglass center bound 2.5×10²⁴ ⟹ center > 2.5×10²⁵ for any
9-square) — our run is a *third independent verification* of the Buell
null (after Morgenstern 2014's ~5×10¹², ours is ~200× deeper in center
value), exercising the new chunked engine end-to-end. To actually beat
Buell the nsq9 hunt needs W > 1.6×10⁸ — a C/numpy port (the Python
engine's cost scales as ~W log W with heavy constants; estimated
multi-day at W=10⁹).
**Structural lemmas filed** (see [notes.md](notes.md),
`[mss-structural-lemmas-verified]`): (1) closed form
$|D(w^2)|=(\prod_{p\equiv1(4)}(2v_p(w)+1)-1)/2$; (2) primitive ⟺ $w$ odd
(even-$w$ configs are exactly the $4=k^2$ scalings); (3) $\ge7$-square ⟹
$|D(w^2)|\ge2$ ⟹ center divisible by $p^2$ ($p\equiv1\bmod4$) or by two
distinct 1-mod-4 primes [**corrected 2026-08-31**: first draft claimed
$|D|\ge3$/3-complete-pairs — wrong; Bremner has 2 complete pairs + 2
accidental half-pairs, 7 = 2·2+2+1]; (4) 24 | every $d\in D(w^2)$ ⟹ all
nine entries of a primitive config ≡ 1 (mod 24). Full solution
(nsq=9, all nine entries square) needs $|D|\ge4$; nsq=8 alone needs only
$|D|\ge3$ (3 complete pairs + 2 accidental halves).

**Prime-power freeness theorem — first proved family `[mss-primepower-freeness]`
(2026-09-01).** For $w=2^ep^k$ ($p\equiv1\bmod4$ prime), $D(w^2)$ is
sum-free, AP-free, and parallelogram-free — *proved* (Gaussian-integer
structure: elements $d_m=p^{2(k-m)}|\operatorname{Im}(\bar\pi^{4m})|$
have pairwise distinct $p$-valuations; ultrametric kills sums; UFD
argument gives the key lemma $p\nmid\operatorname{Im}(\bar\pi^{4m})$).
Corollary: **no 9-square solution has center $w^2$ with $\omega_1(w)\le1$**
(one distinct 1-mod-4 prime) — an unbounded family of centers, beyond
any census. **Strengthened same day** (pattern extraction): the
hypothesis is $\omega_1(w)\le1$ with *arbitrary* $2$- and $3\bmod4$
parts — every $r\equiv3\pmod4$ forces $r\mid u,v$ ($-1$ a non-residue),
so $D((sm)^2)=s^2D(m^2)$; falsification boundary verified ($s=35$
fails, as it must). Bremner's $\omega_1=2$ center consistent. Evidence:
census all $p<2000$, $p^k\le10^9$ (413 families) A2=A3=AP=0
(`primepower_freeness.log`); full proof + failed-attempt tracking in
[notes.md](notes.md).

**Two-prime structure `[mss-two-prime]` (2026-09-01).** For $w=pq$:
closed form $D((pq)^2)=\{p^2Y_q,\ q^2Y_p,\ |X-Y|,\ X+Y\}$ (derived,
builder-verified); census all $p<q\le3000$ (22,155 pairs) A2=A3=AP=0;
valuation profile $\{0,0,0,2{+}v_p(Y_q)\}$ — pigeonhole kills the
prime-power proof's ultrametric mechanism, and the two-prime freeness
question is **open** even at $|D|=4$ (stall + partial mod-$p$
constraints recorded in notes.md).
**$\omega_1$-stratified heuristic `[mss-omega1-stratification]` (2026-09-01,
`mss_omega1_stratification.py`):** bucketing the window-corrected expected
hourglass count by $\omega_1(w)$ (distinct 1-mod-4 primes of $w$) —
validated by reproducing the filed window-corrected total
$H_2=0.07753$ exactly (after self-catching a wrong window upper end:
the theorem's bound is $(u-v)^2-1=w^2-x-1$, not $(2v)^2-1$): at
$W=10^6$ (276,569 centers with $|D|\ge2$; partial sums already carry the
full plane mass) the naive mass $1.00858$ splits
$\{0.147, 0.713, 0.140, 0.008\}$ over $\omega_1=\{1,2,3,4\}$, but the
window-corrected mass $0.07753$ splits $\{0.00004, 0.047, 0.028,
0.002\}$ — **the partner-window theorem alone suppresses the proved-free
$\omega_1=1$ stratum $3{,}700\times$** (theorem-conditioned total
$0.07749$: conditioning the model on the freeness theorem changes
essentially nothing — proof and model are mutually consistent), and
**$97.5\%$ of the surviving expected mass sits at $\omega_1\in\{2,3\}$**
($60.7\%$ at $2$, $36.7\%$ at $3$; per-center intensity rises with
$\omega_1$, $2.1\cdot10^{-7}\to2.0\cdot10^{-6}$, but center counts decay
faster). Under the model a 9-square center (if any exists) has $\omega_1=2$
or $3$ — consistent with Bremner's $\omega_1=2$ center $425=5^2\cdot17$;
the proved condition stops at $\omega_1\ge2$, and an $\omega_1=2$ freeness
theorem (open, `[mss-two-prime]`) would prune the model's largest stratum,
cutting the expected total to $\approx0.030$.

Resolution on a slice (many near-misses; relaxed variants solved) → control
= the full nine-distinct-squares + three-equalities simultaneous system —
a simultaneous-Diophantine control step (the magic-sum + square constraints
are one-dimensional engines that do not compose, echoing the non-composition
obstruction in [[PvsNP]] / [[birch_swinnerton_dyer]]).

## See also
- [[square_of_cubes]] — the cubic sibling (semi-magic, 8/9 near-miss).
- [[PvsNP]], [[birch_swinnerton_dyer]] — non-compositional simultaneous
  construction control.