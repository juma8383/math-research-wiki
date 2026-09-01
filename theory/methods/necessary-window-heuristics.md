# Method: Necessary-window heuristics

> Toolbox method distilled 2026-09-01 from two independent attacks
> (`[mss-partner-window]` on [[magic_square_of_squares]],
> `[brocard-rootofunity-heuristic]` on [[brocard_problem]]).
> Reusable whenever a Diophantine solution set is cut by a *structural
> necessity* into a much thinner slice than the naive count suggests.

## The pattern

Many open problems have the shape: *solutions are special configurations
inside a large, apparently random set* (a set of divisors, residues,
roots). The naive probabilistic model treats the ambient set as
uniformly random with the right marginal density and asks how often the
special configuration appears. The answer typically comes out
$O(1)$ — inconclusive: "the null is consistent with chance."

The upgrade: most such configurations carry an **algebraic necessity**
— a hidden parameter (a representation, a congruence class, a witness
structure) that *forces* the co-configured partner to lie in a narrow,
computable **window**, far narrower than the ambient range. Injecting
the window into the model sharpens the expectation by orders of
magnitude and converts "inconclusive" into a definite lean.

## Instance 1 — MSS additive triples (partner window)

Setup: $D(w^2)=\{2uv : u^2+v^2=w^2\}$; a 9-square solution needs an
additive parallelogram in some $D(w^2)$, a first necessary condition
being an additive triple $\{x,y,x+y\}$.

- **Naive model**: pairs $(x,y)\subseteq D(w^2)$, each $x+y\in D(w^2)$
  with probability $24|D|/w^2$ ⟹ expected hourglasses over the whole
  plane $\approx 1.01$ — inconclusive.
- **Window theorem**: if $\{x,y,x+y\}\subseteq D(w^2)$ with $x=2uv$,
  then both roles force
  $2(u+v)+1\le y\le (u-v)^2-1$ — because
  $y=(u-v)^2-s^2=t^2-(u+v)^2=p(p+2(u+v))=r(r+2(u-v))$ with $p,r\ge1$.
- **Corrected model**: $H_2=0.0775$ (13× sharpening, verified against
  the naive value reproduced exactly with the same conventions);
  parallelogram expectation $E_{A3}\approx4.4\cdot10^{-5}$ (refined
  $\approx3.4\cdot10^{-6}$ by window-correcting the second hit too)
  ⟹ $P(\text{no 9-square solution})\approx99.9997\%$ *under the model*.

## Instance 2 — Brocard roots of unity (structure window)

Setup: $n!+1=m^2$ forces $m^2\equiv1\pmod{n!}$: $m$ is one of exactly
$R(n)=2^{\pi(n)+1}$ square roots of unity mod $n!$, scattered in
$[0,n!)$.

- **Naive question** "do roots of unity hit the target $m\approx
  \sqrt{n!}$?" has no useful marginal — the target is a single point.
- **Window**: $m^2=n!+1$ confines $m$ to $(\sqrt{n!},\,2\sqrt{n!}]$,
  relative width $\sim1/\sqrt{n!}$.
- **Corrected model**: $E(n)=2^{\pi(n)+1}\sqrt{n!}/n!\to0$
  superexponentially ($\log_{10}E=-71$ at $n=100$); exact enumeration
  ($n\le12$) reproduces the known solutions as the only small-$n$ window
  hits. The heuristic is abc-independent and explains the Legendre
  sieve's observed per-prime halving.

## How to apply

1. Identify the **witness parameter** of a would-be solution (the rep
   $(u,v)$; the CRT class of $m$).
2. Derive the **two-sided window** the necessity forces on the partner
   object — usually by writing the partner as a product form that must
   factor positively (here: $p(p+2(u+v))$, $r(r+2(u-v))$; a square
   difference).
3. Re-run the **counting model with the window injected**; report both
   naive and corrected expectations. A 10×+ sharpening that moves the
   lean from "inconclusive" to "decisive under the model" is the
   signal.
4. **Verify the theorem empirically** at scale (spacing corollary:
   1.26M consecutive-pair tests, 0 violations; root counts by
   enumeration) — window claims are checkable, so check them.
5. State honestly what remains model, not theorem: equidistribution and
   independence assumptions are unproven; the window part is exact.

## Cross-links

- Both instances feed the control-step framing: the window is the
  *reduction-layer* obstruction; the final control step (abc for
  Brocard; a proven freeness theorem for MSS) remains open.
- Related: `theory/methods/two-avatars-control-step.md`.