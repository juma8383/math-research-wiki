#!/usr/bin/env python3
"""
Verify the birational equivalence  x^3 + y^3 = N  <->  Y^2 = X^3 - 432*N^2
and locate the Mordell-curve points for the gap-1 near-misses.
Map (one common form):  X = 12N/(x+y),  Y = 36N(x-y)/(x+y).
Check both directions and the constant 432.
"""
from fractions import Fraction as F

def mordell_map(x, y, N):
    s = x + y
    X = F(12 * N, s)
    Y = F(36 * N * (x - y), s)
    return X, Y

def check_on_curve(X, Y, N, const):
    lhs = Y * Y
    rhs = X * X * X - F(const * N * N)
    return lhs == rhs

# Test the constant: try 432 and -432 and a few candidates on the Ramanujan point.
N = 1729
for (x, y) in [(1, 12), (9, 10)]:
    X, Y = mordell_map(x, y, N)
    print(f"(x,y)=({x},{y}), N={N}  ->  X={X}, Y={Y}")
    for const in [432, -432, 108, -108, 432*8]:
        ok = check_on_curve(X, Y, N, const)
        if ok:
            print(f"   on curve Y^2 = X^3 - {const}*N^2  ✓  (const={const})")

print("\n--- brute search for the right Mordell curve constant ---")
# For (9,10) N=1729, compute X^3 - Y^2 and see what * N^2 it is.
X, Y = mordell_map(9, 10, 1729)
diff = X*X*X - Y*Y
print(f"X^3 - Y^2 = {diff}   (as fraction)")
print(f"N^2 = {1729**2},  (X^3-Y^2)/N^2 = {diff / F(1729*1729)}")

print("\n--- verify gap-1 near-miss points map to a common Mordell family ---")
# Each near-miss x^3+y^3 = z^3 + 1  ->  N = z^3 + 1, point from (x,y).
near_misses = [
    (9, 10, 12),   # 9^3+10^3 = 1729 = 12^3+1
    (6, 8, 9),     # 6^3+8^3 = 728 = 9^3-1  (here N = 9^3-1)
]
for x, y, z in near_misses:
    for ksign, k in [(1, 1), (-1, -1)]:
        N = z**3 + k
        if x**3 + y**3 == N:
            X, Y = mordell_map(x, y, N)
            const_found = (X*X*X - Y*Y) / F(N*N)
            print(f"  {x}^3+{y}^3={N}={z}^3{'+'+str(k) if k>0 else k}  ->  X={X}, Y={Y},  const=(X^3-Y^2)/N^2={const_found}")