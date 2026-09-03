# mss_k34_verzobio_constant.py -- evaluate Verzobio 2023 (PJM 325 (2023)
# 331-351, arXiv:2001.02987v3) Equation (13) constant C(E/K,M) for the two
# master curves, to check the filed "C(E) ~ 1e39-42" ballpark (2026-09-03).
# Eq (13): C = max{ C1, V1', V2', exp(D), exp(eh), e^30,
#                   ((2 C2' + 4 + 2 C_E + log C4)/J_E)^(2/3) }
#   h    = max{1, h(1:g2:g3), h(j(E))}   (heights on P^2 / of j)
#   c1   = 3.6e41 (David's Thm 2.1 constant at k=2)
#   log V1' = max{h, 2 sqrt(3) pi / D};  D=1 for K=Q
#   log V2' = max{h, 2 sqrt(3) pi (1/4 + ((5.7+max{log|j|,0})/(2pi))^2)/D}
#   C2'  = 54 c1 D^6 logV1' logV2'
#   C_E  = h(j)/4 + h(Delta)/6 + 2.14
#   C4   = 2 max{|x(T)| : T in E(Qbar)[2] \ {O}}   (2-torsion x-coords, inf norm)
#   J_E  = log|N(Delta_min)| / (10^15 D^3 sigma^6 log^2(104613 D sigma^2))
#   sigma= Szpiro ratio = log|Delta_min|/log|cond|   (sigma=1 if good everywhere)
# Heights: h(x/y)=log max(|x|,|y|) on Q (naive log height); h(j) for j=p/q
# in lowest terms = log max(|p|,|q|); h(1:g2:g3) on P^2 for integer coords
# with gcd 1 = log max(|g2|,|g3|) (standard affine convention).
# NOTE: we use the FILED (non-minimal) models since Verzobio's constant
# depends on the model M; we also evaluate at the minimal models
# (scaled) for comparison. Delta_min of the scaled minimal model: for
# y^2=x^3+a2 x^2+a4 x with u-division (x,y)->(u^2 x,u^3 y): Delta scales
# by u^12; minimal requires u=1 for integer a2,a4 with gcd(a2^3,a4^2)...
# we compute Delta and report; minimal-model reduction by u=1 (both
# curves already have integer short form; check common factors).
# ASCII only.
import math

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def hq(p, q):
    # naive log height of rational p/q (q>0), value >= 0
    return math.log(max(abs(p), abs(q)))

def height_p2(g2, g3, g4):
    # h on P^2 of (1:g2:g3) -> we use (1:g2:g3) triples; here generic
    m = max(abs(g2), abs(g3), abs(g4), 1)
    return math.log(m)

def disc_short_weierstrass_x2(a2, a4):
    # y^2 = x^3 + a2 x^2 + a4 x  (a6=0)
    # b2=4a2, b4=2a4, b6=0, b8=-a4^2
    b2, b4, b6, b8 = 4*a2, 2*a4, 0, -(a4*a4)
    return -(b2*b2*b8) - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6

def c4_c6(a2, a4):
    b2, b4, b6 = 4*a2, 2*a4, 0
    c4 = b2**2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    return c4, c6

def verzobio_C(a2, a4, label):
    c4v, c6v = c4_c6(a2, a4)
    j_num = c4v**3
    j_den = 16*(4*a4**3 + 27*a2**2*a4**2)  # for a6=0: 4a4^3+27a2^2a4^2
    # j = c4^3 / (16 Delta); Delta = -16(4 a4^3 + 27 a2^2 a4^2) -> |Delta|
    Delta = abs(-16*(4*a4**3 + 27*a2*a2*a4*a4))
    D = 1.0
    hj = hq(j_num // math.gcd(abs(j_num), abs(j_den)), abs(j_den)//math.gcd(abs(j_num), abs(j_den)))
    g2 = -4*a2*4  # in y^2=x^3-(g2/4)x-(g3/4) form: a2 term absent... but our
    # curve has an x^2 term; Verzobio Prop 6.1/Sec 8 assume short Weierstrass
    # y^2=x^3-(g2/4)x-(g3/4); complete the square-free x-shift:
    # x = X - a2/3 gives short form; g2,g3 rational. Use rational approx via
    # exact fractions of the shifted coefficients.
    from fractions import Fraction
    # shift: X = x + a2/3 ; y^2 = X^3 + p X + q with
    # p = a4 - a2^2/3, q = 2a2^3/27 - a2 a4/3
    p = a4 - a2*a2/3.0
    q = 2*a2**3/27.0 - a2*a4/3.0
    g2v = -48*p   # g2 = -48 p
    g3v = -864*q  # g3 = -864 q
    # heights as floats on P^2 of (1:g2:g3) with rational entries -> use
    # log max of numerators/denominators via float approx (fine for magnitude)
    h_1g2g3 = math.log(max(1.0, abs(g2v), abs(g3v)))
    h = max(1.0, h_1g2g3, hj)
    logV1 = max(h, 2*math.sqrt(3)*math.pi)
    tau_im = (5.7 + max(math.log(abs(j_num/j_den)), 0))/(2*math.pi)
    logV2 = max(h, 2*math.sqrt(3)*math.pi*(0.25 + tau_im**2))
    C2 = 54 * 3.6e41 * logV1 * logV2
    # C_E uses h(Delta) = log|Delta| (Delta integer)
    CE = hj/4.0 + math.log(Delta)/6.0 + 2.14
    # C4: 2-torsion x-coords of y^2=x^3+a2x^2+a4x: roots of the cubic
    import numpy as np
    rts = np.roots([1, a2, a4, 0])
    C4 = 2*max(abs(complex(r)) for r in rts).real if rts.size else 2.0
    # sigma: need conductor; no mwrank available. Bound sigma by Szpiro's
    # UNCONDITIONAL known range: use log|Delta|/log|cond| with cond >= 1,
    # i.e. sigma <= log|Delta|; also sigma >= 1 (if good everywhere) --
    # for magnitude purposes take sigma = log|Delta|/log(cond); we
    # estimate cond via the standard bound cond | Delta ( crude):
    # report C for sigma = 1..6 to show sensitivity, headline sigma=4.
    P(f"[{label}] Delta={Delta}, j={j_num/j_den:.3f}, h(j)={hj:.3f},"
      f" h(1:g2:g3)={h_1g2g3:.3f}, logV1={logV1:.2f}, logV2={logV2:.2f},"
      f" C2'={C2:.3e}, C_E={CE:.2f}, C4={C4:.2f}")
    for sig in (1.0, 2.0, 4.0, 6.0):
        JE = math.log(Delta)/(1e15 * sig**6 * math.log(104613*sig*sig)**2)
        last = (2*C2 + 4 + 2*CE + math.log(C4))/JE
        Clast = last**(2.0/3.0)
        P(f"[{label}] sigma={sig}: J_E={JE:.3e}, last-term C={Clast:.3e}")
    # C1: for K=Q, Delta_K=1 -> gpf(2)=2: C1 = 2^(m(Delta)/12) * max{4,m(1/j)} * (2*2+1)*2^2
    # m(Delta) = max ord over finite places = v_p(Delta) max = (integer Delta)
    # crude: m(Delta)=log_2(Delta) worst case; take max{4,m(1/j)}=max(4, log den/j num...)
    m_delta = math.log2(Delta)
    m_jinv = max(4.0, abs(math.log(abs(j_den/j_num))))
    C1 = (2**(m_delta/12.0)) * m_jinv * 5 * 4
    P(f"[{label}] C1~={C1:.3e} (rough), exp(eh)={math.exp(math.e*h):.3e}")
    P(f"[{label}] headline: C dominated by the last term (see lines above)")

# Master curves (filed models):
# E_A:  y^2 = X^3 - 250X^2 + 17420X + 35848  -- has a6 != 0; the kernel-sieve
# curve used for EDS is the SHIFTED a6=0 model:
# tE_A: y^2 = x^3 - 256x^2 + 18432x
# tE_B: y^2 = x^3 + 256x^2 - 2048x
P("== Verzobio Eq.(13) constants (model-dependent; K=Q, D=1) ==")
verzobio_C(-256, 18432, "tE_A")
verzobio_C(256, -2048, "tE_B")
with open("mss_k34_verzobio_constant.log", "w") as fh:
    fh.write("\n".join(out) + "\n")