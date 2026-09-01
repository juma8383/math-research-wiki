# Hodge Conjecture — notes / sparks

> Working scratchpad. Not a polished page; sparks for later attempts.

## 5-for-5 cross-problem methodology

The "obstruction at the control/reduction step, NOT the resolution step" lens
is now 5-for-5:

| Problem | Resolution step (works) | Control step (the obstruction) |
|---|---|---|
| Beal | Chabauty / effective Faltings / Mordell–Weil sieve | reduction-to-finite-curves (needs shared/even/spherical exp.) |
| BSD | descent, Tamagawa, regulator, Sha computation (all ranks) | Selmer-group control (Euler system is one-point-shaped, rank ≤1) |
| NS | local existence, conditional regularity, partial regularity | critical-norm control ($L^2$ subcritical cannot bound $L^3$ critical) |
| YM | lattice definition, reflection positivity, strong-coupling gap | continuum-limit convergence + uniform-in-$a$ IR gap transport |
| Hodge | Chow groups + cycle class map; exponential seq. for $p=1$ | analytic→algebraic conversion in codim $\ge2$ |

The common spine: each problem has a working "engine" that resolves a *slice*
of the question (one signature / one rank / one regime / one codimension), and
the obstruction is the **control** that stops the engine from reaching the rest.
Candidate reusable methodology — worth a standalone theory/method page once it
stabilizes across one more problem.

## Spark: the "one-dimensional engine stops" pattern

Beal (cubic coincidence), BSD (one-point Euler system), NS (2D Serrin equality
$3=3$), YM (one-scale asymptotic freedom), Hodge (Picard variety / exponential
sequence = one-dimensional analytic→algebraic object). In each case the working
tool is intrinsically *one-dimensional* / *one-scale* / *one-codimension*, and
the open content is the leap to higher dimension / rank / scale / codimension.
This is a sharper common thread than just "control step" — the engine's
*shape* (rank ≤1, codim 1, 2D, single RG scale) is what limits it. Possible
page: `method-one-dimensional-engine-limit`.

## Spark: analytic vs algebraic as the Hodge-specific unifying lens

Where Beal is spherical/hyperbolic, BSD is Euler-system shape, NS is
subcritical/critical scaling, YM is UV/IR RG — Hodge is **analytic vs
algebraic**. Hodge classes are defined analytically (Hodge theory / harmonic
forms); algebraic cycles are algebraic. GAGA + Lefschetz $(1,1)$ is the bridge
that works for divisors; the conjecture asserts it works for all codimensions.
This is the Hodge-specific instance of the cross-problem "control over the
conversion" theme.

## Spark: integral vs rational (the torsion wrinkle)

The integral Hodge conjecture is *false* (Atiyah–Hirzebruch, Kollár). Unlike
the other four problems, Hodge has a built-in "the naive strong statement is
false" — the $\mathbb Z$-version fails, only $\mathbb Q$ works. Analog: Beal
has no such wrinkle; BSD's refined-coefficient is the closest (the exact order
of Sha, an arithmetic refinement). Worth tracking whether the torsion
obstruction is a *separate* obstruction from the analytic→algebraic one or a
symptom of it.

## Spark: the motive reduction as "reduction to finite/specific classes"

The standard conjectures reduce the *full* HC to the algebraicity of a few
*specific* Hodge classes (Künneth components, inverse Lefschetz). This is the
Hodge analog of Beal's "reduce to finitely many curves" — a reduction from
the universal statement to a finite/specific set. And like Beal, that
reduction is itself open (B, C not known in general; known only for surfaces,
abelian, hyper-Kähler). The "reduction step is the obstruction" pattern
recurs one level down.

## Spark: generalized Hodge conjecture and coniveau

Grothendieck's GHC (coniveau $r$) is a finer statement: Hodge substructures of
coniveau $\ge r$ come from cohomology supported on codim-$\ge r$ algebraic
subsets. Usual HC = GHC at $k=2r$. Hodge's original stronger conjecture was
*false* (Grothendieck). The GHC is the "right" generalization — and it is
mostly open beyond the coniveau-1 case (which reduces to Lefschetz $(1,1)$ via
weak Lefschetz / blow-ups). Another instance of "the clean codim-1 / coniveau-1
case works; the rest is open." [[conj-generalized-hodge]]

## Spark: is there a Hodge-side "counting / sparsity" angle?

Beal developed a counting heuristic ($\sim H^{r\chi}$, monotone sparsity). Is
there an analogue for Hodge — a heuristic for "how many" Hodge classes are
algebraic, or a measure of the gap between $\mathrm{Hdg}^p$ and the algebraic
classes? Voisin's "no uniform bound on cycle complexity" result is a
*negative* such measure. Possibly a soft angle like Beal's thread 6*, but
Hodge theory gives less to count. Park for later.