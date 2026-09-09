---
type: dag
problem: riemann-hypothesis
last-updated: 2026-09-09
---

# Proof DAG — riemann-hypothesis

Live frontier: every zero on the line (verified to $T=3\cdot10^{12}$;
Guth-Maynard 2024 broke Ingham's zero-density record); the obstruction
is the control step (slice/average to every zero), with the
bandwidth-one certificate ceiling $p_0\le0.6818287$ as its quantitative
face.

- id: rh-itself
  kind: conjecture
  status: open
  uses: [zero-density-ladder, hilbert-polya-selfadjointness, weil-li-positivity, function-field-frobenius-positivity]
  source: [[riemann_hypothesis]]
  next: three exact control-reductions (attempt-01), none
    dischargeable with current tools; the two-avatars structure
    (function-field proven / number-field open) is the deepest link
- id: zero-density-ladder
  kind: theorem
  status: proven
  uses: []
  source: [[zero-density-ladder]]
  next: Ingham 1940 to Huxley 1972 ($12/5$) to Guth-Maynard 2024
    ($\frac{15(1-\sigma)}{3+5\sigma}$, Annals 203(2) 2026) — powers
    primes-in-intervals and the proportion ladder but stops at the
    certificate ceiling $p_0\le0.6818287$: density control
    quantitatively cannot certify all zeros
- id: hilbert-polya-selfadjointness
  kind: method
  status: open
  uses: []
  source: problems/riemann-hypothesis/attempts/attempt-01.md
  next: RH iff the zeros are the spectrum of a self-adjoint operator —
    control tool would be self-adjointness; no such operator known
    (Connes's adele-class spectral interpretation reduces to a trace
    formula but the operator is not self-adjoint on a space with
    spectrum exactly the zeros)
- id: weil-li-positivity
  kind: method
  status: open
  uses: []
  source: problems/riemann-hypothesis/attempts/attempt-01.md
  next: RH iff Weil's explicit-formula distribution $\ge0$ iff Li
    coefficients $\lambda_n\ge0$ for all $n$ (Bombieri-Lagarias;
    Suzuki 2023 screw-function form) — control = proving the
    positivity for all test functions, not done
- id: function-field-frobenius-positivity
  kind: method
  status: conditional
  uses: []
  source: problems/riemann-hypothesis/attempts/attempt-01.md
  next: PROVEN over function fields (Weil/Deligne, via etale
    cohomology + Rosati positivity) — and it STOPS at the number
    field: no Frobenius and no Rosati positivity in characteristic 0,
    so the control tool has no char-0 translation (the cleanest
    one-dimensional-engine-stops instance); conditional on a missing
    characteristic-0 translation, not on a stated conjecture