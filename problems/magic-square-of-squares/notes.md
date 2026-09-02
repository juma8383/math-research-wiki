# Notes — Magic Square of Squares

> Session findings and structural lemmas. Read [problem.md](problem.md)
> first for status and censuses. Wikilinks: problem slugs use UNDERSCORE,
> theory slugs kebab.

## Structural lemmas (2026-08-31 loop block) `[mss-structural-lemmas-verified]`

Setup: square-center config = center $a=w^2$, entries
$a\pm b,\ a\pm c,\ a\pm(b+c),\ a\pm(b-c)$ (distinct). A pair $a\pm d$ is
*complete* (both entries square) ⟺ $d\in
D(w^2):=\{2uv: u^2+v^2=w^2,\ u>v>0\}$.

**Lemma 1 (D closed form).** For any $w\ge2$,
$$|D(w^2)|=\Bigl(\prod_{p\equiv 1(4)}(2\,v_p(w)+1)-1\Bigr)/2 .$$
*Proof sketch:* $|D|$ = # unordered positive reps of $w^2$ as a sum of two
squares (product/sum determine the pair); $r_2(w^2)=4\prod_{p\equiv1(4)}
(2v_p(w)+1)$ (3-mod-4 primes have even exponent in $w^2$); subtract the 4
zero-coordinate reps and divide by 8 (signs/order). Verified: 0 mismatches,
all $w\le6000$ (`check1`).

**Lemma 2 (primitivity ⟺ w odd).** If $w$ is even then every rep has
$u,v$ both even, so $D(w^2)=4D((w/2)^2)$ and entries $a\pm d=4\bigl((w/2)^2
\pm d'\bigr)$ — the config is the global scaling by $4=2^2$ of one with
center $(w/2)^2$. Hence *primitive configs (no $k^2$ scaling quotient)
have $w$ odd*. This is the structural reason the triple-engine census's
primitive quotient is exactly "divide out even $w$". Verified: 0
mismatches, even $w\le2000$ (`check2`); consistent with the W=10⁶ census
(all raw configs = Bremner scalings).

**Lemma 3 (center necessity — CORRECTED).** *Correction history:* an
earlier draft of this lemma claimed $\ge7$ squares force 3 complete pairs
($|D|\ge3$, $s\ge7$) — **wrong**, caught 2026-08-31 by hand-checking the
Bremner pair structure: its 7 squares split as **2 complete pairs**
($a\pm b$, $a\pm(b+c)$) **+ 2 accidental half-pairs** ($a+c=373^2$,
$a-(b-c)=23^2$) + center. 7 = 2·2+2+1, not 3·2+1. Corrected statement:
$$\ge7\ \text{squares}\ \Longrightarrow\ |D(w^2)|\ \ge\ 2\ \Longrightarrow\ \prod_{p\equiv1(4)}(2\,v_p(w)+1)\ \ge\ 5,$$
i.e. the center must be divisible either by $p^2$ for some $p\equiv1\bmod4$
(Bremner: $425=5^2\cdot17$, both properties) or by two distinct
1-mod-4 primes. The half-pair squares need no D-membership at all — the
"additive closure among D-elements" framing of the first draft was
overclaimed; with only 2 complete pairs there is *no* additive condition
on $D$, which is why $\ge7$-square configs are ~1000× more common than a
3-element closure condition would suggest (and why Bremner-type examples
exist at all).

**Lemma 4 (24-divisibility / entries mod 24).** For **every** $w\ge2$ and
every $d\in D(w^2)$: $24\mid d$. *Proof:* (mod 8) if $w$ odd, $u,v$ have
opposite parity; say $u$ even — then $v,w$ odd, so
$u^2=w^2-v^2\equiv0\pmod8$, forcing $4\mid u$, so $8\mid 2uv=d$; if $w$
even, $u,v$ both even and $8\mid d$ directly. (mod 3) if $3\nmid w$, then
$u^2+v^2\equiv w^2\equiv1\pmod3$ forces one of $u,v\equiv0\pmod3$ (the
only nonzero square mod 3 is 1), so $3\mid d$; if $3\mid w$ then $u,v$
both $\equiv0\pmod3$, again $3\mid d$. Hence $24\mid d$ — and **every
entry $a\pm(\cdots)$ of a square-center config satisfies entry $\equiv
w^2\pmod{24}$**; for primitive ($w$ odd, $3\nmid w$ by scaling quotient)
that is entry $\equiv1\pmod{24}$, so **all nine entries of a primitive
config are $\equiv1\pmod{24}$ and the magic sum $\equiv3\pmod{24}$.**
Verified: gcd over all $d$, $w\le5000$ = **exactly 24** (no further common
factor exists); all nine Bremner/Sallows entries ≡ 1 mod 24; magic sum
541875 ≡ 3 mod 24. **Independently corroborated 2026-09-01:** the
Zimmermann–Pierrat–Thiriet 2015 mod-2⁵⁹ work states squared entries of
primitive solutions must be 1 mod 24 and magic sum ≡ 3 mod 72 (consistent
with our ≡ 3 mod 24 for square-center configs) `[summary]` — our
contribution is the *proof* (two lines, via D-divisibility) and the
exactness of the 24. Search implication: candidate entries must lie in the
single residue class 1 mod 24 — an 8× filter on brute force, and a
necessary condition any nonexistence proof may exploit.

**Corollary (full solution needs |D|≥4 — survives the correction; label
fixed).** The FULL 9-square solution (ALL nine entries square = nsq**9**)
needs 4 complete pairs (all 8 non-center entries square) ⟹ $|D(w^2)|\ge4$
⟹ $\prod_{p\equiv1(4)}(2v_p(w)+1)\ge 9$ — necessary, not sufficient
(Bremner: $|D|=7\ge4$, yet nsq=7). (An earlier draft mislabeled this
"nsq=8"; nsq=8 alone may have 3 complete pairs + 2 accidental halves and
needs only $|D|\ge3$.) This is the strongest clean filter on candidate
centers for the full problem.

**Status:** these are provable-by-inspection lemmas (proofs sketched
above; numerics re-checked this session, scripts inline in log). They
sharpen the census claim's *why*: the uniqueness box could have been
predicted to extend cleanly because D-sets are divisor-structured, not
random.

## The additive-parallelogram reduction (2026-09-01 loop block)
`[mss-parallelogram-reduction]`

**Theorem (exact reduction, provable).** A 3×3 magic square of 9 distinct
squares exists **iff** for some $w$ the set $D(w^2)$ contains an *additive
parallelogram*: distinct $x<y\in D(w^2)$ with $x+y\in D(w^2)$ and $y-x\in
D(w^2)$ (four distinct elements). *Proof.* (⟸) take $b=y,\ c=x$ with the proviso $y\ne2x$: all four
role quantities $|b|,|c|,|b+c|,|b-c|$ lie in $D$, so all 8 non-center
entries of `entries(w²,b,c)` are squares; the roles are then distinct
(the only possible collision is $b-c=c$, i.e. $y=2x$, which would
duplicate the $a\pm c$ pair and repeat entries); positivity holds since
$d<w^2$ for every $d\in D$. (⟹)
Any full solution has square center $a=w^2$; its four opposite pairs need
$b,c,b+c,b-c\in D(w^2)$, and the nine entries distinct force the four
roles distinct ($b-c=c$ would duplicate the $a\pm c$ pair). ∎ The
**hourglass** (top row + center + bottom row) is exactly the weaker
condition $\{b,\ c,\ b+c\}\subseteq D(w^2)$ — an *additive triple* in
$D$ — so Buell's 1999 theorem ("no hourglass with center $<2.5\cdot10^{24}$")
is exactly: **no additive triple in any $D(w^2)$ with $w\le5\cdot10^{12}$.**

**Census (`scripts/mss_d_additive_patterns.py`, reusing the validated
chunked builder).** For all $w\le10^6$ (centers $\le10^{12}$): 257,824 w
have $|D|\ge3$; **zero additive triples (A2) and zero parallelograms
(A3)**; 0 violations of Lemma 4. Independent re-verification of Buell's
null at small $w$ by a different engine (his bound covers $w\le5\cdot
10^{12}$, so the census is subsumed — filed as re-verification, not new
territory).

**Euler-product heuristic (`scripts/mss_hourglass_heuristic.py`).** The
naive random model for the total number of hourglass triples over ALL
centers (unbounded) collapses to exact Euler products: with $P(w) =
\prod_{p\equiv1(4)}(2v_p(w)+1)$,
$$H=\tfrac32\bigl(S_3-5S_2+7S_1-3S_0\bigr),\qquad
S_k=\zeta(2)\prod_{p\equiv1(4)}(1-p^{-2})\,T_p(k),$$
$T_p(k)=\sum_{e\ge0}(2e+1)^k p^{-2e}$ (closed forms for $k=1,2,3$).
Evaluated (mpmath, 40 dps): $S_1=1.8319312$, $S_2=2.4731144$,
$S_3=5.1530044$ ⟹ **H ≈ 1.014** (density $|D|$); strict density $|D|-2$
(the sum must be a third element) ⟹ $H\approx 0.533$. Both are upper
bounds: pairs with $x+y>w^2$ are invalid and only overcounted. **Reading:
the model predicts at most about ONE hourglass triple in the entire
infinite plane of centers** — Buell's exhaustive null to $2.5\times10^{24}$
is the expected behavior, and a solution, if it exists, is a ~1σ global
fluctuation.

**Calibration against the censused range (`mss_heuristic_partial.py`).**
The model places **1.0086 of the total 1.0142 expected mass at w ≤ 10⁶**
(≈99.5% — the series is dominated by small w with large |D|), yet the
census observed **0** triples there. Poisson: P(0 | mean 1.01) ≈ 36% —
so Buell's null is *consistent* with the naive model (a ~1σ fluctuation),
and the honest reading is: the model is an upper bound whose true value
is likely smaller (the arithmetic condition on x+y is unmodeled). |D|
histogram over w ≤ 10⁶: the weight is dominated by |D|=4 (195,396 w),
|D|=13 (28,394 w), |D|=7 (21,160 w); max |D| = 94.

**Window-corrected heuristic (2026-09-01, later block;
`mss_window_spacing.py`).** The partner-window theorem is *provable*, so
it upgrades the heuristic from model to partial theorem: only pairs with
$y$ in the window of $x$'s rep AND $x$ in the window of $y$'s rep can
possibly satisfy $x+y\in D$. Computing the admissible pairs exactly for
all $w\le10^6$ (reps extracted by isqrt from $w^2\pm d$, all $1{,}980{,}642$
elements verified; $|D|$ counts matched the validated chunked engine with
0 mismatches):
$$H_2=\sum_{w\le10^6}\#\{\text{admissible pairs}\}\cdot\tfrac{24|D|}{w^2}
\approx 0.0775\quad(\text{strict }|D|-2:\ 0.0556),$$
against the naive all-pairs partial $1.0086$ reproduced exactly by the
same run (density $24|D|$: the $24\mid d$ lattice correction). **The
provable window alone cuts the model's expected hourglass count by
$13\times$** — and the tail beyond $10^6$ is bounded by the naive tail
$0.0056$, so the corrected total is $\lesssim 0.083$.
*Reading:* Poisson $P(0\mid 0.08)\approx92\%$ ($94\%$ strict) — the
"at most about one hourglass in the entire plane" reading sharpens to
**expected $\lesssim0.08$: the null is not a $1\sigma$ fluctuation but
the strongly expected outcome** (observing even one hourglass would be a
$\sim8\%$-probability event under the corrected model, vs $\sim64\%$
under the naive one). Mechanism: the naive
model counts close pairs of D-elements freely, but the window (equival-
ently the spacing corollary: gaps $\ge 2\sqrt{w^2+x}+1$, empirically
$\ge 2\times$ that, 1,259,270 consecutive-pair tests, 0 violations) makes
an admissible sum-partner rare. Same caveats as the naive heuristic
(density model for $P(x+y\in D)$; no calibration example), but the
window factor itself is now theorem, not model.

**Parallelogram expected count (2026-09-01, later block;
`mss_parallelogram_heuristic.py`) — the main problem quantified.** The
iff reduction says the FULL problem is: does any $D(w^2)$ contain an
additive parallelogram $\{x,y,x+y,y-x\}$? Both the sum triple
$\{x,y,x+y\}$ and the difference triple $\{y-x,x,y\}$ are additive
triples, so the provable windows apply, plus Corollary A on the pair
$(x,y-x)$ when $y>2x$. Model (both hits independent at density
$24|D|/w^2$; difference-side window for $y<2x$ unmodelable before
$y-x\in D$ — no filter there, so the estimate stays an upper bound):
$$E_{A3}=\sum_{w\le10^6}\sum_{\text{admissible pairs}}
\Bigl(\tfrac{24|D|}{w^2}\Bigr)^{2}\ \approx\ 4.4\cdot10^{-5}$$
(naive all-pairs: $1.1\cdot10^{-2}$ — the windows cut it $257\times$;
the $\sum w^{-4}$-type tail beyond $10^6$ is negligible). *Reading
(honest):* under the corrected model **a 9-square solution is expected
not to exist with probability $\approx 99.996\%$** — the first
quantitative heuristic aimed at the full problem rather than the
hourglass subsystem. It is still a heuristic: the density model for the
two independent hits is uncalibrated (no known parallelogram exists to
calibrate against — that is the problem), and nonexistence is not
proved. But the necessary-condition part is theorem, and the census
(0 parallelograms, $w\le10^6$) plus Buell (none, $w\le5\cdot10^{12}$)
are exactly what this model predicts. *Refinement (same block):* the
second hit $y-x\in D$ is itself an additive triple, so its probability
should carry the same window correction as the first — multiplying by
the measured factor $0.0775/1.0086\approx0.077$ gives
$E_{A3}\approx3.4\cdot10^{-6}$, strengthening the reading to
$P(\text{no solution})\approx99.9997\%$ (same caveats).

**Honest caveats.** Heuristic, not proof: (i) the density model ignores
clustering of D-elements and the arithmetic condition $x+y=2u''v''$; (ii)
sensitivity to the conditioning ($|D|$ vs $|D|-2$ swings $H$ by ~2×) shows
the model is order-of-magnitude only; (iii) no calibration against a known
nontrivial example (Bremner's 7-square satisfies a different, weaker
condition set); (iv) the parallelogram census to $w\le10^6$ is subsumed by
Buell. What IS new and rigorous: the exact iff reduction, which turns "the
full problem" into the clean additive-combinatorics question *does any
$D(w^2)$ contain an additive parallelogram?* — and the observation that
$D$-sets appear to be additive-triple-free in every searched range.

**3-term-AP census (2026-09-01, later block; `mss_d_ap_census.py`).**
The natural sibling pattern: does $D(w^2)$ contain a 3-term arithmetic
progression $\{x,m,z\}$ ($x+z=2m$)? For the cubic sibling this is
trivially impossible (`[[square_of_cubes]]` `[cubic-dset-vanishes]` —
Legendre's no-three-cubes-in-AP theorem IS the empty cubic D-set). For
the square D-sets, censused over all $w\le10^6$ (257,824 w with
$|D|\ge3$): **zero 3-term APs** — matching the A2 triple count exactly
in population and adding a second, independent additive-freeness
property. Expected count under the Euler-product model is again
$O(1)$ over the whole plane, so the null is the expected behavior; note
AP-freeness is a *different* condition from the hourglass triple
($x+z=2y$ vs $x+y=z$) and neither implies the other.

**Targeted beyond-Buell search (2026-09-01, later block;
`mss_hourglass_targeted.py`).** Buell exhausts $w\le5\cdot10^{12}$; this
run goes past that frontier at *targeted* centers: 2500 centers with the
largest $|D|$ (all $=3280$, i.e. products of 8 distinct primes
$\equiv1\bmod4$, a few of $|D|=337$-tier), $w\in(5\cdot10^{12},\,
2.5\cdot10^{15})$ — centers up to $6.4\cdot10^{30}$, ~7 orders of
magnitude beyond Buell's $2.5\cdot10^{24}$. The engine computes
$D(w^2)$ EXACTLY by Gaussian-integer exponent-split enumeration
($d=|\operatorname{Im}z^2|$, $z\bar z=w^2$) — no bound on $u,v$ needed,
so $w$ can be astronomically large; validated three ways (exact
Lemma-1 counts at every $w$, isqrt membership test
$w^2\pm d$ both squares for every element, Lemma 4; spot-check
$w=1.4\cdot10^{15}$, $|D|=29524$ in 0.07 s). **Result: zero additive
triples (A2), zero parallelograms (A3), zero Lemma-1/Lemma-4 violations
across all 2500 centers** (log `hourglass_targeted.log`). Honest scope:
targeted, not exhaustive — under the Euler-product model the expected
yield in this regime is $\sim10^{-3}$, so a null is the expected
outcome; the value is that the model's max-$|D|$ regime (where its tail
mass concentrates) is now exactly verified far past the exhaustive
frontier, on the largest-$|D|$ D-sets ever additively censused
($|D|=3280$ vs Buell's engine range).

**Difference census (2026-09-01, later block; `mss_d_diff_census.py`)
— with a logical correction.** The A2 census tested sums; the AP census
tested midpoints; neither tested **differences**: are there pairs
$x<y$ in $D(w^2)$ with $y-x\in D(w^2)$? Over all $w\le10^6$
(6,162,178 pairs): **zero** — but this is *not new information*: a
difference pair $(x,y)$ with $y-x=d''\in D$ IS a sum triple
$\{d'',x,y\}$ ($d''+x=y$), so **sum-freeness ⟺ difference-freeness
exactly**, and an AP $\{x,m,z\}$ decomposes as the sum triple
$\{x,\,z-m,\,m\}$ — so **sum-freeness (A2) implies AP-freeness too**.
[*Correction 2026-09-01, caught immediately on re-derivation:* the
first draft of this paragraph claimed difference-freeness is "the
strongest" property implying the other two — backwards; sum-freeness
is the strongest, difference-freeness is *equivalent* to it, and the
difference census is a re-derivation of A2=0, not an independent
fact.] The value of the run is the explicit check of the equivalence
and the confirmation that the window machinery covers both signs (the
difference triple $\{y-x,x,y\}$ is an additive triple, same window,
same $\sim0.08$ corrected expectation).

**Sharp partner-window theorem (2026-09-01, later block — supersedes the
one-sided bound below).** Let $\{x,y,x+y\}\subseteq D(w^2)$ with $x=2uv$,
$u>v>0$ the (unique) rep of $x$. Then $w^2\pm x=(u\mp v)^2$, and since
$x+y\in D$ both $w^2\pm(x+y)$ are squares: write $s^2=w^2-(x+y)$,
$t^2=w^2+(x+y)$ with $1\le s<u-v$ and $t>u+v$ (as $x+y<w^2$, so $s\ge1$;
and $t>u+v$ since $y>0$). Then
$$y=(u-v)^2-s^2=t^2-(u+v)^2=p\,(p+2(u+v))=r\,(r+2(u-v)),$$
$p=t-u-v\ge1$, $r=u-v-s\ge1$, giving the **two-sided window**
$$2(u+v)+1\ \le\ y\ \le\ (u-v)^2-1 .$$
The same holds with the roles swapped ($x$ in the window of $y$'s rep).
*Consequences:* (i) the window is nonempty only if $(u-v)^2>2(u+v)+1$,
i.e. (solving the quadratic in $u$) $u\ge v+1+\sqrt{4v+1}$ — **any
element of an additive triple has $u-v\gtrsim 2\sqrt{v}$: the two legs of
its rep must differ by more than roughly twice the square root of the
smaller leg.** [*Correction 2026-09-01, caught on re-derivation:* an
earlier draft here claimed this forces $u/v>3+2\sqrt2\approx5.83$ — that
is the threshold for $(u-v)^2>2uv$, not $2(u+v)$; the true condition is
much weaker and scales as $u-v>2\sqrt v$, e.g. $(u,v)=(5,1)$ and
$(12,5)$ both have nonempty windows while $u/v\ll5.83$. The exact
window-corrected heuristic below is unaffected — it uses the windows
themselves, not this asymptotic.]
(ii) $x+y<w^2$ automatically (the window's upper end is $w^2-x-1$), so
the "sum exceeds $w^2$" overcount in the heuristic disappears inside the
window; (iii) the window is a huge pruning filter for any future
exhaustive search: from $x$'s rep alone, the partner $y$ is confined to
an interval of length $(u-v)^2-2(u+v)-1$. (The earlier one-sided bound
$y\le(u^2-v^2)^2/(4uv)$ in the slope-form paragraph below was a weaker
algebraic consequence; the window here is sharper and two-sided, derived
directly from the two entries adjacent to the triple.)

**Slope-form reformulation (2026-09-01, same block).** Writing $t_i =
v_i/u_i\in\mathbb{Q}\cap(0,1)$ for the slopes of the reps, $d = w^2\cdot
2t/(1+t^2)$, so the additive-triple condition becomes the **rational
surface**
$$\frac{t_1}{1+t_1^2}+\frac{t_2}{1+t_2^2}=\frac{t_3}{1+t_3^2},\qquad
x=k_1^2\!\cdot\!\tfrac{2u_1v_1}{1},\ \dots$$
more precisely: rational solutions $(t_1,t_2,t_3)$ exist in abundance as a
surface, but the common-hypotenuse constraint $u_i^2+v_i^2=w^2$ (all three
$w$ equal) reduces the integer problem to a **ternary condition**
$k_1^2u_1v_1+k_2^2u_2v_2=k_3^2u_3v_3$ on primitive triples — the shape of
a congruent-form/elliptic-curve problem, consistent with Robertson's 1996
rank-4 elliptic-curve reduction of the full problem `[to-verify vs
primary]`. Factor-form corollary (proved same block): $x+y\in D(w^2)$ with
$x=2uv$ requires $\exists a,b>0:\ 2ab=xy,\ a+b=u^2-v^2$, hence the sharp
partner bound $y\le(u^2-v^2)^2/(4uv)$ — any counterexample has its second
element $y$ bounded by the first rep's co-leg, a strong asymmetry future
searches can exploit.

**Corollary A (D-set spacing — testable form of the window).** The lower
bound of the window uses only $x\in D$, $x+y\in D$, $y>0$ — not $y\in D$.
So for **any** two elements $x<d'$ of $D(w^2)$ (take $y=d'-x$), with
$(u,v)$ the rep of $x$:
$$d'-x\ \ge\ 2(u+v)+1\ =\ 2\sqrt{w^2+x}+1,\qquad\text{i.e.}\quad
d'\ \ge\ (\sqrt{w^2+x}+1)^2=(u+v+1)^2 .$$
$D(w^2)$ is *forcibly separated*: no two of its elements are closer than
$2\sqrt{w^2+x}+1$ apart (the worst case is the smallest gap, so testing
consecutive pairs suffices). Note the upper window end degenerates to the
trivial $d'<w^2$ for general pairs; its content is only in the triple
case. This is the mechanism behind additive freeness: a sum $x+y$ of two
D-elements that stays in $D$ must clear $x$ by more than $2\sqrt{w^2+x}$
— the sum cannot be an "adjacent" element. Numerics: consecutive-pair
test over all $w\le10^6$ — see `window_spacing_W1e6.log` and the
heuristic paragraph below.

## The prime-power freeness theorem (2026-09-01, first proved family) `[mss-primepower-freeness]`

**Theorem.** Let $p\equiv1\pmod4$ be prime, $e\ge0$, $k\ge1$,
$w=2^e p^k$. Then $D(w^2)$ contains **no additive triple**
$\{x,y,x+y\}$, no 3-term AP, and no additive parallelogram.
**Corollary: no 9-square magic square of squares has square center
$w^2=p^{2k}$ (with any $2^e$ factor).** Bremner's center $425=5^2\cdot17$
has two distinct 1-mod-4 primes — not covered, consistent with its
existence.

*Proof.* Write $p=a^2+b^2$ ($a>b>0$), $\pi=a+bi\in\mathbb Z[i]$, and
$\gamma=\bar\pi^2=c-di$ with $c=a^2-b^2$, $d=2ab$ (so $c^2+d^2=p^2$).

*Step 1 (structure).* Every rep $u^2+v^2=p^{2k}$ has $u+iv=\mathrm{unit}
\cdot\pi^j\bar\pi^{2k-j}$, $j=0..2k$ (UFD in $\mathbb Z[i]$); pairing
$j$ with $2k-j$ (conjugation) leaves $k$ nontrivial unordered pairs
plus the trivial $j=k$ — matching Lemma 1's $|D(p^{k\,2})|=k$. (The
injectivity of $m\mapsto d_m$ is established a posteriori by Steps 2–3:
$v_p(d_m)=2(k-m)$ pairwise distinct, so the $k$ listed values exhaust
$D$ by Lemma 1's independent count.) For
$j\le k$: $\pi^j\bar\pi^{2k-j}=p^j(\bar\pi^2)^{k-j}=p^j\gamma^{k-j}$,
and $2\,\mathrm{Re}(z)\,\mathrm{Im}(z)=\mathrm{Im}(z^2)$, so with
$m=k-j$:
$$d_m \;=\; p^{2(k-m)}\,\bigl|\operatorname{Im}(\bar\pi^{4m})\bigr|,
\qquad m=1,\dots,k,$$
and these are all the elements.

*Step 2 (key lemma: $p\nmid Y_m$ where $Y_m=|\operatorname{Im}(\bar\pi^{4m})|$).*
Suppose $p\mid Y_m$. Then $\bar\pi^{4m}=X+pYi$ for integers $X,Y$, i.e.
$\bar\pi^{4m}\equiv X\pmod{p\,\mathbb Z[i]}$; conjugating gives
$\pi^{4m}\equiv X$. Multiplying: $p^{4m}-X^2\in p\,\mathbb Z[i]$, and
$p^{4m}\in p\,\mathbb Z[i]$, so $X^2\in p\,\mathbb Z[i]=(\pi)(\bar\pi)$.
$\mathbb Z[i]$ is a UFD and $\pi,\bar\pi$ are non-associate primes, so
$\pi\mid X$ and $\bar\pi\mid X$, hence $p\mid X$. Then
$\bar\pi^{4m}\equiv0\pmod{p\,\mathbb Z[i]}$ would force
$\pi\mid\bar\pi^{4m}$, i.e. $\pi\mid\bar\pi$ — false (they are coprime
prime factors of $p$). $\blacksquare$ (lemma)

*Step 3 (distinct valuations).* $v_p(d_m)=2(k-m)$ — pairwise distinct
across $m=1..k$.

*Step 4 (freeness).* Take distinct $d_{m_1},d_{m_2},d_{m_3}$.
**Additive triple** $x+y=z$: since $v_p(x)\ne v_p(y)$, the ultrametric
gives $v_p(x+y)=\min(v_p(x),v_p(y))=2(k-\max(m_1,m_2))$, so
$m_3=\max(m_1,m_2)$, say $m_3=m_2>m_1$; then $z=d_{m_2}=y$ and
$x+y=y\Rightarrow x=0$ — contradiction. **AP** $x+z=2y$: same
computation forces $m_2=\max(m_1,m_3)$, i.e. $y$ is the largest-index
element and equals one of $x,z$ — contradiction with distinctness.
**Parallelogram** $\{x,y,x+y,y-x\}$: contains the additive triple
$\{x,\,y-x,\,y\}$ — excluded by the first part. ∎ (theorem)

*The 2-part (verified, then proved).* $v_2(u^2+v^2)$ odd unless $u,v$
both even (odd²+odd²≡2 mod 4); descent gives $2^e\mid u,v$ for every
rep of $2^{2e}p^{2k}$, so $D((2^ep^k)^2)=2^{2e}\,D((p^k)^2)$ exactly —
freeness transfers under scaling. Verified: exact builder match at
$(e,p,k)=(1,5,1),(2,5,1),(1,5,2),(3,5,2),(1,13,2),(2,17,2),(1,5,3)$,
all True (`_tmp_gen_check.py` output in session log).

*Evidence (step 9).* Full census `mss_primepower_freeness.py`
(`primepower_freeness.log`): all $p\equiv1(4)$, $p<2000$,
$p^k\le10^9$ (413 families; largest $w=5^{12}$, elements to
$5.96\cdot10^{16}$): A2=0, A3=0, AP=0, and Lemma 1's $|D|=k$ asserted
at every point; the valuation lemma verified separately (0 violations).

*Failed first attempt (tracked, step 6).* The natural mod-$p$ argument
"work in $\mathbb Z[i]/(p)$ and show $\operatorname{Im}(\bar\pi^{4m})
\equiv0$ forces $\bar\pi\equiv\pm i$" is **wrong**: $\mathbb Z[i]/(p)
\cong\mathbb F_p\times\mathbb F_p$ is not a domain — $u^2\equiv-1$ has
two roots and $u\mp i$ need not vanish (e.g. $p=5$: $2^2\equiv-1$ but
$2\not\equiv\pm i$ in $\mathbb Z[i]/(5)$). The correct argument
multiplies the congruence by its conjugate and uses UFD unique
factorization, as above.

*What stays open (honest scope).* This proves freeness only where $w$
has **one** distinct 1-mod-4 prime factor ($\omega_1(w)\le1$). General
$w$ — in particular the max-$|D|$ centers where the window-corrected
heuristic concentrates all its mass — remains open; the control step is
unchanged. But the family is unbounded (centers $p^{2k}\to\infty$), so
this is structure no finite census can reach: for every such center the
9-square necessary condition fails identically. The natural next
question is the two-prime case $\omega_1=2$ (Bremner's $\omega_1=2$
center is the unique known config there — is $|D|=2$ with both primes
squared the *only* possible shape?), and whether Step 2's UFD trick
extends to $p^k q^\ell$.

## The two-prime case (2026-09-01, structure + census, open) `[mss-two-prime]`

The natural next target after the prime-power theorem: $w=pq$ ($p,q$
distinct $1\bmod4$ primes), $|D((pq)^2)|=4$ — Bremner's home turf
($425=5^2\cdot17$, so his center is $\omega_1=2$ with $k=2,\ell=1$,
$|D|=7$).

**Closed form (derived + verified).** With $\pi=a+bi$ ($a^2+b^2=p$),
$\rho=c+di$ ($c^2+d^2=q$), $Y_p=|\operatorname{Im}(\pi^4)|=
4ab|a^2-b^2|$ (prime-power lemma: $p\nmid Y_p$), $X=|\operatorname{Re}
(\pi^4)|\,Y_q$, $Y=Y_p|\operatorname{Re}(\rho^4)|$ (note
$\operatorname{Re}(\pi^4)=a^4-6a^2b^2+b^4\equiv8a^4\not\equiv0\pmod p$,
and similarly for $\rho$):
$$D((pq)^2)\;=\;\bigl\{\;p^2Y_q,\;\; q^2Y_p,\;\; |X-Y|,\;\; X+Y\;\bigr\}.$$
*Derivation:* the reps of $p^2q^2$ are $\pi^j\bar\pi^{2-j}\rho^a
\rho\bar^{2-a}$ ($j,a\in\{0,1,2\}$, 9 of them); $\zeta=z^2$ has
imaginary part $\operatorname{Im}(U V)$ with $U\in\{\bar\pi^4,p^2,\pi^4\}$,
$V\in\{\bar\rho^4,q^2,\rho^4\}$; the trivial $\operatorname{Im}(p^2q^2)=0$
and conjugate pairing collapse $9\to4$. Verified: exact equality with the
general builder for 5 pairs (self-test in
`mss_two_prime_structure.py`).

**Valuation obstruction (why the prime-power proof dies here).** The
$p$-valuation profile of the four elements is $\{0,0,0,2+v_p(Y_q)\}$ —
three elements share $v_p=0$ (namely $q^2Y_p$ — by the prime-power
lemma — and $|X-Y|,X+Y$: both $\equiv\pm X\pm Y\not\equiv0\pmod p$
generically). Pigeonhole: only $2k+1=3$ distinct $p$-valuations exist
for $k=1$, so distinctness fails structurally — the ultrametric
mechanism does not extend. The same profile shows the interesting
elements $|X-Y|,X+Y$ are generically **coprime to $w$**.

**Census.** All $p<q\le3000$ (211 primes, 22,155 pairs): **A2=0, A3=0,
AP=0** (`two_prime_structure.log`). Note this is inside Buell's bound
($w=pq\le9\cdot10^6\ll5\cdot10^{12}$), so it re-verifies rather than
extends — its value is the closed form as a handle for a proof.

**Partial mod-$p$ constraints (toward a proof, stalled).** Mod $p$:
$d_1=p^2Y_q\equiv0$, $d_2=q^2Y_p\not\equiv0$, $d_3,d_4\equiv\pm X\pm Y$
with $X\equiv8a^4Y_q$, $Y\equiv Y_p\operatorname{Re}(\rho^4)$ — both
generically nonzero, so each sum equation mod $p$ becomes a genuine
diophantine constraint (e.g. $d_2+d_3=d_4$ forces $q^2Y_p\equiv2Y
\pmod p$) — no generic contradiction found; the constraint involves
$Y_q\bmod p$ and $\operatorname{Re}(\rho^4)\bmod p$, which vary freely
over the primes. **Stall recorded** (protocol step 6): the two-prime
freeness question is open even for $|D|=4$, and a proof for all
$\omega_1=2$ would be a serious step toward the full problem (it would
cover Bremner's own center, where $D(425^2)$ is nonetheless sum-free —
census-verified, $w\le10^7$).

**Strengthening (same day, via pattern extraction).** The 2-part was
never special: for any prime $r\equiv3\pmod4$, $r\mid u^2+v^2$ forces
$r\mid u,v$ ($-1$ is a non-residue mod $r$), so iterating gives
$D((s\,m)^2)=s^2\,D(m^2)$ for **any** $s$ all of whose prime factors are
$2$ or $\equiv3\pmod4$ (verified: exact builder match at
$(s,p,k)=(3,5,1),(9,5,1),(3,5,2),(7,13,1),(21,5,2),(6,5,2),(3,13,2),
(2,5,3),(33,5,1)$ — and the scaling FAILS for every $s$ containing a
$1\bmod4$ prime: the genuine (coprime) falsification boundary is
$(s,p)=(5,13),(13,5),(65,17)$ — 4, 4, 13 elements where the scaled
image has 1 *(skeptic-verified; note the initially-filed example
$s=35,p=5$ is non-coprime, $\gcd=5$, and so diagnoses two causes at
once — replaced here by the clean cases)*). **Final form of the theorem: for every $w$ with
at most one distinct prime factor $\equiv1\pmod4$ ($\omega_1(w)\le1$,
arbitrary $2$- and $3\bmod4$ parts), $D(w^2)$ is sum-free, AP-free, and
parallelogram-free. Corollary: the center $w$ of any 9-square magic
square of squares satisfies $\omega_1(w)\ge2$ — unconditional and
unbounded.**

## Stratifying the hourglass heuristic by $\omega_1$ (2026-09-01)
`[mss-omega1-stratification]`

**Question.** The freeness theorem forces $\omega_1(w)\ge2$ for any
9-square center. Under the window-corrected probabilistic model, how
much stronger is the necessary condition — i.e., where does the model's
expected hourglass mass actually live as a function of $\omega_1(w)$?

**Method** (`mss_omega1_stratification.py`). For every $w\le W$ with
$|D(w^2)|\ge2$: build $D(w^2)$ exactly (corrected builder), extract each
element's rep $((u{+}v)=\sqrt{w^2+x},\ (u{-}v)=\sqrt{w^2-x})$, count
unordered pairs passing the partner-window theorem in **both roles**
($y\in[2(u{+}v){+}1,(u{-}v)^2-1]$ from $x$'s rep AND $x$ in the same
window from $y$'s rep), weight by $24|D|/w^2$, bucket by
$\omega_1(w)=\#\{p\equiv1(4):p\mid w\}$ (sympy factorint).

**Validation trap (self-caught, worth recording).** The window's upper
end is $(u-v)^2-1 = w^2-x-1$ — the script initially wrote
$(rp-rm)^2-1=(2v)^2-1$, a *smaller-or-larger* window depending on
$u\lessgtr 3v$; with the bug the total came out $0.09997$ (and a
one-sided variant gave $1.05$, *above* naive — impossible for a
restriction). Corrected to $rm^2-1$: **total $=0.07753$, reproducing the
filed window-corrected $H_2=0.077531$ exactly** — the stratification
sits on the validated engine.

**Results at $W=10^6$** (276,569 centers with $|D|\ge2$; the partial
sums at $W=10^6$ already carry essentially the full plane mass —
density $\sim24|D|/w^2$ decays fast):

**$W=10^7$ confirmation** (3,116,858 centers): window total $0.07856$,
strata $\{0.00004, 0.04714, 0.02884, 0.00249, 0.00005\}$ at
$\omega_1=\{1..5\}$ — shares $\{0.05\%, 60.00\%, 36.71\%, 3.17\%,
0.06\%\}$: the $\omega_1\in\{2,3\}$ concentration ($96.7\%$) and the
$3700\times$-suppressed $\omega_1=1$ stratum are box-stable.

| $\omega_1$ | centers | $H_2$ naive | $H_2$ window | share of window mass |
|---|---|---|---|---|
| 1 | 22,927 | 0.14743 | 0.00004 | 0.05% |
| 2 | 220,288 | 0.71272 | 0.04710 | 60.74% |
| 3 | 32,372 | 0.14030 | 0.02843 | 36.68% |
| 4 | 982 | 0.00812 | 0.00196 | 2.53% |
| **total** | 276,569 | **1.00858** | **0.07753** | 100% |

**Theorem-conditioned total** (proved-free $\omega_1\le1$ stratum
removed): naive $0.86114$, window $0.07749$ — the theorem removes only
$4\cdot10^{-5}$ of the model's window-corrected mass.

**Reading (honest).**
1. *The window model already "predicts" the freeness theorem's
   corollary:* the partner-window theorem alone suppresses the
   $\omega_1=1$ stratum from naive $0.147$ to $4\cdot10^{-5}$ — a
   $3{,}700\times$ cut — so conditioning the model on the proved theorem
   changes almost nothing. Theorem and heuristic are mutually consistent,
   and the corollary $\omega_1\ge2$ is *independently visible* in the
   window arithmetic (a nice coherence check between a proof and a
   model — the method-page pattern `[[necessary-window-heuristics]]`
   again).
2. *The model does NOT push the necessary condition past
   $\omega_1\ge2$:* within the surviving $\omega_1\ge2$ mass, 60.7%
   sits at $\omega_1=2$ and 36.7% at $\omega_1=3$ — i.e. **97.5% of the
   model's expected hourglass mass lives at $\omega_1\in\{2,3\}$**, and
   the conditional-per-center intensity *rises* with $\omega_1$
   ($2.1\cdot10^{-7}$ at $\omega_1=2$, $8.8\cdot10^{-7}$ at $3$,
   $2.0\cdot10^{-6}$ at $4$ per center) while the center counts decay
   faster ($220{,}288 \to 982$). Higher $\omega_1$ centers are
   individually hotter but collectively negligible.
3. *Consistency with the one known object:* Bremner/Sallows' center
   $425=5^2\cdot17$ has $\omega_1=2$ — exactly where the model says a
   hypothetical 9-square center (if any exists) should sit.
4. So the sharpened statement is **not** "$\omega_1$ must be large" but:
   *under the model, a 9-square center has $\omega_1=2$ or $3$ with
   $\approx97.5\%$ probability* — a prediction about WHERE to search,
   complementing the proved unconditional $\omega_1\ge2$. The proved
   part stops at $\omega_1\ge2$; extending the proof to $\omega_1\ge3$
   would remove 60.7% of the model's remaining mass and is precisely
   the open two-prime question `[mss-two-prime]` inverted: proving the
   $\omega_1=2$ stratum free would prune the model's single largest
   stratum — the census ($22{,}155$ two-prime centers,
   $A2=A3=AP=0$, plus all $w\le10^7$) says the truth is "free so far",
   so the model's 60.7% at $\omega_1=2$ is likely overestimated mass —
   the same shape the naive model showed before window correction (and
   the same pruning an $\omega_1=2$ freeness theorem would perform:
   it would cut the model's remaining expected total from $0.077$ to
   $\approx0.030$, $P(0)\approx97\%$).

## Two-prime sum-freeness: slice theorems + complete kill-equation case tree (2026-09-01, `[mss-two-prime-freeness]`)

Attack on the omega_1 = 2 stratum (`[mss-two-prime]` inverted). On the
verified closed form $D((pq)^2)=\{A,B,C,D_0\}$, $A=p^2Y_q$, $B=q^2Y_p$,
$X=R_pY_q$, $Y=Y_pR_q$, $C=|X-Y|$, $D_0=X+Y$ (pi=a+bi, rho=c+di;
$Y_p=|4ab(a^2-b^2)|$, $R_p=|a^4-6a^2b^2+b^4|$), script
`scripts/mss_two_prime_freeness_closedform.py` (self-test: closed form ==
builder for all $p<q\le120$; distinctness/positivity for all $p<q\le1200$):

**PROVED (slice theorems; script-verified 0 violations / 53,956 pairs to $q\le5000$):**
- **S1.** $A+B>D_0$ strictly, since $A+B-D_0=(p^2-R_p)Y_q+(q^2-R_q)Y_p>0$
  ($|\mathrm{Re}\,\pi^4|<|\pi^4|=p^2$ because $\mathrm{Im}\,\pi^4\ne0$). So
  $A+B$ hits nothing in the set.
- **S2.** $C+D_0=2\max(X,Y)$. $C+D_0=A$ with $X\ge Y$ $\iff$ $2R_p=p^2$:
  **dead by parity** ($p^2$ odd, $2R_p$ even). Mirror for $B$ with $Y\ge X$.
  (Brute corroboration: the expanded quartics $a^4-14a^2b^2+b^4=0$ and
  $3a^4-10a^2b^2+3b^4=0$ have no solutions $a,b\le4000$; the parity kill is
  the proof.)
- **S3.** $p\nmid Y_p$ always; $p\nmid R_p$, $q\nmid Y_q$, $q\nmid R_q$
  (0 hits / 53,956 pairs — the per-prime UFD lemma persists in the two-prime
  closed form).
- Dead-parity kills: $A+C=D_0$ with $X<Y$ $\iff p^2=2R_p$ (odd = even);
  mirror $B+C=D_0$ with $Y<X$ $\iff q^2=2R_q$.
- $C+D_0\in\{C,D_0\}$ forces $C=0$ or $D_0=0$; distinctness/positivity
  (4,465 pairs to $q\le1200$) excludes it.

**STALL (precise):** after S1/S2/S3 and the dead-parity kills, sum-freeness
of $D((pq)^2)$ is EQUIVALENT to: **no valid $(a,b,c,d)$ solves any of**
- K1: $p^2Y_q=2Y_pR_q$ (forces $v_p(R_q)\ge2$; 2-adically forces
  $v_2(Y_q)=1+v_2(Y_p)$)
- K2: $q^2Y_p=2R_pY_q$ (forces $v_p(Y_q)=2$, i.e. $p^2\mid Y_q$)
- K3/K4: $R_pY_q=3Y_pR_q$ / mirror ($\iff 2C=D_0$, i.e. $\{X,Y\}=\{3m,m\}$)
- K5: $Y_q(p^2+R_p)=Y_p(q^2-R_q)$ ($A+D_0=B$); K6a/b: $A+C=B$ sign-split
  $Y_q(p^2\pm R_p)=Y_p(q^2\pm R_q)$; K7a/b, K8 the $B$-side mirrors
- K9-K16: $2A=B$, $2B=A$, $2C=A$/$2C=B$ (sign-split), $2A=D_0$, $2B=D_0$,
  $2D_0=A$, $2D_0=B$.
The case tree was **mechanically verified as iff-reductions** (666 pairs,
0 mismatches): each listed equation holds iff the corresponding relation
holds.

**Census (closed form, this script):** every relation $x+y=z$ and $2x=y$ over
$\{A,B,C,D_0\}$ for all $p<q\le1500$ (6,670 pairs): **ZERO hits**, consistent
with the builder census to $w\le10^7$. Twin regime $q=p+2$: **vacuous** —
twin primes cannot both be $1\bmod4$, so that structured search space is
empty. $p\mid Y_q$ regime: 2,617 pairs ($q\le2\cdot10^4$), zero relations.

**Near-miss structure (counterevidence hunt):** the closest approach to a
kill-equation is K3 at $(p,q)=(173,7933)$: $X-3Y=50{,}004{,}240\ne0$,
$|\log(X/3Y)|\approx4\cdot10^{-5}$ — the ratios distribute densely near 1
(argmin pairs K1 $(41,4657)$, K2 $(181,17497)$, K4 $(137,3709)$), so **no
congruence or size argument can kill K1-K4 pointwise**: they are genuine
exponential Diophantine equations in $(a,b,c,d)$. Confidence: S1-S3 and the
case-tree reduction high (proved + machine-checked); full freeness still
OPEN — stalled exactly at K1-K4 + K5-K16, which need a descent / mod-$p^2$
/ Gaussian-lattice idea not available this round. Next lever if resumed:
K1's necessary condition $p^2\mid R_q$ (= $p^2\mid q^2-8c^2d^2$) is a
congruence condition on the rep of $q$ — check whether $p^2\mid R_q$ ever
occurs at all, and whether K1 can be killed mod $p^2$ from it.
## Cross-prime divisibility: K2/K9/K11 dead, K1 gated mod 8 (2026-09-01, `[mss-two-prime-crossdiv]`)

Continuation of `[mss-two-prime-freeness]` (the K1-K16 stall). Scripts
`scripts/mss_two_prime_k1_crossdiv.py`, `scripts/mss_two_prime_k12_census.py`
(self-tests inside: closed form == builder, 91 pairs q<=120; identity
$R_q=|8c^4-8qc^2+q^2|$ exact). The named lever — the cross-prime divisibility
conditions K1/K2 force — partially lands:

**CORRECTION (append-only, to `[mss-two-prime-freeness]`).** The filed K2
annotation "(forces $v_p(Y_q)=2$, i.e. $p^2\mid Y_q$)" is **wrong**. The
$p$-valuation of K2 ($2R_pY_q=q^2Y_p$) reads $v_p(\text{LHS})=0$ (S3:
$p\nmid R_p$), forcing $v_p(Y_q)=0$ — vacuous. The load-bearing valuation is
at $q$, and it kills K2 outright:

**T1 (K2 dead).** K2 $\Rightarrow v_q(R_p)=2+v_q(Y_p)\ge2\Rightarrow q^2\mid
R_p$; but $0<R_p<p^2<q^2$ ($|\mathrm{Re}\,\pi^4|<|\pi^4|=p^2$ since
$\mathrm{Im}\,\pi^4=Y_p\ne0$; $R_p\ne0$ since $a^2=b^2(3\pm2\sqrt2)$ has no
integer solutions). Contradiction. Verified: 0 hits / 53,956 pairs
($q\le5000$) and 0 / 11.4M pairs (census below); inequality chain
0 violations.

**T2 (K9, K11 dead).** $2A=B$: $v_p(2p^2Y_q)\ge2$ vs $v_p(q^2Y_p)=0$.
$2B=A$: $v_q(2q^2Y_p)\ge2$ vs $v_q(p^2Y_q)=0$. Both impossible.

**T3 (Lemma A — cross-prime gate on $p\mid R_q$; necessity only).**
$p\mid R_q\Rightarrow$ (i) $p\equiv1\pmod8$; (ii) $\chi_p(q)=\chi_p((2+\sqrt2)/4)$
(a single well-defined coset: the two roots $x=(2\pm\sqrt2)/4$ of
$8x^2-8x+1\equiv0\pmod p$, where $x=c^2q^{-1}$, share a character since
$x_1x_2=1/8$ and $\chi_p(2)=1$). *Proof:* identity
$R_q=|8c^4-8qc^2+q^2|$; mod $p$: $8x^2-8x+1\equiv0$. Verified (22,155 pairs
$q\le3000$): 182 hits, 0 mod-8 violations, 0 coset violations; 11,823
$p\equiv5\pmod8$ pairs: 0 hits; exactly 4 roots $c$ mod $p$ (40/40).
**Reverse FALSE (tracked failure):** the coset is necessary, not sufficient —
4,966/5,148 coset pairs have $p\nmid R_q$; the actual rep $(c,d)$ of $q$ is
one point on the mod-$p$ circle $c^2+d^2\equiv q$, not one of the 8
quartic-root points.

**Consequence for K1.** K1 $\Rightarrow p^2\mid R_q\Rightarrow$ T3 gate, so
K1 is vacuous for every $p\equiv5\pmod8$ — half the pair space gone. But the
gate is not a kill: $p^2\mid R_q$ genuinely occurs — 99 pairs $q\le10^5$
(**79 at $p=17$** — an $R_q$-Wieferich anomaly, next 41:9, 73:4, 89:2;
the uniform model predicts $\approx\pi_4(10^5)/p^2\approx17$ for $p=17$
($\approx23$ total), so $p=17$ runs $\approx5\times$ over and $p=41$ too
(9 vs 2.9) — structurally special, worth its own census). Closest K1 approach
among $p^2\mid R_q$ pairs: $|\log(p^2Y_q/2Y_pR_q)|=0.0117$ at $(41,64997)$.

**K12 checked, not killed.** K12 ($2B=D_0$) forces only
$R_pY_q\equiv-Y_pR_q\pmod q$ — the two terms can cancel mod $q$, so (unlike
K2) no forced individual cross-divisibility; the tempting
"$q\mid Y_p\wedge q\mid R_p\Rightarrow q^2\mid p^4$ impossible" does NOT
apply. (Working notes: `scripts/_tmp_k1_working.txt`.)

**Extended census (script 2).** All 6 sums + 4 doubles over
$\{A,B,C,D_0\}$ for every $p<q\le10^5$ (**11,436,153 pairs**; $w=pq\le10^{10}$,
three orders beyond the $w\le10^7$ builder census): **0 relations**. Cross-div
counts: $q\mid Y_p$: **0**; $q\mid R_p$: 714; both: 0; $p\mid Y_q$: 12,414;
$p\mid R_q$: 5,883; $p^2\mid R_q$: 99; $q^2\mid R_p$: **0** (T1 re-confirmed at
scale). The cross-asymmetry is stark: $p\mid Y_q$ common (0.11%) while
$q\mid Y_p$ never occurs in range (forced $q<2p^2$ by size — $|Y_p|<2p^2$ —
and empirically empty).

**Status after this round.** K2, K9, K11 DEAD (proved); K1 gated
($p\equiv1\bmod8$ + coset + Wieferich-type $p^2\mid R_q$); open: K1, K3, K4,
K5-K8, K10, K12-K16. The K2 kill is a cross-prime SIZE observation
($q^2\mid R_p$ impossible since $R_p<p^2<q^2$); the same asymmetry cannot
touch K1 ($p^2\mid R_q$ is compatible with $R_q<q^2$). Next levers: (a)
explain the $p=17$ $R_q$-Wieferich anomaly (positive density of $q$?); (b)
K3/K4 remain the dense-near-miss wall — genuinely exponential Diophantine.

## K3/K4: quartic-to-quadratic reduction, per-prime square sieve (2026-09-01, `[mss-two-prime-k34]`)

Attack on the two open kill-equations NOT gated by the Wieferich anomaly
(continuation of `[mss-two-prime-freeness]`, `[mss-two-prime-crossdiv]`).
Script `scripts/mss_two_prime_k34_quartic.py` (+ log). K3: $R_pY_q=3Y_pR_q$
($2C=D_0$, $X=3Y$ side); K4 the mirror.

**Near-miss confirmed.** $(173,7933)$: $X-3Y=50{,}004{,}240$ exactly,
$|\log(X/3Y)|=3.589\cdot10^{-5}$ (filed values reproduced).

**CORRECTION (append-only, to `[mss-two-prime-freeness]`).** The filed
argmin line "over $p\le200$, $q\le2\cdot10^5$" overstated the range: that
script's prime table was capped at 20000, so $(173,7933)$ is the closest
K3 pair only for $q\le2\cdot10^4$. Extended to $q\le2\cdot10^5$ the argmins
are K3 $(101,47681)$, $|\log|=1.18\cdot10^{-5}$, and K4 $(61,198221)$,
$3.2\cdot10^{-5}$ (filed K4 $(137,3709)$ was $2.06\cdot10^{-4}$ within
$q\le2\cdot10^4$). The "dense near 1, no pointwise kill" conclusion is
unchanged (and strengthened).

**THEOREM K34 (quadratic reduction; the descent-shaped lever partially
lands).** Fix $p$; let $x=c/d>1$ be the rep ratio of $q$ ($Y_q=d^4\,4x(x^2-1)$,
$R_q=d^4|x^4-6x^2+1|$). Dividing K3 by $x^2$ and setting $u=x-1/x$
($x^2+x^{-2}=u^2+2$):
$$4R_pu=3Y_p|u^2-4|\;\Longleftrightarrow\;3Y_pu^2\mp4R_pu-12Y_p=0$$
-- the kill-equation is a QUADRATIC in $u$. A positive rational root
forces $\Delta=16(R_p^2+9Y_p^2)$ to be a rational square. Mirroring (fix
$q$, quartic in $x_p=a/b$, $u_p=a/b-b/a$, $\Delta=16(9R_q^2+Y_q^2)$):
$$\mathrm{K3}\Rightarrow A(p)\wedge B(q),\quad
  \mathrm{K4}\Rightarrow B(p)\wedge A(q),$$
where $A(n)$: $R_n^2+9Y_n^2=k^2$ and $B(n)$: $9R_n^2+Y_n^2=k^2$ (integer
squares). Machine-verified as an IFF at the equation level (10,731 pairs
$p<q\le2000$, 0 mismatches; the $\Delta$-square step is necessity-only).
Gcd lemmas used: $\gcd(R_p,Y_p)=1$ (S3-refined: odd part of
$\gcd(R,4ab(a^2-b^2))$ is 1), $R_p$ odd, $8\mid Y_p$, $3\nmid R_p$,
$3\nmid k$.

**Primitive-triple / conic characterization (descent shape).**
$A(n)\iff\exists$ coprime $m>n$: $mn=3Y_n/2$, $|m^2-n^2|=R_n$;
$B(n)\iff\exists$ coprime $m>n$: $mn=Y_n/2$, $|m^2-n^2|=3R_n$
($(R,3Y,k)$ / $(Y,3R,k)$ primitive Pythagorean triples). Using
$R^2+Y^2=n^4$: $A(n)\iff\exists$ coprime $r,s$: $rs=Y_n$ and
$n^2=2s^2-r^2$ or $n^2=s^2-2r^2$ (Pell-type conics; parametrizations
$n=|m^2+2mn-n^2|$ resp. $n=|m^2-2n^2|$ with product equation
$rs=Y_n=4ab|a^2-b^2|$ -- a smaller-variables system a descent could
target; NOT discharged this round).

**Census (the per-prime sieve).** $A$, $B$ tested for all 12,980 1 mod 4
primes $\le3\cdot10^5$: **0 hits**. Hence **K3 and K4 are dead for every
pair with $\min(p,q)\le3\cdot10^5$ with the other side UNBOUNDED** (any
K3/K4 solution needs $p,q>3\cdot10^5$, $w=pq>9\cdot10^{10}$) -- a
per-prime sieve, strictly stronger than the pair census (which bounds
only $q$). Direct K3/K4 pair census $p<q\le3\cdot10^5$: **84,233,710
pairs, 0 hits** (independent confirmation).

**Conjecture K34** (new, cheap to test, kills K3+K4 outright if proved):
$A(n)$ and $B(n)$ never hold for a prime $n\equiv1\pmod4$. Heuristic:
requires a primitive Pythagorean triple whose leg product is exactly
$3Y_n/2$ (resp. $Y_n/2$) -- probability $\sim O(n^{-2})$ per prime,
summable, so expected total hits over ALL primes $\ll1$.

**Status.** K3/K4: not killed in general, but reduced from exponential
pair-Diophantine to two per-prime square tests + a named descent gap.
Open: the conic-descent (case $lpha$: $n^2+r^2=2s^2$, case $eta$:
$n^2+2r^2=s^2$, both with $rs=Y_n$) and the same treatment for K5-K8,
K10, K13-K16.

## K5-K8 DEAD: branch-split + rep-ratio injectivity (2026-09-01, `[mss-two-prime-k58]`)

Attack on the six remaining separated kill-equations (continuation of
`[mss-two-prime-freeness]`, `[mss-two-prime-crossdiv]`, `[mss-two-prime-k34]`).
Script `scripts/mss_two_prime_k58_branch.py` (+ log). Unlike K1-K4, K5-K8 are
**separated** multiplicative equations $Y_q\alpha_p=Y_p\beta_q$ with
$\alpha\in\{p^2\pm R_p\}$, $\beta\in\{q^2\pm R_q\}$ — the quartic reduction of
K3/K4 is not needed; a direct branch argument kills all four sign combos:

**Lemma B1 (branch split).** For prime $n=a^2+b^2$ ($1\bmod4$, $a>b>0$), put
$s=a^2-b^2$, $t=ab$, $u=s/t=x-1/x$ ($x=a/b$). Then $n^2=s^2+4t^2$ and
$$\{n^2+R_n,\;n^2-R_n\}=\{2s^2,\;8t^2\},\qquad
n^2+R_n=2s^2\iff \mathrm{Re}(\pi^4)=s^2-4t^2>0\iff u>2.$$
(The threshold $u=2$ is exactly $x=1+\sqrt2$; note $R_n\ne0$, $s,t>0$,
$\gcd(s,t)=1$.) Call $2s^2$ the S-branch, $8t^2$ the T-branch of $n$.

**Lemma B2 (same-branch kill).** Same branch on both sides of
$Y_q\alpha_p=Y_p\beta_q$ forces $s_pt_q=s_qt_p$, i.e. $u_p=u_q$, i.e.
$a_p/b_p=a_q/b_q$; both reps primitive, so $(a_p,b_p)=(a_q,b_q)$ and $p=q$ —
impossible.

**Lemma B3 (cross-branch kill, "$q=2p$").** Cross branches force
$s_ps_q=4t_pt_q$, i.e. $u_pu_q=4$. Since $u=x-1/x$ is a bijection
$(1,\infty)\to(0,\infty)$, the unique solution is
$x_q=\dfrac{x_p+1}{x_p-1}=\dfrac{a_p+b_p}{a_p-b_p}$ (always $>1$); and
$\gcd(a_p+b_p,a_p-b_p)=1$ ($a,b$ opposite parity, both sums odd, common
divisor divides $2a,2b$ and is odd), so the rep of $q$ is
$(c_q,d_q)=(a_p+b_p,\,a_p-b_p)$ and
$q=c_q^2+d_q^2=2(a_p^2+b_p^2)=2p$ — impossible for distinct odd primes.

**THEOREM K58.** None of the four equations
$Y_q(p^2\pm R_p)=Y_p(q^2\pm R_q)$ holds for any distinct $1\bmod4$ primes
$p<q$. Mapping to the filed labels: K5 ($A{+}D_0=B$) = combo $(+,-)$: dead by
B2/B3; K6a/b ($A{+}C=B$, cases $X{>}Y$/$Y{>}X$) = combos $(+,+)/(-,-)$: dead;
K7/K8 (B-side mirrors $B{+}D_0=A$, $B{+}C=A$) = combos $(-,+)/(-,-)$: dead.
(For $(\pm,\mp)$ the two branch cases are even incompatible with
$u_pu_q=4$, which forces $u_p,u_q$ on opposite sides of 2; for
$(\pm,\pm)$ the cross case is branch-compatible and dies only via $q=2p$.)

**Machine verification** (log): branch-split lemma 0 violations on all 2,549
$1\bmod4$ primes $\le5\cdot10^4$; equation-iff-branch-prediction check 0
mismatches over all 1,296,855 pairs $p<q\le3\cdot10^4$; all five K5-K8
relations 0 hits; extended relations census $p<q\le10^5$ (**11,436,153
pairs**) 0 hits; $u\cdot u'=4$ identity 0 violations on 2,000 random
coprime trials (an initial identity check with 1,216 "violations" was a
bug in the test's cross-multiplication, not in the math — fixed with exact
Fractions and re-verified).

**Status.** K5, K6a, K6b, K7a, K7b, K8 all DEAD (proved, no conjectures
used). Sum-freeness kill list down to **K1** (Wieferich-gated:
$p^2\mid R_q$, $p\equiv1\bmod8$), **K3/K4** (K34-conjecture-gated:
$A(n),B(n)$ per-prime square conditions), **K10, K12-K16**. Flagged
discrepancy (not touched here): the filed T2 in `[mss-two-prime-crossdiv]`
explicitly kills "$2B=A$", which under the sequential K9-K16 labeling
(line order $2A{=}B, 2B{=}A,\ldots$) is K10 — yet that section's status line
lists K10 as open; one of the two is mislabeled, resolve on next visit.
Note also the killed K5-K8 shape (per-prime ratio equality
$(p^2\pm R_p)/Y_p\in\{s/2t,\,2t/s\}$ taking equal values at two primes) is
the same "per-prime value-set collision" genus as Conjecture K34 — here the
collision is provably impossible, there it is only conjectured.


**LABEL RESOLUTION (2026-09-01, appended after a subagent's reading pass; agent itself died
on the output cap before filing).** The K10-mislabel flag above was a FALSE ALARM. The canonical
K9-K16 mapping is pinned by `sign_reduce` in `mss_two_prime_freeness_closedform.py` (lines 129-146):
K9=2A=B, K10=2A=D0, K11=2B=A, K12=2B=D0, K13/K14=2C=A/B, K15/K16=2D0=A/B. Under this mapping T2
kills exactly K9 and K11 (as the filed status lines state); "2B=A" is K11, not K10. No status-line
correction needed; this note supersedes the flag. Lead left unverified by the same agent (treat as
conjecture): every D-element factors as 4 t_p^2 t_q^2 x (u-only quantity) with u=s/t=x-1/x, which
would reduce ALL kill-equations to quadratic curves in (u_p,u_q) and give per-prime Delta-square
sieves for K1-K4, K10, K12-K16 uniformly.

## u-factorization theorem; K1, K10, K12-K16 all DEAD; kill list down to K3/K4 (2026-09-01, `[mss-two-prime-uquad]`)

Attack on the six open doubles K10, K12-K16 + the gated K1 (continuation of
`[mss-two-prime-freeness]`, `[mss-two-prime-crossdiv]`, `[mss-two-prime-k34]`,
`[mss-two-prime-k58]`; the LABEL RESOLUTION lead is VERIFIED below). Scripts
`scripts/mss_two_prime_u_factorization.py`, `mss_two_prime_k10_16_sieve.py`,
`mss_two_prime_k10_16_closedforms.py`, `mss_two_prime_k10_16_discsq.py`,
`mss_two_prime_k1_k12_gates.py` (+ logs; two bugs found and fixed en route,
see tracked failures).

**THEOREM U (u-factorization; the dead agent's lead, verified).** For a
1 mod 4 prime $n=a^2+b^2$ put $s=a^2-b^2$, $t=ab$ ($\gcd(s,t)=1$, $s$ odd,
$t$ even), $x=a/b$, $u=s/t=x-1/x$. Then $n^2=t^2(u^2+4)$, $Y_n=4t^2u$,
$R_n=t^2|u^2-4|$, and with $f=4t_p^2t_q^2$ EVERY element of the closed form
is $f\times$ a function of $(u_p,u_q)$ alone:
$$A=f\,u_q(u_p^2{+}4),\quad B=f\,u_p(u_q^2{+}4),\quad X=f\,|u_p^2{-}4|u_q,\quad
Y=f\,u_p|u_q^2{-}4|$$
(one-line proof: $p^2=s_p^2{+}4t_p^2=t_p^2(u_p^2{+}4)$, $Y_q=4s_qt_q$).
Machine-verified exact (Fractions) on all 3,160 pairs $p<q\le1000$, 0
mismatches. Consequence: every kill-equation, after cancelling $f$, is an
equation in $(u_p,u_q)$ ONLY.

**Reduction machinery (iff-verified).** Each of K1, K10, K12-K16 is
piecewise-quadratic in $w=u_q$ (pieces = the two $Q=|w^2-4|$ branches, plus
the $g$-vs-$h$ sign for K13/K14; 16 pieces for K10/K12-K16, 2 more for K1),
with closed-form coefficients in $(v,P)=(u_p,|u_p^2-4|)$, all 16 machine-equal
to an independent interpolation solver (2,352 checks, 0 mismatches) and the
iff "relation $\iff$ $w$ is a region-valid rational root" checked on all 1,275
pairs $p<q\le600$ (0 mismatches; brute census 22,155 pairs $q\le3000$, 0
relations). The same reduction reproduces K3/K4 exactly ($P^2{+}144v^2=\Box$
$\iff$ filed $A(n)$: $R^2{+}9Y^2=\Box$), unifying the whole kill list as
predicted. Per-prime square-gate census (disc-square test, all pieces, all
12,980 1 mod 4 primes $\le3\cdot10^5$): **0 hits** (233,640 conic tests).

**THEOREM K1-DEAD (all pairs, unconditional).** K1 ($p^2Y_q=2Y_pR_q$)
$\iff w(v^2{+}4)=2vQ$; rational $w$ forces
$\Delta=(v^2{+}4)^2{+}64v^2=(p^4{+}4Y_p^2)/t_p^4=\Box$, i.e. $(p^2)^2{+}(2Y_p)^2=k^2$
a primitive Pythagorean triple ($p\nmid Y_p$, S3). Odd leg: $p^2=m^2-n^2$,
$2Y_p=2mn$; $(m{-}n)(m{+}n)=p^2$, $\gcd=1$ (both odd) forces $m-n=1$,
$m+n=p^2$, so $Y_p=mn=(p^4{-}1)/4$; but $Y_p=4ab(a^2{-}b^2)<2p\cdot p=2p^2<(p^4{-}1)/4$
for $p\ge5$. Contradiction. **K1 was the last Wieferich-gated equation; the
gate dissolves.**

**THEOREM K10/K12-DEAD (all pairs, unconditional).** K12 ($2B=D_0$)
$\iff$ one of two quadratics in $w$, both with
$\Delta=P^2-48v^2=(R_p^2-3Y_p^2)/t_p^4$; so K12 forces
$R_p^2-3Y_p^2=k^2$. Then $(R{-}k)(R{+}k)=3Y^2$; $R,k$ odd, $3\nmid R$,
$\gcd(R,Y)=1$ give coprime $d=(R{-}k)/2,\ e=(R{+}k)/2$ with
$de=3(Y/2)^2$, so $\{d,e\}=\{u^2,3w^2\}$, $Y=2uw$, $R=u^2{+}3w^2$ (or
mirror). Combined with $R^2{+}Y^2=p^4$ (exact identity):
$(u^2{+}w^2)(u^2{+}9w^2)=p^4$. Both factors $>1$, so
$\{u^2{+}w^2,\,u^2{+}9w^2\}=\{p,p^3\}$ (the $p^2,p^2$ and $1,p^4$ cases
die), giving $8w^2=p^3-p$ with $p\mid w$ -- but then $u^2{+}w^2>p=u^2{+}w^2$.
Contradiction; $R^2-3Y^2=\Box$ is IMPOSSIBLE for every 1 mod 4 prime
(verified 0 hits, primes $\le10^5$). K10 $\iff$ K12 with $p\leftrightarrow q$
($2A=D_0$ for $(p,q)$ $=$ $2B=D_0$ for $(q,p)$), and the gate sits on the
first label's prime, so **K10 and K12 are both dead for all pairs**.

**THEOREM K13-K16 DEAD (all pairs, unconditional).** All four pieces of K14
and both pieces of K16 share $\Delta=4(P^2{+}12v^2)$, so any solution forces
the per-prime gate **G3(n): $s_n^4+4s_n^2t_n^2+16t_n^4=\Box$**. G3 is
impossible: $s^4{+}4s^2t^2{+}16t^4=(s^2{+}2st{+}4t^2)(s^2{-}2st{+}4t^2)$
(Sophie-Germain shape), the two factors are coprime (odd, and any common odd
prime divides $4st$ and then both $s,t$), so each is a square: $U^2,W^2$ with
$U^2+W^2=2p^2$, $U^2-W^2=4st$. In $\mathbb Z[i]$, $2p^2=(1+i)(1-i)\pi^2\bar\pi^2$
($\pi=a{+}bi$); primitivity ($\gcd(U,W)=1$; $U=W=p$ gives $U^2-W^2=0$) forces
$\{U,W\}=\{|s{+}2t|,|s{-}2t|\}$, whence $U^2-W^2=8st\ne 4st$. Contradiction
(verified: $\gcd(A,B)=1$ all 329 primes $\le5000$; G3 0 hits $\le10^5$).
Since K13 $\iff$ K14 and K15 $\iff$ K16 under $p\leftrightarrow q$ (C is
symmetric, $A\leftrightarrow B$), **all four of K13, K14, K15, K16 are dead
for every distinct 1 mod 4 pair.**

**Tracked failures (append-only).** (i) Interpolation bug: Lagrange basis
initialized as $w^2$ instead of $1$ made every prediction empty -- the first
iff-check "PASS" was vacuous; caught because a hand slip claimed K12's
discriminant $(y^2-32)^2$ is auto-square (it is $(y^2-32)^2-768$); fixed +
re-run non-vacuously. (ii) Two closed-form transcription errors (K10 sig$-$
$w^2$-coeff; K13(-1,+1) middle coeff) caught by the 2352-check equality test.
(iii) A tempting mod-9 kill of G3 ($\equiv3\bmod9$ when $3\nmid st$) is
VACUOUS: $3\mid s_n\iff n\equiv2\pmod3$ and $3\mid t_n\iff n\equiv1\pmod3$
(verified 4,783/4,783 primes $\le10^5$), so $3\nmid st$ never occurs; the
real kill is the $\mathbb Z[i]$ argument above.

**Status after this round.** Every kill-equation is now dead or per-prime
square-gated: K1, K2, K5-K12, K13-K16 all DEAD (proved, unconditional);
**the ONLY survivors are K3/K4**, which are dead for every pair with
$\min(p,q)\le3\cdot10^5$ (K34 sieve) and in general are gated exactly by
**Conjecture K34** ($A(n)$: $R_n^2{+}9Y_n^2=\Box$, $B(n)$: $9R_n^2{+}Y_n^2=\Box$
never hold for a 1 mod 4 prime; 0 hits on 12,980 primes $\le3\cdot10^5$).
**Two-prime sum-freeness of $D((pq)^2)$ is now EQUIVALENT to Conjecture
K34** -- the entire $\omega_1=2$ stratum hangs on one cheap per-prime square
condition. Next lever: the K34 conic descent (filed in
`[mss-two-prime-k34]`: $n^2=2s^2-r^2$ or $n^2=s^2-2r^2$ with $rs=Y_n$), now
the single named gap for the whole two-prime freeness theorem.

## K34 as rational points on genus-1 quartics M_A, M_B (2026-09-01, `[mss-k34-elliptic]`)

Goal: settle K3/K4 (the last gates for two-prime sum-freeness) by determining
the rational points on the two master quartics. Result: the reduction, the
Weierstrass models, and the full Mordell-Weil ranks are now PROVED with
machine-checked descent; K34 itself (no non-degenerate square-X point)
remains OPEN, with the Mordell-Weil sieve built but not collapsed. Scripts:
`scripts/mss_k34_elliptic.py` (+ parts p2..p12) and
`scripts/mss_k34_elliptic.log`.

### 1. The reduction (verified, exact)

With $n=a^2+b^2$ prime $\equiv 1 \pmod 4$, $s=a^2-b^2$, $t=ab$, $u=s/t$:
$A(n)\ \Longleftrightarrow\ t^4(u^4+136u^2+16) = \square$ and
$B(n)\ \Longleftrightarrow\ t^4(9u^4-56u^2+144) = \square$
(re-verified from scratch: `QA*(x^4)-P_A(x^2) = 0`, `QB*(x^4)-P_B(x^2) = 0`
with $u=x-1/x$, and $t^4Q_A = a^8+132a^6b^2-250a^4b^4+132a^2b^6+b^8$,
$t^4Q_B = 9a^8-92a^6b^2+310a^4b^4-92a^2b^6+9b^8$, all exact in sympy).
Hence, with $X=(a/b)^2$:

- **K34-A** $\Longleftrightarrow$ $M_A:\ V^2 = X^4+132X^3-250X^2+132X+1$
  has no rational point with $X$ a positive rational square other than the
  degenerate $X=0,1$;
- **K34-B** $\Longleftrightarrow$ $M_B:\ V^2 = 9X^4-92X^3+310X^2-92X+9$
  likewise.

### 2. Weierstrass models and birational maps (verified on all known points)

- $M_A \leftrightarrow E_A:\ Y^2 = X^3-250X^2+17420X+35848$, via
  $\psi_A(X,V):\ x_E=(V-1-66X)/X^2$,
  $(X_E,Y_E)=(-2x_E,\ 2(x_E^2-1)X+132(x_E-1))$; inverse
  $X = 2(y+66x)/(x(x-4))$ on the shifted model
  $\tilde E_A:\ y^2=x^3-256x^2+18432x$ ($x=X_E+2$). Origin choice:
  $(0,-1)\mapsto O$, $(0,1)\mapsto(4606,-304128)$; the standard conversion
  with origin $(0,1)$ is $\chi_A=-\psi_A\circ(V\mapsto -V)$ (tangent-line
  algorithm; $\chi_A(0,1)=O$).
- $M_B \leftrightarrow E_B:\ Y^2 = X^3+310X^2+8140X+51912$, via
  $\psi_B(X,V):\ x_E=(V-3+\tfrac{46}{3}X)/X^2$,
  $(X_E,Y_E)=(-6x_E,\ 3(2(x_E^2-9)X-\tfrac{92}{3}(x_E-3)))$;
  $(0,-3)\mapsto O$, $(0,3)\mapsto(-\tfrac{674}{9},-\tfrac{23552}{27})$.

All 12 known $M_A$ points (including $X=\tfrac{66}{1151},\tfrac{1151}{66}$
with $V=\pm\tfrac{3693311}{q^2}$; the search log stores $V\cdot q^2$) and all
12 known $M_B$ points (including $X=\tfrac{209}{414},\tfrac{414}{209}$,
$V=\pm\tfrac{943587}{q^2}$) map onto their curves and back (exact Fraction
arithmetic, every point verified on-curve in both directions).

**Jacobian correction (tracked failure, now fixed).** The binary-quartic
invariants are $I_1=10240,\ I_2=-8912896$ for $M_A$ and $I_1=71680,\
I_2=-38273024$ for $M_B$ (as previously claimed), but the Jacobian is
$y^2=x^3-27I_1x-27I_2$ — the earlier claim $y^2=x^3-27I_2x-27I_1$ has the two
invariants swapped. Evidence: (i) the generic tangent construction applied to
the test quartic $v^2=x^4+3x^3+5x^2+3x+1$ gives $j=256000/117$, equal to
$j(y^2=x^3-27I_1x-27I_2)$ and unequal to the swapped form
($j=10536048/6091$); (ii) Frobenius traces of the swapped cubic differ from
$\tilde E_A$ at $p=7,13,17,19,23,29,31$; (iii) $y^2=x^3-276480x+240648192$
($=x^3-27I_1x-27I_2$ for $M_A$) is $\mathbb{Q}$-isomorphic to $E_A$ ($c_4$
ratio $u^4=81$, $c_6$ ratio $u^6=729$, i.e. scaling $u=3$ plus shift), and
$x^3-1935360x+1033371648\cong E_B$ likewise.
`[to-verify]` cite the classical normalization from a primary source.

### 3. Mordell-Weil groups (proved)

**Theorem.** $E_A(\mathbb{Q}) \cong \mathbb{Z}\cdot(126,512)\oplus\mathbb{Z}/2$
with torsion generator $(-2,0)$, and
$E_B(\mathbb{Q}) \cong \mathbb{Z}\cdot(-146,1536)\oplus\mathbb{Z}/2$ with
torsion generator $(-18,0)$. In particular $M_A(\mathbb{Q})$ and
$M_B(\mathbb{Q})$ are infinite; the "exactly the known points"
hypothesis is FALSE.

*Proof.* (a) *Torsion:* the gcd of $\#E(\mathbb{F}_p)$ over
$p\in\{5,7,11,13,17,19\}$ equals 2 for $E_A, E_B, \tilde E_A, \tilde E_B$,
so the torsion divides 2; each curve has a rational 2-torsion point
($x^3-250x^2+17420x+35848=(x+2)(x^2-252x+17924)$ and
$x^3+310x^2+8140x+51912=(x+18)(x^2+292x+2884)$, quadratic factors
irreducible over $\mathbb{Q}$) — torsion is exactly $\mathbb{Z}/2$.
(b) *2-isogeny descent* (exact arithmetic; locally insoluble homogeneous
spaces $C_d:\ N^2=dM^4+aM^2e^2+(b/d)e^4$, squarefree $d\mid b$, killed mod
$p^2$ for $p\le97$ and mod 32 for $p=2$, primitive classes only — these are
rigorous one-way obstruction kills):
- $\tilde E_A:\ y^2=x^3-256x^2+18432x$ ($a=-256$, $b=18432=2^{11}\cdot3^2$):
  $\alpha(\tilde E_A)=\{1,2\}$ (both realized: $(4,264)$ and $(128,512)$);
  dual $E'_A:\ y^2=x^3+512x^2-8192x$: $\alpha'(E'_A)\subseteq\{\pm1,\pm2\}$
  with all four locally soluble, so $|\alpha'|\le4$ and
  $2^{r+2}=|\alpha|\,|\alpha'|\le8$, i.e. $r\le1$; $(128,512)$ is not
  torsion (the torsion group has only $O$ and $(0,0)$) $\Rightarrow r=1$.
- $\tilde E_B:\ y^2=x^3+256x^2-2048x$ ($b=-2048=-2^{11}$):
  $\alpha(\tilde E_B)=\{1,-2\}$ (realized by $(16,192)$ and $(-2,192)$);
  dual $E'_B:\ y^2=x^3-512x^2+73728x$: soluble classes $\{1,2,3,6\}$, so
  $|\alpha'|\le4$ and $r\le1$; $(-146,1536)$ is not torsion
  $\Rightarrow r=1$.

**Correction (tracked failure):** an earlier session line "rank$(E_B)=2$"
was a bookkeeping slip ($2\cdot4=8=2^{r+2}$ gives $r=1$, not 2). The descent
record above is the corrected one. `[to-verify]` the kill implementation has
not been independently reimplemented; the kills are load-bearing only for
the upper bounds $r\le1$.

(c) *Generators and known points.* $G_A=(126,512)$ and $G_B=(-146,1536)$
have infinite order; every known point is a small combination. $M_A$
(writing $T_A=(-2,0)$): $(1,4)\mapsto-G_A$; $(1,-4)\mapsto-G_A+T_A$;
$(31/35,\pm\cdot)\mapsto G_A+T_A,\ -3G_A$; $(35/31,\pm\cdot)\mapsto
-3G_A+T_A,\ G_A$; $(66/1151,\pm\cdot)\mapsto-4G_A,\ -4G_A+T_A$;
$(1151/66,\pm\cdot)\mapsto2G_A,\ 2G_A+T_A$; $(0,1)\mapsto-2G_A+T_A$;
$(0,-1)\mapsto O$. $M_B$ ($T_B=(-18,0)$): $(1,12)\mapsto G_B$; $(1,-12)\mapsto G_B+T_B$;
$(5/41,2508)\mapsto-G_B$; $(41/5,2508)\mapsto3G_B$;
$(209/414,943587)\mapsto4G_B+T_B$ (verified exactly in rational
arithmetic); $(414/209,-943587)\mapsto4G_B$; $(0,3)\mapsto2G_B+T_B$
(verified exactly). The complete on-curve image list is in
`mss_k34_elliptic_p12.log`. Note the involution rule (checked on all
verified pairs): the quartic sign flip $V\mapsto-V$ acts on $E(\mathbb{Q})$
as $P\mapsto C-P$ with $C=\psi(0,v_0)$, i.e. $C=-2G_A+T_A$ for $M_A$ and
$C=2G_B+T_B$ for $M_B$; this determines every paired image from its partner.
Index of
$\langle G\rangle$ inside the free part not proved `[to-verify]`; nothing
below depends on index 1.

### 4. Genus-3 square covers: killing primes

Non-degenerate square-$X$ points of $M_A$ correspond to rational points
$x\ne0,\pm1$ on the genus-3 double covers
$C3_A:\ W^2=x^8+132x^6-250x^4+132x^2+1$ and
$C3_B:\ W^2=9x^8-92x^6+310x^4-92x^2+9$ (take $W=V$, $X=x^2$). Brute-force
residue classification gives **killing primes** (primes at which the only
solvable residue classes are $x\equiv0,\pm1$): $C3_A$: $\{3,5,11,13\}$;
$C3_B$: $\{3,5,19,29\}$. Consequence: any K34-A counterexample
$n=a^2+b^2$ prime satisfies $3\cdot5\cdot11\cdot13\mid ab(a^2-b^2)$;
any K34-B counterexample satisfies $3\cdot5\cdot19\cdot29\mid ab(a^2-b^2)$.

### 5. Mordell-Weil sieve on the square-X condition: OPEN

The square-X condition on the rank-1 group $\langle G_A\rangle\oplus
\mathbb{Z}/2$ was sieved over $n\in\mathbb{Z}$ (condition
$X(nG_A+tT_A)\in\{0,1\}$ at the killing primes $3,5,11,13$ and
QR-or-infinity elsewhere, classes merged by CRT, primes ordered by
constraint density). With primes $<400$ the sieve does NOT collapse: coset
$t=0$ retains 379,620 classes mod 653,083,200; coset $t=1$ retains
16,322,040 classes mod 528,313,804,200 (stopped at $p=389$ on modulus size;
survivor density $\approx3\cdot10^{-5}$, still decreasing). So no proof and
no refutation this round. Next levers: primes with
$\mathrm{ord}_p(G_A)$ coprime to the accumulated modulus; sieving the
genus-3 Jacobian directly; or the sibling 2-cover
$D_A:\ w^2=z^4+128z^2-512$ (same invariants $I_1,I_2$, another 2-covering
of $E_A$) with the extra condition $z^2-4=\square$.

### 6. Tracked failures (append-only)

1. The brief's Jacobian formula $y^2=x^3-27I_2x-27I_1$ is **wrong**
   (invariants swapped); correct is $y^2=x^3-27I_1x-27I_2$ (Section 2).
2. "rank$(E_B)=2$": arithmetic slip ($2\cdot4=8\Rightarrow r=1$); corrected
   in Section 3.
3. Discriminant $-b_2^4b_6-8b_4^3-27b_6^2+9b_2b_4b_6$ is wrong; correct:
   $\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6$ (verified on
   $y^2=x^3+ax^2+bx$ and by locating the singular point of $\tilde E_B$
   mod 3).
4. Infinite loop in the group-law `mul` for negative $n$ ($n\gg=1$ never
   reaches 0) — hit twice.
5. Sieve bookkeeping: skipping classes where $X\bmod p$ is undefined (the
   infinity class) wrongly killed them; fix: keep those classes.
6. Modular doubling slope is $(3x^2+2a_2x+a_4)/(2y)$ — dropping $a_4$
   silently leaves the curve mod $p$.
7. `Fraction % p` is not modular reduction of a rational; use
   $n\cdot d^{-1}\bmod p$.
8. Part-1 reduction first used $u=s/t-t/s$ (wrong identity); correct is
   $u=s/t$.
9. **Claude independent verification of Section 3 (exact arithmetic,
   `mss_k34_claude_mw_check.py`): the rank/torsion theorem and maps are
   CONFIRMED (all 24 images on-curve, all +V image classes reproduced,
   $C_A=-2G_A+T_A=(4606,-304128)$ and $C_B=2G_B+T_B$ reproduced). Three
   transcription slips found, none load-bearing:** (i) the Section 3 witness
   "$(-2,192)$" for class $-2$ of $\alpha(\tilde E_B)$ is not on the curve —
   the class is realized by the torsion point $(0,0)$ ($\alpha=b=-2048$);
   (ii) the p4 script comment's witness "$(x=-144)$" for class $-1$ is not on
   the curve (class $-1$ is Selmer-killed anyway, so no impact); (iii) the
   Section 3 image table swaps the $T$-partners of the $(66/1151)$ and
   $(1151/66)$ rows — correct entries (consistent with the verified flip
   rule $P\mapsto C-P$): $(66/1151,-)\mapsto 2G_A+T_A$,
   $(1151/66,-)\mapsto -4G_A+T_A$. The p12 log's on-curve image list remains
   the authoritative record.
10. **Genus-3 first decomposition attempt was WRONG and self-detected**: the
    `mss_k34_g3jac_frobenius.py` run pairing the Prym against
    ("EBt", $E_B$)-type candidates matched only 4/36 primes and failed 5/8
    full Frobenius checks — the agent's own script caught it before any
    claim was filed; the correct decomposition (quotient-involution route,
    Section 8, 36/36 primes) supersedes it. Claude's first hand spot-check
    also produced a false mismatch: miscounting $\#\tilde E_A(\mathbb{F}_7)$
    as 5 (actual 6, $t=2$); with the correct quotient traces the
    decomposition is consistent at all 8 full primes. Lesson: verify
    elliptic-curve point counts by script, not by hand, before declaring a
    Frobenius mismatch.

### 7. Bottom line

K3/K4 (K34) remain OPEN. New and proved here: the two-prime question is
exactly a rational-point question on two genus-1 curves with **rank-1**
Mordell-Weil groups (fully computed), the genus-3 covers have killing primes
forcing $3\cdot5\cdot11\cdot13\mid ab(a^2-b^2)$ (A-case) and
$3\cdot5\cdot19\cdot29$ (B-case), and the MW sieve machinery for the final
square-X condition is built and running. The obstruction is now precisely
located: the sieve must separate the rank-1 lattice from the square-X locus,
and primes below 400 do not suffice.
### 8. Genus-3 Jacobian decomposition and the Chabauty gate (NEW 2026-09-01)

Both genus-3 covers are **bielliptic-hyperelliptic** (octic even in $x$; the
three involutions $\iota:x\mapsto-x$, $\rho$, $\iota\rho$ have genus-1
quotients), and their Jacobians split:

$$J(C3_A)\sim E_{\iota}\times E_{\rho}\times E_G,\qquad
J(C3_B)\sim E'_{\iota}\times E'_{\rho}\times E_G,$$

with (classical binary-quartic invariants of the quotient quartics, Jacobian
normalization $y^2=x^3-27I_1x-27I_2$ as in Section 2):
- $C3_A/\iota$ and $C3_A/\rho$ both give $y^2=x^3-276480x+240648192$
  ($I_1=10240$, $I_2=-8912896$) — $\mathbb{Q}$-isogenous to the **master
  $E_A$** (equal $j=-8000/81$; Frobenius traces agree with $\tilde E_A$ at
  **all 45 good primes $7\le p\le211$**, zero mismatches, independently
  recomputed in `mss_k34_g3jac_claude_check.py`);
- $C3_B/\iota$, $C3_B/\rho$ give $y^2=x^3-1935360x+1033371648$
  ($I_1=71680$) — isogenous to the **master $E_B$** (same check, 0
  mismatches);
- the **common Prym factor** $E_G:\ y^2=x^3-504576x+131604480$
  ($I_1=18688$, $I_2=-4874240$), $j=1556068/81$ (exact), with cubic
  $(x-480)(x-336)(x+816)$ — full rational 2-torsion — and torsion group
  exactly $\mathbb{Z}/2\times\mathbb{Z}/4$ (order-4 points $(48,\pm10368)$,
  $(912,\pm20736)$; $\gcd\#E_G(\mathbb{F}_p)=8$ over $p\in\{5..43\}$).

**Theorem (rank drop).** $\operatorname{rank}E_G=0$, rigorously, by sharp
2-isogeny descent at all three 2-torsion points (same kill method as
Section 3): at each $\theta\in\{-816,336,480\}$ the locally soluble classes
give $s_A\le2,\ s_B\le0$ (resp. $1,1$; $2,0$), and the sharp subgroup bound
$\operatorname{im}\alpha_1\subseteq\langle$ known-point images$\rangle$ with
$\dim=2$ forces $\operatorname{rank}E_G\le0$ at all three $\theta$; equality
since known points span. Hence

$$\operatorname{rank}J(C3_A)=\operatorname{rank}J(C3_B)=1+1+0=2<3=\text{genus}.$$

*Verification record (Claude, independent):* the degree-6 Frobenius
polynomial of both covers equals the product of the three quotient
char-polynomials at all 8 full primes $7\le p\le31$ (every
$\sigma_1=p+1-\#C3(\mathbb{F}_p)$ cross-checked by hand against the trace
triples) and the $\#C(\mathbb{F}_p)$ predictions hold at **36/36** primes up
to 211; quartic-vs-cubic trace agreement 7..211 with zero mismatches; the
$\theta=-816$ descent chain independently re-derived (soluble classes
$[1,2,3,6]$, dual $s_B\le0$). Bad primes of both octics: $\{2,3\}$ only.
Scripts: `mss_k34_g3jac_frobenius.py/.log` (superseded first attempt
$P\sim$EBt$\,\times\,E_B$ FAILED its own checks, 4/36 primes — discarded;
see tracked failure 10), `mss_k34_g3jac_quotients.py/.log` (final,
authoritative), `mss_k34_g3jac_rank.py/.log`, `mss_k34_g3jac_claude_check.py/.log`.

**Chabauty gate.** Since rank $J=2<g=3$, Coleman's method applies **in
principle**: at a good prime $p>2g+1$, $\#C3_A(\mathbb{Q})\le
\#C3_A(\mathbb{F}_p)+2g-2$. At $p=11$: $\#C3_A(\mathbb{F}_{11})=8$, giving
$\#C3_A(\mathbb{Q})\le12$. The 8 already-known points ($x=0$: $W=\pm1$;
$x=\pm1$: $W=\pm4$; two points at infinity) leave only 4 spare points.
**NAMED GAP (the gate to K34-A): the actual Coleman computation** —
$p$-adic annihilation of the rank-2 Mordell-Weil basis of
$J(C3_A)(\mathbb{Q})$ (basis from $E_A$ copies $\times$ $E_G$ torsion; the
Prym quotient is trivial on rank) via an honest annihilating differential
$\omega\in H^0(C3_A,\Omega^1)$ with $\int_{\gamma}\omega=0$ for all MW
classes, then a residue/Clarkson-type bound — has NOT been carried out.
If it yields $\#C3_A(\mathbb{Q})=\{$the 8 known points$\}$, then K34-A is
**PROVED** (no square-$X$ points $\ne0,1$ on $M_A$, hence no $\omega_1=2$
counterexample). Same program for $C3_B$ ($\#C3_B(\mathbb{F}_{11})=24$,
bound $\le28$) closes K34-B. This is the first proof *path* (not just
evidence) found for K34; it is a standard-but-laborious computation
(MW-basis p-adic precision, MWM integration à la Balakrishnan–Tuitman or
Coleman integration in Sage).

## K34 round 2: deepened sieve + sibling covers D_A/D_B (2026-09-02, `[mss-k34-sieve2]`)

Scripts `mss_k34_sieve2_p1..p9.py` + state files `mss_k34_sieve2_state{A,B}.json`
(scripts folder). Nothing here modifies the proved content of
`[mss-k34-elliptic]`; it deepens the sieve (Section 7 there), settles the
sibling covers (lever 2), and adds one genuinely new, **verified** mechanism
(p-adic refinement of pole classes, 2c below) that is the first
concrete path from "sieve says few classes survive" to an actual proof.

### 1. Corrections to the killing-prime list (both cases)

- **$p=3$ is vacuous, not killing.** $C3_A \bmod 3:\ W^2=(x^4+1)^2$ — all
  three residue classes $x$ are solvable (likewise $C3_B$), and
  $\tilde E_A,\tilde E_B$ are singular mod 3 ($T=(0,0)$ is the singular
  point). Brute re-verification over $p\le300$
  (`mss_k34_sieve2_p2/p5.py`) gives killing primes **A: $\{5,11,13\}$**,
  **B: $\{5,19,29\}$** exactly. The standing divisibility consequence
  $3\cdot5\cdot11\cdot13\mid ab(a^2-b^2)$ survives unchanged because the
  factor 3 is automatic mod 3 ($a^2\equiv b^2\equiv1$ whenever $3\nmid ab$),
  but 3 carries no sieve content. (Append-only note; the Section 7 summary
  text above is left as filed.)
- Floor classes (degenerate rational points) for the sieve, $t=0$ coset:
  A: $\{0, \pm2, -1\}$ ($O$; $\pm2G_A$ map to the point at infinity,
  $X=\infty$; $-G_A$ has $X=1$); B: $\{0, \pm2, 1\}$ ($X(G_B)=1$; the class
  $-1$ has $X(-G_B)=\tfrac5{41}$, a non-square, so it is **not** protected
  for B).

### 2. Sibling covers D_A and D_B (lever 2: settled, sieve-equivalent)

- $D_A:\ w^2=z^4+128z^2-512$ (`p1.py`): invariants $I_1=10240,\
  I_2=-8912896$ match $M_A$; $f_D(x+\tfrac1x)\,x^4 \equiv$ the $C3_A$ octic
  (symbolic identity); with $z^2=u^2+4$ it becomes $u^4+136u^2+16$; the
  parametrization $z=(r^2+4)/(2r)$ ($r=2x$) realizes the correspondence.
  Known points $(2,\pm4)$ correspond to $M_A(1,\pm1)$, image classes
  $-G_A$ and $-G_A+T_A$. **K34-A $\iff$ $D_A(\mathbb{Q})$ point with
  $z^2-4$ a nonzero rational square** (verified symbolically).
- $D_B:\ w^2=9z^4-128z^2+512$ (`p6.py`): invariants $I_1=71680,\
  I_2=-38273024$ match $M_B$; $f_B(x+\tfrac1x)x^4=$ the $C3_B$ octic; with
  $z^2=u^2+4$: $9u^4-56u^2+144$; known point $(2,\pm12)$.
  **K34-B $\iff$ $D_B(\mathbb{Q})$ point with $z^2-4$ a nonzero rational
  square.**
- **Sieve equivalence (honest outcome of lever 2):** all three quotients of
  $C3$ ($M$, $D$, $D'$) impose the *same* local condition — the image of
  $C3(\mathbb{F}_p)$ — so $D_A,D_B$ add **no sieve power**; their value is
  the cleaner square-condition formulation ($z^2-4=\square$ instead of
  "$X$ square") plus the descent lever below.
- **Twist subtlety (tracked, general lesson):** the tangent-method cubic
  for $D_A$ is a *nontrivial twist* of $E_A$ (matching $a_2/a_4$ forces
  $\sigma^2=1/16$ but the $a_6$ equation fails) — $j$-only validation is
  insufficient when claiming an explicit isomorphism (the trap p11 hit).
- **Factorization descent lever (open):** $(R-W)(R+W)=4608a^4b^4$ with
  $R=a^4+66a^2b^2+b^4$ and bounded $\gcd$ — a potential Fermat-style
  descent on K34-A; not developed this round.

### 2b. Flip rule made exact; pole subtlety resolved

The flip $V\mapsto-V$ acts as $P\mapsto C-P$ ($C_A=-2G_A+T_A$,
$C_B=2G_B+T_B$), i.e. $\mathrm{flip}_A(n,t)=(-2-n,\,1-t)$,
$\mathrm{flip}_B(n,t)=(2-n,\,1-t)$ — **exact** on rational points, and
$X\circ\mathrm{flip}=X$ (only $V$ changes sign). The round-1 "failures" of
the mod-p flip check happen exactly when the reduced point sits on a pole
of $X$ (a 0/0 evaluation); they are artifacts, not counterexamples.

### 3. Deepened MW sieve on $\tilde E_A$ (t=0; t=1 by exact flip)

Engine (`p2/p3.py`): killing primes $\{5,11,13\}$, then
- *grow*: ordinary primes $\le400$ ordered by $|OK|/\mathrm{ord}_p(G)$,
  merged while expected count $\le3\cdot10^5$;
- *hunt*: modulus-neutral kills — primes $p$ with
  $\mathrm{ord}_p(G)\mid M$ (found by BSGS order + factor support check,
  $p\le3\cdot10^5$) shrink the count by $|OK|/\mathrm{ord}\approx\tfrac12$
  at zero modulus cost.

**Result:** 23 modulus-neutral hunt primes ($p\le3\cdot10^5$) on top of the
grow phase (all shrinking ordinary primes $\le400$) give

$$M_A=42{,}078{,}090{,}600 = 2^3\cdot3^4\cdot5^2\cdot7\cdot13\cdot17\cdot23\cdot73,$$

with **5 survivor classes** $S=\{0,\ 2,\ \tfrac{M}2-1,\ -2,\ -1\}$, density
$1.19\cdot10^{-10}$ (round 1: $3\cdot10^{-5}$, modulus
$5.3\cdot10^{11}$, stopped at $p=389$). Four survivors are exactly the
floor classes containing the degenerate points $O,\ 2G_A,\ -2G_A,\ -G_A$;
the fifth, $c=\tfrac{M}2-1$ (i.e. $n\equiv-1$ mod the odd part of $M$, and
$n\equiv3 \bmod 8$), is a **genuine non-degenerate survivor** — no known
point lives in it, and the hunt to $p\le3\cdot10^6$ had not killed it at
filing time (hunt still extensible). The $t=1$ coset by flip is
$\{0,-1,-2,-4,-\tfrac{M}2-1\}$; note class $-4$ ($t=1$) contains the actual
point $-4G_A+T_A$ with $X=\tfrac{1151}{66}$, a non-square, so it is **not**
protected — it survives only through the pole escape at mod-$p$ precision
(see 2c).

**Honest status.** This is a congruence theorem, not a proof of K34-A:
conditional on the (proved) structure
$E_A(\mathbb{Q})=\langle G_A\rangle\oplus\langle T_A\rangle$ and on sieve
exhaustiveness up to the stated prime bounds, **any K34-A counterexample
point $nG_A+tT_A$ has $n$ in the listed classes mod $M_A$**. Degenerate
points protect their classes at mod-$p$ precision forever, so a pure
mod-$p$ sieve can never terminate; a proof needs the refinement below.

### 2c. NEW VERIFIED LEVER: p-adic refinement kills pole classes

$X=2(y+66x)/(x(x-4))$ is a rational function on $\tilde E_A$; at the point
$(4,-264)=2G_A$ (reduction of every $n\equiv2 \bmod 10$ point mod 13) both
numerator and denominator vanish, but the ratio extends **regularly** with
value $\tfrac{1151}{66}$ (local computation: $x=4+\varepsilon,\
y=-264-\tfrac{1027}{33}\varepsilon+\cdots$ gives $y+66x\sim\tfrac{1151}{33}\varepsilon$).
Hence **every** rational point $nG_A$ with $n\equiv2\pmod{10}$ satisfies

$$X(nG_A)\ \equiv\ \tfrac{1151}{66}\ \equiv\ 7 \pmod{13},$$

and 7 is a **nonresidue** mod 13 (QRs: $\{0,1,3,4,9,10,12\}$). Verified in
exact arithmetic: $X(12G_A),X(22G_A),X(32G_A),X(42G_A),X(52G_A)\equiv7
\pmod{13}$ (units mod 169: 85, 150, 46, 111, 7). Therefore the whole
survivor class $n\equiv2\pmod{10}$ — including $n=2$ itself (point at
infinity, $X=\infty$) — is **dead as a K34-A candidate**: the class was
protected only by the 0/0 pole at mod-$p$ precision. Same kill available at
$p=17$ ($\tfrac{1151}{66}\equiv11$, nonresidue). For the other pole branch
($n\equiv-2$, point $(4,264)$) the numerator does not vanish mod 13, so
square-X forces $v_{13}(x(nG_A)-4)$ **even**; generically
$\mathrm{ord}_{13}(G)\mid M$ makes $x\equiv4$ and the first-order term
gives $v_{13}(x-4)=1+v_{13}(k)$ for members $n=-2+kM$, so the class
refines to $n\equiv-2 \pmod{10\cdot13}$ (members with odd valuation die),
and iterating drives the class $p$-adically onto the exact point $-2G_A$.

**Endgame now concrete (open).** A rational point has $x=4$ *only* at
$\pm2G_A$ (rank 1), so every non-degenerate member of a pole class has
$x(nG_A)-4\ne0$. Iterating the refinement over all primes kills a member
as soon as any $p\mid(x-4)$ has odd valuation or any resolved unit value is
a nonresidue. If the refined sieve drives every class onto the exact
degenerate points $n\in\{0,\pm1,\pm2\}$ (and their $t=1$ partners), whose
$X$-values are $0,1,\infty$ — never a positive square $\ne0,1$ — **K34-A
follows**. Carrying out this collapse is the named next-round gate,
alongside the Chabauty gate of Section 8. Not yet done: the refinement is
verified at $p=13$ (and structurally at 17); the full iteration +
termination argument is open. `[to-verify]`

### 2d. Refinement round: the congruence endgame is IMPOSSIBLE; coset
reduction + primitive-divisor gate (2026-09-02, `[mss-k34-refine]`)

Claude round, all computations exact (`mss_k34_refine1.py`/`.log`). Three
findings that reshape gate 2c.

**(1) Exact ord-3/ord-4 primes.** $3G_A=(\tfrac{156800}{961},\cdot)$,
$4G_A=(\tfrac{1324801}{1089},\cdot)$: $\mathrm{denom}(x(3G_A))=961=31^2$,
$\mathrm{denom}(x(4G_A))=1089=3^2\cdot11^2$. Since
$\mathrm{ord}_p(G)=3\iff p\mid 961$ and $=4\iff p\mid 1089$ (ord 1, 2
impossible: $x(G),x(2G)$ have unit denominators), the *only* primes that
could reduce classes $-1$, $M/2-1$ ($g=\gcd(c-2,M_A)=3$) or $-2$
($g=4$) onto the 0/0 pole $2G_A$ are $p=31$ (ord 3) and $p=11$ (ord 4).
At $p=31$ the constant $\tfrac{1151}{66}$ is a **residue** $\Rightarrow$
classes $-1$, $M/2-1$ survive the pole lever. At $p=11$,
$v_{11}(\tfrac{1151}{66})=-1$ (odd) $\Rightarrow$ class $-2$ members at
kernel depth 1 die, but deeper members face only parity/unit conditions.

**(2) STRUCTURAL: the congruence endgame of 2c cannot terminate.** The 0/0
points of $X$ (numerator $2(y+66x)$ and denominator $x(x-4)$ both
vanishing with unit constant) are exactly $2G_A=(4,-264)$ (constant
$\tfrac{1151}{66}$) — and no other. At $-2G_A=(4,264)$ the numerator is
$528=48\cdot 11\neq0$: genuine pole, so squareness forces only
$v_p(\varepsilon)$ parity (with $\varepsilon=x(nG)-4\sim-528\,t(kH)$,
$v_p(\varepsilon)=v_p(k)+s_p$, $s_p$ = kernel depth of $H$) — a condition
the free integer $k$ can always satisfy. At $-G_A$, $X=1$ is a regular
value: $X(nG)\equiv1\pmod p$ for every odd valid prime — no kill exists.
At $O$, $X\to0$ (a square) and the leading term $-2\,t(kH)$ varies freely
with $k$. Since local conditions at distinct primes are CRT-independent,
**no finite (or infinite) congruence refinement kills the classes**
$-2,-1,M/2-1,0$: the 2c collapse onto degenerate points is impossible as
stated. The verified part of 2c (class $2$ dead at $p=13$, and also at
$p=11$ via the odd valuation) stands unchanged.

**(3) Sharp reduction + new gate.** What survives is exact: every
non-degenerate K34-A candidate lies in one of four $k$-cosets of the
cyclic group generated by $H_A=M_A\cdot G_A$:
$$kH_A,\quad -G_A+kH_A,\quad -2G_A+kH_A,\quad (\tfrac{M_A}2-1)G_A+kH_A
\qquad(k\in\mathbb Z,\ k\neq\text{degenerate values}),$$
with $X\equiv1$ at all odd valid primes for the middle two classes and
$X\equiv-2\,t(kH_A)$ for the first. (The $t=1$ coset adds nothing: the
flip $P\mapsto C_A-P$ preserves $X$ exactly, so both cosets carry the
same $X$-values.) **New named gate (primitive-divisor route):** prove
K34-A by showing each coset point $P=cG_A+kH_A$ has a *primitive* prime
divisor $q$ of its EDS denominator (Ingram: primitive divisors exist for
all sufficiently large indices, exceptions listable) with
$\mathrm{ord}_q(G)=\text{index}\Rightarrow q\equiv1\pmod{\text{index}}
\Rightarrow q\nmid\text{index}\Rightarrow$ kernel depth $1$, whence
$v_q(x)=-2$, $v_q(y)=-3$, $v_q(x(x-4))=-4$ and — pending the
**numerator-cancellation lemma** ($y+66x$ has exact valuation $-3$ at
primitive $q$; the curve $y=-66x$ has no rational point, so cancellation
can only come from a finite set of exceptional primes to be enumerated) —
$v_q(X(P))=1$ odd $\Rightarrow$ $X(P)$ is not a rational square. If both
lemmas hold, only the degenerate points $n\in\{0,\pm1,\pm2\}$ remain and
**K34-A follows**; the same argument ports to $C3_B$/K34-B with
$H_B=M_B\cdot G_B$. Status: route identified and reduced to two lemmas;
neither lemma proved. `[to-verify]`

### 4. B-side sieve (first sieving of $\tilde E_B$)

Model: $\tilde E_B:\ y^2=x^3+256x^2-2048x$ ($E_B$ shifted by 18),
$G=(-128,1536)$, $T=(0,0)$; inverse quartic
$X=(6y-92x)/(x(x-36))$ with poles $x\in\{0,36\}$. Verified exactly:
$X(G_B)=1$, $X(-G_B)=\tfrac5{41}$, $X(3G_B)=\tfrac{41}5$,
$X(4G_B)=\tfrac{414}{209}$, $2G_B=(36,-552)$ (pole) — consistent with the
Section 2 image table. Killing primes $\{5,19,29\}$ ($p=3$ vacuous).
Sieve result (`p5/p9.py`): **5 classes mod $M_B=264=2^3\cdot3\cdot11$:**
$\{0,1,2,-2,\ \tfrac{M}2+2\}$, density $1.9\cdot10^{-2}$ — much weaker than
A because $\mathrm{ord}_p(G_B)$ is rarely $M_B$-smooth (only 4 hunt primes
$\le10^5$). Floor $\{0,1,2,-2\}$ all contain degenerate points. The
grow+hunt continuation (to $p\le2\cdot10^6$) was still running at filing
time — final B numbers `[to-verify]` in `mss_k34_sieve2_stateB.json`.
Note B's mod-8 ambiguity mirrors A: the extra class is "class 2 with
twisted 2-part" ($\equiv6 \bmod 8$).

### 5. Tracked failures (append-only)

- **F11 (composite-prime sieve bug).** The round-2 phase-1 loop iterated
  `range(7,400,2)`, including odd composites (39, 57, ...): the "group law"
  over composite moduli is invalid and illegitimately killed the protected
  classes 2, 58, 59, leaving the invalid state $M=60, S=\{0\}$
  (`mss_k34_sieve2_stateA.json`, discarded and regenerated). Fix: explicit
  prime sieving; lesson — assert primality inside sieve loops.
- **F12 (pole 0/0 masquerading as flip failure).** The mod-p flip check
  fails exactly at pole classes; resolved via the regular-extension
  refinement (2c). A related self-correction this round: briefly concluding
  "$X(2G)=\tfrac{1151}{66}$ makes $2G$ a finite $M_A$-point" — false;
  $2G_A$ is the image of the point at infinity, and $\tfrac{1151}{66}$ is
  the holomorphic extension value of the *function* $X$, which is exactly
  what the refinement exploits.
- **F13 (Fraction `%` misuse).** `Fraction % p` is rational remainder, not
  modular reduction; using it for "residues of exact rational points" gave
  garbage valuations before being caught by cross-checking against the
  mod-$p$ group law. Lesson: reduce via `num * den^{-1} mod p` with
  separately tracked valuations.

### 6. Claude verification record (2026-09-01, `[mss-k34-sieve2-verify]`)

Independent re-verification of Sections 1–4 by deterministic re-runs of the
agent's own drivers plus fresh stress tests (`mss_k34_sieve2_claude_check2.py`,
`mss_k34_sieve2_b_check.py`, `mss_k34_sieve2_b_stress.py`; logs alongside).

**A-side — CONFIRMED.** (i) Driver `p3` re-run from scratch reproduces the
state exactly: killing primes $\{5,11,13\}$ → 33 classes mod 60; grow →
291 610 classes mod $M_A=42\,078\,090\,600$; hunt (23 kills) → **5 classes**
$\{0,\,2,\,M_A/2-1,\,-2,\,-1\}$; `stateA.json` rewritten identically.
(ii) Stress vs all good primes $p\le3\cdot10^5$ with
$\mathrm{ord}_p(G)\mid M_A$ (624 primes): **zero violations**. Extension
$3\cdot10^5$–$10^6$ (231 more valid primes): **zero violations** — the
"hunt to $3\cdot10^6$ does not kill class $M_A/2-1$" claim is confirmed at
the $10^6$ level. (iii) The 2c lever verified
exactly: $X(nG_A)\equiv 7\pmod{13}$ for every $n\equiv2\bmod10$ tested
(n up to 192), and $X(12,22,32,42,52\,G_A)\bmod169 = 85,150,46,111,7$;
extension value $1151/66$ confirmed via the local expansion
$y'(4,-264)=-1027/33$. (iv) Two of my own initial "discrepancies" were
semantic, not agent errors — both instructive: the grow cap counts
*expected survivors* $|S|\,|OK|/\gcd(M,N)$, not lifts; and the class-level
condition is well-defined only when $\mathrm{ord}_p(G)\mid M$ (my unfiltered
stress produced a spurious violation at $p=23$, since $\#$Ẽ$_A(\mathbb F_{23})=32$
and $M_A$ carries only $2^3$). Recorded here so future rounds don't repeat them.

**B-side — CONFIRMED, `[to-verify]` lifted for the $t=0$ state.** (i) Exact
$X_B$ identities re-derived independently: $X(G_B)=1$, $X(-G_B)=\tfrac5{41}$,
$X(3G_B)=\tfrac{41}5$, $X(4G_B)=\tfrac{414}{209}$, $2G_B=(36,-552)$ (pole) —
all match the Section 2 image table. (ii) Killing primes re-derived from the
$C3_B$ octic: $\{5,19,29\}$; $p=3$ vacuous (all 3 classes solvable mod 3).
(iii) Driver `p5` re-run from scratch: kill → 66 classes mod
$\mathrm{lcm}(6,8,22)=264$; grow → 29; hunt kills at
$p=1097,1571,5297,9769,93407$ → **5 classes mod 264**:
$\{0,1,2,134,262\}=\{0,1,2,-2,M/2+2\}$, density $1.894\cdot10^{-2}$ — exact
match to `stateB.json`. (iv) Stress vs valid primes ($\mathrm{ord}\mid264$,
$p\le2\cdot10^5$, 33 primes): **zero violations**. Floor claim confirmed:
$\{0,1,2,-2\}$ all contain degenerate points; $-1$ dies ($X(-G)=5/41\equiv8$
mod 19, a nonresidue). One text correction: "only 4 hunt primes $\le10^5$"
should read **5** (1097, 1571, 5297, 9769, 93407). The $p9$ continuation
(grow to 3000, hunt to $2\cdot10^6$) found no further kills — consistent
with the filed state.

### 2e. The cancellation lemma is PROVED; K34-A reduced to odd-depth primitive divisors (2026-09-02, `[mss-k34-refine2]`)

Of the two lemmas opening the primitive-divisor gate in 2d, **Lemma 2 (no
cancellation) is now proved outright** — it needs no exceptions, no
resultant, no enumeration. Script `mss_k34_refine2.py` (+ log).

**Lemma 2 (valuation formula — PROVED).** Let $q\ge5$ be a good prime and
$P=nG_A$ a kernel point at $q$ of depth $s\ge1$ (i.e.
$v_q(\mathrm{denom}\,x_P)=2s$). Write $x_P=\varphi/\psi^2$,
$y_P=\varphi_3/\psi^3$ in lowest terms; the standard integrality lemma gives
$\gcd(\varphi_3,\psi)=\gcd(\varphi,\psi)=1$, so $v_q(\varphi_3)=v_q(\varphi)=0$.
Then, with $X=2(y+66x)/(x(x-4))$:
- $y+66x=(\varphi_3+66\varphi\psi)/\psi^3$: the second term has valuation
  $\ge s\ge1>-3s=v(\varphi_3)$, so **no cancellation is possible**;
  $v_q(y_P+66x_P)=-3s$ exactly.
- $x-4=(\varphi-4\psi^2)/\psi^2$: $\varphi-4\psi^2\equiv\varphi\not\equiv0$,
  so $v_q(x_P-4)=-2s$ exactly.
- Hence $v_q(X(P))=-3s-(-4s)=\boxed{+s}$ **unconditionally** — the $0/0$
  exceptional points of $X$ (pole points $(4,\pm264)$, zero $T=(0,0)$) can
  never coincide with a kernel point (a depth-$s$ point reduces to $O$; the
  exceptional points are affine). Verified exactly: 256 kernel-prime cases
  ($n\le60$, all good $q\le4000$ with $\mathrm{ord}_q(G)\mid n$), **0
  failures** (`mss_k34_refine2.log`).

**Consequence — square condition.** $X(nG_A)=w^2$ forces $s_q$ **even** for
*every* kernel prime $q$ of $nG_A$ (every good $q$ with $\mathrm{ord}_q(G)\mid n$).
So any kernel prime of odd depth kills the point.

**Lemma 1 refined to the exact remaining gap.** By Ingram's primitive-divisor
theorem (primitive divisors of $\psi_n$ exist for $n\ge13$; all coset indices
$n=c+kM_A\ge M_A-2\approx4.2\cdot10^{10}$ qualify), take $q$ primitive for
$\psi_n$: $\mathrm{ord}_q(G)=n$, and $q\nmid n$ (if $q\mid n$ with $q\ge5$
prime then $n=qj\ge2q$, but $\mathrm{ord}_q(G)=n\le\#Ẽ(\mathbb F_q)\le q+1+2\sqrt q$
gives $q\le1+2\sqrt q$, i.e. $n\le11$ — impossible for
$n\ge M_A-2$; and $n$ is composite so $q\ne n$). The depth of $nG$ at $q$
is then $v_q(\psi_n)=1+\delta_q$ where $\delta_q\ge0$ is the **elliptic
Wieferich defect** ($q^2\mid\psi_n\iff\delta_q\ge1$). So:

> **K34-A reduces to:** for every coset index $n$ ($n\equiv c\bmod M_A$,
> $c\in\{0,2,M_A/2-1,-2,-1\}$), some primitive divisor $q$ of $\psi_n$ has
> $v_q(\psi_n)$ **odd** (equivalently: not every primitive divisor of
> $\psi_n$ is an odd-Wieferich prime, i.e. $v_q(\psi_n)\in\{2,4,\dots\}$).

That is the *exact* residue of the problem: ruling out "all primitive
divisors have even depth" unconditionally would require a non-Wieferich
bound for elliptic divisibility sequences — the direct analogue of the
Wall–Sun–Sun obstruction for Lucas sequences. Silverman's conditional-on-abc
result (Wieferich primes for fixed $(E,P)$ are sparse) suggests the condition
holds with heuristic probability $\to1$, but unconditionally this is open.
`[to-verify]` exact statement + hypotheses of Ingram's theorem (does
$n\ge13$ hold for all nonsingular $E/\mathbb Q$, infinite-order $G$, or are
there curve-dependent exceptions?).

**Empirical evidence for the gate (this round).** Depth census
$s_q=v_q(\psi_{\mathrm{ord}_q})$ over all good $q\le4000$ with
$\mathrm{ord}_q(G)\le60$: **78/78 primes have depth exactly 1** — depth
histogram $\{1:78\}$, **zero odd-Wieferich primes found** for $(Ẽ_A,G_A)$.
Consistent with the gate being satisfiable.

**Port to K34-B (Lemma 2 only).** Same argument with
$X_B=(6y-92x)/(x(x-36))$: $6y-92x=(6\varphi_3-92\varphi\psi)/\psi^3$ has
valuation $-3s$ at any kernel point for $q\ge5$ ($v(6\varphi_3)=0$,
second term $\ge s$); $x-36=(\varphi-36\psi^2)/\psi^2$ gives $-2s$; so
$v_q(X_B(P))=+s$ and the identical reduction holds for the four $k$-cosets
of $\langle H_B\rangle$ ($n\equiv c\bmod M_B$, $M_B=264$). **Lemma 2 is
fully ported; Lemma 1 (odd-depth primitive divisors) is the shared gap.**

### §2f Depth census via a Shipsey EDS engine; the class-0 constraint; first odd-Wieferich primes `[mss-k34-refine3]` (2026-09-02)

**The depth-decomposition theorem.** *Proof (no LTE needed — pure formal
group).* Let $q\ge5$ be a good prime, $Q=d\,G\in E_1(\mathbb{Q}_q)$ a kernel
point of base depth $b_d=v_q(\psi_d(x_G))\ge1$ (so $Q\in E_b\setminus E_{b+1}$
under the depth filtration). Multiplication-by-$m$ on the formal group
satisfies $t(mQ)=m\,t(Q)+O(t^2)$ where $t$ is the local parameter, so
$v_q(t(mQ))=v_q(m)+b$ for every $m\ge1$: the map $Q\mapsto mQ$ sends depth
$s$ to $s+v_q(m)$ exactly. Hence for $P=nG$ with $d=\mathrm{ord}_q(G)\mid n$:
$$\mathrm{depth}_q(nG)\;=\;b_d+v_q(n/d).$$
**The class-0 constraint theorem.** For the coset $n=kM_A$ ($c=0$), every
valid prime $p$ (i.e. $\mathrm{ord}_p(G_A)=d\mid M_A$) is a kernel prime of
$kH_A$, and $X(kH_A)=w^2$ forces $b_p+v_p(k)+v_p(M_A)-v_p(d)\equiv0\pmod2$.
Since typically $p\nmid\#E(\mathbb{F}_p)$ (so $v_p(d)=0$) and $p\nmid M_A$:
$v_p(k)\equiv b_p\pmod2$ — **$k$ must absorb every valid prime with odd base
depth**. Define $R_0=\prod\{p\text{ valid}:b_p\text{ odd},\ p\nmid M_A\}$;
then $k=R_0k'$. (For $c\in\{2,-1,-2,M_A/2-1\}$ no valid prime is a kernel
prime of the coset point, so this constraint is exclusive to class 0.)

**The engine.** Shipsey-style elliptic-divisible-sequence recurrence
$W_{m+n}W_{m-n}=W_{m+1}W_{m-1}W_n^2-W_{n+1}W_{n-1}W_m^2$ ($W_n=\psi_n(x_G)$,
$W_1=1$, $W_2=2y_G$), maintained as a 7-window $(W_{n-3}..W_{n+3})$ over the
binary expansion of $N$: doubling divides only by $W_2=2y_G$ (a power of
2 — invertible at $p\ge5$), the add step divides by $W_n$ with
valuation-tracked arithmetic mod $p^{8}$. Computes $v_p(W_N)$ in $O(\log N)$
steps — **first time these depths are computable for large indices**
(`scripts/mss_k34_refine3.py`, validated 378/378 against exact $W_n$ on both
curves).

**Census results (all good primes $q\le20000$, 2260 primes per curve).**
- $(Ẽ_A,G_A)$: depth histogram $\{1:2259,\ 2:1\}$ — **first odd-Wieferich
  prime: $q=167$, $\mathrm{ord}_{167}(G_A)=84$, $v_{167}(\psi_{84})=2$**.
- $(Ẽ_B,G_B)$: histogram $\{1:2257,\ 2:3\}$ — odd-Wieferich primes
  $q=13$ (ord 18), $q=419$ (ord 200), $q=2351$ (ord 610), all depth 2.
- Rate check: heuristic $\sum_{q\le B}1/q\approx2.5$ expected odd-Wieferich
  primes per curve; observed 1 (A) and 3 (B) — consistent with Poisson.
  Higher-depth ($\ge3$) defects: none found.

**What this means for the gate.** Odd-Wieferich primes exist for both curves
— depth 1 is *not* universal, so a naive "every primitive divisor has odd
depth" lemma is false as stated. But they are rare (~0.1%), and the gate only
requires *some* primitive divisor of each $\psi_n$ to have odd depth —
ruling out "all primitive divisors odd-Wieferich" remains a
Wall–Sun–Sun-type gap (Silverman's abc-conditional sparsity supports it).
The census is the measured base-rate evidence that the gate is satisfiable.

**Valid-prime census** (`scripts/mss_k34_refine3_valid.py`, saved to
`validA_primes.json` / `validB_primes.json`): all valid primes
($\mathrm{ord}_p(G)\mid M_A$, resp. $\mid M_B$) with their base depths $b_p$
and the exact class-0 constraint $v_p(k)\equiv b_p+v_p(M_A)+v_p(d)\pmod2$;
$R_0$ computed from the odd-depth subset. **Results (35 min run):** curve A
has **640 valid primes $\le3e5$** with depth histogram $\{1:639,\,2:1\}$ —
the only even-depth valid prime is $p=167$ — so
$R_0=\prod_{\text{639 primes}}p$, $\log_{10}R_0=2712.0$ (lower bound: the
true $R_0$ over all valid primes is larger). Curve B has **34 valid primes
$\le2e5$, all depth 1** ($R_0^{(B)}$, $\log_{10}=103.2$). Class re-check
(`mss_k34_refine3_classcheck.py`): the five survivor classes hold on all 640
(A) and 34 (B) valid primes, 0 violations. **Append-only correction to
[mss-k34-sieve2]**: the W2 count "624 valid primes $\le3e5$" was an
undercount — its `bsgs_order` returned None for 16 primes (silently
skipped); complete order-finding (trial-division factorization of
$\#E(\mathbb{F}_p)$) gives 640. Class conclusions unaffected (0 violations). `[to-verify→verified-with-caveat,
2026-09-02]` Primitive-divisor status: Ingram's rank-one $Z\le12$ ($n\ge13$)
is **conditional on Lang's height conjecture** (Ingram, *JNT* 123 (2007),
473–486); unconditional: Silverman 1988 gives $Z<\infty$ but *ineffective*;
**Verzobio 2023 (Pacific J. Math 325, 331–352) gives an explicitly
computable constant $C(E/K)$ beyond which every term has a primitive
divisor** — the right tool for the gate (compute $C$ for $(Ẽ_A,G_A)$,
$(Ẽ_B,G_B)$); Ingram–Silverman 2012 gives a uniform bound conditional on
abc. Sources: Verzobio arXiv:2001.02987 ($C$ depends only on the model —
computable for $(Ẽ_A,G_A)$, $(Ẽ_B,G_B)$: next-round task); Ingram
math/0409540; msp.org/pjm/2023/325-2/p07.

### §2g Class-0 descent: hypothetical solutions are forced past the effective primitive-divisor constant `[mss-k34-refine3]` (2026-09-02)

**Proposition (class-0 size forcing).** If $X(kH_A)=w^2$ for some $k\ge1$,
then for every valid prime $p$ the constraint of §2f fixes $v_p(k)\bmod2$,
so $k\ge R_0=\prod\{p\text{ valid}: b_p+v_p(M_A)+v_p(d)\equiv1\pmod2\}$ and
$$n=kM_A\ \ge\ R_0\,M_A .$$
With 640 valid primes $\le3e5$ and depth-1 the norm (§2f census: 2259/2260
primes odd depth), $\log_{10}R_0=2712.0$ from the census (a lower bound), so
$n\ge R_0M_A>10^{2721}\gg10^{42}$.

**Verzobio's constant for our curves (order of magnitude).** Equation 13 of
arXiv:2001.02987 with $K=\mathbb{Q}$ ($D=1$, $\Delta_K=1$), $h(j(Ẽ_A))\approx2.5$
($j\approx-12.6$), $\log|\Delta_{Ẽ_A}|\approx34.5$, $\sigma\approx2$:
the bottleneck is $C_2'=54\,c_1 D^6\log V_1'\log V_2'$ with $c_1=3.6\cdot10^{41}$
(David's elliptic-logarithm bound), giving $C(E_A)\approx10^{39}$–$10^{42}$
**[to-verify: recompute exactly]** — either way $\gg M_A=4.2\cdot10^{10}$ but
$\ll R_0M_A$.

**Consequence — the two coset families split.**
- **Class 0** ($n=kM_A$): any hypothetical solution has
  $n\ge R_0M_A>C(E_A)$, so $\psi_n$ **provably has a primitive divisor**
  (Verzobio, unconditional and effective). The class-0 gate reduces to pure
  depth: *some primitive divisor of $\psi_{kM_A}$ has $v_q(\psi_{kM_A})$
  odd* — an odd-Wieferich question about specific enormous terms, no
  existence gap.
- **Nonzero cosets** ($n\equiv\pm1,\pm2,M_A/2-1$): $n$ ranges over
  $[M_A-2,\,C(E_A)]\approx[4.2\cdot10^{10},\,10^{40}]$ with no effective
  primitive-divisor guarantee — this finite but astronomically large window
  is the honest remaining existence gap, bridgeable conditionally via
  Lang's conjecture (Ingram's $n\ge13$) or abc (Silverman's odd-Wieferich
  sparsity).

**Sharper statement of the total remaining gap (K34-A).** (i) effective
primitive divisors for the nonzero-coset window; (ii) odd depth of some
primitive divisor for all cosets. Both are Wall–Sun–Sun-type; (i) has a
conditional resolution (Lang/abc), (ii) is supported by the §2f census base
rate (odd-Wieferich rate $\sim0.1\%$).

## Cross-problem links



- Engine: `scripts/mss_census_pythagorean.py` (validated 3 ways — see
  problem.md frontier block).
- [[square_of_cubes]] — cubic sibling: the open question "is there a
  D-set closed form for the cubic case?" is now ANSWERED (2026-09-01,
  `[cubic-dset-vanishes]`): the cubic D-set is provably **empty** —
  $w^3\pm d$ both cubes forces $x^3+y^3=2w^3$, whose only solutions are
  trivial ($x=y=z$, Euler descent in $\mathbb{Z}[\omega]$; brute-verified
  to 600). The MSS engine cannot transfer in principle, and the two
  problems are structurally disjoint (full-magic squares open with rich
  D-theory; full-magic cubes dead by mod 9, semi-magic cubes with
  4-dimensional linear freedom and no pair structure). **Sharper (same
  date):** the vacuous cubic D-set immediately re-derives Wroblewski's
  fully-magic impossibility (opposite pairs of a fully magic 3×3 sum to
  2·center ⟹ each pair satisfies $x^3+y^3=2c^3$ ⟹ all entries equal) —
  so the open/dead dichotomy between the siblings is EXACTLY the
  richness (squares: Pythagorean D-sets) vs vacuity (cubes: D=∅) of the
  two D-sets. Our problem is hard *because* its pair-completion
  condition has deep arithmetic structure.
- Methodology: simultaneous-Diophantine control step (problem.md) — per
  the corrected Lemma 3, $\ge7$-square configs need only TWO D-elements
  (no additive condition), so they are common enough to exist (Bremner);
  the control step for the FULL problem is the third and fourth pair
  completions — i.e. needing 4 D-elements whose pairwise additive
  combinations stay inside $D$ (or accidental squares). The rarity
  escalates sharply between 7 (exists) and 9 (unknown).
