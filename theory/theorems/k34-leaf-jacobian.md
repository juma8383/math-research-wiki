---
type: theorem
name: k34-leaf-jacobian-theorem
created: 2026-09-07
tags: [number-theory, elliptic-curves, sha, descent]
used-in: [[magic_square_of_squares]]
provenance: private notes (mss-k34-jacobian, notes.md §2j)
---

# Theorem — K34 leaf quartics: one Jacobian, three insoluble leaves

**Setting.** The four layer-2 leaf quartics of the K34 descent tree
(`mss-k34-descent`):
$$C_{238}:\ u^2=238r^4+32r^2s^2+s^4,\quad
  C_{-119}:\ u^2=32r^2s^2-119r^4-2s^4,$$
$$C_{17}:\ 9u^2=17r^4+32r^2s^2+14s^4,\quad
  C_{-34}:\ 9u^2=32r^2s^2-34r^4-7s^4.$$

**Statement.**
1. All four have binary-quartic invariants $(I,J)=(3880,\,482816)$; their
   common Jacobian is $E_2: y^2=x^3-104760x-13036032$
   ($j=7301384000/9639$), not ℚ-isogenous to the master $E_A$.
2. Writing $E_a: y^2=x^3+32x^2+238x$ (the 2-isogenous partner carrying
   rational 2-torsion $T_a=(0,0)$), the four leaves are exactly the
   $\alpha$-covers $C_d$ ($d\in\{238,-119,17,-34\}$, all $ae=238$) via
   $(X,y)\mapsto(dX^2,\ dXy)$.
3. mwrank (2-isogeny descent, unconditional):
   $\operatorname{rank}(E_a)=1$, $E_a(\mathbb{Q})=\langle P_a\rangle\oplus
   \langle T_a\rangle$, $P_a=(-14,14)$; hence
   $\operatorname{image}(\alpha)=\{1,\,238,\,-14,\,-17\}$.
4. Therefore $C_{-119}$, $C_{17}$, $C_{-34}$ have **no rational points**
   (their classes are nontrivial $\Sha(E_a)[\phi]$ elements), while
   $C_{238}(\mathbb{Q})=\{X^2=x(P)/238: P\in T_a+2E_a(\mathbb{Q})\}$ is
   parametrized by the fiber $T_a+2mP_a$.
5. (Halving identity, verified $m=2,\dots,28$) The Fermat/Germain descent
   loop on $C_{238}$ admissible points maps the fiber point of index $2m$
   exactly to the fiber point of index $m$ (up to the $X\leftrightarrow Z$
   transposition, which lands in the killed $(1,238)$ cell); odd indices
   exit to $C_1$ with $3\nmid r$ — every chain terminates in a killed
   residue class. No infinite-descent contradiction is available on this
   branch.

**Proof status.** Parts 1–4 PROVED (exact integer arithmetic +
mwrank's unconditional 2-descent; scripts `k34j_theorem_check.py`,
`k34j_check_alpha.py`, mwrank log `k34j_mwrank_Ea.log`). Part 5 is an
exact computational verification over all testable indices, not a general
proof — the identity is expected to hold for all $m$ (it is a group-law
identity on $E_a$) but is filed as verified-census. Consequences for the
K34 descent tree: three leaves insoluble, live leaf tame, stall items
(ii)/(iii) resolved negatively/obsoleted. K34 itself unchanged.

**Proof sketch (parts 1–4).** (1) Direct computation of the classical
binary-quartic invariants; identical $(I,J)$ ⟹ isomorphic Jacobians by the
classical invariant theory of binary quartics (Cremona–Stoll normalization).
(2) Substitution identity: for $(X,y)$ on $C_d$, $(dX^2)^3+32(dX^2)^2+238(dX^2)
= d^2X^2(dX^4\cdot d + 32X^2\cdot d + 238)/1\cdot$… $= (dXy)^2$ exactly when
$y^2=dX^4+32X^2+238/d$; degree 2, surjective onto the $\alpha$-fiber.
(3) mwrank first descent: $S^\phi(E'_a)$ 2-rank 1, $S^{\phi'}(E_a)$ 2-rank 4,
second descent shortfall 0 — rank exactly 1, basis found and saturated;
the four α-classes are realized by $\{2P_a,\ T_a,\ P_a,\ P_a+T_a\}$.
(4) Cover solubility criterion (classical, e.g. Silverman XPS, or
mwrank's quartic machinery): $C_d(\mathbb{Q})\ne\varnothing\iff
d\in\operatorname{image}(\alpha)$.