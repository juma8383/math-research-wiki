---
type: theorem
name: Conway (1972) — undecidability of generalized Collatz maps
created: 2026-08-24
tags: [number-theory, dynamical-systems, computability, collatz]
used-in: [[collatz_conjecture]]
provenance: [[collatz-survey]]
---

# Undecidability of generalized Collatz maps (Conway)

## Conway (1972)

A **generalized Collatz-type map** (Conway map) is a piecewise-linear map
$T(n)=(m_i n-r_i)/p$ on residue classes mod $p$. Conway proved such maps can
**simulate a universal Turing machine**, so the question "does a given
trajectory eventually cycle?" (a generalized halting problem) is
**undecidable** in general [collatz-conway-undecidable].

## 3n+1 is a "weak" / contracting case

The original Collatz map is far below the universality threshold. The
**Matthews–Watts** framework classifies such maps by a growth parameter
$\mu$ [collatz-matthews-watts]:
- **Contracting** ($\mu<p^p$): all trajectories conjectured ultimately cyclic.
  For 3n+1, $\mu=3<4=2^2$ — contracting; no divergent trajectory expected.
- **Expanding** ($\mu>p^p$): almost all trajectories conjectured divergent
  (experimentally ~1.3% of starts diverge for $\mu=28>27=3^3$).

## Role in the obstruction map

This is a **framework / diagonalization** context, not a resolution of 3n+1:
- Conway's undecidability is for *general* maps; it does **not** prove 3n+1
  is undecidable (a common overclaim to avoid). It shows the *family* of
  problems 3n+1 belongs to is undecidable, so there is no universal algorithm
  — but a 3n+1-specific proof may well exist.
- This parallels YM's "framework itself is open" wrinkle [[yang_mills]] and
  the spectral-gap undecidability (Cubitt et al.): a general undecidability
  result that does not preclude a problem-specific proof. Flagged, not
  asserted. A candidate attempt-02 line: is there a 3n+1-specific
  independence/undecidability result (Kurtz–Simon 2007)?