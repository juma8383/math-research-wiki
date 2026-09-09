#!/usr/bin/env python3
# While the search runs — the decisive alternative: match the pair against
# the LMFDB genus-2 / elliptic-curve database via the quartic factor traces.
# Actually a MUCH better idea: use the mod-5 data we already have.
# The mod-5 sieve on Z_D: W_5 = {0, ±1}. The condition on (r,s): s ≡ 0, ±r.
# The 33 surviving admissible points satisfy this. Push the sieve further:
# W_7(Z_D) = {0,1,3,4,6} = {0,±1,±3} mod 7 (i.e. s ≡ 0, ±r, ±3r mod 7? no:
# w = s/r mod p requires r invertible; when 5|r, w ≡ ∞: handle via the
# leading-coefficient character). For primes p ∤ r: s/r ∈ W_p.
# The composite condition: s/r mod p ∈ W_p for all p (p∤r). This is a strong
# joint constraint — the MW-sieve on the ratio w = s/r.
# The ratio w = s/r is FIXED per fiber point. The sieve can't kill individual
# known points beyond what we test — but for the DESCENT-CHAIN question, we
# don't have a bounded box: the chain is infinite. The sieve kills finite
# boxes. The Chabauty route (rank) remains the only path to a full kill.
# => The named next step stands: pin the ±pair, compute ranks.
# While waiting: verify Z_D's OTHER two elliptic quotients more directly:
# compute the quartic Frobenius factor at p=13, 19, 29 and compare against
# the hypothesis "pair surface = Jac of genus-2 curve y^2 = ...?":
# A natural genus-2 candidate: the D-tower has TWO involutions besides the
# hyperelliptic one: w->-w (quotient: V^2 = u^4-4u^3-604u^2-952u+56644 with
# u=w^2 — that's D itself!). So Z_D/w~−w = D (the gate quartic, genus 1!).
# Jac(Z_D) = Jac(D) x Prym, Prym = genus 2 (since 3-1 = 2). The ±pair IS the
# Prym surface (genus 2), not two elliptics! Its charpoly at split primes
# factors as two quadratics because the Prym genus-2 curve ALSO splits
# (bielliptic). The genus-2 Prym curve: the standard Prym for the double
# cover (w,V)->(u=w^2, V) of D... which is exactly the curve whose Jac has
# charpoly x^4 + (2p-t^2)x^2 + p^2 at split primes.
# So the pair = Jac of a genus-2 curve P: y^2 = ? with the property that
# P's elliptic subcovers are the ±twist pair. 
# FOR THE WIKI: rank Jac(Z_D) = 1 + rank(Jac(P)); P is genus 2; rank(Jac(P))
# <= 1 needed. Compute P's model: the Prym of the double cover Z_D -> D
# ramified at the 8 branch points of D not... The Prym dimension 2 = Jac(P).
# The cover Z_D -> D is (w, V) -> (u = w^2, V): y^2 = V^2 = N(u) with u = w^2:
# a double cover of the quartic D ramified at u-roots of N (no rational roots)
# and at infinity (2 points). The Prym: classical formula for the quadratic
# twist: Jac(P) = the twist of Jac(D)=J_L by the cover character — the twist
# by Q(sqrt(8))? or by the branch structure. We TESTED "J_L twisted by 8"
# earlier and it FAILED. The Prym of a degree-2 cover of a GENUS-1 curve
# ramified at 4 points (the branch points of the quartic map, i.e. the roots
# of N(u)=0 — 4 roots over Q(i)sqrt-ish) is a genus-2 curve; its Jac is NOT
# generally a twist of Jac(D). The genus-2 P: V^2 = N(u) + something*... the
# standard model: P is the curve (V^2 - N(u) = 0, u = w^2) — eliminating w:
# the cover is u = w^2, so P = Z_D itself?? No: Z_D IS the cover. P = Prym
# = the "difference" — a genus-2 curve whose Jac is the anti-invariant part
# of Jac(Z_D) under the D-cover involution. 
# P's model: for the double cover C': y^2 = f(w) -> C: y^2 = f(w^2)?? I had it
# backwards: Z_D: V^2 = N(w^2) covers D: V^2 = N(u), u = w^2. The involution
# w -> -w. The Prym P: the quotient by (w,V) -> (-w,-V): invariants wV and
# w^2: P: (wV)^2 = w^2 N(w^2) => (wV)^2 = w^2 N(w^2): set Y = wV, u = w^2:
# Y^2 = u N(u) = u(u^4 - 4u^3 - 604u^2 - 952u + 56644) — GENUS 2: y^2 = x^5-4x^4-604x^3-952x^2+56644x!
print("Prym P (genus 2): y^2 = x(x^4 - 4x^3 - 604x^2 - 952x + 56644) = x*N(x)")
print("rank(Jac(Z_D)) = rank(J_L) + rank(Jac(P)); need rank(Jac(P)) <= 1.")
print("P has rational points: x=0 => y=0 (the branch point); x=4: y^2 = 4*43172?")
print("P's Frobenius at split primes = the (t,-t) pair ✓ consistent.")
print("Genus-2 rank machinery: 2-descent on Jac(P) — no Sage; PARI has none.")
print("BUT the (t,-t) pattern suggests Jac(P) ~ E x E-twist (elliptic factors):")
print("then rank(Jac(P)) = rank(E) + rank(E-twist) = 2*rank(E) (twists have equal")
print("rank when the twist character's root numbers align...). If E has CM or is")
print("a Q-curves, rank(E^chi) = rank(E). So rank Jac(P) is even: 0 or 2+.")
print("rank Jac(Z_D) = 1 + {0 or 2} = 1 or 3. Chabauty needs 1: the pair E rank 0.")
print("Empirical: search E among small curves continued; also compute P's")
print("2-division field structure to pin E.")
print()
print("Get P's charpoly at a few primes and fit E, E-twist precisely:")