---
type: theorem
name: Catalan–Mihăilescu theorem
created: 2026-08-24
tags: [number-theory, exponential-diophantine]
used-in: [[beals_conjecture]]
provenance: []
---

# Catalan–Mihăilescu theorem

**Statement.** The only solution in integers $a,b,x,y > 1$ to

$$a^x - b^y = 1$$

is $3^2 - 2^3 = 1$. Equivalently, $8$ and $9$ are the only consecutive perfect
powers.

**Status.** Proved. Predraga Mihăilescu (2002), using cyclotomic-field methods.
Catalan conjectured it in 1844.

**Relevance to Beal.** Context for the "tight-by-1" phenomenon observed in
attempt-01 of [[beals_conjecture]]: the gap-1 near-misses there are
$A^x+B^y = C^z \pm 1$ — a *three-term* sum/difference landing one off a perfect
power, more general than Catalan's *two-term* $a^x-b^y=1$. Catalan rules out
two-term gap-1 perfect-power coincidences (except $8,9$); Beal's near-misses are
a genuinely different, three-term analogue. Catalan does not directly prove
Beal, but the gap-1 structure suggests the obstruction is of the same delicate
arithmetic kind, and the Mordell-curve / elliptic-fiber viewpoint on
$A^x+B^y-C^z=k$ (small $k$) is the natural setting for studying it.