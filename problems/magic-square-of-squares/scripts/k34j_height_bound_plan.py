#!/usr/bin/env python3
# HEIGHT BOUND on Z_D : V^2 = w^8 - 4w^6 - 604w^4 - 952w^2 + 56644  (genus 3)
# Effective-Chabauty input: with rank Jac(Z_D) = 1 < 3 now UNCONDITIONAL (§2aj),
# the closure of Z_D(Q) to the known degenerate orbit needs:
#   #Z_D(Q) <= #Z_D(F_p) + 2g - 2 + #MW-residue-spare   (Coleman bound), and
#   a HEIGHT BOUND: any point outside a finite enumerated set has canonical
#   height > H0 — then Coleman + Mumford/Mestre reduction closes.
# Standard effective route (Flynn–Smart / Coleman-gross): canonical height
# h(P) >= (1/(2g+2)) * (log |disc| - c) style bound via bad-prime reduction
# analysis. For the gate we need: an explicit H0 such that any Z_D(Q) point
# with |w| > H0 reduces to the known set mod enough primes.
# THIS SCRIPT: step 1 — the Mumford–David bounding constants on the
# Jacobian; step 2 (separate script): Coleman at p=11,13 (tight primes
# from §2ae, #C3_A(F_p) = 8) — the height bound consumes the §2ae data.
# Plan (documented, exact):
#  1. Compute the global minimal model invariants of Z_D (bad primes {2,3,7,17,271}).
#  2. Silverman height machinery: h(P) >= (1/12g) log |Disc| - C (Faltings
#     delta) — the effective constants via local height decompositions at
#     the bad primes (each P-adic reduction type: compute with Sage's
#     hyperelliptic local data).
#  3. The output: explicit H0 such that #\{P in Z_D(Q): h(P) <= H0\} is
#     enumerable; combined with the mod-p sieve kills (§2o) => closure.
print("Height-bound plan set; computing invariants + local height data next.")