from fractions import Fraction as F
import math

# D's quartic structure: V^2 = N(x) = (x^2-238)^2 * phi-map... degenerate pts:
#   x=0: V=+-238 (R=T_a);  x=4: N(4)=? ; roots of x^2-238x+3364? disc=238^2-4*56644=0? 
N = lambda x: x**4 - 4*x**3 - 604*x*x - 952*x + 56644
print("N(0) =", N(0), "= 238^2 :", N(0)==238**2)
print("N(4) =", N(4))
# factor N over Q? try small rational roots
for cand in [1,2,4,7,14,17,34,119,238,-1,-2,-4,-7,-14,-17]:
    if N(cand)==0: print("root:", cand)
# N as quadratic in x + ... complete square: (x^2-2x)^2 = x^4-4x^3+4x^2
# N = (x^2-2x)^2 - 608x^2 - 952x + 56644
print("\ncomplete-square: N = (x^2-2x)^2 - (608x^2+952x-56644)")
# discriminant of the quadratic remainder
discq = 952**2 + 4*608*56644
print("608x^2+952x-56644 disc =", 952*952 + 4*608*56644, "=", )
def pf(n):
    fs=[]; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e: fs.append((d,e))
        d+=1
    if n>1: fs.append((n,1))
    return fs
print("   factored:", pf(952*952 + 4*608*56644))
# The quartic D is an elliptic curve in disguise with full rational 2-torsion?
# N has rational root iff it factors; degenerate point (0,238) only.
# J_L Frobenius vs D's local solubility at small primes: quick check
print("\nD local points x mod small primes (V^2=N(x) solvable?):")
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43]:
    QR = {pow(k,2,p) for k in range(p)}
    sol = any(((x*x*x*x - 4*x**3 - 604*x*x - 952*x + 56644) % p) in QR for x in range(p))
    print(f"  p={p}: soluble {sol}")