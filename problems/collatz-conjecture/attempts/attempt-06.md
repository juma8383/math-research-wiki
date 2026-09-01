---
type: attempt
problem: collatz_conjecture
attempt: 6
date: 2026-08-25
approach: Status-check the 2024-26 claimed-proof preprints (attempt-05 option (a), the deferred attempt-04 target) — verify peer-review/reception status of Fathi 2025 / Nwankpa 2025 / Chang 2026 and any sibling claims
outcome: confirmed
tags: [verification, status-check, claimed-proofs, preprint-wave, control-step, average-vs-pointwise, cross-problem, refutation, machine-review]
---

# Attempt 06 — 2024-26 Collatz claimed proofs status-checked: ALL unreviewed, ALL fail at the average→pointwise control step (one REFUTED); the 6-for-6 wall reinforced from the negative side

Cycle-3/new-run Continue on Collatz (resumed /loop; yellow zone, weekly 71.9%
/ session 13%, 0 subagents — one targeted WebSearch; weekly ~3% below the
75% pause threshold, so budget-conservative). Attempt-05's `Next` option
(a): status-check the **2024-26 claimed-proof preprints** (Fathi 2025 /
Nwankpa 2025 / Chang 2026) — the one remaining attempt-04 target deferred
for budget. This cycle closes it. **Headline: NONE of the flagged preprints
is peer-accepted; each fails at exactly the average-vs-pointwise control
step the wiki named (the 6-for-6 wall); and the search surfaced 2-3 sibling
2025-26 claims — including one REFUTED by counterexample.** The control-
step obstruction is reinforced from the *negative* side (every amateur
attempt hits the same wall). Same append-only-honesty discipline as YM
Agawa (retracted) / Hodge Tate⟺BSD (scope-refined).

## The three flagged preprints — status-checked

### Fathi 2025 — THREE Zenodo preprints, all unreviewed, all distributional

**Kevin Fathi** posted not one but **three** claimed proofs on **Zenodo**
(a CERN-hosted DOI-assigning preprint server — DOI assignment ≠ peer
review) in 2025:

1. *A Proof of the Collatz Conjecture via Recursive Type Arithmetic and
   Entropy Descent* (Zenodo, 2025-04-10, DOI 10.5281/zenodo.15191755) —
   "entropy descent" via bit-length $H(n)=\lfloor\log_2 n\rfloor$ + a
   compressed Collatz operator; argues entropy decreases **in expectation**
   via $\mathbb E[k(n)]=2>\log_2 3$. **This IS the standard average-
   contraction heuristic** — distributional, not pointwise; does not exclude
   a measure-zero exceptional divergent/cyclic orbit. Confirms attempt-05's
   "Fathi 2025 ('entropy descent' = the standard average-contraction
   heuristic)" framing exactly.
2. *A Complete Proof via Adaptive Potential Descent, Symbolic Compression,
   and Modular Exhaustion* (Zenodo, 2025-04-30, DOI 10.5281/zenodo.15313916)
   — potential-function descent + modular exhaustion up to mod 32.
3. *Kolmogorov Compression Bounds and the Termination of Collatz
   Trajectories* (Zenodo, 2025-05-29, DOI 10.5281/zenodo.15549017) —
   Kolmogorov-complexity termination argument.

**All three: 0 citations, not peer-reviewed, not on arXiv.** The first is
the named "entropy descent" item; the other two are siblings. **Verdict:
Fathi = unreviewed Zenodo preprints; the load-bearing one fails at the
average-vs-pointwise control step (distributional $\mathbb E[k]=2$ ≠
pointwise).** Flag RESOLVED.

### Nwankpa 2025 — Preprints.org, a fundamental FSM-reduction flaw (correction)

**Amarachukwu Nwankpa**, *The Collatz Conjecture: A Graph-Theoretic
Structural Proof*, **Preprints.org** (2025-10-22, v9, DOI
10.20944/preprints202503.0929.v9) — claims a proof via a **17-state finite
state machine (FSM) on mod-9 residue classes**: the transient states form a
single strongly connected component with a unique exit to the terminal
cycle $\{1,2,4\}$.

**Fundamental flaw:** reducing an **infinite-state** problem (all positive
integers) to a **17-state FSM via modular residues** captures only the
modular residue, **not the magnitude** of the number. The "unique exit"
through state $S_{11}$ (representing $n=8$) shows only that the residue
$8\bmod 9$ provides an exit — **not** that every trajectory passes through
the actual value $n=8$. **Append-only correction of the progress.md
honesty-check:** attempt-05/progress.md wrote "Nwankpa 2025 (mod-4/12,
gaps in the accelerated-map accounting)." The actual mechanism is a
**mod-9 FSM** (not mod-4/12); the flaw is the modular-residue≠magnitude
reduction (more fundamental than "accelerated-map accounting gaps"). The
"unreviewed + fails at the control step" verdict is unchanged; the
mechanism label is corrected here.

**Preprints.org (not peer-reviewed), 0 citations, not on arXiv.** Flag
RESOLVED.

### Chang 2026 — the most substantial & HONESTLY FRAMED; explicitly NOT a proof

**Edward Yi Chang**, *Exploring Collatz Dynamics with Human-LLM
Collaboration*, **arXiv:2603.11066** (submitted 2026-03-10) — the most
substantial and honestly framed of the three. **Explicitly does NOT claim
a proof.** It presents:

- A **conditional framework** reducing Collatz to an **"Orbit
  Equidistribution Conjecture"** (open) — confirms attempt-05's "Chang 2026
  (honestly conditional on an open equidistribution conjecture)" framing.
- Several **unconditional structural results**: Scrambling Lemma, 1/4
  Persistent-Transition Law, Known-Zone Decay.
- An **honest acknowledgment** that the key hypotheses remain open.
- A **documented self-correction** of a false lemma — the "Gap Lemma"
  claiming $G_i=1$ always was found false (gaps of length 2 constitute
  ~19% of gaps).

Reviewed by **Pith** (a **machine-review** platform — *not* human peer
review), which gave a **"CONDITIONAL"** verdict: the "Paradigm Exhaustion
Theorem" rests on an unverified completeness claim; computational results
lack error analysis. **On arXiv but NOT peer-reviewed by a journal;
explicitly exploratory.** Flag RESOLVED + sharpened (machine-reviewed
CONDITIONAL, Gap Lemma self-corrected).

## Sibling 2025-26 claims surfaced by the search (not in the original three)

- **Eduardo Santana**, *On the Collatz Conjecture: Topological and Ergodic
  Approach*, **arXiv:2601.03297** (2026-01) — **REJECTED** by Pith review;
  the main theorem is **REFUTED by the counterexample $f_0(n)=n$** (which
  gives infinitely many fixed points in the paper's own family of maps);
  Lemma 14's converse unsupported; the abstract overclaims a "no divergent
  orbits" result not proved in the body. **A refuted claimed proof** — the
  cleanest non-result of the batch (the $n\to n$ fixed point is a trivial-
  to-check counterexample in the family). *(Refutation search-surfaced via
  the Pith review; flagged minor to-verify the refutation directly, but the
  counterexample is self-evident.)*
- **Toshiharu Kawasaki**, *A proof of the Collatz conjecture*,
  **arXiv:2502.20642** (2025-02) — fixed-point-theorem approach; not peer-
  reviewed; widely considered flawed by experts.
- **Fabrice Trifaro** (viXra, 2025-06) — "R-Cz sequences" + cardinality;
  viXra (not arXiv), not peer-reviewed.
- **Xavier J. Régent**, *The Collatz Conjecture through the Lens of the
  Nitescu Theorem …* — PhilPapers listing; not peer-reviewed.

## The 6-for-6 wall, reinforced from the negative side (the load-bearing finding)

Every 2025-26 claimed proof fails at **exactly the average-vs-pointwise
control step** the wiki named (attempt-02 direction (A-ii), attempt-04
$\Pi^0_2$-completeness):

- Fathi: distributional $\mathbb E[k]=2>\log_2 3$ (the **Terras/Allouche-
  Korec average-contraction engine**, which stops at density-1 — attempt-03's
  "one-dimensional engine stops" #1).
- Nwankpa: modular-residue FSM (captures residue, not magnitude — a
  **finite-slice** engine that cannot control the unbounded magnitude /
  pointwise orbit).
- Chang: honestly conditional on an **Orbit Equidistribution Conjecture** —
  the **Tao log-density↔natural-density control gap** (attempt-02 (A-i),
  the $\exp(O(n^{1/2}))$ error) made explicit as an open hypothesis.
- Santana: refuted (a fixed-point family overclaim).

So the amateur preprint wave is a **negative-side confirmation of the
obstruction**: the wall the wiki derived from the *positive* frontier
(Tao's log-density limit, Terras/Krasikov-Lagarias stopping at density-1,
$\Pi^0_2$-completeness ruling out a uniform argument) is the **same wall**
every claimed proof hits. This is **corroborative, not probative** (an
attempt failing does not prove the problem is hard) — but it is a real
convergent signal, parallel to the YM Eriksson self-concession (attempt-06,
this same run) and the Hodge/BSD control-step triangulation.

## What this changes in the obstruction map

- **All three flagged preprints: status RESOLVED — none peer-accepted.**
  Fathi = 3 unreviewed Zenodo preprints (distributional, fail at average-
  vs-pointwise); Nwankpa = unreviewed Preprints.org, **mod-9 FSM** reduction
  flaw (correction: not "mod-4/12"); Chang = arXiv, **honestly conditional**
  on an open Orbit Equidistribution Conjecture, machine-reviewed
  (Pith) CONDITIONAL, Gap Lemma self-corrected. Plus 2-3 sibling claims
  surfaced (Santana REFUTED, Kawasaki flawed, Trifaro viXra).
- **Nwankpa mechanism CORRECTED (append-only):** mod-9 FSM (not mod-4/12);
  the flaw is modular-residue≠magnitude reduction.
- **`collatz-recent-claims-unverified` flag: REINFORCED + expanded.** Now
  covers Fathi×3 / Nwankpa / Chang / Santana(refuted) / Kawasaki / Trifaro
  — a 2024-26 wave, all unreviewed, all hitting the control step.
- **6-for-6 wall reinforced from the negative side:** the average-vs-
  pointwise control step is where every claimed proof fails — corroborative
  convergence with the positive-frontier derivation.
- **No change to the Collatz frontier** (pointwise/universal control
  remains open; Tao 2019/22 the strongest rigorous result; $2^{68}$
  peer-reviewed / $2^{71}$ project-reported the computational frontier).

## Honesty / scope

- **All items are unreviewed preprints** (Zenodo / Preprints.org / arXiv /
  viXra / PhilPapers); **NONE peer-accepted or journal-published.** Zenodo
  assigns DOIs but is NOT peer-reviewed; Preprints.org and viXra likewise;
  arXiv is unmoderated. This is the same publication-status discipline as
  YM Faizal-Shabir / NS Hou-Seregin / Hodge Shimizu.
- **Pith is a MACHINE-review platform, not human peer review** — a Pith
  verdict (CONDITIONAL / REJECTED) is an automated assessment, NOT
  community acceptance. Flagged honestly (Chang CONDITIONAL, Santana
  REJECTED both via Pith).
- **The Santana refutation** ($f_0(n)=n$ counterexample) is search-surfaced
  via the Pith review; the counterexample itself (a fixed point in the
  paper's own family) is trivial to check, but I did not read the arXiv
  body line-by-line — flagged minor to-verify the refutation directly.
- **Corroborative not probative:** amateur attempts failing at the control
  step do NOT prove the problem is hard or the obstruction correct — only
  a weak convergent signal. The wiki's obstruction rests on the *positive*
  frontier (Tao, Terras, Krasikov-Lagarias, $\Pi^0_2$-completeness), which
  is unchanged.
- No proof of Collatz. The conjecture remains **OPEN**; strongest rigorous
  result Tao 2019/22 (almost all almost-bounded); computational frontier
  $2^{68}$ (peer-reviewed) / $2^{71}$ (project-reported).
- Outcome: **confirmed** (all flagged preprints status-resolved as
  unreviewed + control-step-failing; Nwankpa mechanism corrected; sibling
  claims incl. a refutation surfaced; 6-for-6 wall reinforced from the
  negative side), **partial** overall (frontier unchanged).

## Next (attempt-07)

Remaining deferred items: (b) primary-source-verify the **$2^{71}$ bound
against a publication** if Barina publishes the extension (currently
project-reported, unreviewed); (c) deepen a direction (A/B/C) sub-thread
— e.g. the (A-i) $\exp(O(n^{1/2}))$ Syracuse-error control, or the (B-
uniform) irrationality-measure wall. The rotation continues; weekly ~72%,
approaching the 75% pause threshold — the next cycle must re-check weekly
before a heavy move.