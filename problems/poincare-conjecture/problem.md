# Poincaré Conjecture

> Problem statement. For the running state, read [progress.md](progress.md)
> first. **STATUS: PROVEN (Perelman 2002–03).** This is the one *solved* Clay
> Millennium problem in the wiki; the folder is a reference / verification /
> control-step-contrast page, not an open-problem attack.

## Statement

Every simply connected, closed (compact, no boundary) 3-manifold is
homeomorphic to the 3-sphere $S^3$.

Equivalently (in the simply-connected setting): the only closed 3-manifold
with trivial fundamental group is $S^3$, up to homeomorphism. (In dimension 3
homeomorphism and diffeomorphism coincide for simply-connected closed
manifolds — Perelman's argument actually yields the stronger $S^3$ up to
diffeomorphism in this case, via Moise.)

Poincaré's original 1904 form is the $n=3$ case of the general question "is a
homotopy $n$-sphere homeomorphic to $S^n$?" — solved in every dimension
**except** $n=3$ by the mid-20th century (Smale $n\ge5$, 1961; Freedman $n=4$,
1982); $n=3$ was the last open case and the hardest.

A Millennium problem (one of the seven Clay Millennium Prize Problems, $1M
prize). **Uniquely among them, it is SOLVED.**

## Status

**PROVEN.** Grigori Perelman posted three arXiv preprints in 2002–2003
completing Richard Hamilton's Ricci-flow-with-surgery program:

- **arXiv:math/0211159** (Nov 2002) — the entropy formula for Ricci flow
  ($F$/$W$ functionals, reduced volume, no-local-collapsing).
- **arXiv:math/0303109** (Mar 2003) — Ricci flow with surgery on 3-manifolds
  (canonical neighborhoods, $\delta$-cutoff surgery, discreteness of surgery
  times, long-time existence).
- **arXiv:math/0307245** (Jul 2003) — finite extinction time on certain
  3-manifolds (sketched; made rigorous by Colding–Minicozzi, JAMS 2005).

Together these prove **Thurston's Geometrization Conjecture**, of which the
Poincaré Conjecture is the simply-connected corollary. The proof was
independently verified:

- Kleiner–Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008).
- Cao–Zhu, *A complete proof of the Poincaré and geometrization conjectures*,
  Asian J. Math. 10 (2006).
- Morgan–Tian, *Ricci Flow and the Poincaré Conjecture* (AMS, 2007).
- Bessières et al., *Geometrization of 3-manifolds* (EMS, 2010).

Clay Millennium Prize **awarded** to Perelman (2010); he **declined** the
prize. Fields Medal (2006) also **declined**. The only solved Millennium
problem.

## The frontier (after the proof)

There is no open frontier for the conjecture itself. Live 3-manifold topology
questions sit at a higher level: effective/bound versions of geometrization,
the Ricci-flow-through-singularities program (via mean-convex mean curvature
flow, e.g. Bamler–Kleiner 2023–), and quantitative curvature-flow questions —
none of these are "the Poincaré Conjecture." This folder's role in the wiki is
**the control-step contrast case**: the one problem where the control step
(reported in [notes.md](notes.md)) was actually *discharged*, validating the
methodology applied to the seven still-open problems.

## See also

- [progress.md](progress.md) — read-first running state (solved status
  front-and-center, the control-step framing as positive validation).
- [notes.md](notes.md) — the Hamilton→Perelman proof sketch through the
  control-step lens; cross-problem contrast (esp. [[navier_stokes]]).
- [attempts/attempt-01.md](attempts/attempt-01.md) — exposition / verification
  attempt of the known proof; honesty-flagged as not an open-problem attack.