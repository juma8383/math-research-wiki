---
type: conjecture
name: Fermat–Catalan conjecture
status: open
raised-by: []
created: 2026-08-24
evidence: only 10 known primitive solutions, all with min exponent 2; computational verification to z^r <= 2^100 [rg2024-comp-bound]
---

# Fermat–Catalan conjecture

**Statement.** The equation $x^p+y^q=z^r$ has only **finitely many** solutions in
positive integers $(p,q,r,x,y,z)$ with $\gcd(x,y,z)=1$ and
$1/p+1/q+1/r<1$ (exponents allowed to vary).

This is the *exponents-vary* finiteness conjecture, weaker in scope than Beal:
here $\min\{p,q,r\}$ may be $2$.

## Relation to Beal [[beals_conjecture]]
Per [rg2024-fc-vs-beal]: Beal asserts **zero** coprime solutions when
$\min\{p,q,r\}\geq 3$; Fermat–Catalan asserts only **finiteness** across all
signatures with $1/p+1/q+1/r<1$ (including those with a $2$). Beal is strictly
stronger in the $\geq 3$ regime. They are **distinct** conjectures — do not
conflate (a common error).

## Known solutions [rg2024-10-solns]
Exactly 10 primitive solutions are known, and **all have a $2$** among the
exponents — none lies in Beal's $\min\geq 3$ regime. Notable ones:
$2^5+7^2=3^4$, $7^3+13^2=2^9$, $43^8+96222^3=30042907^2$.

## Evidence / status
Open. Verified computationally for $z^r\le 2^{100}$ [rg2024-comp-bound] — beyond
the 10 known, no others. The **abc conjecture** would imply Fermat–Catalan (and
stronger); Mochizuki's claimed abc proof remains contested (Scholze–Stix).

## Why it matters here
Filing it keeps the Beal/Fermat–Catalan distinction explicit and records the 10
"solution witnesses" — all sitting just outside Beal's regime (they use a $2$),
which is itself suggestive evidence for Beal.