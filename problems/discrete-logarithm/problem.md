# Discrete Logarithm Problem (DLP)

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/DLP.htm.
> Computational-complexity problem; a full attack routes through [[PvsNP]].

## Statement
In a cyclic group $G=\langle g\rangle$, given $g$ and $h=g^x$, find $x$ (the
discrete logarithm). Is there a polynomial-time (in $\log|G|$) algorithm
(in the classical model)?

## Status
**OPEN.** Hard in the black-box/generic-group model (Shoup: $\Omega(\sqrt{|G|})$,
1997); sub-exponential index-calculus in some groups ($\mathbb F_p^\times$,
$(\mathbb Z/n)^\times$, elliptic curves with low embedding degree); no poly
classical algorithm known. Shor: quantum poly (1994).

## Frontier (one line)
Generic lower bound $\Omega(\sqrt q)$ (Shoup 1997); index-calculus
$L[1/3]$–$L[1/2]$ in vulnerable groups; elliptic-curve DLP has no
sub-exponential known classical algorithm (the basis of elliptic-curve
cryptography) `[to-verify]`.

## Control-step framing (one line)
A subface of [[PvsNP]]'s `[witness-needs-explicit-lb]` / one-way-function
hardness: a generic (black-box) lower bound exists (the slice), but lifting
to a concrete-group super-polynomial *lower bound* is the open non-
compositional construction — control, not resolution.

## See also
- [[PvsNP]] — parent complexity problem.
- [[rsa_factoring]], [[diffie_hellman]] — sibling algebraic one-way-function
  problems (DH ⟸ DLP).