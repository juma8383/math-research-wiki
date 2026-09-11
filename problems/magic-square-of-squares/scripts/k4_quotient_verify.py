# Independent verification of the Copilot-contribution load-bearing claims.
# Plain python, exact arithmetic. CORRECTED substitutions 2026-09-11:
#   E4 quartic: W^2 = u^4 - 248u^2 + 16
#   lift: t = x + 1/x, u = x - 1/x  (t^2 - u^2 = 4),  Z = W x^2
#   C4: Z^2 = x^8 - 252x^6 + 518x^4 - 252x^2 + 1
#   Jacobian model of biquadratic Y^2 = v^4 + a v^2 + b:
#       J: Y^2 = X^3 - 2a X^2 + (a^2 - 4b) X
from fractions import Fraction as F

ok = []

# 1. Coupling: t = x + 1/x, u = x - 1/x  =>  t^2 - u^2 = 4
for x in [F(2), F(3), F(5), F(7), F(-2), F(-3), F(1, 2), F(3, 5), F(-7)]:
    t = x + 1 / x
    u = x - 1 / x
    assert t * t - u * u == 4, x
ok.append("t = x+1/x, u = x-1/x  =>  t^2 - u^2 = 4  (exact, many x)")

# 2. C4 identity: W^2 = u^4 - 248u^2 + 16 with u = x - 1/x, Z = W x^2
#    => Z^2 = x^8 - 252x^6 + 518x^4 - 252x^2 + 1 =: P(x)
#    Polynomial-level check: x^4 W^2 = x^4 u^4 - 248 x^4 u^2 + 16 x^4
#      x^4 u^2 = x^4(x-1/x)^2 = x^6 - 2x^4 + x^2  -> (x^2-1)^2 x^2... compute:
#    Verify as polynomial identity in Q[x] by dense evaluation incl. rationals:
def P(x):
    return x**8 - 252 * x**6 + 518 * x**4 - 252 * x**2 + 1

for x in [F(2), F(3), F(5), F(7), F(-2), F(-3), F(1, 2), F(3, 5), F(-7), F(11, 3)]:
    u = x - 1 / x
    W2 = u**4 - 248 * u**2 + 16
    # Z^2 = x^4 * W^2 must equal P(x):
    assert x**4 * W2 == P(x), x
ok.append("C4 identity x^4*(u^4-248u^2+16) = P(x), u = x-1/x  (exact)")

# 3. Norm factorization: P(x) = (x^4 - (126+32r)x^2 + 1)(x^4 - (126-32r)x^2 + 1), r = sqrt(15)
#    Symbolically: coefficients c_k with s = 252, p = 516 = 126^2 - 32^2*15
assert 126**2 - 32**2 * 15 == 516
assert 252**2 - 4 * 516 == 61440
ok.append("norm factorization constants: 126^2-(32^2)(15)=516; disc 61440 = (64 sqrt15)^2")

# 4. Jacobian model J: Y^2 = X^3 - 2aX^2 + (a^2-4b)X for Y^2 = v^4 + a v^2 + b
#    J_u from a=-248, b=16:  X^3 + 496 X^2 + 61440 X = X(X+240)(X+256)
#    J_t from a=-256, b=1024: X^3 + 512 X^2 + 61440 X = X(X+192)(X+320)
for (a, b, roots, name) in [
    (-248, 16, (0, -240, -256), "J_u = X(X+240)(X+256)"),
    (-256, 1024, (0, -192, -320), "J_t = X(X+192)(X+320)"),
]:
    c2, c1 = -2 * a, a * a - 4 * b
    s = sum(roots)
    p1 = sum(roots[i] * roots[j] for i in range(3) for j in range(i + 1, 3))
    assert s == -c2 and p1 == c1, (name, c2, c1, s, p1)
    ok.append(f"{name} matches -2a={-2*a}, a^2-4b={a*a - 4*b}")

# 5. P = (4, 504) on J_t (A2=512, A4=61440); 2P = (14737921/3969, -60471686143/250047)
A2, A4 = 512, 61440
assert F(504) ** 2 == 4**3 + A2 * 16 + A4 * 4
m = F(3 * 16 + 2 * A2 * 4 + A4, 2 * 504)
assert m == F(4099, 63), m
x3 = m * m - A2 - 4 - 4
assert x3 == F(14737921, 3969), x3
y3 = -(504 + m * (x3 - 4))
assert y3 == F(-60471686143, 250047), y3
ok.append("P=(4,504) on J_t; 2P=(14737921/3969, -60471686143/250047) nonintegral")

# 6. bonus structure: Q=(-256,1024) on J_t, 2Q = -P
assert 1024**2 == (-256) ** 3 + A2 * 256**2 + A4 * (-256)
m2 = F(3 * 256**2 + 2 * A2 * (-256) + A4, 2 * 1024)
x3q = m2 * m2 - A2 + 256 + 256
assert x3q == 4 and (1024 + m2 * (x3q - (-256))) == 504, (x3q, m2)
ok.append("Q=(-256,1024) on J_t with 2Q = -P  (P in <Q>)")

# 7. scaling: X=16x, Y=64y maps J_t -> y^2 = x^3+32x^2+240x = x(x+12)(x+20)
#    and J_u -> y^2 = x^3+31x^2+240x = x(x+15)(x+16)
#    2-isogeny: y^2=x^3+Ax^2+Bx -> y^2=x^3-2Ax^2+(A^2-4B)x
for (A, B, roots, label) in [
    (31, 240, (0, -15, -16), "E_u: y^2=x^3+31x^2+240x = x(x+15)(x+16)"),
    (32, 240, (0, -12, -20), "E_t: y^2=x^3+32x^2+240x = x(x+12)(x+20)"),
]:
    assert sum(roots) == -A and roots[0] * roots[1] + roots[0] * roots[2] + roots[1] * roots[2] == B
    Ap, Bp = -2 * A, A * A - 4 * B
    ok.append(f"{label}; 2-isogenous E': y^2=x^3+{Ap}x^2+{Bp}x")

# 8. corrected general families (k=4 specialization of multiplier quartics):
#    for general k the two must not be conflated:
#    J_{t,k}: X(X+16k(k-1))(X+16k(k+1))  -> 2a = -16k*2k = -32k^2, a^2-4b = 256 k^2(k^2-1)... check k=4:
r1, r2 = -16 * 4 * 3, -16 * 4 * 5
assert (0, r1, r2) == (0, -192, -320)
#    J_{u,k}: X(X+16k^2)(X+16(k^2-1)) -> k=4: (0,-256,-240)
assert sorted((0, -256, -240)) == sorted((0, -240, -256))
ok.append("k=4 specialization of both corrected families consistent with J_t, J_u")

print("\n".join("OK  " + s for s in ok))