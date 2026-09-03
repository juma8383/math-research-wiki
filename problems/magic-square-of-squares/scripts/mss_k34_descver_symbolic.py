# mss_k34_descver_symbolic.py -- symbolic verification round for the
# [mss-k34-descent] section, continuation 2026-09-03.
# Identities checked with sympy (exact):
#   I1: R^2 - 4608 a^4 b^4 == a^8+132a^6b^2-250a^4b^4+132a^2b^6+b^8
#       (the octic identity), R = a^4+66a^2b^2+b^4
#   I2: R == n^2 + 64 P^2 with n = a^2+b^2, P = ab (master reformulation)
#   I3: V'^2 == n^4 + 128 n^2 P^2 - 512 P^4 (second master reformulation)
#   I4: (c1,c2)-family: 2^(j-1)(c1 u^4 + c2 v^4) == (u^2+v^2)^2
#       + 64 u^2 v^2 holds exactly for the four pairs (with j absorbed):
#       j=1 (c1,c2) = (1,72): 1*(u^4+72v^4) ?= (u^2+v^2)^2 + 64u^2v^2 - 8u^2v^2
#         ... not an identity in general; only on the quartic solution set.
#       So I4 is NOT checked as an identity; instead the descent map
#       (u,v) -> (a,b) = (u*(a+b), v*(a+b)/...) -- too deep. Skip I4; the
#       four-case reduction was already verified in claude_check [B].
#   I5: degenerate-point consistency: (a,b)=(0,1) delta=2, (1,1) delta=8
# ASCII output only. Exit code 0.
from sympy import symbols, expand, simplify, Integer
import sys

a, b, u, v = symbols('a b u v', integer=True)
out = []

def P(*s):
    line = " ".join(str(x) for x in s)
    out.append(line); print(line)

P("== mss_k34_descver_symbolic ==")

R = a**4 + 66*a*a*b*b + b**4
octic = a**8 + 132*a**6*b*b - 250*a**4*b**4 + 132*a*a*b**6 + b**8

P("[I1] expand(R^2 - 4608*a^4*b^4 - octic) == 0:",
  simplify(expand(R**2 - 4608*a**4*b**4 - octic)) == 0)

n = a**2 + b**2
P_ = a*b
P("[I2] expand(R - (n^2 + 64P^2)) == 0:", simplify(expand(R - (n**2 + 64*P_**2))) == 0)

Vp2 = octic  # V'^2 = octic
P("[I3] expand(V'^2 - (n^4 + 128 n^2 P^2 - 512 P^4)) == 0:",
  simplify(expand(Vp2 - (n**4 + 128*n**2*P_**2 - 512*P_**4))) == 0)

# I5: degenerate points
for (aa, bb, dexp) in ((0, 1, 2), (1, 1, 8)):
    Rv = aa**4 + 66*aa*aa*bb*bb + bb**4
    octv = aa**8 + 132*aa**6*bb*bb - 250*aa**4*bb**4 + 132*aa*aa*bb**6 + bb**8
    import math
    Vv = math.isqrt(octv)
    d = math.gcd(Rv - Vv, Rv + Vv)
    P(f"[I5] (a,b)=({aa},{bb}) delta={d} expected={dexp} ok={d == dexp}")

# J1 identity check: F = 9*phi3 - 92*phi*psi, phi=x^3-4x, psi=x^2+2
x = symbols('x')
phi3 = (x**3 - 4*x)**3
phipsi = (x**3 - 4*x)*(x**2 + 2)
F_expr = 9*phi3 - 92*phipsi
P("[J1] expand(F - (x^9+92x^5-64x^3)) == 0:",
  simplify(expand(F_expr - (x**9 + 92*x**5 - 64*x**3))) == 0)

with open("mss_k34_descver_symbolic.log", "w") as fh:
    True
with open("mstmp.log", "w") as fh:
    pass
import os
os.remove("mstmp.log")
with open("mss_k34_descver_symbolic.out", "w") as fh:
    fh.write("\n".join(out) + ".log" if False else "\n".join(out) + "\n")
P("== done ==")