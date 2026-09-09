from fractions import Fraction as F
import math

# J_L : y^2 = x^3 - 27894240 x + 56491485696 ; T = (-6096, 0)
# Shift X = x + 6096 (move 2-torsion to X=0):
# y^2 = (X-6096)^3 - 27894240(X-6096) + 56491485696
def f(x): return x**3 - 27894240*x + 56491485696
# expand (X+t)^3 + A(X+t) + B with t = -6096
t = -6096; A = -27894240; B = 56491485696
a2 = 3*t
a4 = 3*t*t + A
a6 = t**3 + A*t + B
print(f"shifted J_L: y^2 = X^3 + {a2}X^2 + {a4}X + {a6}" if False else
      f"shifted J_L: y^2 = X^3 + {a2} X^2 + {a4} X + {a6}" if False else
      f"shifted J_L: y^2 = X^3 + {a2}X^2 + {a4}X + {a6}")
a6 = a6 if False else None
# careful: we want y^2 = X^3 + a2 X^2 + a4 X (+ a6 = 0?)
# f(X + t) = (X+t)^3 + A(X+t) + B -> constant term f(t) = f(-6096) = 0 (T on curve)
const = f(t)
print("f(t) =", const, "(should be 0)")
print(f"shifted: y^2 = X^3 + {a2}X^2 + {a4}X")
# So alpha^L(P) = X(P) mod squares, alpha^L(T) = a4 (the X-coefficient, like b=238 before)
print("a4 =", a4, "=", pf_str := None)
def pf(n):
    fs=[]; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e: fs.append((d,e))
        d+=1
    if n>1: fs.append((n,1))
    return fs
print("a4 factored:", pf(a4))
# known point G = (2472, 51408) on the UNSHIFTED model -> X = 2472 - 6096 = -3624
XG = 2472 + t
print("X(G_L) =", XG, " factored:", pf(abs(XG)), " sign:", 1 if XG>0 else -1)
def sqclass(n):
    s = -1 if n < 0 else 1
    n = abs(n); out=1; d=2
    while d*d<=n:
        e=0
        while n%d==0: n//=d; e+=1
        if e%2: out*=d
        d+=1
    if n>1: out*=n
    return (s*out)
print("alpha^L(G_L) sqclass:", sqclass(XG))
# verify G on curve:
y2 = 51408**2
chk = 2472**3 - 27894240*2472 + 56491485696
print("G on J_L:", y2 == chk if False else (51408*51408 == chk))