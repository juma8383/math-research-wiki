---
type: theorem
name: Leray-Hopf weak solutions
created: 2026-08-24
tags: [pde, fluid-mechanics, analysis, weak-solutions]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Leray-Hopf weak solutions

For any divergence-free $u_0\in L^2$ there exists a global-in-time **weak
(Leray-Hopf) solution** [[def-navier-stokes-equation]] satisfying the energy
inequality [ns-leray-weak]:
$$\|u(t)\|_{L^2}^2 + 2\nu\int_0^t\|\nabla u(s)\|_{L^2}^2\,ds\le\|u_0\|_{L^2}^2.$$
- **Leray (1934)** ($\mathbb R^3$), **Hopf (1951)** (bounded domains).
- The set of singular times has box-counting dimension $\le 1/2$.

## What is NOT known

- **Uniqueness**: Leray-Hopf weak solutions are not known to be unique.
  Uniqueness would be a major step (a Clay-adjacent open problem).
- **Regularity**: a Leray-Hopf solution is not known to be smooth; where it is
  smooth it agrees with the strong solution.
- **Buckmaster-Vicol (2017)** [ns-buckmaster-vicol]: non-uniqueness holds for
  "very weak" solutions (non-Leray-Hopf; they do NOT satisfy the energy
  inequality) — so non-uniqueness is known only *below* the Leray-Hopf class.

## Role in the obstruction

Leray-Hopf solutions show a global object exists, but at subcritical ($L^2$)
regularity — the energy-controlled level. The Millennium problem asks for
global smoothness, i.e. lifting the Leray-Hopf solution to critical regularity,
which needs the missing critical bound [[method-energy-supercriticality]].