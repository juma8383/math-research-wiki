# Brocard's Problem (Brown Numbers)

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/Brocard.htm.

## Statement
Find integer solutions $(n,m)$ to $n! + 1 = m^2$ (Brown numbers). Are there
finitely many, and which?

## Status
**OPEN.** Known solutions: $(n,m)=(4,5),(5,11),(7,71)$ — the three Brown
numbers, confirmed; conjectured no more.

## Frontier (one line)
*(2026-08-31 hunt-scan update; 2026-09-01 verification pass — figures
now `[summary]`-verified against Wikipedia/OEIS/arXiv pages.)*
**Search bounds (verified 2026-09-01):** Berndt–Galway $n\le10^9$ (2000,
Ramanujan J.); Tim Peters 2006: $n>4\cdot10^9$ (sieve vs primes
$>4\cdot10^9$); Matson 2015 (`unsolvedproblems.org` S73): $n>4\cdot
10^{11}$, extended in his 2017 *Unsolved Problems* publication; Wikipedia
(as of Oct 2022): **no further solutions with $n\le10^{15}$**
collectively (Berndt–Galway, Matson, Epstein–Glickman). **Kurz 2003
(CORRECTED 2026-09-01): a fourth solution has $m^2>10^{850}$** (OEIS
A085692: "greater than $10^{850}$ as the value of the square $m^2$")
⟹ $m>10^{425}$ — the earlier filing "$m>10^{850}$" overstated by the
squaring. **Overholt 1993 (Bull. LMS 25(2):104): abc ⟹ finitely many**
Brown numbers (Dąbrowski 1996 extends to $n!+A=m^2$) — confirmed;
the same load-bearing external conjecture as [[beals_conjecture]]'s
resolution layer. Maiti 2020 (arXiv:2004.09256, verified): for
$n\ge10^5$ a fourth solution needs the fractional part $\varepsilon$
of $\sqrt{n!}$ to exceed $0.\underbrace{9\cdots9}_{228287}$ — i.e.
$\sqrt{n!}$ within $\sim10^{-228288}$ of an integer from below — and
$\varepsilon$ is strictly monotone across solutions; **caution: the
same paper claims an unconditional finiteness/no-more-solutions proof —
not accepted by mainstream sources; the problem remains open**. Peixoto 2026 **verified to exist**
(arXiv:2606.23485, "The Brocard Problem: Structural Invariants, p-Adic
Density, and the Generative Sieve", Leandro Vieira Peixoto, submitted
22 Jun 2026 — confirmed against the arXiv abstract page 2026-09-01):
structural reformulation via primorial cycles + a claimed "Triangular
Equivalence" theorem (Brown number ⟺ $n!/8$ triangular) + a generative
p-adic sieve (LLL-reduction angle); non-peer-reviewed preprint, does not
claim to resolve the problem `[summary — abstract-verified, body unread]`.

## Structural lemmas (2026-09-01 attack block) `[brocard-structural]`

**Lemma B1 (triangular reformulation).** For $n\ge4$, $n!+1=m^2$ ⟺
$n!/8=T_{(m-1)/2}$ is a triangular number. *Proof:* $n\ge4$ ⟹
$3\le v_2(n!)$; $m^2=n!+1$ is odd so $m$ odd; $(m-1)(m+1)=n!$, and with
$m-1=2a$: $4a(a+1)=n!$, i.e. $a(a+1)/2=n!/8$ with $a=(m-1)/2$. ∎ (The
three Brown numbers: $24/8=3=T_2$, $120/8=15=T_5$, $5040/8=630=T_{35}$.)

**Lemma B2 (root-of-unity structure / sieve basis).** $m^2=n!+1$ gives
$m^2\equiv1\pmod{n!}$, so $m$ is a square root of unity mod $n!$: for
every odd prime $p\le n$, $m\equiv\pm1\pmod{p^{v_p(n!)}}$, and
$m\equiv\pm1$ or $\pm(1+2^{v_2(n!)-1})\pmod{2^{v_2(n!)}}$ — one of
$2^{\omega(n!)}$ CRT classes. Combined with $m\approx\sqrt{n!}\ll n!$:
**a fourth solution is a square root of unity mod $n!$ confined to the
narrow window above $\sqrt{n!}$** — the structural reason the
quadratic-residue sieve (primes $p>n$, where $n!\not\equiv0$) is the
natural engine (Matson's sieve), and the reason small primes give no
information ($n!\equiv0\pmod p$ for $p\le n$). **Novelty scan (2026-09-01, resolved).** Lemma B1 is **not novel as
stated**: Peixoto 2026 (arXiv:2606.23485) states the same equivalence as
its "Triangular Equivalence theorem" (verified against the arXiv abstract;
a search-summary attribution to a Kevin Brown MathPages article could not
be confirmed — candidate URLs 404 / wrong content, so any earlier
statement remains `[to-verify]`). Lemma B2: **no prior statement found**
in scan sources; the underlying facts are classical (count of square
roots of unity mod $n$ — Finch–Sebah arXiv:math/0604465; standard
CRT/Miller–Rabin material), so B2 as a sieve basis is likely elementary
folklore `[not found in scan sources]`. Both lemmas are here re-derived
independently; B2's *use* as a window sieve (below) appears to be the
new part.

**Independent sieve re-verification (`scripts/brocard_legendre_sieve.py`).**
Documented Legendre-symbol sieve over primes $p>N$: for each $p$,
$(n!+1\mid p)=-1$ excludes $n$; survivors exact-checked. Self-test at
$N=2\cdot10^5$ (12 primes): survivors halve per prime (99963 → 56) and
the exact hits are **exactly** the three known Brown numbers
$(4,5),(5,11),(7,71)$. Full run at $N=10^7$ (20 primes in
$(10^7,1.00004\cdot10^7]$, 2056 s): **12 survivors** (model expectation
$10^7/2^{20}\approx9.5$), exact hits **exactly** the three known Brown
numbers — **no fourth solution with $4<n\le10^7$** (log
`brocard_sieve_N10000000.log`; subsumed by Berndt–Galway's $10^9$ — filed
as an independent re-verification with documented code, the same honest
framing as the Buell/MSS re-verifications).

**Overholt's abc mechanism, explicit (approach 3; derived here,
mechanism due to Overholt 1993 `[to-verify vs primary]`).** For
$n!+1=m^2$ the abc triple is $(1,\ n!,\ m^2)$ (coprime: $\gcd(n!,\,m^2)=
\gcd(n!,\,n!+1)=1$), with
$$\operatorname{rad}(abc)=\operatorname{rad}(n!)\cdot\operatorname{rad}(m)
= e^{\theta(n)}\cdot\operatorname{rad}(m),$$
$\theta(n)\sim n$ (Chebyshev) and $\operatorname{rad}(m)\le m\approx
\sqrt{n!}$. The abc **quality**
$$q=\frac{\log m^2}{\log\operatorname{rad}(abc)}
\ \gtrsim\ \frac{n\log n}{\;n+\tfrac12 n\log n\;}\ \longrightarrow\ 2 .$$
Since abc asserts $c<K_\varepsilon\operatorname{rad}^{1+\varepsilon}$
(quality $\le 1+\varepsilon+o(1)$) and $q\to2$, any fixed $\varepsilon<1$
excludes all sufficiently large $n$ — this is Overholt's finiteness
theorem made quantitative; solving the displayed inequality gives the
effective (K$_\varepsilon$-dependent) bound $n\le N(\varepsilon)$, and
with the searches to $10^{15}$, **abc for any single fixed $\varepsilon$
would reduce the conjecture to a finite check** (Dąbrowski 1996 extends
the framework to $n!+A=m^2$). The known solutions' qualities (computed
directly, factorint): $n=4,5,7$ give $q\approx0.946/0.827/0.887$ — all
below $1$, comfortably abc-consistent. *(Self-caught correction: an
earlier version of this paragraph filed $q\approx1.26/1.32/1.35$ — those
figures were wrong, never recomputed. The asymptotic $q\to2$ statement is
unaffected.)* The drift of $q$ toward $2$ as $n$ grows is what pushes any
fourth solution out: at $n=7$, $\log\operatorname{rad}$ is already
dominated by $\tfrac12\log n!$, and the ratio only climbs from there.

**Root-of-unity window heuristic (Corollary to Lemma B2;
`scripts/brocard_rootofunity_heuristic.py`).** By B2 a solution $m$ is a
square root of unity mod $n!$; the number of such roots is exactly
$R(n)=2^{\pi(n)+1}$ for $n\ge4$ (two per odd prime power, four for the
2-part since $v_2(n!)\ge3$ — verified by direct enumeration, $n\le12$).
Since $m^2=n!+1$, $m$ must lie in the window
$(\sqrt{n!},\,2\sqrt{n!}]$ of relative width $\sim n^{-n/2}$. If roots of
unity mod $n!$ are equidistributed in $[0,n!)$, the expected number in the
window is
$$E(n)=2^{\pi(n)+1}\frac{\sqrt{n!}}{n!},\qquad
\log_{10}E(n)=-71.2\ (n=100),\ -1232.9\ (n=1000).$$
Exact enumeration agrees: window hits at $n=4,5,7$ are exactly the known
$m$ values ($5,11,71$; plus non-solutions $7,19$ occupying the same
window — window occupancy is necessary, not sufficient), $E(4)\approx1.63,
E(5)\approx1.46$ then $E(6)\approx0.60,\ E(7)\approx0.45$, decaying
superexponentially. **This is the abc-independent heuristic: a fourth
Brown number is a root of unity mod $n!$ that lands in a window of
relative width $1/\sqrt{n!}$, an event of expected count
$2^{\pi(n)+1}/\sqrt{n!}\to0$** — the structural reason the Legendre sieve
halves the survivor set per prime, and consistent with the sieve's
observed halving ($5{,}002{,}216\to12$ over 20 primes).

### Exact root-of-unity window verification through $n=60$
(`scripts/brocard_rootofunity_exact.py`, log `brocard_rootofunity_exact.log`;
2026-09-01.) The window heuristic above is upgraded from equidistribution
model to an **exact enumeration**: all $R(n)=2^{\pi(n)+1}$ square roots of
unity mod $n!$ were enumerated by CRT (four 2-adic classes
$\{\pm1,\ \pm(1+2^{b-1})\}$ for $2^b\,\|\,n!$, two per odd prime power),
for every $4\le n\le 60$ — up to $R(60)=2^{18}=262144$ roots ($\approx272$-bit
integers). Self-tests pass: (i) full brute-force agreement for $n\le10$
(all of $x^2\equiv1\bmod n!$ checked exhaustively); (ii) every enumerated
root verified $x^2\equiv1\bmod n!$ ($n\le14$ exhaustive, random sample of 64
above). Census result (exact arithmetic, total runtime 0.9 s): **the window
$(\operatorname{isqrt}(n!),\,2\operatorname{isqrt}(n!)]$ is occupied only at
$n=4$ (roots $5,7$), $n=5$ (roots $11,19$), $n=7$ (root $71$) — zero window
hits for every $6\le n\le 60$**, and the roots satisfying
$m^2=n!+1$ *exactly* are exactly $m=5,11,71$ (the three Brown numbers, each
exact-checked against `math.factorial`). No surprises at any $n\ge8$: the
clean equidistribution picture holds exactly through $n=60$, i.e. a fourth
Brown number is a root of unity mod $n!$ that must land in a window no root
of unity has occupied since $n=7$ in the exact census.

### More-general statement (Dabrowski family $n!+A=m^2$)
(`scripts/brocard_dabrowski_general.py`, log
`brocard_dabrowski_general.log`; brute force, exact big ints,
$2\le n\le200$, $|A|\le12$.) Lemma B2 generalizes verbatim: $m^2\equiv A$
mod $n!$ makes $m$ a **square root of $A$ mod $n!$** — a set that is empty
unless $A$ is a quadratic residue mod every prime power $p^a\|n!$ with
$p\nmid A$; in particular (i) $A\bmod 8\in\{0,1,4\}$ for $n\ge4$, and (ii)
$(A\mid p)=+1$ for every odd prime $p\le n$ with $p\nmid A$ (the script
verifies (ii) at every solution found). For **non-square $A$** condition
(ii) is a genuine Legendre sieve that eventually fails — in the computed
range it kills each non-square $A$ by $n\le11$ (e.g. $A=6$ dies at $p=7$,
$A=7$ at $p=11$, $A=10$ at $p=7$, $A=-4$ at $p=3$). For **square
$A=s^2$** the sieve is vacuous ($(s^2\mid p)=1$ always) and the equation
degenerates to the factorization $(m-s)(m+s)=n!$ — exactly the Lemma-B1
shape with a shifted square; the Dabrowski family thus splits into a
"Brown-type" square channel ($A=s^2$, incl. $A=1$) and non-square $A$
that are sieve-dead at a small prime. Computed solutions
($n\le200$; only these, none else in range):
$A=-8:(4,4)$; $A=-5:(3,1)$; $A=-2:(3,2)$; $A=-1:(2,1)$; $A=1:(4,5),(5,11),(7,71)$;
$A=2:(2,2)$; $A=3:(3,3)$; $A=7:(2,3)$; $A=9:(6,27)$; $A=10:(3,4)$; $A=12:(4,6)$.
Reading: for $n\ge5$ the only survivors are $A=1$ (the three Brown numbers)
and $A=9$ ($6!+9=729=27^2$, with $(27-3)(27+3)=24\cdot30$ — the same
$(m-s)(m+s)=n!$ shape, $s=3$); every $A\equiv2,3,5,6,7\bmod8$ is dead at
$n\ge4$ by the mod-8 condition (verified: zero solutions); the dual form
$A=-1$ ($n!-1=m^2$) has only the trivial $(2,1)$ — empty as expected.
Counterevidence angle checked: no non-square $A$ survives past $n=4$ in the
range, consistent with (and explained by) the Legendre sieve. (Dąbrowski
1996 established the abc-finiteness framework for this family; the
sieve/channel split above is the local-structure observation filed here.)

**Confidence re-evaluation (2026-09-01, protocol step 10).** After the
exact census: confidence that no fourth Brown number exists — high and
raised (window occupancy verified *exactly* empty for $6\le n\le60$ with
all self-tests passing, on top of searches to $10^{15}$ and the
superexponential heuristic). Confidence that the window/equidistribution
model is the right frame — raised (exact agreement at every $n$ through
60, including the two benign non-solution hits at $n=4,5$). The
control-step obstruction is unchanged: the window argument is a
heuristic-plus-exact-small-verification, not a proof for all $n$; the
provable route to finiteness remains abc-dependent (Overholt/Dąbrowski).

## Control-step framing (one line)
Resolution on a slice (verified no new solutions to large $n$) → control =
global finiteness/nonexistence; the obstruction is Diophantine — a linear-
form-in-logarithms / transcendence wall (echoes the [[collatz_conjecture]]
cycle-exclusion via linear forms in logs).

## See also
- [[collatz_conjecture]] — cycle exclusion via linear forms in logarithms is
  the shared Diophantine control tool.