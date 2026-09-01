---
type: attempt
problem: birch-swinnerton-dyer
attempt: 12
date: 2026-08-31
approach: point-supply reduction candidate from the ultracode breakthrough hunt; adversarially verified (survives novelty, needs revision on soundness/referee)
outcome: partial
tags: [kurihara-numbers, kim-2024, point-supply, reduction, sha]
---

# Attempt 12 — the point-supply reduction (filed with the required Sha-fix)

**The candidate.** In Kim's class (arXiv:2203.12159, to appear AJM;
$p\ge5$ good ordinary, $\bar\rho_p$ surjective, Manin constant prime to
$p$ — the Iwasawa main conjecture inverting $p$ is a theorem there by
Kato–Skinner–Urban–Wan), define the Kurihara numbers $\tilde\delta_n$
(finite modular-symbol computations). Claimed: BSD rank part
$\iff$ (a) point supply $\mathrm{rank}\,E(\mathbb Q)\ge r_{\mathrm{an}}$
plus (b) one nonzero $\tilde\delta_n$ with $\nu(n)\le r_{\mathrm{an}}$.

**Adversarial verification (3 lenses, this session).**
- *Novelty: SURVIVES.* Checked against the primary source: Kim states only
  the upper bound (Cor. 1.13: one nonzero $\tilde\delta_n$ with
  $\nu(n)$ prime factors $\Rightarrow \mathrm{rank}\le\nu(n)$) and the
  rank-0 equivalence; the packaged "supply + one Kurihara check $\iff$ BSD
  rank part" formulation is absent, and Kurihara explicitly frames his
  $\delta_n$ theory as "very different from BSD". Closest prior art:
  Kurihara's Conjecture 0.1 ($\delta$-minimal $n\Rightarrow r_{n,p}$
  bijective $\Rightarrow \mathrm{rank}=\nu(n)$) — its surjectivity half is a
  supply statement in disguise.
- *Soundness: NEEDS REVISION — the naive converse is FALSE.* Forward
  direction verified sound: (a)+(b) $\Rightarrow r_{\mathrm{an}}\le
  \mathrm{rank}\le\mathrm{cork}\,\mathrm{Sel}_p=\mathrm{ord}(\tilde\delta)
  \le r_{\mathrm{an}}$ (Kim Thm 1.8(1) + Cor 1.6; no need for Thm 1.8(4)),
  giving rank equality AND $\Sha(E/\mathbb Q)[p^\infty]$ finite for free.
  But "BSD $\Rightarrow$ (b) trivially" is wrong: the rank part alone does
  not bound $\mathrm{corank}\,\Sha[p^\infty]$ — exactly the hypothesis
  Kim himself carries in Thm 1.8(4).
- *Referee: NEEDS REVISION (corollary altitude).* The whole content is
  Kim's theorems plus the elementary rank $\le$ cork inequality; honest
  vehicle = short expository note/survey remark, not a research paper.

**The corrected statement (to file; supersedes the candidate's wording):**
In Kim's class, for $E/\mathbb Q$ with $r_{\mathrm{an}}$ certified
($L^{(r)}(E,1)\ne0$):
$$\text{(a)}\wedge\text{(b)} \iff \big[\,r_{\mathrm{alg}}=r_{\mathrm{an}} \ \wedge\ \Sha(E/\mathbb Q)[p^\infty]\ \text{finite}\,\big],$$
i.e. the conjunction is equivalent to the rank part *plus p-primary Sha
finiteness* — strictly stronger than the rank part. Best corollary:
(a)+(b) forces $\mathrm{rank}=\mathrm{cork}$, so $\Sha[p^\infty]$ finiteness
and structure come out with no finiteness hypothesis. Honest caveats:
(b) is *semi-decidable* (one nonzero $\tilde\delta_n$ certifies; refutation
needs all $n$ with $\nu(n)\le r_{\mathrm{an}}$); classical mod-$p$ descent
already gives a finite rank-upper-bound certificate
($\dim_{\mathbb F_p}\mathrm{Sel}_p\le r_{\mathrm{an}}$), and Kim's
certificate is strictly finer precisely because it survives $\Sha[p]$
torsion — the note must argue this explicitly. Residual to-verify before any
write-up: Kim §1.9–1.10 full read; SU14 fine print beyond Kim's secondhand
citation.

**Structural read (why this matters to the folder's frontier).** The
reduction makes the wiki's two-engine thesis concrete in Kim's framework:
the *control half* ((b): Selmer-corank pinning) is a finite computation at
every rank, and **all residual open weight sits on the supply half** ((a)),
for which no rank-$\ge2$ engine exists (Heegner/Darmon points are rank-1
engines). This is the BSD avatar of "[[average-vs-pointwise-control]]":
control is computable, supply is the wall.

**Outcome.** Filed; not developed into a paper this session (referee
verdict). The corrected statement + caveats above are the reusable content.