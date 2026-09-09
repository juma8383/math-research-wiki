---
type: dag
problem: navier-stokes
last-updated: 2026-09-09
---

# Proof DAG — navier-stokes

Live frontier: global regularity for large 3D data (or a true-NS
blowup); the obstruction is the critical-norm control step — the only
unconditional global bound is the subcritical energy
(method-energy-supercriticality), and 3D is supercritical ($S=4>3.5$).

- id: navier-stokes-itself
  kind: conjecture
  status: open
  uses: [navier-stokes-equation, local-wellposedness, leray-weak-solutions, serrin-regularity, beale-kato-majda, caffarelli-kohn-nirenberg, energy-supercriticality, tao-averaged-blowup]
  source: [[navier_stokes]]
  next: the missing control step is a global a priori bound on a
    critical norm ($L^3$/$\dot H^{1/2}$) — open leaves: (A) a critical
    a priori bound, (B) a non-self-similar true-NS blowup bridging
    generalized to true viscosity (attempt-04/05)
- id: navier-stokes-equation
  kind: definition
  status: open
  uses: []
  source: [[navier-stokes-equation]]
  next: —
- id: local-wellposedness
  kind: theorem
  status: proven
  uses: []
  source: [[local-wellposedness]]
  next: small-data global regularity is resolution-side; no
    data-independent rate — the control step to large data is open
- id: leray-weak-solutions
  kind: theorem
  status: proven
  uses: []
  source: [[leray-weak-solutions]]
  next: uniqueness of Leray-Hopf solutions still open; Hou-Wang-Yang
    2026 computer-assisted nonuniqueness claim is the top to-verify
    item (attempt-08) and does not touch regularity
- id: serrin-regularity
  kind: theorem
  status: proven
  uses: []
  source: [[serrin-regularity]]
  next: endpoint $L^\infty L^3$ (ESS 2003) — a global $L^\infty L^3$
    bound would prove regularity; the bound itself is the open
    control step
- id: beale-kato-majda
  kind: theorem
  status: proven
  uses: []
  source: [[beale-kato-majda]]
  next: —
- id: caffarelli-kohn-nirenberg
  kind: theorem
  status: proven
  uses: []
  source: [[caffarelli-kohn-nirenberg]]
  next: strongest unconditional structural bound (singular set dim
    $\le1$) — does not rule out blowup
- id: energy-supercriticality
  kind: method
  status: open
  uses: [navier-stokes-equation, serrin-regularity]
  source: [[energy-supercriticality]]
  next: the unifying lens — energy ($L^2$, subcritical) cannot control
    the scale-invariant critical norm; Serrin-number equality is why
    2D is solved and 3D is not
- id: tao-averaged-blowup
  kind: theorem
  status: proven
  uses: []
  source: [[tao-averaged-blowup]]
  next: the averaged/modified NS model blows up (resolution side) —
    the control step (averaged to true NS) is the wall; the 1D
    Hou-Li engine now achieves blowup fully analytically
    (attempt-07/08) and stops at the 1D-to-3D control step