---
type: definition
name: Mass gap and confinement
created: 2026-08-24
tags: [mathematical-physics, qft, confinement]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Mass gap and confinement

## Mass gap

A QFT has a **mass gap** $\Delta>0$ if the two-point function decays
$$\langle\phi(0,t)\phi(0,0)\rangle\sim\sum_n A_n e^{-\Delta_n t},\qquad
\Delta_0=\Delta>0,$$
i.e. the lightest excitation above the vacuum has strictly positive mass
[ym-mass-gap]. Equivalently the spectrum of the Hamiltonian above the vacuum
starts at $\Delta>0$.

## Confinement and the Wilson loop area law [ym-confinement-area-law]

Non-abelian YM exhibits **confinement**: color charges are connected by
chromodynamic flux tubes giving a **linear potential** $V(r)\sim\sigma r$.
The diagnostic is the **Wilson loop area law**:
$$\langle W(C)\rangle\sim e^{-\sigma\,\mathrm{Area}(C)}$$
(string tension $\sigma>0$). Consequences:
- no isolated color charges or massless gluons;
- physical states are color-neutral **glueballs**, which are massive.
- The mass gap ensures glueballs have a lower mass bound.

Lattice QCD confirms the mass gap **numerically**; no rigorous analytic proof
in the continuum exists.

## Relation to the problem

The mass gap is the "$\Delta>0$" half of the Millennium problem [[yang_mills]].
It is the IR, strongly-coupled, non-perturbative phenomenon complementary to
asymptotic freedom's UV control [[thm-asymptotic-freedom]]. The two are
bridged by dimensional transmutation [[def-yang-mills-theory]].