---
type: theorem
name: Balaban renormalization group for lattice Yang-Mills
created: 2026-08-24
tags: [mathematical-physics, qft, renormalization-group]
used-in: [[yang_mills]]
provenance: [[ym-survey]]
---

# Balaban RG and the constructive-continuum machinery

The machinery aimed at controlling the continuum limit of lattice YM
[[thm-lattice-gauge-constructive]].

## Balaban (1984-89)

A **multi-scale renormalization group** for lattice gauge theory, iterating
integrated-out scales to control the UV (small-scale) behavior. Balaban
established **UV stability** bounds — controlling the short-distance
renormalization needed for a continuum limit.

## Magnen-Rivasseau-Sénéor (1993)

Constructed **YM₄ with an infrared cutoff** — a rigorous YM measure at finite
volume with UV control, but with an IR regulator still in place. Removing the
IR cutoff (infinite volume) and taking $a\to0$ together is the open step.

## Aizenman-Fröhlich-Spencer (1982) infrared bound

A probabilistic **infrared bound** controlling the IR of lattice models; a
key ingredient (adopted as a technical hypothesis for $SU(N)$ by recent
attempts [ym-recent-claims-unverified]).

## Role in the obstruction

This is the **continuum-limit control machinery** — the engine for direction
(A) [[method-constructive-continuum-limit]]. It is **incomplete**: full
control (convergence + $O(4)$ covariance + uniform-in-$a$ gap transport) is
not proved. Recent preprints rely on its bounds as (often unverified)
hypotheses [ym-recent-claims-unverified]. [to-verify: exactly what Balaban's
RG proves vs leaves open.]