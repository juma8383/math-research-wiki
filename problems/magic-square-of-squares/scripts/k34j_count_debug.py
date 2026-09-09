#!/usr/bin/env python3
# Debug point-counting exactly (the gp version had a formula bug).
def pow_set(p):
    return {k*k % p for k in range(p)}

def count(f, p):
    PS = pow_set(p)
    cnt = 1
    chi = 0
    for x in range(p):
        v = f(x, p) % p
        if v == 0: cnt += 1
        elif v in PS: cnt += 2; chi += 1
        else: chi += -1
    return cnt, chi

# C1: y^2 = 8x^4+1016x^2+9
fC1 = lambda x: 8*pow(x,4,p if False else 0) if False else None
def fC1(x, p): return 8*pow(x,4,p) + 1016*pow(x,2,p) + 9
def fD(x, p): return pow(x,4,p) - 4*pow(x,3,p) - 604*pow(x,2,p) - 952*x + 56644
def fJL(x, p): return (x*x*x - 27894240*x + 56491485696) % p

print("p | #C1 | ap(Jac C1)=p+1-#C1 | ap(JL) | match")
for p in (5, 7, 11, 13, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71):
    c1, _ = count(fC1, p)
    c2, _ = count(fJL, p)
    print(f"{p:>3} | {c1:>4} | ap_C1={p+1-c1:>3} | ap_JL={p+1-c2:>3} | {p+1-c1 == p+1-c2}")