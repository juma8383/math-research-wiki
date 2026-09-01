---
type: attempt
problem: beals_conjecture
attempt: 16
date: 2026-08-24
approach: Close-out consolidation — update synthesis.md to reflect the full 15-attempt arc and the unifying triangle-group lens
outcome: partial
tags: [synthesis, close-out, consolidation, state-of-attack]
loop_cycle: 14 of 20
---

# Attempt 16 — Close-out consolidation of `synthesis.md`

With 15 attempts filed and two Lint passes clean, the loop enters its final
stretch. This cycle consolidates `synthesis.md` so it fully reflects the
15-attempt arc and is a complete, self-contained handoff for the next session.

## What changed in `synthesis.md`

1. **Unifying lens added** to the "hard kernel" section: the five threads are
   not just five independent failures but **five symptoms of one structural
   absence** — no finite group at a hyperbolic signature. The
   spherical/hyperbolic triangle-group distinction ($\Delta(p,q,r)$ finite iff
   $1/p{+}1/q{+}1/r>1$) explains *why* both thread 5 (spherical reduction) and
   direction (B) (effective geometric descent, PSS) are unavailable at
   $(3,5,7)$. (From attempt-14.)

2. **Computational state expanded**: added the attempt-12 exhaustive
   $(3,5,7)$ gap-1 classification (4 hits, all degenerate + universal-family,
   0 genuine, min gap 29) and the attempt-13 $(3,5,11)$ probe (0 exact, 0 genuine
   gap-1, all degenerate on $t^{33}{+}1$/$t^{55}{+}1$, min gap 77), stating the
   rigidity is **uniform across the open class and monotone in the exponents**,
   plus the general degenerate-family formula
   $t^{\operatorname{lcm}(p,r)}{+}1$, $t^{\operatorname{lcm}(q,r)}{+}1$. Added the
   honest box-scope caveat.

3. **To-verify items** updated: added the PSS `pss2007` mechanism (ingested
   from a search summary, to verify against paper), with the note that the
   spherical-triangle-group finiteness criterion is standard/robust regardless.

4. **Attempt index table** extended from 8 to 15 rows (attempts 09–15 added).

5. **Bottom line rewritten** as a structured close-out: frontier, open content,
   obstruction (reduction not resolution; hyperbolic no-finite-group unifier),
   empirical uniformity, and the two candidate proof directions, ending with the
   compounding-artifact statement (the map is the durable handoff).

## Why consolidate now

The diagnostic arc is essentially complete: every classical tool is mapped to a
failure, the failures are unified by one structural fact, the open class is
empirically confirmed rigid and uniform, and the two forward directions are
named with their precise missing pieces. Further cycles add marginal value
unless they (a) verify a flagged item against a paper, or (b) introduce a
genuinely new idea. Consolidating now ensures the wiki's single canonical
reference (`synthesis.md`) is the complete handoff — a fresh session reading it
reaches the full state of the attack without reading 15 attempt files.

## Honest outcome

**partial — consolidating, not advancing.** No new mathematics; the value is
durability and a single-source-of-truth handoff. The substantive research arc
ran attempts 01–14; 15–16 are maintenance/consolidation. Remaining cycles
(15–20) should be low-risk: final Lint, optional paper-verification of flagged
items, and a clean loop close.

## Next cycles (6 remain)

- Optional: verify the PSS `pss2007` descent details against the actual paper
  (the one substantive to-verify item with real content).
- Final Lint pass.
- A short "loop close-out" attempt summarizing the 20-cycle run for the log.
- Guard against fabricating progress: if no genuine new angle appears, the
  honest move is to declare the arc complete rather than pad.