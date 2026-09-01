---
type: theorem
name: Caffarelli-Kohn-Nirenberg partial regularity
created: 2026-08-24
tags: [pde, fluid-mechanics, partial-regularity]
used-in: [[navier_stokes]]
provenance: [[ns-survey]]
---

# Caffarelli-Kohn-Nirenberg (CKN) partial regularity

For **suitable weak solutions** of 3D NS [[def-navier-stokes-equation]], the
space-time singular set has **parabolic Hausdorff dimension $\le 1$** [ns-ckn]
(Caffarelli-Kohn-Nirenberg, 1982; Acta Math.).

## What it says precisely

Singularities (if any) of a suitable weak solution are confined to a set so
small it **cannot contain a space-time curve** — at most 1-dimensional in the
parabolic metric (where time counts double). A smooth solution has no
singular set; CKN bounds how bad a singular Leray-Hopf solution can be.

## Role in the obstruction

CKN is the strongest **unconditional** structural result on singularities:
even if blowup occurs, it is geometrically tiny. But "tiny" $\ne$ "empty" —
CKN does NOT rule out blowup, and does not prove regularity. It is consistent
with both global regularity and a measure-$\le1$ blowup set. Like the
conditional criteria, it is a resolution-layer tool that characterizes
singularities without producing (or ruling out) them. The obstruction — a
global critical bound [[method-energy-supercriticality]] — is untouched.