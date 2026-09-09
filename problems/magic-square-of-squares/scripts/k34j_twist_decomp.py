print("E(K) rank: use simon_two_descent signature + point search; ALSO the KEY")
print("structure: E over K = Q(sqrt(238)) is the base change of the SAME E over Q")
print("(the coefficients are rational!), so E(K) rank = rank E(Q) + rank E^238(Q)")
print("where E^238 = the 238-quadratic twist of E over Q.")
print("Both are ordinary Q-elliptic curves -> mwrank handles them exactly!")
from sage.all import *
E = EllipticCurve([0, 32, 0, 238, 0])
print("E/Q rank:", E.rank())
Etw = E.quadratic_twist(238)
print("E^238:", Etw)
print("E^238 rank:", Etw.rank())
print("=> rank E(K) = rank E(Q) + rank E^238(Q) =", E.rank(), "+", Etw.rank(),
      "=", E.rank() + Etw.rank())