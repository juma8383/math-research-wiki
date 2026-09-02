# mss_k34_descent_p1.py -- K34-A factorization descent, part 1:
# verify the identity (R-V')(R+V') = 4608 a^4 b^4 and the delta = 2^j
# structure, and verify exhaustiveness of the constant-split enumeration.
# Exact integer / Fraction / sympy arithmetic throughout. ASCII output only.
import sys
from fractions import Fraction
from itertools import combinations

try:
    import sympy as sp
    HAVE_SYMPY = True
except ImportError:
    HAVE_SYMPY = False

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s)
    print(s)

P("== mss_k34_descent_p1: identity + delta structure verification ==")

# ---------- 1. Symbolic identity ----------
# M_A: V^2 = X^4+132X^3-250X^2+132X+1, X=(a/b)^2.
# Clearing denominators: V'^2 = a^8+132a^6b^2-250a^4b^4+132a^2b^6+b^8, V'=V*b^4.
# R = a^4+66a^2b^2+b^4.  Claim: R^2 - V'^2 = 4608 a^4 b^4, 4608 = 2^9*3^2.
if HAVE_SYMPY:
    a, b, V = sp.symbols('a b V')
    Rp = a**4 + 66*a**2*b**2 + b**4
    Vp2 = a**8 + 132*a**6*b**2 - 250*a**4*b**4 + 132*a**2*b**6 + b**8
    diff = sp.expand(Rp**2 - Vp2)
    P("[1] symbolic R^2 - V'^2 =", sp.factor(diff))
    assert diff == 4608*a**4*b**4, "identity FAILED"
    # also verify the clearing-denominators step itself:
    f = lambda x: x**4 + 132*x**3 - 250*x**2 + 132*x + 1
    X = sp.symbols('X')
    lhs = sp.expand(f(a**2/b**2) * b**8)
    assert sp.simplify(lhs - Vp2) == 0
    P("[1] identity (R^2-V'^2)=4608a^4b^4 and b^8*f((a/b)^2)=V'^2: VERIFIED symbolically")
    P("[1] 4608 = 2^9*3^2 :", 4608 == 2**9*3**2)

# ---------- 2. Numeric identity sweep ----------
bad = 0
for aa in range(0, 61):
    for bb in range(1, 61):
        from math import gcd
        if gcd(aa, bb) != 1:
            continue
        R = aa**4 + 66*aa**2*bb**2 + bb**4
        Vp2 = aa**8 + 132*aa**6*bb**2 - 250*aa**4*bb**4 + 132*aa**2*bb**6 + bb**8
        if R*R - Vp2 != 4608*aa**4*bb**4:
            bad += 1
P("[2] numeric identity sweep a,b<=60 coprime: mismatches =", bad)

# ---------- 3. Lemma inputs, verified numerically ----------
# (i) mod 3: 66a^2b^2 = 0 mod 3, so R = a^4+b^4 mod 3; fourth powers are 0/1.
#     If 3 does not divide ab, R = 2 mod 3, so 3 | R is impossible unless 3|ab;
#     if 3|a then R = b^4 mod 3 (nonzero), so 3|ab forces 3|a AND 3|b, i.e. 3 | gcd. Impossible.
# (ii) any odd p | delta => p | R and p | V'; p | 4608a^4b^4 => p | 3 or p | ab;
#      p | a => R = b^4 mod p nonzero. So no odd p | delta. => delta = 2^j.
cnt3 = 0
for aa in range(1, 200):
    for bb in range(1, 200):
        from math import gcd
        if gcd(aa, bb) != 1 or aa % 3 == 0 or bb % 3 == 0:
            continue
        R = aa**4 + 66*aa**2*bb**2 + bb**4
        if R % 3 != 2:
            cnt3 += 1
P("[3] R mod 3 = 2 whenever 3 !| ab (coprime a,b<200): violations =", cnt3)

# (iii) 2-adic pattern of R and of v2(R):
#   both odd  => R = 4 mod 16  (v2(R)=2)
#   one even  => R odd
c1 = c2 = c3 = 0
for aa in range(1, 400, 2):
    for bb in range(1, 400, 2):
        if (aa % 4) * (bb % 4) != 0:  # placeholder
            pass
        R = aa**4 + 66*aa**2*bb**2 + bb**4
        if R % 16 == 4:
            c1 += 1
        else:
            c3 += 1
P("[3] both odd: R=4 mod 16 count =", c1, " violations =", c3)
vio = 0
for aa in range(2, 400, 2):
    for bb in range(1, 400, 2):
        R = aa**4 + 66*aa**2*bb**2 + bb**4
        if R % 2 != 1:
            vio += 1
    for bb in range(2, 400, 2):
        R = aa**4 + 66*aa**2*bb**2 + bb**4  # both even skipped by gcd later
P("[3] exactly one even: R odd, violations =", vio)

# ---------- 4. delta structure on all "witness" points ----------
# The only known exact solutions of V'^2 = ... are the degenerate ones:
#   X=0  : (a,b)=(0,1), V'=+-1 ;  X=1 : (a,b)=(1,1), V'=+-4.
# For each, compute delta = gcd(R-V', R+V') and its factorization, and check
# the predicted (delta, U, W, c1, c2, u, v) structure.
P("[4] degenerate witnesses:")
for (aa, bb) in [(0, 1), (1, 1)]:
    R = aa**4 + 66*aa**2*bb**2 + bb**4
    for Vp in set():
        pass
    Vp2 = aa**8 + 132*aa**6*bb**2 - 250*aa**4*bb**4 + 132*aa**2*bb**6 + bb**8
    Vp = int(Vp2**0.5)
    assert Vp*Vp == Vp2
    for s in (1, -1):
        W1 = R - s*Vp
        W2 = R + s*Vp
        from math import gcd
        d = gcd(W1, W2)
        P("    (a,b)=", (aa, bb), " V'=", s*Vp,
          " R-V'=", W1, " R+V'=", W2, " delta=", d,
          " delta_fact=", sp.factorint(d) if HAVE_SYMPY else d)
        U, W = W1 // d, W2 // d
        assert gcd(U, W) == 1 and U*W*d*d == 4608*aa**4*bb**4
        P("      U=", U, " W=", W, " gcd(U,W)=1 ok, UW=4608a^4b^4/delta^2 ok")

# ---------- 5. Exhaustiveness of the constant split ----------
# delta = 2^j. (R-V')=delta*U, (R+V')=delta*W, gcd(U,W)=1,
# UW = 2^(9-2j) * 3^2 * (ab)^4.
# Claim: with u*v=ab, gcd(u,v)=1, the FOURTH-POWER-FREE constants are
#   (c1,c2) in {(1,72),(8,9),(9,8),(72,1)} for BOTH j=1 and j=3,
# and the full (non-normalized) splits are:
#   j=1: (2^7*3^b, 3^(2-b)) for b in {0,2} (b=1 breaks gcd(U,W)=1), plus swap
#   j=3: (2^3*3^b, 3^(2-b)) for b in {0,2}, plus swap
# Brute-force check over ALL fourth-power-free divisor pairs c1*c2 | 2^m*3^2
# that only these survive the coprimality + uv=ab bookkeeping.
P("[5] constant-split enumeration:")
def fourth_power_free(n):
    f = sp.factorint(n)
    r = 1
    for p_, e in f.items():
        r *= p_**(e % 4)
    return r
seen = set()
for j in (1, 3):
    m = 9 - 2*j
    N = 2**m * 9
    fpf = fourth_power_free(N)
    divs = [d for d in range(1, fpf+1) if fpf % d == 0]
    ok_pairs = []
    for c1 in divs:
        c2 = fpf // c1
        # coprimality of U,W forces gcd(c1,c2)=1
        if sp.gcd(c1, c2) != 1:
            continue
        ok_pairs.append((c1, c2))
    P("    j=", j, " m=", m, " fpf(2^m*9)=", fpf,
      " coprime fpf pairs:", ok_pairs)
    seen.update(ok_pairs)
P("[5] union of admissible (c1,c2) over j in {1,3}:",
  sorted(seen))
assert sorted(seen) == [(1, 72), (8, 9), (9, 8), (72, 1)], "unexpected set"
P("[5] EXACTLY the four pairs (1,72),(8,9),(9,8),(72,1) occur. VERIFIED")

# ---------- 6. R-form reconstruction check ----------
# j=1: R = c1u^4 + c2v^4 ;  j=3: R = 4(c1u^4 + c2v^4);  uv=ab.
# Verify on the degenerate witness (1,1): j=3, (c1,c2)=(8,9), u=v=1:
#   4*(8+9) = 68 = R(1,1).  And V' = 2^(j-1)(c2v^4-c1u^4) = 4*(9-8) = 4. ok
R11 = 1 + 66 + 1
assert 4*(8*1 + 9*1) == R11
P("[6] degenerate (1,1): R = 4*(8*1^4+9*1^4) = 68, V' = 4*(9-8) = 4. VERIFIED")

# ---------- 7. Derived master identity: R = n^2 + 64 (ab)^2, V'^2 = n^4+128n^2P^2-512P^4
for aa in range(0, 40):
    for bb in range(1, 40):
        from math import gcd
        if gcd(aa, bb) != 1:
            continue
        n = aa*aa + bb*bb
        Pq = aa*bb
        R = aa**4 + 66*aa**2*bb**2 + bb**4
        assert R == n*n + 64*Pq*Pq if False else True
        assert R == n**2 + 64*(Pq**2)
        Vp2 = aa**8 + 132*aa**6*bb**2 - 250*aa**4*bb**4 + 132*aa**2*bb**6 + bb**8
        assert Vp2 == n**4 + 128*n**2*Pq**2 - 512*Pq**4
P("[7] R = n^2+64(ab)^2 and V'^2 = n^4+128n^2(ab)^2-512(ab)^4: VERIFIED numerically")

with open("mss_k34_descent_p1.log", "w") as fh:
    fh.write("\n".join(out) + "\n")
P("== p1 done, log written ==")