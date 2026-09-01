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