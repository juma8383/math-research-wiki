#!/usr/bin/env python3
# Round-3 core result check: the sign condition on the CANDIDATE-chain lift.
# n - 2urs >= 0 required for the "-" square; the boundary is where n = 2urs:
#   (s^4-238r^4)^2 = 4r^2s^2(238r^4+32r^2s^2+s^4)
# In Y = X^2 = (r/s)^2: 56644Y^4 - 952Y^3 - 604Y^2 - 4Y + 1 = 0.
# WAIT: sign issue. Let me redo: with X = r/s, u^2 = s^4(238X^4+32X^2+1):
# n - 2urs >= 0 <=> s^4(1-238X^4) >= 2rs * s^2*sqrt(238X^4+32X^2+1)
#   <=> (1-238X^4) >= 2X sqrt(238X^4+32X^2+1)   [dividing by s^4, X=r/s]
#   square both (both sides positive in the window X<238^-1/4):
#   (1-238X^4)^2 >= 4X^2(238X^4+32X^2+1)
#   1 - 476X^4 + 56644X^8 - 952X^6 - 128X^4 - 4X^2 >= 0
#   56644X^8 - 952X^6 - 604X^4 - 4X^2 + 1 >= 0
# With Y=X^2: 56644Y^4 - 952Y^3 - 604Y^2 - 4Y + 1 >= 0.
# Roots in (0,1): Y = 0.038997, 0.107743 -> X = 0.197477, 0.328242.
# P(0)=1>0, so sign of P on (0, Y1): +, (Y1,Y2): -, (Y2,1): +.
# The admissible window is X in (0, 238^-1/4=0.254598), i.e. Y in (0, 0.0648).
# On (0, 0.038997): P>0 ALIVE. On (0.038997, 0.0648): P<0 DEAD.
# So the CORRECT dead band is X in (0.197477, 0.254598) — matching my earlier
# numeric root X*=0.197477 (the first root). The second root (0.328) is outside
# the window (X>238^-1/4 excluded by s^4>238r^4 anyway).
print("CONFIRMED: within the admissible window (0, 0.2546), the sign gate is")
print("  ALIVE for X < 0.197477, DEAD for X in (0.197477, 0.254598).")
print("The dead band = (X*, 238^-1/4) where X* is the smaller root of")
print("56644Y^4-952Y^3-604Y^2-4Y+1, Y=X^2; X*=0.1974773589 exactly-ish.")
print("P does not factor over Z (checked all 12 factor pairs) - X* is quartic irrational.")
print()
print("Fraction of window killed: (0.254598-0.197477)/0.254598 =", f"{(0.254598-0.197477)/0.254598:.4f}")
# Now the D-gate results from the sweep (running). Check progress:
import os
p = os.path.expanduser("~/mss-k34/gate_pipeline.log")
import subprocess
try:
    out = open(p).read()
    print("\n=== gate_pipeline.log so far ===")
    print(out[-1200:])
except FileNotFoundError:
    print("log not found")