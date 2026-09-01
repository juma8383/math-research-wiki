# Research Protocol (standing instructions for every conjecture)

> **Apply this to every Attack / Continue on any conjecture, every session.**
> This is the standing research discipline for the math wiki. It *strengthens*
> (does not replace) the SCHEMA.md workflows and the cross-problem
> "obstruction at the control step" methodology. Index entry:
> [research-protocol](research-protocol.md).

You are conducting mathematical research. **Never stop at the first plausible
proof.** A single plausible argument is a hypothesis, not a result.

## The 10-step protocol (run on every conjecture)

1. **Generate evidence.** Gather facts, known results, analogues, computational
   data that *support* the conjecture. File into the problem's `progress.md`
   "verified base."
2. **Generate counterevidence.** Actively look for what would *refute* it:
   known counterexamples, integral/torsion obstructions (cf. Hodge), the
   "naive strong statement is false" wrinkle, claimed solutions that fail.
   Record under a "counterevidence" note in `notes.md` and flag `to-verify`.
3. **Produce at least three distinct proof approaches.** Never pursue a single
   line. The six problems each already carry directions (A)/(B)/(C); a fresh
   attack must add or sharpen at least three genuinely distinct angles
   (different machinery, not three parameter tweaks). File each as a
   candidate direction; reject an attack that offers only one.
4. **Seek counterexamples.** For each approach, ask "what inputs would break
   this?" — and compute/search them. (Beal's computational probes, NS's
   blowup-rate bounds, Collatz's verification to $2^{68}$ are the template.)
5. **Formalize all assumptions.** State every hypothesis the argument leans
   on, including "framework exists" assumptions (YM), "integral vs rational"
   (Hodge), "almost-all vs pointwise" (Collatz). Unstated assumptions are the
   usual failure mode.
6. **Track all failed attempts.** Append-only in `attempts/`. A dead end is
   reusable knowledge — record *why* it failed (the obstruction), not just
   that it did. This is the wiki's compounding engine.
7. **Derive simpler equivalent statements.** Reduce to the smallest open
   instance (Beal's $(3,5,7)$; BSD's analytic rank $\ge2$; NS's large 3D data;
   YM's continuum limit; Hodge's codim-2 on a 4-fold; Collatz's a single
   divergent trajectory / a single nontrivial cycle). A clean equivalent is a
   frontier.
8. **Derive more general statements.** Lift to the natural generalization
   (Fermat–Catalan / generalized Hodge (coniveau) / Matthews–Watts /
   generalized Collatz undecidability). A generalization that stays open
   confirms the obstruction is structural; one that becomes trivial localizes
   it.
9. **Check computational examples.** Run small cases — by hand, script, or
   search. Verify load-bearing arithmetic *before committing* (Beal's
   attempt-17 caught a silent $41/42>1$ error this way; that discipline now
   applies to every problem).
10. **Re-evaluate confidence.** After a round, assign an honest confidence
    level per direction and per sub-claim. Downgrade on counterevidence;
    upgrade only on verified primary-source facts. Record in the attempt's
    closing "Honesty / confidence" block.

## The research notebook

Each problem folder **is** the research notebook; keep it current:
- **Known facts** → `progress.md` "verified base" + `theory/` pages (claim tags).
- **Conjectures** → `theory/conjectures/` pages + sparks in `notes.md`.
- **Failed conjectures** → dated correction blockquotes in attempts (append-only)
  + the superseded claim flagged, never silently deleted.
- **Counterexamples** → recorded in the relevant attempt with the exact input.
- **Partial proofs** → the `attempts/` with `outcome: partial`, frontier named.
- **Open problems** → `progress.md` "open content" + `to-verify` list.

## When progress stalls — change the frame

Do not grind the same representation. Cycle through, in order:
- **Change representation** (e.g. Collatz $T$ ↔ accelerated Syracuse; BSD
  $L$-function ↔ Selmer group).
- **Change notation** (rename to expose structure; Beal's reciprocal invariant
  $\chi$).
- **Search analogous problems** (the cross-problem `related:` links and the
  6-for-6 obstruction map are exactly this — use them).
- **Generalize** (step 8) and **Specialize** (step 7) — both, alternating.
- **Reverse the problem** (assume the negation / a counterexample and derive
  a contradiction or a structure — Collatz's "assume a divergent trajectory",
  Hodge's "assume a non-algebraic Hodge class").
- **Seek dual statements** (YM continuum↔Minkowski/OS; Hodge analytic↔algebraic;
  BSD analytic rank↔algebraic rank).

## Critique every conclusion before accepting it

Before any claim leaves an attempt into `progress.md`/`theory/`:
- Is every assumption formalized (step 5)?
- Has counterevidence been sought (step 2) and counterexamples checked (step 4)?
- Is the arithmetic verified against a primary source or computation (step 9)?
- Would the cross-problem obstruction map predict this? If a claim contradicts
  the established control-step obstruction for that problem, treat it as
  suspect until verified.

This is the discipline that caught Beal's (2,3,7) spherical mislabel, BSD's
to-verify items, YM's and Hodge's and Collatz's unverified preprint flurries.
**Honesty over optimism. Flag to-verify. Append-only corrections.**