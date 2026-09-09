#!/usr/bin/env python3
# Height bound on Z_D — step 3: archimedean constant + conservative r0.
from sage.all import *
import math
R = PolynomialRing(QQ, 'w')
w = R.gen()
f = w**8 - 4*w**6 - 604*w**4 - 952*w**2 + 56644
rts = f.roots(ComplexField(50), multiplicities=False)
mx = max(abs(r) for r in rts)
print("branch roots max |.| =", float(mx))
C_inf = 2 * math.log(1 + mx)
print("archimedean constant C_inf <=", "%.3f" % C_inf)
C_finite = 0.5 * (44*math.log(2) + 4*math.log(3) + 6*math.log(7) + 6*math.log(17) + 4*math.log(271))
print("finite constant (conservative) =", "%.2f" % C_finite)
C_total = C_inf + C_finite
print("total C =", "%.2f" % C_total)
r0 = math.exp(C_total)
print("conservative r0 bound =", "%.3e" % r0, "[to-verify: exact constants shrink this]")
print("DONE")