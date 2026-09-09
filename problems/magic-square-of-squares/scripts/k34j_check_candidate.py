from fractions import Fraction as F
import math

# CANDIDATE for the ±pair member: E: y^2 = x^3 + 2178x + 225
# ap: 23:-4 31:8 47:8 79:10 103:-10 151:-12 191:-18 199:4 223:24 239:12 241:18
# The Z ±pair traces: (4,-4) at 23... the pair members have OPPOSITE signs;
# ap(23) here = -4 (so E = the (-t) member at 23). But at 103: ap(E) = -10 vs
# pair (10,-10): E = (-10) member ✓; at 151: -12 vs (12,-12) ✓; at 199: 4 vs
# (2,-2): MISMATCH! pair at 199 = (2,-2), ap(E)=4. NOT a member!
# So this curve is a false positive (matched 7 filters of 11). The full
# 11-prime match wasn't enforced (only 7 in find_pair4). Re-check with all:
targets = {23:4, 31:8, 47:8, 79:10, 103:10, 151:12, 191:18, 199:2, 223:26, 239:2, 241:30}
got = {23:-4, 31:8, 47:8, 79:10, 103:-10, 151:-12, 191:-18, 199:4, 223:24, 239:12, 241:18}
ok = all(abs(got[p]) == targets[p] for p in targets)
print("abs-match all 11?", ok)
mism = [p for p in targets if got[p] != targets[p] and got[p] != -targets[p]]
print("primes where |ap| mismatches:", mism)
# 223: |24| vs 26 — mismatch! 239: 12 vs 2 — mismatch! 241: 18 vs 30 — mismatch.
# So A=2178,B=225 is NOT the pair member. The search continues with all 11 filters.
print("continue search with the full 11-prime filter (background).")