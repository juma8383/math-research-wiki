# sage_k34_class_m2m1.sage -- check the M/2-1 survivor class properly
# (2026-09-03). The class M/2-1 survives the filed sieve but my probe killed
# it: because X(nG) is only defined mod p for n mod ord_p(G), and the class
# c = M/2-1 reduces to n_mod = c mod o per prime. Verify with the exact
# pole-refinement conditions: at p=13 the pole constant is 1151/66 = 7 mod 13
# (nonresidue), killing n = 2 mod 10 classes. For c = M/2-1: check what
# X(c*G) mod p is at valid primes.
EA = EllipticCurve([0,-256,0,18432,0])
M = 42078090600
c = M//2 - 1
print("class M/2-1 =", c, " mod small primes:")
# M/2 = 21039045300. c mod o for various primes:
for p in [5, 7, 11, 13, 17, 19, 23, 73, 163, 313]:
    Ep = EA.change_ring(GF(p))
    Gp = Ep(128, 512)
    o = Gp.order()
    nmod = c % o
    Pt = nmod * Gp
    if Pt == Ep(0):
        print(f"p={p}: ord={o}, n mod ord = {nmod} -> point at infinity (keep)")
        continue
    xP = Pt[0]
    if xP == 0 or xP == 4:
        print(f"p={p}: X undefined (pole) - refinement needed")
        continue
    num = 2*Pt[1] + 66*xP
    den = xP*(xP - 4)
    if den == 0:
        print(f"p={p}: pole (x=4) - p-adic refinement (filed lever)")
        continue
    val = num/den
    squares = set(GF(p)(i)^2 for i in range(p))
    isQR = val in squares
    print(f"p={p}: n mod ord = {nmod}, X = {val}, QR = {isQR}" +
          ("  -> KILL" if (p in (5,11,13) and val not in (0,1)) or (p not in (5,11,13) and not isQR) else "  -> keep"))