---
type: lemma
name: k34-lift-gate-quartic
created: 2026-09-08
tags: [number-theory, elliptic-curves, descent, covering-towers]
used-in: [[magic_square_of_squares]]
provenance: private notes ([mss-k34-liftgate], notes.md §2k)
---

# Lemma — the K34-A candidate lift is a square-x question on a third quartic

**Setting.** Leaf fiber point of C₂₃₈ (on E_a, `[mss-k34-jacobian]`):
$(r,s,u)$, $n_{L2}=s^4-238r^4$, candidate-chain layer-1 preimage
$(u,\pm rs,\ n_{L2})$ with lift condition $n_{L2}\pm2u\cdot(rs)=(a\pm b)^2$.

**Statement.**
1. (Reduction) $n^2-4u^2(rs)^2 = r^8 N\!\big((s/r)^2\big)$ exactly, where
   $N(x)=x^4-4x^3-604x^2-952x+56644$. So the candidate lift holds ⟺
   $N(X^2)$ is a rational square at $X=s/r$.
2. $D: V^2=N(x)$ has binary-quartic invariants $(1033120,\,-2092277248)$;
   its Jacobian $J_L: y^2=x^3-27894240x+56491485696$ is NOT isogenous to
   $E_a$ or $E_2$ (bad primes {2,3,7,17,271} vs {2,3,7,17}).
3. mwrank (unconditional): rank$(J_L)=1$, $J_L(\mathbb{Q})=\langle G_L\rangle
   \oplus\langle T\rangle$, $G_L=(2472,51408)$, $T=(-6096,0)$. Shifted
   ($X=x+6096$): $\operatorname{image}(\alpha^L)=\{1,238,271,64498\}$ —
   $\alpha^L(G_L)=238$: **the master constant 238 recurs as a generator's
   square class**.
4. $D(\mathbb{Q})$ contains $(0,\pm238)$ and $(-33/2,\pm5/4)$; no point with
   $x$ a positive rational square was found in $p\le400$, $q\le40$. PARI
   `ell2cover(J_L^sh)` gives exactly two soluble covers, $C_1: y^2=
   8x^4+1016x^2+9$ (the class-1 fiber) and $C_2: y^2=9x^4+168x^3+566x^2
   -1312x+477$; all three quartics share $(I,J)=(1033120,-2092277248)$.
5. **Structural conclusion:** the K34-A candidate lift = class-1 fiber of
   $\alpha^L$ on $J_L$ = a square-x question of the SAME shape as K34-A
   itself. The lift gate does not collapse by rank-0; it recurses.

**Status.** Parts 1–3 PROVED (exact arithmetic + mwrank unconditional
descent); part 4 verified-census (finite box); part 5 structural
interpretation. Scripts `k34j_lift_gate_D.py`, `k34j_lift_verify_m2.py`,
`k34j_gate_final.py`, `k34j_mwrank_JL.log`.

**Why it matters.** Together with §2j this exhibits a **lift tower**: each
height's gate quartic has a rank-1 Jacobian carrying 238 in its α-image,
and "the lift condition at height h" is "the K34-A question at height h+1."
If the tower's fibers are all isogenous copies (they are so far: E_a's
class-1 fiber quartic is C₁ with the SAME Jacobian J_L as D), the tower
either closes by a finite-height argument or reduces K34-A to a
self-similar obstruction — the structural analogue of the Wall–Sun–Sun
gap already named in §2e–2g.