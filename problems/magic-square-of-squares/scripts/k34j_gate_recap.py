#!/usr/bin/env python3
# While the analytic rank runs: sanity-check the rank expectation.
# rank Jac(P) = rank E(K), K = Q(sqrt(238)).
# The wiki's [mss-k34-descent] leaf-layer data: the leaf fiber points (2,3,71)-type
# and the layer-1 solutions give elements of Jac(P)(Q)... actually of Jac(D) etc.
# Empirical expectation: P(Q) = {(0,0)} only (searched to p<=3000, q<=40) —
# very few points, but Jac(P) rank can still be positive (Jac points ≠ P points).
# The analytic rank sum slope will discriminate rank 0/1/2 within the loglog range.
# ALSO: parity check — the root number of Jac(P): for rank parity. The
# functional equation sign: W(Jac(P)) = prod W_local. If W = +1: rank even (0, 2);
# if -1: rank odd (1, 3, ...). For the gate rank <= 1: W=+1 with rank 0 is the
# BEST case; W=-1 with rank 1 also passes (rank Jac(Z_D) = 2 < 3 still Chabauty!).
# Actually rank Jac(Z_D) = 1 + rank Jac(P) <= 2 < 3 works for BOTH rank 0 and 1!
# The gate fails only if rank Jac(P) >= 2, i.e. rank E(K) >= 2.
print("Gate recap: rank Jac(Z_D) = 1 + rank Jac(P) = 1 + rank E(Q(sqrt(238))).")
print("Chabauty applies iff rank Jac(Z_D) < 3, i.e. rank E(K) <= 1.")
print("The analytic rank sum will show the slope within ~loglog(5000) = 2.2 —")
print("enough to distinguish rank 0/1 (slope <= ~1-2) from rank 2+ (slope >= 2).")