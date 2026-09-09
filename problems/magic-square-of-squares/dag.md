---
type: dag
problem: magic-square-of-squares
last-updated: 2026-09-09
---

# Proof DAG — magic-square-of-squares

Live frontier: the K34 ladder — two-prime sum-freeness iff Conjecture
K34 (kill list down to K3/K4 only); the K34-A candidate chain closes
via the two Chabauty targets (C3_A and Z_D, both rank 1 < 3), with
rank Jac(Z_D) = 1 < 3 now proven unconditionally (selmer2i).

- id: mss-itself
  kind: conjecture
  status: open
  uses: [k34-conjecture]
  source: [[magic_square_of_squares]]
  next: two-prime sum-freeness iff K34 (kill equations K1-K16 dead
    except K3/K4, gated on K34) — K34 closure is the single standing
    obstruction; expected-null heuristic says no 9-square center
    exists ($P\approx99.996\%$, model not proof)
- id: k34-conjecture
  kind: conjecture
  status: open
  uses: [k34-leaf-jacobian, k34-lift-gate-quartic, c3a-coleman-gate, zd-chabauty-gate]
  source: problems/magic-square-of-squares/progress.md
  next: A(n), B(n) never hold (K3+K4 die); the K34-A candidate lift
    chain closes via the Chabauty gates — remaining named: height
    bound, then Coleman on Z_D and on C3_A
- id: k34-leaf-jacobian
  kind: theorem
  status: proven
  uses: []
  source: [[k34-leaf-jacobian]]
  next: the four K34 leaf quartics share one Jacobian $E_a$;
    three leaves insoluble (nontrivial Sha[phi]) — the live leaf
    $C_{238}$ is parametrized by the rank-1 fiber
- id: k34-lift-gate-quartic
  kind: lemma
  status: proven
  uses: [k34-leaf-jacobian]
  source: [[k34-lift-gate-quartic]]
  next: the K34-A candidate lift reduces exactly to square-x points
    on the third quartic D (Jacobian $J_L$, rank 1 unconditional) —
    the lift gate is structurally K34-A one level up; lift tower open
- id: zd-chabauty-gate
  kind: method
  status: conditional
  uses: [k34-lift-gate-quartic, k34-leaf-jacobian]
  source: problems/magic-square-of-squares/progress.md
  next: rank Jac(Z_D) = 1 < 3 PROVEN unconditionally (rank
    E_+(Q(sqrt(-271))) = 0 by hand 2-isogeny descent, selmer2i) so
    Chabauty applies to Z_D — but the closure is conditional on the
    height bound (effective Chabauty) then the Coleman execution;
    the unconditional m $\le$ 240 mod-p sieve already kills all
    50 alive admissible indices
- id: c3a-coleman-gate
  kind: method
  status: open
  uses: [k34-leaf-jacobian]
  source: problems/magic-square-of-squares/progress.md
  next: the Coleman computation on C3_A at a good prime (rank 1 < 3,
    #C3_A(F_11)=8, bound $\le$ 12) is the named proof path for the
    C3_A branch — not yet carried out (Coleman not executed)