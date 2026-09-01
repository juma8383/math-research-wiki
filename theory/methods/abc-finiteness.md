---
type: method
name: abc-conjecture finiteness argument (and its limit)
created: 2026-08-24
tags: [number-theory, abc-conjecture, exponential-diophantine]
used-in: [[beals_conjecture]]
provenance: []
---

# abc-conjecture finiteness argument (and its limit)

**The abc conjecture** (Oesterlé–Masser): for coprime $a+b=c$ and any
$\varepsilon>0$, $c \le K_\varepsilon\,\mathrm{rad}(abc)^{1+\varepsilon}$ with a
constant depending only on $\varepsilon$.

## Application to Beal signatures

For a primitive $A^x+B^y=C^z$ set $a=A^x,\ b=B^y,\ c=C^z$ (pairwise coprime by
[[method-pairwise-coprime-reduction]]). Then
$\mathrm{rad}(abc)=\mathrm{rad}(ABC)\le ABC$, and from $A^x,C^z$ sizes,
$A<C^{z/x},\ B<C^{z/y}$. abc gives

$$C^z \le K_\varepsilon\,(ABC)^{1+\varepsilon} < K_\varepsilon\,
   C^{(1+\varepsilon)(z/x+z/y+1)}.$$

So $C^{\,z-(1+\varepsilon)(z/x+z/y+1)} \le K_\varepsilon$. The exponent is
positive (for small $\varepsilon$) precisely when $1/x+1/y+1/z<1$. Hence abc ⟹
**$C$ is bounded ⟹ finitely many primitive solutions for that signature.**

## The limit (why abc does NOT prove Beal)

This finiteness is **identical in strength** to the *unconditional*
Darmon–Granville result [[thm-darmon-granville]] (which already gives finiteness
via Faltings). abc yields no improvement toward the actual Beal claim of
**zero** primitive solutions. The boundary case $1/x+1/y+1/z=1$ (only
$(3,3,3)$) is outside abc's reach anyway and is covered by FLT.

## When to reach for it

Useful only as a **negative** reference: if tempted to argue "abc implies
Beal," don't — it gives only finiteness, already known. Filed to prevent
revisiting this as a shortcut. The real gap (finitely-many → zero) requires the
modular machinery [[method-frey-modularity]], not abc.