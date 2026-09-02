#!/usr/bin/env python
# Part 7: local sieve on the genus-3 square covers.
# C3_A: W^2 = x^8+132x^6-250x^4+132x^2+1     (X = x^2 must be a rational square)
# C3_B: W^2 = 9x^8-92x^6+310x^4-92x^2+9
# For each prime p: find residue classes r mod p with a solution W.
# Classes {0, +1, -1} are always solutions (degenerate). If for some p the ONLY
# solution classes are 0,+-1 (and p small enough that these are distinct), then
# any rational solution has x = a/b with p | a or p | (a+-b) ... i.e.
# p | a*(a-b)*(a+b) (for the C3_A/B curves x=a/b).
# Collect many such "killing primes" and the resulting constraint set.
import sys
def out(*a): print(*a); sys.stdout.flush()

def sqres(p):
    s = {0}
    for i in range(1, p):
        s.add(i*i % p)
    return s

def good_classes(fcoeffs, p):
    # fcoeffs: list c_i for x^(2i) (palindromic in x^2), i=0..4
    # returns set of r mod p with f(r) a square (including r=0,+-1 if square)
    S = sqres(p)
    good = set()
    for r in range(p):
        r2 = r*r % p
        v = 0
        for c in fcoeffs[::-1]:
            v = (v*r2 + c) % p
        if v in S: good.add(r)
    return good

killA = []; killB = []
resA = {}; resB = {}
for p in range(3, 400):
    gA = good_classes([1, 132, -250, 132, 1], p)
    gB = good_classes([9, -92, 310, -92, 9], p)
    deg = {0, 1, p-1}
    resA[p] = len(gA); resB[p] = len(gB)
    if gA <= deg: killA.append(p)
    if gB <= deg: killB.append(p)
out("C3_A killing primes (<400):", killA)
out("C3_B killing primes (<400):", killB)
# class counts for small primes (diagnostic)
out("p: #goodA #goodB (degenerate=3 for p>3)")
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
    out(" ", p, resA[p], resB[p])