# Source: P vs NP multi-angle workflow output

**Provenance:** Produced by a 10-agent Workflow (`p-vs-np-attack`, run `wf_65eb3496-963`, 2026-08-21): 8 parallel angle deep-dives + 1 synthesizer + 1 completeness critic. ~508k tokens, 72 tool calls, ~11 min. Each angle agent was instructed to make a *genuine novel attempt*, not just survey, and to report honestly where it broke. Raw structured output stored in the session task output; this file captures the load-bearing claims with stable tags for wiki cross-reference.

## Extracted claims (stable tags — defined here, cited from pages)

- `[bgs-1975]` — Relativization (Baker-Gill-Solovay): oracles A,B with P^A=NP^A and P^B≠NP^B; any relativizing proof fails.
- `[rr-1997]` — Natural proofs (Razborov-Rudich): a "natural" (constructive + large) combinatorial lower-bound property yields a polytime distinguisher breaking PRFs/OWFs.
- `[aw-2008]` — Algebrization (Aaronson-Wigderson): algebraic-oracle worlds with P=NP and P≠NP; arithmetization-based non-relativizing proofs still fail.
- `[williams-2011]` — NEXP ⊄ non-uniform ACC0 via a faster-than-brute-force ACC0-SAT algorithm + easy-witness lemma; non-relativizing, non-natural.
- `[alman-williams-2015]` — Threshold/MAJORITY F_p-approximate degree is Θ√t (tight), NOT polylog like AND/OR.
- `[n2-wall]` — The ACC0 finite-ring trick provably stalls at n² wires for THR∘THR: composed degree Θ√(mt) is tight (contains OR∘AND); ≥2ⁿ monomials at n² wires. A theorem about the class, not the construction.
- `[tamaki-2025]` — Sub-2ⁿ SAT for sub-quadratic depth-2 (SYM∪THR)²; the polynomial method's current frontier.
- `[lss-2025]` — Limaye-Srinivasan-Srinivasan: first #SAT/lower bound for ACC0∘3-PTF via probabilistic rank + Coppersmith.
- `[chen-2018]` — A polylog shaving of Max-IP / ℓ₂-Furthest-Pair ⟹ NEXP ⊄ poly-size THR∘THR. Proven-correct sufficient condition; only the algorithm is missing.
- `[heavy-avoid]` — Lu-Oliveira-Ren-Santhanam 2024: Heavy Avoid problem ⇔ uniform randomized lower bounds against ACC0/TC0/NC1.
- `[mr-2004]` — Mignon-Ressayre: dc(perm_m) ≥ m²/2 via Hessian rank; best unconditional bound, still quadratic.
- `[bip-2019]` — Bürgisser-Ikenmeyer-Panova: no occurrence obstructions for n ≥ m^25.
- `[elsw-2017]` — Efremenko-Landsberg-Schenck-Weyman: shifted partials cannot separate padded perm from det for n > 2m²+2m (a SUM of multiplicities).
- `[fi-2020-asymmetry]` — Fischer-Ikenmeyer: plethysm Sym^d(Sym^n V) is in P for fixed OUTER d, #P-hard for fixed INNER d.
- `[hl-2016]` — Hüttenhain-Lairez: det_3 orbit boundary fully classified (2 components); only n=3 known.
- `[coarsening-gap]` — NOVEL: both `[bip-2019]` and `[elsw-2017]` rule out only COARSE invariants (positivity, sums); fine INDIVIDUAL multiplicity differences are open.
- `[fixed-degree-escape]` — NOVEL strategy: `[fi-2020-asymmetry]` makes the permanent-side plethysm P-time for fixed d, concentrating ALL difficulty on the determinant orbit-closure boundary (unknown for n≥9).
- `[razborov-1995]` — S²_2(α) cannot prove superpoly circuit LBs for SAT if strong PRGs exist.
- `[ps-2021]` — Pich-Santhanam: unconditional — PV_1, T^0_APC1 cannot prove co-nondeterministic average-case LBs.
- `[lo-2023]` — Li-Oliveira: extends to T_i^PV / APC1 for Π_3/Σ_3 (PH-internal, not P≠NP-adjacent).
- `[tell-2018]` — prBPP=prP ⟹ NTIME[n^ω(1)] ⊄ P/poly; and easy-witness proves NP ⊄ P/poly ⟺ P≠NP.
- `[meta-duality]` — NOVEL framing: for a witnessing theory T, "T does not prove LB" is dual to a weak upper bound (interactive protocol / NW-derandomization). Independence is the SAME difficulty as the direct LB, dualized — not a shortcut.
- `[krajicek-prob-3.2]` — Fixed point: affirmative+(ST) ⟹ NP≠coNP; negative ⟹ P≠NP — never both.
- `[egi-2024]` — Efremenko-Garlík-Itykson: Ω(n) rank/width LB for UNRESTRICTED dag-like Res(⊕) on BPHP; no size LB known.
- `[resopl-obstruction]` — Parity inferences re-expand rank under random restrictions; rank is NOT monotone in size in Res(⊕). The diagnosed obstruction to a size-rank conversion.
- `[meir-2023]` — Strong-composition KRW theorem (γ>0.04, barrier 0.64); the "direct-sum obstacle": KW handles tensor direct-product but KRW needs nested composition f∘g.
- `[iyer-rao-2024]` — Deterministic XOR lemma: D(f^⊕n) ≥ n·Ω(D(f))/√(log rk(f)) − log rk(f); entropy/rectangle method.
- `[cavalar-oliveira-2025]` — Explicit super-logarithmic graph-cover-complexity family ⟹ general circuit-SIZE lower bounds; random graphs achieve it but are non-explicit.
- `[seiller-2023]` — Linear realizability characterizes Logspace/Ptime/NLogspace/PPtime via monoid actions; proposes orbit equivalence as a separation tool.
- `[carderi-2021]` — Carderi-Gaboriau-de la Salle: cost extended to p.m.p. groupoids.
- `[semantic-invariant-gap]` — DEEPEST HOLE: P vs NP is a SEMANTIC distinction (∃ witness); existing orbit-equivalence invariants (cost, KS-entropy, ℓ²-Betti) are DYNAMICAL and miss it. Same gap independently surfaces in GCT (need fine multiplicity, not sums). A "quantifier-order-sensitive invariant" is the missing object — identified by two angles, built by none.
- `[algorithmic-gct]` — NOVEL COMBINED ANGLE: import Williams' fast-test + easy-witness paradigm into GCT; seek a SUB-TRIVIAL determinant-hole/multiplicity test at fixed d=2,3, n=Θ(m²), rather than a full algorithm. Central conjecture unverified and may be false (but falsifying it is itself a theorem).
- `[mcsp-gap]` — MISSED ANGLE (critic): meta-complexity / MCSP program (Hirahara; Hirahara-Ilango 2025 conditional NP-hardness of MCSP) was entirely absent; the single most active current direction on circuit lower bounds. Highest-upside long-term target.
- `[missed-angles]` — Other gaps: derandomization/hardness-vs-randomness as a primary axis, hardness magnification, fine-grained/SETH, learning-theory→LBs, Lutz resource-bounded measure, direct algebraic VP-vs-VNP outside GCT, geometric-group/isoperimetric.
- `[status-map]` — 8-angle compressed status (see [[status-map]]).

## Raw artifact note
Full structured output (all 8 angle reports + synthesis + critique) is in the session task output file `…/tasks/wo32pfqgd.output` (431 lines). Not reproduced verbatim here for size; the claims above are its load-bearing content. If a page needs a verbatim quote, retrieve from that file.