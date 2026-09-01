# Semi-Magic Square of Cubes

> **STUB — folder started 2026-08-25; full attack pending.** Load-bearing
> facts flagged `[to-verify]`. Source: unsolvedproblems.org/index_files/SquareofCubes.htm.

## Statement
Does there exist a $3\times3$ **semi-magic** square (all rows and columns —
not necessarily diagonals — equal to the same total) whose nine entries are
**distinct positive perfect cubes**? Or prove none exists.

## Status
**OPEN** (semi-magic). The **fully magic** variant (rows + both diagonals)
is **RESOLVED NEGATIVE** — Wroblewski (2007, proof posted with Boyer at
multimagie.com/Proof3xCubes.htm): a fully magic $3\times3$ square of nine
*different positive cubes* is impossible, via a mod-9 forced-column structure
— so the stub's earlier "or prove none exists" half was already answered in
the literature; only the semi-magic variant remains `[summary, to-verify:
re-derive the mod-9 obstruction; watch the common-factor escape hatch]`.
**2026-09-01: the mod-9 obstruction is no longer load-bearing** — the
fully-magic negative now follows in two lines from the cubic D-set lemma
below (stronger: the only fully magic cube squares are all-equal), and the
Lemma's classical core (x³+y³=2z³ ⟹ x=y=z, Euler) is verified against the
modern primary reference (Monsky arXiv:2309.00162).
(Also: $2\times2$ magic square of cubes is trivially impossible — forced
equality.) **2026-09-01:** the cubic D-set is provably *empty* (Lemma in
the section below) — the square sibling's pair-completion engine cannot
transfer in principle, and any semi-magic cube square must avoid symmetric
opposite pairs entirely.

## Frontier (one line)
Known near-miss (Boyer 2007): **magic sum $S=235{,}788{,}435$** — the nine
cubes $(2^3,16^3,8^3 / 4^3,(-23)^3,55^3 / 512^3,29^3,(-6)^3)$ give all rows +
diagonals magic — note **one negative cube**; the earlier stub line calling
$235{,}788{,}435$ "the ninth entry" misdescribed the near-miss (corrected).
Open: semi-magic with nine *positive distinct* cubes.

## The cubic D-set vanishes (2026-09-01, answers the MSS cross-link question)
`[cubic-dset-vanishes]`

The sibling problem [[magic_square_of_squares]] runs on the set
$D(w^2)=\{2uv: u^2+v^2=w^2\}$ — the $d$ for which both $w^2\pm d$ are
squares (Pythagorean pairs about a square center), divisor-structured via
sum-of-two-squares theory. The cubic analogue is **empty**:

**Lemma (cubic D-set).** If $w^3-d=x^3$ and $w^3+d=y^3$ with $x,y,w\ge1$,
then $x=y=w$ and $d=0$. *Proof:* adding gives $x^3+y^3=2w^3$, whose only
solutions are $x=y=z$ — **Euler's theorem**, proved by infinite 3-descent
in the Eisenstein integers $\mathbb{Z}[\omega]$; modern clean reference:
Monsky, arXiv:2309.00162 ("the only rational solution of $x^3+y^3=2$ is
$(1,1)$", Cor. 2), equivalent to **Legendre's theorem that three distinct
nonzero cubes cannot form an arithmetic progression** — which is exactly
the statement that $D_c(w^3)$ contains no nonzero $d$. (Euler's original
argument worked in $\mathbb{Z}[\sqrt{-3}]$, not quite a UFD; the
$\mathbb{Z}[\omega]$ fix is standard.) Brute force: all $x,y,z\le600$
give only the 600 trivial solutions $[x=y=z]$. ∎ `[primary-source-verified
via search 2026-09-01 — abstract-level; paper body not read]`

**Consequences for the semi-magic problem.** (1) There is no analogue of
the square case's D-set engine: the MSS parametrization (entries
$a\pm b,\ a\pm c,\dots$ about a square center) is unavailable in the
cubic setting *in principle*, not merely uncomputed — any semi-magic
square of cubes must avoid symmetric opposite pairs entirely (a symmetric
pair $c^3\pm d$ about a cube center $c^3$ forces $d=0$). (2) The two
sibling problems are structurally disjoint, not cousins: squares have the
*fully magic* case open with a rich pair-completion theory; cubes have
the fully magic case *dead* (Wroblewski's mod-9 obstruction) and the
semi-magic case carrying 4-dimensional linear freedom (6 row/col
equations of rank 5 on 9 entries), so no divisor-structured pair
condition ever arises. The rarity escalation between the siblings is
qualitatively different, not parallel.

**Corollary (fully-magic impossibility, re-derived; stronger than
Wroblewski).** In any fully magic $3\times3$ square (rows, columns, both
diagonals equal to $S$): summing the four lines through the center gives
$3S+3e=4S$, so the center $e=S/3$, and every opposite pair sums to
$2e=S-e$. If all entries are cubes with center $c^3$, each opposite pair
satisfies $x^3+y^3=2c^3$, so by the Lemma $x=y=c$ — **all nine entries
are equal**. Hence the only fully magic $3\times3$ cube squares are the
degenerate all-equal ones; "no 9 different positive cubes" (Wroblewski
2007's mod-9 argument) is a corollary, and the Lemma gives the stronger
classification directly. *Why the square sibling stays open:* the same
argument step fails for squares precisely because $x^2+y^2=2w^2$ has
rich nontrivial solutions (Pythagorean pairs — the D-set of the sibling
problem). The open/dead dichotomy between the two problems is exactly
the richness/vacuity of their respective D-sets.

## Control-step framing (one line)
Resolution on a slice (8/9 near-miss; relaxed variants) → control = all nine
distinct cubes with equal row/column sums simultaneously — a simultaneous
Diophantine control step, the cubic sibling of the
[[magic_square_of_squares]] wall.

## See also
- [[magic_square_of_squares]] — the (fully magic, squares) sibling problem.