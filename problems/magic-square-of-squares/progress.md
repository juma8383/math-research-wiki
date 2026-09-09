# Progress — Magic Square of Squares

> Read-first file (SCHEMA Continue protocol). This problem's full state lives
> in [problem.md](problem.md) (statement + published bounds + censuses +
> heuristic quantification) and [notes.md](notes.md) (the working notebook,
> §§1–2j). This file is the resume pointer only — do not duplicate content.

## Current frontier (2026-09-07)

**Conjecture K34** (two-prime/ω₁=2 sum-freeness of $D((pq)^2)$) is the single
standing obstruction — two-prime freeness ⟺ K34 (`[mss-two-prime-uquad]`,
all other kill-equations K1/K2/K5–K16 dead). K34 is reduced to:

1. **Square-X points on the genus-1 quartics $M_A, M_B$** — MW groups fully
   computed (rank 1, torsion Z/2); genus-3 covers have rank J = 2 < 3
   (**Chabauty gate**: the actual Coleman computation at p=11 is the named
   proof path — notes.md §2h "Chabauty gate"; `#C3_A(F_11)=8`, bound ≤12,
   8 known points).
2. **The odd-depth primitive-divisor gate** (§2e–2g): X(nG)=w² forces even
   depth at every kernel prime; one odd-depth primitive divisor kills.
   Class-0 cosets forced past the effective Verzobio constant (n > 10²⁷²¹ ≫
   C ~ 10⁴¹–10⁴⁴ — §2i, correctly cited); nonzero cosets sit in a window
   BELOW the effective constant (existence there ineffective-only). This is
   a Wall–Sun–Sun-type gap — open unconditionally.
3. **The descent tree** (§2i-adjacent, `[mss-k34-descent]`) — **terminal
   layer now ANALYZED (§2j, `[mss-k34-jacobian]`, 2026-09-07; §2k
   `[mss-k34-liftgate]`, 2026-09-08)**: the four leaf quartics share ONE
   Jacobian $E_a: y^2=x^3+32x^2+238x$ and are exactly its four α-descent
   covers. **Three of the four leaves are PROVED INSOLUBLE** (classes −119,
   17, −34 ∉ image(α) = {1, 238, −14, −17}; rank(E_a)=1 unconditional via
   mwrank 2-isogeny descent) — the Z[√2] UFD descent (old stall item iii)
   and the (8,9)/(9,8) sub-tree are closed. The live leaf C_238 is
   parametrized by the rank-1 fiber $T_a + 2mP_a$; first census-breaking
   admissible point (r,s,u) = (852, 3727, 25318369) — the old "0 hits" leaf
   censuses were BOX-LIMITED (r ≤ 610 < 852). The Fermat/Germain loop on
   the live leaf is EXACTLY the index-halving map on the fiber (verified
   m = 2..28) and closes benignly at odd indices — **stall item (ii)
   resolves NEGATIVELY**. **§2k correction:** the K34-A candidate-chain
   lift is a THIRD quartic gate D (Jacobian J_L, rank 1 unconditional,
   image(α^L) = {1, 238, 271, 64498}) — the candidate lift = class-1 fiber
   of α^L = structurally the same square-x question as K34-A itself; the
   lift gate does not collapse, and the lift-tower question is open.
   **§2l:** two-parents structure (Parent A = the K34-A chain = a FIXED
   POINT of Germain — no descent on the chain that matters; Parent B's
   child lands in the killed (1,238) cell) + a proved **sign gate**
   (boundary X* = 0.19748, dead band = 22.4% of the admissible window) +
   full sweep m = 2..60: **0 candidates** (sign kills 2 indices, D-gate
   fails at all 14 alive ones, exact integers to 10³⁶⁰). **§2m:** the
   7–17 kernel lemma PROVED — gcd(f₁,f₂) = 1 unconditionally, so the
   D-gate is EXACTLY the lift; direct census m = 2..240 (59 admissible,
   9 sign-dead): **0 lifts**; tower height 1 = genus-3 curve
   Z : y² = 8w⁸+1016w⁴+9, Jac(Z) splits 3-ways (J_L + a twist pair,
   11/11 split primes; pair ranks open) — Chabauty-on-Z is the named
   sharpest gate on K34-A. **§2n:** the lift-gate tower corrected to
   Z_D : V² = w⁸−4w⁶−604w⁴−952w²+56644; **W₅(Z_D) = {0,±1}** proved —
   s ≡ 0,±r (mod 5) required, killing 17 of the 50 alive indices.
   **Addendum-2:** Jac(Z_D) ~ J_L × Jac(P) CONFIRMED 9/9 primes with
   P : y² = x·N(x) genus 2 (rational Weierstrass point) — the §2m 3-way
   split belongs to the C₁-octic tower; Chabauty gate = rank Jac(P) ≤ 1,
   hand 2-descent on Jac(P) named next. **§2o:** the **full Z_D mod-p
   sieve kills ALL 50 alive admissible indices (m ≤ 240)** — w = s/r mod
   p ∈ W_p for every p ≤ 499 (exact; rational-infinity exclusion);
   P(ℚ) = {(0,0)} in p ≤ 3000, q ≤ 40. Finite-range kill only; full
   closure still via the Jac(P) rank gate. **§2p:** **±pair RESOLVED —
   K = ℚ(√238)** (27/27 prime character match, exact): Jac(P) =
   Res_{K/ℚ}(E_K), rank Jac(P) = rank E(ℚ(√238)); the Chabauty gate is
   rank E(K) ≤ 1, computable by 2-descent over K. **§2q:** K verified
   34/34 primes (new-prime predictions all confirmed); E_a DISCONFIRMED
   as the factor (p=101 traces (−12,+18) vs ap(E_a)=10); analytic rank
   of Jac(P) (model-independent) in flight. **§2r:** **analytic rank
   Jac(P) = 0** (sum a_p/p flat through p=5000) — **rank Jac(Z_D) = 1 < 3:
   Chabauty applies to Z_D**; known Z_D(ℚ) = degenerate orbit; Coleman
   closure of Z_D(ℚ) would kill the K34-A candidate lift for every m.
   Two Chabauty targets: C3_A and Z_D, both rank 1 < 3. **§2s:** the hand
   2-descent is blocked (N has no rational root — Gordon-Grant rational-
   Weierstrass hypothesis fails); rank Jac(P) = 0 honestly filed as
   ANALYTIC/BSD-CONDITIONAL; Chabauty-on-Z_D gate conditional. **§2u:**
   the **Z_D sieve density quantified** — ρ ≈ 8.92×10⁻²⁵⁵ over p ≤ 499
   (exact): the mod-p layer is essentially exhaustive for any enumerable
   candidate set; the bottleneck is the HEIGHT BOUND (effective Chabauty,
   after the Jac(P) rank-0 proof). Numerical L(s) evaluation running
   (5 s-values, primes ≤ 30000; result to be appended). **§2x:**
   **SageMath 10.9 INSTALLED** (Miniforge/conda-forge, user-local) —
   Simon 2-descent over number fields live (the rank E(ℚ(√238)) tool);
   Jac(P) confirmed SIMPLE over ℚ; Stoll's genus-2 descent still
   Magma-only; Prym construction via trace signature named next. **§2y:**
   **RICHELOT STRUCTURE FOUND (exact)** — N(x) = (x²−2x+238)² − 1084x²,
   1084 = 4·271: the decomposable shape y² = x(h²−d·x²); elliptic quotients
   over L = ℚ(√−271): E± : y² = x³+(±2√−271−2)x²+238x (conjugate, L-rational
   2-torsion at (0,0)); **rank Jac(P) = rank E₊(ℚ(√−271))** via the
   Richelot isogeny — the rank gate is an explicit Sage simon_two_descent
   over L (computation launched). **§2aj:** **RANK GATE CLOSED UNCONDITIONALLY**
   — hand 2-isogeny descent on E₊ over L (after killing the 24h-wedged Sage
   descent): Sel(φ) = {1,238}, Sel(φ′) = {1} ⇒ **rank E₊(ℚ(√−271)) = 0
   PROVED**; rank Jac(P) = 0 upgraded from BSD-conditional to unconditional;
   **rank Jac(Z_D) = 1 < 3: Chabauty gate PASSES**; named remaining: height
   bound, then Coleman on Z_D.

## Honest state

No solution found (Buell's null verified independently to centers ≤ 10¹⁴);
no impossibility proof. Under the window-corrected Euler-product model a
solution is expected NOT to exist (P(0) ≈ 99.996% — model, not proof). K34
open; both named gates open; the descent-tree leaf layer is now fully
analyzed and closed except for one census-level lift condition.

## Single next step

Either (a) the Chabauty–Coleman computation on C3_A at a good prime (rank
2 < 3; PARI/GP + mwrank now run locally — see §2j tooling note), or (b) the
§2k lift-tower question: the candidate lift on the leaf layer = class-1
fiber of α^L on J_L (quartic D, rank 1, no square-x point in the box) —
run the §2j halving-map analysis ON D's own fiber (C₁: y² = 8x⁴+1016x²+9)
to determine whether the lift tower closes at finite height; or (c) the
cheap still-open piece: prove the §2j Fermat-regeneration lift census
(s ± 2ρσ never square) via α-descent on the (1,72) quartic.

## Attempt log

MSS work is filed as notes.md sections + log.md entries (no attempt-NN
files): structural lemmas 2026-08-31 → parallelogram reduction + prime-power
freeness + two-prime structure 2026-09-01 → K34 elliptic + sieve2 + refine
2d–2h + descent 2026-09-01/02 → continuation §2i 2026-09-03
(attribution corrected to Verzobio 2023; leaf census extended 0 hits;
layer-1 bookkeeping reconciled; Bennett–Walsh scope clarified) →
**§2j 2026-09-07** (`[mss-k34-jacobian]`: shared Jacobian E_a of all four
leaves; three leaves insoluble; rank-1 parametrization; halving identity;
stall item (ii) negative; local PARI/GP + mwrank tooling) →
**§2k 2026-09-08** (`[mss-k34-liftgate]`: §2j lift test corrected — the
candidate-chain lift is a third quartic gate D with Jacobian J_L (rank 1
unconditional; image(α^L) = {1, 238, 271, 64498}); candidate lift =
class-1 fiber = structurally K34-A again; lift tower open) →
**§2l 2026-09-08** (`[mss-k34-liftgate2]`: two-parents structure — Parent A
is a Germain FIXED POINT (no descent on the K34-A chain), Parent B dies in
the killed cell; new proved sign gate X < X* = 0.19748 (22.4% of the
admissible window dead); full gate sweep m = 2..60: 0 candidates) →
**§2m 2026-09-08** (`[mss-k34-tower1]`: 7–17 kernel lemma — gcd(f₁,f₂)=1
unconditionally, D-gate ⟺ lift exactly; census m=2..240: 59 admissible,
9 sign-dead, 0 lifts; tower height 1 = genus-3 Z: y²=8w⁸+1016w⁴+9,
Jac(Z) splits 3-ways = J_L + twist pair (11/11 split primes); E_Z-Prym
claim retracted; Chabauty-on-Z named as the sharpest gate on K34-A) →
**§2n 2026-09-08** (`[mss-k34-tower2]`: lift-gate tower corrected to
Z_D : V² = w⁸−4w⁶−604w⁴−952w²+56644; W₅(Z_D) = {0,±1} proved, killing
17 of the 50 alive indices; ±pair candidate A=2178,B=225 discarded on the
full 11-prime filter) → **Addendum-2** (Jac(Z_D) ~ J_L × Jac(P) confirmed
9/9 primes, P : y² = x·N(x) genus 2 with rational Weierstrass point; the
3-way split belongs to the C₁-octic tower; rank Jac(P) ≤ 1 is the gate) →
**§2o 2026-09-08** (`[mss-k34-tower3]`: the full Z_D mod-p sieve kills ALL
50 alive admissible indices (m ≤ 240) — w = s/r mod p ∈ W_p for every
K = ℚ(√238), 27/27 prime character match; gate = rank E(ℚ(√238)) ≤ 1) →
**§2q 2026-09-08** (`[mss-k34-tower5]`: K verified 34/34 primes; E_a
disconfirmed as the factor) → **§2r 2026-09-08** (`[mss-k34-tower6]`:
analytic rank Jac(P) = 0 (flat sum); rank Jac(Z_D) = 1 < 3, Chabauty
applies to Z_D; two Chabauty targets: C3_A, Z_D) → **§2s 2026-09-08**
(`[mss-k34-tower7]`: hand 2-descent blocked — N(x) has no rational root,
Gordon-Grant hypothesis fails; rank Jac(P) = 0 filed ANALYTIC/
BSD-CONDITIONAL; Chabauty-on-Z_D gate honestly conditional).