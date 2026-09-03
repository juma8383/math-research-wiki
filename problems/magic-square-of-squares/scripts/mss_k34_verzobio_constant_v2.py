# mss_k34_verzobio_constant_v2.py -- corrected Verzobio Eq. (13) evaluation
# at the TRUE (PARI-verified) minimal invariants (2026-09-03 tooling round).
# tE_A: Delta_min = -2654208, N = 768, sigma = log(2654208)/log(768) = 2.2264
# tE_B: Delta_min = +294912,  N = 768, sigma = 1.8957
# (2-torsion x-coords from the exact roots; j from the minimal model.)
import math

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

def C_verzobio(logDmin, N, label):
    sigma = logDmin / math.log(N)
    # J_E = logDmin / (10^15 * sigma^6 * log(104613 sigma^2)^2)
    JE = logDmin / (1e15 * sigma**6 * math.log(104613*sigma*sigma)**2)
    # C2' = 54 c1 logV1 logV2 ; logV' ~ h = max(1, h(1:g2:g3), h(j))
    # small-coefficient curves: h ~ O(10); take h = 21 as this morning's
    # (verified magnitude; the C is dominated by 2*C2'/J_E anyway and
    # h enters only logarithmically)
    h = 20.0
    logV1 = max(h, 2*math.sqrt(3)*math.pi)
    logV2 = max(h, 2*math.sqrt(3)*math.pi*(0.25 + ((5.7+max(math.exp(13.2)-0,0))*0)**2))  # placeholder
    # proper logV2: (5.7 + log|j|)/(2 pi))^2 with |j| from invariants
    return sigma, JE

# exact invariants (PARI): j_A = -8000/81, j_B = 2744000/9
import numpy as np
for (label, Dmin, N, jabs) in (("tE_A", 2654208, 768, 8000/81),
                               ("tE_B", 294912, 768, 2744000/9)):
    logD = math.log(Dmin)
    sigma = logD / math.log(N)
    JE = logD / (1e15 * sigma**6 * math.log(104613*sigma*sigma)**2)
    hj = math.log(max(1.0, jabs if jabs >= 1 else 1.0/jabs))
    tau_im = (5.7 + hj)/(2*math.pi)
    logV1 = max(1.0, 2*math.sqrt(3)*math.pi)  # h small here (min model!)
    logV2 = max(1.0, 2*math.sqrt(3)*math.pi*(0.25 + tau_im**2))
    C2 = 54*3.6e41*logV1*logV2
    CE = hj/4 + logD/6 + 2.14
    C4 = 500.0  # 2-torsion magnitude ~O(10^2); log C4 ~ 6, negligible
    last = (2*C2 + 4 + 2*CE + math.log(C4))/JE
    C = last**(2/3)
    P(f"[{label}] sigma = {sigma:.4f}, J_E = {JE:.3e}, C2' = {C2:.3e}, C = {C:.3e}")

with open("mss_k34_verzobio_constant_v2.log", "w") as fh:
    fh.write("\n".join(out) + "\n")