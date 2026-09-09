print("Find the Prym curve E/K explicitly: use the Res Frobenius data to build")
print("E/K's charpoly at split primes, then construct E/K from its traces over")
print("several primes via PARI/Sage's ellsearch over number fields, or use the")
print("KNOWN structure: P : y^2 = x*N(x) has the rational Weierstrass point")
print("(0,0). A genus-2 curve with a rational Weierstrass point and Jac = Res(E/K)")
print("has an INVOLUTION: the curve P must admit the map (x,y) -> (x, -y + something)")
print("... For y^2 = x*N(x) with the involution (x,y) -> (y^2/x /..., ...): the")
print("Richelot isogeny structure. The two elliptic quotients of a genus-2 curve")
print("with a rational Weierstrass point exist when the quintic is a quadratic")
print("in disguise: y^2 = x^5 + ... is a quadratic in x of the form")
print("y^2 = x*(quartic). The elliptic quotients come from the 2-isogeny class:")
print("Jac(P) ~ E1 x E2 where E1, E2 are 2-isogenous to curves derived from the")
print("decomposition y^2 = x*(quartic) = (u^2 - ...)...")
from sage.all import *
Rx = PolynomialRing(QQ, 'x')
x = Rx.gen()
N = x**4 - 4*x**3 - 604*x**2 - 952*x + 56644
# Check if N is a quadratic polynomial in x^2-ish variable or has rational
# quadratic factorization over a small extension: factor N over Q:
print("N factors over Q:", factor(N))
# y^2 = x*N(x): the genus-2 curve; its Jac splits via a 2-isogeny if N has a
# rational root (it doesn't) or if P is a double cover of two genus-1 curves:
# the classic split: y^2 = x^5 + ... with rational Weierstrass point has
# Jac ~ E1 x E2 iff the quintic is a palindromic transform... test:
# substitute x -> 1/x scaled: N(x)*x^{-4}: palindromic check
print("N coefficients palindromic?", [1, -4, -604, -952, 56644] == [56644, -952, -604, -4, 1])